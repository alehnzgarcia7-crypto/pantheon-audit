# SLSA Levels Specification

Supply chain Levels for Software Artifacts. Google-originated, OpenSSF-maintained framework.

## SLSA Level 0: No guarantees
- No build process documented or hermetic
- No provenance
- No signing
- Manual builds acceptable

## SLSA Level 1: Documented build
- Build process scripted (CI/CD config in repo)
- Provenance generated (build environment captured)
- Provenance not signed, can be falsified
- Acceptable for low-stakes internal tools

## SLSA Level 2: Hosted build, signed provenance
- Builds run on hosted service (GitHub Actions, GitLab CI, GCP Cloud Build, AWS CodeBuild)
- Provenance signed by build service
- Provenance includes: source location, build inputs, build steps, build environment
- Tampering detectable
- Minimum bar for production software in 2026

## SLSA Level 3: Hardened builds
- Source and build hermetic (no internet access during build)
- Builds isolated (no concurrent jobs sharing state)
- Provenance non-falsifiable by builder
- Source repo enforces 2-person review
- Builds reproducible
- Bar for security-sensitive software (cryptography, auth)

## SLSA Level 4: Highest assurance (proposed)
- Two-person review of build process changes
- Formal verification of critical components
- Reproducible builds verified by independent rebuilds
- Mandatory for life-safety, defense

## Required components for SLSA L2+

### Build provenance
in-toto attestation format, signed:
```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{"name": "myapp", "digest": {"sha256": "..."}}],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {...},
    "runDetails": {...}
  }
}
```

### Signing
Sigstore cosign for keyless signing via OIDC.

### Verification
Consumers verify before deploying:
```bash
cosign verify --certificate-identity=... --certificate-oidc-issuer=... myimage:tag
```

## Common audit findings
- No build provenance: Critical (cannot verify what was built)
- Builds not hermetic: High (build can inject malware)
- No signing: High (artifacts can be swapped)
- Single point of failure (one CI account): High
- Vulnerable dependencies unmonitored: Critical
- Single-maintainer critical deps: High

## References
- SLSA spec: slsa.dev
- in-toto: in-toto.io
- Sigstore: sigstore.dev
- OpenSSF Best Practices: openssf.org

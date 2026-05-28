# PANTHEON Ethics and Responsible Use

PANTHEON is a security research tool. Misuse can cause real harm to systems, users, and organizations.

## Authorized use only

You may use PANTHEON to audit:
1. Systems you own
2. Systems you have explicit written authorization to audit (penetration testing contract, internal security review charter, bug bounty program scope, employer assignment within job responsibilities)

You may NOT use PANTHEON to:
- Audit third-party systems without authorization
- Conduct unauthorized vulnerability assessments
- Facilitate access to systems you do not have permission to access
- Aggregate findings about third parties for sale or publication

## Responsible disclosure

If you discover vulnerabilities in third-party systems through any means:
1. Verify scope of testing authorization
2. Report to vendor through responsible disclosure process
3. Allow reasonable remediation time (typically 90 days, longer for complex fixes)
4. Coordinate public disclosure with vendor when appropriate
5. Do not exploit vulnerabilities beyond proof-of-concept needed for verification

## Data handling during audits

When PANTHEON discovers sensitive data exposure during authorized audit:
1. Document existence and scope without retaining copies
2. Do not exfiltrate beyond minimum needed to prove finding
3. Securely delete temporary copies
4. Report through agreed channel
5. Do not use sensitive data for any other purpose

## Specific prohibitions

PANTHEON may not be used to:
- Develop offensive cyber capabilities for unauthorized targets
- Create attack tooling for criminal use
- Train AI models for unauthorized vulnerability discovery
- Generate exploitation content for sale on dark markets
- Conduct surveillance of individuals without legal authorization

## Reporting suspected misuse

If you observe PANTHEON being used outside authorized contexts, contact maintainer Alex (@nexogeopo) directly. Reports confidential.

## Disclaimer

PANTHEON is provided AS-IS under MIT license. Maintainer makes no warranty of completeness, accuracy, or fitness for any particular purpose. Users are solely responsible for ensuring authorized use, legal compliance with applicable jurisdictions, and appropriate handling of audit findings.

PANTHEON output should be treated as AI-augmented audit infrastructure, not as a substitute for human-led tier-S security audit. Findings should be reviewed by qualified security professionals before action.

## Jurisdictions

Different jurisdictions have different rules for security research:
- US: Computer Fraud and Abuse Act (CFAA), DMCA Section 1201
- EU: NIS2 Directive, CRA, GDPR (for PII handling during research)
- Mexico: Código Penal Federal articles related to unauthorized access
- UK: Computer Misuse Act 1990

When in doubt, consult legal counsel before conducting security research on systems you do not fully own.

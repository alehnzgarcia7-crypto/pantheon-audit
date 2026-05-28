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

## Cloud-sync and audit-output handling (PANTHEON-0014 mitigation)

PANTHEON output is sensitive multi-party data. The `.pantheon/` workspace tree and the `~/Downloads/pantheon-audit-<uuid>/` deliverables directory both contain step-by-step exploitation guidance for the audit subject until remediation ships. They also contain finding bodies that may reference third-party assets (vendor libraries, customer integrations, regulated personal data identifiers).

Default rules:

1. Do not commit `.pantheon/` to version control. The PANTHEON scaffolding script auto-appends `.pantheon/` to a local `.gitignore`. Do not undo that.
2. Do not store `~/Downloads/pantheon-audit-<uuid>/` in cloud-sync backends (iCloud, Google Drive, OneDrive, Dropbox, Box, etc.). Exclude both directories at the OS sync agent level. See `docs/installation.md` for OS-specific procedure.
3. If the audit subject is a multi-party system (your code plus a vendor plus a customer), notify affected parties before sharing PANTHEON output that touches their assets, even with the auditor's own legal counsel.
4. When transmitting findings to vendors during responsible disclosure, encrypt the payload (age, PGP, or SOPS) and use a channel both parties trust. Email attachments traverse multiple party infrastructures and are inappropriate for raw exploitation guidance.
5. When discarding finished audit bundles, delete with `srm -v` (macOS) or `shred -uvz` (Linux) on the deliverables tarball rather than `rm`. Filesystem semantics make plain `rm` non-destructive for journaled filesystems on SSDs.

If a leak occurs (cloud sync surfaced findings to an unauthorized party, deliverables emailed to wrong recipient, etc.), invoke your organization's incident response process and notify the audit subject within 72 hours per the GDPR Art. 33 / LFPDPPP Art. 40 standard, even if those regimes do not strictly apply.

## Jurisdictions

Different jurisdictions have different rules for security research:
- US: Computer Fraud and Abuse Act (CFAA), DMCA Section 1201
- EU: NIS2 Directive, CRA, GDPR (for PII handling during research)
- Mexico: Código Penal Federal articles related to unauthorized access
- UK: Computer Misuse Act 1990

When in doubt, consult legal counsel before conducting security research on systems you do not fully own.

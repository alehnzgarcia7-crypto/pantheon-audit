# Proof-of-Concept Repository
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}

## Purpose
Sanitized proof-of-concept exploits and reproduction notes for every accepted Critical and High finding. Audience: engineering remediators, validators reproducing findings, future regression tests.

## Populated from state
| Field | Source |
|---|---|
| accepted_findings_critical_high | state.json/findings filtered severity in (Critical, High), status accepted |
| pocs_per_finding | state.json/findings/[id]/poc |

## Executive Summary
Count of PoCs by severity. Reproduction reliability metric.

## Per-PoC entries
For each Critical or High finding:
- PANTHEON-NNNN id and title
- Affected component, version, commit
- Setup instructions (containerized where possible)
- Reproduction steps
- Expected output demonstrating the vulnerability
- Sanitization notes (what was redacted to protect customer data)
- Regression test template (for after fix)
- Disclosure status (private, coordinated disclosure, public)

## Ethics and safety
- PoCs are NOT runnable against production.
- PoCs that demonstrate working exploits MUST be defanged (replaced sensitive payloads with placeholders).
- PoCs MUST NOT exfiltrate real customer data.

## Reproducibility
- Each PoC includes container or VM specification.
- Each PoC includes random seeds where applicable.
- Each PoC documents environmental dependencies.

## Compliance mappings cited
ISO 19011 audit evidence, AICPA SSAE 18 evidence sufficiency, ENISA Good Practices for Disclosing Vulnerabilities.

## Hard fails (validation rules)
- Every Critical or High accepted finding has at least one PoC OR explicit not-reproducible note with reasoning.
- Every PoC is sanitized (no real PII, no real keys).
- No em-dashes.

## Signoff
Prepared by: trail-of-bits-auditor + bishop-fox-red-team + cure53-web-app
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- ENISA Good Practices for Disclosing Vulnerabilities
- ISO 30111 vulnerability handling

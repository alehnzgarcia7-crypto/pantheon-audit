# OWASP ASVS Level 3 Checklist
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Standard**: OWASP ASVS v5.0 (Level 3)

## Purpose
Coverage assessment against OWASP Application Security Verification Standard v5.0 at Level 3 (the highest assurance level), the standard for systems processing high-value data such as financial, health, or government workloads. Audience: engineering, security engineering, third-party validators.

## Populated from state
| Field | Source |
|---|---|
| asvs_chapters | state.json/phases/3/asvs_chapters |
| controls_total | sum of all controls applicable |
| controls_met | controls verified met |
| controls_partial | controls partially met |
| controls_not_met | controls failed |
| controls_na | controls not applicable |
| controls_with_findings | controls that triggered PANTHEON-NNNN findings |

## Executive Summary
Compliance posture. Coverage by chapter. Mandatory controls met percentage.

## ASVS v5.0 chapters
Per chapter (V1 Architecture, V2 Authentication, V3 Session Management, V4 Access Control, V5 Validation Sanitization Encoding, V6 Stored Cryptography, V7 Error Handling Logging, V8 Data Protection, V9 Communication, V10 Malicious Code, V11 Business Logic, V12 Files and Resources, V13 API Web Service, V14 Configuration):
- Total controls at L3
- Met
- Partial
- Not met
- N/A
- Findings PANTHEON-NNNN tied to gaps

## Coverage by chapter
Markdown table with chapter, total controls, met, partial, not met, coverage percentage.

## Gap analysis
Per gap (control not met or partial):
- Control ID and statement
- Reason for gap (code path, missing implementation, weak implementation)
- PANTHEON-NNNN finding ID
- Remediation effort
- Priority

## Compliance mappings cited
PCI-DSS v4 maps to ASVS V5 V6 V8 V9. SOC 2 Trust Services to ASVS broadly. GDPR Art. 32 to ASVS V8 V9 V6.

## Hard fails (validation rules)
- All 14 chapters present.
- Each chapter shows percentage coverage.
- Every gap MUST link to a PANTHEON-NNNN finding.
- No em-dashes.

## Signoff
Prepared by: trail-of-bits-auditor + ncc-group-auditor + cure53-web-app
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-asvs-l3-audit/references/asvs-v5-l3-checklist.md

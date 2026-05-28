---
name: pantheon-finding-format
description: Strict finding format spec. All PANTHEON findings must conform to PANTHEON-NNNN format with mandatory fields including severity matrix, CVSS v4 vector, exploitation difficulty, business impact USD, threat actor mapping T1-T8, affected code citations path:line, exploitation scenario, recommendations short and long-term, compliance mappings to 18 frameworks, adversarial gate verdict. Activates when any persona outputs finding or /pantheon:finding runs.
---

# PANTHEON Finding Format Specification

## Mandatory fields
1. ID: PANTHEON-NNNN
2. Title: max 80 chars
3. Severity: Critical/High/Medium/Low/Informational
4. CVSS v4.0 vector + score
5. Exploitation difficulty: Low/Medium/High
6. Business impact USD with reasoning
7. Threat actors capable: array T1-T8
8. Affected files: path:LINE-LINE
9. First introduced commit SHA
10. Description: 2-4 paragraphs technical
11. Exploitation scenario: step-by-step concrete
12. Recommendation short-term and long-term
13. Compliance mappings: all 18 frameworks (null where N/A)
14. Adversarial gate result with verdict, confidence, PoC verified
15. Cross-verified by personas
16. References: CWE, OWASP, RFC, regulation, papers
17. Status: draft/adversarial-review/accepted/disputed/withdrawn

## References
- `references/tob-format-spec.md`
- `references/cvss-v4-vector-builder.md`
- `references/exploitation-difficulty-rubric.md`

## Hard rules
1. All mandatory fields present
2. CVSS v4.0 validates against spec
3. file:line exact
4. No em-dashes

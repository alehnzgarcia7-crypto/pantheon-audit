---
name: pantheon-compliance-mapper
description: "Compliance framework mapping skill. Maps every accepted finding to 18 frameworks: CWE, OWASP Top 10 2021, OWASP API Top 10 2023, OWASP ASVS 5.0, CNBV CUF/CUIFPEs, LFPDPPP 2025, SAT CFF, GDPR, PCI-DSS 4.0.1, HIPAA Security Rule, SOC 2 TSC, ISO 27001 Annex A, ISO 27017, ISO 27018, ISO 27701, NIST 800-53 Rev 5, MITRE ATT&CK, CAPEC. Auto-activates after every adversarial gate ACCEPT verdict."
---

# PANTHEON Compliance Mapper Skill

## Workflow
1. Receive finding category, component type, geographic scope, industry from orchestrator
2. Read 18-frameworks-catalog.md for current article numbers
3. For each of 18 frameworks: determine applicability and primary/secondary article refs
4. Output structured JSON for finding metadata

## References
- `references/18-frameworks-catalog.md`

## Hard rules
1. All 18 frameworks evaluated (null where N/A)
2. Article-level citations
3. mapping_confidence honestly estimated
4. No fabricated citations
5. No em-dashes

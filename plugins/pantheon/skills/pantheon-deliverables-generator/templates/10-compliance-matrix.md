# Compliance Matrix (18 frameworks stacked)
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Mapped by**: compliance-mapper

## Purpose
Article-level compliance mapping of every accepted finding to 18 frameworks. Audience: legal counsel, compliance officers, internal audit, external auditors, regulators.

## Populated from state
| Field | Source |
|---|---|
| findings | state.json/findings filtered status accepted |
| framework_coverage | state.json/phases/9/framework_coverage |
| provenance_per_citation | state.json/phases/9/citation_provenance |
| jurisdiction_determination | state.json/sow/jurisdictions |

## Executive Summary
Compliance coverage per framework. Gaps highlighted by severity.

## Per-Framework Sections
For each of 18 frameworks (OWASP ASVS v5 L3, OWASP API Top 10 2023, CWE, MITRE ATT&CK Enterprise v15, NIST CSF 2.0, NIST SP 800-53 r5, ISO 27001:2022, ISO 27017, ISO 27018, SOC 2 Trust Services, PCI DSS v4, HIPAA Security Rule, GDPR, LFPDPPP 2025, CNBV CUF + CUIFPEs 2026, DORA, NIS2, EU CRA):

### Framework Name
- Total requirements applicable: N
- Met: N
- Partially met: N
- Not met: N
- Not applicable: N
- Coverage percentage: X%
- Critical gaps (findings): list of PANTHEON-NNNN
- Remediation priority: P0 / P1 / P2

## Cross-Framework Mapping
Findings table with all 18 framework citations per finding. Confidence column included.

## Regulatory Filing Readiness
Per applicable regulator:
- CNBV (Mexico): documentation readiness, key gaps
- LFPDPPP 2025 (Mexico): privacy compliance readiness
- GDPR (EU): readiness, key gaps
- PCI-DSS: readiness if cardholder data
- HIPAA: readiness if PHI
- SOC 2: readiness for attestation
- DORA: readiness for register of information

## Provenance Chain per citation
For every citation, the catalog version, source article paragraph, and mapping_confidence.

## Audit Trail
Evidence locations for each compliance claim.

## Compliance mappings cited
This deliverable IS the compliance citation. Cross-references to 18-frameworks-catalog.md.

## Hard fails (validation rules)
- All 18 frameworks rendered with totals.
- Mapping_confidence below 0.7 MUST surface in mapping_notes.
- Every finding cites at least one framework or explicitly states none-applicable.
- No em-dashes.

## Signoff
Prepared by: compliance-mapper
Reviewed by: Adversarial Judge
Mapped by: compliance-mapper (self)

## References
- plugins/pantheon/skills/pantheon-compliance-mapper/references/18-frameworks-catalog.md

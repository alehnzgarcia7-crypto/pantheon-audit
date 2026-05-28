# EU Cyber Resilience Act (CRA) Conformity Evidence Pack

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11  
**Baseline reference**: EU Regulation 2024/2847; vulnerability reporting effective September 11, 2026; full applicability December 11, 2027

## Purpose
For any "product with digital elements" placed on EU market, this pack is the conformity evidence required for CE marking.

## Product identification
| Field | Value |
|---|---|
| Product name | <name> |
| Version | <semver> |
| Manufacturer (or open-source steward per Article 25) | <entity> |
| Product class | <Class I / Class II / Important / Critical> |
| CE marking applied | <yes/no, date> |

## Essential cybersecurity requirements (Annex I)
| Requirement | Implementation | Evidence |
|---|---|---|
| Secure by design | <text> | <link> |
| Risk-based security level | <text> | <link> |
| Vulnerability handling | <text> | <link> |
| Secure default configuration | <text> | <link> |
| Protection from unauthorised access | <text> | <link> |
| Confidentiality (encryption) | <text> | <link> |
| Integrity (signing, checksums) | <text> | <link> |
| Process and store only necessary data | <text> | <link> |
| Resilience and availability | <text> | <link> |
| Minimise attack surface | <text> | <link> |
| Mitigate exploitation impact | <text> | <link> |
| Security information sharing | <text> | <link> |
| Updates and patching | <text> | <link> |
| Authentication and identity | <text> | <link> |

## Vulnerability reporting workflow (effective September 11, 2026)
- [ ] ENISA Single Reporting Platform credentials provisioned
- [ ] 24-hour initial report workflow tested
- [ ] 72-hour follow-up workflow tested
- [ ] 14-day or 1-month final report workflow tested
- [ ] Disclosure policy published per Article 13

## SBOM (machine-readable, mandatory)
- Format: <CycloneDX 1.6+ / SPDX 3.0>
- Includes CBOM (PQC migration tracking)?: <yes/no>
- Generation toolchain: <Syft/Trivy/CycloneDX-CLI>
- Refresh cadence: <per release>

## Conformity Assessment
- Conformity Assessment Body involvement?: <yes (CAB ID) / self-declaration>
- CAB rules effective June 11, 2026

## Open Source Steward (Article 25, if applicable)
- Steward entity: <Eclipse Foundation, etc.>
- Steward obligations distinct from manufacturer: documented per Open Regulatory Compliance WG

## Findings
| Finding ID | Title | Severity |
|---|---|---|
| PANTHEON-<NNNN> | <title> | <severity> |

## Hard fails (audit auto-fail)
- [ ] No SBOM in machine-readable format
- [ ] No vulnerability disclosure workflow tested
- [ ] CE marking applied without conformity evidence
- [ ] Penalty exposure: greater of 15 million euros or 2.5% global turnover

## Signoff
- compliance-mapper persona
- Date: <ISO-8601>

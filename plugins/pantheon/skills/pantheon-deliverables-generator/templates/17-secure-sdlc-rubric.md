# Secure SDLC Rubric
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Standard**: NIST SP 800-218 SSDF + OWASP SAMM 2 + BSIMM 14

## Purpose
SDLC maturity rubric across the development lifecycle (requirements, design, build, test, release, operate). Audience: engineering leadership, security engineering, internal audit, M&A diligence.

## Populated from state
| Field | Source |
|---|---|
| sdlc_practices | state.json/phases/8/sdlc_observations |
| ci_cd_observations | state.json/phases/6/ci_cd |
| code_review_observations | state.json/phases/8/code_review |
| testing_observations | state.json/phases/8/testing |

## Executive Summary
Overall SDLC maturity rating. Top 3 gaps.

## SSDF practice areas
For each SSDF practice (PO, PS, PW, RV):
- Tasks applicable
- Implementation status: Implemented, Partial, Missing
- Evidence (artifacts, code, runbooks)
- Findings PANTHEON-NNNN tied

## SAMM 2 business functions
For each (Governance, Design, Implementation, Verification, Operations):
- Maturity level (1 to 3) per security practice
- Evidence
- Gap to next level

## BSIMM observations (descriptive, not normative)
Observed activities mapped to BSIMM domains.

## Toolchain observations
SAST, DAST, SCA, IAST, fuzzing, secret scanning, IaC scanning. Coverage and effectiveness.

## Code review and approval
Two-person review enforcement, security-sensitive area annotations, merge gates.

## Release and change management
Release governance, change advisory, post-release monitoring.

## Compliance mappings cited
NIST SP 800-218 SSDF, OWASP SAMM 2, BSIMM 14, ISO 27001 A.14 system acquisition and development, NIS2 Art. 21(2)(d) SDLC.

## Hard fails (validation rules)
- All four SSDF practice areas rated.
- All five SAMM business functions rated.
- Toolchain observation includes SAST and SCA at minimum.
- No em-dashes.

## Signoff
Prepared by: mudge-holistic + latacora-pragmatic
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- NIST SP 800-218 v1.1
- OWASP SAMM 2.0
- BSIMM 14

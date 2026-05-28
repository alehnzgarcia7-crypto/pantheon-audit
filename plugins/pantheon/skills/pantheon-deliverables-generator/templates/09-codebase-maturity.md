# Codebase Maturity Scorecard
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Lead persona**: mudge-holistic

## Purpose
13-dimension maturity scorecard with evidence and improvement roadmap. Audience: engineering leadership, executive sponsors, M&A diligence.

## Populated from state
| Field | Source |
|---|---|
| dimensions | state.json/phases/8/dimensions |
| evidence_per_dimension | state.json/phases/8/evidence |
| aggregate_score | state.json/phases/8/maturity_aggregate |
| launch_readiness | state.json/phases/8/launch_readiness |

## Executive Summary
Overall maturity: X/13 dimensions at Satisfactory+. Launch readiness assessment.

## 13 Dimensions
For each dimension:
- Dimension name
- Rating: Strong / Satisfactory / Moderate / Weak / Missing
- Evidence (file:line citations or absence)
- Improvement priority: P0 / P1 / P2 / P3
- Effort to reach next level

Dimensions: Arithmetic and numeric precision, Cryptography, Data handling, Memory safety, Error handling and logging, Authentication and identity, Access control and authorization, Configuration and secrets, API surface security, Dependency hygiene, Threat intelligence integration, Testing and verification, Documentation and runbooks.

## Aggregate Score
- Strong: X/13
- Satisfactory: X/13
- Moderate: X/13
- Weak: X/13
- Missing: X/13

Aggregate at Satisfactory+: X/13.

## Launch Readiness Recommendation
Based on aggregate:
- 13/13 Strong: ELITE
- 9 to 13 Satisfactory+: PRODUCTION-READY
- 7 to 8 Satisfactory+: CONDITIONAL
- under 7: NOT READY

## Improvement Roadmap
Per dimension below Satisfactory: specific actions, effort, priority.

## Compliance mappings cited
NIST CSF 2.0 Protect category, ISO 27001 A.8 A.12 A.14, NIS2 Art. 21(2), CIS Controls v8.

## Hard fails (validation rules)
- All 13 dimensions rated.
- Each dimension has at least one evidence citation or explicit absence note.
- Aggregate score reconciles with per-dimension ratings.
- No em-dashes.

## Signoff
Prepared by: mudge-holistic
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-codebase-maturity/references/13-dimensions-rubric.md

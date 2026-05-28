# Strategic Threat Model
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Methodology**: PASTA + STRIDE-per-element + LINDDUN

## Purpose
Strategic threat model combining PASTA seven stages, STRIDE per architectural element, and LINDDUN for privacy-sensitive elements. Audience: security architects, engineering leads, regulator preparers.

## Populated from state
| Field | Source |
|---|---|
| asset_inventory | state.json/phases/1/asset_inventory |
| dfd_level_1 | state.json/phases/2/dfd_level_1 |
| trust_boundaries | state.json/phases/2/trust_boundaries |
| threat_actor_relevance | state.json/phases/2/threat_actor_relevance |
| stride_per_element | state.json/phases/2/stride_per_element |
| linddun_per_element | state.json/phases/2/linddun_per_element |
| attack_trees | state.json/phases/2/attack_trees |
| risk_register | state.json/phases/2/risk_register |

## Executive Summary
3 to 5 paragraphs. Threat landscape characterization, top 3 risks monetized, mitigation maturity assessment.

## Business Objectives Context
From SoW: business purpose, regulatory scope, SLAs, critical processes.

## Technical Scope
Architecture summary, tech stack, integrations, trust boundaries, deployment.

## Data Flow Diagrams
Level 1 DFD (Mermaid). Trust boundaries marked. Critical data flows highlighted.

## Asset Classification
Four-tier table:
- Tier 1 (money plus life-safety): {{tier1_assets}}
- Tier 2 (PII plus reputation): {{tier2_assets}}
- Tier 3 (operational): {{tier3_assets}}
- Tier 4 (auxiliary): {{tier4_assets}}

## Threat Actor Matrix
T1 to T8 customized for this engagement. Per actor: capability, motivation, resources, patience, typical TTPs, relevance score.

## STRIDE Per Element Analysis
Per major DFD element, STRIDE table with ratings.

## LINDDUN Privacy Analysis
Per PII-processing element, LINDDUN table.

## Attack Trees: Top 10 Threats
Mermaid diagrams for top 10. Per leaf: difficulty, detection probability, mitigation status.

## Risk Register
Monetized table:
| Risk ID | Description | Likelihood | Impact USD | Risk Score | Mitigation Status | Residual |

## Mitigation Roadmap
Prioritized by risk score.

## Assumptions and Limitations

## Compliance mappings cited
GDPR Art. 35 (DPIA), NIST CSF 2.0 Identify, ISO 27001 A.5, NIS2 risk management, CNBV CUF Chapter X.

## Hard fails (validation rules)
- Every Tier 1 asset MUST have STRIDE row.
- Every PII-processing element MUST have LINDDUN row.
- Top 10 attack trees MUST be rendered.
- Risk register MUST monetize impact USD.
- No em-dashes.

## Signoff
Prepared by: mudge-holistic + bishop-fox-red-team
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-threat-model/SKILL.md
- references/pasta-7-stages.md, stride-per-element.md, linddun-privacy.md, attack-tree-patterns.md

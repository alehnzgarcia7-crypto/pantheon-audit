# Recommendations
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Lead persona**: pantheon-orchestrator

## Purpose
Strategic remediation roadmap synthesized across all findings, maturity dimensions, and compliance gaps. Audience: engineering leadership, security engineering, executive sponsors.

## Populated from state
| Field | Source |
|---|---|
| findings_open | state.json/findings filtered status accepted |
| top_strategic_risks | state.json/phases/2/top_risks |
| maturity_gaps | state.json/phases/8/dimensions where rating below Satisfactory |
| compliance_gaps | state.json/phases/9/gaps |

## Executive Summary
Top 5 strategic recommendations with effort, business value, and risk reduction.

## Recommendations by Pillar

### Identity and Access
- Specific recommendations from findings PANTHEON-NNNN
- Effort, owner, priority

### Cryptography
- Specific recommendations
- PQ migration timing
- Effort, owner, priority

### Supply Chain
- SLSA target uplift
- Dependency hygiene
- Effort, owner, priority

### Application Security
- ASVS gap closures
- Effort, owner, priority

### Detection and Response
- SIEM and EDR rule additions
- IR runbook coverage
- Effort, owner, priority

### Architecture
- Trust boundary improvements
- Crisis-response architecture
- Effort, owner, priority

### Compliance
- Per regulator preparation actions
- Effort, owner, priority

## Quick wins (under 2 weeks each)
Numbered list with PANTHEON-NNNN references.

## Strategic initiatives (one quarter or longer)
Numbered list with effort estimates.

## Items explicitly NOT recommended
Risks accepted with rationale.

## Compliance mappings cited
NIST CSF 2.0 Improve category, ISO 27001 A.5 leadership, NIS2 Art. 21 governance.

## Hard fails (validation rules)
- Every recommendation ties to at least one PANTHEON-NNNN finding, maturity dimension, or compliance gap.
- Owner assignment present.
- Effort sizing present.
- No em-dashes.

## Signoff
Prepared by: pantheon-orchestrator
Reviewed by: Adversarial Judge (consistency check)
Mapped by: Compliance Mapper

## References
All deliverables 01 through 35.

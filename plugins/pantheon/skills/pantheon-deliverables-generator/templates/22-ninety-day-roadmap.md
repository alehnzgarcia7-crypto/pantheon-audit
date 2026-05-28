# Ninety-Day Roadmap
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Lead persona**: pantheon-orchestrator

## Purpose
Prioritized 90-day remediation plan with effort sizing. Audience: engineering management, project managers, security leadership.

## Populated from state
| Field | Source |
|---|---|
| findings_open | state.json/findings filtered status accepted |
| effort_estimates | state.json/findings/[id]/effort_estimate |
| maturity_gaps | state.json/phases/8/dimensions where rating below Satisfactory |
| compliance_gaps | state.json/phases/9/gaps |

## Executive Summary
Total effort estimate (person-weeks). Top 3 weeks 1 to 4 priorities.

## Sprint structure
Six 2-week sprints over 90 days.

### Sprint 1 (weeks 1 to 2): Stabilization
- All Critical findings addressed
- Immediate compensating controls deployed
- Effort: X person-weeks
- Owners

### Sprint 2 (weeks 3 to 4): High severity
- Highest-priority High findings remediated
- Top detection gaps closed
- Effort, owners

### Sprint 3 (weeks 5 to 6): Compliance
- Top compliance gaps closed for primary regulator
- Documentation updated
- Effort, owners

### Sprint 4 (weeks 7 to 8): Crypto and supply chain
- Crypto findings remediated
- Dependency advisories resolved
- Effort, owners

### Sprint 5 (weeks 9 to 10): Codebase maturity
- Lowest-rated dimensions addressed
- Tooling deployed (SAST, SCA additions)
- Effort, owners

### Sprint 6 (weeks 11 to 12): Verification
- Regression tests for fixed findings
- Re-audit selected findings
- Tabletop exercises executed
- Effort, owners

## Per-sprint deliverables
List of PANTHEON-NNNN remediations per sprint.

## Dependencies
External team dependencies, vendor dependencies, budget approvals required.

## Risk-acceptance items
Findings explicitly deferred beyond 90 days with rationale.

## Compliance mappings cited
NIST CSF 2.0 Govern (governance and management), ISO 27001 A.5 leadership, NIS2 Art. 21 risk management measures.

## Hard fails (validation rules)
- Six sprints present.
- Every Critical finding scheduled in Sprint 1 or 2.
- Every High finding scheduled by Sprint 4.
- Risk-acceptance items have rationale.
- No em-dashes.

## Signoff
Prepared by: pantheon-orchestrator
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- All deliverables 01 through 22 cross-referenced.

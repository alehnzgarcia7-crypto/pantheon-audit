# Executive Summary
## {{project_name}} Security Audit

**Audit Date**: {{timestamp}}
**Audit ID**: {{audit_id}}

Maximum 5 pages, approximately 2500 words.

## Purpose
Senior-stakeholder one-page summary of audit posture, top 3 strategic risks, and the launch decision. Audience: board, CISO, CTO, CEO, legal counsel, regulator-facing executive.

## Populated from state
| Field | Source |
|---|---|
| project_name | state.json/sow.project_name |
| audit_id | state.json/audit_id |
| critical_count | state.json/findings filtered status accepted, severity Critical |
| high_count | state.json/findings filtered status accepted, severity High |
| medium_count | state.json/findings filtered status accepted, severity Medium |
| low_count | state.json/findings filtered status accepted, severity Low |
| info_count | state.json/findings filtered status accepted, severity Informational |
| maturity_score | state.json/phases/8/maturity_aggregate |
| compliance_coverage_pct | state.json/phases/9/coverage_percentage |
| launch_decision | computed from criteria in template 13 |
| top_3_risks | state.json/phases/2/top_risks |
| top_3_strengths | state.json/phases/8/top_strengths |

## Bottom Line Up Front
Single paragraph: launch decision plus top 3 actions.

## Audit Scope
One paragraph drawn from sow.md.

## Top 3 Strategic Risks
Per risk: description, business impact USD, mitigation effort.

## Top 3 Strengths
Per strength: what is working, business value.

## Findings Summary
- Critical: {{critical_count}}
- High: {{high_count}}
- Medium: {{medium_count}}
- Low: {{low_count}}
- Informational: {{info_count}}

## Codebase Maturity
{{maturity_score}}/13 Satisfactory+. One-paragraph assessment.

## Compliance Posture
Per applicable regulator: posture summary. Source from compliance-matrix.md.

## Recommended Investments
Top 3 investments to make, each with cost and business value.

## Launch Decision
{{launch_decision}} with one-paragraph reasoning.

## What This Audit Did Not Cover
Honest limitations: not human-led tier-S pentest, no live exploitation, no production access, AI-augmented infrastructure.

## Next Steps
1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

## Compliance mappings cited
This summary cites compliance posture by framework. Detailed mappings in deliverable 10 (Compliance Matrix).

## Hard fails (validation rules)
- Document MUST fit within 5 pages.
- Document MUST contain a launch decision value (GO, CONDITIONAL_GO, or NO_GO).
- Document MUST cite findings counts that reconcile with state.json.
- No em-dashes anywhere.

## Signoff
Prepared by: PANTHEON Orchestrator
Reviewed by: Adversarial Judge (gate-log.md)
Mapped by: Compliance Mapper

## References
See accompanying deliverables 02 through 35 for detail.

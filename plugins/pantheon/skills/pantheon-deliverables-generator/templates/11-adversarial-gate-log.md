# Adversarial Gate Log
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Gate persona**: adversarial-judge

## Purpose
Complete audit trail of adversarial-judge verdicts and reasoning across every finding. Audience: third-party validators, regulators, audit reproducibility verifiers, future audit run baseliners.

## Populated from state
| Field | Source |
|---|---|
| gate_verdicts | state.json/gate_verdicts |
| seven_question_chain | state.json/gate_verdicts/[id]/cross_examination |
| revision_cycles | state.json/gate_verdicts/[id]/revision_count |
| disputes | state.json/gate_verdicts where verdict == DISPUTE |
| calibration_per_persona | state.json/telemetry/calibration |

## Executive Summary
Verdict distribution. Calibration per persona. Disputes flagged.

## Verdict Distribution
- ACCEPT: count, percentage
- REVISE: count, percentage
- WITHDRAW: count, percentage
- DISPUTE: count, percentage

## Per-finding entries
For each finding:
- PANTHEON-NNNN id, title, lead persona, reporter confidence
- Seven-question cross-examination chain (Q1 through Q7)
- Final verdict and reasoning
- Revision count if revised
- Mitigation cross-check result

## Calibration metrics
Per persona:
- Confidence to verdict correlation
- Withdrawn rate at high confidence
- Accepted rate at low confidence
- Calibration status: well-calibrated / overconfident / underconfident

## Hallucinations detected
File path hallucinations, CVE hallucinations, framework article hallucinations, API hallucinations. Counts and persona attribution.

## Disputed findings
Findings flagged for human arbitration with reasoning chains.

## Compliance mappings cited
ISO 19011 audit principles (independence, evidence-based), AICPA SSAE 18 audit evidence sufficiency.

## Hard fails (validation rules)
- Every finding has a verdict entry.
- Every verdict cites seven-question chain.
- Calibration table present.
- No em-dashes.

## Signoff
Prepared by: adversarial-judge
Reviewed by: pantheon-orchestrator (meta-audit)
Mapped by: Compliance Mapper

## References
- plugins/pantheon/references/adversarial-gate-protocol.md
- plugins/pantheon/skills/pantheon-adversarial-judge/references/cross-examination-protocol.md
- plugins/pantheon/skills/pantheon-adversarial-judge/references/false-positive-patterns.md

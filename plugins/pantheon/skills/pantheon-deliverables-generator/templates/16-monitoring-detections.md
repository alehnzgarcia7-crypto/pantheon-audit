# Monitoring and Detections
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}

## Purpose
Sigma rule and Elastic / Splunk equivalent detections for the high-priority detection gaps identified during red team simulation. Audience: detection engineering, SOC, SIEM administrators.

## Populated from state
| Field | Source |
|---|---|
| detection_gaps | state.json/phases/7/detection_gaps |
| attack_chains | state.json/phases/7/attack_chains |
| mitre_techniques_in_scope | state.json/phases/7/mitre_techniques |

## Executive Summary
Top detection priorities with rule counts and log source requirements.

## Per-gap detections
For each detection gap:
- Gap description and MITRE ATT&CK technique ID
- Log source required (e.g., AWS CloudTrail, Linux auditd, Kubernetes audit, application logs)
- Sigma rule (vendor-agnostic, full YAML)
- Splunk SPL equivalent
- Elastic ESQL or EQL equivalent
- False positive considerations
- Tuning guidance

## Detection coverage matrix
ATT&CK technique columns vs source columns. Coverage cells: Detected, Partial, Missing.

## Pipeline recommendations
Hypothesis to rule to test to deploy to measure cycle. Detection-as-code adoption.

## Metrics targets
- MTTD per attack chain stage
- True positive rate per rule type
- Alert volume target per day

## Compliance mappings cited
NIST SP 800-92 log management, NIS2 Art. 21(2)(c), DORA Art. 10 detection, SOC 2 CC7 monitoring.

## Hard fails (validation rules)
- Every detection gap from phase 7 has at least one Sigma rule proposed.
- Every rule includes log source requirement.
- Coverage matrix present.
- No em-dashes.

## Signoff
Prepared by: bishop-fox-red-team
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- Sigma project, SigmaHQ
- MITRE ATT&CK Enterprise v15

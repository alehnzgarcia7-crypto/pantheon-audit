# Incident Response Runbook
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}

## Purpose
Findings-driven IR playbooks. For each high-impact attack chain identified, document detection, containment, eradication, recovery, and lessons-learned procedures. Audience: SOC, IR team, on-call engineering, legal counsel.

## Populated from state
| Field | Source |
|---|---|
| attack_chains | state.json/phases/7/attack_chains |
| top_findings | state.json/findings filtered severity Critical High accepted |
| detection_gaps | state.json/phases/7/detection_gaps |
| regulator_notification_obligations | state.json/sow/regulators_applicable |

## Executive Summary
IR readiness assessment, top playbooks delivered.

## Playbook structure (per playbook)
1. Scenario (attack chain reference)
2. Trigger conditions (SIEM rule fires, log patterns)
3. Detection actions (initial triage, severity assignment)
4. Containment actions (isolate, block, revoke)
5. Eradication actions (remove persistence, rotate secrets)
6. Recovery actions (restore, validate)
7. Communication actions (customer comms, regulator notification with hours)
8. Post-incident actions (postmortem, detection rule improvement)
9. Roles and responsibilities matrix
10. Decision tree
11. Reference findings (PANTHEON-NNNN)

## Playbooks delivered (minimum 5)
- Ransomware via supply chain
- Insider data exfiltration
- Critical zero-day in dependency
- Authentication bypass detected in production
- Cryptographic key compromise

## Regulator notification matrix
Per applicable regulator: hours to notify, notification content, escalation contact.

## Tabletop integration
See deliverable 15 for tabletop scenarios that exercise these playbooks.

## Compliance mappings cited
NIS2 Art. 23 incident notification, GDPR Art. 33-34 breach notification, DORA Art. 19 incident reporting, HIPAA Breach Notification Rule, LFPDPPP Art. 40 (vulneraciones).

## Hard fails (validation rules)
- Minimum 5 playbooks.
- Each playbook covers 9 standard sections.
- Regulator notification matrix present if any regulator in scope.
- No em-dashes.

## Signoff
Prepared by: bishop-fox-red-team + mudge-holistic
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- deliverables 08 (Red Team Narrative), 15 (Tabletop Scenarios), 16 (Monitoring Detections)

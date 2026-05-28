# Tabletop Exercise Scenarios
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}

## Purpose
Five tabletop scenarios derived from the threat model and red team narrative. Audience: SOC, IR team, executive crisis team, legal counsel, comms.

## Populated from state
| Field | Source |
|---|---|
| attack_chains | state.json/phases/7/attack_chains |
| regulator_applicable | state.json/sow/regulators_applicable |
| critical_findings | state.json/findings severity Critical, status accepted |

## 5 Scenarios

### Scenario 1: Ransomware via supply chain
- Trigger: malicious dependency update detected by SIEM
- Decisions required: isolate, communicate, restore, regulator notify
- Roles tested: SOC, Engineering, Legal, Comms, Executive
- Expected duration: 60 to 90 min
- Key learnings expected
- Related findings: PANTHEON-NNNN

### Scenario 2: Insider data exfiltration
- Trigger: anomalous bulk database query by departing employee
- Decisions required: contain, investigate, legal action, customer notify
- Roles tested: HR, SOC, Legal, Engineering, Executive
- Duration: 60 to 90 min
- Related findings: PANTHEON-NNNN

### Scenario 3: Critical zero-day in dependency
- Trigger: Log4Shell-style vulnerability announced
- Decisions required: patch timeline, customer comms, workaround deployment
- Roles tested: Engineering, SOC, Comms, Executive
- Duration: 45 to 60 min
- Related findings: PANTHEON-NNNN

### Scenario 4: Regulator inspection
- Trigger: CNBV / SEC / EDPB notifies inspection in 30 days
- Decisions required: preparation timeline, evidence collection, legal counsel
- Roles tested: Legal, Compliance, Engineering, Executive
- Duration: 90 min
- Related findings: PANTHEON-NNNN

### Scenario 5: Public security disclosure
- Trigger: researcher publishes critical bug 0-day
- Decisions required: patch acceleration, customer comms, media response
- Roles tested: Engineering, Comms, Legal, Executive
- Duration: 60 min
- Related findings: PANTHEON-NNNN

## Per scenario template
- Background context
- Initial trigger / inject
- Subsequent injects (timeline)
- Decision points
- Evaluation criteria
- After-action review template

## Compliance mappings cited
NIS2 Art. 21(2)(j) testing, DORA Art. 26 threat-led testing, NIST IR 800-84 tabletop guidance.

## Hard fails (validation rules)
- Exactly 5 scenarios.
- Each scenario includes timing, roles, decisions, and after-action template.
- At least one scenario maps to each top-3 strategic risk.
- No em-dashes.

## Signoff
Prepared by: bishop-fox-red-team + mudge-holistic
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- deliverables 03 (Threat Model), 08 (Red Team Narrative), 14 (IR Runbook)

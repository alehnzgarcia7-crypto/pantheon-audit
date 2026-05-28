# Red Team Narrative
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Framework**: TIBER-EU adapted for code review, MITRE ATT&CK Enterprise v15
**Lead persona**: bishop-fox-red-team + project-zero-researcher

## Purpose
Adversary emulation narrative tying findings into attack chains a real threat actor would execute. Audience: SOC, detection engineering, executive leadership, regulator (TIBER-EU consumers).

## Populated from state
| Field | Source |
|---|---|
| threat_actors_selected | state.json/phases/7/threat_actors_selected |
| attack_chains | state.json/phases/7/attack_chains |
| kill_chain_stages | state.json/phases/7/kill_chain_stages |
| detection_gaps | state.json/phases/7/detection_gaps |
| evasion_techniques | state.json/phases/7/evasion_techniques |
| typhoon_family_iocs | state.json/phases/7/typhoon_iocs |

## Executive Summary
1 to 3 threat actors emulated. Chain count. Detection coverage gap summary.

## Threat Profile
1 to 3 selected threat actors from T1 to T8 customized. Each with capability, motivation, patience, and signature TTPs.

## Adversary Emulation Plan
Per TIBER-EU stage:
1. Reconnaissance: techniques plus ATT&CK TTPs plus detection gap
2. Weaponization
3. Delivery
4. Exploitation
5. Installation
6. C2
7. Actions on Objectives

## Attack Chains
Per chain (2+ findings linked):
- Chain ID
- Threat actor profile assumed
- Steps and PANTHEON-NNNN references per step
- MITRE ATT&CK technique progression
- Detection coverage gap per step
- Evasion techniques required
- Time-to-objective estimate

## Blue Team Effectiveness Assessment
What would be detected at each kill chain stage. Detection gaps prioritized.

## Typhoon family TTPs (if relevant)
Volt, Salt, Flax, Brass Typhoon TTPs cross-referenced. See red-team-simulation reference.

## Recommendations
Quick wins for detection plus long-term blue team improvements.

## Compliance mappings cited
TIBER-EU v2024, DORA Art. 26 threat-led testing, NIS2 Art. 21(2)(j), MITRE ATT&CK Enterprise v15.

## Hard fails (validation rules)
- Minimum 1 attack chain rendered.
- Each chain ties to PANTHEON-NNNN findings.
- MITRE ATT&CK technique IDs cited.
- Detection coverage gap stated per stage.
- No em-dashes.

## Signoff
Prepared by: bishop-fox-red-team + project-zero-researcher
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-red-team-simulation/references/adversary-emulation-library.md
- plugins/pantheon/skills/pantheon-red-team-simulation/references/mitre-attack-mapping.md
- plugins/pantheon/skills/pantheon-red-team-simulation/references/tiber-eu-framework.md

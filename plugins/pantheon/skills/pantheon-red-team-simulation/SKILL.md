---
name: pantheon-red-team-simulation
description: Red team simulation skill following TIBER-EU and MITRE ATT&CK frameworks. Activates in phase 9. Coordinates bishop-fox-red-team (lead) + project-zero-researcher (technical depth) + ncc-group-auditor (regulatory framing). Constructs Adversary Emulation Plan, attack chains, detection coverage gaps, evasion techniques.
---

# PANTHEON Red Team Simulation Skill

## Workflow

1. Read threat-model.md to identify priority threat actors (typically T4, T6, T7)
2. Build Adversary Emulation Plan per TIBER-EU stages: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, C2, Actions on Objectives
3. Per stage: technique used (MITRE ATT&CK ID), exploitable surface, blue team detection gap
4. Construct attack chains stitching 2+ findings into realistic exploitation
5. Output red-team-report.md plus individual findings for novel chains

## What this skill does NOT do
- Does not run actual exploits
- Does not test in production
- Reasons about exploitability through review

## References
- `references/adversary-emulation-library.md`
- `references/mitre-attack-mapping.md`
- `references/tiber-eu-framework.md`

## Hard rules
1. Chains have 2+ findings linked
2. MITRE ATT&CK TTPs cited
3. Detection coverage gap per stage
4. Threat actor profile cited
5. No actual exploitation
6. No em-dashes

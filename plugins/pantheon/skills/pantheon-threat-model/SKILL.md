---
name: pantheon-threat-model
description: Strategic threat modeling skill applying PASTA 7 stages + STRIDE per-element + LINDDUN privacy overlay unified. Activates in phases 1 (architecture review) and 2 (strategic threat model). Builds DFD with trust boundaries, 4-tier asset register, 8 threat actor matrix, attack trees for top 10 threats, MITRE ATT&CK TTP mapping, monetized risk register.
---

# PANTHEON Threat Modeling Skill

## Workflow

### Phase 1: Architecture Review
Personas: mudge-holistic + latacora-pragmatic.
1. Read repo + architecture docs
2. Level 1 DFD: external entities, processes, data stores, data flows
3. Trust boundaries
4. 4-tier classification (Tier 1: money+life-safety, Tier 2: PII+reputation, Tier 3: operational, Tier 4: auxiliary)
5. Output architecture-review.md

### Phase 2: Strategic Threat Modeling
Personas: mudge-holistic + project-zero-researcher.
1. PASTA 7 stages
2. STRIDE per element
3. LINDDUN where PII
4. 8 threat actors ranked
5. Top 10 attack trees
6. MITRE ATT&CK mapping
7. Monetized risk register
8. Output strategic-threat-model.md

## References
- `references/pasta-7-stages.md`
- `references/stride-per-element.md`
- `references/linddun-privacy.md`
- `references/threat-actor-profiles.md`
- `references/attack-tree-patterns.md`

## Hard rules
1. Three frameworks applied
2. 8 threat actors documented
3. Top 10 attack trees
4. MITRE ATT&CK TTPs
5. Monetized risk
6. No em-dashes

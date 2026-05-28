---
name: pantheon-orchestrator
description: Master orchestration skill for high-assurance security audits via PANTHEON. Activates on /pantheon:start, mentions of elite security audit, multi-vendor parallel audit, threat modeling at enterprise scale, regulatory inspection prep, adversarial assessment, or production audit deliverables. Coordinates pantheon-orchestrator sub-agent dispatching 10 specialized auditor personas across 12 mandatory phases with persistent state and 35-deliverable artifact stack.
---

# PANTHEON Orchestrator Skill

Entry point. Dispatches `pantheon-orchestrator` sub-agent.

## Activation triggers
- `/pantheon:start <scope>`
- "audit this project for production"
- "run a high-assurance audit"
- "threat model this codebase"
- "prepare for regulatory inspection"

## What this skill does
1. Verifies `.pantheon/` directory at workspace root
2. Activates `pantheon-orchestrator` sub-agent via Task tool
3. Sub-agent reads CLAUDE.md, .pantheon/threat-model.md if present, orchestrates 12-phase workflow

## References
- `${CLAUDE_PLUGIN_ROOT}/references/12-phases-spec.md`
- `${CLAUDE_PLUGIN_ROOT}/references/persona-doctrines.md`

## Hard rules
1. All personas Opus 4.7 max effort
2. Every finding through adversarial gate
3. Every accepted finding mapped to 18 frameworks
4. No em-dashes
5. Final deliverables only after all 12 phases complete

# PANTHEON Plugin

A multi-persona adversarially gated security audit workflow for Claude Code. This is the plugin source directory inside the `pantheon-audit` marketplace.

For full documentation, see the repository root: `../../README.md`.

## Plugin layout

```
pantheon/
├── .claude-plugin/plugin.json       (plugin manifest)
├── README.md                         (this file)
├── agents/                           (11 sub-agent personas)
├── commands/                         (10 slash commands)
├── hooks/                            (5 hook types + 6 scripts)
├── references/                       (9 shared reference files)
├── scripts/                          (5 utility scripts)
└── skills/                           (16 skills + 35 reference files + 35 templates)
```

## Component summary

- **11 sub-agents**: orchestrator + 8 auditor personas + adversarial-judge + compliance-mapper
- **16 skills**: one per workflow stage + 4 v4.0 frontier-intelligence additions
- **10 commands**: start, phase, persona, status, cross, finding, final, deliverables, resume, reset
- **5 hooks**: SessionStart, PreCompact, Stop (2 hooks), PostToolUse, UserPromptSubmit
- **35 deliverable templates**: regulator/board-grade artifacts
- **18 compliance frameworks** mapped per finding
- **8 threat actor profiles** (T1-T8) for risk assessment

## Quick reference

| Command | Purpose |
|---|---|
| `/pantheon:start <scope>` | Initialize audit |
| `/pantheon:phase <N>` | Execute phase 1-12 |
| `/pantheon:persona <name> <task>` | Ad-hoc persona dispatch |
| `/pantheon:status` | Show audit progress |
| `/pantheon:cross <finding-id> <persona>` | Cross-verify finding |
| `/pantheon:finding <id>` | View finding details |
| `/pantheon:final` | Generate 35 deliverables |
| `/pantheon:deliverables` | List deliverable types |
| `/pantheon:resume` | Continue from checkpoint |
| `/pantheon:reset` | Archive state (irreversible) |

## State

Audit state lives in `.pantheon/state.json` at workspace root. Schema in `references/pantheon-state-schema.json`.

## See also

- Repository root README for installation and full documentation
- `docs/architecture.md` for component diagram
- `docs/how-pantheon-works.md` for end-to-end flow
- `docs/persona-deep-dive.md` for persona methodology context
- `docs/adversarial-gate-explained.md` for verification protocol
- `docs/deliverables-walkthrough.md` for output artifact descriptions

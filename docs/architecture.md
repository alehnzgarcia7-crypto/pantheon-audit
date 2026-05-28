# PANTHEON Architecture

PANTHEON is a Claude Code plugin that orchestrates 11 specialized sub-agent personas across 12 audit phases with persistent state, adversarial verification, and 35-deliverable output.

## Component diagram

```
User
 │
 ├─► /pantheon:start
 │     │
 │     ▼
 ┌──────────────────────────────────────────────────────────────────┐
 │                     pantheon-orchestrator                         │
 │  - Reads CLAUDE.md, state.json                                    │
 │  - Dispatches personas via Task tool                              │
 │  - Maintains state                                                │
 │  - Enforces adversarial gate                                      │
 │  - Triggers compliance auto-mapping                               │
 │  - Generates 35 deliverables on final                             │
 └──────────────┬──────────────────────────┬─────────────────────────┘
                │                          │
        ┌───────┴────────┐         ┌───────┴────────┐
        ▼                ▼         ▼                ▼
   trail-of-bits    ncc-group   bishop-fox      cure53
   (parallel via Task tool split-and-merge)
        │                │         │                │
        └────────┬───────┴─────────┴────────────────┘
                 ▼
         adversarial-judge  ◄── seven-question gate
                 │
                 ▼ (ACCEPT)
         compliance-mapper  ◄── 18 frameworks
                 │
                 ▼
            state.json
                 │
                 ▼ (on /pantheon:final)
   pantheon-deliverables-generator
                 │
                 ▼
   ~/Downloads/pantheon-audit-<uuid>/
   ├── 01-35.md (all deliverables)
   └── README.md (index)
```

## Layered design

### Layer 1: Plugin manifest
`marketplace.json` + `plugin.json`. Discoverable by Claude Code via `/plugin marketplace add`.

### Layer 2: Skills
16 skills under `plugins/pantheon/skills/`. Each defines activation triggers and what gets dispatched.

### Layer 3: Sub-agents
11 sub-agents under `plugins/pantheon/agents/`. Specialized Opus 4.7 instances with persona system prompts.

### Layer 4: Slash commands
10 commands under `plugins/pantheon/commands/`. User-facing entry points.

### Layer 5: Hooks
5 hook types via `hooks.json` + 6 scripts. State preservation, format checking, intent capture.

### Layer 6: References
9 reference files in `plugins/pantheon/references/`. Shared knowledge accessible to all skills/agents.

### Layer 7: Templates
35 deliverable templates in `plugins/pantheon/skills/pantheon-deliverables-generator/templates/`.

### Layer 8: Utility scripts
5 Python/Bash scripts in `plugins/pantheon/scripts/`. Mechanical helpers.

## State management

`.pantheon/state.json` is the single source of truth for active audit. Schema in `references/pantheon-state-schema.json`. Survives session restart, compaction, and resume via SessionStart and PreCompact hooks.

## Concurrency model

- Phases sequential by default
- Within phase, personas may operate in parallel via Task tool spawn-multiple pattern
- Phase 3 explicitly uses 3 parallel personas with orthogonal scope
- Adversarial gate is sequential bottleneck after parallel persona work

## Failure modes

- State.json corruption: backup restored automatically by SessionStart hook
- Persona dispatch failure: orchestrator logs, attempts re-dispatch, escalates to user if repeated
- Adversarial gate timeout: DISPUTE verdict, flagged for human
- Token exhaustion mid-phase: orchestrator pauses, recommends /pantheon:resume

## Extension points

- New persona: add `agents/<name>.md` + `references/persona-doctrines.md` entry
- New framework: add to `18-frameworks-catalog.md` + compliance-mapper skill
- New deliverable: add `templates/NN-name.md` + orchestrator final logic update
- New phase: add to `references/12-phases-spec.md` + orchestrator workflow + state schema

See CONTRIBUTING.md for full process.

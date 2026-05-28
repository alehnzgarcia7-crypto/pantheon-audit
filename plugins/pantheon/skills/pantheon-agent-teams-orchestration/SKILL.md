---
name: pantheon-agent-teams-orchestration
description: Cross-session Agent Teams orchestration for PANTHEON Phase P7 multi-persona consensus. Activates when CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 is set, when Phase P7 begins, or when the orchestrator requests parallel adversarial review across multiple personas. Each persona becomes an independent Claude instance with its own context window per Finding 5.6.1.6. Distinct from in-session sub-agent dispatch.
---

# PANTHEON Agent Teams Orchestration Skill

## When this activates
1. Environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set at session start
2. `pantheon-orchestrator` invokes Phase P7 (multi-persona consensus)
3. Agent count for parallel review exceeds 3 (in-session limit becomes inefficient)

## What this skill does
1. Reads `references/agent-team-manifest-schema.md` and constructs a team manifest for the current audit phase
2. Spawns N independent Claude instances (one per persona being run in parallel), each with its own context window
3. Coordinates via `references/message-passing-contract.md` (file-based message-queue under `.pantheon/agent-teams/<team-id>/`)
4. Aggregates per-persona findings, runs consensus calculation via `pantheon-adversarial-judge`, writes final consolidated findings back to main session

## When NOT to use
- Single-persona audits (in-session sub-agent is faster)
- Phases P1-P6 (sequential, not parallel)
- Sessions without `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` flag

## References
- `references/agent-team-manifest-schema.md`
- `references/message-passing-contract.md`

## Hard rules
1. All team members Opus 4.7 max effort
2. Team manifest signed by orchestrator before dispatch
3. Each team member writes findings to its own scratch file; never directly to shared state
4. Aggregation is gate-mediated through `pantheon-adversarial-judge`
5. Team timeout 90 minutes per persona; idle members terminated and logged
6. No em-dashes

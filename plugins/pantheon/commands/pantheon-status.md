---
description: Display current PANTHEON audit status.
allowed-tools: Read, Bash
model: claude-opus-4-7
---

# /pantheon:status

Show current PANTHEON audit progress.

## Usage
`/pantheon:status`

## What this command does
1. Reads .pantheon/state.json
2. Displays orchestrator discipline format output:
   - Audit ID
   - Current phase
   - Findings counts
   - Maturity score
   - Adversarial gate pass rate
   - Compliance coverage
   - Top 3 priorities
   - Next phase recommendation

## Activate
Read .pantheon/state.json. If not exists, output: "No active PANTHEON audit. Run /pantheon:start to begin." Otherwise format per orchestrator output discipline.

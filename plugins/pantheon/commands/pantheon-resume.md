---
description: Resume PANTHEON audit from last checkpoint.
allowed-tools: Task, Read
model: claude-opus-4-7
---

# /pantheon:resume

Resume PANTHEON audit from .pantheon/state.json checkpoint.

## Usage
`/pantheon:resume`

## What this command does
1. Reads .pantheon/state.json
2. Identifies last completed phase
3. Displays status format
4. Confirms continuation with user
5. Dispatches pantheon-orchestrator to continue from next phase

## Activate
Read state.json. If not exists, recommend /pantheon:start. Otherwise: display orchestrator discipline status format. Ask user to confirm. If confirmed, dispatch orchestrator to continue.

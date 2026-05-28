---
description: Reset PANTHEON state (irreversible). Requires explicit confirmation.
allowed-tools: Bash, Read
model: claude-opus-4-7
---

# /pantheon:reset

Reset PANTHEON state. IRREVERSIBLE.

## Usage
`/pantheon:reset`

## What this command does
1. Reads .pantheon/state.json to display current state
2. Requires explicit user confirmation typing "RESET PANTHEON"
3. If confirmed, archives current .pantheon/ to .pantheon-archive-<timestamp>/
4. Removes .pantheon/
5. Reports completion

## Safety
- Never deletes findings without confirmation
- Archive preserved for recovery
- User must type exact string "RESET PANTHEON"

## Activate
Read .pantheon/state.json. Display contents summary. Print: "Type 'RESET PANTHEON' to confirm. This action archives current state to .pantheon-archive-<timestamp>/." Wait for user input. If exact match: execute mv .pantheon .pantheon-archive-$(date +%s) and confirm. Otherwise: abort.

---
description: View detailed finding by ID.
argument-hint: <finding-id>
allowed-tools: Read
model: claude-opus-4-7
---

# /pantheon:finding

Display full finding details.

## Usage
`/pantheon:finding PANTHEON-0042`

## What this command does
Reads .pantheon/state.json, locates finding by ID, displays full PANTHEON-NNNN format.

## Arguments
$ARGUMENTS: finding ID (PANTHEON-NNNN)

## Activate
Read state.json. Search findings array for ID = $ARGUMENTS. If found, display full format. If not, list available finding IDs.

---
description: Cross-verify a specific finding against another persona perspective.
argument-hint: <finding-id> <persona-name>
allowed-tools: Task, Read
model: claude-opus-4-7
---

# /pantheon:cross

Cross-verify finding against another persona perspective.

## Usage
`/pantheon:cross PANTHEON-0042 ncc-group-auditor`

## What this command does
1. Reads finding from .pantheon/state.json
2. Dispatches specified persona with finding details
3. Persona analyzes from their methodology perspective
4. Result appended to finding cross_verified_by array

## Arguments
$ARGUMENTS: finding ID + persona name

## Activate
Parse $ARGUMENTS. Load finding from state.json. Dispatch persona with: "Cross-verify finding PANTHEON-NNNN from your methodology perspective. Finding details: <full finding>. Return: agree/partial/disagree + reasoning."

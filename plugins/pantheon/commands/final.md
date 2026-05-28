---
description: Generate the 35-deliverable final artifact stack.
allowed-tools: Task, Read, Write, Bash
model: claude-opus-4-7
---

# /pantheon:final

Generate the 35 PANTHEON final deliverables.

## Usage
`/pantheon:final`

## Prerequisites
- All 12 phases status="complete" in state.json
- All findings status=accepted/withdrawn/disputed (none draft/review)

## What this command does
1. Verifies prerequisites. If gaps, lists blockers.
2. Activates pantheon-deliverables-generator skill
3. Generates 35 deliverables to ~/Downloads/pantheon-audit-<uuid>/
4. Includes Launch Decision Document with GO/CONDITIONAL_GO/NO_GO
5. Returns output directory path

## Activate
Read state.json. Verify prerequisites. If pass, dispatch pantheon-orchestrator: "Execute /pantheon:final per orchestrator final deliverables protocol. Generate all 35 deliverables in ~/Downloads/pantheon-audit-<audit_id>/."

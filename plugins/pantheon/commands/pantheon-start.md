---
description: Initialize a high-assurance PANTHEON security audit on the current project.
argument-hint: <scope-description>
allowed-tools: Task
model: claude-opus-4-7
---

# /pantheon:start

Initialize a PANTHEON multi-persona elite security audit.

## Usage
`/pantheon:start "Audit Phoenix Financial OS for production launch readiness"`

## What this command does
1. Verifies `.pantheon/` directory at workspace root (creates if missing)
2. Activates pantheon-orchestrator skill
3. Phase 0 (kickoff): captures scope, exclusions, threat actors via dialogue
4. Generates `.pantheon/sow.md`
5. Recommends `/pantheon:phase 1` to begin technical phases

## Arguments
$ARGUMENTS: scope description for the audit. Should include codebase scope, deployment context, regulatory requirements, intended use.

## Activate
Use Task tool to dispatch `pantheon-orchestrator` sub-agent with task:
"Initialize PANTHEON audit. Scope description: $ARGUMENTS. Run phase 0 (kickoff) per pantheon-orchestrator skill workflow."

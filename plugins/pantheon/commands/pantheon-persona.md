---
description: Invoke a specific PANTHEON persona for ad-hoc analysis outside phase workflow.
argument-hint: <persona-name> <task-description>
allowed-tools: Task
model: claude-opus-4-7
---

# /pantheon:persona

Invoke a specific persona for targeted analysis.

## Usage
`/pantheon:persona trail-of-bits-auditor "Review src/crypto/jwt.ts for alg confusion vulnerabilities"`

## Available personas
- pantheon-orchestrator
- trail-of-bits-auditor
- ncc-group-auditor
- bishop-fox-red-team
- cure53-web-app
- latacora-pragmatic
- project-zero-researcher
- galois-formal-verif
- mudge-holistic
- adversarial-judge
- compliance-mapper

## What this command does
Dispatches specified persona via Task tool with provided task description. Useful for focused review outside standard 12-phase workflow.

## Arguments
$ARGUMENTS: persona name + task description

## Activate
Parse $ARGUMENTS into persona name (first word) and task (remainder). Dispatch persona via Task tool with task.

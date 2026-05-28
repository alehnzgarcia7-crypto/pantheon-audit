---
description: Execute a specific PANTHEON phase (1-12).
argument-hint: <phase-number>
allowed-tools: Task, Read, Bash
model: claude-opus-4-7
---

# /pantheon:phase

Execute a specific PANTHEON phase.

## Usage
`/pantheon:phase 3`

## Phases
1. Architecture Review
2. Strategic Threat Model
3. ASVS L3 Audit
4. Crypto Deep Dive
5. Formal Verification Candidates
6. SAST/DAST/SCA Coverage
7. Property-Based Fuzzing Strategy
8. Supply Chain SLSA
9. Red Team Simulation
10. Compliance Mapping
11. Cross-Vendor Adversarial Verification
12. Executive Final Report

## What this command does
1. Reads .pantheon/state.json to verify previous phases complete
2. If gaps, lists blockers and exits
3. Activates pantheon-orchestrator to dispatch correct personas
4. Personas perform phase work
5. Findings through adversarial gate
6. State updated incrementally

## Arguments
$ARGUMENTS: phase number 1-12

## Activate
Read state.json. Verify phase ($ARGUMENTS - 1) complete. Dispatch pantheon-orchestrator with: "Execute phase $ARGUMENTS per pantheon-orchestrator skill workflow."

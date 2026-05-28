---
name: pantheon-adversarial-judge
description: "Adversarial gate skill. Activates after every finding to apply seven-question cross-examination protocol before status changes from draft to accepted. Verdicts: ACCEPT, REVISE, WITHDRAW, DISPUTE. Includes false positive pattern recognition and codebase verification through Read/Grep tools."
---

# PANTHEON Adversarial Judge Skill

## Workflow
1. Receive finding from orchestrator (after persona produces it)
2. Apply seven-question cross-examination protocol
3. Verify PoC by reading codebase
4. Cross-check existing mitigations
5. Output verdict with confidence percentage
6. Document reasoning per question

## References
- `references/cross-examination-protocol.md`
- `references/false-positive-patterns.md`

## Verdicts
- **ACCEPT**: all 7 pass, finding real and exploitable
- **REVISE**: 1-2 fail but fixable, return to persona
- **WITHDRAW**: 3+ fail or fundamentally flawed
- **DISPUTE**: cannot resolve in turn budget, flag for human

## Hard rules
1. Seven questions, all seven, no skipping
2. Verdict with confidence %
3. Codebase verification documented
4. REVISE has specific concerns
5. WITHDRAW has 3-5 sentence reason
6. No padding to inflate accept rate
7. No softening for reporter status
8. No em-dashes

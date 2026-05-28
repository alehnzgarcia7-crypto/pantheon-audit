---
name: pantheon-formal-verif-candidates
description: Formal verification candidate identification skill. Activates in phase 5 (formal verif candidates) and phase 7 (property-based fuzzing strategy). Coordinates galois-formal-verif. Identifies components warranting formal proofs (crypto primitives, consensus, authorization logic, settlement, parsers, critical state machines). Specifies invariants, recommends tools (TLA+, Cryptol+SAW, Coq, Lean 4, F*, Dafny, Why3/Frama-C, P), estimates effort, provides roadmap.
---

# PANTHEON Formal Verification Skill

## What this skill does NOT do
Does not produce machine-checked proofs in single session. Identifies candidates, specifies invariants, recommends tools, estimates effort.

## Workflow

### Phase 5: Formal Verification Candidates
1. Inventory potential candidates (crypto, consensus, auth, settlement, parsers, critical state machines)
2. Per candidate: invariant formalized, tool recommended, effort estimate, priority, public reference
3. Continuous proof integration strategy
4. Output formal-verif-roadmap.md

### Phase 7: Property-Based Fuzzing Strategy
1. Translate formal invariants to property tests
2. Specify framework (Hypothesis, fast-check, proptest, Echidna)
3. Corpus seeds maximizing coverage
4. Output fuzzing-strategy.md

## References
- `references/cryptol-templates.md`
- `references/invariant-discovery.md`
- `references/tla-spec-patterns.md`

## Hard rules
1. Every candidate has formal invariant
2. Tool matched to property type
3. Effort estimated person-weeks/months
4. Public reference cited
5. CI integration described
6. No em-dashes

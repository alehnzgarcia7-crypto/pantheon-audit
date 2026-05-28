---
name: pantheon-crypto-deep-dive
description: Cryptographic correctness audit skill. Activates in phase 4 (crypto deep dive). Coordinates trail-of-bits-auditor (crypto specialist mode) + galois-formal-verif. Verifies algorithm selection, mode/padding, key sizes, IV/nonce uniqueness, CSPRNG vs PRNG, constant-time comparison, key lifecycle, JWT specifics (alg validation, key confusion, kid injection), post-quantum readiness.
---

# PANTHEON Crypto Deep Dive Skill

## Workflow
1. Identify all crypto code paths
2. Per path verify: algorithm, mode/padding, key size, IV/nonce uniqueness, CSPRNG source, constant-time comparison, key lifecycle, post-quantum readiness
3. JWT-specific: alg validation, key confusion, kid injection, exp/nbf validation
4. Findings with `references/constant-time-checklist.md` and other crypto refs cited

## References
- `references/constant-time-checklist.md`
- `references/jwt-attack-vectors.md`
- `references/key-management-lifecycle.md`
- `references/post-quantum-readiness.md`

## Hard rules
1. No roll-your-own crypto (auto-Critical)
2. CSPRNG required (no Math.random)
3. IV uniqueness verified
4. Post-quantum readiness assessed
5. No em-dashes

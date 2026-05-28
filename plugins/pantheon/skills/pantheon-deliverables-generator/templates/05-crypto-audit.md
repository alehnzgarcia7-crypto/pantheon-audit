# Cryptographic Audit
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Lead personas**: trail-of-bits-auditor + ncc-group-auditor + galois-formal-verif

## Purpose
Cryptographic correctness, key management lifecycle, constant-time properties, JWT exposure, and post-quantum readiness across every crypto code path. Audience: engineering, cryptographers, regulators.

## Populated from state
| Field | Source |
|---|---|
| crypto_inventory | state.json/phases/4/crypto_inventory |
| algorithm_assessment | state.json/phases/4/algorithm_assessment |
| key_lifecycle | state.json/phases/4/key_lifecycle |
| constant_time_findings | state.json/phases/4/constant_time |
| jwt_findings | state.json/phases/4/jwt |
| pq_readiness | state.json/phases/4/pq_readiness |
| cnsa_2_0_alignment | state.json/phases/4/cnsa_2_0 |

## Executive Summary
Top crypto risks. Algorithm posture. Key management maturity. PQ migration status.

## Crypto Inventory
All crypto code paths identified. Per path: algorithm, mode, key size, library used.

## Algorithm Assessment
Per algorithm: approved, deprecated, or forbidden per current NIST guidance.

## Key Management Assessment
Per key: generation, distribution, storage, rotation, revocation, destruction.

## Constant-Time Analysis
Per comparison operation on secrets: constant-time verified or finding.

## JWT Assessment (if applicable)
Algorithm validation, key confusion vectors, kid injection, expiration validation.

## Post-Quantum Readiness
HNDL risk analysis. Migration plan to hybrid (classical plus PQC) or PQC.

## CNSA 2.0 Alignment
For NSA-aligned workloads: deadline matrix per primitive. See deliverable 25.

## Findings
PANTHEON-NNNN format for all crypto findings.

## Recommendations
Short-term: specific code changes.
Long-term: architectural improvements plus PQC migration.

## Compliance mappings cited
NIST SP 800-131A revisions, FIPS 140-3 boundary review, PCI-DSS v4 cryptography sections, GDPR Art. 32, CNSA 2.0 NSA-IAD.

## Hard fails (validation rules)
- Every crypto code path is in the inventory.
- Every secret comparison MUST be assessed for constant-time.
- PQ readiness section MUST exist (even if conclusion is no PQ exposure).
- No em-dashes.

## Signoff
Prepared by: trail-of-bits-auditor, ncc-group-auditor, galois-formal-verif
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/constant-time-checklist.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/jwt-attack-vectors.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/key-management-lifecycle.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/post-quantum-readiness.md

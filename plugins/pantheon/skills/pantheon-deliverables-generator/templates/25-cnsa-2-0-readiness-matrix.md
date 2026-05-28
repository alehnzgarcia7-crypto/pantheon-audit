# CNSA 2.0 Readiness Matrix

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11  
**Baseline reference**: NSA Cybersecurity Advisory (updated May 30, 2025); CNSA 2.0 hard procurement gate January 1, 2027

## Purpose
For any US National Security Systems (NSS) touching audit, verify readiness against the CNSA 2.0 per-category deadline matrix per Finding 5.6.4.4.

## Per-category gates
| Category | Support+Prefer | Exclusive | Current state | Gap |
|---|---|---|---|---|
| Software/firmware signing | 2025 | 2030 (LMS/XMSS per SP 800-208) | <current> | <gap> |
| Web browsers/servers/cloud | 2025 | 2033 | <current> | <gap> |
| Traditional networking (VPN/routers) | 2026 | 2030 | <current> | <gap> |
| Operating systems | 2027 | 2033 | <current> | <gap> |
| Niche/PKI | 2030 | 2033 | <current> | <gap> |
| All custom/legacy | - | 2033 | <current> | <gap> |

## Excluded algorithms (NSS auto-fail if used in CNSA-claimed paths)
- SLH-DSA: <PASS/USED IN: list>
- FN-DSA: <PASS/USED IN: list>
- HashML-DSA: <PASS/USED IN: list>

## Permitted CNSA 2.0 algorithms
- ML-KEM (FIPS 203)
- ML-DSA (FIPS 204)
- AES-256
- SHA-384, SHA-512
- LMS, XMSS (signature, software/firmware signing only)
- ECDH P-384 (transition only)
- ECDSA P-384 (transition only)

## Hybrid PQ/T evidence (RFC 9794)
- TLS hybrid kex used: <yes (X25519MLKEM768/SecP256r1MLKEM768/SecP384r1MLKEM1024) / no>
- SSH hybrid kex used: <yes (mlkem768x25519-sha256 / mlkem768nistp256-sha256 / mlkem1024nistp384-sha384) / no>
- OpenPGP PQC: <IETF-standard / GnuPG-incompatible / not used>

## Findings
| Finding ID | Title | Severity | CNSA category |
|---|---|---|---|
| PANTHEON-<NNNN> | <title> | Critical | <category> |

## Hard fails
- [ ] Any CNSA-claimed system using SLH-DSA, FN-DSA, or HashML-DSA
- [ ] Any NSS without CNSA 2.0 procurement readiness for its category's `support+prefer` deadline

## Roadmap
- Next 90 days: <list>
- Pre-January 2027: <list>
- 2030 and beyond: <list>

## Signoff
- Compliance-mapper persona attestation
- Date: <ISO-8601>

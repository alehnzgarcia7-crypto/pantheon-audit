# Post-Quantum Readiness

NIST PQC selected algorithms (2024):
- Key encapsulation: ML-KEM (Kyber)
- Digital signature: ML-DSA (Dilithium), SLH-DSA (SPHINCS+), FN-DSA (Falcon)

## Current quantum-vulnerable
- RSA (any key size eventually)
- DSA
- ECDSA (all curves)
- ECDH (all curves)
- Diffie-Hellman (classical)

## Quantum-resistant (symmetric)
- AES-256 (quantum reduces effective security to 128 bits, still adequate)
- ChaCha20-Poly1305
- HMAC-SHA-256+
- All hash functions with sufficient output size

## Harvest now, decrypt later (HNDL) threat
Adversaries capturing encrypted traffic today to decrypt when quantum computers available. Long-confidentiality-required data (medical records, state secrets, financial records with retention) at risk.

## Migration strategy
1. Inventory crypto usage with classical algorithms
2. Identify long-confidentiality data (>5 years)
3. Plan hybrid mode (classical + PQC) for transition
4. Monitor NIST PQC finalization (FIPS 203, 204, 205 published 2024)
5. TLS migration via hybrid key exchange (X25519 + ML-KEM)
6. Code signing migration to ML-DSA or SLH-DSA

## Current status (2026)
- TLS 1.3 hybrid key exchange experimental (Chrome, Firefox)
- Cloudflare, Google, AWS testing PQC
- OpenSSL 3.5+ has PQC support
- Most production systems not yet migrated

## Finding severity
- New systems using only classical crypto: High (recommend hybrid)
- Long-confidentiality data with classical: Critical
- Code signing with classical: High (sign with hybrid until full PQC)

## References
- NIST FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA)
- IETF draft-ietf-tls-hybrid-design
- "Quantum Threat Timeline 2023" Global Risk Institute

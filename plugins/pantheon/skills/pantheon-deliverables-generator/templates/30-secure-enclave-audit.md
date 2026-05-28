# Secure Enclave Audit (post-Battering-RAM)

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11  
**Baseline reference**: Findings 5.6.6.8 (Battering RAM defeats SGX + SEV-SNP), 5.6.6.9 (Heracles SEV-SNP CCS 2025), 5.6.6.10 (AMD SB-3020 RMP init), 5.6.6.11 (WeSee #VC attack)

## Purpose
For any audit relying on TEE (Intel SGX, AMD SEV-SNP, ARM TrustZone, Apple Secure Enclave, Intel TDX), this deliverable assesses post-2025 hardware-attack residual risk.

## TEE inventory
| TEE | Vendor | Use case | Physical-tamper threat plausible? |
|---|---|---|---|
| Intel SGX | <use> | <yes/no> |
| AMD SEV-SNP | <use> | <yes/no> |
| ARM TrustZone | <use> | <yes/no> |
| Apple Secure Enclave | <use> | <yes/no> |
| Intel TDX | <use> | <yes/no> |

## Physical-tamper threat model
- [ ] Are the TEE-hosting systems in physically-controlled DCs?
- [ ] Is data confidentiality dependent on TEE alone, or are there cryptographic layers above?
- [ ] What is the recovery plan if Battering-RAM-class attack is successful?

## SEV-SNP specific gates (if used)
- [ ] AMD microcode version is post-Heracles mitigation level
- [ ] AMD SB-3014 and SB-3020 advisories addressed
- [ ] Guest `#VC` handler hardening verified (WeSee mitigation)
- [ ] CVE-2024-56161 microcode patch loader signature verification confirmed

## TDX specific gates (if used)
- [ ] TDX module version current
- [ ] Confidential VM attestation policies (RVPS reference values) match expected guest-image digests
- [ ] Dual remote attestation (CPU TEE + GPU TEE if applicable) verified

## NVIDIA Blackwell B200 specific (if applicable, Finding 5.6.8.21)
- [ ] TDISP plus IDE for inline-encrypted GPU-to-CVM communication
- [ ] Encrypted NVLink in multi-GPU pass-through
- [ ] Dual remote attestation JWT validated (intel_tee + nvidia_gpu sub-objects)

## Findings
| Finding ID | Title | Severity | TEE |
|---|---|---|---|
| PANTHEON-<NNNN> | <title> | <severity> | <SGX/SEV/TDX/TrustZone/SE> |

## Hard fails
- [ ] TEE-only trust assumption when physical access is plausible
- [ ] SEV-SNP firmware below Heracles-mitigation level on confidential-workload nodes
- [ ] AMD microcode without CVE-2024-56161 patch

## Signoff
- Bishop-Fox red-team + Galois personas attestation
- Date: <ISO-8601>

---
name: pantheon-supply-chain-slsa
description: Supply chain security and SLSA framework audit skill. Activates in phase 8 (supply chain). Coordinates latacora-pragmatic. Evaluates SLSA level current vs target, signing and provenance (Sigstore, in-toto), SBOM generation (CycloneDX or SPDX), dependency graph (direct + transitive), typo-squatting risk, maintainer concentration risk, recent ownership changes. Critical post-SolarWinds, xz-utils, event-stream.
---

# PANTHEON Supply Chain SLSA Skill

## Workflow

1. Inventory dependencies (direct + transitive)
2. Check for outdated with known CVEs
3. Single-maintainer critical deps (bus factor risk)
4. Recently changed ownership (compromise risk)
5. Typo-squatting risk
6. SLSA level assessment current vs target
7. Signing and provenance verification (Sigstore cosign, in-toto attestations)
8. SBOM generation/verification (CycloneDX or SPDX)
9. Output supply-chain-report.md

## References
- `references/slsa-levels-spec.md`
- `references/sigstore-integration.md`
- `references/sbom-cyclonedx-template.md`

## Hard rules
1. SLSA level documented
2. SBOM generated and verifiable
3. Critical dep CVE status verified
4. No em-dashes

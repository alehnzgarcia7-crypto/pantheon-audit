# Supply Chain and SLSA Evidence
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Framework**: SLSA + in-toto + Sigstore Cosign v3 + CycloneDX SBOM

## Purpose
Supply-chain integrity posture. SLSA level assessment with concrete evidence, SBOM with vulnerability correlation, dependency provenance, and build-pipeline insider threat. Audience: SRE, security engineering, procurement, regulatory inspectors.

## Populated from state
| Field | Source |
|---|---|
| sbom | state.json/phases/6/sbom_cyclonedx |
| slsa_level_current | state.json/phases/6/slsa_level_current |
| slsa_level_target | state.json/phases/6/slsa_level_target |
| dependency_advisories | state.json/phases/6/dependency_advisories |
| signing_posture | state.json/phases/6/signing_posture |
| provenance | state.json/phases/6/provenance |

## Executive Summary
Current SLSA level. Critical advisories. Path to target SLSA level.

## SLSA Level Assessment
Current level (0/1/2/3) with evidence.
Target level recommended.
Gap analysis.

## SBOM (CycloneDX 1.5)
Full CycloneDX JSON document. Metadata, components (direct plus transitive), dependency graph.

## Vulnerability Correlation
Per component, correlated CVEs from OSV.dev / NVD / GitHub Advisory:
- Component@version
- CVE ID
- Severity (CVSS)
- Patch available (yes/version/no)
- Exploitability (KEV catalog: yes/no)

## Component Risk Assessment
- Single-maintainer critical deps
- Recently ownership-changed deps
- Typo-squatting risk deps
- Unmaintained deps (no commits in 12+ months)
- npm Shai-Hulud IoCs (cross-reference)

## License Analysis
Per component license. License compatibility for project license.

## Build Pipeline Assessment
CI/CD platform, hermeticity, build provenance generation, provenance signing, reproducibility.

## Signing Assessment
Artifact signing (cosign v3 bundle), key management, signature verification at deployment.

## In-Toto Attestation
Current attestations generated. Recommended attestations.

## Cross-registry pinning policy
See deliverable 29.

## Compliance mappings cited
EU Cyber Resilience Act Annex I, NIS2 Art. 21(2)(d) supply chain, NIST SP 800-218 SSDF, NIST SP 800-204D, SLSA v1.1 source track.

## Hard fails (validation rules)
- SBOM MUST validate against CycloneDX 1.5 schema.
- SLSA level MUST be assessed with concrete evidence.
- KEV-listed vulnerabilities MUST be flagged.
- No em-dashes.

## Signoff
Prepared by: latacora-pragmatic + trail-of-bits-auditor
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-supply-chain-slsa/references/slsa-levels-spec.md
- plugins/pantheon/skills/pantheon-supply-chain-slsa/references/sigstore-integration.md
- plugins/pantheon/skills/pantheon-supply-chain-slsa/references/sbom-cyclonedx-template.md
- plugins/pantheon/skills/pantheon-npm-supply-chain/references/cross-registry-pinning-spec.md

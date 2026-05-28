# SBOM in CycloneDX Format

Software Bill of Materials. Inventory of all components in software artifact.

## CycloneDX vs SPDX
- CycloneDX: OWASP, security-focused, vuln data integration
- SPDX: Linux Foundation, license-focused
- Both ISO/IEC standards (CycloneDX 5962, SPDX 5962)
- PANTHEON uses CycloneDX (security focus)

## Minimum SBOM content (per NTIA)
- Author
- Timestamp
- Components: name, version, supplier, unique identifier (purl, CPE), dependencies
- Component relationships (direct/transitive)

## CycloneDX template
```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "version": 1,
  "metadata": {
    "timestamp": "2026-05-27T12:00:00Z",
    "tools": [{"vendor": "anchore", "name": "syft", "version": "1.0.0"}],
    "component": {
      "type": "application",
      "name": "myapp",
      "version": "1.0.0"
    }
  },
  "components": [
    {
      "type": "library",
      "bom-ref": "pkg:npm/express@4.18.2",
      "name": "express",
      "version": "4.18.2",
      "purl": "pkg:npm/express@4.18.2",
      "licenses": [{"license": {"id": "MIT"}}]
    }
  ],
  "dependencies": [
    {"ref": "pkg:application/myapp@1.0.0", "dependsOn": ["pkg:npm/express@4.18.2"]}
  ]
}
```

## Generation tools
- **syft** (Anchore): excellent multi-ecosystem
- **cdxgen** (CycloneDX official)
- **trivy** (Aqua, includes vuln scanning)
- **grype**: vulnerability scanner that reads CycloneDX

## Generation in CI/CD
```yaml
- name: Generate SBOM
  uses: anchore/sbom-action@v0
  with:
    output-file: sbom.cyclonedx.json
    format: cyclonedx-json

- name: Attest SBOM with cosign
  run: |
    cosign attest --predicate sbom.cyclonedx.json \
      --type cyclonedx \
      ghcr.io/myorg/myapp:${{ github.sha }}
```

## Common findings
- No SBOM generated: High (cannot inventory components)
- SBOM not attested/signed: Medium (can be tampered)
- SBOM not consumed at deployment (just file in artifact): Medium (verification gap)
- Vulnerability scanning not integrated: High

## Vulnerability correlation
Once SBOM exists, automatically correlate components to CVEs via OSV.dev, NVD, GitHub Advisory:
```bash
grype sbom.cyclonedx.json --output json > vulns.json
```

## References
- CycloneDX: cyclonedx.org
- SPDX: spdx.dev
- NTIA Minimum SBOM Elements
- "Securing the Software Supply Chain: Recommended Practices for SBOM Consumption" CISA

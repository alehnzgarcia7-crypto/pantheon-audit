# Cross-Registry Pinning Specification

Driven by Mini Shai-Hulud (May 11, 2026, Finding 5.6.6.5) which compromised 170+ npm packages PLUS 2 PyPI packages: the first cross-registry attack. Polyglot projects must pin across all registries.

## Registries in scope
- npm (Node.js): `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, `pnpm-lock.yaml`
- PyPI (Python): `requirements.txt` with hashes, `Pipfile.lock`, `poetry.lock`, `uv.lock`
- RubyGems (Ruby): `Gemfile.lock`
- Maven (Java): `pom.xml` with `<version>` pinning, never `LATEST`
- NuGet (.NET): `packages.lock.json`
- crates.io (Rust): `Cargo.lock`
- Go modules: `go.sum` with hashes
- pkg.go.dev: `go.mod` exact versions

## Polyglot project policy
For projects using 2+ of the above registries, the audit MUST verify:
1. Each registry has lockfile with integrity hashes
2. CI pipeline installs from each lockfile with `--frozen-lockfile` equivalent
3. Renovate / Dependabot config covers all registries (no orphaned registry)
4. SBOM (CycloneDX 1.6+ or SPDX 3.0) generated covering all registries
5. Mirror / proxy registry (e.g., Verdaccio, JFrog Artifactory, Nexus) used in production builds to break direct-registry dependency

## Severity
- Single registry without integrity hashes: High
- Polyglot project without cross-registry policy: Critical
- Production build pulling directly from public registries without proxy: High

## References
- Finding 5.6.6.5 Shai-Hulud cross-registry evolution
- CycloneDX 1.6 multi-registry SBOM
- in-toto Attestation Framework v1.1 cross-component provenance

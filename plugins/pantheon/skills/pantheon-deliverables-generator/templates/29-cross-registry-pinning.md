# Cross-Registry Pinning Audit

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11  
**Baseline reference**: Mini Shai-Hulud (May 11, 2026, Finding 5.6.6.5), first cross-registry attack

## Purpose
For polyglot projects (2+ package registries), verify cross-registry pinning policy per Finding 5.6.6.5.

## Registries in scope
| Registry | Lockfile | Integrity hashes? | Frozen-install in CI? |
|---|---|---|---|
| npm | <path> | <yes/no> | <yes/no> |
| PyPI | <path> | <yes/no> | <yes/no> |
| RubyGems | <path> | <yes/no> | <yes/no> |
| Maven | <path> | <yes/no> | <yes/no> |
| NuGet | <path> | <yes/no> | <yes/no> |
| crates.io | <path> | <yes/no> | <yes/no> |
| Go modules | <path> | <yes/no> | <yes/no> |

## Polyglot-policy gates
- [ ] Each registry has lockfile with integrity hashes
- [ ] CI installs from each lockfile with `--frozen-lockfile` equivalent
- [ ] Dependency-update bot (Renovate/Dependabot) covers ALL registries (no orphaned)
- [ ] SBOM (CycloneDX 1.6+ or SPDX 3.0) covers all registries
- [ ] Mirror/proxy registry used in production builds

## Shai-Hulud IOC check
- [ ] No packages on Shai-Hulud Campaign 1 IOC list
- [ ] No packages on Shai-Hulud 2.0 IOC list
- [ ] No packages on Mini Shai-Hulud IOC list (170+ npm + 2 PyPI, 404 versions)

## Findings
| Finding ID | Title | Severity | Registry |
|---|---|---|---|
| PANTHEON-<NNNN> | <title> | <severity> | <registry> |

## Hard fails
- [ ] Polyglot project without cross-registry policy (Critical)
- [ ] Any package on any Shai-Hulud IOC list (Critical, audit auto-fail)
- [ ] CI installs without `--ignore-scripts` AND without manual review of install scripts (High)

## Signoff
- pantheon-npm-supply-chain skill output
- Date: <ISO-8601>

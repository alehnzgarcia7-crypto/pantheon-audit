---
name: pantheon-npm-supply-chain
description: npm and cross-registry supply-chain defense after Shai-Hulud worm campaigns (September 2025, November 2025, May 2026). Activates when audit scope includes Node.js dependencies, package.json, package-lock.json, npm-shrinkwrap.json, yarn.lock, pnpm-lock.yaml, OR when CI/CD pipeline installs npm or PyPI packages. Implements detection for lockfile-only-deps without integrity hashes, pre-install scripts, post-install scripts harvesting secrets, GitHub Actions workflows publishing to webhook[.]site, cross-registry pinning policy (npm + PyPI + RubyGems + Maven + NuGet + crates.io + Go modules), and the specific IOCs from Wiz, Microsoft, Trend Micro, Palo Alto Unit 42, and ReversingLabs Shai-Hulud reporting per Findings 5.6.6.4 through 5.6.6.6.
---

# PANTHEON npm Supply Chain Skill

## When this activates
1. `package.json`, `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, or `pnpm-lock.yaml` present in audit scope
2. Audit phase P5 (threat-model) or P6 (deep-audit) scans dependencies
3. CI/CD pipeline being audited installs npm or PyPI packages
4. Mexican fintech context (Phoenix Financial OS) with heavy npm dependency surface

## What this skill does
1. **Lockfile integrity check**: Every dependency must have `integrity` field with sha256+ hash; flag `null` or missing as PANTHEON High severity finding
2. **Pre-install detection**: Reads `package.json` `scripts.preinstall` and `scripts.postinstall` for any binary execution, shell call, or unbound network call; flags as Critical per Shai-Hulud 2.0 pre-install evolution
3. **Workflow exfiltration scan**: GitHub Actions `.github/workflows/*.yml` files scanned for: writes to public repos, environment-variable dumps to logs, calls to `webhook[.]site` or any non-allowlisted egress
4. **Shai-Hulud IOC match**: Cross-references known-compromised packages (Wiz, Microsoft, ReversingLabs reports) against current `package-lock.json` resolved tree
5. **Cross-registry pinning audit**: For polyglot projects, verifies that npm AND PyPI AND any other registry pin to integrity hash (cross-registry attack via Mini Shai-Hulud May 2026)
6. **`--ignore-scripts` enforcement**: CI pipelines audited for `npm install --ignore-scripts` or equivalent; absence is High

## References
- `references/shai-hulud-iocs.md`: tracked compromised packages and IOCs
- `references/lockfile-policy.md`: integrity hash policy spec
- `references/cross-registry-pinning-spec.md`: cross-registry pinning patterns

## Hard rules
1. ANY post-install or pre-install script in dependencies surfaces a finding regardless of perceived intent
2. Lockfile without `integrity` field is High severity unconditionally
3. CI pipeline without `--ignore-scripts` and without manual review of all install scripts is High
4. Cross-registry projects (npm + PyPI) without registry-pinning policy is Critical
5. Package on Shai-Hulud IOC list is Critical, audit auto-fails until removed
6. No em-dashes

# Lockfile Integrity Hash Policy

Every dependency entry in `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, or `pnpm-lock.yaml` must include:

1. **Integrity hash**: `sha512-...` or `sha256-...` format. Missing field is High severity finding.
2. **Resolved URL**: Pinned to registry. `latest` tag or wildcard versions are findings.
3. **Reproducible install**: Reinstall with `--ignore-scripts --frozen-lockfile` produces identical tree.

## Detection
```bash
# npm
jq '.. | objects | select(has("integrity") | not) | keys[]' package-lock.json
# yarn (v1)
grep -L "integrity " yarn.lock
# pnpm
yq '.packages | map(select(.integrity == null))' pnpm-lock.yaml
```

## Remediation
- Run `npm install --package-lock-only` to regenerate integrity hashes
- If installing private packages, configure `.npmrc` with `audit=true` and `package-lock=true`
- For CI: `npm ci --ignore-scripts` is the gold-standard install command

## Exemptions
None. There is no business reason to deploy without integrity hashes post-2023.

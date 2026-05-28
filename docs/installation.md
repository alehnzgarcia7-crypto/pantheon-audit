# PANTHEON Installation

## System requirements

- Operating system: macOS, Linux, or WSL2 on Windows
- Claude Code 2.1.144 or newer
- Anthropic Claude subscription with Opus 4.7 access (Max recommended)
- Disk space: ~5 MB for plugin, ~50-500 MB per audit (`.pantheon/` directory)
- Memory: 4 GB minimum, 8 GB+ recommended for large audits
- jq installed (usually pre-installed; otherwise: `brew install jq` or `apt install jq`)
- Python 3.10+ for utility scripts
- Git for cloning the repo

## Installation

### Step 1: Acquire the repository

Option A: clone from GitHub
```bash
git clone git@github.com:alehnzgarcia7-crypto/pantheon-audit.git ~/repos/pantheon-audit
```

Option B: download release tarball (if released)

### Step 2: Verify integrity

Releases are signed with Sigstore Cosign v3 (see `plugins/pantheon/scripts/release-sign.sh`). Before installing a release tarball, verify the bundle:

```bash
cd ~/repos/pantheon-audit
cosign verify-blob \
  --bundle pantheon-v1.0.0.zip.cosign.bundle \
  --trusted-root https://tuf-repo-cdn.sigstore.dev/targets/trusted_root.json \
  --certificate-identity-regexp '^https://github.com/alehnzgarcia7-crypto/pantheon-audit/' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  pantheon-v1.0.0.zip
```

Expected output: `Verified OK`. If verification fails, abort installation and report to the maintainer (@nexogeopo).

Cosign v3.0.4 or newer is required (GHSA-whqx-f9j3-ch6m fix). On macOS: `brew install cosign`. On Linux: see https://docs.sigstore.dev/cosign/installation/.

If installing from a local clone (Option A above, no release tarball), verify the manifests exist and parse:

```bash
ls -la .claude-plugin/marketplace.json plugins/pantheon/.claude-plugin/plugin.json
jq empty .claude-plugin/marketplace.json plugins/pantheon/.claude-plugin/plugin.json && echo "OK"
```

Both must exist and `jq empty` must return zero (silent success).

### Step 3: Add marketplace

Start Claude Code in any directory:
```bash
claude
```

Inside Claude Code:
```
/plugin marketplace add ~/repos/pantheon-audit
```

Expected: `Marketplace pantheon-audit added.`

### Step 4: Install plugin

```
/plugin install pantheon@pantheon-audit
```

Expected: `Plugin pantheon installed.`

### Step 5: Reload plugins

```
/reload-plugins
```

Expected: plugin commands now available.

### Step 6: Verify

```
/pantheon:status
```

Expected: `No active PANTHEON audit. Run /pantheon:start to begin.`

If you see this, installation succeeded.

### Step 7: First audit

Navigate to a project root:
```bash
cd ~/projects/my-project
claude
```

Inside Claude Code:
```
/effort max
/model opus
ultrathink

/pantheon:start "Audit my-project for production launch readiness. Mexican fintech, CNBV scope, target: production-ready in 90 days."
```

Phase 0 dialogue begins.

## Updating

```bash
cd ~/repos/pantheon-audit
git pull
```

Inside Claude Code:
```
/reload-plugins
```

## Uninstalling

```
/plugin uninstall pantheon
/plugin marketplace remove pantheon-audit
```

Audit state in projects' `.pantheon/` directories preserved.

## Troubleshooting installation

See `references/troubleshooting.md`.

## Environment recommendations

Add to `~/.zshrc` or `~/.bashrc`:
```bash
export MAX_THINKING_TOKENS=31999
```

Helps PANTHEON personas reason at depth.

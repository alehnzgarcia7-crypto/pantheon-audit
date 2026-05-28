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

## Cloud-sync warning (PANTHEON-0014 mitigation)

`.pantheon/` in your project workspace and `~/Downloads/pantheon-audit-<uuid>/` in your Downloads directory both contain exploitation guidance for the audit subject until remediation. These directories include:

- Phase outputs that describe attack chains step by step
- Finding bodies with file:line citations and reproduction commands
- Proofs of concept and sample payloads
- The full adversarial-gate log with the auditor's reasoning chain

If these files are syncronized to iCloud, Google Drive, OneDrive, Dropbox, or any third-party storage backend, the audit subject's exploitable weaknesses leak to that backend. For multi-party audits (your code, a vendor's library, a customer's data), this is third-party harm.

Recommended exclusions:

```bash
# macOS iCloud
cd ~/Downloads
xattr -w com.apple.metadata:com_apple_backup_excludeItem com.apple.backupd pantheon-audit-*
xattr -w com.apple.metadata:com_apple_backup_excludeItem com.apple.backupd .pantheon

# Dropbox or Google Drive
# Use the application's selective-sync UI to deselect ~/Downloads/pantheon-audit-* and any
# workspace .pantheon/ tree.

# OneDrive
# Settings -> Sync and backup -> Choose folders -> uncheck the audit directories.
```

The `init-pantheon-dir.sh` script appends `.pantheon/` to a local `.gitignore` automatically, so accidental `git add .` does not capture the audit state. The cloud-sync exclusion is your responsibility because the OS-level sync agents have no awareness of audit-state semantics.

## Marketplace typosquatting (PANTHEON-0015 awareness)

The PANTHEON plugin is published as `pantheon@pantheon-audit` from the marketplace `alehnzgarcia7-crypto/pantheon-audit`. Look-alike names to refuse on install:

- `pantheon-pro`, `pantheon-audit-pro`, `pantheon-audit-plus`
- `panthe0n-audit`, `pantheon-audít` (Unicode lookalike)
- `pantheon-audit-mx`, `pantheon-audit-en` (regional variants by unknown maintainer)
- Marketplaces other than `alehnzgarcia7-crypto/pantheon-audit` that claim to host PANTHEON

Verify the marketplace owner against the maintainer's GitHub profile (https://github.com/alehnzgarcia7-crypto) before adding any marketplace claiming to publish PANTHEON. The canonical `marketplace.json` is signed via Sigstore Cosign v3; see Step 2 above for the verification flow.

If you discover a typosquatted PANTHEON plugin in any marketplace, please report via SECURITY.md so the maintainer can coordinate takedown.

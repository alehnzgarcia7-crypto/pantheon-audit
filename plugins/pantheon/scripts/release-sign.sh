#!/usr/bin/env bash
# PANTHEON release signing (Finding 5.6.1.3): sign the plugin .zip with Sigstore
# Cosign v3 bundle and record a Rekor v2 inclusion proof. Distribution via --plugin-url.
set -euo pipefail

PLUGIN_DIR="${1:-plugins/pantheon}"
VERSION="${2:-$(jq -r '.version' "$PLUGIN_DIR/.claude-plugin/plugin.json")}"
OUT="pantheon-${VERSION}.zip"

# 1. Package
( cd "$(dirname "$PLUGIN_DIR")" && zip -r "$OLDPWD/$OUT" "$(basename "$PLUGIN_DIR")" -x '*.git*' )

# 2. Sign with Cosign v3 (bundle format v0.3). Requires cosign >= 3.0.4 (GHSA-whqx-f9j3-ch6m fix).
COSIGN_VERSION="$(cosign version --json 2>/dev/null | jq -r '.gitVersion // empty')"
case "$COSIGN_VERSION" in
  v3.0.0|v3.0.1|v3.0.2|v3.0.3|v2.6.0|v2.6.1)
    echo "ERROR: cosign $COSIGN_VERSION is vulnerable to GHSA-whqx-f9j3-ch6m. Upgrade to v3.0.4+ or v2.6.2+." >&2
    exit 1
    ;;
esac

cosign sign-blob \
  --yes \
  --bundle "${OUT}.cosign.bundle" \
  "$OUT"

echo "Signed $OUT"
echo "Bundle: ${OUT}.cosign.bundle"
echo "Verify with: cosign verify-blob --bundle ${OUT}.cosign.bundle --trusted-root <root> $OUT"
echo "Distribute via: claude --plugin-url https://github.com/alehnzgarcia7-crypto/pantheon-audit/releases/download/${VERSION}/${OUT}"
exit 0

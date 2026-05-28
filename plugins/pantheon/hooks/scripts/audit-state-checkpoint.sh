#!/usr/bin/env bash
# audit-state-checkpoint.sh
# Invoked on Stop. Backs up state.json to state.json.backup atomically.

set -euo pipefail

PANTHEON_DIR=".pantheon"
STATE_FILE="${PANTHEON_DIR}/state.json"
BACKUP_FILE="${STATE_FILE}.backup"

if [ ! -f "$STATE_FILE" ]; then
    exit 0
fi

# Atomic backup via temp file
TMP_BACKUP=$(mktemp "${PANTHEON_DIR}/state.json.tmp.XXXXXX")
cp "$STATE_FILE" "$TMP_BACKUP"
mv "$TMP_BACKUP" "$BACKUP_FILE"

# Validate JSON
if ! jq empty "$STATE_FILE" 2>/dev/null; then
    echo "[PANTHEON] WARNING: state.json is invalid JSON. Backup preserved." >&2
    exit 1
fi

exit 0

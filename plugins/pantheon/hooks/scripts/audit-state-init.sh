#!/usr/bin/env bash
# audit-state-init.sh
# Invoked on SessionStart. Ensures .pantheon/state.json exists or signals init needed.

set -euo pipefail

PANTHEON_DIR=".pantheon"
STATE_FILE="${PANTHEON_DIR}/state.json"

# If no .pantheon dir, no active audit, exit silently
if [ ! -d "$PANTHEON_DIR" ]; then
    exit 0
fi

# If .pantheon exists but no state.json, attempt recovery from backup
if [ -d "$PANTHEON_DIR" ] && [ ! -f "$STATE_FILE" ]; then
    if [ -f "${STATE_FILE}.backup" ]; then
        cp "${STATE_FILE}.backup" "$STATE_FILE"
        echo "[PANTHEON] Recovered state.json from backup" >&2
    else
        echo "[PANTHEON] WARNING: .pantheon directory exists but state.json missing and no backup. Manual intervention required." >&2
        exit 1
    fi
fi

# Output state summary to stderr (visible to Claude)
if [ -f "$STATE_FILE" ]; then
    AUDIT_ID=$(jq -r '.audit_id // "unknown"' "$STATE_FILE")
    PHASE=$(jq -r '.current_phase // 0' "$STATE_FILE")
    FINDINGS=$(jq -r '.findings | length' "$STATE_FILE" 2>/dev/null || echo "0")
    echo "[PANTHEON] Active audit detected. Audit ID: $AUDIT_ID. Phase: $PHASE/12. Findings: $FINDINGS." >&2
fi

exit 0

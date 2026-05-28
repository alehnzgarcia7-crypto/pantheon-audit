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

# If .pantheon exists but no state.json, attempt recovery from backup.
# Validate the backup parses as JSON before adopting it (PANTHEON-0009).
if [ -d "$PANTHEON_DIR" ] && [ ! -f "$STATE_FILE" ]; then
    if [ -f "${STATE_FILE}.backup" ]; then
        if ! jq empty "${STATE_FILE}.backup" >/dev/null 2>&1; then
            echo "[PANTHEON] ERROR: backup ${STATE_FILE}.backup failed JSON parse. Refusing restoration; manual intervention required." >&2
            exit 1
        fi
        cp "${STATE_FILE}.backup" "$STATE_FILE"
        if ! jq empty "$STATE_FILE" >/dev/null 2>&1; then
            echo "[PANTHEON] ERROR: restored $STATE_FILE failed JSON parse after copy. Removing partial restore." >&2
            rm -f "$STATE_FILE"
            exit 1
        fi
        echo "[PANTHEON] Recovered state.json from backup (JSON validated)" >&2
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

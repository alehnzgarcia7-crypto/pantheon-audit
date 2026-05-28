#!/usr/bin/env bash
# audit-state-precompact.sh
# Invoked on PreCompact. Ensures critical audit state survives compaction.

set -euo pipefail

PANTHEON_DIR=".pantheon"
STATE_FILE="${PANTHEON_DIR}/state.json"

if [ ! -f "$STATE_FILE" ]; then
    exit 0
fi

# Force checkpoint
cp "$STATE_FILE" "${STATE_FILE}.precompact.$(date +%s)"

# Emit critical state to context (stderr visible to Claude)
echo "[PANTHEON PRECOMPACT] State preserved." >&2
echo "[PANTHEON PRECOMPACT] Audit ID: $(jq -r '.audit_id' "$STATE_FILE")" >&2
echo "[PANTHEON PRECOMPACT] Phase: $(jq -r '.current_phase' "$STATE_FILE")/12" >&2
echo "[PANTHEON PRECOMPACT] Findings: $(jq -r '.findings | length' "$STATE_FILE")" >&2
echo "[PANTHEON PRECOMPACT] Use /pantheon:resume after compaction to continue." >&2

exit 0

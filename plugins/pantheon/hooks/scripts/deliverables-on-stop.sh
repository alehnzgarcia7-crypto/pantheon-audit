#!/usr/bin/env bash
# deliverables-on-stop.sh
# Invoked on Stop. If all 12 phases complete and deliverables not yet generated, suggests /pantheon:final.

set -euo pipefail

PANTHEON_DIR=".pantheon"
STATE_FILE="${PANTHEON_DIR}/state.json"

if [ ! -f "$STATE_FILE" ]; then
    exit 0
fi

# Count completed phases
COMPLETED=$(jq -r '[.phases[] | select(.status == "complete")] | length' "$STATE_FILE" 2>/dev/null || echo "0")
DELIVERABLES_GENERATED=$(jq -r '.deliverables_generated // false' "$STATE_FILE" 2>/dev/null || echo "false")

if [ "$COMPLETED" -eq 12 ] && [ "$DELIVERABLES_GENERATED" = "false" ]; then
    echo "[PANTHEON] All 12 phases complete. Run /pantheon:final to generate 35 deliverables." >&2
fi

exit 0

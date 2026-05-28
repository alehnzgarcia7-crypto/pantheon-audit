#!/usr/bin/env bash
# intent-capture.sh
# Invoked on UserPromptSubmit. Captures user intent for audit trail.

set -euo pipefail

PANTHEON_DIR=".pantheon"
INTENT_LOG="${PANTHEON_DIR}/intent-log.jsonl"

if [ ! -d "$PANTHEON_DIR" ]; then
    exit 0
fi

INPUT=$(cat)
PROMPT=$(echo "$INPUT" | jq -r '.user_prompt // empty')
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

if [ -n "$PROMPT" ]; then
    echo "{\"timestamp\":\"$TIMESTAMP\",\"prompt\":$(echo "$PROMPT" | jq -Rs .)}" >> "$INTENT_LOG"
fi

exit 0

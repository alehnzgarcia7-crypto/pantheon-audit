#!/usr/bin/env bash
# finding-format-check.sh
# Invoked on PostToolUse for Write/Edit. Checks if finding format violations.

set -euo pipefail

# Read input from stdin (Claude Code passes tool data)
INPUT=$(cat)

# Check if write was to .pantheon/findings/ or similar
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [[ -z "$FILE_PATH" ]] || [[ ! "$FILE_PATH" =~ \.pantheon/findings/.*\.md$ ]]; then
    exit 0
fi

# Check em-dash violation
if grep -qP "\\x{2014}" "$FILE_PATH" 2>/dev/null; then
    echo "[PANTHEON FORMAT] WARNING: em-dash found in finding file $FILE_PATH. Per PANTHEON style: replace with comma, period, or restructure." >&2
fi

# Check PANTHEON-NNNN format
if ! grep -q "^### PANTHEON-[0-9]\{4\}:" "$FILE_PATH" 2>/dev/null; then
    echo "[PANTHEON FORMAT] WARNING: finding file $FILE_PATH does not start with PANTHEON-NNNN heading." >&2
fi

exit 0

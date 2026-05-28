#!/usr/bin/env bash
# PANTHEON PreToolUse hook: MCP tool-integrity gate (Finding 5.6.1.10).
# Reads PreToolUse hook input JSON from stdin. Emits hookSpecificOutput JSON to stdout.
# For PreToolUse, the correct mechanism is permissionDecision (allow/deny/ask),
# NOT continueOnBlock. continueOnBlock is a PostToolUse mechanism.
set -euo pipefail

INPUT="$(cat)"
TOOL_NAME="$(printf '%s' "$INPUT" | jq -r '.tool_name // empty')"

# Only gate MCP-served tools (names beginning with mcp__)
case "$TOOL_NAME" in
  mcp__*)
    : # proceed to integrity checks below
    ;;
  *)
    # Non-MCP tool: allow without gating
    jq -n '{
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: "allow"
      }
    }'
    exit 0
    ;;
esac

# CVE blocklist: unconditional deny regardless of trusted-root
SERVER_VERSION="$(printf '%s' "$INPUT" | jq -r '.mcp_server_version // empty')"
# Normalize to defeat whitespace/case bypass (PANTHEON-0008).
SERVER_VERSION_NORM="$(printf '%s' "$SERVER_VERSION" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')"
if [ "$SERVER_VERSION_NORM" = "windsurf/1.9544.26" ]; then
  jq -n --arg reason "BLOCKED: CVE-2026-30615 Windsurf MCP prompt-injection-to-RCE" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: $reason
    }
  }'
  exit 0
fi

# Manifest verification (ATTESTMCP): require signed tool manifest when strict mode on
STRICT="$(cat .pantheon/state.json 2>/dev/null | jq -r '.pantheon_mcp_strict // true')"
MANIFEST_OK="$(printf '%s' "$INPUT" | jq -r '.mcp_manifest_verified // false')"
if [ "$STRICT" = "true" ] && [ "$MANIFEST_OK" != "true" ]; then
  jq -n --arg reason "MCP tool $TOOL_NAME has no verified signed manifest (ATTESTMCP). Strict mode denies." '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: $reason
    }
  }'
  exit 0
fi

# VIGIL verify-before-commit: log hypotheses, allow if no out-of-scope side effects flagged
mkdir -p .pantheon
printf '{"timestamp":"%s","event":"vigil_gate","tool":"%s","decision":"allow"}\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$TOOL_NAME" >> .pantheon/audit-log.jsonl

jq -n '{
  hookSpecificOutput: {
    hookEventName: "PreToolUse",
    permissionDecision: "allow"
  }
}'
exit 0

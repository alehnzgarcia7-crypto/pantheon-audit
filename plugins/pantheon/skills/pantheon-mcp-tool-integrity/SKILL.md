---
name: pantheon-mcp-tool-integrity
description: MCP server tool-integrity defense for PANTHEON. Activates on use of any MCP-served tool (Snyk, Semgrep, CodeQL, SonarQube, Trivy, Endor, Cycode, Aikido MCP servers), or when PreToolUse hook detects an MCP tool not previously verified in the session. Implements ATTESTMCP signed-tool-manifest verification and VIGIL verify-before-commit per Findings 5.6.1.10 and 5.6.2.5. Defends against tool-description prompt injection (Maloyan-Namiot arXiv:2601.17549, >85% ASR baseline), client-side tool poisoning (Lin and Milani Fard arXiv:2603.22489), and Windsurf-class MCP-RCE (CVE-2026-30615).
---

# PANTHEON MCP Tool Integrity Skill

## When this activates
1. Any persona invokes a tool whose name begins with `mcp__`
2. PreToolUse hook `mcp-tool-integrity-check.sh` fires
3. New MCP server appears in `.mcp.json` not seen in prior session
4. Tool description changes hash between sessions

## What this skill does (5-step ATTESTMCP plus VIGIL pipeline)
1. **Manifest fetch**: Pulls signed tool manifest from MCP server registry (`server_info` request)
2. **Signature verify**: Validates Sigstore Cosign signature on manifest against trusted-root
3. **Description hash**: SHA-256 of tool description matches manifest entry
4. **Intent grounding (VIGIL)**: Generates 3 speculative hypotheses of what the tool will do; rejects if any hypothesis includes filesystem write outside scope, network egress to non-allowlisted domain, or secret exfiltration
5. **Tool invocation**: Only after steps 1-4 pass. Otherwise the PreToolUse hook returns `permissionDecision: "deny"` with `permissionDecisionReason`, which denies the specific call and feeds the reason back to the agent.

## References
- `references/attestmcp-attestation-pattern.md`: full ATTESTMCP protocol spec
- `references/vigil-verify-before-commit.md`: VIGIL hypothesis-generation patterns
- `references/mcp-cve-catalog.md`: tracked MCP CVEs (CVE-2026-30615 Windsurf, 10 OX Security CVEs, etc.)

## Hard rules
1. NO MCP tool invokes without manifest verification when `pantheon_mcp_strict=true` in state.json (default: true)
2. Manifest signature failure is auto-reject, never warning
3. VIGIL hypotheses logged to `.pantheon/audit-log.jsonl` per invocation
4. CVE-2026-30615 (Windsurf 1.9544.26 prompt-injection-RCE) is unconditional reject regardless of trusted-root
5. No em-dashes

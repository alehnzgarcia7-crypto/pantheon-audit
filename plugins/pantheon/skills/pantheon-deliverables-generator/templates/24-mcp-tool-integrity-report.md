# MCP Tool Integrity Report

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11

## Purpose
Per Finding 5.6.1.10 (MCP-specific vulnerability class, January-March 2026), this deliverable reports on attestation status of every MCP server used during the audit and every MCP tool the audit's sub-agents invoked.

## MCP servers in scope
| Server | Version | Signed manifest? | Signed-by identity | Rekor entry |
|---|---|---|---|---|
| mcp__snyk | 1.6.1 | yes | <identity> | <rekor-uri> |
| mcp__semgrep | <ver> | yes | <identity> | <rekor-uri> |
| mcp__codeql | 2.24.3 | yes | <identity> | <rekor-uri> |
| <others> | | | | |

## Tool invocations attested
Per session, counted by `mcp-tool-integrity-check.sh` PreToolUse hook:
- Total MCP tool invocations: <N>
- Manifest-verified invocations: <N>
- VIGIL-gated invocations: <N>
- Rejected (signature failure): <N>
- Rejected (description hash mismatch): <N>
- Rejected (out-of-scope filesystem or egress): <N>

## CVE blocklist check
- CVE-2026-30615 (Windsurf 1.9544.26 MCP-RCE): <PASS/BLOCKED, never used>
- GHSA-whqx-f9j3-ch6m (Cosign bundle verification regression): Cosign version in use is <ver>, status <PASS/FAIL>
- OX Security MCP STDIO advisory (10 CVEs): <PASS/list of partial-matches>

## Findings
| Finding ID | Title | Severity |
|---|---|---|
| PANTHEON-<NNNN> | <title> | <severity> |

## Compliance mappings
| Framework | Mapping |
|---|---|
| SLSA v1.2 | Build Track L3, Source Track L2 |
| in-toto v1.1 | Verification statement attached |
| NIST SSDF | PO.1.3, PW.4 |

## Hard fails (audit auto-fail)
- [ ] Any MCP server in scope without signed manifest
- [ ] CVE-2026-30615 vector present in any MCP server in use

## Signoff
- Auditor: pantheon-mcp-tool-integrity skill output
- Date: <ISO-8601>

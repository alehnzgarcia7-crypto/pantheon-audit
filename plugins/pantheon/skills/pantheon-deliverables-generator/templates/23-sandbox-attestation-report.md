# Sandbox Attestation Report

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11

## Purpose
Per Finding 5.6.1.2 (Claude Managed Agents API plus user-controlled sandbox, April 10, 2026 GA), tool execution occurs in user-controlled infrastructure while orchestration stays on Anthropic. This deliverable attests the sandbox configuration is consistent with the audit's confidentiality requirements.

## Sandbox configuration verified
| Field | Value |
|---|---|
| Sandbox provider | <Anthropic-Cloudflare-Daytona-Modal-Vercel-OwnCloud> |
| Sandbox region | <region> |
| Sovereignty (EU/US/Sovereign-Mex) | <region-flag> |
| Network egress allowlist | <list> |
| Filesystem persistence | <yes/no, scope> |
| Identity federation token | <ANTHROPIC_WORKSPACE_ID-bound or not> |
| Audit log retention | <duration, location> |
| Sandbox version pinned | <semver> |

## Verification evidence
1. Sandbox provider's attestation document (link)
2. Network policy snapshot (file:line in deliverables/evidence/)
3. WORKSPACE_ID binding evidence (token introspection JSON, redacted)
4. Sandbox provider's SOC 2 Type II or equivalent (if applicable)

## Risk findings
- [ ] Sandbox egress allowlist matches audit scope
- [ ] Sandbox region matches data-residency requirements
- [ ] Identity federation is workspace-bound

## Compliance mappings
| Framework | Mapping |
|---|---|
| FedRAMP High | SC-7, SC-39, AC-4 |
| ISO 27001 | A.13.1, A.13.2 |
| Mexican LFPDPPP 2025 | Article 71 cross-border (if applicable) |

## Signoff
- Sandbox attestation accepted: <yes/no>
- If no, justification: <text>
- Auditor signature: <persona-id>
- Date: <ISO-8601>

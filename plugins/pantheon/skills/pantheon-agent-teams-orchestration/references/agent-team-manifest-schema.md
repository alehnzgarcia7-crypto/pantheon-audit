# Agent Team Manifest Schema

JSON schema for `.pantheon/agent-teams/<team-id>/manifest.json`.

```json
{
  "team_id": "uuid",
  "created_at": "ISO-8601",
  "created_by": "pantheon-orchestrator",
  "phase": 7,
  "members": [
    {
      "persona": "trail-of-bits-auditor",
      "scope": ["src/auth/", "src/crypto/"],
      "model": "opus",
      "effort": "max",
      "context_seed": "sha256-of-shared-context",
      "turn_budget": 50,
      "timeout_minutes": 90,
      "scratch_file": ".pantheon/agent-teams/<team-id>/trail-of-bits-findings.jsonl"
    }
  ],
  "aggregation_target": ".pantheon/agent-teams/<team-id>/consolidated-findings.jsonl",
  "gate_persona": "pantheon-adversarial-judge"
}
```

## Validation
- Schema validation via `scripts/validate-team-manifest.py`
- Signature: SHA-256 of manifest body + orchestrator session-id, stored in `manifest.sig`

## Aggregation contract
1. Each persona writes findings to its `scratch_file` only
2. Orchestrator polls all `scratch_file` until all members report `STATUS: COMPLETE` or timeout
3. Findings deduped by `(file, line, vulnerability_class)` triple
4. Conflicting severity ratings flagged for adversarial-judge review
5. Final consolidated findings written to `aggregation_target` after gate review

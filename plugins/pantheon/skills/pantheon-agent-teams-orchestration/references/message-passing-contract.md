# Agent Teams Message Passing Contract

File-based message-queue under `.pantheon/agent-teams/<team-id>/messages/`.

## Message types

| Type | From | To | Contents |
|---|---|---|---|
| `KICKOFF` | orchestrator | all members | manifest + initial scope |
| `STATUS` | member | orchestrator | progress percentage, turns consumed, current focus |
| `FINDING` | member | scratch_file | one finding in PANTHEON-NNNN format |
| `BLOCK_REQUEST` | member | orchestrator | reason for blocked progress, requested action |
| `GATE_RESULT` | adversarial-judge | member | ACCEPT/REVISE/WITHDRAW per finding |
| `COMPLETE` | member | orchestrator | final summary, all findings written |
| `TIMEOUT` | orchestrator | member | terminate signal |

## File layout

```
.pantheon/agent-teams/<team-id>/
├── manifest.json
├── manifest.sig
├── messages/
│   ├── 0001-kickoff.json
│   ├── 0002-status-trail-of-bits.json
│   └── ...
├── trail-of-bits-findings.jsonl
├── bishop-fox-findings.jsonl
├── ...
└── consolidated-findings.jsonl
```

## Polling cadence
Orchestrator polls `messages/` every 30 seconds. Members write atomically (write to .tmp, rename).

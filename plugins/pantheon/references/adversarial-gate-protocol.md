# Adversarial Gate Protocol

Every finding produced by any PANTHEON persona passes through adversarial-judge before status changes from `draft` to `accepted`.

## Workflow
1. Persona produces finding in PANTHEON-NNNN format. Status: `draft`.
2. Orchestrator dispatches finding to adversarial-judge.
3. Adversarial-judge applies seven-question cross-examination protocol.
4. Adversarial-judge verifies PoC by reading codebase (Read/Grep tools).
5. Adversarial-judge returns verdict: ACCEPT / REVISE / WITHDRAW / DISPUTE.

## Verdicts

### ACCEPT
- All 7 questions pass
- PoC verified
- Status changes to `accepted`
- Finding proceeds to compliance mapping

### REVISE
- 1-2 questions fail but fixable
- Status stays `adversarial-review`
- Specific revision notes returned to persona
- Persona revises, re-submits

### WITHDRAW
- 3+ questions fail or finding fundamentally flawed
- Status changes to `withdrawn`
- Reason documented (3-5 sentences)
- Finding excluded from deliverables

### DISPUTE
- Cannot reach conclusion in turn budget (30 turns max)
- Or genuine methodological disagreement
- Status changes to `disputed`
- Flagged in state.json for human review
- Excluded from automated deliverables but listed in disputes appendix

## Seven questions
1. Working PoC: concrete reproduction available?
2. Severity defensibility: would survive cross-examination?
3. Threat actor specificity: T1-T8 cited?
4. CVSS v4.0 vector correctness: mathematically consistent?
5. Path to production impact: preconditions exist?
6. False positive checks: defense in depth considered?
7. Existing mitigation cross-check: codebase already handles?

## Failure modes the gate exists to prevent
- Inflated severity (Critical for Medium impact)
- Theoretical bugs without PoC
- Findings already mitigated by other layers
- Findings only exploitable in dev configuration
- Misread language semantics
- Outdated CVE patterns on patched code

## Non-bypassable
The gate is structural. Personas cannot mark findings `accepted` directly. Orchestrator cannot bypass on persona request. Only path to accepted: ACCEPT verdict.

## Audit trail
Every gate decision logged in `.pantheon/state.json` per finding:
```json
{
  "adversarial_gate": {
    "verdict": "ACCEPT",
    "confidence": 0.92,
    "reviewed_at": "2026-05-27T12:34:56Z",
    "cross_examination": {
      "q1_working_poc": "PASS",
      ...
    },
    "verification_files_read": ["src/auth/login.ts:42-89"],
    "notes": "..."
  }
}
```

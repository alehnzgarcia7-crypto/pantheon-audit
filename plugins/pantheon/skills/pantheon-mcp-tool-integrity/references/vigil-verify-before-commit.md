# VIGIL: Verify-Before-Commit Protocol

Defends LLM agents against tool stream injection via speculative hypothesis generation and intent-grounded verification.

## Protocol

Before any agent commits to an MCP tool invocation:

1. **Hypothesis generation**: Agent emits 3 speculative outcomes of the tool call as natural-language hypotheses, each tagged with expected side effects.
2. **Intent grounding**: Compare hypotheses against current audit intent declared in `.pantheon/state.json:current_intent`.
3. **Side-effect classification**: Tag each hypothesis side effect as `safe`, `read-only`, `write-in-scope`, `write-out-of-scope`, `network-egress`, `secret-access`.
4. **Gate decision**: Block if any hypothesis includes `write-out-of-scope`, `secret-access` outside declared scope, or `network-egress` to non-allowlisted domain.

## Hypothesis template (used by skill)

```
HYPOTHESIS 1: <tool> will <action> on <target>. Side effects: <classified list>.
HYPOTHESIS 2: <tool> will <alternative action>. Side effects: <classified list>.
HYPOTHESIS 3: <tool> will fail or produce empty output. Side effects: none.
```

## Logging

Every VIGIL decision logged to `.pantheon/audit-log.jsonl`:

```jsonl
{"timestamp":"...","event":"vigil_gate","tool":"mcp__snyk__test","hypotheses":[...],"decision":"PROCEED","verifier_confidence":0.92}
```

## References
- arXiv 2601.15778 (Agentic Confidence Calibration)
- Three-Pillar Model for Safe AI Agents (2026)

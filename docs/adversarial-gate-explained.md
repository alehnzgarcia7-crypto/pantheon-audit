# The Adversarial Gate Explained

## Why it exists

Traditional security tools have a false positive problem. Findings get accepted because:
- Reporter has high status (senior auditor's opinion not challenged)
- Tool finding patterns recognized but not verified for specific codebase
- Severity inflated for visibility
- "Looks plausible" without working PoC

This produces noise. Real attackers find the actual vulnerabilities, not the inflated alarms.

PANTHEON makes adversarial verification structural. No finding is accepted without surviving seven-question cross-examination.

## The protocol

Adversarial-judge reviews every finding:

1. **Working PoC**: concrete reproduction available?
2. **Severity defensibility**: would survive cross-examination in legal discovery?
3. **Threat actor specificity**: which T1-T8 can exploit?
4. **CVSS vector correctness**: mathematically consistent?
5. **Path to production impact**: preconditions exist in this codebase?
6. **False positive check**: defense in depth considered?
7. **Existing mitigation cross-check**: does codebase already handle?

## The verdicts

- **ACCEPT**: all 7 pass, finding real. Status: `accepted`.
- **REVISE**: 1-2 fail but fixable. Return to persona for revision.
- **WITHDRAW**: 3+ fail or fundamentally flawed. Status: `withdrawn`.
- **DISPUTE**: cannot resolve in turn budget. Flagged for human.

## Why this matters

Without the gate:
- 200 findings claimed
- 80% false positive
- 40 real findings buried in 160 noise

With the gate:
- 100 findings claimed (others WITHDRAW)
- 95% true positive
- 95 real findings, 5 in DISPUTE for human review

Better signal-to-noise ratio means:
- Engineering team trusts findings, addresses them
- Compliance reports defensible in regulator inspection
- Launch Decision based on real risk, not inflated count

## Why opus 4.7 max

Adversarial-judge runs Opus 4.7 max effort. Cheap models miss the false positives that look superficially correct. The cost differential vs Sonnet ($) is much less than the cost of an inflated audit (engineering hours wasted + regulator credibility damaged).

## Non-bypassable

The gate is structural. Personas cannot mark findings `accepted` directly. Orchestrator cannot bypass on persona request. Only path to `accepted`: ACCEPT verdict from judge.

This is intentional. Tools that allow bypass become checkbox tools. PANTHEON is not a checkbox tool.

## Dispute handling

DISPUTE flags for human review. State.json preserves dispute notes. Final deliverables include disputes appendix. User reviews, makes final call.

This is the only path through the gate that does not produce binary accept/reject. Disputes acknowledge that AI judgment has limits.

## Audit trail

Every gate decision logged in state.json per finding. Verdict, confidence, cross-examination Q1-Q7 results, files verified, notes. Reviewable, defensible, reproducible.

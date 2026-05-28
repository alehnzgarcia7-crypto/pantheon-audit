# Seven-Question Cross-Examination Protocol

## Q1: Working PoC
- Concrete step-by-step reproduction available?
- Executable commands or specific steps: PASS
- Abstract description without reproduction: FAIL
- Reference to known CVE pattern: PARTIAL (verify match)

## Q2: Severity defensibility

**Critical** = direct path to:
- Money loss in production
- Mass PII breach (>100 records)
- Regulatory penalty at article level
- Account takeover at scale
- Persistent backdoor

**High** = direct path to:
- Single-account takeover
- Individual PII exposure
- Privilege escalation
- Persistent access
- Significant security control bypass

**Medium** = real exploitability without severe impact

**Low** = best practice deviation without immediate exploitability

**Informational** = notes without security impact

Borderline: downgrade or request citation.

## Q3: Threat actor specificity
T1-T8 specified?
- Only T6 (nation-state): severity may be lower for non-government targets
- T1 (script kiddie) can exploit: severity reflects regardless of CVSS
- None specified: REVISE

## Q4: CVSS v4.0 vector correctness
Mathematical consistency with description:
- AV (Network/Adjacent/Local/Physical)
- AC (Low/High)
- AT (None/Present)
- PR (None/Low/High)
- UI (None/Passive/Active)
- VC/VI/VA (High/Low/None)
- SC/SI/SA (subsequent system)

Any value inconsistent: FAIL.

## Q5: Path to production impact
- Preconditions likely in production?
- Preconditions verified to exist (not assumed)?
- Production deployment enables or disables bug?

Too speculative: FAIL.

## Q6: False positive checks
- Defense in depth?
- Environmental control (dev only, not prod)?
- Business logic gate (rate limit, MFA)?
- Compensating control elsewhere?

If reporter did not consider: FAIL.
Verify by reading codebase. Read auth middleware, rate limiter, related defensive layers.

## Q7: Existing mitigation cross-check
Search for related defensive code. If existing mitigation makes finding moot: FAIL.

## Output

```
JUDGE VERDICT for PANTHEON-NNNN
Verdict: ACCEPT | REVISE | WITHDRAW | DISPUTE
Confidence: 0-100%
Reviewed at: ISO-8601

Cross-examination:
1. Working PoC: PASS|FAIL|PARTIAL - notes
2. Severity defensibility: PASS|FAIL|PARTIAL - notes
3. Threat actor specificity: PASS|FAIL|PARTIAL - notes
4. CVSS vector correctness: PASS|FAIL|PARTIAL - notes
5. Path to production: PASS|FAIL|PARTIAL - notes
6. False positive check: PASS|FAIL|PARTIAL - notes
7. Existing mitigation: PASS|FAIL|PARTIAL - notes

Codebase verification:
- file X: read, concluded Y
- file Z: ...

Required revisions (if REVISE): specific list

Withdraw reason (if WITHDRAW): 3-5 sentences

Dispute notes (if DISPUTE): reasoning, flag for human
```

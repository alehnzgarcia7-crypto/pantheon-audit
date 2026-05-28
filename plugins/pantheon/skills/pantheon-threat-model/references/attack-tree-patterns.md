# Attack Tree Patterns

## Account Takeover
```
Root: Take over user account
├── Credential theft (phishing, stuffing, breach correlation, XSS session theft)
├── Auth bypass (SQLi login, JWT alg, reset flaw, OAuth misconfig)
└── MFA bypass (SMS interception, TOTP seed leak, recovery flaw)
```

## Data Exfiltration
```
Root: Exfiltrate sensitive data
├── Direct (SQLi mass extract, IDOR bulk PII, API enum)
├── Indirect (S3 misconfig, log access, cache poisoning)
└── Insider (privileged copy, vendor access abuse)
```

## Money Loss (Fintech)
```
Root: Steal funds
├── Account takeover then transfer
├── Transfer auth bypass (race idempotency, decimal arbitrage, replay)
├── Internal accounting (negative balance, double-spend, currency confusion)
└── Payment rail abuse (SPEI tampering, card replay, webhook spoofing)
```

## Construction rules
1. Root = business objective
2. Each leaf: difficulty + detection + mitigation status + residual
3. Mark T1-T8 per path
4. Depth 3-5 levels
5. Cross-reference PANTHEON-NNNN findings
6. Mark high-impact + low-difficulty as priority

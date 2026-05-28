---
name: pantheon-codebase-maturity
description: Codebase maturity scorecard skill. Activates as cross-cutting concern throughout audit. Every persona contributes to the 13-dimension scorecard. Independent of findings list. Rates each dimension Strong / Satisfactory / Moderate / Weak / Missing with evidence citations. Output integrates into final deliverables.
---

# PANTHEON Codebase Maturity Skill

## 13 dimensions
1. Arithmetic and decimal precision
2. Authentication and authorization
3. Comments and documentation
4. Cryptography
5. Data handling (input validation, sanitization)
6. Dependencies management
7. Documentation (external)
8. Error reporting and handling
9. Logging and monitoring
10. Memory safety and resource management
11. Test suite design and effectiveness
12. Configuration management
13. Threat intelligence integration

## Rating scale
- **Strong**: industry-leading practices, evidence of intentional design
- **Satisfactory**: meets reasonable expectations, no urgent gaps
- **Moderate**: gaps present but defensible, plan to improve exists
- **Weak**: significant gaps without remediation plan
- **Missing**: absent or grossly inadequate

## Workflow
Each persona contributes to relevant dimensions during their phase:
- trail-of-bits: arithmetic, crypto, data handling, memory safety, test suite
- ncc-group: auth/authz, dependencies, configuration, threat intel
- cure53: data handling (XSS), dependencies (client-side)
- latacora: auth/authz, dependencies, logging/monitoring, error handling
- galois: crypto, test suite (property-based), arithmetic
- mudge: dependencies (supply chain), threat intel, configuration

Orchestrator aggregates into final scorecard. Conflicts resolved by lowest rating (conservative).

## References
- `references/13-dimensions-rubric.md`

## Output format
Table per dimension with rating + evidence:

| Dimension | Rating | Evidence | Improvement priority |
|---|---|---|---|

Plus narrative explanation per dimension.

## Hard rules
1. Every dimension rated
2. Evidence cites specific file:line or absent feature
3. Improvement priority P0-P3
4. No em-dashes

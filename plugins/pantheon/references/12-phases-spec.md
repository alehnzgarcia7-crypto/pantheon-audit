# PANTHEON 12-Phase Specification

| # | Phase | Skill | Personas | Output |
|---|---|---|---|---|
| 0 | Kickoff | pantheon-orchestrator | self | sow.md, threat-actor-profile.md |
| 1 | Architecture Review | pantheon-threat-model | mudge-holistic + latacora-pragmatic | architecture-review.md |
| 2 | Strategic Threat Model | pantheon-threat-model | mudge-holistic + project-zero-researcher | strategic-threat-model.md |
| 3 | ASVS L3 Audit | pantheon-asvs-l3-audit | trail-of-bits + ncc-group + cure53 (parallel) | asvs-findings.md |
| 4 | Crypto Deep Dive | pantheon-crypto-deep-dive | trail-of-bits (crypto mode) + galois-formal | crypto-validation.md |
| 5 | Formal Verif Candidates | pantheon-formal-verif-candidates | galois-formal | formal-verif-roadmap.md |
| 6 | SAST/DAST/SCA Coverage | pantheon-asvs-l3-audit | trail-of-bits + ncc-group | automated-coverage.md |
| 7 | Property-Based Fuzzing | pantheon-formal-verif-candidates | trail-of-bits + galois-formal | fuzzing-strategy.md |
| 8 | Supply Chain SLSA | pantheon-supply-chain-slsa | latacora-pragmatic | supply-chain-report.md |
| 9 | Red Team Simulation | pantheon-red-team-simulation | bishop-fox + project-zero | red-team-report.md |
| 10 | Compliance Mapping | pantheon-compliance-mapper | compliance-mapper | compliance-matrix.md |
| 11 | Adversarial Cross-Verification | pantheon-adversarial-judge | adversarial-judge | cross-verification.md |
| 12 | Final Deliverables | pantheon-deliverables-generator | self + all | 35 deliverables in ~/Downloads/pantheon-audit-<uuid>/ |

## Phase order and parallelism

Phases 0-11 sequential by default. Within phase, multiple personas may operate in parallel via Task tool split-and-merge pattern.

Exception: phase 3 (ASVS L3) explicitly uses three personas in parallel with orthogonal scope:
- trail-of-bits: crypto, state machines, money flows
- ncc-group: API surface, auth breadth, configuration
- cure53: web/mobile/browser specifics

## State transitions

Per phase:
1. `status: "in-progress"` + `started_at`
2. Personas work, produce findings
3. Each finding through adversarial gate
4. Accepted findings through compliance mapper
5. Phase deliverable written
6. `status: "complete"` + `completed_at` + `deliverable_path`

## Skipping phases

Orchestrator does not skip phases without explicit user authorization. To authorize: user must explicitly state "skip phase N because <reason>" and orchestrator records in state.json `phases.N.status = "skipped"` with reason.

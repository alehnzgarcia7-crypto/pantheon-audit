# Formal Verification Candidates
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Lead persona**: galois-formal-verif

## Purpose
Identify code regions where machine-checked formal verification produces highest assurance return on effort. Audience: engineering leads, formal-methods teams, ROI-evaluating executives.

## Populated from state
| Field | Source |
|---|---|
| candidates | state.json/phases/5/candidates |
| invariants | state.json/phases/5/invariants |
| tools_recommended | state.json/phases/5/tools |
| tcb_assumptions | state.json/phases/5/tcb |
| side_channel_assumptions | state.json/phases/5/side_channel |

## Executive Summary
5 to 15 candidates with effort estimates and ROI summary.

## Candidates by Priority
For each candidate:
- Candidate name
- Component path
- Invariant (formal)
- Tool recommended (TLA+, Cryptol+SAW, Coq, Lean 4, F*, Dafny)
- Effort estimate (person-weeks)
- Priority (P0 / P1 / P2)
- Public reference (similar verification published)
- CI integration approach

## Recommended Phasing
Year 1 candidates, Year 2 candidates, Year 3+ candidates.

## TCB Assumptions
What is assumed correct (compiler, runtime, hardware).

## Side-Channel Assumptions
What side-channel attacks are out of scope.

## ROI Analysis
Cost (person-time plus tooling) vs benefit (defect reduction plus assurance level).

## Symbolic-to-computational gap (where applicable)
Note where symbolic proofs do not bound the computational adversary; cite cure53 / ncc / galois symbolic-to-computational reference.

## Compliance mappings cited
DO-178C / DO-330 verification credit (avionics), FIPS 140-3 high assurance, Common Criteria EAL evidence, NSA Common Evaluation Module guidance.

## Hard fails (validation rules)
- Minimum 5 candidates.
- Each candidate states invariant in machine-checkable form.
- Each candidate has effort estimate in person-weeks.
- No em-dashes.

## Signoff
Prepared by: galois-formal-verif
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-formal-verif-candidates/references/cryptol-templates.md
- plugins/pantheon/skills/pantheon-formal-verif-candidates/references/invariant-discovery.md
- plugins/pantheon/skills/pantheon-formal-verif-candidates/references/tla-spec-patterns.md

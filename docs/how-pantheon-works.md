# How PANTHEON Works

End-to-end flow of a PANTHEON audit.

## Phase 0: Kickoff

1. User: `claude`, then `/pantheon:start "Audit Phoenix Financial OS for production launch"`
2. pantheon-orchestrator skill activates
3. Sub-agent dispatched, reads CLAUDE.md and project structure
4. Init script creates `.pantheon/` directory and `state.json`
5. Orchestrator runs structured dialogue:
   - Scope of audit (which subsystems?)
   - Geographic scope (Mexico? EU? US?)
   - Industry context (fintech? healthcare?)
   - Regulatory requirements (CNBV, GDPR, PCI-DSS, etc.)
   - Threat actors most relevant (T1-T8 ranking)
   - Success criteria (launch decision? regulatory inspection? Series A diligence?)
   - Exclusions (out-of-scope subsystems)
6. Generates `.pantheon/sow.md`
7. Marks phase 0 complete in state.json
8. Recommends `/pantheon:phase 1`

## Phase 1: Architecture Review

1. User: `/pantheon:phase 1`
2. Orchestrator dispatches mudge-holistic + latacora-pragmatic in parallel
3. Both personas read repo structure, architecture docs, identify trust boundaries
4. Generate design-level findings in PANTHEON-NNNN format
5. Each finding through adversarial-judge gate
6. Accepted findings through compliance-mapper
7. Output: `.pantheon/phase-outputs/01-architecture-review.md`
8. Phase 1 marked complete

## Phases 2-11

Similar pattern: orchestrator dispatches appropriate personas, personas produce findings, gate processes each, mapper assigns compliance, state updated, deliverable written.

Phase 3 notable: trail-of-bits + ncc-group + cure53 in parallel with orthogonal scope.

Phase 9 notable: bishop-fox leads with TIBER-EU framework, project-zero supports with technical exploit chain depth.

Phase 11 notable: adversarial-judge performs final cross-verification of all findings, ensures consistency.

## Phase 12: Final Deliverables

1. User: `/pantheon:final`
2. Orchestrator verifies all 12 phases complete and all findings in terminal status (accepted/withdrawn/disputed)
3. Activates pantheon-deliverables-generator skill
4. Reads all phase outputs, state.json
5. For each of 35 templates: loads template, populates with findings/evidence/citations
6. Writes 22 files to `~/Downloads/pantheon-audit-<uuid>/`
7. Includes Launch Decision Document with GO/CONDITIONAL_GO/NO_GO based on mechanical criteria
8. Returns output directory path

## State persistence

- Every meaningful update writes to `.pantheon/state.json`
- Stop hook backs up state.json to state.json.backup
- PreCompact hook preserves state.json.precompact.<timestamp>
- SessionStart hook restores from backup if state.json missing/corrupted
- /pantheon:resume continues from last completed phase

## Cost model

For 50-200K LoC codebase:
- Per persona dispatch: 20-50K input tokens, 10-30K output tokens
- Phase with 1 persona: 30-80K tokens total
- Phase with 3 parallel personas: 90-240K tokens
- Full 12-phase audit: 1-3M tokens
- Plan for Claude Max usage (or be patient on Pro)

## Quality bar

PANTHEON output should be reviewed by qualified security professionals before action. Not a substitute for human-led tier-S audit. AI-augmented audit infrastructure that reduces the cost barrier from $50M to accessible for solo founders, startups, and resource-constrained teams.

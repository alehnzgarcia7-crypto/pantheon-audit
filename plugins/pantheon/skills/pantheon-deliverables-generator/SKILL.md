---
name: pantheon-deliverables-generator
description: 35-deliverable artifact generation skill. Activates on /pantheon:final after all 12 phases complete. Reads .pantheon/state.json plus all phase outputs and generates 35 artifacts in ~/Downloads/pantheon-audit-<uuid>/. Each deliverable is regulator/board-grade quality, audience-specific (technical, executive, regulatory, legal, M&A, customer).
---

# PANTHEON Deliverables Generator Skill

## Workflow
1. Verify phases 0-11 complete in state.json
2. Verify all findings have status accepted/withdrawn/disputed
3. Read all phase outputs from .pantheon/
4. For each of 35 deliverables: load template, populate from state, write to output directory
5. Validate output (no em-dashes, no markdown errors, no truncated sections)
6. Generate index README.md listing all 35
7. Return absolute path of output directory

## Output location
`~/Downloads/pantheon-audit-<uuid>/`

## 35 deliverables list (v4.0)
1. Strategic Threat Model
2. Architecture Security Review
3. Pentest Report (Trail of Bits style)
4. Pentest Report (NCC Group style)
5. Pentest Report (Bishop Fox style)
6. Red Team Engagement Report
7. Purple Team Improvement Plan
8. Codebase Maturity Scorecard (13 dimensions)
9. Crypto Validation Report
10. Formal Verification Roadmap
11. Compliance Matrix (18 frameworks stacked)
12. SBOM (CycloneDX)
13. Supply Chain Provenance Report
14. Bug Bounty Program Recommendations
15. Insider Threat Assessment
16. SOC Effectiveness Baseline
17. DR/BCP Validation
18. Tabletop Scenarios (5 scenarios)
19. Vendor Risk Matrix
20. Launch Decision Document (GO/CONDITIONAL_GO/NO_GO)
21. Executive Summary (5 pages max)
22. Strategic Security Roadmap (24-month plan)

## References
Templates in `templates/01-strategic-threat-model.md` through `templates/22-strategic-roadmap-24-months.md`.

## Hard rules
1. All 35 generated
2. No em-dashes in any output
3. Each cites specific findings, evidence, frameworks
4. Executive Summary fits 5 pages
5. Launch Decision applies mechanical criteria from orchestrator spec
6. Output directory created if not exists

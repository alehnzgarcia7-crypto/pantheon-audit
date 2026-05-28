---
name: pantheon-asvs-l3-audit
description: OWASP ASVS 5.0 Level 3 audit skill. Activates in phase 3 (ASVS L3) and phase 6 (SAST/DAST/SCA coverage). Systematic verification against all 14 ASVS chapters at L3 for critical systems (financial, healthcare, defense). Coordinates trail-of-bits-auditor + ncc-group-auditor + cure53-web-app parallel scope subset audit.
---

# PANTHEON ASVS L3 Audit Skill

## Workflow

### Phase 3: ASVS L3 (parallel personas)
- trail-of-bits: crypto, state, money
- ncc-group: API, auth breadth, configuration
- cure53: web/mobile/browser

Each persona:
1. Read ASVS 5.0 L3 checklist
2. Map chapters to scope
3. Verify each L3 requirement
4. Finding for non-compliance with `owasp_asvs_v5_l3: ["X.Y.Z"]`

### Phase 6: SAST/DAST/SCA coverage
trail-of-bits + ncc-group parallel.
1. Inspect CI/CD config
2. Identify tools and gaps
3. Recommend custom rules

## References
- `references/asvs-v5-l3-checklist.md`
- `references/owasp-top10-2021.md`

## Hard rules
1. ASVS L3 cited every finding
2. OWASP Top 10 2021 cited
3. No em-dashes

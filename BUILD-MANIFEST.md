# BUILD-MANIFEST

PANTHEON v1.0.0 (v5.0 mega-prompt) manifest. Sprint 2 added 8 CI configuration files (PANTHEON-0005 remediation). Sprint 4 adds SECURITY.md (PANTHEON-0004 remediation). Post-re-audit handoff adds PANTHEON-STATUS.md (project state for session resumption).

Total files: **166** (157 plugin + 8 CI configs + 1 handoff doc).

CC MUST create exactly these 156 files. No additions, no omissions, no silent renames. Content for each path resolves via Subsection 0.7 File Content Resolution Rule (explicit `### File:` section, else Section 5.6 Finding extraction, else category contract). Validation in Appendix A diffs `find . -type f | sort` against this list.

## Repo-level (9)
- BUILD-MANIFEST.md
- LICENSE
- README.md
- CLAUDE.md
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md
- SECURITY.md
- PANTHEON-STATUS.md
- .gitignore

## Marketplace + Plugin manifests (2)
- .claude-plugin/marketplace.json
- plugins/pantheon/.claude-plugin/plugin.json

## Sub-agents (11)
- plugins/pantheon/agents/adversarial-judge.md
- plugins/pantheon/agents/bishop-fox-red-team.md
- plugins/pantheon/agents/compliance-mapper.md
- plugins/pantheon/agents/cure53-web-app.md
- plugins/pantheon/agents/galois-formal-verif.md
- plugins/pantheon/agents/latacora-pragmatic.md
- plugins/pantheon/agents/mudge-holistic.md
- plugins/pantheon/agents/ncc-group-auditor.md
- plugins/pantheon/agents/pantheon-orchestrator.md
- plugins/pantheon/agents/project-zero-researcher.md
- plugins/pantheon/agents/trail-of-bits-auditor.md

## Slash commands (10)
- plugins/pantheon/commands/cross.md
- plugins/pantheon/commands/deliverables.md
- plugins/pantheon/commands/final.md
- plugins/pantheon/commands/finding.md
- plugins/pantheon/commands/persona.md
- plugins/pantheon/commands/phase.md
- plugins/pantheon/commands/reset.md
- plugins/pantheon/commands/resume.md
- plugins/pantheon/commands/start.md
- plugins/pantheon/commands/status.md

## Hooks (9: 1 json + 8 scripts)
- plugins/pantheon/hooks/hooks.json
- plugins/pantheon/hooks/scripts/audit-state-checkpoint.sh
- plugins/pantheon/hooks/scripts/audit-state-init.sh
- plugins/pantheon/hooks/scripts/audit-state-precompact.sh
- plugins/pantheon/hooks/scripts/deliverables-on-stop.sh
- plugins/pantheon/hooks/scripts/finding-format-check.sh
- plugins/pantheon/hooks/scripts/intent-capture.sh
- plugins/pantheon/hooks/scripts/mcp-tool-integrity-check.sh
- plugins/pantheon/hooks/scripts/frontier-intelligence-refresh.sh

## Plugin references (9)
- plugins/pantheon/references/12-phases-spec.md
- plugins/pantheon/references/35-deliverables-catalog.md
- plugins/pantheon/references/adversarial-gate-protocol.md
- plugins/pantheon/references/ethics-disclaimer.md
- plugins/pantheon/references/installation-guide.md
- plugins/pantheon/references/pantheon-state-schema.json
- plugins/pantheon/references/persona-doctrines.md
- plugins/pantheon/references/threat-actor-matrix-8-profiles.md
- plugins/pantheon/references/troubleshooting.md

## Utility scripts (6)
- plugins/pantheon/scripts/compliance-mapper.py
- plugins/pantheon/scripts/generate-deliverables.py
- plugins/pantheon/scripts/init-pantheon-dir.sh
- plugins/pantheon/scripts/release-sign.sh
- plugins/pantheon/scripts/threat-actor-evaluator.py
- plugins/pantheon/scripts/validate-finding-format.py

## Skill SKILL.md files (16)
- plugins/pantheon/skills/pantheon-adversarial-judge/SKILL.md
- plugins/pantheon/skills/pantheon-agent-teams-orchestration/SKILL.md
- plugins/pantheon/skills/pantheon-asvs-l3-audit/SKILL.md
- plugins/pantheon/skills/pantheon-codebase-maturity/SKILL.md
- plugins/pantheon/skills/pantheon-compliance-mapper/SKILL.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/SKILL.md
- plugins/pantheon/skills/pantheon-deliverables-generator/SKILL.md
- plugins/pantheon/skills/pantheon-finding-format/SKILL.md
- plugins/pantheon/skills/pantheon-formal-verif-candidates/SKILL.md
- plugins/pantheon/skills/pantheon-mcp-tool-integrity/SKILL.md
- plugins/pantheon/skills/pantheon-mexican-data-protection/SKILL.md
- plugins/pantheon/skills/pantheon-npm-supply-chain/SKILL.md
- plugins/pantheon/skills/pantheon-orchestrator/SKILL.md
- plugins/pantheon/skills/pantheon-red-team-simulation/SKILL.md
- plugins/pantheon/skills/pantheon-supply-chain-slsa/SKILL.md
- plugins/pantheon/skills/pantheon-threat-model/SKILL.md

## Skill reference files (39, real ### File: sections)
- plugins/pantheon/skills/pantheon-adversarial-judge/references/cross-examination-protocol.md
- plugins/pantheon/skills/pantheon-adversarial-judge/references/false-positive-patterns.md
- plugins/pantheon/skills/pantheon-agent-teams-orchestration/references/agent-team-manifest-schema.md
- plugins/pantheon/skills/pantheon-agent-teams-orchestration/references/message-passing-contract.md
- plugins/pantheon/skills/pantheon-asvs-l3-audit/references/asvs-v5-l3-checklist.md
- plugins/pantheon/skills/pantheon-asvs-l3-audit/references/owasp-top10-2021.md
- plugins/pantheon/skills/pantheon-codebase-maturity/references/13-dimensions-rubric.md
- plugins/pantheon/skills/pantheon-compliance-mapper/references/18-frameworks-catalog.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/constant-time-checklist.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/jwt-attack-vectors.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/key-management-lifecycle.md
- plugins/pantheon/skills/pantheon-crypto-deep-dive/references/post-quantum-readiness.md
- plugins/pantheon/skills/pantheon-finding-format/references/cvss-v4-vector-builder.md
- plugins/pantheon/skills/pantheon-finding-format/references/exploitation-difficulty-rubric.md
- plugins/pantheon/skills/pantheon-finding-format/references/tob-format-spec.md
- plugins/pantheon/skills/pantheon-formal-verif-candidates/references/cryptol-templates.md
- plugins/pantheon/skills/pantheon-formal-verif-candidates/references/invariant-discovery.md
- plugins/pantheon/skills/pantheon-formal-verif-candidates/references/tla-spec-patterns.md
- plugins/pantheon/skills/pantheon-mcp-tool-integrity/references/attestmcp-attestation-pattern.md
- plugins/pantheon/skills/pantheon-mcp-tool-integrity/references/mcp-cve-catalog.md
- plugins/pantheon/skills/pantheon-mcp-tool-integrity/references/vigil-verify-before-commit.md
- plugins/pantheon/skills/pantheon-mexican-data-protection/references/arco-objection-rights.md
- plugins/pantheon/skills/pantheon-mexican-data-protection/references/cnbv-cuifpes-2026.md
- plugins/pantheon/skills/pantheon-mexican-data-protection/references/lfpdppp-2025-articles.md
- plugins/pantheon/skills/pantheon-mexican-data-protection/references/sabg-complaint-workflow.md
- plugins/pantheon/skills/pantheon-npm-supply-chain/references/cross-registry-pinning-spec.md
- plugins/pantheon/skills/pantheon-npm-supply-chain/references/lockfile-policy.md
- plugins/pantheon/skills/pantheon-npm-supply-chain/references/shai-hulud-iocs.md
- plugins/pantheon/skills/pantheon-orchestrator/references/agent-reliability-axes.md
- plugins/pantheon/skills/pantheon-red-team-simulation/references/adversary-emulation-library.md
- plugins/pantheon/skills/pantheon-red-team-simulation/references/mitre-attack-mapping.md
- plugins/pantheon/skills/pantheon-red-team-simulation/references/tiber-eu-framework.md
- plugins/pantheon/skills/pantheon-supply-chain-slsa/references/sbom-cyclonedx-template.md
- plugins/pantheon/skills/pantheon-supply-chain-slsa/references/sigstore-integration.md
- plugins/pantheon/skills/pantheon-supply-chain-slsa/references/slsa-levels-spec.md
- plugins/pantheon/skills/pantheon-threat-model/references/attack-tree-patterns.md
- plugins/pantheon/skills/pantheon-threat-model/references/linddun-privacy.md
- plugins/pantheon/skills/pantheon-threat-model/references/pasta-7-stages.md
- plugins/pantheon/skills/pantheon-threat-model/references/stride-per-element.md

## Deliverable templates (35: 13 explicit + 22 via resolution rule)
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/01-executive-summary.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/02-findings-detail.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/03-threat-model.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/04-asvs-checklist.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/05-crypto-audit.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/06-formal-verif-candidates.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/07-supply-chain-slsa.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/08-red-team-narrative.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/09-codebase-maturity.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/10-compliance-matrix.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/11-adversarial-gate-log.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/12-recommendations.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/13-launch-decision.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/14-incident-response-runbook.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/15-tabletop-scenarios.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/16-monitoring-detections.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/17-secure-sdlc-rubric.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/18-architecture-review.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/19-data-flow-diagram.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/20-attack-surface-map.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/21-poc-repository.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/22-ninety-day-roadmap.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/23-sandbox-attestation-report.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/24-mcp-tool-integrity-report.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/25-cnsa-2-0-readiness-matrix.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/26-transparency-controls-report.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/27-eu-send-model-card.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/28-edge-device-attestation-report.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/29-cross-registry-pinning.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/30-secure-enclave-audit.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/31-dora-register-of-information.xbrl-xml
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/32-cra-conformity-evidence-pack.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/33-lfpdppp-2025-readiness.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/34-fintech-law-2-0-readiness.md
- plugins/pantheon/skills/pantheon-deliverables-generator/templates/35-source-track-attestation.md

## Repo docs (8)
- docs/adversarial-gate-explained.md
- docs/architecture.md
- docs/comparison-with-other-tools.md
- docs/deliverables-walkthrough.md
- docs/how-pantheon-works.md
- docs/installation.md
- docs/persona-deep-dive.md
- docs/research-provenance.md

## Examples (3)
- examples/sample-audit-output-README.md
- examples/sample-finding.md
- examples/sample-state.json

## Plugin README (1)
- plugins/pantheon/README.md

## CI configs (8, Sprint 2 supply-chain remediation per PANTHEON-0005)
- .github/workflows/security.yml
- .github/workflows/codeql.yml
- .github/workflows/scorecard.yml
- .semgrep/pantheon-custom-rules.yml
- .gitleaks.toml
- .pre-commit-config.yaml
- bandit.yaml
- markdownlint.json

## Reconciliation
9 + 2 + 11 + 10 + 9 + 9 + 6 + 16 + 39 + 35 + 8 + 3 + 1 + 8 = 166

CC validates `find . -type f | sort | uniq | wc -l` equals 156 before declaring complete. Any deviation halts with MANIFEST_ERROR. Content for templates 01-22 and any reference lacking an explicit `### File:` section resolves via Subsection 0.7 (Section 5.6 Finding extraction or category contract). Note: skill reference file names reflect the real `### File:` sections in this document. Some v5.0 frontier references (for example CNSA matrix, Digital Omnibus timeline) extract their content from the corresponding Section 5.6 Finding per the resolution rule.

PANTHEON v1.0.0 manifest. Authoritative for v1.0.0.

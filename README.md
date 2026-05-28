# PANTHEON

> A multi-persona adversarially gated security audit workflow for Claude Code.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-2.1.144%2B-orange)](https://claude.com/claude-code)
[![Status](https://img.shields.io/badge/status-research%20preview-red)](#status)

PANTHEON convenes eight public-methodology-inspired security audit personas (Trail of Bits, NCC Group, Bishop Fox, Cure53, Latacora, Project Zero, Galois, Mudge holistic) to operate in parallel over a single codebase. Twelve-phase workflow, persistent state across sessions, adversarial gate verification, compliance auto-mapping to eighteen frameworks, and thirty-five auto-generated deliverables.

This is the security audit infrastructure that previously required a $50M multi-year engagement with three concurrent tier-1 consultancies.

## Why PANTHEON exists

The security audit market operates in two tiers separated by an unreasonable price differential. Tier-S engagements with firms such as Trail of Bits, NCC Group, or Bishop Fox cost between $500K and $5M per audit, take months to schedule, and require dedicated person-quarters of human auditor time. Tier-C automation (SAST and DAST scanners, npm audit, Snyk Code) costs a few hundred dollars per developer per year and runs in minutes, but its findings rate of true positives is low and its coverage of cryptographic, supply-chain, and threat-model concerns is shallow. The gap between these tiers is wide and most organizations land in it.

Mid-stage startups, scale-ups, and even some enterprises cannot afford tier-S but need more than tier-C. They need the methodology rigor of a Trail of Bits engagement applied to a scope that fits a quarterly budget. They need defensible findings, threat models, and compliance mappings that an inspector or acquirer will accept. They need their security engineering staff augmented, not replaced, by a system that does the labor-intensive parts of audit preparation, finding triage, and deliverable generation.

The 2025 CNBV inspection cycle in Mexico fined three institutions a combined MXN 185M not for policy gaps but for evidence-absence: they had policies but could not produce defensible technical findings, threat models, and compliance mappings on demand. PANTHEON is built for that gap.

PANTHEON is AI-augmented infrastructure for elite methodology. It does not replace human judgment but it reduces the labor cost of applying tier-S methodology by orders of magnitude. The architecture is not "Claude with a security prompt". It is 11 specialized sub-agents (each running Opus 4.7 max), an adversarial gate that cross-examines every finding, compliance auto-mapping to 18 frameworks, and 35 auto-generated deliverables. Multi-persona structural rigor.

## What PANTHEON is NOT

- PANTHEON is NOT a replacement for human pentesters. The personas reason about exploitability; they do not actually run exploits. Live exploitation requires human operators with scope authorization.
- PANTHEON is NOT a generator of formal proofs. The galois-formal-verif persona identifies candidates for formal verification and provides effort estimates. Machine-checked proofs require dedicated person-months in tools like Coq, Lean 4, F*, or TLA+.
- PANTHEON is NOT a compliance attestation issuer. It produces compliance mappings with article-level citations, but attestation (SOC 2 Type II, ISO 27001, PCI DSS Report on Compliance) requires accredited human auditors.
- PANTHEON is NOT an autonomous attacker. The bishop-fox-red-team persona reasons about attack chains. Actual red team operations require authorization, scope letters, and human operators.
- PANTHEON is NOT a substitute for security engineering staff. It augments their work by doing rigorous audit preparation, finding triage, and deliverable generation. Strategic decisions stay with humans.
- PANTHEON is NOT regulatory advice. Compliance citations are technical mappings, not legal opinions. Consult counsel for regulatory interpretation.

## Quick start

```bash
# 1. Add marketplace
/plugin marketplace add alehnzgarcia7-crypto/pantheon-audit
# Expected: "Marketplace added successfully"

# 2. Install plugin
/plugin install pantheon@pantheon-audit
# Expected: "Plugin pantheon installed"

# 3. Reload plugins
/reload-plugins
# Expected: "Plugins reloaded. 1 plugin enabled: pantheon@pantheon-audit"

# 4. Start an audit
/pantheon:start "Audit of my fintech API for production readiness"
# Expected: PANTHEON orchestrator begins phase 0 dialogue
```

The first invocation creates a `.pantheon/` directory in the workspace root. Subsequent sessions automatically resume from the saved state.

## The eight personas

| Persona | Primary doctrine source | Signature focus |
|---|---|---|
| trail-of-bits-auditor | Trail of Bits public reports, ToB skills marketplace | Invariant-driven crypto and protocol depth, PoC-first findings |
| ncc-group-auditor | NCC Group whitepapers and research blog | Cryptographic and protocol implementation review |
| bishop-fox-red-team | Bishop Fox methodology pages, Cosmos AI research | Adversarial attack chains, T5 to T8 threat actor emulation |
| cure53-web-app | Cure53 public audit reports | Web application security, XSS variants, browser-attack surfaces |
| latacora-pragmatic | Latacora blog and posts | Pragmatic minimum cryptography, secure defaults |
| galois-formal-verif | Galois Inc publications | Formal verification candidate identification, Cryptol and TLA+ harnesses |
| mudge-holistic | L0pht and Mudge's historical work | Whole-systems thinking, organizational maturity |
| project-zero-researcher | Google Project Zero blog | Memory-safety bugs, novel bug-class discovery, exploit theory |

The eleventh agent (compliance-mapper) is not a persona but a verifier that auto-maps findings to 18 frameworks. The tenth (adversarial-judge) cross-examines each finding before it enters the canonical record. The first (pantheon-orchestrator) plans and dispatches.

## The twelve phases

Canonical numbering per `plugins/pantheon/references/12-phases-spec.md`. Phases 0-11 sequential by default; phase 12 generates final deliverables.

| Phase | Name | Primary personas | Output |
|---|---|---|---|
| 0 | Kickoff | orchestrator | sow.md, threat-actor-profile.md |
| 1 | Architecture Review | mudge-holistic, latacora-pragmatic | architecture-review.md |
| 2 | Strategic Threat Model | mudge-holistic, project-zero-researcher | strategic-threat-model.md |
| 3 | ASVS L3 Audit | trail-of-bits, ncc-group, cure53 (parallel) | asvs-findings.md |
| 4 | Crypto Deep Dive | trail-of-bits, galois-formal | crypto-validation.md |
| 5 | Formal Verif Candidates | galois-formal | formal-verif-roadmap.md |
| 6 | SAST/DAST/SCA Coverage | trail-of-bits, ncc-group | automated-coverage.md |
| 7 | Property-Based Fuzzing | trail-of-bits, galois-formal | fuzzing-strategy.md |
| 8 | Supply Chain SLSA | latacora-pragmatic | supply-chain-report.md |
| 9 | Red Team Simulation | bishop-fox, project-zero | red-team-report.md |
| 10 | Compliance Mapping | compliance-mapper | compliance-matrix.md |
| 11 | Adversarial Cross-Verification | adversarial-judge | cross-verification.md |
| 12 | Final Deliverables | orchestrator + all personas | 35 deliverables in `~/Downloads/pantheon-audit-<uuid>/` |

## The thirty-five deliverables

| Number | Name | One-line description |
|---|---|---|
| 01 | Executive Summary | One-page senior-stakeholder summary |
| 02 | Findings Detail | All findings, Trail of Bits format, PANTHEON-NNNN IDs |
| 03 | Threat Model | STRIDE per element, LINDDUN privacy, PASTA stages |
| 04 | ASVS L3 Checklist | OWASP ASVS v5.0 Level 3 coverage |
| 05 | Crypto Audit | Constant-time, key lifecycle, JWT, PQ-readiness |
| 06 | Formal Verification Candidates | TLA+ / Cryptol / F* targets with effort estimates |
| 07 | Supply Chain SLSA | SBOM, attestations, SLSA level evidence |
| 08 | Red Team Narrative | Adversary emulation library mapped to MITRE ATT&CK |
| 09 | Codebase Maturity | 13-dimension rubric with measurable scores |
| 10 | Compliance Matrix | 18-framework citations per finding |
| 11 | Adversarial Gate Log | All gate verdicts with reasoning |
| 12 | Recommendations | Strategic remediation roadmap |
| 13 | Launch Decision | Go/no-go memo for engineering leadership |
| 14 | Incident Response Runbook | Findings-driven IR playbooks |
| 15 | Tabletop Scenarios | Exercises from threat model and red team |
| 16 | Monitoring Detections | Sigma and elastic-rule equivalents |
| 17 | Secure SDLC Rubric | Maturity assessment of SDLC controls |
| 18 | Architecture Review | C4 model views with risk overlays |
| 19 | Data Flow Diagram | DFD with trust boundaries |
| 20 | Attack Surface Map | External, internal, and physical surfaces |
| 21 | PoC Repository | PoCs (sanitized) for accepted findings |
| 22 | Ninety-Day Roadmap | Prioritized fixes with effort sizing |
| 23 | Sandbox Attestation Report | Containment evidence for AI workloads |
| 24 | MCP Tool Integrity Report | Findings on connected MCP servers |
| 25 | CNSA 2.0 Readiness Matrix | NSA post-quantum deadlines per primitive |
| 26 | Transparency Controls Report | Disclosure and explainability evidence |
| 27 | EU SEND Model Card | SEND-compliant model card |
| 28 | Edge Device Attestation Report | Hardware-rooted attestation evidence |
| 29 | Cross-Registry Pinning | npm and registry pinning policy |
| 30 | Secure Enclave Audit | TEE/SGX/SEV-SNP review |
| 31 | DORA Register of Information | XBRL-XML register for EU DORA |
| 32 | CRA Conformity Evidence Pack | EU Cyber Resilience Act evidence |
| 33 | LFPDPPP 2025 Readiness | Mexican federal data protection readiness |
| 34 | Fintech Law 2.0 Readiness | Mexican Fintech Law evolution readiness |
| 35 | Source Track Attestation | SLSA v1.2 source-track evidence |

## Architecture

```
User
 |
 v
/pantheon:start
 |
 v
[pantheon-orchestrator]  <--reads/writes-->  .pantheon/state.json
 |     ^
 | dispatch
 v     |
[11 sub-agent personas] --findings--> [adversarial-judge] --ACCEPT--> [compliance-mapper]
                                          |                                  |
                                          v                                  v
                                       REVISE/WITHDRAW/DISPUTE          18-framework citations
                                          |                                  |
                                          v                                  v
                                       state.json                       state.json

After all 12 phases:

state.json --> [pantheon-deliverables-generator] --> 35 deliverables in ~/Downloads/pantheon-audit-<uuid>/
```

See `docs/architecture.md` for the deep dive.

## Comparison with existing tools

| Capability | PANTHEON | ToB skills | Anthropic security-guidance | /ultrareview | codex-plugin-cc | Snyk Code | GHAS |
|---|---|---|---|---|---|---|---|
| Multi-persona orchestration | Yes (8) | No | No | No | No | No | No |
| Adversarial gate | Yes | No | No | No | Limited | No | No |
| Compliance auto-mapping | Yes (18 frameworks) | No | No | No | No | No (partial) | No |
| Deliverable count | 35 | None | None | Inline | Inline | Scan only | Scan only |
| State persistence | Yes (state.json) | No | Limited | No | No | Yes | Yes |
| Threat-led testing | Yes | Yes (per-skill) | No | No | No | No | No |
| Formal verification candidates | Yes | No | No | No | No | No | No |
| Methodology source diversity | 8 firms | Trail of Bits only | Anthropic | None | None | None | None |

PANTHEON is not always better. Snyk has a strong SCA database. GHAS has CodeQL queries. The differentiator is multi-persona orchestration plus adversarial gate plus compliance auto-mapping in one tool. See `docs/comparison-with-other-tools.md` for the full version.

## Installation

Prerequisites:
- Claude Code 2.1.144 or later
- Opus 4.7 access via Max plan or API
- Write access to your workspace root (PANTHEON creates `.pantheon/`)
- Write access to `~/Downloads/` (PANTHEON writes deliverables there)

```bash
/plugin marketplace add alehnzgarcia7-crypto/pantheon-audit
/plugin install pantheon@pantheon-audit
/reload-plugins
```

Install only from `alehnzgarcia7-crypto/pantheon-audit`. Reject look-alike names: `pantheon-pro`, `pantheon-audit-pro`, `pantheon-audit-plus`, `panthe0n-audit`, regional variants like `pantheon-audit-mx`. Verify release bundles with `cosign verify-blob` per the `SECURITY.md` policy. Typosquatting awareness detail is in `docs/installation.md`.

First-run initialization creates the `.pantheon/` scaffold (auto-appended to `.gitignore`). See `docs/installation.md` for the troubleshooting walkthrough, the cloud-sync warning, and the full typosquatting list.

## Usage patterns

Pattern 1: Pre-merge MP audit. Before merging a large feature branch, run a focused audit on the new code.

```bash
/pantheon:start "audit of MP-15 connector layer changes"
```

Expected duration: 2-4 sessions on Opus 4.7 max.

Pattern 2: Regulatory compliance check. CNBV or similar regulator inspection in 30 days; need defensible technical evidence.

```bash
/pantheon:start "CNBV regulatory inspection preparation, fintech, scope: full backend"
```

Expected duration: 1-2 weeks of audit work.

Pattern 3: Deep crypto review. Suspect a cryptographic implementation may be incorrect; want trail-of-bits plus galois-formal coverage.

```bash
/pantheon:start "cryptographic deep dive of src/crypto/"
```

Expected duration: 3-5 sessions.

## Configuration

Customization points:
- Adding a new persona: see `CONTRIBUTING.md` for the file structure required.
- Adding a custom compliance framework: see `plugins/pantheon/skills/pantheon-compliance-mapper/references/18-frameworks-catalog.md`.
- Adjusting persona dispatches: orchestrator reads `sow.md` industry field for domain-specific variations.
- Output language: pass `output language: Spanish` (or other) in `/pantheon:start` prompt.
- Token budget control: phase-level turn budgets configurable via `state.json.budget_overrides`.

Most users will not need to customize. The defaults are designed for full-rigor audits.

## State management

`.pantheon/state.json` is the audit's source of truth. It survives session restart.

- Schema version 1.0.0. Schema in `plugins/pantheon/references/pantheon-state-schema.json`.
- `/pantheon:resume` reads `state.json` and continues from the last completed phase.
- `/pantheon:reset` asks for explicit confirmation before deleting state. This is the only way to delete state.
- State backups: `.pantheon/state.json.backup` (maintained by Stop hook), `.pantheon/state.json.precompact.<timestamp>` (maintained by PreCompact hook).
- If `state.json` corrupts, recovery from backups; PANTHEON does not silently regenerate.

## Output language

Plugin source is English (international standard for security tools). Findings can be produced in any language by passing `output language: <language>` in `/pantheon:start`. The personas adapt to the requested language while maintaining technical accuracy. Compliance framework citations remain in their original language (CNBV in Spanish, GDPR in English official translation, and so on).

The personas are not equally fluent in all languages. English produces the most consistent quality. Spanish produces high quality. Other languages may have variable quality depending on training data coverage.

## Cost considerations

| Audit scope | Input tokens | Output tokens | Approximate Max sessions |
|---|---|---|---|
| Quick (single MP, <20K LoC) | 100-300K | 50-150K | 1-2 |
| Medium (50-200K LoC, full backend) | 500K-1.5M | 250-750K | 5-10 |
| Large (full enterprise codebase, all 12 phases comprehensive) | 2M-5M+ | 1-3M+ | 20+ |

Caveats:
- Claude Max plan provides usage-based access. Heavy audits can hit rate limits.
- Opus 4.7 with effort max is the assumption. Lower effort or Sonnet would reduce token usage but is not supported by PANTHEON (Opus 4.7 max is a hard requirement).
- Token estimates vary widely based on codebase complexity, finding count, and persona dispatch parallelism.
- Budget 1.5x the estimate for the first audit on an unfamiliar codebase.

The Max plan with Opus 4.7 is the recommended configuration. The tokenizer changed from Opus 4.6 to 4.7, so token counts for the same content differ slightly between versions.

## Ethics and responsible disclosure

PANTHEON is for auditing systems you own or have explicit written authorization to audit. Using PANTHEON on systems without authorization is unauthorized access and likely illegal.

If PANTHEON identifies a vulnerability in a third-party system you do not own (for example, in a dependency), follow responsible disclosure: contact the maintainer privately, allow reasonable time for remediation (90 days is industry standard, derived from Project Zero policy), publish only after coordinated disclosure or unreasonable delay.

Findings generated by PANTHEON are NOT public until you choose to publish them. They live in `.pantheon/` on your workspace. Treat them as sensitive (they are exploitation guidance until remediated).

If your audit subject is a multi-party system (your code plus your vendor's code plus your customer's data), notify affected parties before publishing or sharing PANTHEON output that touches their assets.

See `plugins/pantheon/references/ethics-disclaimer.md` for the full ethical-use policy.

## Limitations and known issues

- Token usage is high. A full 12-phase audit on a large codebase can consume 5M+ tokens. Users on lower-tier plans will hit rate limits.
- The adversarial-judge can WITHDRAW true positives that are novel (the seven-question protocol requires PoC, which is harder to construct for genuinely novel bug classes). Mitigation: PANTHEON flags DISPUTE for novel findings and surfaces them to the user.
- Compliance mappings require verification for jurisdiction-specific edge cases. The compliance-mapper produces citations with confidence scores; low-confidence citations (mapping_confidence < 0.7) require manual review.
- State JSON can grow large for big audits (10MB+ for 500+ findings). The compaction hook reduces but does not eliminate growth.
- The personas are LLM-based and exhibit stochasticity. Two runs of the same audit may produce 80-90% overlapping findings, not 100%. The meta-audit (section 0.5.4 of the build spec) helps quantify this.
- Compliance framework versions are point-in-time. Regulations change. The 18-frameworks-catalog.md must be maintained. Stale citations are a risk.
- PANTHEON does not currently integrate with external tools (CodeQL, Semgrep, npm audit). Roadmap v1.1 will add MCP server integration.
- Self-audit (PANTHEON auditing its own source) has a high false-positive rate. The plugin is metadata, not application code; the personas can produce findings that do not apply.

## Roadmap

v1.0 (this release): the foundation. 11 sub-agents, 12 phases, 35 deliverables, 18 compliance frameworks, adversarial gate, meta-cognitive loops.

v1.1 (planned Q3 2026): MCP server integration. Personas can dispatch CodeQL queries, Semgrep rules, npm audit, gitleaks. External tool output becomes input to the gate review.

v1.2 (planned Q1 2027): live red team mode with sandboxed adversary emulation. The bishop-fox persona can construct PoCs in a sandboxed environment for empirical verification.

v2.0 (research goal, 2027+): formal verification via embedded TLA+ and Cryptol harness. The galois persona can produce machine-checked proofs for narrow scope (cryptographic primitives, state-machine correctness) within session.

These are research goals, not promises. The roadmap depends on Claude Code platform capabilities, Anthropic API features, and user feedback.

## Contributing

See `CONTRIBUTING.md`. PANTHEON has strict standards because its output is consumed in legal, regulatory, and acquisition contexts. New personas must represent actual public methodologies. New compliance framework mappings must have public technical specifications. New deliverable templates must justify the gap from the existing 22.

## Status

Research preview. Plugin features, pricing, and availability may change. Tested with Claude Code 2.1.144 and Opus 4.7. Tested workflows: pre-merge MP audit (fintech), regulatory compliance preparation (Mexican fintech CNBV), and deep crypto review (custom JWT implementation). Report issues and feature requests via GitHub Issues.

## Credits

Methodology sources:
- Trail of Bits public audit reports and trailofbits/skills marketplace
- NCC Group research blog and public whitepapers
- Bishop Fox methodology pages and Cosmos AI research
- Cure53 public audit reports
- Latacora blog and public posts
- Galois Inc publications
- Google Project Zero blog
- L0pht and Mudge's historical work
- Anthropic security-guidance plugin (hooks patterns)

Individual researchers whose work informed persona doctrines: Tavis Ormandy, Natalie Silvanovich, Samuel Groß, Maddie Stone, Peiter "Mudge" Zatko, Daniel Bernstein, Theo de Raadt, Bryan Cantrill, Thomas Ptacek, Mario Heiderich.

Frameworks and standards: OWASP, MITRE, NIST, ISO, CNBV, CNPDP-Mexico, EU regulatory bodies, AICPA.

Anthropic for the Claude Code platform and the Opus 4.7 model that powers all personas.

None of the cited firms or individuals have endorsed PANTHEON. PANTHEON references their public methodologies as inspiration; the responsibility for PANTHEON's output is the maintainer's, not theirs.

## License

MIT. See LICENSE file.

## Author

Alex (@nexogeopo). GitHub: [alehnzgarcia7-crypto](https://github.com/alehnzgarcia7-crypto).

# PANTHEON STATUS

Project handoff document. Read this first when resuming work on `pantheon-audit` in a new session.

Last updated: 2026-05-29.

---

## 1. Current state

| Field | Value |
|---|---|
| Version | v1.0.0 |
| Main commit (post-Sprint-4 merge) | `13872e0` |
| Re-audit verdict | **LAUNCH DECISION: GO** |
| Re-audit ID | `42892f54-48a7-4a2e-b1a2-74bf9988d16c` |
| Baseline audit ID | `8407227c-6a16-44fc-8810-82e2012a6eb7` |
| Baseline verdict | NO_GO (snapshot pre-remediation) |
| Findings remediated from baseline | 14 of 14 trackable (12 strict-closed + 2 partial-shifted to adjacent layer) |
| Strict regressions | 0 |
| Sprints completed | 1, 2 (+2.1 hotfix), 3, 4 |
| File count | 166 (was 165 before this handoff doc) |
| License | MIT |
| Maintainer | Alex (@nexogeopo, GitHub `alehnzgarcia7-crypto`) |

Re-audit was deliberately independent: it audited the current source from scratch without consulting baseline findings except in the final Phase 11 cross-check. The result is a NET POSITIVE diff with risk register reduction of approximately USD 140,000 annualized (49%).

---

## 2. Architecture

### Plugin overview

PANTHEON is a Claude Code plugin that orchestrates a high-assurance security audit workflow. It does NOT run live exploits; it reasons about exploitability through code review and dispatches multiple persona perspectives in parallel.

### Sub-agents (11 total)

Located at `plugins/pantheon/agents/`:

| Agent | Role |
|---|---|
| `pantheon-orchestrator` | Master coordinator; dispatches all other personas; manages state.json |
| `adversarial-judge` | Seven-question cross-examination gate; produces ACCEPT/REVISE/WITHDRAW/DISPUTE verdicts |
| `trail-of-bits-auditor` | Line-by-line crypto/protocol depth |
| `ncc-group-auditor` | Threat-intelligence-led, regulatory framework awareness |
| `bishop-fox-red-team` | Attack chain construction, MITRE ATT&CK mapping |
| `cure53-web-app` | Web/mobile/browser internals |
| `latacora-pragmatic` | Pragmatic AppSec, embedded perspective |
| `project-zero-researcher` | Memory-safety, novel bug classes, PoC depth |
| `galois-formal-verif` | Formal verification candidate identification |
| `mudge-holistic` | Whole-systems thinking, organizational maturity |
| `compliance-mapper` | 18-framework + 12-auxiliary citation mapping |

All sub-agents use `model: opus`, `effort: max`. All 11 contain the PANTHEON-0013 boundary clause appended at end-of-body.

### Twelve phases (canonical)

Per `plugins/pantheon/references/12-phases-spec.md`. Aligned in README.md table during Sprint 4 (PANTHEON-0006 fix):

| # | Phase | Primary personas |
|---|---|---|
| 0 | Kickoff | orchestrator |
| 1 | Architecture Review | mudge-holistic + latacora-pragmatic |
| 2 | Strategic Threat Model | mudge-holistic + project-zero-researcher |
| 3 | ASVS L3 Audit | trail-of-bits + ncc-group + cure53 (parallel) |
| 4 | Crypto Deep Dive | trail-of-bits + galois-formal |
| 5 | Formal Verif Candidates | galois-formal |
| 6 | SAST/DAST/SCA Coverage | trail-of-bits + ncc-group |
| 7 | Property-Based Fuzzing | trail-of-bits + galois-formal |
| 8 | Supply Chain SLSA | latacora-pragmatic |
| 9 | Red Team Simulation | bishop-fox + project-zero |
| 10 | Compliance Mapping | compliance-mapper |
| 11 | Adversarial Cross-Verification | adversarial-judge |
| 12 | Final Deliverables | orchestrator + all |

Phases 4, 5, 7 are typically marked `skipped` when the audit subject has no application crypto, no formal-verification surface, and no application fuzzing surface. The orchestrator records skip justifications in state.json.

### CI pipeline (Sprint 2 / 2.1 / 3 / 4)

`.github/workflows/security.yml` runs on push to main, pull_request to main, weekly schedule, and workflow_dispatch. Six jobs in parallel plus PR comment aggregator:

| Job | Tool | Threshold |
|---|---|---|
| Secrets | gitleaks 8.21.2 | 0 secrets allowed |
| SAST | semgrep 1.152.0 (custom + p/ci + p/security-audit + p/secrets) | 0 ERROR allowed |
| SAST | bandit 1.8.0 with `[sarif]` extra, severity HIGH+MEDIUM gate | 0 HIGH or MEDIUM |
| SAST | shellcheck (apt) | 0 errors and 0 warnings |
| Lint | markdownlint-cli2 0.14.0 | 0 issues |
| Style | inline grep | 0 em-dash, 0 AI sig, 11/11 persona boundary |

Sidecar workflows: `codeql.yml` (workflow_dispatch + schedule, graceful skip on private repo without GHAS), `scorecard.yml` (publish_results=false, artifact only).

All actions SHA-pinned to Node 24-compatible majors. Step-Security Harden-Runner v2.19.4 on every job. Concurrency cancel-in-progress on non-main refs. SHA-pin SHA list captured in commit messages of Sprint 2.1 and Sprint 4.

### Branch protection

`main` is protected with: require pull request before merge, require signed commits, require status checks to pass. All four of the Sprint 2/3/4 PRs were merged through this gate. Maintainer applied via GitHub Settings → Branches (PANTHEON-0002 baseline closure).

---

## 3. Signing configuration (CRITICAL: read this if commits start failing)

### Local config (per-repo, not global)

`.git/config` (effective via `git config --local`):

```
[commit]
    gpgsign = true
[gpg]
    format = ssh
[user]
    signingkey = /Users/alex/.ssh/pantheon_signing.pub
[gpg "ssh"]
    allowedSignersFile = /Users/alex/.config/git/allowed_signers
```

### Key locations

- **Private key (operational)**: `~/.ssh/pantheon_signing` (mode 600, FileVault-protected)
- **Private key (backup)**: maintainer's password manager (entry titled `pantheon-audit signing key (ed25519)`)
- **Public key**: `~/.ssh/pantheon_signing.pub`
- **Public key registered**: GitHub Settings → SSH and GPG keys → Signing keys (type SIGNING, not authentication)
- **Public key fingerprint**: `SHA256:OcFWU7wSxPiy+qAIOyy/JUDurgHQW1RMYr67wO1vlkM`

### Allowed signers (for local `git log --show-signature`)

`~/.config/git/allowed_signers`:

```
255492989+alehnzgarcia7-crypto@users.noreply.github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFAXo5nNO+Hp2QDs96nL4YiS9h7/JkaPhwP5xNqx3QMT
```

### Recovery if commits get blocked by branch protection

If `git push` returns rejected with `Commits must have verified signatures`:

```bash
# Re-sign the last commit and force-push
git commit --amend --no-edit -S
git push --force-with-lease

# Verify via GitHub API
gh api repos/alehnzgarcia7-crypto/pantheon-audit/commits/$(git rev-parse HEAD) \
  --jq '.commit.verification | {verified, reason}'
# Expected: {"verified": true, "reason": "valid"}
```

If multiple commits are unsigned, rebase-sign:

```bash
git rebase --exec 'git commit --amend --no-edit -S' main
git push --force-with-lease
```

If GitHub still rejects with `bad_cert` or `unverified`: verify the SSH public key is still registered at https://github.com/settings/ssh/new (Signing keys section). The key may have been accidentally deleted; re-register from the `.pub` file or restore from the password manager backup.

### Key revocation (if compromise suspected)

1. Delete the key from GitHub Settings → SSH and GPG keys → Signing keys.
2. Generate a replacement: `ssh-keygen -t ed25519 -C "alex@pantheon-audit signing key v2" -f ~/.ssh/pantheon_signing_v2`.
3. Upload new public to GitHub as a new Signing key.
4. Update `~/.config/git/allowed_signers` with the new key fingerprint.
5. Update `git config --local user.signingkey ~/.ssh/pantheon_signing_v2.pub`.
6. File a GitHub Security Advisory if any release artifacts were signed with the compromised key during the suspected window.
7. Update SECURITY.md disclosure timeline if the compromise is publicly material.

---

## 4. Open findings (re-audit Sprint 5 backlog, optional)

Ten findings ratified by the re-audit, none Critical, none High. They are the natural deeper-layer surface exposed by Sprint 1-4 remediations. Closing them is optional and brings the plugin to "elite tier" maturity. Owner: the maintainer.

### Medium (4)

| ID | Title | File |
|---|---|---|
| PANTHEON-0001 (re-audit) | MCP audit log JSONL forgery via unescaped `tool_name` interpolation | `plugins/pantheon/hooks/scripts/mcp-tool-integrity-check.sh:57` |
| PANTHEON-0003 (re-audit) | Custom Semgrep rule `pantheon-untrusted-path-concat` misses string-concat form | `.semgrep/pantheon-custom-rules.yml` rule 1 |
| PANTHEON-0005 (re-audit) | Release-signing pipeline not automated; cert-OIDC-issuer mismatch between docs and reality | `release-sign.sh` + `docs/installation.md` Step 2 |
| PANTHEON-0010 (re-audit) | Host instrumentation gap precludes detection of zip-swap attack during manual signing window | release flow |

### Low (6)

| ID | Title | File / area |
|---|---|---|
| PANTHEON-0002 (re-audit) | CI threshold gates rely on numeric jq output without type validation | `.github/workflows/security.yml` |
| PANTHEON-0004 (re-audit) | Missing `dependabot.yml` and `CODEOWNERS` | repo root / `.github/` |
| PANTHEON-0006 (re-audit) | Some main HEAD commits unsigned despite policy (partial regression of PANTHEON-0003 baseline) | git history |
| PANTHEON-0007 (re-audit) | SBOM not versioned as artifact; not signed via `cosign attest` | release pipeline |
| PANTHEON-0008 (re-audit) | gitleaks tarball downloaded without SHA256 verification | `.github/workflows/security.yml` gitleaks job install step |
| PANTHEON-0009 (re-audit) | Node installed via `curl ... | sudo bash` in markdownlint job | `.github/workflows/security.yml` markdownlint job |

These IDs are independent of the baseline (baseline used the same `PANTHEON-NNNN` namespace ending at 0019). The re-audit numbering restarts at 0001 with the new audit UUID as disambiguator.

---

## 5. Report bundle paths

| Audit | Output bundle | Findings | Verdict |
|---|---|---|---|
| Baseline (8407227c) | `<repo>/.pantheon-baseline-8407227c/` | 19 entries (14 accepted) | NO_GO |
| Re-audit (42892f54) | `~/Downloads/pantheon-audit-42892f54-48a7-4a2e-b1a2-74bf9988d16c/` | 10 accepted | GO |
| Re-audit diff vs baseline | `~/Downloads/pantheon-audit-42892f54-48a7-4a2e-b1a2-74bf9988d16c/36-re-audit-diff-vs-baseline.md` | side-by-side | NET POSITIVE |

Both directories are gitignored. The repo only contains source code; audit output is local-only and treated as Tier 2 sensitive per `plugins/pantheon/references/ethics-disclaimer.md`.

---

## 6. Next steps (any of these are valid; user decides which path)

### Path A: Sprint 5 (close the 10 remaining findings)

Estimated effort: 2 to 9 days of maintainer time depending on depth. Outputs:

- `release.yml` GitHub Actions workflow with OIDC keyless signing via `slsa-framework/slsa-github-generator` (closes PANTHEON-0005, 0010, 0007 re-audit)
- `dependabot.yml` + `CODEOWNERS` (closes PANTHEON-0004 re-audit)
- gitleaks/Node install steps gated by SHA256 verification (closes PANTHEON-0008, 0009 re-audit)
- jq output type validation in workflow gates (closes PANTHEON-0002 re-audit)
- `mcp-tool-integrity-check.sh` JSONL forgery fix: escape `tool_name` via `jq -n --arg name "$TOOL_NAME"` instead of `printf '...'` interpolation (closes PANTHEON-0001 re-audit)
- Semgrep rule 1 expanded with `+` concat form variants (closes PANTHEON-0003 re-audit)
- Branch protection audit to ensure no unsigned commits land on main (closes PANTHEON-0006 re-audit)

Outcome: 0 findings remaining, push toward SLSA L2/L3 and OpenSSF Scorecard 8.5+.

### Path B: Release v1.0.1

Tag with current main HEAD (post-Sprint-5 if done, else 13872e0). Run `release-sign.sh` on maintainer machine to produce `pantheon-v1.0.1.zip` and `pantheon-v1.0.1.zip.cosign.bundle`. Upload as GitHub release assets. Update marketplace.json version field. Push tag.

If Sprint 5 PANTHEON-0005 fix is in place, release is fully automated by tag push.

### Path C: Pivot to Phoenix Financial OS audit

PANTHEON v1.0.0 is production-ready as audit infrastructure. Apply it to Phoenix Financial OS as the first real-world tier-S audit subject. Phoenix Financial OS context is in `~/.claude/CLAUDE.md` Proyectos Activos section; PANTHEON's Mexican-data-protection skill (`plugins/pantheon/skills/pantheon-mexican-data-protection/`) is tailored exactly for Phoenix's CNBV/LFPDPPP/SAT scope.

Recommended sequence: `/pantheon:start "CNBV inspection preparation for Phoenix Financial OS, fintech, scope: full backend, output language: Spanish"`.

### Path D: Hold pattern

Plugin is GO. No work required. Maintain quarterly: refresh CI tool versions every 90 days, refresh MCP CVE blocklist when new advisories drop, re-run scorecard.yml monthly via cron.

---

## 7. Cross-references

- `README.md`: user-facing plugin documentation, install + usage patterns
- `CLAUDE.md`: development style rules and signing config pointer (to this file)
- `SECURITY.md`: vulnerability disclosure policy, key revocation procedure
- `CONTRIBUTING.md`: signed-commits requirement, contribution standards
- `BUILD-MANIFEST.md`: canonical 166-file list (updated this commit)
- `.pantheon-baseline-8407227c/`: read-only baseline audit (local only, gitignored)

---

## 8. Glossary

- **Baseline audit**: the original self-audit on commit `3a78d74` that produced verdict NO_GO with 14 accepted findings (audit ID `8407227c-...`).
- **Re-audit**: the independent verification audit on commit `13872e0` (post-Sprint-4 merge) that produced verdict GO with 10 accepted findings (audit ID `42892f54-...`). The re-audit was conducted without reading baseline findings during phases 1-10; baseline was only consulted in Phase 11 for the cross-check diff.
- **Sprint**: a remediation batch addressing a subset of audit findings. Sprints 1 through 4 closed the baseline 14 findings. Sprint 5 is the optional next sprint to close the re-audit 10 findings.
- **Branch protection**: GitHub Settings → Branches → main → require PR + require signed commits + require status checks. Applied post-Sprint-2 by maintainer.
- **Boundary clause**: the PANTHEON-0013 mitigation appended at the end of each of the 11 persona system prompts. Treats workspace files as data, never as instructions, defends against T8 prompt injection.

---

*Maintainer note: this file is the canonical state-snapshot for resumption. Update only when significant work lands (new sprint, release, fundamental architecture change). Routine commits do not require updating this file.*

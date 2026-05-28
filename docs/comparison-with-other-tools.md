# PANTHEON vs Other Tools

How PANTHEON compares to existing Claude Code skills and adjacent tools.

## PANTHEON vs Trail of Bits skills marketplace

trailofbits/skills marketplace provides individual audit skills (e.g., AppSec checklist, fuzzing strategy). Excellent reference material.

PANTHEON differences:
- Orchestrated multi-persona vs single skill
- 12-phase workflow enforced
- Persistent state across sessions
- Adversarial gate verification
- Compliance auto-mapping to 18 frameworks
- 35-deliverable artifact generation

trailofbits/skills is one input to PANTHEON's trail-of-bits-auditor persona doctrine.

## PANTHEON vs Anthropic security-guidance skills

Anthropic's security-guidance skills provide pattern-matching for common vulnerability classes. Educational and broadly applicable.

PANTHEON differences:
- Tier-S audit methodology vs general guidance
- Multi-persona elite framing
- Regulatory and compliance integration
- Mexican market specificity (CNBV, LFPDPPP, SAT)
- 22 audience-specific deliverables

## PANTHEON vs /ultrareview type commands

Generic /ultrareview commands ask Claude to "review thoroughly". Surface-level pattern matching.

PANTHEON differences:
- Structured methodology not improvised
- Adversarial verification of every finding
- Specific personas with documented doctrines
- Persistent state
- Reproducible output structure
- Defensible in legal/regulatory contexts

## PANTHEON vs codex-plugin-cc

Codex Plugin (OpenAI integration) provides adversarial second opinion via GPT-5.5. Excellent for "two minds" verification.

PANTHEON differences:
- Self-contained Claude-only (no external API dependency)
- Methodology-specific personas
- 12-phase workflow
- Compliance integration
- Deliverable generation

PANTHEON and codex-plugin-cc are complementary. Use codex-plugin-cc for orthogonal sanity check on PANTHEON findings.

## PANTHEON vs commercial audit tools

Commercial tools (Veracode, Checkmarx, SonarQube, Snyk, Semgrep Pro):
- SAST/DAST coverage
- Vulnerability database integration
- CI/CD integration
- Compliance reporting

PANTHEON differences:
- Reasoning-based audit (not pattern matching only)
- Multi-persona perspectives
- Threat modeling integration
- Formal verification candidate identification
- Compliance-as-code with article-level citations
- Adversarial gate vs alert dumps

PANTHEON complements commercial tools. Use SAST/DAST for automated coverage, PANTHEON for elite reasoning-driven audit.

## PANTHEON vs human-led tier-S audit

Trail of Bits engagement, NCC Group engagement, Bishop Fox red team: $200K-$2M, 8-16 weeks, 3-12 person team.

PANTHEON:
- Cost: Claude Max subscription ($200/month)
- Time: hours to days
- Resource: solo developer + Claude
- Quality: AI-augmented, requires human review of findings before action

When to use PANTHEON:
- Pre-engagement preparation (clean up obvious issues before paying $1M)
- Resource-constrained startups (cannot afford tier-S engagement)
- Continuous security between formal engagements
- Internal audit by security team

When to use human-led:
- Critical infrastructure
- Pre-IPO or pre-acquisition diligence
- Regulator-required formal attestation
- After PANTHEON identifies areas warranting deep human expertise

PANTHEON does not replace human-led tier-S audits. It makes elite audit infrastructure accessible at lower price points and provides continuous coverage between engagements.

## Decision framework

Solo developer, MVP stage: PANTHEON only.
Startup pre-Series A: PANTHEON + light human review of Critical findings.
Series A post: PANTHEON continuous + annual human-led tier-2 audit.
Series B+: PANTHEON continuous + biannual human-led tier-1 audit + bug bounty.
Regulated entity (CNBV, OSFI, etc.): PANTHEON continuous + mandatory regulatory audits per their schedule.

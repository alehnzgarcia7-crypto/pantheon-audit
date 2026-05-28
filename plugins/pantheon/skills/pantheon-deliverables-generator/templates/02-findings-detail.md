# Findings Detail
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Format**: Trail of Bits style, PANTHEON-NNNN finding IDs

## Purpose
Canonical record of every accepted finding with full reproduction detail, exploitation scenario, recommendation, and compliance mapping. Audience: engineering, security engineering, third-party validators.

## Populated from state
| Field | Source |
|---|---|
| findings | state.json/findings filtered status in {accepted, revised} |
| consensus_findings | state.json/findings where consensus_finding == true |
| disputed_findings | state.json/findings where status == disputed |

## Findings index
Table with: ID, title, severity, CVSSv4, exploitation difficulty, affected component, lead persona.

## Severity distribution
- Critical: count
- High: count
- Medium: count
- Low: count
- Informational: count

## Per-finding sections
For each finding, render the full PANTHEON-NNNN block as authored by the lead persona and accepted by the gate:
- ID, title, severity, CVSS v4 vector and score
- exploitation_difficulty
- business_impact_usd and reasoning
- threat_actors_capable (T1 to T8)
- affected_component, affected_files (path:line-line), affected_function
- first_introduced_commit
- description (2 to 4 paragraphs)
- exploitation_scenario (numbered steps)
- recommendation_short_term
- recommendation_long_term
- references
- discovered_by (one or more personas)
- gate_verdict and gate_reasoning
- compliance_mappings (18 frameworks)

## Consensus findings highlight
Findings discovered by 2+ personas. Higher baseline confidence.

## Disputed findings
Findings where the adversarial gate could not reach verdict. Flagged for human review.

## Compliance mappings cited
Each finding cites article-level controls across the 18 frameworks. Confidence per citation included.

## Hard fails (validation rules)
- Every finding MUST be in PANTHEON-NNNN format.
- Every finding MUST have at least one compliance mapping (null fields acceptable, omission is not).
- Every finding MUST cite affected_files path:line-line.
- No em-dashes.

## Signoff
Prepared by: contributing personas
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- plugins/pantheon/skills/pantheon-finding-format/SKILL.md
- plugins/pantheon/skills/pantheon-finding-format/references/tob-format-spec.md

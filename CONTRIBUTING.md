# Contributing to PANTHEON

PANTHEON has strict contribution standards because security audit output is consumed in legal, regulatory, and acquisition contexts. Errors propagate downstream.

## Before you contribute
1. Read `README.md` and relevant `docs/` files.
2. Run PANTHEON against a sample codebase end-to-end.
3. Read the persona doctrine in `plugins/pantheon/references/persona-doctrines.md`.

## Types of contributions

### New personas
Must represent actual public methodologies from named consultancies, researchers, or organizations.
1. Identify methodology source.
2. Cite at least three public references.
3. Write sub-agent in `plugins/pantheon/agents/<name>.md`.
4. Add doctrine entry to `references/persona-doctrines.md`.
5. Update orchestrator persona list.
6. Update phase-to-persona mapping if applicable.

### New compliance frameworks
1. Framework must have public technical specification.
2. Add entry to `plugins/pantheon/skills/pantheon-compliance-mapper/references/18-frameworks-catalog.md` with article-level citations.
3. Provide at least 5 example finding mappings.
4. Update mapper SKILL.md.

### New deliverable templates
1. Justify gap not covered by existing 22.
2. Identify regulatory or business audience.
3. Create template in `plugins/pantheon/skills/pantheon-deliverables-generator/templates/NN-name.md`.
4. Update orchestrator final phase logic.
5. Update `references/35-deliverables-catalog.md`.

### Bug fixes
1. Open issue first with reproduction steps.
2. PR must include test case or evidence demonstrating fix.

## Style requirements
- No em-dashes anywhere. Hard rule.
- English in plugin source.
- No marketing language.
- Sub-agent system prompts: 800 to 3000 words.
- Skill descriptions: specific activation triggers.
- Reference files: primary sources, not Wikipedia.

## Review process
1. Lint pass (markdown, JSON, YAML frontmatter)
2. Style pass (em-dash check, marketing language check)
3. Methodology pass (accuracy of persona/framework representation)
4. Self-audit pass (run PANTHEON on changes)

## License
Contributions licensed under MIT.

## Maintainer
Alex (@nexogeopo). Reviews typically within 7 days.

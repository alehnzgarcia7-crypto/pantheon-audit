# PANTHEON Troubleshooting

## Plugin does not load
- Check Claude Code version: requires 2.1.144+
- Run `/reload-plugins` after marketplace add
- Check marketplace.json valid JSON: `jq empty /path/to/pantheon-audit/.claude-plugin/marketplace.json`
- Check plugin.json valid: `jq empty /path/to/pantheon-audit/plugins/pantheon/.claude-plugin/plugin.json`

## /pantheon:start fails with permission error
- Use `claude` (plain). Approve specific safe actions when prompted. Reserve `--dangerously-skip-permissions` for disposable sandboxes only
- Ensure write access to current working directory (PANTHEON creates `.pantheon/`)

## Sub-agent dispatch fails
- Sub-agents require Opus model access
- Check `/model opus` set
- Check Claude Max subscription active

## State.json missing after compaction
- Check `.pantheon/state.json.backup`
- If exists, copy back: `cp .pantheon/state.json.backup .pantheon/state.json`
- Check `.pantheon/state.json.precompact.*` files
- Latest precompact has most recent state

## Adversarial-judge rejects all findings
- Check finding format conforms to PANTHEON-NNNN spec
- Ensure mandatory fields present
- Check PoC concrete and reproducible
- Check threat actors specified

## Compliance mapper outputs all-null
- Verify SoW captured geographic scope and industry
- Verify finding category specified
- Check `references/18-frameworks-catalog.md` accessible

## Deliverables generation stops mid-stream
- Check disk space in `~/Downloads/`
- Check `.pantheon/state.json` phases all `status: complete`
- Check all findings status accepted/withdrawn/disputed (no `draft` remaining)
- Resume via `/pantheon:resume`

## Hooks not executing
- Check executable permission on hook scripts: `chmod +x plugins/pantheon/hooks/scripts/*.sh`
- Check `jq` installed: `which jq`
- Check hooks.json valid JSON

## Em-dash in output despite hook
- Hook generates warning but does not block
- Manually fix or run grep: `grep -rn '\x{2014}' .pantheon/`

## State.json corrupted (invalid JSON)
- DO NOT run /pantheon:resume
- Inspect: `cat .pantheon/state.json | jq .`
- Recover from backup: `cp .pantheon/state.json.backup .pantheon/state.json`
- If backup also corrupt, recover from precompact: `ls -t .pantheon/state.json.precompact.* | head -1`

## Memory pressure on Opus 4.7
- Audit large codebases (200K+ LoC) may hit context limit per phase
- Solution: scope phases more narrowly via /pantheon:phase N "scope subset"
- Or pause between phases to let context reset

## Performance
- Full 12-phase audit on 50-200K LoC: ~200-500K input tokens + 100-250K output per persona x 8
- Plan for Claude Max usage
- Phases 3 (parallel personas) heaviest

## Reporting bugs
- File issue at github.com/alehnzgarcia7-crypto/pantheon-audit
- Include: Claude Code version, plugin version, command run, output observed
- Do NOT include sensitive audit data

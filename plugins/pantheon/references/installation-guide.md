# PANTHEON Installation Guide

## Prerequisites
- Claude Code 2.1.144+
- Claude Max subscription (Opus 4.7 access)
- Default launch is `claude` (plain). PANTHEON audits repositories that may contain secrets or production credentials, so approve specific safe actions when prompted rather than skipping permission checks
- `jq` installed for hook scripts (usually pre-installed on macOS/Linux)
- Git installed

## Installation steps

### Step 1: Clone or note repository location
```bash
git clone git@github.com:alehnzgarcia7-crypto/pantheon-audit.git ~/repos/pantheon-audit
```

Or if you have the repo already.

### Step 2: Add marketplace to Claude Code
Inside any Claude Code session:
```
/plugin marketplace add ~/repos/pantheon-audit
```

Or by GitHub URL once published:
```
/plugin marketplace add alehnzgarcia7-crypto/pantheon-audit
```

### Step 3: Install plugin
```
/plugin install pantheon@pantheon-audit
```

### Step 4: Reload plugins
```
/reload-plugins
```

### Step 5: Verify installation
```
/pantheon:status
```

Should output: "No active PANTHEON audit. Run /pantheon:start to begin."

### Step 6: Run first audit
Navigate to project root:
```bash
cd ~/projects/my-project
claude
```

Inside Claude Code:
```
/effort max
/model opus
ultrathink

/pantheon:start "Audit my-project for production launch readiness"
```



### Advanced disposable sandbox mode

Use only in a local disposable sandbox with no secrets, no production credentials, no client data, and no regulated data:

```bash
claude --dangerously-skip-permissions
```

Never use this as the default launch path. PANTHEON is a security audit tool; skipping permission checks on a real target exposes its contents to any compromised MCP server or hook.

## Configuration

### Output language
Default English. To request Spanish output at runtime:
```
/pantheon:start "Audit ... Output findings in Spanish."
```

### Persona customization
To add custom persona, see CONTRIBUTING.md.

### Compliance scope
PANTHEON evaluates all 18 frameworks. To restrict:
```
/pantheon:start "Audit ... Geographic scope: EU only. Industry: SaaS B2B. Skip CNBV, SAT, HIPAA mappings."
```

## Troubleshooting

See `${CLAUDE_PLUGIN_ROOT}/references/troubleshooting.md`.

## Uninstall
```
/plugin uninstall pantheon
```

State in `.pantheon/` directories preserved.

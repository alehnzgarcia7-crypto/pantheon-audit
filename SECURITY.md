# Security Policy

PANTHEON is a security audit tool. We take its supply-chain integrity seriously.

## Reporting a vulnerability

If you discover a vulnerability in PANTHEON itself (the plugin source, hook scripts, Python utilities, or release artifacts), please follow responsible disclosure.

**Preferred channel**: open a private security advisory at
https://github.com/alehnzgarcia7-crypto/pantheon-audit/security/advisories/new

**Alternative**: direct message to the maintainer (@nexogeopo) on a channel you both control.

Do not file a public GitHub issue or open a public PR that demonstrates the vulnerability. Public disclosure before a fix ships puts users at risk.

## What to include in your report

1. PANTHEON version (`git rev-parse HEAD` of the plugin source, or `plugin.json` version field).
2. A minimal reproduction (commands, inputs, expected vs actual behavior).
3. Impact assessment (what an attacker can do, what data or systems are affected).
4. Suggested remediation, if you have one.
5. Whether you intend to disclose publicly and on what timeline.

If the vulnerability involves a third-party dependency, please file it with that project as well.

## Response process

The maintainer commits to:

1. Acknowledge the report within 5 business days.
2. Provide a preliminary triage and severity assessment within 14 business days.
3. Coordinate a fix and disclosure timeline with the reporter.
4. Credit the reporter in release notes unless they request anonymity.

The default disclosure window is 90 days from report, derived from Project Zero policy. The window may be shortened if the vulnerability is being actively exploited, or extended if remediation requires coordination across multiple ecosystem participants.

## Release signing and verification

PANTHEON releases are signed with Sigstore Cosign v3 in bundle format. The signing script is `plugins/pantheon/scripts/release-sign.sh`. The verification procedure is documented in `docs/installation.md` Step 2.

Always verify the bundle before installing a release. If `cosign verify-blob` fails, abort the install and contact the maintainer.

## Revocation

If a release is found to contain a vulnerability or supply-chain compromise after publication, the maintainer will:

1. Publish a GitHub Security Advisory describing the vulnerable versions.
2. Tag a patched release with a new version bump.
3. Update `marketplace.json` and `installation-guide.md` to reference the patched version.
4. Where applicable, file a transparency-log revocation entry via the Sigstore Rekor public log so downstream verifiers can detect the compromised signature on a re-verify.

The Rekor entry alone does not invalidate cached client installs. Users should re-run the install + verify flow on the patched release. The marketplace metadata update is the primary out-of-band signal for downstream tools.

## Supported versions

Only the latest minor release on the `main` branch is supported. There is no LTS branch. If you depend on a specific PANTHEON version for an audit in flight, pin to a commit SHA in your runbook and re-verify on every install.

## Known security limitations

These are not vulnerabilities but design properties users should be aware of:

1. PANTHEON output (`.pantheon/state.json`, `findings/`, `~/Downloads/pantheon-audit-<uuid>/`) contains exploitation guidance for the audit subject until remediation. Treat it as sensitive. See the cloud-sync warning in `docs/installation.md` and `plugins/pantheon/references/ethics-disclaimer.md`.
2. Personas read workspace files as data, never as instructions. The instruction/data boundary clause in every persona system prompt blocks prompt-injection escalation. Adversarial directives in audited material are reported as findings, not obeyed.
3. The MCP tool-integrity check (`plugins/pantheon/hooks/scripts/mcp-tool-integrity-check.sh`) maintains a CVE blocklist with Unicode-resistant normalization. The blocklist is point-in-time; refresh quarterly to track new MCP-server CVEs.
4. Self-audit of PANTHEON has a high false-positive rate. See the Limitations section of the README.

## Cosign version requirement

Cosign v3.0.4 or newer is required for signing and verification, due to GHSA-whqx-f9j3-ch6m (vulnerable versions: v3.0.0 through v3.0.3, v2.6.0, v2.6.1). The signing script enforces this guard.

## License

This security policy is part of the PANTHEON project, licensed under MIT.

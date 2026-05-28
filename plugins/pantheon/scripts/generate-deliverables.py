#!/usr/bin/env python3
"""
generate-deliverables.py

Helper for /pantheon:final. Reads .pantheon/state.json and produces the
35-deliverable output directory skeleton at ~/Downloads/pantheon-audit-<uuid>/.
The actual content generation is performed by pantheon-deliverables-generator
skill running on Opus 4.7; this script only creates the directory + skeleton
files for the skill to fill in.

Usage:
    generate-deliverables.py
"""

import json
import os
import re
import sys
from pathlib import Path

UUID_V4_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)

_MARKDOWN_ESCAPE_RE = re.compile(r"([\\`*_{}\[\]()#+\-.!|<>])")


def markdown_escape(value):
    """Escape markdown control characters so an untrusted scalar from
    state.json cannot inject links, headings, or HTML when interpolated
    into a generated deliverable. PANTHEON-0010 mitigation.
    """
    return _MARKDOWN_ESCAPE_RE.sub(r"\\\1", str(value))

DELIVERABLES = [
    "01-executive-summary.md",
    "02-findings-detail.md",
    "03-threat-model.md",
    "04-asvs-checklist.md",
    "05-crypto-audit.md",
    "06-formal-verif-candidates.md",
    "07-supply-chain-slsa.md",
    "08-red-team-narrative.md",
    "09-codebase-maturity.md",
    "10-compliance-matrix.md",
    "11-adversarial-gate-log.md",
    "12-recommendations.md",
    "13-launch-decision.md",
    "14-incident-response-runbook.md",
    "15-tabletop-scenarios.md",
    "16-monitoring-detections.md",
    "17-secure-sdlc-rubric.md",
    "18-architecture-review.md",
    "19-data-flow-diagram.md",
    "20-attack-surface-map.md",
    "21-poc-repository.md",
    "22-ninety-day-roadmap.md",
    "23-sandbox-attestation-report.md",
    "24-mcp-tool-integrity-report.md",
    "25-cnsa-2-0-readiness-matrix.md",
    "26-transparency-controls-report.md",
    "27-eu-send-model-card.md",
    "28-edge-device-attestation-report.md",
    "29-cross-registry-pinning.md",
    "30-secure-enclave-audit.md",
    "31-dora-register-of-information.xbrl-xml",
    "32-cra-conformity-evidence-pack.md",
    "33-lfpdppp-2025-readiness.md",
    "34-fintech-law-2-0-readiness.md",
    "35-source-track-attestation.md",
]


def main():
    state_path = Path(".pantheon/state.json")
    if not state_path.exists():
        print("[PANTHEON] state.json not found. Cannot generate deliverables.", file=sys.stderr)
        sys.exit(1)
    state = json.loads(state_path.read_text(encoding="utf-8"))
    audit_id = state.get("audit_id", "unknown")
    if not UUID_V4_RE.match(audit_id):
        print(
            f"[PANTHEON] audit_id is not a UUID v4: {audit_id!r}",
            file=sys.stderr,
        )
        sys.exit(2)
    downloads_root = (Path.home() / "Downloads").resolve()
    output_dir = (downloads_root / ("pantheon-audit-" + audit_id)).resolve()
    if not output_dir.is_relative_to(downloads_root):
        print(
            f"[PANTHEON] output_dir escapes Downloads: {output_dir!r}",
            file=sys.stderr,
        )
        sys.exit(3)
    output_dir.mkdir(parents=True, exist_ok=True)
    for deliverable in DELIVERABLES:
        skeleton = output_dir / deliverable
        if not skeleton.exists():
            skeleton.write_text(
                f"# {deliverable}\n\n"
                "[Placeholder. Populate during PANTHEON final generation.]\n",
                encoding="utf-8",
            )
    readme = output_dir / "README.md"
    project_name = state.get("scope", {}).get("project_name", "unknown")
    readme.write_text(
        "# PANTHEON Audit Deliverables\n\n"
        f"**Audit ID**: {markdown_escape(audit_id)}\n"
        f"**Project**: {markdown_escape(project_name)}\n\n"
        "## Deliverables\n\n"
        + "\n".join(f"- {deliverable}" for deliverable in DELIVERABLES)
        + "\n",
        encoding="utf-8",
    )
    print(str(output_dir))


if __name__ == "__main__":
    main()

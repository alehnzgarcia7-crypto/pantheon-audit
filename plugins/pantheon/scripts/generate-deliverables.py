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
import sys
from pathlib import Path

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
    output_dir = Path.home() / "Downloads" / f"pantheon-audit-{audit_id}"
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
    readme.write_text(
        "# PANTHEON Audit Deliverables\n\n"
        f"**Audit ID**: {audit_id}\n"
        f"**Project**: {state.get('scope', {}).get('project_name', 'unknown')}\n\n"
        "## Deliverables\n\n"
        + "\n".join(f"- {deliverable}" for deliverable in DELIVERABLES)
        + "\n",
        encoding="utf-8",
    )
    print(str(output_dir))


if __name__ == "__main__":
    main()

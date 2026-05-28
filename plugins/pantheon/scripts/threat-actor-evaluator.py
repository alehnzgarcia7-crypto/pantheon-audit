#!/usr/bin/env python3
"""
threat-actor-evaluator.py

Given finding metadata, suggests which threat actors (T1-T8) are capable of
exploiting it. Used as pre-fill for orchestrator/persona dispatch.

Usage:
    threat-actor-evaluator.py <finding.json>
"""

import json
import sys
from pathlib import Path


def evaluate(finding: dict) -> list:
    severity = finding.get("severity", "Informational")
    difficulty = finding.get("exploitation_difficulty", "High")
    description = (finding.get("description", "") + " " + finding.get("title", "")).lower()

    actors = set()

    if difficulty == "Low":
        actors.update(["T1", "T2", "T3", "T4", "T6", "T8"])
    if difficulty == "Medium":
        actors.update(["T2", "T3", "T4", "T6", "T8"])
    if difficulty == "High":
        actors.update(["T4", "T6"])

    if "insider" in description or "privilege" in description or "internal" in description:
        actors.add("T5")

    if "supply chain" in description or "dependency" in description or "ci/cd" in description:
        actors.add("T7")

    if severity == "Informational":
        actors = {"T6"} if actors else set()

    return sorted(actors)


def main():
    if len(sys.argv) != 2:
        print("Usage: threat-actor-evaluator.py <finding.json>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    finding = json.loads(path.read_text(encoding="utf-8"))
    actors = evaluate(finding)
    print(json.dumps({"threat_actors_capable": actors}, indent=2))


if __name__ == "__main__":
    main()

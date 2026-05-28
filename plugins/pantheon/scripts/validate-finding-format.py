#!/usr/bin/env python3
"""
validate-finding-format.py

Validates a finding JSON object or .md file against PANTHEON-NNNN format spec.
Returns exit code 0 if valid, non-zero with error description otherwise.

Usage:
    validate-finding-format.py <finding.json>
    validate-finding-format.py <finding.md>
"""

import json
import re
import sys
from pathlib import Path

MANDATORY_FIELDS = [
    "id", "title", "severity", "cvss_v4_vector", "cvss_v4_score",
    "exploitation_difficulty", "business_impact_usd", "business_impact_reasoning",
    "threat_actors_capable", "discovered_by", "phase", "discovered_at",
    "affected_component", "affected_files", "description",
    "exploitation_scenario", "recommendation_short_term", "recommendation_long_term",
    "compliance_mappings", "status"
]

SEVERITY_VALUES = ["Critical", "High", "Medium", "Low", "Informational"]
DIFFICULTY_VALUES = ["Low", "Medium", "High"]
STATUS_VALUES = ["draft", "adversarial-review", "accepted", "disputed", "withdrawn"]
THREAT_ACTORS = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]


def validate_json(data: dict) -> list:
    errors = []
    for field in MANDATORY_FIELDS:
        if field not in data:
            errors.append(f"Missing mandatory field: {field}")
    if "id" in data and not re.match(r"^PANTHEON-\d{4}$", data["id"]):
        errors.append(f"Invalid id format: {data['id']}. Must be PANTHEON-NNNN.")
    if "severity" in data and data["severity"] not in SEVERITY_VALUES:
        errors.append(f"Invalid severity: {data['severity']}. Must be one of {SEVERITY_VALUES}.")
    if "exploitation_difficulty" in data and data["exploitation_difficulty"] not in DIFFICULTY_VALUES:
        errors.append(f"Invalid exploitation_difficulty: {data['exploitation_difficulty']}.")
    if "status" in data and data["status"] not in STATUS_VALUES:
        errors.append(f"Invalid status: {data['status']}.")
    if "threat_actors_capable" in data:
        actors = data["threat_actors_capable"]
        if not isinstance(actors, list):
            errors.append("threat_actors_capable must be a list")
        else:
            for a in actors:
                if a not in THREAT_ACTORS:
                    errors.append(f"Invalid threat actor: {a}. Must be T1-T8.")
    if "cvss_v4_vector" in data:
        v = data["cvss_v4_vector"]
        if not v.startswith("CVSS:4.0/"):
            errors.append(f"Invalid CVSS v4.0 vector prefix: {v}")
    if "title" in data and len(data["title"]) > 80:
        errors.append(f"Title exceeds 80 chars: {len(data['title'])}")
    if "compliance_mappings" in data:
        cm = data["compliance_mappings"]
        if not isinstance(cm, dict):
            errors.append("compliance_mappings must be an object")
    return errors


def validate_md(content: str) -> list:
    errors = []
    if chr(0x2014) in content:
        errors.append("Em-dash found. Per PANTHEON style: replace with comma, period, or restructure.")
    if not re.search(r"^### PANTHEON-\d{4}:", content, re.MULTILINE):
        errors.append("Missing PANTHEON-NNNN heading")
    required_sections = [
        "**Metadata**", "**Severity**", "**Affected**", "**Description**",
        "**Exploitation Scenario**", "**Recommendation (Short-term)**",
        "**Recommendation (Long-term)**", "**Compliance Mappings**",
        "**Adversarial Gate**", "**References**"
    ]
    for section in required_sections:
        if section not in content:
            errors.append(f"Missing section: {section}")
    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: validate-finding-format.py <finding.json|finding.md>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    content = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}", file=sys.stderr)
            sys.exit(2)
        errors = validate_json(data)
    elif path.suffix == ".md":
        errors = validate_md(content)
    else:
        print(f"Unsupported file type: {path.suffix}. Use .json or .md.", file=sys.stderr)
        sys.exit(1)
    if errors:
        print(f"[PANTHEON FORMAT] {len(errors)} error(s) in {path}:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(3)
    print(f"[PANTHEON FORMAT] {path} is valid.")
    sys.exit(0)


if __name__ == "__main__":
    main()

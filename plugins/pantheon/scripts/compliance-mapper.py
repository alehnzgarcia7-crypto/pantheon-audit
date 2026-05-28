#!/usr/bin/env python3
"""
compliance-mapper.py

Helper for mechanical compliance mapping. Reads finding JSON, outputs candidate
mappings for the 18 PANTHEON frameworks. Used as input pre-fill for compliance-mapper
sub-agent (which validates and refines with Opus 4.7).

Usage:
    compliance-mapper.py <finding.json>
"""

import json
import sys
from pathlib import Path

CWE_HEURISTICS = {
    "sql injection": "CWE-89",
    "xss": "CWE-79",
    "csrf": "CWE-352",
    "ssrf": "CWE-918",
    "deserialization": "CWE-502",
    "path traversal": "CWE-22",
    "command injection": "CWE-78",
    "open redirect": "CWE-601",
    "broken access control": "CWE-285",
    "broken authentication": "CWE-287",
    "idor": "CWE-639",
    "race condition": "CWE-362",
    "jwt": "CWE-345",
    "weak crypto": "CWE-327",
    "hardcoded credentials": "CWE-798",
    "improper certificate validation": "CWE-295",
    "buffer overflow": "CWE-120",
    "integer overflow": "CWE-190",
    "ldap injection": "CWE-90",
    "xml external entity": "CWE-611",
}

OWASP_TOP10_HEURISTICS = {
    "broken access control": "A01:2021",
    "cryptographic failure": "A02:2021",
    "injection": "A03:2021",
    "insecure design": "A04:2021",
    "security misconfiguration": "A05:2021",
    "vulnerable component": "A06:2021",
    "outdated component": "A06:2021",
    "authentication failure": "A07:2021",
    "identification failure": "A07:2021",
    "software integrity": "A08:2021",
    "data integrity": "A08:2021",
    "logging failure": "A09:2021",
    "monitoring failure": "A09:2021",
    "ssrf": "A10:2021",
}


def suggest_mappings(finding: dict) -> dict:
    title = finding.get("title", "").lower()
    description = finding.get("description", "").lower()
    text = f"{title} {description}"
    mappings = {k: None for k in [
        "cwe", "owasp_top10", "owasp_api_top10", "owasp_asvs_v5_l3",
        "cnbv_cuf_cuifpes", "lfpdppp_2025", "sat_cff", "gdpr", "pci_dss_401",
        "hipaa", "soc2_tsc", "iso27001_annex_a", "iso27017", "iso27018",
        "iso27701", "nist_800_53_rev5", "mitre_attack", "capec"
    ]}
    for keyword, cwe in CWE_HEURISTICS.items():
        if keyword in text:
            mappings["cwe"] = cwe
            break
    for keyword, owasp in OWASP_TOP10_HEURISTICS.items():
        if keyword in text:
            mappings["owasp_top10"] = owasp
            break
    mappings["mapping_confidence"] = 0.5
    mappings["mapping_notes"] = "Heuristic pre-fill. Refine via compliance-mapper sub-agent."
    return mappings


def main():
    if len(sys.argv) != 2:
        print("Usage: compliance-mapper.py <finding.json>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    finding = json.loads(path.read_text(encoding="utf-8"))
    mappings = suggest_mappings(finding)
    print(json.dumps(mappings, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

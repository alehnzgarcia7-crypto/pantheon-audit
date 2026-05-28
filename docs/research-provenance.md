# PANTHEON Research Provenance

This file records the primary sources behind Section 5.6 frontier-intelligence findings (assembled May 27, 2026). Auditees can and will cross-check these. Use verbatim primary-source quotes where central to a compliance assertion.

## Source categories
Each Section 5.6 finding traces to at least one of:
- Anthropic-official (docs.anthropic.com, code.claude.com, anthropic.com blog)
- Regulator-official (NIST CSRC, NSA Cybersecurity Advisory, ENISA, ECB DORA portal, DOF Mexico, CNBV)
- Academic primary (arXiv, IACR eprint, OpenReview, ACM, USENIX, CCS)
- Vendor advisory (AMD, Intel, NVIDIA, Microsoft, GitHub Security Advisories, Sigstore)
- Threat-intel primary (CISA advisories, FBI statements, Wiz, ReversingLabs, Microsoft Security, Palo Alto Unit 42)

## Selected primary sources by area
- Claude Code platform: docs.anthropic.com sub-agents and hooks pages; SecurityWeek security-guidance plugin coverage (May 27, 2026).
- MCP vulnerabilities: arXiv 2601.17549 (Maloyan, Namiot); arXiv 2603.22489 (Lin, Milani Fard); OX Security MCP advisory.
- Agent reliability: Narayanan and Kapoor, Towards a Science of AI Agent Reliability (March 24, 2026).
- Formal verification: AWS Automated Reasoning Group blog (A billion SMT queries a day, February 4, 2026); IACR eprint 2025/1700.
- Post-quantum: NIST CSRC FIPS 206 IPD; NSA CNSA 2.0 advisory (updated May 30, 2025); RFC 9794.
- EU AI Act: European Commission Digital Omnibus political agreement (May 7, 2026).
- Adversary TTPs: CISA AA25-239A (September 3, 2025); FBI AD Brett Leatherman statement (August 27, 2025); ReversingLabs 4th Annual Software Supply Chain Security Report (January 27, 2026); Wiz, Microsoft, Palo Alto Unit 42 Shai-Hulud coverage.
- Mexico: DOF March 20 2025 (LFPDPPP 2025); CNBV CUIFPEs; SMPS Legal, legalparadox, Chambers Fintech Mexico 2026.
- Supply chain crypto: Sigstore blog (Cosign v3, Rekor v2 GA); SLSA v1.2 RC2; CycloneDX 1.7; W3C WebAuthn L3 CR; FIDO CXF/CXP.

## Caveats
- Future-dated EU items rest on political agreement pending formal trilogue text.
- WASI 0.3.0 February 2026 is expected per roadmap, not gated until released.
- CNSA 2.0 exclusions are NSA policy; non-NSS sectors may still use SLH-DSA, FN-DSA, HashML-DSA.
- Mexico Fintech Law 2.0 is in debate stage; readiness deliverable is advisory only.
- Cosign GHSA-whqx-f9j3-ch6m version ranges cross-verify against the GitHub Security Advisory before use as compliance evidence.

This file is generated during the build per the File content resolution rule and reflects Section 5.6 at freeze time.

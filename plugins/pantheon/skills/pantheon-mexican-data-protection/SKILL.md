---
name: pantheon-mexican-data-protection
description: Mexican fintech data-protection compliance for PANTHEON (Phoenix Financial OS-critical). Activates whenever audit scope mentions Mexico, CNBV, Banxico, SAT, IMSS, INFONAVIT, SPEI, CFDI, RFC, CLABE, CURP, NSS, IFPE, ITF, CUIFPEs, LFPDPPP, INAI (legacy), SABG, AML, CTF, or Mexican personal-data processing. Implements the March 21, 2025 LFPDPPP reform per Finding 5.6.7.8 (dissolution of INAI, SABG as new authority, AI/automated-decision objection rights, processor liability, sensitive-data category, specialized federal courts, cross-border transfer with equivalent-obligations clause), the 2026 CUIFPEs IFPE vendor authorization sanctions matrix per Finding 5.6.7.9, the Fintech Law 2.0 advisory readiness per Finding 5.6.7.10, the July 2025 CIBanco/Intercam/Vector enforcement context per Finding 5.6.7.11, and the July 2025 Federal Economic Competition Law reform per Finding 5.6.7.12.
---

# PANTHEON Mexican Data Protection Skill

## When this activates
1. Audit scope is a Mexican entity, fintech, IFPE, ITF, or processes Mexican-resident personal data
2. CFDI 4.0 invoicing flows in scope
3. SPEI or any Banxico-connected payment system in scope
4. CNBV-regulated activity in scope
5. The user explicitly invokes via `/pantheon:mexican-fintech` command

## What this skill does (Phoenix Financial OS-priority)
1. **LFPDPPP 2025 ARCO+ audit**: Access, Rectification, Cancellation, Opposition rights flow exists AND the new objection-to-automated-processing right is honored
2. **SABG complaint workflow**: Data-subject complaint endpoint exists and routes to SABG (Secretariat of Anti-Corruption and Good Governance), NOT to the dissolved INAI
3. **AI-decision explainability**: Article 6 second paragraph (data-subject interest priority) compliance check: any automated decision affecting a data subject must be explainable on-demand
4. **Sensitive-data category check**: Identifies sensitive data (racial, ethnic origin, present and future health, genetic, biometric, religious, philosophical, moral convictions, sexual preference, political opinions) and verifies heightened-obligations controls in place
5. **Cross-border transfer audit**: Any data flow to a foreign processor verifies the contractual equivalent-obligations clause exists per LFPDPPP 2025 Article 71
6. **Processor-versus-controller liability**: Detects implicit processor relationships (third-party data hosting, analytics SDKs, etc.) and verifies processor agreements per Article 50
7. **CNBV CUIFPEs IFPE vendor authorization gate**: For IFPEs, any vendor providing critical service requires CNBV authorization or notice; flag absence
8. **AML/CTF exposure modeling**: Maps audit findings to the July 2025 CIBanco/Intercam/Vector enforcement pattern (USD cash above limits, international-transfer reporting failures)
9. **Fintech Law 2.0 advisory**: For IFPEs and ITFs, generates forward-readiness recommendations for the publicly-debated Fintech Law 2.0 (March 26, 2026 debate stage)
10. **Federal Economic Competition Law reform (July 2025) gate**: Checks merchant-fee policies and interest-free instalment terms against the new 20%-of-revenue fine exposure

## References
- `references/lfpdppp-2025-articles.md`: full article-by-article spec
- `references/sabg-complaint-workflow.md`: SABG complaint procedure (replaces INAI)
- `references/arco-objection-rights.md`: ARCO + new objection-to-automated-processing rights
- `references/cnbv-cuifpes-2026.md`: CUIFPEs 2026 vendor authorization sanctions matrix

## Hard rules
1. LFPDPPP 2025 references the SECRETARIAT OF ANTI-CORRUPTION AND GOOD GOVERNANCE (SABG), NOT INAI. INAI dissolution is effective March 21, 2025. Any audit deliverable mentioning INAI as live authority is auto-reject.
2. AI/automated-decision objection rights (NEW in LFPDPPP 2025) MUST be honored. Absence is Critical for any AI-deploying fintech.
3. Sensitive-data category requires explicit consent unless legal basis. Implicit consent is unconditional finding.
4. Cross-border transfer without equivalent-obligations clause is Critical.
5. IFPE deploying critical third-party service without CNBV authorization or notice is Critical, audit auto-fails.
6. Audit outputs in Spanish when context includes `userMemories.communicates in informal Mexican Spanish`. English when not specified.
7. No em-dashes

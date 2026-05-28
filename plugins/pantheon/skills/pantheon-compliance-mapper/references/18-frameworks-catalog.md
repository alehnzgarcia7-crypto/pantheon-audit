# Compliance Frameworks Index (18 frameworks)

## 1. CWE (Common Weakness Enumeration)
- Maintainer: MITRE
- Citation format: `CWE-XXX` (single ID)
- Reference: cwe.mitre.org

## 2. OWASP Top 10 2021
- Citation: `A0X:2021 - Category Name`
- 10 categories (A01-A10)
- Reference: owasp.org/Top10/

## 3. OWASP API Security Top 10 2023
- Citation: `APIX:2023 - Category Name`
- 10 categories (API1-API10)
- Reference: owasp.org/API-Security/

## 4. OWASP ASVS 5.0
- Citation: `V.X.Y.Z` (chapter.section.subsection.requirement)
- 14 chapters, three levels (L1, L2, L3)
- Reference: owasp.org/www-project-application-security-verification-standard/

## 5. CNBV CUF/CUIFPEs (Mexico)
- Comisión Nacional Bancaria y de Valores
- CUF: Circular Única de Bancos
- CUIFPEs: Circular Única de Instituciones de Tecnología Financiera y de Pago
- Citation: `Art. X CUF` or `Art. X CUIFPEs`
- Key articles: CUIFPEs Art. 32 (operational risk), 44 (information security), 56 (cyber incident reporting)
- Applies when: Mexican fintech, ITF, banks

## 6. LFPDPPP 2025 (Mexico)
- Ley Federal de Protección de Datos Personales en Posesión de los Particulares (2025 reform)
- Citation: `Art. X`
- Key articles: Art. 14 (data quality), 19 (security measures), 20 (breach notification within 72h), 31 (security measures), 64-66 (sanctions)
- Applies when: Mexican PII

## 7. SAT CFF (Mexico)
- Servicio de Administración Tributaria - Código Fiscal de la Federación
- Citation: `Art. X CFF`
- Key articles: Art. 49 Bis (e-invoicing security), 86 Quater (PII protection)
- Applies when: Mexican tax/CFDI processing

## 8. GDPR (EU)
- General Data Protection Regulation
- Citation: `Art. X` or `Recital X`
- Key articles: Art. 5 (principles), 6 (lawfulness), 25 (privacy by design), 32 (security), 33-34 (breach notification), 35 (DPIA)
- Applies when: EU resident PII

## 9. PCI-DSS 4.0.1
- Payment Card Industry Data Security Standard
- Citation: `Req. X.Y.Z`
- 12 requirement groups
- Applies when: cardholder data processed/stored/transmitted

## 10. HIPAA Security Rule (US)
- Citation: `45 CFR 164.XXX(X)(X)`
- Administrative, Physical, Technical safeguards
- Key sections: 164.308 (admin), 164.310 (physical), 164.312 (technical), 164.314 (org), 164.316 (policies)
- Applies when: US PHI

## 11. SOC 2 TSC (Trust Services Criteria)
- AICPA framework
- Citation: `CCX.Y` (Common Criteria) or specific category
- Categories: Security (CC), Availability (A), Processing Integrity (PI), Confidentiality (C), Privacy (P)
- Applies when: SOC 2 attestation goals

## 12. ISO 27001 Annex A (2022)
- Citation: `A.X.Y.Z`
- 93 controls in 4 themes (Organizational 37, People 8, Physical 14, Technological 34)
- Applies when: ISO certification or alignment

## 13. ISO 27017
- Cloud-specific extension to 27001
- Citation: `CLD.X.Y.Z`
- Applies when: cloud services consumed/provided

## 14. ISO 27018
- Cloud PII processor
- Citation: `A.X.Y`
- Applies when: cloud PII

## 15. ISO 27701
- Privacy information management
- Citation: `A.X.Y.Z`
- Extends 27001 with privacy
- Applies when: privacy management certification

## 16. NIST 800-53 Rev 5
- US federal control catalog
- Citation: `XX-Y` (family-control, e.g., `IA-2`, `SC-13`)
- 20 control families
- Applies when: US federal or FedRAMP

## 17. MITRE ATT&CK Enterprise
- Adversary tactics, techniques
- Citation: `TXXXX` or `TXXXX.YYY` (technique.sub-technique)
- v15 (latest 2026)
- Applies always (universal language for attacker behavior)

## 18. CAPEC
- Common Attack Pattern Enumerations and Classifications
- Citation: `CAPEC-XXX`
- v3.9 (latest 2026)
- Applies when: attack pattern documented

## Update mechanism
This index updated annually or when framework version released. Auditor verifies article references against current official sources before citing in production deliverables.

---

## Auxiliary frameworks (PANTHEON-0019 expansion)

These frameworks are not part of the canonical 18 catalog above but are routinely cited by PANTHEON personas in phase outputs and finding mappings. Maintained here for citation provenance and to satisfy the meta-audit consistency check.

### A1. NIST SP 800-218 SSDF
- Secure Software Development Framework
- Citation: `PO.x.y`, `PS.x.y`, `PW.x.y`, `RV.x.y` (Practice category dot task)
- v1.1 (latest 2026)
- Applies always (every development practice maps to one or more SSDF tasks)

### A2. SLSA
- Supply-chain Levels for Software Artifacts
- Citation: `SLSA L<n>` for level, `SLSA <track> L<n>` for track and level
- v1.1 source track, build track, deployment track
- Applies when: build pipeline, artifact distribution, or dependency provenance is in scope

### A3. MITRE ATLAS
- Adversarial Threat Landscape for AI Systems
- Citation: `AML.T<NNNN>` for techniques, `AML.TA<NNNN>` for tactics
- v2026 (latest)
- Applies when: AI/ML, LLM applications, RAG, agentic systems, MCP-served tools in scope

### A4. OWASP Top 10 for LLM Applications
- Citation: `LLM<NN>:<YEAR>` (e.g., LLM01:2025)
- 2025 edition
- Applies when: LLM applications in scope

### A5. NIST AI RMF
- AI Risk Management Framework
- Citation: framework function (`GOVERN`, `MAP`, `MEASURE`, `MANAGE`) and subcategory
- v1.0 plus Generative AI Profile (NIST AI 600-1)
- Applies when: AI systems in scope or AI risk governance evidence required

### A6. ISO/IEC 42001
- AI Management System Standard
- Citation: clause number (e.g., `Clause 8.4`)
- 2023 edition
- Applies when: AI/ML in scope and organization seeks ISO certification path

### A7. EU AI Act
- Regulation (EU) 2024/1689
- Citation: Article number (e.g., `Article 15`)
- In force progressively from August 2024 (general purpose AI models from August 2025; full applicability August 2026)
- Applies when: AI system placed on EU market, used by EU establishment, or affecting persons located in EU

### A8. OWASP SAMM 2
- Software Assurance Maturity Model
- Citation: business function + security practice + maturity level (e.g., `Verification.Security Testing.L3`)
- v2.0
- Applies when: SDLC maturity assessment is in scope

### A9. BSIMM
- Building Security In Maturity Model
- Citation: domain.practice.activity-id (e.g., `SR1.1`)
- v14 (latest 2026)
- Applies when: empirical SDLC benchmarking against industry peers is in scope

### A10. OpenSSF Scorecard
- Citation: check name (e.g., `Branch-Protection`, `Pinned-Dependencies`, `Token-Permissions`)
- v5 checks suite
- Applies always for open source repositories

### A11. OpenSSF Best Practices Badge
- Citation: `BasicBadge`, `SilverBadge`, `GoldBadge` and the criterion identifier
- Applies when: badge claim is part of the project's public attestation

### A12. TIBER-EU
- Threat Intelligence-Based Ethical Red Teaming framework
- Citation: TIBER stage (e.g., `Targeting`, `Reconnaissance`, `Weaponization`, ...)
- v2024 (latest)
- Applies when: financial entity in EU/UK regulated environment requires threat-led testing

### Update mechanism (auxiliary)

Auxiliary frameworks are reviewed semi-annually. The compliance-mapper persona is authorized to cite from this auxiliary section as long as the article-level citation includes the version cited (e.g., `MITRE ATLAS AML.T0051 (v2026)`). When citing in a deliverable, the auditor confirms the auxiliary framework is in the SoW's jurisdictional or industry scope; otherwise the citation is informational and labeled as such.

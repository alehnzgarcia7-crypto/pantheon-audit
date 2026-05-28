# PASTA: 7 Stages

UcedaVelez/Morana. Risk-centric.

1. Define Business Objectives: business purpose, regulatory (CNBV, LFPDPPP, PCI, HIPAA, GDPR), SLAs, critical processes, reputation.
2. Define Technical Scope: architecture, tech stack, integrations, trust boundaries, network, deployment.
3. Application Decomposition: DFD Level 0/1/2, entry/exit points, internal flows, dependencies.
4. Threat Analysis: STRIDE per element. LINDDUN for privacy.
5. Vulnerability/Weakness Analysis: per threat enabling CWEs, codebase vulnerabilities (CVE or locations), exploitability.
6. Attack Modeling: attack trees for top threats. Root attacker objective. Per node: difficulty, detection probability, mitigation.
7. Risk/Impact Analysis: likelihood (0.0-1.0), monetized impact, risk score (SLE * ARO), mitigation status, residual risk.

Reference: UcedaVelez & Morana (2015). Risk Centric Threat Modeling. Wiley.

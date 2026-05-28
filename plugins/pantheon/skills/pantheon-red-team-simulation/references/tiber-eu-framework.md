# TIBER-EU Framework

Threat Intelligence-Based Ethical Red-teaming for European Union. ECB framework. Mandatory for systemically important financial institutions in EU. Bank of England equivalent: CBEST. Hong Kong: iCAST. Saudi Arabia: FEER.

## TIBER-EU stages

### 1. Preparation
- Define scope and engagement objectives
- Identify critical functions
- Stakeholder alignment
- Procurement of threat intelligence and red team providers

### 2. Threat Intelligence Phase
- Targeted threat intelligence report
- Threat actor selection (typically 1-3 based on TI)
- TTPs per actor relevant to target
- Generic and targeted attack scenarios

### 3. Red Team Test Phase
TIBER-EU kill chain:
1. **Reconnaissance**: external recon, OSINT, employee enumeration
2. **Weaponization**: exploit selection, payload construction
3. **Delivery**: how exploit reaches target (phishing, exploit public app, supply chain)
4. **Exploitation**: triggering vulnerability
5. **Installation**: persistence mechanism
6. **Command and Control**: C2 channel establishment
7. **Actions on Objectives**: data exfil, financial fraud, control assumption

### 4. Closure Phase
- Red team report
- Blue team detection assessment
- Lessons learned
- Remediation plan

## TIBER-EU vs traditional pentest
- Pentest: scope-limited, time-boxed, find-as-many-bugs
- TIBER-EU: realistic adversary emulation, scenario-driven, end-to-end kill chain, with active blue team

## PANTHEON adaptation
PANTHEON does not run actual exploits in production. Adapts TIBER-EU to code review:
1. Reasoning-based threat intelligence (synthesized from codebase + threat actor matrix)
2. Constructed attack chains using actual findings
3. Theoretical kill chain walkthrough
4. Detection coverage gap analysis based on logging/monitoring code review
5. Output: TIBER-EU style report (deliverable #5)

## Regulator equivalents
- EU: TIBER-EU (ECB)
- UK: CBEST (Bank of England)
- Hong Kong: iCAST (HKMA)
- Saudi Arabia: FEER (SAMA)
- Singapore: AASE (MAS)
- Canada: CRIBE (OSFI)
- Australia: under development (APRA)

## References
- TIBER-EU Framework v2024 (ECB)
- "Cyber Threat Intelligence-Based Penetration Testing" (Bank of England)
- Mandiant TIBER-EU adoption guides

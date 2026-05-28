# Threat Actor 8-Profile Matrix

(See pantheon-threat-model skill references for full content; this file is canonical reference.)

## T1: Script Kiddie
- Capability: Low
- Motivation: Reputation, vandalism, low-effort fraud
- Resources: Single individual, public tooling
- Patience: Low
- Examples: Defacement campaigns, automated credential stuffing

## T2: Hacktivist
- Capability: Low-Medium
- Motivation: Ideological, political, social
- Resources: Crowdsourced
- Patience: Moderate
- Examples: Anonymous operations, LulzSec, regional hacktivist groups

## T3: Criminal Opportunist
- Capability: Medium
- Motivation: Direct financial gain
- Resources: Solo/small criminal cell, dark market tooling
- Patience: Low-moderate
- Examples: Generic phishing campaigns, smaller ransomware operators

## T4: Organized Cybercrime
- Capability: High
- Motivation: Large financial gain, long-term operations
- Resources: Significant, multiple developers, money laundering infrastructure
- Patience: High
- Examples: Conti, LockBit, FIN7, Carbanak

## T5: Disgruntled Insider
- Capability: Variable, has legitimate access
- Motivation: Revenge, financial, ideology, coercion
- Resources: Legitimate credentials, insider knowledge
- Patience: Variable
- Examples: Snowden, internal fraud cases

## T6: Nation-State APT
- Capability: Highest
- Motivation: Geopolitical, espionage, IP theft, sabotage
- Resources: Government-funded, indefinite timeline
- Patience: Very high
- Examples: APT28, APT41, Lazarus, Equation Group, Unit 8200

## T7: Supply Chain Compromise
- Capability: Variable (T3-T6)
- Motivation: Indirect access to downstream
- Resources: Variable
- Patience: High
- Examples: SolarWinds, xz-utils, event-stream, codecov

## T8: AI-Augmented Attacker
- Capability: Medium-High
- Motivation: Variable, often T3 or T4 augmented
- Resources: Variable, lower barrier via AI tools
- Patience: Moderate
- Examples: Emerging category, documented 2024-2026

## Per-finding usage
Every finding cites which T1-T8 can exploit. Output: `threat_actors_capable: [T1, T3, T4, T7]`.

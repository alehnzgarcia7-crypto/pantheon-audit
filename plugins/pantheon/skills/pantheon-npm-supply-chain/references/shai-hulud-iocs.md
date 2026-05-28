# Shai-Hulud IOC Reference

Tracked indicators of compromise from the three Shai-Hulud campaigns. Refreshed quarterly per Subsection 5.6.10.

## Campaign 1: Shai-Hulud original (September 15, 2025)
- First self-replicating npm supply-chain worm
- Phishing vector: npmjs[.]help (Porkbun registration September 5, 2025)
- ~500 packages compromised including `@ctrl/tinycolor`
- TruffleHog integration to harvest secrets
- GitHub REST API for lateral movement
- Creates public "Shai-Hulud" repos with exfiltrated secrets
- Source: Wiz blog, CISA alert September 23 2025, Picus, Splunk

## Campaign 2: Shai-Hulud 2.0 (November 2025)
- Switch from post-install to PRE-INSTALL execution
- LLM-generated bash payload (Unit 42 moderate confidence)
- Combined with Campaign 1: 1,000+ npm packages compromised, ~25,000 GitHub repos exposed (ReversingLabs Jan 27 2026 report)
- Source: Microsoft Security Blog, Palo Alto Unit 42

## Campaign 3: Mini Shai-Hulud (May 11, 2026)
- First cross-registry attack (npm + PyPI)
- 170+ npm packages compromised
- 2 PyPI packages compromised
- 404 malicious versions across both registries
- Source: Microsoft Security Blog

## IOC patterns to detect
- File paths: `node_modules/<pkg>/.shai-hulud/`, `node_modules/<pkg>/secrets.txt`
- Network egress: `webhook[.]site`, `npmjs[.]help`
- GitHub Actions: workflows creating public repos with names containing "Shai-Hulud"
- Process: TruffleHog binary execution from package post-install scripts
- Package metadata: maintainer changes within 48 hours of publication

## Known compromised package families (sample)
Maintainer-account-takeover targeted what ReversingLabs CEO Mario Vuksan described as "the most influential open source maintainer accounts and the widely-used packages they manage." Specific package list refreshed via `frontier-intelligence-refresh.sh` quarterly.

## References
- Wiz Shai-Hulud blog
- Microsoft Security Blog Shai-Hulud 2.0 and Mini Shai-Hulud guidance
- ReversingLabs 4th Annual SSCS Report (January 27, 2026)
- Palo Alto Unit 42 npm supply chain attack analysis

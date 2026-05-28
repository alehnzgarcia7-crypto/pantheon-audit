# Adversary Emulation Library

Standard adversary emulation profiles. Pick relevant for codebase context.

## APT29 (Cozy Bear, Russia SVR)
Targets: government, think tanks, healthcare research, technology.
Initial access: spear phishing with macro-enabled docs, supply chain (SolarWinds).
Persistence: scheduled tasks, registry run keys, WMI event subscriptions.
C2: HTTPS over CDN-fronted infrastructure (Azure, AWS).
Exfil: Slow drip via legitimate cloud services.

## APT41 (Double Dragon, China MSS-aligned)
Targets: technology, telecom, healthcare, gaming, financial.
Initial access: exploit public-facing apps, supply chain (CCleaner), spear phishing.
Persistence: web shells (China Chopper), DLL side-loading.
C2: Cobalt Strike, custom backdoors.
Exfil: zip archives via FTP or HTTP POST.

## Lazarus (North Korea)
Targets: cryptocurrency exchanges, financial institutions, defense.
Initial access: spear phishing (LinkedIn job offers), supply chain (3CX 2023).
Persistence: services, scheduled tasks, BOOTKIT.
C2: TOR, custom protocols.
Exfil: cryptocurrency transfers, file exfil via custom tools.

## FIN7 (Carbanak)
Targets: retail, hospitality, financial.
Initial access: spear phishing (weaponized docs), SQL injection.
Persistence: scheduled tasks, registry, COM hijacking.
C2: PowerShell Empire, Carbanak.
Actions: card data theft, BEC, ransomware deployment.

## Conti / Conti successors (LockBit, BlackBasta)
Targets: any with revenue.
Initial access: phishing (BazarLoader), exploit public apps (Log4Shell, ProxyShell).
Persistence: scheduled tasks, services, Cobalt Strike beacons.
C2: Cobalt Strike + custom.
Actions: data exfil + ransomware deployment + extortion.

## Insider (T5) emulation
- Disgruntled developer: code-level backdoor, time bomb, credential leak
- Departing employee: bulk download, IP theft, customer list theft
- Bribed admin: credential sharing, security control bypass

## Per-engagement profile construction
1. Identify 1-3 most relevant from above + threat-model.md
2. Customize TTPs to codebase
3. Construct attack chain using actual findings
4. Document blue team detection coverage per kill chain stage

## References
- MITRE ATT&CK Groups: attack.mitre.org/groups/
- Mandiant APT reports
- CrowdStrike Adversary Universe
- Bishop Fox adversary emulation guides

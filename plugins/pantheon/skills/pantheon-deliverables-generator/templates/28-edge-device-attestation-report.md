# Edge Device Attestation Report (Salt Typhoon resistant)

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11  
**Baseline reference**: Finding 5.6.6.1 Salt Typhoon (FBI confirmation August 27, 2025, 80 countries scope); CISA AA25-239A September 3, 2025

## Purpose
For any audit where network edge devices (routers, BMCs, firewalls, VPN concentrators) are in scope, this deliverable attests integrity per Salt Typhoon TTPs.

## Devices in scope
| Device | Vendor | Model | Firmware version | Integrity verified? |
|---|---|---|---|---|
| Router 1 | Cisco | <model> | <ver> | <yes/no, method> |
| Firewall 1 | Palo Alto | <model> | <ver> | <yes/no, method> |
| BMC | <vendor> | <model> | <ver> | <yes/no, method> |

## Salt Typhoon CVE blocklist verification
| CVE | Vendor | Status |
|---|---|---|
| CVE-2018-0171 | Cisco | <PATCHED / UNPATCHED / NOT-APPLICABLE> |
| CVE-2023-20198 | Cisco | <status> |
| CVE-2023-20273 | Cisco | <status> |
| CVE-2024-21887 | Ivanti | <status> |
| CVE-2024-3400 | Palo Alto | <status> |

## TTP coverage (Salt Typhoon, Volt Typhoon, Flax/Silk/Velvet)
- [ ] BMC firmware verified (against vendor signed images)
- [ ] Edge device admin access requires MFA
- [ ] DLL sideloading detection (per Darktrace October 2025 Salt Typhoon observation: Norton, Bkav, IObit abused)
- [ ] SNAPPYBEE/Deed RAT signatures in EDR
- [ ] Citrix NetScaler patches current
- [ ] Living-off-the-land detection (PowerShell, WMIC anomaly patterns)
- [ ] KV Botnet residual cleanup (end-of-life Cisco RV320/RV325, Netgear ProSafe quarantined)

## Findings
| Finding ID | Title | Severity | Typhoon family |
|---|---|---|---|
| PANTHEON-<NNNN> | <title> | <severity> | <Salt/Volt/Flax/Silk/Velvet> |

## Hard fails
- [ ] Any of the 5 Salt Typhoon CVEs unpatched on internet-facing edge device
- [ ] BMC firmware unsigned or with vendor-default credentials

## Signoff
- Bishop-Fox red-team persona attestation
- Date: <ISO-8601>

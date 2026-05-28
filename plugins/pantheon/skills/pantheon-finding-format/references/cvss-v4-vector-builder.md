# CVSS v4.0 Vector Builder

Format: `CVSS:4.0/AV:X/AC:X/AT:X/PR:X/UI:X/VC:X/VI:X/VA:X/SC:X/SI:X/SA:X`

## Base
- AV: N/A/L/P
- AC: L/H
- AT: N/P
- PR: N/L/H
- UI: N/P/A

## Impact (vulnerable + subsequent)
- VC/VI/VA, SC/SI/SA: H/L/N

## Ranges
- 0.0 None, 0.1-3.9 Low, 4.0-6.9 Medium, 7.0-8.9 High, 9.0-10.0 Critical

## Examples
Critical SQLi: `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N` → ~9.3
High IDOR: `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N` → ~7.7
Medium XSS: `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:P/VC:L/VI:L/VA:N/SC:L/SI:L/SA:N` → ~5.5

Reference: https://www.first.org/cvss/v4-0/

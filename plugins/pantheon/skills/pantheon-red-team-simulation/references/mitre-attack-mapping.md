# MITRE ATT&CK Mapping

Enterprise matrix. Every red team finding maps to ATT&CK technique IDs.

## Tactic categories
- TA0001 Initial Access
- TA0002 Execution
- TA0003 Persistence
- TA0004 Privilege Escalation
- TA0005 Defense Evasion
- TA0006 Credential Access
- TA0007 Discovery
- TA0008 Lateral Movement
- TA0009 Collection
- TA0010 Exfiltration
- TA0011 Command and Control
- TA0040 Impact

## Common techniques in app security findings

### Initial Access
- T1190 Exploit Public-Facing Application (SQLi, RCE, deserialization)
- T1133 External Remote Services (exposed admin panels)
- T1078 Valid Accounts (credential stuffing)

### Execution
- T1059.001 PowerShell, .003 Windows Command Shell, .004 Unix Shell, .006 Python, .007 JavaScript
- T1203 Exploitation for Client Execution (XSS to local code)

### Persistence
- T1505.003 Web Shell
- T1098 Account Manipulation (rogue admin)
- T1136 Create Account

### Privilege Escalation
- T1068 Exploitation for Privilege Escalation (kernel exploits, container escape)
- T1078.004 Cloud Accounts (privilege escalation in cloud IAM)

### Defense Evasion
- T1027 Obfuscated Files
- T1562 Impair Defenses (disable security controls)
- T1070 Indicator Removal (log deletion)

### Credential Access
- T1110 Brute Force (.001 password guessing, .003 stuffing, .004 spraying)
- T1555 Credentials from Password Stores
- T1212 Exploitation for Credential Access (Kerberoasting)
- T1539 Steal Web Session Cookie (XSS, MITM)

### Discovery
- T1087 Account Discovery
- T1518 Software Discovery
- T1018 Remote System Discovery

### Lateral Movement
- T1021 Remote Services
- T1550 Use Alternate Authentication Material (pass-the-hash)

### Collection
- T1213 Data from Information Repositories
- T1005 Data from Local System
- T1119 Automated Collection

### Exfiltration
- T1041 Exfiltration Over C2 Channel
- T1567 Exfiltration Over Web Service (cloud storage abuse)
- T1048 Exfiltration Over Alternative Protocol

### Impact
- T1486 Data Encrypted for Impact (ransomware)
- T1565 Data Manipulation (financial fraud)
- T1499 Endpoint Denial of Service

## Mapping example
Finding: SQL injection allows unauthenticated read of users table
Maps to: T1190 (Initial Access), T1213 (Collection from databases)

Finding: JWT alg confusion enables admin impersonation
Maps to: T1078 (Valid Accounts), T1212 (Exploitation for Credential Access)

Finding: SSRF to cloud metadata exposes instance role credentials
Maps to: T1190 -> T1552.005 (Cloud Instance Metadata) -> T1078.004 (Cloud Accounts)

## Sub-techniques
Use sub-technique IDs (T1110.001 not just T1110) when applicable. Specificity helps SOC mapping.

## References
- MITRE ATT&CK Enterprise v15: attack.mitre.org
- "Threat-Based Defense" CIS Critical Security Controls v8

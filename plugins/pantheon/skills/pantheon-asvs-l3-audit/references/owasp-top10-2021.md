# OWASP Top 10 2021

Cite as `A0X:2021 - Category Name`.

## A01:2021 Broken Access Control
IDOR, missing function-level auth, privilege escalation, JWT alg confusion, force browsing.

## A02:2021 Cryptographic Failures
Weak algorithms, weak keys, missing encryption, hardcoded keys, weak random.

## A03:2021 Injection
SQL, NoSQL, LDAP, OS command, XSS, XPath, expression language.

## A04:2021 Insecure Design
Missing control design, lack of threat modeling, missing rate limiting.

## A05:2021 Security Misconfiguration
Defaults, verbose errors, unnecessary features, outdated headers, cloud misconfigurations.

## A06:2021 Vulnerable and Outdated Components
CVEs in libs, no SBOM, no dependency scanning.

## A07:2021 Identification and Authentication Failures
Missing stuffing protection, weak recovery, missing MFA, session prediction.

## A08:2021 Software and Data Integrity Failures
Auto-update without verification, untrusted deserialization, CI/CD without integrity.

## A09:2021 Security Logging and Monitoring Failures
Insufficient logging, no integrity protection, no alerting, no IR capability.

## A10:2021 SSRF
User-supplied URL fetch without validation. Cloud metadata, internal scanning, file:// abuse.

Source: https://owasp.org/Top10/

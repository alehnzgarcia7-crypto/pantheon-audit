# OWASP ASVS 5.0 Level 3 Checklist

14 chapters. L3 = critical systems.

## Ch1 Architecture
Secure SDLC, auth/session/access/input/crypto/error/data/comms/malicious/business-logic/file/API/config architecture documented.

## Ch2 Authentication
Anti-automation, NIST 800-63B passwords, Argon2/bcrypt/scrypt/PBKDF2 storage, recovery without security questions, OTP, out-of-band, SSO, WebAuthn/client certs, service auth.

## Ch3 Session
Random unguessable IDs, Secure+HttpOnly+SameSite=Strict cookies for L3, timeout/logout/concurrent limits, JWT considerations, federated re-auth.

## Ch4 Access Control
Deny by default, server-side enforced, vertical authorization, admin interfaces protected.

## Ch5 Validation
Input validation allowlist/length/type/range/format, sanitization HTML/SQL/command/LDAP/XPath/JSON, output encoding, memory/string safety, deserialization prevention.

## Ch6 Stored Crypto
Data classification, approved algorithms (no MD5/SHA1/DES/RC4), CSPRNG only, vault for secrets.

## Ch7 Errors and Logging
Log privileged actions/auth/access failures, centralized immutable integrity-protected, no PII at L3, encrypted at rest, no stack traces to users.

## Ch8 Data Protection
Classification labels, cache controls, no sensitive in localStorage, encryption at rest.

## Ch9 Communications
TLS 1.2+ mandatory, 1.3 preferred, cert validation, pinning at L3.

## Ch10 Malicious Code
Sign and verify code, SCA scanning, dependency confusion prevention, SRI.

## Ch11 Business Logic
Sequential processing, anti-automation, anti-replay.

## Ch12 Files
Upload limits, antivirus, separate storage, no execution, outside web root, randomized names, validated paths no traversal, SSRF protection.

## Ch13 API
TLS, auth on all, RESTful method/content-type validation, SOAP/XML, GraphQL depth/complexity limits, no introspection in prod.

## Ch14 Configuration
Reproducible builds, SBOM, vuln scanning, locked versions, no debug endpoints in prod, security headers (CSP HSTS X-Content-Type-Options Referrer-Policy), Host header injection prevention.

Source: https://owasp.org/www-project-application-security-verification-standard/

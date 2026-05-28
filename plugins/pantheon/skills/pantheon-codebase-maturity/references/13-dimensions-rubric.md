# 13-Dimension Maturity Rubric

## Dimension 1: Arithmetic and decimal precision
- **Strong**: BigDecimal/Decimal types for money, explicit precision/scale, overflow checks
- **Satisfactory**: Decimal for money, basic overflow awareness
- **Moderate**: Float for money in non-critical paths, some overflow awareness
- **Weak**: Float for money, no overflow protection
- **Missing**: Float arithmetic in financial calculations, integer overflows possible

## Dimension 2: Authentication and authorization
- **Strong**: WebAuthn/MFA mandatory, centralized policy engine, ABAC/ReBAC, deny by default, audit logged
- **Satisfactory**: MFA available, RBAC implemented, server-side enforced
- **Moderate**: Basic auth/RBAC, some inconsistencies
- **Weak**: Auth implemented but bypassable, authorization scattered
- **Missing**: Authentication broken or absent, no authorization model

## Dimension 3: Comments and documentation
- **Strong**: WHY comments throughout, ADRs for architectural decisions, code self-documenting
- **Satisfactory**: Sufficient comments, README adequate
- **Moderate**: Some areas commented, others not
- **Weak**: Sparse comments, outdated documentation
- **Missing**: No comments or all WHAT not WHY

## Dimension 4: Cryptography
- **Strong**: Well-vetted libraries (libsodium, ring, age), formal verification where possible, post-quantum readiness plan, hardware-backed keys
- **Satisfactory**: Modern algorithms, proper key management, CSPRNG
- **Moderate**: Acceptable algorithms, some key management gaps
- **Weak**: Outdated algorithms (SHA1, MD5 for security), poor key management
- **Missing**: Roll-your-own crypto, hardcoded keys, weak random

## Dimension 5: Data handling
- **Strong**: Input validation centralized, output encoding context-aware, parameterized queries, allowlist-based
- **Satisfactory**: Validation present, parameterized queries, basic sanitization
- **Moderate**: Some validation, occasional manual escaping
- **Weak**: Inconsistent validation, manual string concatenation
- **Missing**: SQL injection trivially exploitable, no input validation

## Dimension 6: Dependencies management
- **Strong**: SBOM generated, signed provenance (SLSA L3+), automated PRs for security updates, dependency confusion prevention, single-maintainer risk monitored
- **Satisfactory**: Pinned versions, regular updates, vulnerability scanning
- **Moderate**: Pinned versions, ad-hoc updates
- **Weak**: Unpinned, manual updates, no scanning
- **Missing**: No dependency hygiene, vulnerable libs

## Dimension 7: Documentation (external)
- **Strong**: README complete, architecture docs, runbooks, threat model, ADRs
- **Satisfactory**: README and basic architecture
- **Moderate**: README only
- **Weak**: Sparse README
- **Missing**: No external documentation

## Dimension 8: Error reporting and handling
- **Strong**: Structured errors with context, no information disclosure in user errors, recoverable vs unrecoverable distinguished, Sentry/structured logging
- **Satisfactory**: Errors handled, basic logging
- **Moderate**: Most errors handled, some stack traces leak
- **Weak**: Inconsistent handling, frequent leaks
- **Missing**: Unhandled exceptions everywhere, verbose errors to users

## Dimension 9: Logging and monitoring
- **Strong**: Structured logging, centralized (ELK/Splunk/Datadog), real-time alerting, log integrity protected, retention policy aligned to compliance
- **Satisfactory**: Centralized logging, basic alerting
- **Moderate**: Some logging, manual review
- **Weak**: Local logs only, no alerting
- **Missing**: No logging or trivially bypassed

## Dimension 10: Memory safety and resource management
- **Strong**: Memory-safe language (Rust, Go, JVM, .NET, JS/TS) or unsafe blocks formally verified, bounded resources, OOM tested
- **Satisfactory**: Memory-safe language, basic resource limits
- **Moderate**: Some unsafe code reviewed
- **Weak**: Unsafe code unreviewed
- **Missing**: C/C++ without static analysis, no resource limits

## Dimension 11: Test suite design and effectiveness
- **Strong**: Unit + integration + E2E, property-based tests, mutation testing, security regression tests, >80% meaningful coverage
- **Satisfactory**: Unit + integration, ~60% coverage
- **Moderate**: Some tests, low coverage
- **Weak**: Sparse tests, no coverage tracking
- **Missing**: No tests or only happy path

## Dimension 12: Configuration management
- **Strong**: Configuration as code (versioned), environment-specific separation, secrets externalized (KMS/Vault), config drift detection
- **Satisfactory**: Env vars + config files, secrets in vault
- **Moderate**: Some config externalization, secrets in env vars
- **Weak**: Secrets in config files, manual deployment
- **Missing**: Hardcoded secrets, no environment separation

## Dimension 13: Threat intelligence integration
- **Strong**: Active threat intel feeds integrated into SOC, attacker emulation regularly tested, deception (honeypots/honey tokens), UEBA
- **Satisfactory**: Periodic threat assessments, basic IOC monitoring
- **Moderate**: Annual threat review, no automation
- **Weak**: No threat intel program
- **Missing**: Unaware of threat landscape

## Aggregate scoring
- 13/13 Strong: ELITE (rare)
- 9-13 Satisfactory+: PRODUCTION-READY
- 7-8 Satisfactory+: CONDITIONAL launch
- <7 Satisfactory+: NOT READY

PANTHEON Launch Decision Document uses this aggregate as one criterion.

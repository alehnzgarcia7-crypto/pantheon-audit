# Architecture Security Review
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Lead personas**: mudge-holistic + latacora-pragmatic

## Purpose
C4 model views overlaid with security risk annotations. Audience: security architects, engineering leadership, regulator-facing architects.

## Populated from state
| Field | Source |
|---|---|
| components | state.json/phases/1/components |
| services | state.json/phases/1/services |
| integrations | state.json/phases/1/integrations |
| trust_boundaries | state.json/phases/2/trust_boundaries |
| design_findings | state.json/findings filtered category design |

## Executive Summary
Architecture risk posture. Top 3 architecture-level findings.

## Architecture as documented
Inventory of components, services, integrations, trust boundaries from architecture docs.

## Architecture as built
Discrepancies vs documented. Code-level review of actual implementation.

## C4 views with risk overlays
Context view, Container view, Component view, and code-level view (selected). Mermaid diagrams with risk annotations.

## Trust boundary analysis
Per boundary: identity at each side, authentication mechanism, authorization policy, audit logging.

## Design-level findings
Each finding in PANTHEON-NNNN format at design level (not implementation bugs).

## Identity architecture
SSO, MFA enforcement, PAM, JIT access, session management.

## Supply chain architecture
Build pipeline, signing, provenance, dependency hygiene.

## Crisis response architecture
IR runbooks, on-call, postmortem culture, regulator notification procedures.

## Regulatory architecture
Multi-jurisdiction obligations mapped to architectural support.

## Recommendations
Architectural improvements prioritized.

## Compliance mappings cited
ISO 27001 A.5 leadership, A.8 asset management, A.12 operations, NIST CSF 2.0 Identify and Protect, NIS2 Art. 21(2)(b) policies.

## Hard fails (validation rules)
- C4 Context and Container views rendered.
- Every trust boundary documented.
- At least one design-level finding (or explicit none-applicable note).
- No em-dashes.

## Signoff
Prepared by: mudge-holistic + latacora-pragmatic
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- C4 model (Simon Brown)
- ISO 27001:2022 Annex A

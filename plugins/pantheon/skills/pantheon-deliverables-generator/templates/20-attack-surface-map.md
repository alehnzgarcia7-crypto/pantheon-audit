# Attack Surface Map
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}
**Lead persona**: bishop-fox-red-team

## Purpose
Attack surface inventory across external, internal, and physical surfaces. Audience: SOC, threat intel, security engineering, executive risk view.

## Populated from state
| Field | Source |
|---|---|
| external_surfaces | state.json/phases/7/attack_surface/external |
| internal_surfaces | state.json/phases/7/attack_surface/internal |
| physical_surfaces | state.json/phases/7/attack_surface/physical |
| leaks | state.json/phases/7/leaks |

## Executive Summary
Surface size, top exposed surfaces by risk score.

## External attack surface
- Domains, subdomains, exposed services
- Open ports per service
- Web endpoints (paths and methods)
- API endpoints
- Identity provider exposure
- DNS records of interest
- Certificates (validity, key strength, SAN coverage)
- GitHub leaks, paste-bin leaks, breach dataset hits

## Internal attack surface
- Service-to-service trust paths
- Privileged access roles and paths
- Lateral movement opportunities
- Privilege escalation routes
- Data store access from compromised services
- Backup access paths

## Physical attack surface (if applicable)
- Office and data center perimeters
- Tailgating risk
- USB and removable media policy enforcement
- Workstation lock policy
- Camera and badge coverage

## Identity surface
- SSO IdP exposure
- MFA enrollment percentage
- Federation trust chain
- API token sprawl
- Service account exposure

## Cloud control plane
- Cloud admin role enumeration
- IAM permission boundary review
- Misconfigured exposures (public buckets, public databases)

## Compliance mappings cited
PCI-DSS Req. 1 network controls, NIST CSF 2.0 Identify (Asset Management), NIS2 Art. 21(2)(g) basic cyber hygiene.

## Hard fails (validation rules)
- External, internal, identity sections present.
- DNS and certificate inventory captured (if external).
- Public-bucket and public-DB scan results captured (if cloud).
- No em-dashes.

## Signoff
Prepared by: bishop-fox-red-team + project-zero-researcher
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- LOLBAS, GTFOBins, OWASP Amass, ProjectDiscovery tools

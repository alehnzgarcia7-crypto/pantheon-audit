# Data Flow Diagram
## {{project_name}}

**Audit ID**: {{audit_id}}
**Generated**: {{timestamp}}

## Purpose
Data flow diagrams (DFD) with trust boundaries and classification annotations. Audience: security architects, privacy officers (LINDDUN consumers), DPIA preparers.

## Populated from state
| Field | Source |
|---|---|
| processes | state.json/phases/1/processes |
| data_stores | state.json/phases/1/data_stores |
| external_entities | state.json/phases/1/external_entities |
| data_flows | state.json/phases/1/data_flows |
| trust_boundaries | state.json/phases/2/trust_boundaries |
| pii_inventory | state.json/phases/2/pii_inventory |

## Executive Summary
Number of DFD elements, trust boundaries, PII-processing flows.

## Level 0: Context DFD
Mermaid diagram with external entities, top-level process, and primary data stores. Trust boundaries marked.

## Level 1: System DFD
Mermaid diagram with all major processes, data stores, and flows. Trust boundaries marked. PII flows highlighted.

## Level 2 DFDs (per critical process)
For each Tier-1 or Tier-2 process: dedicated Level 2 DFD.

## Data classification
Per data store and flow: classification (Public, Internal, Confidential, Restricted, Regulated). Volume estimate.

## PII inventory
LFPDPPP / GDPR categories per PII type. Storage location, retention period, processing purpose.

## Cross-border data flows
Per cross-border flow: source jurisdiction, destination jurisdiction, legal basis (SCC, BCR, adequacy decision), data minimization status.

## Encryption posture per flow
Per flow: TLS version, certificate validation, field-level encryption status, at-rest encryption.

## Compliance mappings cited
GDPR Art. 30 records of processing, LFPDPPP 2025 sistema de tratamiento, HIPAA risk analysis, PCI-DSS data flow diagrams.

## Hard fails (validation rules)
- Level 0 and Level 1 DFDs rendered.
- Every PII data store appears in PII inventory.
- Every trust boundary marked.
- No em-dashes.

## Signoff
Prepared by: mudge-holistic + cure53-web-app
Reviewed by: Adversarial Judge
Mapped by: Compliance Mapper

## References
- Adam Shostack threat modeling
- Mermaid diagram syntax

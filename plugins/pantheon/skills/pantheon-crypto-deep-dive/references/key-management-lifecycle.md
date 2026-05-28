# Key Management Lifecycle

## Phases
1. Generation: CSPRNG, sufficient entropy, appropriate length
2. Distribution: secure channel, no email/Slack
3. Storage: HSM > KMS > sealed secrets > env vars > config file
4. Usage: minimum privilege, audit logged
5. Rotation: scheduled, automated, support multiple active keys during rotation
6. Revocation: immediate on compromise, propagation verified
7. Destruction: cryptographic zeroization, no backups retained

## Storage hierarchy (most secure first)
1. Hardware Security Module (HSM): YubiHSM, AWS CloudHSM, Azure Dedicated HSM
2. Cloud KMS: AWS KMS, Azure Key Vault, GCP KMS
3. Sealed secrets: SOPS, sealed-secrets controller for K8s
4. Secret manager: HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager
5. Environment variables (acceptable for low-stakes)
6. Config files: anti-pattern unless encrypted

## Anti-patterns (findings)
- Hardcoded keys in source
- Keys in config files committed to git
- Keys in Docker images
- Keys in CI/CD logs
- Keys with no rotation
- Shared keys across environments (dev = staging = prod)
- Long-lived keys for short-lived workloads
- Symmetric keys distributed via insecure channels

## Cloud KMS specifics
- AWS KMS: use envelope encryption, separate keys per workload, key policies restrictive
- Azure Key Vault: managed identities preferred, no shared service principals
- GCP KMS: separate key rings per environment, IAM least privilege

## Verification checklist
1. Where are keys stored? (path or service)
2. Who can read keys? (IAM/RBAC)
3. Are keys rotated? (schedule, mechanism, automation)
4. What happens on compromise? (revocation, propagation, incident response)
5. Are keys audit-logged? (CloudTrail, audit log)

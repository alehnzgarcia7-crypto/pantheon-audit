# Sigstore Integration

Sigstore is the open-source standard for signing software artifacts. Keyless signing via OIDC identity.

## Components
- **Cosign**: container and artifact signing
- **Rekor**: transparency log for signatures (immutable, public, append-only)
- **Fulcio**: certificate authority issuing short-lived signing certs

## Signing workflow (CI/CD)
```yaml
- name: Sign container with cosign
  env:
    COSIGN_EXPERIMENTAL: 1
  run: |
    cosign sign --yes ghcr.io/myorg/myapp@${{ steps.build.outputs.digest }}
```

This:
1. Authenticates to Fulcio via OIDC (GitHub Actions identity)
2. Receives short-lived cert (10 min validity)
3. Signs artifact digest
4. Records signature in Rekor transparency log

## Verification workflow (deployment)
```bash
cosign verify ghcr.io/myorg/myapp:v1.0 \
  --certificate-identity=https://github.com/myorg/myapp/.github/workflows/release.yml@refs/heads/main \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com
```

This verifies:
1. Artifact was signed by GitHub Actions in expected repo
2. From expected workflow file
3. From expected branch
4. Signature recorded in Rekor (cannot be silently revoked)

## Common findings
- Container images deployed without signing: High
- No verification at deployment time: Critical (defeats purpose)
- Verification accepts any identity: Critical
- Cosign verify without `--certificate-identity`: Critical

## Integration patterns

### Kubernetes admission control
Sigstore policy controller blocks unsigned image deployment:
```yaml
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
spec:
  images:
    - glob: ghcr.io/myorg/**
  authorities:
    - keyless:
        identities:
          - issuer: https://token.actions.githubusercontent.com
            subject: https://github.com/myorg/.+
```

### Container registry policy
Docker Content Trust + cosign integration.

### CI/CD attestation chain
Build provenance signed, deployment verifies provenance, links artifact to source code commit verifiably.

## References
- Sigstore: sigstore.dev
- "Sigstore: software signing for everybody" academic paper (USENIX Security 2023)
- GitHub OIDC docs
- Policy controller: github.com/sigstore/policy-controller

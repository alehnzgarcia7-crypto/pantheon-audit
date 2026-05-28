# SLSA v1.2 Source Track Attestation

**Audit ID**: <uuid>  
**Generated**: <ISO-8601>  
**Phase**: P11  
**Baseline reference**: SLSA v1.2 RC2 Source Track (October 21, 2025, Finding 5.6.8.5); SLSA v1.1 (April 2025, Finding 5.6.8.4)

## Purpose
Per SLSA v1.2 Source Track, attest two-party review controls and Threat B "Modifying the source" coverage.

## Repository identification
| Field | Value |
|---|---|
| Repository | <owner/repo> |
| Forge | <GitHub / GitLab / Bitbucket / Codeberg> |
| Default branch | <main/master> |
| Source Track Level claim | <L1 / L2 / L3> |

## Two-party review controls
- [ ] Branch protection enabled on default branch
- [ ] PR-only merge enforced
- [ ] Required approvals >= 1 (L2) or >= 2 (L3)
- [ ] Stale approvals dismissed on new commits
- [ ] Force-push disabled
- [ ] Code-owner review required for sensitive paths
- [ ] Admin bypass disabled or audit-logged

## Threat B coverage (Modifying the source)
- [ ] All commits signed (Sigstore Cosign git signing or GPG)
- [ ] Signed-commit policy enforced via CI gate
- [ ] Bot commits restricted to specific actors with attestation

## SLSA Source Track evidence
```json
{
  "type": "https://slsa.dev/source-track/v1.2",
  "predicate": {
    "repository_uri": "https://github.com/<owner>/<repo>",
    "branch": "main",
    "level": "L2",
    "two_party_review": true,
    "signed_commits": true,
    "audited_period": {"from": "<ISO>", "to": "<ISO>"}
  }
}
```

## Build Track evidence (SLSA v1.1, complementary)
- [ ] Build platform isolated and hermetic
- [ ] Provenance signed and stored
- [ ] external_parameters, dependency digests, invocation metadata present per v1.1

## Findings
| Finding ID | Title | Severity |
|---|---|---|
| PANTHEON-<NNNN> | <title> | <severity> |

## Hard fails
- [ ] Default branch without protection
- [ ] Force-push enabled
- [ ] Admin bypass enabled without audit trail
- [ ] No signed commits

## Signoff
- pantheon-supply-chain-slsa skill output
- Date: <ISO-8601>

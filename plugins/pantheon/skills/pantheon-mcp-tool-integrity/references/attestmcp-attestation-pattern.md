# ATTESTMCP Attestation Pattern

Derived from Maloyan and Namiot, "Breaking the Protocol" (arXiv:2601.17549, January 2026).

## Attestation manifest schema (JSON)

```json
{
  "mcp_server_name": "string",
  "version": "semver",
  "signed_by": "sigstore-identity",
  "signature": "base64-cosign-bundle-v3",
  "tools": [
    {
      "tool_name": "string",
      "description_sha256": "hex",
      "expected_inputs_schema": {},
      "expected_outputs_schema": {},
      "permitted_filesystem_paths": ["allowlist"],
      "permitted_network_egress": ["allowlist"],
      "secrets_access_required": []
    }
  ],
  "rekor_entry_uri": "https://rekor.../api/v2/log/entries/<sharded-tile-uri>"
}
```

## Verification flow
1. Fetch manifest via MCP server's `server_info` extension method
2. `cosign verify-blob --bundle <bundle> --signing-config <config> --trusted-root <root> <manifest.json>`
3. For each tool the agent intends to call: lookup `description_sha256`, compute SHA-256 of received `tool.description`, compare. Mismatch is auto-reject.
4. Compare requested filesystem paths against `permitted_filesystem_paths`. Out-of-scope auto-reject.
5. Compare requested network egress against `permitted_network_egress`. Out-of-scope auto-reject.

## Failure modes catalogued
- Manifest unavailable: reject with `MCP_MANIFEST_NOT_SIGNED`
- Signature invalid: reject with `MCP_SIGNATURE_FAIL`
- Description hash mismatch: reject with `MCP_TOOL_DESCRIPTION_TAMPERED`
- Out-of-scope filesystem: reject with `MCP_FS_OUT_OF_SCOPE`
- Out-of-scope egress: reject with `MCP_EGRESS_OUT_OF_SCOPE`

## References
- arXiv:2601.17549 (Maloyan, Namiot, January 2026)
- arXiv:2603.22489 (Lin, Milani Fard, March 2026)
- Sigstore Cosign v3 bundle spec

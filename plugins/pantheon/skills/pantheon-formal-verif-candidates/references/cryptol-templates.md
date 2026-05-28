# Cryptol Templates for Crypto Verification

Cryptol is Galois Inc's DSL for cryptographic algorithm specification and verification. Paired with SAW (Software Analysis Workbench) for proof.

## When to use Cryptol
- Cryptographic primitive correctness (HMAC, AEAD, signatures, KDF)
- Bit-level cryptographic operations
- Equivalence checking between reference spec and implementation

## Template: HMAC verification
```cryptol
HMAC : {n} (fin n, n >= 1) => [256] -> [n] -> [256]
HMAC key msg = sha256 (opad ^ paddedKey # sha256 (ipad ^ paddedKey # msg))
  where
    paddedKey = if `n > 64 then sha256 key # zero else key # zero
    ipad = repeat 0x36
    opad = repeat 0x5c
```

## SAW proof obligation
```saw
let hmac_proof = do {
  ll <- llvm_load_module "hmac.bc";
  llvm_verify ll "hmac_sha256" [] false hmac_spec abc;
};
```

## Examples in production
- AWS s2n: TLS handshake state machine + HMAC verified via SAW
- Curve25519: scalar multiplication verified via Cryptol
- Galois open-source CryptoVerif models

## Effort estimate
- Single primitive (HMAC, ChaCha20): 2-4 person-weeks initial proof, 1 week ongoing
- Protocol layer (TLS handshake): 6-12 person-months
- Full TLS stack (project Everest): person-years

## CI integration
- Cryptol + SAW available as Docker images
- GitHub Actions can run proofs on PR
- Failure should block merge (proof-as-test)

## References
- Cryptol homepage: cryptol.net
- SAW: saw.galois.com
- "Continuous Formal Verification of Amazon s2n" Chudnov et al.

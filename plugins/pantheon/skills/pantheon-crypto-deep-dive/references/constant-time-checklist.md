# Constant-Time Comparison Checklist

Timing side-channel attacks extract secrets from non-constant-time comparisons.

## Required for
- HMAC verification
- Password/token comparison
- Cryptographic signature verification
- Authentication tokens
- API keys
- Any secret comparison

## Language-specific constant-time functions
- Node.js: `crypto.timingSafeEqual(a, b)`
- Python: `hmac.compare_digest(a, b)`
- Go: `subtle.ConstantTimeCompare(a, b)`
- Java: `MessageDigest.isEqual(a, b)` (constant-time since Java 6u17)
- Rust: `subtle::ConstantTimeEq` trait
- C: `CRYPTO_memcmp` (OpenSSL) or `sodium_memcmp` (libsodium)

## Anti-patterns (findings)
- `if (token === userInput)` in JS
- `if (token == userInput)` in Python (==)
- `bytes.Equal(a, b)` in Go (not constant-time)
- `string.equals` in Java
- `==` byte comparison in Rust without subtle crate
- Loops that early-exit on mismatch

## Verification
Search codebase for: `==`, `===`, `.equals(`, `bytes.Equal`, `memcmp`, manual byte loops in auth paths. Each is potential finding.

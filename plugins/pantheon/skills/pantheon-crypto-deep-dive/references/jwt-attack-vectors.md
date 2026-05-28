# JWT Attack Vectors

## Alg confusion attacks
- `alg: none`: server accepts unsigned tokens
- HS256 vs RS256 confusion: attacker uses public key as HMAC secret
- HS256 vs ES256 confusion: similar
- Key confusion via `kid` header injection

## Verification requirements
1. Whitelist allowed algorithms (do not trust `alg` header)
2. Verify signature before reading claims
3. Validate `exp` (expiration) and `nbf` (not before)
4. Validate `iss` (issuer) against expected
5. Validate `aud` (audience) against expected
6. Validate `kid` against known key set, no path traversal in kid
7. Rotate signing keys, support multiple kids during rotation

## Anti-patterns
- `jwt.decode(token)` without verification (Node.js jsonwebtoken)
- Accepting `alg: none`
- Trusting `alg` from header for algorithm selection
- Storing JWTs in localStorage (XSS theft)
- Long expiration (>15 min for access tokens)
- No refresh token rotation

## Library-specific
- `jsonwebtoken` (Node.js): Use `jwt.verify(token, secret, {algorithms: ['RS256']})`. Never `jwt.decode` for trust.
- `PyJWT` (Python): `jwt.decode(token, key, algorithms=["RS256"])`. Pass `algorithms` explicit.
- `golang-jwt/jwt` (Go): Use `ParseWithClaims`, validate alg in `KeyFunc`.
- `jjwt` (Java): Use `parser().verifyWith(key).build()`.

## References
- CVE-2018-1000531 (jsonwebtoken vuln)
- "Critical vulnerabilities in JSON Web Token libraries" (Tim McLean, 2015)
- Auth0 JWT attack handbook

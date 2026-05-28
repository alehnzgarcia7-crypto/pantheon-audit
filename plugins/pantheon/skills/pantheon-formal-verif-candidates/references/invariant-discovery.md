# Invariant Discovery

Before formal proof, discover invariants candidate must satisfy.

## Categories

### Functional invariants
- "HMAC(key, m) is deterministic given key and m"
- "Decrypt(key, Encrypt(key, m)) = m"
- "Verify(pk, m, Sign(sk, m)) = true"

### Safety invariants
- "Balance never negative"
- "Sum of all balances = total supply"
- "Authenticated users only access own resources"
- "Transaction id is unique"

### Liveness invariants
- "Consensus reaches agreement in N+1 rounds (BFT)"
- "Every transaction submitted eventually committed or rejected"
- "No deadlock under concurrent access"

### Temporal invariants
- "Always: if X then eventually Y"
- "Never: state S1 directly followed by state S3 without S2"

## Discovery techniques

1. **Specification reading**: documented requirements often state invariants implicitly
2. **Code reading**: assertions, exceptions, validation logic encode invariants
3. **Test reading**: test cases often verify invariants
4. **Behavior observation**: run system, observe properties that hold
5. **Domain expert interview**: experts know unwritten invariants
6. **Failure analysis**: bugs reveal violated invariants

## Formal expression

For Cryptol/SAW: bit-level functional specification.
For TLA+: temporal logic formula.
For Coq/Lean: dependent type or theorem.
For F*: refinement type predicate.
For Hypothesis/fast-check: Python/JS predicate function.

## Anti-patterns

- "Should not crash" (too weak)
- "Works correctly" (vague)
- "Tests pass" (tests can be wrong)
- "Common case works" (invariants hold always)

## Examples

Bad: "Login works"
Good: "For all (user, password) where User.exists(user) and User.password_hash(user) = hash(password), login(user, password) returns valid session token"

Bad: "Transfer is correct"
Good: "For all transfers (from, to, amount) where amount > 0 and balance(from) >= amount, after transfer: balance(from) = pre_balance(from) - amount AND balance(to) = pre_balance(to) + amount"

## References
- "How AWS uses formal methods" (Chris Newcombe et al., 2015)
- "Specifying Systems" (Lamport, on TLA+)
- "Software Foundations" (Pierce et al., on Coq)

# False Positive Patterns

Common FP patterns to recognize and reject.

## Pattern 1: Defense-in-depth not considered
Finding claims XYZ bug, but auth middleware blocks before XYZ code path executes.
Cross-check: read middleware chain. If middleware blocks: WITHDRAW.

## Pattern 2: Environment-specific
Finding claims bug exists, but only in dev configuration. Production uses different config.
Cross-check: read NODE_ENV/ENVIRONMENT checks, prod config files. If prod safe: WITHDRAW.

## Pattern 3: Theoretical without preconditions
"This would be exploitable if attacker had X, Y, Z" but X, Y, Z don't exist in this codebase.
Cross-check: verify each precondition. If preconditions don't exist: WITHDRAW or downgrade severity.

## Pattern 4: Already mitigated
Finding describes XYZ, but other code path sanitizes before reaching vulnerable function.
Cross-check: trace input flow end-to-end. If sanitized: WITHDRAW.

## Pattern 5: Misread of language semantics
JavaScript `==` vs `===`, Python list comparison vs identity, Go nil semantics. Finding assumes wrong semantics.
Cross-check: verify language behavior. If finding wrong: WITHDRAW.

## Pattern 6: Library does the right thing
Finding claims library X is vulnerable. Read library docs/code: library handles edge case correctly.
Cross-check: read library source. If safe: WITHDRAW.

## Pattern 7: Outdated CVE pattern
Finding cites CVE-XXXX-XXXX. Codebase uses patched library version.
Cross-check: verify version. If patched: WITHDRAW.

## Pattern 8: Race condition theoretical
Race condition possible in principle but not exploitable due to:
- Database transaction isolation level (SERIALIZABLE)
- Distributed lock acquisition
- Idempotency keys
- Compare-and-swap operations
Cross-check: read transactional code. If safe: WITHDRAW or downgrade.

## Pattern 9: Validation present
Finding assumes no input validation. Read validation middleware: zod schema, joi, manual checks.
Cross-check: trace input. If validated: WITHDRAW.

## Pattern 10: Severity inflated for visibility
Finding rated Critical but real impact is Medium. Reporter inflates for attention.
Cross-check: severity rubric. Downgrade as appropriate.

## When in doubt
- Default to skepticism
- Verify by reading code, not trusting reporter
- Better to WITHDRAW false positive than accept and inflate count
- DISPUTE if cannot reach conclusion in budget

## Anti-patterns for judge
- Accepting findings to appear thorough
- Softening WITHDRAW because persona has high status
- Skipping verification because finding "looks right"
- Accepting "I think this might be" without PoC

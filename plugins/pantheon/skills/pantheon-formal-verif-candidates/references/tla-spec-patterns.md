# TLA+ Specification Patterns

TLA+ is Leslie Lamport's specification language for concurrent and distributed systems. Used by AWS for DynamoDB, S3, EBS verification.

## When to use TLA+
- Distributed consensus algorithms
- Eventually consistent data stores
- Replication protocols
- State machines with concurrent access
- Locking and synchronization
- Workflow orchestration

## Template: Distributed counter

```tla
VARIABLES counter, pending

Init == counter = 0 /\ pending = {}

Increment(id) == /\ id \notin pending
                 /\ pending' = pending \cup {id}
                 /\ counter' = counter + 1

Spec == Init /\ [][\E id \in Ids : Increment(id)]_<<counter, pending>>

Invariant == counter = Cardinality(pending)
```

## Common invariants for distributed systems
- Safety: "At most one leader at any time"
- Liveness: "Every transaction eventually commits or aborts"
- Consistency: "All replicas converge to same state"
- Progress: "If client sends request, client eventually receives response"

## TLC model checker
- Bounded exploration of state space
- Finds counterexamples to invariants
- Output: specific trace violating invariant

## TLAPS theorem prover
- Mathematical proof of invariants (not just bounded check)
- Steeper learning curve
- Used for highest-assurance proofs

## Effort estimate
- Simple state machine: 1-2 person-weeks
- Distributed consensus: 2-6 person-months
- Production system spec: 6-18 person-months

## AWS examples
- DynamoDB: replication protocol verified
- S3: durability properties verified
- EBS: replication protocol verified
- Athena: snapshot isolation verified

## CI integration
- TLC can run in CI on PR
- Counterexamples block merge
- TLA+ Toolbox or pTLA+ for development

## References
- Lamport, L. (2002). Specifying Systems.
- "How Amazon Web Services uses formal methods" (CACM 2015)
- TLA+ home page: lamport.azurewebsites.net/tla/tla.html
- Hillel Wayne's "Practical TLA+"

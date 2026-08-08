# ADR-0009 Semantic Constraints for Relations

## Status

Accepted

## Context

RFC-0025 defines the canonical internal representation of relations
within the ATON Foundation.

The canonical representation identifies a relation by its predicate and
target. This provides a structural representation, but it does not by
itself determine whether a relation is semantically valid for the source
and target entity types involved.

NOTE-0021 identified this limitation.

A predicate may be meaningful only for specific combinations of source
and target types.

For example:

    Finding --motivates--> Note

may be semantically valid, while:

    Note --motivates--> Decision

may be semantically invalid.

Both relations can nevertheless be structurally representable using the
same predicate.

Therefore, structural relation validity and semantic relation validity
must be distinguished.

## Decision

ATON SHALL define semantic constraints for relation predicates at the
ontology level.

Each relation predicate SHALL have a semantic contract defining the
allowed source and target ontology types.

The semantic contract SHALL determine at minimum:

- which ontology types may occur as the source of the predicate;
- which ontology types may occur as the target of the predicate.

A relation SHALL be considered semantically valid only when both its
source type and target type satisfy the constraints defined for its
predicate.

The predicate name alone SHALL NOT be sufficient to establish semantic
validity.

The canonical Relation domain object defined by RFC-0025 SHALL remain
independent of these semantic constraints.

The ontology SHALL therefore provide the semantic layer that gives a
predicate its domain and range.

## Architectural Separation

The following responsibilities SHALL remain separate:

### Relation Model

The Relation model defines how a relation is represented internally.

It provides:

- predicate;
- target;
- source context through the owning Entity.

The Relation model SHALL NOT contain ontology-specific domain and range
definitions.

### Ontology

The ontology defines the semantic meaning and applicability of relation
predicates.

It provides:

- predicate semantics;
- allowed source types;
- allowed target types.

### Verification

Verification SHALL evaluate concrete relations against the semantic
constraints defined by the ontology.

Verification SHALL distinguish at least:

- structurally valid relations;
- semantically valid relations;
- structurally valid but semantically invalid relations.

### RFC

A subsequent RFC SHALL define the concrete serialization and verification
mechanism for semantic relation constraints.

This ADR does not prescribe the final serialization format.

## Source and Target Semantics

Relation validity SHALL be evaluated using the following conceptual model:

    Source Type --Predicate--> Target Type

A predicate therefore has a constrained domain and range.

The domain identifies the permitted source types.

The range identifies the permitted target types.

A relation is valid only when the concrete source and target satisfy both
constraints.

The architecture SHALL support predicates whose domain or range contains
multiple ontology types.

The architecture SHALL also permit future ontology mechanisms such as
type specialization to participate in constraint evaluation.

The exact inheritance and specialization rules are deferred to the
corresponding RFC.

## Invalid Relations

A relation SHALL NOT become semantically valid merely because:

- the predicate exists;
- the target artifact exists;
- the source artifact exists;
- the relation is syntactically well formed.

For example, if `motivates` is defined with a domain that includes
`Finding` and a range that includes `Note`, then:

    Finding --motivates--> Note

is semantically valid.

A relation such as:

    Note --motivates--> Decision

is semantically invalid unless the ontology explicitly permits
`Note` as a source and `Decision` as a target for `motivates`.

## Consequences

### Positive

- Relation semantics become explicitly defined.
- Invalid source/predicate/target combinations can be detected.
- The ontology becomes the authoritative source for predicate semantics.
- The canonical Relation model remains simple and format independent.
- Verification can distinguish structural correctness from semantic
  correctness.
- Future tooling can reason about relation applicability.

### Negative

- The ontology must maintain predicate constraints.
- Verification becomes dependent on ontology information.
- Existing relations may require classification or correction.
- A migration mechanism will be required when semantic constraints are
  introduced.

## Migration

Existing relations SHALL initially remain structurally representable.

Semantic verification SHALL be introduced after the ontology contains
the required predicate constraints.

Existing relations that do not satisfy a defined semantic constraint
SHALL be reported as semantic verification issues.

They SHALL NOT be silently rewritten by the verifier.

Migration and remediation rules SHALL be defined by the subsequent RFC.

## Alternatives Considered

### Constraints inside the Relation object

Rejected.

This would couple the canonical Relation model to ontology semantics and
would duplicate semantic definitions across individual relations.

### Constraints only in application code

Rejected.

Application-specific validation would prevent the ontology from being
the authoritative semantic source and could lead to inconsistent
interpretations between tools.

### Predicate name without domain and range

Rejected.

A predicate name alone cannot establish whether a concrete source and
target combination is semantically valid.

## Decision Boundary

This ADR establishes the architectural principle that relation predicates
have ontology-defined semantic constraints.

It does not define:

- the final YAML representation;
- the exact predicate schema;
- inheritance algorithms;
- cardinality constraints;
- inverse predicates;
- validation severity;
- migration tooling.

Those details SHALL be specified by the subsequent RFC.

## References

- NOTE-0021 Semantic Constraints for Relations
- RFC-0025 Canonical Relation Model
- ENTITY-0001 Universal Entity Model

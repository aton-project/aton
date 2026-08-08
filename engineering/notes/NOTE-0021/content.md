# NOTE-0021 Semantic Constraints for Relations

## Status

Open

## Observation

The current ATON relation model identifies a relation by its predicate
and target, but does not yet express which source and target entity types
are semantically valid for a given predicate.

As a result, a relation may be structurally valid while its semantic
meaning is not valid for the involved source and target types.

## Problem

A predicate alone does not determine the complete semantic contract of
a relation.

For example, the predicate `motivates` may be meaningful for a
particular source and target type combination, while the same predicate
may be meaningless for another combination.

Therefore, the current relation representation cannot distinguish
between:

- a structurally valid relation
- a semantically valid relation

## Example

A relation such as:

    Finding --motivates--> Note

may be semantically valid.

A relation such as:

    Note --motivates--> Decision

must not be assumed to be valid merely because the predicate
`motivates` exists.

The validity depends on the semantic types of the source and target
entities.

## Impact

Without semantic constraints on relations:

- invalid relation combinations cannot be reliably detected;
- the ontology cannot fully define relation semantics;
- verification can establish that a target exists, but cannot establish
  that the relation itself is semantically permitted;
- tooling may accept structurally valid but semantically invalid
  relations.

## Scope

This Note records the observed limitation of the current relation model.

It does not define the solution.

In particular, this Note does not decide:

- how source and target constraints shall be represented;
- whether predicates shall define domains and ranges;
- whether constraints belong to the ontology or relation model;
- whether cardinality or inverse relations are required;
- how verification shall enforce semantic constraints.

These decisions are subject to Architecture Board review.

## Expected Outcome

The Architecture Board shall determine whether the ATON architecture
requires an explicit semantic constraint model for relations and, if so,
define the architectural direction.

## References

- RFC-0025 Canonical Relation Model

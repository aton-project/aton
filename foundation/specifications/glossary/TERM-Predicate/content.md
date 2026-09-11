# Predicate

## Definition

A Predicate is a named semantic relation that expresses a defined relationship
between a source Entity and a target Entity in the ATON Engineering Knowledge
Model.

A Predicate gives a relation its semantic meaning and direction.

## Role in ATON

Predicate is a fundamental term of the ATON Engineering Knowledge Model.

A Predicate defines what a relation between two Entities means. It is
directional and is applied from a source Entity to a target Entity.

Concrete Predicates define specific semantic relationships such as:

- governs
- motivates
- references
- refines

Each concrete Predicate defines its own semantic meaning and permitted
source-to-target relationships.

## Relationship to Relations

A Relation represents an occurrence of a Predicate between a source Entity and
a target Entity.

The Predicate defines the meaning of the relationship; the Relation records
its use between specific Entities.

## Relationship to Constraints

A concrete Predicate may define constraints on which source-to-target Concept
pairs are permitted.

These constraints determine whether a relation using the Predicate is
semantically valid within the ATON Engineering Knowledge Model.

## Direction

Predicates are directional.

The direction is expressed as:

    source -> Predicate -> target

The existence of an inverse Predicate does not imply that the original
Predicate may be used in the reverse direction.

## Related Terms

- Entity
- Relation
- Artifact
- Constraint Pattern
- Knowledge Model

## References

- PRED-governs
- PRED-motivates
- PRED-references
- PRED-refines

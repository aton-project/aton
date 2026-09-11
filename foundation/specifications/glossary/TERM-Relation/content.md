# Relation

## Definition

A Relation is a semantic connection between a source Entity and a target Entity
using a defined Predicate.

A Relation represents the occurrence of a Predicate between specific Entities
within the ATON Engineering Knowledge Model.

## Role in ATON

Relation is a fundamental term of the ATON Engineering Knowledge Model.

A Relation connects Entities and expresses a defined semantic relationship
between them.

The meaning of a Relation is determined by its Predicate.

## Relationship to the Relation Model

The normative Relation model is defined by ONT-Relation and ADR-0014 —
Canonical Semantic Relation Model.

The Glossary Entry defines the terminology used to refer to this concept. It
does not replace or redefine the normative Relation model.

## Relationship to Predicate

A Relation uses a Predicate to express its semantic meaning.

The Predicate defines what the relationship means and may constrain which
source-to-target Concept pairs are permitted.

## Direction

Relations are directional unless their Predicate explicitly defines symmetric
semantics.

The direction is expressed as:

    source -> Predicate -> target

The source and target remain distinct concepts.

## Identity

Within the canonical Relation model, a Relation is identified by its:

- source;
- predicate; and
- target.

## Persistence Independence

A Relation is independent of its physical serialization.

A Relation MAY be represented using different persistence formats, but
persistence-specific representations do not change its conceptual meaning or
identity.

## Related Terms

- Entity
- Predicate
- Artifact
- Knowledge Model

## References

- ONT-Relation — Relation
- ENTITY-0001 — Universal Entity Model
- ADR-0014 — Canonical Semantic Relation Model

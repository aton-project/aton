# ENTITY-0001 Universal Entity Model

## Status

Draft

## Purpose

The Entity is the fundamental unit of identifiable engineering knowledge
within ATON.

Every engineering object represented by the ATON Foundation SHALL be
an Entity.

## Definition

An Entity is the smallest independently identifiable unit of engineering
knowledge.

An Entity SHALL have:

- a unique identity
- exactly one conceptual type
- content
- metadata
- relationships to other Entities where applicable

The identity of an Entity SHALL remain stable independently of its
serialization format.

## Identity

Every Entity SHALL be uniquely identifiable within the ATON Foundation.

Entity Identity and Artifact Identity SHALL remain semantically distinct.
In the normal one-Entity/one-Artifact case they MAY use the same identifier
value; distinct meanings SHALL NOT require a second technical Artifact ID.

The identifier SHALL be independent of:

- file name
- directory location
- serialization format
- rendered documentation

## Type

Every Entity SHALL have exactly one primary conceptual type.

The primary type determines the semantic category of the Entity and SHALL be
explicitly declared as `ontologyType`, referencing a canonical ontology
Concept identifier according to ADR-0008.

`ontologyType` belongs to the Engineering Entity. `artifactType`, when
applicable, belongs to the Engineering Artifact representing it. Serializing
both values in `metadata.yaml` SHALL NOT change their semantic ownership.

Specialized engineering concepts such as Requirements, Architecture
Decisions, RFCs, Components, Interfaces and Tests SHALL be represented
as specialized Entity types.

## Content

An Entity MAY contain normative or descriptive engineering knowledge.

The representation of content SHALL be independent of the Entity identity.

## Metadata

Metadata describes properties of an Entity that are required for
identification, lifecycle management, classification or processing.

Metadata SHALL remain separate from the primary engineering content.

## Relationships

Entities MAY be related to other Entities.

Relationships SHALL identify their source Entity, relation predicate and
target Entity.

Relationship semantics are defined by the ATON relation model.

## Persistence Independence

The Entity model SHALL be independent of the physical persistence
mechanism.

An Entity MAY be serialized using different formats without changing
its conceptual identity or semantics.

## Specialization

The Entity model provides the foundation for specialized ATON Entity
types.

A specialized type SHALL NOT redefine the fundamental identity model
of an Entity.

Specialization SHALL add domain-specific semantics to the common Entity
model.

## Consequences

The Entity model provides a common conceptual foundation for all ATON
engineering artifacts.

This allows the ATON kernel to operate on a uniform model while
supporting specialized engineering concepts.

## References

- RFC-0025 Canonical Relation Model

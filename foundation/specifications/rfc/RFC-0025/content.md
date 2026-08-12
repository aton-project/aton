# RFC-0025 Canonical Relation Model

## Status

Draft

## Summary

This RFC specifies the canonical internal representation of relations within
the ATON kernel.

The specification implements the architectural principle established by
ADR-0008: every domain concept SHALL have exactly one canonical internal
representation.

## Scope

This RFC specifies:

- the canonical Relation domain object
- supported relation serialization formats
- loader normalization
- canonical kernel representation
- verification requirements
- migration strategy

The semantic definition and validity of relation predicates are outside the
scope of this RFC.

## Relation Domain Object

The kernel SHALL provide a dedicated canonical Relation domain object.

Each Relation SHALL identify:

- a source;
- a predicate; and
- a target.

The source identifies the Engineering Knowledge object from which the
relation originates.

The predicate identifies the canonical relation predicate.

The target identifies the Engineering Knowledge object to which the relation
points.

The canonical Relation domain object SHALL represent the relation itself and
SHALL NOT depend on the serialization format used by the Foundation
repository.

The semantic validity of the predicate for a particular source and target
combination is defined separately by the applicable ontology and semantic
constraint specifications.

## Supported Serialization Formats

The loader SHALL support the relation serialization formats currently present
in the Foundation.

### Legacy List Format

An empty relation set MAY be represented as:

    []
    
### Mapping Format

Relations MAY be represented as a mapping from relation type to target
identifiers:

    references:
      - RFC-0001

    dependsOn:
      - ADR-0003

### Embedded Relation Object Format

Relations MAY be represented explicitly as relation objects:

    relations:
      - type: refines
        target: AX-0001

## Canonical Representation

Regardless of the serialization format, the loader SHALL normalize relation
data into the canonical Relation domain model.

The canonical representation SHALL preserve the semantic identity of:

- the source;
- the predicate; and
- the target.

Kernel components SHALL operate exclusively on the canonical representation.

Kernel components MUST NOT depend on the serialization format of
relations.yaml.

The serialization of a relation SHALL therefore be considered a physical
representation of the canonical Relation domain object and SHALL NOT define
its semantics.

## Loader Requirements

The loader SHALL:

- detect supported relation serialization formats
- parse relation data
- validate the structural representation
- normalize relation data
- construct canonical Relation objects

The loader SHALL be the boundary between serialized Foundation data and the
kernel domain model.

## Verification Requirements

The verification subsystem SHALL operate exclusively on canonical Relation
objects.

Verification rules MUST NOT inspect or interpret the original serialization
format.

Verification MAY validate:

- existence of relation sources;
- existence of relation targets;
- duplicate relations;
- self references;
- structural consistency of Relation objects; and
- consistency between the canonical Relation representation and its
  serialized representation.

Semantic validation of source, predicate and target combinations SHALL be
performed according to the applicable ontology and semantic relation
constraint specifications.

Validation of whether a specific predicate is semantically valid for a given
source and target artifact type is outside the scope of this RFC.

## Predicate Semantics

This RFC defines the structural representation of a relation but does not
define the semantic meaning or allowed usage of individual predicates.

A predicate therefore does not become semantically valid merely because it
can be represented by the canonical Relation domain object.

Semantic constraints MAY define:

- the meaning of a predicate;
- allowed source ontology types;
- allowed target ontology types;
- cardinality;
- inverse predicates;
- symmetry or directionality;
- transitivity; and
- other semantic constraints.

Such rules SHALL be defined by the applicable ontology and semantic relation
constraint specifications.

The canonical Relation domain model SHALL remain independent of these
ontology-specific constraints.

## Migration Strategy

### Phase 1

The loader SHALL support all currently existing relation serialization
formats.

### Phase 2

Foundation artifacts SHALL be migrated toward the preferred serialization
format.

### Phase 3

Legacy serialization formats MAY be removed from the loader once the
Foundation no longer depends on them.

Removal of a legacy format SHALL NOT change the canonical Relation domain model.

## Consequences

The canonical Relation model provides:

- one stable representation inside the kernel
- separation between persistence and domain logic
- simpler verification
- simpler rendering
- consistent handling of relations
- a stable foundation for future ontology validation
- easier support for additional import and export formats

## Future Extensions

The canonical Relation model SHALL provide the foundation for future
ontology-based relation validation.

Future specifications MAY define:

- predicate semantics
- allowed source artifact types
- allowed target artifact types
- inverse predicates
- cardinality constraints
- relation lifecycle rules
- derived and inferred relations

These extensions SHALL build upon the canonical Relation domain model defined
by this RFC.

## References

- ADR-0008 Canonical Domain Models

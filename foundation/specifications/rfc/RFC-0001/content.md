# RFC-0001 — Engineering Entity Model

## Status

Draft

## Summary

This RFC defines the canonical semantic model for Engineering Entities within
the ATON Engineering Knowledge Model.

An Engineering Entity represents a semantically identifiable engineering
concept.

Engineering Entities are logical concepts and are independent of their
physical representation, storage location or presentation.

An Engineering Entity MAY be represented by one or more Engineering Artifacts.

Entity identity and entity evolution are defined separately by RFC-0002 and
the applicable version semantics.

## Motivation

Engineering knowledge consists of identifiable engineering concepts such as
requirements, specifications, components, interfaces, decisions, findings,
tests and other domain concepts.

These concepts must be distinguishable from the physical artifacts used to
represent them.

Without a canonical Entity model, implementations may incorrectly treat:

- files as engineering entities;
- directories as engineering entities;
- document sections as engineering entities; or
- physical representations as semantic identity.

ATON therefore requires a persistence-independent definition of an
Engineering Entity.

## Goals

This RFC SHALL:

- define the semantics of an Engineering Entity;
- distinguish Engineering Entities from Engineering Artifacts;
- establish the relationship between entities and their representations;
- define the role of entities within the Engineering Knowledge Model;
- provide a stable foundation for identity, metadata, relations and versioning;
- support entities represented by one or more physical artifacts; and
- remain independent of persistence and rendering technologies.

## Non Goals

This RFC does not define:

- the complete identity model;
- engineering version semantics;
- artifact serialization formats;
- relation predicate semantics;
- ontology-specific entity types;
- engineering process semantics;
- a specific persistence technology;
- a specific repository structure;
- a specific user interface; or
- a mandatory physical representation format.

Entity identity is defined by RFC-0002.

Engineering version semantics are defined by the applicable version model.

## Proposal

### Engineering Entity

An Engineering Entity SHALL represent a semantically identifiable concept
within the Engineering Knowledge Model.

An Engineering Entity SHALL have semantic meaning independent of the physical
representation used to store or present it.

Examples MAY include:

- Requirement;
- Specification;
- Component;
- Interface;
- Architecture Decision;
- Finding;
- Test;
- Review;
- Process;
- Baseline;
- Release; or
- another concept defined by the applicable ontology.

The concrete semantic type of an Engineering Entity SHALL be determined by the
applicable ontology.

### Entity Identity

An Engineering Entity SHALL be identifiable independently of its physical
representation.

The identity of an Engineering Entity SHALL NOT be determined solely by:

- file name;
- directory path;
- repository location;
- document title;
- database identifier; or
- URL.

An implementation MAY use such information as an access mechanism, but such
information SHALL NOT define the semantic identity of the entity.

The canonical identity semantics are defined by RFC-0002.

### Entity and Artifact

An Engineering Entity SHALL be distinct from an Engineering Artifact.

An Engineering Artifact represents a physical or logical representation of
engineering knowledge.

An Engineering Entity represents the semantic concept represented by that
artifact.

The relationship may therefore be expressed as:

    Engineering Entity
            |
            | represented by
            ▼
    Engineering Artifact

One Engineering Entity MAY be represented by multiple Engineering Artifacts.

One Engineering Artifact MAY contain or represent multiple Engineering
Entities.

The existence of an artifact SHALL NOT by itself imply that the artifact and
the entity are the same object.

### Entity and Metadata

Metadata MAY describe an Engineering Entity.

Metadata SHALL NOT redefine the semantic identity of the entity unless the
applicable normative model explicitly assigns such semantics to the metadata.

Metadata associated with an entity SHALL therefore remain distinguishable from
the physical representation of the entity.

The canonical metadata model is defined separately.

### Entity and Relations

Engineering Entities MAY participate in canonical relationships.

Relations SHALL connect semantic engineering concepts rather than merely
physical representations.

For example:

    Requirement
        |
        | refines
        ▼
    Specification

The validity and semantics of such relationships are defined by the
canonical relation model and applicable ontology constraints.

### Entity and Version

An Engineering Entity MAY evolve through multiple Engineering Versions.

The persistent identity of an Engineering Entity SHALL remain stable across
versions of the same engineering concept.

A change to an Engineering Entity SHALL NOT automatically create a new
Engineering Entity identity.

The rules for determining when a new identity is required are defined by
RFC-0002.

Engineering Version semantics are defined separately by the applicable
versioning specification.

### Entity and Physical Representation

An Engineering Entity SHALL remain independent of its physical
representation.

An entity MAY be represented through:

- Markdown;
- YAML;
- JSON;
- a database record;
- an API representation;
- generated documentation;
- another exchange format; or
- another supported representation.

Changing the physical representation SHALL NOT inherently change the identity
or semantic meaning of the Engineering Entity.

The logical-to-physical representation boundary is defined separately by the
applicable architectural decisions and RFCs.

### Entity Addressability

An Engineering Entity SHALL be addressable through its canonical identity.

A physical location MAY provide an access mechanism for an entity, but SHALL
NOT replace its canonical identity.

An implementation MAY therefore resolve an entity through:

- a repository path;
- a URL;
- a database key;
- an API endpoint; or
- another technical mechanism.

Such mechanisms SHALL remain distinguishable from the semantic identity of
the entity.

### Entity Type

An Engineering Entity MAY have an applicable semantic type.

Entity types SHALL be defined by the applicable ontology.

The entity type SHALL describe the semantic class of the entity and SHALL NOT
be inferred solely from its physical storage format.

For example, an entity stored in Markdown does not become a Requirement merely
because it is stored in a Markdown file.

### Entity Participation in the Knowledge Graph

Engineering Entities SHALL be first-class elements of the Engineering
Knowledge Graph.

Entities MAY participate in:

- semantic relations;
- version relationships;
- provenance relationships;
- process relationships;
- baseline membership;
- release membership; and
- other relationships defined by the Engineering Knowledge Model.

The graph semantics are defined independently of the physical representation.

### Entity Containment

An Engineering Entity MAY contain or reference other Engineering Entities
where the applicable ontology defines such a relationship.

Physical containment SHALL NOT automatically imply semantic containment.

For example, placing two entities in the same Markdown document SHALL NOT by
itself establish a semantic relationship between them.

### Canonical Domain Representation

The ATON kernel SHALL operate on a canonical domain representation of
Engineering Entities.

Persistence-specific structures SHALL be normalized before being consumed by
kernel components.

Kernel components SHALL NOT depend directly on repository-specific
serialization structures.

This requirement follows the canonical domain model principle established by
the ATON architecture.

## Consequences

### Positive

- Engineering concepts are separated from their physical representations.
- Entity identity can remain stable across physical changes.
- Multiple artifacts can represent the same engineering concept.
- Entities can participate consistently in the Engineering Knowledge Graph.
- Identity, metadata, relations and versioning can build upon a common entity
  model.
- Alternative persistence and exchange mechanisms remain possible.
- The kernel can operate on stable semantic domain objects.

### Negative

- Implementations must explicitly distinguish entities from artifacts.
- Loaders must normalize physical representations into canonical entities.
- Entity identity requires explicit modeling.
- Ontology definitions are required to establish concrete semantic entity
  types.
- Some physical representations may contain multiple entities and therefore
  require explicit entity extraction or mapping.

## Alternatives

### Treat files as Engineering Entities

Rejected.

Files are physical representations and may contain multiple engineering
entities. File identity must therefore not define engineering identity.

### Treat document sections as Engineering Entities

Rejected.

Document structure is a representation mechanism and may differ between
physical representations.

### Define entity identity through repository paths

Rejected.

Repository paths are implementation-specific and may change without changing
the engineering concept.

### Define a separate entity model for each physical representation

Rejected.

This would create competing semantic models and prevent consistent
interoperability.

### Treat every artifact as one Engineering Entity

Rejected.

A physical artifact MAY represent multiple engineering entities, and one
engineering entity MAY be represented by multiple artifacts.

## Migration

Existing ATON artifacts SHALL be interpreted according to the canonical Entity
model.

Implementations migrating existing repositories SHOULD:

1. identify the engineering concepts represented by existing artifacts;
2. assign or preserve canonical entity identities;
3. distinguish entities from their physical artifacts;
4. establish explicit entity-to-artifact relationships;
5. preserve existing provenance information;
6. normalize representations into the canonical domain model; and
7. establish ontology-specific entity types where applicable.

Migration SHALL NOT assume that every physical artifact represents exactly one
Engineering Entity.

Existing Git history MAY provide provenance evidence but SHALL NOT by itself
define Engineering Entity identity.

## Open Questions

The following questions remain subject to further specification:

- Which universal properties SHALL every Engineering Entity provide?
- Which entity types SHALL be part of the ATON Foundation ontology?
- How should embedded entities be identified within artifacts?
- How should entity extraction from compound artifacts be represented?
- Which entity properties are normative across all entity types?
- How should entity identity changes be verified?
- Which entity lifecycle states are canonical?
- How should external entity identities be mapped into the ATON identity model?

These questions MAY be addressed by subsequent RFCs and ontology
specifications.

## References

- ADR-0004 — Artifact-Based Knowledge Organization
- ADR-0005 — Separation of Content, Metadata and Relations
- ADR-0006 — Engineering Knowledge Graph
- ADR-0008 — Canonical Domain Models
- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- RFC-0002 — Identity Model
- RFC-0010 — Artifact Model
- RFC-0015 — Logical Engineering Knowledge and Physical Representations
- RFC-0025 — Canonical Relation Model
- NOTE-0008 — Entity and Artifact Semantics

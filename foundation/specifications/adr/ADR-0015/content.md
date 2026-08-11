# Embedded and Contextual Engineering Entities

## Context

ATON engineering knowledge may contain concepts that are meaningful only
within the context of another engineering concept.

A Review, for example, may contain Findings that describe observations made
during that Review.

Such concepts must be distinguished from the physical representation in
which they happen to be stored.

ADR-0013 establishes the distinction between Engineering Entities and
Engineering Artifacts.

The remaining question is whether context-dependent entities require a
separate artifact concept or whether their contextual semantics can be
expressed through relationships between Engineering Entities.

## Problem Statement

Some engineering concepts have meaning only within a defined context.

A Finding may belong to a Review.

A review-local observation may therefore have:

- a semantic identity;
- a defined contextual owner;
- traceability to the context in which it was created;
- its own content and metadata.

Treating such concepts as merely embedded file fragments would couple their
semantic identity to a physical representation.

Conversely, treating every contextual concept as completely independent
without representing its context would lose important engineering semantics.

ATON therefore requires a consistent model for contextual Engineering
Entities.

## Decision

ATON SHALL model context-dependent concepts as Engineering Entities when
they possess independent engineering meaning.

Context SHALL be represented semantically rather than being inferred from
physical containment.

A contextual Engineering Entity SHALL remain distinguishable from the
Engineering Artifact that represents it.

Contextual ownership or containment SHALL be represented through the
canonical relation model where such a relationship is semantically required.

A contextual entity SHALL NOT become a different fundamental kind of
Engineering Entity merely because its meaning depends on another entity.

## Contextual Identity

A contextual Engineering Entity MAY have an identity that is globally
addressable within the Engineering Knowledge Model.

Its identity SHALL remain independent of:

- file names;
- repository paths;
- directory structure;
- serialization format; and
- physical nesting.

An implementation MAY use a context-local identifier for presentation or
authoring purposes, provided that the canonical model can resolve the entity
unambiguously.

## Context Relationship

The relationship between a contextual entity and its context SHALL be
explicit when that relationship carries engineering meaning.

For example, a Finding may be associated with a Review.

The semantic relationship SHALL NOT be inferred solely from the fact that one
artifact is physically stored inside another directory or document.

Physical containment MAY be used as an implementation convenience, but SHALL
NOT define canonical engineering semantics.

## Artifact Representation

A contextual Engineering Entity MAY be represented:

- by a standalone artifact;
- within an artifact containing other entities;
- through generated or derived representations; or
- through another physical representation supported by ATON.

The choice of physical representation SHALL NOT change the semantic identity
of the entity.

Multiple contextual entities MAY therefore share a physical artifact.

A single contextual entity MAY also have multiple physical representations.

## Traceability

Contextual entities SHALL participate in the Engineering Knowledge Graph
according to the same fundamental traceability principles as other
Engineering Entities.

A contextual entity MAY have relations to:

- its contextual owner;
- other engineering entities;
- decisions;
- requirements;
- artifacts; or
- external entities.

Contextual dependency SHALL NOT prevent independent traceability.

## Versioning

Contextual Engineering Entities SHALL follow the version semantics defined
by ADR-0012.

A change to the context SHALL NOT automatically create a new identity for
every contextual entity.

Likewise, a change to a contextual entity SHALL NOT automatically create a
new identity for its context.

Whether a new engineering version is required depends on the semantic
change to the respective Engineering Entity.

## Lifecycle

The lifecycle of a contextual entity MAY depend on the lifecycle of its
context.

Such dependency SHALL be explicitly defined by the applicable ontology or
governance model.

The physical deletion of the representation containing a contextual entity
SHALL NOT by itself determine the semantic lifecycle of the entity.

## Findings and Reviews

Findings are a primary example of contextual Engineering Entities.

A Finding MAY be semantically associated with a Review without requiring the
Finding to be modeled as a special physical artifact type.

The Review provides the context in which the Finding was produced.

The Finding remains an Engineering Entity when it has independent engineering
meaning, such as an observation, issue, assessment or conclusion that may
participate in traceability.

The exact lifecycle and semantics of Reviews and Findings are defined by the
Review Process specification.

## Consequences

### Positive

- Contextual engineering concepts retain semantic identity.
- Physical containment does not become part of the domain model.
- Findings and similar concepts can participate in traceability.
- Multiple physical representations remain possible.
- Context can be modeled explicitly.
- The kernel remains independent of repository structure.

### Negative

- Contextual relationships must be explicitly modeled where semantically
  relevant.
- Implementations must distinguish physical containment from semantic
  context.
- Context-dependent lifecycle rules may require additional domain
  specifications.

## Relationship to Other Decisions

ADR-0013 defines Engineering Entity and Engineering Artifact semantics.

ADR-0011 defines the separation between the logical Engineering Knowledge
Model and physical representations.

ADR-0012 defines engineering identity and version semantics.

ADR-0014 defines the canonical semantic relation model used to represent
contextual relationships.

The Review Process specification defines the normative semantics of Reviews
and Findings.

## Alternatives Considered

### Model contextual concepts only as embedded artifacts

Rejected.

This would couple semantic identity to physical representation and make
traceability dependent on storage structure.

### Make every contextual concept globally independent

Rejected.

This would lose the semantic relationship between a contextual concept and
the context in which it exists.

### Infer context from repository structure

Rejected.

Repository structure is a physical representation detail and must not define
canonical engineering semantics.

## Expected Outcome

ATON SHALL support contextual Engineering Entities without introducing a
separate fundamental entity model for embedded concepts.

Context SHALL be represented explicitly through the canonical Engineering
Knowledge Model.

Physical embedding MAY be used as a representation technique but SHALL NOT
define the semantic identity or meaning of an Engineering Entity.

# Entity and Artifact Semantics

## Context

ATON distinguishes between engineering knowledge and its physical
representation.

An engineering concept has semantic identity, while an artifact provides a
representation of engineering information.

The distinction is required to preserve the independence of the Engineering
Knowledge Model from physical storage, serialization and tooling.

The existing Engineering Knowledge Model does not yet define the normative
relationship between an engineering entity and an artifact.

## Problem Statement

If engineering entities and artifacts are treated as identical concepts,
physical representation details become part of engineering identity.

This creates ambiguity when:

- one engineering concept has multiple representations;
- a representation is moved between persistence systems;
- several artifacts contribute to one engineering concept;
- one artifact contains information about multiple engineering concepts;
- representations are transformed or generated;
- different views of the same engineering knowledge are created.

ATON therefore requires a clear semantic distinction between an engineering
entity and an artifact.

## Decision

ATON SHALL distinguish between an Engineering Entity and an Engineering
Artifact.

An Engineering Entity SHALL represent a logical engineering concept within
the Engineering Knowledge Model.

An Engineering Artifact SHALL represent a persisted or otherwise
addressable representation of engineering information.

An artifact SHALL NOT automatically constitute the semantic identity of the
engineering entity it represents.

## Engineering Entity

An Engineering Entity SHALL have semantic identity within the Engineering
Knowledge Model.

The identity of an entity SHALL be independent of:

- repository paths;
- file names;
- directory names;
- serialization formats;
- databases;
- APIs;
- generated representations; and
- other physical storage details.

An entity MAY evolve through multiple engineering versions according to the
version semantics defined by ADR-0012.

## Engineering Artifact

An Engineering Artifact SHALL be a representation of engineering information.

An artifact MAY contain:

- engineering content;
- canonical metadata;
- relations;
- other explicitly defined artifact components.

The physical representation of an artifact MAY change without changing the
identity of the engineering entity represented by that artifact.

An artifact MAY therefore be replaced, transformed, migrated or regenerated
without necessarily creating a new engineering entity.

## Entity-to-Artifact Relationship

An Engineering Entity MAY be represented by one or more artifacts.

An artifact MAY represent one or more engineering entities when the artifact
format explicitly supports such representation.

The relationship between an entity and an artifact SHALL therefore be
explicitly modeled where necessary and SHALL NOT be inferred solely from
physical location.

A one-to-one relationship between entity and artifact SHALL NOT be assumed
by the kernel.

## Artifact Components

Content, metadata and relations are components of an artifact
representation.

They SHALL NOT automatically be interpreted as separate engineering
entities.

Whether a component constitutes an independent engineering entity depends on
its semantic definition within the Engineering Knowledge Model.

This distinction allows an artifact to contain multiple logical engineering
concepts without requiring every physical component to become an independent
artifact.

## Identity

Engineering identity SHALL belong to the Engineering Entity.

Artifact identity SHALL identify the representation itself.

The two identities SHALL remain conceptually distinct.

A change in artifact identity SHALL NOT automatically imply a change in
engineering identity.

A change in engineering identity SHALL NOT be inferred merely from a change
in physical representation.

## Persistence Independence

An Engineering Entity SHALL remain identifiable when its artifact is moved
between persistence implementations.

For example, an entity MAY be represented successively by:

- a Markdown artifact in Git;
- a database representation;
- an API representation; or
- an exported exchange representation.

These representations MAY differ physically while referring to the same
Engineering Entity.

The canonical semantic identity SHALL remain independent of the persistence
mechanism.

## Versioning

Engineering versions SHALL apply to Engineering Entities according to
ADR-0012.

Artifact revisions SHALL describe changes to artifact representations.

An artifact revision and an engineering version SHALL therefore remain
distinct concepts.

One engineering version MAY involve multiple artifact revisions.

One artifact revision MAY contain changes affecting multiple engineering
entities.

## Traceability

Relations between Engineering Entities SHALL express engineering semantics.

Relations between physical artifacts MAY be used for implementation,
provenance or representation purposes.

The kernel SHALL NOT infer engineering semantics from arbitrary physical
artifact relationships unless such semantics are explicitly defined.

Traceability SHALL therefore operate primarily on the logical Engineering
Knowledge Model.

## Derived Representations

An artifact MAY be generated from the canonical Engineering Knowledge Model.

A generated artifact SHALL remain a representation and SHALL NOT
automatically become authoritative merely because it exists physically.

Conversely, an explicitly authoritative artifact MAY provide the persisted
representation from which the canonical model is loaded.

The authority of a representation SHALL be defined by the applicable
architecture and governance rules.

## Consequences

### Positive

- Engineering identity is independent of physical storage.
- Multiple representations of the same engineering concept are possible.
- Alternative persistence implementations can be supported.
- Versioning can distinguish semantic evolution from artifact changes.
- Traceability remains focused on engineering semantics.
- Generated and transformed representations can be handled without changing
  entity identity.

### Negative

- Implementations must distinguish entity identity from artifact identity.
- Entity-to-artifact relationships require explicit modeling where
  ambiguity exists.
- Some simple file-based assumptions cannot be used by the kernel.
- Additional modeling is required when an artifact represents multiple
  engineering entities.

## Relationship to Other Decisions

ADR-0010 defines canonical metadata and its persistence-independent semantics.

ADR-0011 defines the separation between the logical Engineering Knowledge
Model and physical representations.

ADR-0012 defines engineering identity, engineering versions, artifact
revisions, baselines and releases.

The canonical relation model defines how Engineering Entities participate in
semantic relationships.

## Alternatives Considered

### Treat every artifact as an engineering entity

Rejected.

This would couple engineering identity to physical representation and prevent
multiple representations of the same engineering concept.

### Treat entities as purely derived from artifacts

Rejected.

Engineering identity must remain stable across persistence and
representation changes.

### Require exactly one artifact per entity

Rejected.

Complex engineering knowledge may require multiple representations or
artifacts for a single engineering concept.

## Expected Outcome

ATON SHALL maintain a normative distinction between Engineering Entities and
Engineering Artifacts.

Engineering Entities SHALL own semantic identity.

Engineering Artifacts SHALL provide physical or addressable representations
of engineering information.

The kernel SHALL preserve this distinction independently of persistence,
serialization and tooling.

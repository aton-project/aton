# Logical Engineering Knowledge Model and Physical Representations

## Context

ATON represents engineering knowledge through a combination of engineering
entities, artifacts, metadata, relationships and other semantic concepts.

These concepts have logical meaning independent of how they are persisted,
transported or presented.

The same engineering knowledge may be represented physically through files,
Git repositories, databases, APIs, generated documents or other
representations.

Without an explicit architectural separation between the logical model and
its physical representations, kernel components may become dependent on
specific persistence formats or repository structures.

This would make the Engineering Knowledge Model dependent on implementation
details and would prevent alternative representations from expressing the
same engineering knowledge consistently.

## Problem Statement

The ATON architecture must distinguish between:

- the logical Engineering Knowledge Model;
- the canonical domain representation used by the kernel; and
- physical representations used for persistence, exchange or presentation.

Physical representations must not define the semantics of the logical model.

A file path, directory structure, serialization format or rendering mechanism
must therefore not determine the semantic identity or meaning of an
engineering concept.

## Decision

ATON SHALL define the Engineering Knowledge Model independently of its
physical representations.

The logical Engineering Knowledge Model SHALL be the semantic source for
engineering knowledge handled by the ATON kernel.

The kernel SHALL operate on canonical domain representations and SHALL NOT
depend directly on persistence-specific serialization structures.

Physical representations SHALL be treated as representations of the logical
model rather than as the model itself.

Multiple physical representations MAY represent the same logical engineering
knowledge.

A physical representation SHALL NOT introduce, modify or redefine the
semantics of the logical Engineering Knowledge Model.

## Representation Boundary

ATON SHALL maintain a clear boundary between physical representations and
the canonical domain model.

Transformation between a physical representation and the canonical domain
model SHALL occur at an explicit architectural boundary.

For imported or persisted representations, the loader or corresponding
translation component SHALL perform normalization into the canonical domain
model.

Kernel components SHALL consume the canonical domain model rather than
interpreting persistence-specific structures.

The same principle SHALL apply to generated or exported representations:
renderers and exporters SHALL derive their output from the canonical domain
model.

## Logical Engineering Knowledge

The logical model includes semantic concepts such as:

- entities;
- artifacts;
- metadata;
- relations;
- predicates;
- ontology concepts;
- versions and other engineering concepts defined by the Foundation.

The existence of a physical representation is therefore separate from the
existence and identity of the corresponding logical engineering knowledge.

## Physical Representations

Physical representations MAY include, but are not limited to:

- Markdown files;
- YAML metadata;
- Git repositories and revisions;
- databases;
- APIs;
- exchange formats;
- generated documentation;
- rendered views.

These representations are implementation or persistence concerns unless
explicitly defined as normative by the Foundation.

ATON SHALL avoid treating any particular physical representation as the
semantic definition of an engineering concept.

## Consequences

### Positive

- The kernel remains independent of persistence formats.
- Multiple physical representations can represent the same logical model.
- Import and export mechanisms can evolve independently of the domain model.
- Verification and reasoning operate on stable domain semantics.
- Renderers do not need to understand persistence-specific structures.
- Alternative storage and exchange mechanisms can be introduced without
  redefining the Engineering Knowledge Model.

### Negative

- Implementations require explicit translation boundaries.
- Loaders and exporters become responsible for normalization and mapping.
- Changes to the canonical domain model may require corresponding changes in
  physical representation adapters.

## Relationship to Other Decisions

This decision establishes the architectural boundary between the logical
Engineering Knowledge Model and its physical representations.

The canonical relation model is defined separately by RFC-0025 and related
architecture and semantic decisions.

Metadata semantics are defined separately by the canonical metadata model.

Engineering version, baseline and release semantics are defined separately
from physical representation.

## Alternatives Considered

### Treat the repository structure as the domain model

Rejected.

Repository paths and file structures are physical representations and must
not determine domain semantics.

### Allow kernel components to interpret persistence formats directly

Rejected.

This couples domain logic to implementation details and makes alternative
representations unnecessarily difficult.

### Define a separate domain model for every representation

Rejected.

This would create multiple competing semantic models instead of one canonical
Engineering Knowledge Model.

## Expected Outcome

ATON SHALL provide one logical Engineering Knowledge Model with explicit
translation boundaries to and from physical representations.

The kernel SHALL remain representation-independent while loaders, exporters
and renderers handle the concerns of individual physical representations.

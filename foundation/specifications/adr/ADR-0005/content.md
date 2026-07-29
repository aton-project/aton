# ADR-0005 — Separation of Content, Metadata and Relations

## Status

Accepted

---

## Context

Engineering artifacts contain different kinds of information that evolve
independently.

The engineering content expresses the technical knowledge.

Metadata describes the artifact itself.

Relationships define how artifacts are connected.

Combining these concerns in a single structure reduces maintainability,
reusability, and automated processing.

---

## Decision

Artifacts SHALL separate engineering content, metadata, and relationships
into independent logical components.

Engineering content SHALL contain only the technical knowledge intended for
human understanding.

Metadata SHALL describe the artifact itself and SHALL NOT contain engineering
content.

Relationships SHALL explicitly describe dependencies and connections between
artifacts.

Each component MAY evolve independently while remaining part of the same
logical artifact.

---

## Consequences

This decision provides:

- clear separation of concerns
- simplified maintenance
- improved traceability
- reusable engineering content
- implementation-independent artifact structure
- efficient automated processing

Engineering knowledge becomes easier to analyze, transform, and reuse without
mixing different responsibilities.

---

## Rationale

Engineering content, metadata, and relationships serve fundamentally
different purposes.

Separating these concerns creates a cleaner architecture, reduces coupling,
and enables specialized tooling without affecting the engineering knowledge
itself.

---

## Alternatives Considered

### Single Document Structure

Rejected because engineering content, metadata, and relationships become
intermixed.

### Embedded Metadata

Rejected because metadata becomes difficult to process independently.

### Implicit Relationships

Rejected because traceability should always be explicit rather than inferred.

---

## Architectural Principle

> Content expresses engineering knowledge.

> Metadata describes artifacts.

> Relationships connect engineering knowledge.

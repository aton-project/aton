# ADR-0005 — Separation of Content, Metadata and Relations

## Status

Accepted

---

## Context

Engineering artifacts contain different kinds of information that evolve
independently.

Engineering content expresses engineering knowledge.

Metadata describes engineering artifacts.

Relationships describe how engineering concepts are connected.

Combining these concerns in a single structure reduces maintainability,
reusability, and automated processing.

---

## Decision

Engineering artifacts SHALL separate engineering content, metadata, and
relationships into independent logical components.

Engineering content SHALL contain only engineering knowledge intended for
human understanding.

Metadata SHALL describe engineering artifacts and SHALL NOT contain
engineering knowledge.

Engineering relationships SHALL be represented explicitly.

Each logical component MAY evolve independently while remaining part of the
same engineering artifact.

---

## Consequences

This decision provides:

- clear separation of concerns
- simplified maintenance
- improved traceability
- reusable engineering knowledge
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

Rejected because engineering relationships should always be represented
explicitly rather than being inferred.

---

## Architectural Principle

> Content expresses engineering knowledge.

> Metadata describes engineering artifacts.

> Relationships connect engineering concepts.

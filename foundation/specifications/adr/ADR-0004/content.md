# ADR-0004 — Artifact-Based Knowledge Organization

## Status

Accepted

---

## Context

Traditional engineering documentation is organized around documents.

As projects grow, documents become increasingly difficult to maintain,
review, trace, and reuse. Individual engineering concepts are often embedded
within large documents, making them difficult to reference independently.

The Foundation requires a more granular approach that enables precise
identification, versioning, traceability, and reuse of engineering knowledge.

---

## Decision

Engineering knowledge SHALL be organized as engineering entities.

Engineering entities SHALL be represented by engineering artifacts.

An engineering entity represents a uniquely identifiable unit of engineering
knowledge.

Engineering entities MAY represent requirements, architecture decisions,
specifications, glossary terms, interfaces, models, examples, templates,
or other engineering concepts.

Engineering artifacts SHALL be uniquely identifiable and independently
versionable.

Engineering relationships SHALL be represented explicitly rather than being
inferred from document structure.

Views MAY present engineering knowledge using different representations.

Examples of views include documents, websites, APIs, IDEs, AI assistants,
and other presentation formats.

Views SHALL NOT be considered the primary organizational unit of engineering
knowledge.

---

## Consequences

This decision provides:

- fine-grained engineering knowledge
- explicit traceability
- independent versioning
- improved reuse
- implementation-independent organization
- graph-based knowledge structures

Engineering knowledge becomes modular and can evolve independently while
remaining connected through explicit relationships.

Different views can present the same engineering knowledge without changing
its underlying structure.

---

## Rationale

Engineering knowledge naturally consists of interconnected engineering
entities rather than isolated documents.

Engineering artifacts provide canonical representations of engineering
knowledge while remaining independent of presentation formats.

Views remain valuable for presenting engineering knowledge but no longer
define its organization.

---

## Alternatives Considered

### Document-Centric Organization

Rejected because documents combine many independent engineering concepts into
large monolithic structures.

### File-Centric Organization

Rejected because files are implementation artifacts rather than engineering
concepts.

### Database Records

Rejected because database structures are implementation-specific and should
not define the conceptual organization of engineering knowledge.

---

## Architectural Principle

> Engineering knowledge is organized as engineering entities.

> Engineering artifacts provide canonical representations of engineering
> knowledge.

> Views present engineering knowledge but do not define its organization.

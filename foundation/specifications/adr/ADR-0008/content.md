# ADR-0008 Canonical Domain Models

## Status

Accepted

## Context

Engineering Note NOTE-0020 identified that the kernel currently depends on
multiple serialization formats for relations.

The analysis concluded that kernel components interpret persistence formats
instead of operating on stable domain concepts.

The Architecture Board reviewed the findings and concluded that this is a
general architectural concern rather than a relation-specific issue.

## Decision

The ATON kernel SHALL expose exactly one canonical internal representation for
every domain concept.

Kernel components MUST operate exclusively on canonical domain models.

External serialization formats SHALL be normalized at the system boundary.

The loader SHALL translate external representations into canonical kernel
representations.

## Rationale

Canonical domain models separate persistence concerns from domain logic.

This provides:

- clear separation of responsibilities
- stable kernel interfaces
- simplified verification
- simplified rendering
- consistent reasoning
- extensible import capabilities

The kernel architecture therefore becomes independent of storage formats.

## Consequences

Kernel components SHALL depend only on canonical domain models.

Serialization details SHALL remain confined to loader components.

Future importers and exporters SHALL translate between external formats and the
canonical kernel representation.

This principle applies to all future domain concepts including:

- Relations
- Metadata
- Attributes
- Ontologies
- Traceability
- Requirements
- Tests
- Views

## Initial Application

The first application of this architectural principle SHALL be the Relation
domain model.

Subsequent architectural decisions SHALL follow the same principle for all
future domain concepts.

## Alternatives Considered

### Preserve multiple internal representations

Rejected.

This increases coupling between kernel components and persistence formats.

### Normalize inside each subsystem

Rejected.

Duplicating normalization logic leads to inconsistent behaviour and increased
maintenance effort.

## References

- NOTE-0020 Canonical Relation Model Required

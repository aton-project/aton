# RFC-0000 – Document Conventions

## Summary

This RFC defines the conventions for all ATON Request for Comments (RFCs).
It specifies the required document structure, metadata, lifecycle, naming,
referencing, and writing style to ensure a consistent and machine-readable
specification.

## Motivation

A consistent document structure is essential for:

- Human readability
- Machine processing
- Automated validation
- Traceability
- Long-term maintainability

## Goals

- Standardize all RFCs
- Define mandatory sections
- Define document lifecycle
- Enable automatic validation
- Ensure consistent terminology

## Non Goals

This RFC does not define the ATON data model or ontology.
Those are specified in subsequent RFCs.

## Proposal

Every RFC SHALL:

- have a unique identifier
- contain a metadata.yaml file
- contain a relations.yaml file
- contain a content.md file
- follow the section order defined in this RFC

### Required Sections

1. Summary
2. Motivation
3. Goals
4. Non Goals
5. Proposal
6. Consequences
7. Alternatives
8. Migration
9. Open Questions

### Language

Normative statements SHALL use the keywords:

- SHALL
- SHALL NOT
- SHOULD
- SHOULD NOT
- MAY

according to RFC 2119.

## Consequences

### Advantages

- Consistent documentation
- Easier reviews
- Automated tooling
- Better AI support

### Disadvantages

- Slightly more effort when writing RFCs

## Alternatives

No common document conventions.

Rejected because it would lead to inconsistent specifications.

## Migration

Not applicable.

## Open Questions

None.

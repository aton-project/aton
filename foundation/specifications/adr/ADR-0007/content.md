# ADR-0007 — Foundation as the Normative Engineering Knowledge Base

## Status

Accepted

---

## Context

ATON is an Open Engineering Operating System built around engineering knowledge.

To ensure long-term consistency, maintainability, and interoperability, engineering knowledge SHALL be managed independently of its implementation.

Without a clear separation between knowledge and implementation, engineering concepts become tightly coupled to specific technologies, making evolution and interoperability increasingly difficult.

A stable architectural foundation therefore requires a single canonical source for all normative engineering knowledge.

---

## Decision

The Foundation SHALL serve as the canonical, normative Engineering Knowledge Base of ATON.

The Foundation defines the engineering knowledge required to specify, govern, and evolve the ATON ecosystem.

The Foundation SHALL contain normative engineering knowledge, including but not limited to:

- Specifications
- Ontologies
- Glossaries
- Schemas
- Templates
- Architecture Decision Records (ADRs)
- Governance documents

The Foundation SHALL remain independent of implementation technologies.

The Foundation SHALL NOT contain executable implementation logic.

ATON SHALL act as the reference implementation of the Foundation.

---

## Consequences

This decision establishes a clear separation between engineering knowledge and implementation.

As a consequence:

- Engineering knowledge evolves independently of software implementations.
- Multiple implementations MAY conform to the same Foundation.
- The Foundation becomes the canonical source of engineering knowledge.
- Implementations derive their behavior from the Foundation rather than defining engineering concepts themselves.
- Conformance can be verified against the Foundation.

---

## Rationale

The separation of normative knowledge from implementation follows proven principles established by international standards organizations, where standards and implementations evolve independently.

This approach promotes:

- longevity
- interoperability
- implementation independence
- reuse
- maintainability
- semantic consistency

The Foundation is therefore treated as a long-lived engineering asset rather than application documentation.

---

## Alternatives Considered

### Foundation as Project Documentation

Rejected because documentation is descriptive, whereas the Foundation is normative.

### Foundation Embedded in the Source Code

Rejected because engineering knowledge would become coupled to a specific implementation.

### Independent Standard Outside ATON

Deferred.

The Foundation evolves as part of the ATON project. If it matures into a broadly adopted engineering standard, it MAY be extracted into an independent specification in the future.

---

## Architectural Principle

> **The Foundation is the canonical, normative Engineering Knowledge Base of ATON.**

> **ATON is the reference implementation of the Foundation.**

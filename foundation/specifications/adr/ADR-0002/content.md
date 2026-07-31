# ADR-0002 — Markdown as the Canonical Authoring Format

## Status

Accepted

---

## Context

Engineering knowledge shall remain readable, maintainable, and independent of
specialized tooling throughout its lifecycle.

The authoring format should be simple, human-readable, version-control friendly,
and widely supported across operating systems and development environments.

Long-term accessibility of engineering knowledge is considered more important
than advanced document formatting capabilities.

---

## Decision

Markdown SHALL be used as the canonical authoring format for all engineering
content.

Markdown SHALL be human-readable without requiring specialized software.

Markdown MAY be extended through standardized and widely adopted extensions
where required for engineering purposes.

Examples include mathematical expressions, diagrams, and other
domain-specific representations.

Markdown MAY be transformed into other representations for rendering,
-publishing, exchange, or automated processing.

Markdown is the canonical serialization of engineering content.

The Engineering Knowledge Model defines the semantics of engineering knowledge
independently of its serialization.

---

## Consequences

This decision provides:

- human-readable engineering knowledge
- excellent Git integration
- simple review using standard development tools
- long-term maintainability
- implementation-independent authoring
- broad ecosystem compatibility

Engineering knowledge remains independent of any specific editor or publishing
technology.

---

## Rationale

Markdown has become the de facto standard for lightweight technical
documentation.

Its simplicity allows engineering knowledge to remain accessible for both
humans and automated tooling while avoiding dependencies on proprietary
document formats.

The use of standardized extensions enables domain-specific capabilities
without compromising the simplicity of the canonical authoring format.

---

## Alternatives Considered

### HTML

Rejected because HTML is optimized for presentation rather than authoring.

### XML

Rejected because XML is verbose and significantly reduces readability for
human authors.

### Rich Text Editors

Rejected because proprietary document formats reduce transparency,
portability, and long-term maintainability.

---

## Architectural Principle

> Markdown is the canonical serialization format for engineering content.

> The Engineering Knowledge Model defines the semantics of engineering
> knowledge independently of its serialization.

> Engineering artifacts are authored in implementation-independent canonical
> formats.

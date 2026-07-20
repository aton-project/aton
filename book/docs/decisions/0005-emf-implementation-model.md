---
title: "0005 - EMF as the Implementation Model"
description: Decision to implement the ATON domain model using the Eclipse Modeling Framework.
---

# 0005 - EMF as the Implementation Model

## Status

Accepted

## Date

2026-07-19

## Context

ATON requires a strongly typed domain model that supports:

- code generation
- validation
- serialization
- tooling
- extensibility

The Eclipse Modeling Framework (EMF) provides these capabilities and has a mature ecosystem.

However, the engineering domain model must remain independent from any implementation technology.

---

## Decision

The ATON Kernel Domain Model is defined by the Book.

The Eclipse Modeling Framework (EMF) is used to implement this model.

EMF is an implementation technology, not the source of architectural truth.

---

## Consequences

### Positive

- Mature modeling ecosystem
- Automatic code generation
- Strong tooling support
- Extensible metamodel
- Integration with Eclipse technologies

### Negative

- Dependency on EMF runtime
- Additional complexity compared to plain Java

---

## Architectural Principle

The Book defines the semantics.

The EMF model implements those semantics.

The generated Java code implements the EMF model.

The implementation shall never redefine the domain model.

```
Book
    │
    ▼
Kernel Domain Model
    │
    ▼
EMF Model
    │
    ▼
Generated Java
```

---

## Notes

The Book is the authoritative specification of ATON.

If an inconsistency exists between the Book and the EMF model, the Book is considered correct.

The EMF model shall be updated to conform to the specification.

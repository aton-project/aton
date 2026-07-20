---
title: "0003 - Everything is an Artifact"
description: Decision to model all engineering concepts as Artifacts.
---

# 0003 - Everything is an Artifact

## Status

Accepted

## Date

2026-07-19

## Context

Traditional engineering tools introduce dedicated object models for each discipline.

Examples include:

- Requirement
- Test Case
- Task
- Risk
- Component
- Change Request
- Document

This results in duplicated infrastructure for identity, versioning, reviews and traceability.

---

## Decision

ATON shall represent every engineering concept as an **Artifact**.

Capabilities define specialized Artifact types.

The Kernel defines only the common behavior shared by all Artifacts.

---

## Rationale

Using a single fundamental engineering object

- simplifies the domain model
- reduces duplicated functionality
- provides consistent versioning
- enables uniform reviews
- enables generic queries
- simplifies plugin development

---

## Consequences

### Positive

- Small and stable Kernel
- Consistent engineering model
- Shared infrastructure
- Easier extensibility

### Negative

- Capabilities must provide their own semantics
- Domain-specific behavior is implemented outside the Kernel

---

## Architectural Principle

The Kernel knows only:

- Artifact
- Relation
- Version
- Review
- Baseline

Capabilities define concepts such as

- Requirement
- Test Case
- Risk
- Task
- Project
- UML Model

without modifying the Kernel.

---

## Notes

Everything is an Artifact.

Relationships are represented by independent Relation objects.

This principle is one of the fundamental architectural decisions of ATON.

---
title: Artifact
description: Defines the fundamental engineering object of ATON.
---

# Artifact

## Definition

An **Artifact** is the fundamental unit of engineering knowledge in ATON.

Every engineering concept is represented as an Artifact.

Examples include:

- Requirement
- Task
- Bug
- Review
- Risk
- Test Case
- Component
- Interface
- UML Class
- State Machine
- Project
- Sprint
- Release

Artifacts are independent, versioned engineering objects.

---

# Identity

Every Artifact has a globally unique identifier.

The identifier never changes during the lifetime of the Artifact.

Human-readable identifiers are metadata and may change.

Example

UUID

```
9f9bfa8f...
```

Display ID

```
REQ-4711
```

---

# Lifecycle

Artifacts evolve over time.

An Artifact is never replaced.

Instead, new versions are created.

```
Artifact

↓

Version 1

↓

Version 2

↓

Version 3
```

The complete history remains available.

---

# Content

Artifacts contain engineering knowledge.

The content depends on the Artifact type.

Examples

Requirement

- Title
- Description
- Rationale

Task

- Summary
- Status
- Assignee

Review

- Findings
- Decision

---

# Metadata

Every Artifact provides common metadata.

Typical metadata include

- UUID
- Type
- Author
- Creation Date
- Last Modification
- Status
- Tags

---

# Attributes

Artifacts may define arbitrary attributes.

Examples

Requirement

```
ASIL = D
```

Task

```
Priority = High
```

Component

```
Supplier = Bosch
```

Attributes are extensible.

The kernel does not define domain-specific attributes.

---

# Relationships

Artifacts do not contain references to other Artifacts.

Relationships are represented by separate Relation objects.

```
Requirement

↓

Relation

↓

Test Case
```

This keeps artifacts independent.

---

# Reviews

Every Artifact can be reviewed.

Reviews are independent engineering objects.

Multiple reviews may exist for the same Artifact version.

---

# Baselines

Artifacts may participate in one or more Baselines.

A Baseline references specific versions.

---

# Persistence

Artifacts are persisted independently.

The persistence format is human-readable whenever possible.

The persistence technology does not define the Artifact model.

---

# Design Principles

An Artifact

- has an immutable identity
- is versioned
- is reviewable
- participates in relationships
- may belong to baselines
- contains engineering knowledge
- is independent of its persistence format

---

# Summary

Artifacts are the fundamental building blocks of the Engineering Knowledge Graph.

Everything in ATON begins with an Artifact.

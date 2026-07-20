---
title: Version
description: Defines how engineering knowledge evolves over time.
---

# Version

## Definition

A **Version** represents the state of an Artifact or Relation at a specific point in time.

Versions are immutable.

Once created, a Version never changes.

A new state always results in a new Version.

---

# Motivation

Engineering knowledge evolves continuously.

Requirements change.

Designs mature.

Tests are improved.

Risks are reassessed.

Instead of overwriting previous information, ATON preserves the complete history.

---

# Identity

Every Version has its own unique identifier.

A Version always belongs to exactly one Artifact or Relation.

```
Artifact
    │
    ├── Version 1
    ├── Version 2
    └── Version 3
```

The Artifact identity remains constant.

Versions describe its evolution.

---

# Immutability

A Version cannot be modified.

If engineering knowledge changes, a new Version is created.

```
Version 1

↓

Version 2

↓

Version 3
```

This guarantees reproducibility and traceability.

---

# Metadata

Each Version contains common metadata.

Examples include:

- Version Number
- Author
- Timestamp
- Commit Reference
- Change Description

Capabilities may extend the metadata.

---

# Lifecycle

Versions are created.

They are never deleted or modified.

Versions remain available for:

- audits
- reviews
- baselines
- traceability
- historical analysis

---

# Reviews

Reviews always reference a specific Version.

A Review never approves an Artifact in general.

It approves a particular Version.

```
Requirement

↓

Version 7

↓

Approved
```

If Version 8 is created, it requires a new Review.

---

# Relations

Relations are versioned in the same way as Artifacts.

Changing a Relation creates a new Relation Version.

Traceability therefore has a complete history.

---

# Baselines

Baselines consist of Versions.

They never reference mutable Artifacts.

```
Baseline 1

Requirement v4

Architecture v7

Test Case v2

Risk v5
```

A Baseline therefore represents a reproducible engineering state.

---

# Git Integration

ATON does not replace Git.

Git stores the history of persisted engineering knowledge.

The Version model defines the engineering semantics.

Both complement each other.

---

# Design Principles

A Version

- is immutable
- belongs to exactly one Artifact or Relation
- records a historical state
- can be reviewed
- can belong to one or more Baselines
- is fully traceable

---

# Summary

Versions preserve the evolution of engineering knowledge.

History is never overwritten.

Engineering is a sequence of Versions.

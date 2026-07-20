---
title: Relation
description: Defines the connections between engineering artifacts.
---

# Relation

## Definition

A **Relation** represents a semantic connection between two Artifacts.

Relations are first-class engineering objects.

They are not embedded references or pointers. They exist independently and carry their own identity, lifecycle and metadata.

Without Relations, Artifacts are isolated pieces of knowledge.

Together, Artifacts and Relations form the Engineering Knowledge Graph.

---

## Structure

Every Relation consists of:

- Source Artifact
- Target Artifact
- Relation Type

```
Requirement
     │
     │ satisfies
     ▼
System Requirement
```

The direction of a Relation is significant.

---

## Identity

Like Artifacts, every Relation has a globally unique identifier.

The identifier never changes.

---

## Versioning

Relations evolve over time.

Changing a Relation creates a new version instead of modifying history.

Examples include:

- changing the target
- changing attributes
- changing the relation type
- changing lifecycle state

Historical versions remain available.

---

## Relation Types

The meaning of a Relation is defined by its type.

Examples include:

- refines
- satisfies
- verifies
- dependsOn
- implements
- allocates
- tracesTo
- blocks
- duplicates

Capabilities may define additional relation types.

---

## Metadata

Every Relation provides common metadata.

Typical metadata include:

- UUID
- Type
- Author
- Creation Date
- Last Modification
- Status
- Tags

---

## Attributes

Relations may define additional attributes.

Examples:

```
Confidence = High
```

```
Criticality = ASIL-D
```

```
Weight = 0.8
```

The kernel does not prescribe domain-specific attributes.

---

## Reviews

Relations may be reviewed independently from the connected Artifacts.

This allows engineers to approve or reject traceability separately from the engineering objects themselves.

---

## Baselines

A Baseline references specific versions of Relations together with specific versions of Artifacts.

This guarantees a complete snapshot of engineering knowledge.

---

## Constraints

A Relation always connects exactly two Artifacts.

Self-relations may be allowed depending on the relation type.

Capabilities may define additional constraints.

---

## Design Principles

A Relation

- has its own identity
- is versioned
- is reviewable
- has semantics
- may have attributes
- is independent from Artifacts

---

## Summary

Relations are not implementation details.

They are engineering knowledge.

The Engineering Knowledge Graph is built from Artifacts connected by meaningful Relations.

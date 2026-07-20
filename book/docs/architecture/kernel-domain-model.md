---
title: Kernel Domain Model
description: The conceptual domain model of the ATON Kernel.
---

# Kernel Domain Model

## Purpose

The ATON Kernel defines the fundamental concepts required to manage engineering knowledge.

It intentionally contains only concepts that are independent of any engineering discipline.

The Kernel does not know about Requirements, Test Cases, Risks, UML Models, Projects or Tasks.

Instead, it provides a common domain model upon which all engineering capabilities are built.

---

# Core Concepts

The Kernel consists of five fundamental concepts.

```
           Artifact
              ▲
              │
         has Versions
              │
           Version

Artifact ── Relation ── Artifact
                │
                │
           has Versions
                │
           Version

Review ───────► Version

Baseline ─────► Version*
```

---

## Artifact

Represents a single piece of engineering knowledge.

Artifacts are immutable in their identity and evolve through Versions.

---

## Relation

Represents semantic knowledge connecting two Artifacts.

Relations are first-class engineering objects.

---

## Version

Represents an immutable state of an Artifact or Relation.

Every engineering change creates a new Version.

---

## Review

Represents an engineering assessment of one or more Versions.

Reviews are independent engineering objects.

A Review never approves an Artifact in general.

It always approves specific Versions.

---

## Baseline

Represents a consistent collection of Versions.

A Baseline captures the complete engineering state at a specific point in time.

---

# Design Goals

The Kernel shall remain

- small
- stable
- extensible
- technology independent
- domain independent

Every additional concept requires strong justification.

---

# Responsibilities

The Kernel is responsible for

- identity
- versioning
- traceability
- reviews
- baselines
- querying
- events
- extension points

The Kernel is not responsible for domain-specific engineering concepts.

---

# Extension Model

Engineering capabilities extend the Kernel.

Examples include

```
Requirement
    └── Artifact

Task
    └── Artifact

Test Case
    └── Artifact

Risk
    └── Artifact

Project
    └── Artifact

State Machine
    └── Artifact
```

The Kernel remains unchanged.

---

# Architectural Rule

Capabilities depend on the Kernel.

The Kernel never depends on Capabilities.

Dependency direction is strictly one-way.

---

# Engineering Knowledge Graph

The Engineering Knowledge Graph is composed of

- Versioned Artifacts
- Versioned Relations

Reviews and Baselines provide governance over this graph.

---

# Summary

The Kernel is intentionally minimal.

Its purpose is not to model every engineering discipline.

Its purpose is to provide the stable foundation upon which all engineering knowledge can be represented.

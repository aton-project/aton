---
title: Kernel Architecture Rules
description: Architectural rules that every ATON component must follow.
---

# Kernel Architecture Rules

The following rules are mandatory for every implementation of the ATON Kernel.

Violating these rules requires an explicit architectural decision.

---

## Rule 1 – The Kernel is Domain Independent

The Kernel shall not contain concepts from any engineering discipline.

The following concepts are forbidden inside the Kernel:

- Requirement
- Test Case
- Risk
- Task
- Project
- Component
- UML Class
- Safety Goal

These concepts belong to Capabilities.

---

## Rule 2 – Everything is an Artifact

Every engineering object is represented as an Artifact.

Capabilities specialize Artifacts but never replace them.

---

## Rule 3 – Relationships are Explicit

Artifacts never reference other Artifacts directly.

All semantic connections are represented by Relations.

---

## Rule 4 – History is Immutable

Engineering history shall never be overwritten.

Every change creates a new Version.

---

## Rule 5 – The Kernel Owns Identity

Global identities are created and managed exclusively by the Kernel.

Capabilities may not invent alternative identity mechanisms.

---

## Rule 6 – Services Own Behavior

Domain objects describe engineering knowledge.

Kernel Services implement engineering behavior.

Business logic shall not be embedded inside domain objects.

---

## Rule 7 – Persistence is Replaceable

The domain model must not depend on

- Git
- JSON
- YAML
- Markdown
- SQL
- EMF

Persistence is an implementation detail.

---

## Rule 8 – APIs Before User Interfaces

Every Kernel capability is exposed through APIs.

User interfaces consume the same APIs as every other client.

---

## Rule 9 – Capabilities Extend the Kernel

Capabilities may

- introduce new Artifact types
- introduce new Relation types
- provide additional services

Capabilities shall not modify Kernel semantics.

---

## Rule 10 – Dependencies Point Inward

Capabilities depend on the Kernel.

The Kernel never depends on Capabilities.

Dependency direction is strictly one-way.

---

## Rule 11 – Events are the Integration Mechanism

Components communicate using published events.

Direct dependencies should be minimized.

---

## Rule 12 – Keep the Kernel Small

Whenever a new concept is proposed, ask:

"Can this be implemented as a Capability?"

If the answer is yes, it does not belong in the Kernel.

---

# Summary

The Kernel provides the stable engineering foundation.

Everything else is built on top.

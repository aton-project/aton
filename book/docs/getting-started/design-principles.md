---
sidebar_position: 4
title: Design Principles
description: The architectural principles that guide ATON.
---

# Design Principles

The following principles guide every architectural decision in ATON.

## 1. Everything is an Artifact

Every engineering object is represented as an artifact.

Requirements, tasks, models, reviews, tests, risks, projects and documents all share the same foundation.

---

## 2. Relationships are First-Class Citizens

Relationships are explicit engineering knowledge.

They have semantics, history, versioning and lifecycle.

---

## 3. Everything is Versioned

Every artifact and every relationship evolves over time.

History must never be lost.

---

## 4. Knowledge over Documents

Documents are views.

Knowledge is the source of truth.

---

## 5. Git is the Source of Truth

Git provides immutable history, branching and collaboration.

ATON builds on Git instead of replacing it.

---

## 6. Human-Readable Persistence

Engineering knowledge should remain understandable without ATON.

Whenever possible, persisted data should be readable by humans.

---

## 7. Keep the Kernel Small

The kernel provides only fundamental engineering services.

Everything else belongs in capabilities.

---

## 8. Capabilities build on the Kernel

Requirements Management, Modeling, Testing, Project Management and AI are capabilities.

They never redefine kernel concepts.

---

## 9. API First

Every capability must be accessible through stable APIs.

User interfaces are consumers of the same services.

---

## 10. AI Augments Engineers

AI supports engineers.

Engineering decisions always remain under human control.

---

## 11. Open by Design

Open formats.

Open standards.

Open architecture.

Whenever possible, avoid vendor lock-in.

---

## 12. Simplicity over Complexity

Simple concepts scale better than complex frameworks.

Architecture should be understandable before it becomes powerful.

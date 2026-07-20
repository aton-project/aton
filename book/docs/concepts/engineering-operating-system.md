---
title: Engineering Operating System
description: Defines the Engineering Operating System concept of ATON.
---

# Engineering Operating System

## Introduction

ATON is an **Engineering Operating System (EOS)**.

Unlike traditional engineering tools, ATON does not focus on a single engineering discipline such as Requirements Management, Modeling, Test Management or Project Planning.

Instead, ATON provides a common foundation for engineering itself.

Its purpose is to manage engineering knowledge independently of individual disciplines.

---

## Motivation

Today's engineering landscape consists of many specialized tools.

Each tool manages only a subset of the overall engineering knowledge.

Examples include:

- Requirements Management
- Project Management
- Source Code Management
- Test Management
- System Modeling
- Risk Management
- Documentation

Although these tools often describe the same system, they rarely share a common representation of engineering knowledge.

This fragmentation creates unnecessary complexity, duplicated information and broken traceability.

ATON addresses this problem by introducing a common engineering foundation.

---

## Engineering Services

Like a traditional operating system provides common services for applications, ATON provides common services for engineering capabilities.

These include:

- Artifact Management
- Relationship Management
- Versioning
- Reviews
- Baselines
- Queries
- Search
- Events
- Access Control

Capabilities build upon these services instead of implementing them independently.

---

## Kernel

The ATON Kernel contains only the fundamental engineering services.

It intentionally remains small, stable and independent from domain-specific functionality.

The kernel does not know about Requirements, Tasks, UML Models or Test Cases.

It only knows Artifacts, Relationships and the services required to manage them.

---

## Capabilities

Capabilities extend the kernel.

Examples include:

- Requirements Management
- Project Management
- Systems Modeling
- Test Management
- Risk Management
- Functional Safety
- AI Assistance

Capabilities reuse the kernel instead of replacing it.

---

## Engineering Knowledge Graph

All engineering knowledge is represented as a versioned graph of interconnected artifacts.

The Engineering Knowledge Graph is the central data model of ATON.

Every capability contributes to this shared graph.

---

## Vision

ATON is not intended to replace every engineering tool.

Its purpose is to become the common operating system that enables engineering knowledge to exist as one coherent system.

Engineering knowledge.

Versioned.

Connected.

Open.

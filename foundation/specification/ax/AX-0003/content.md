# AX-0003 — Information Architecture

## Purpose

This document defines how engineering knowledge is organized within ATON.

The information architecture shall prioritize understanding over storage structure.

Users shall navigate concepts rather than directories.

---

## Design Goals

The information architecture shall:

- minimize navigation depth
- expose context
- group related knowledge
- remain scalable
- support multiple renderers

---

## Navigation Principles

Information shall be organized by purpose, not by file location.

Primary navigation shall remain stable even if the underlying repository evolves.

---

## Top-Level Structure

The default navigation consists of the following sections:

- Getting Started
- Concepts
- Specifications
- Reference
- Tutorials
- Community

---

## Specification Structure

Specifications shall be grouped by domain.

Examples:

- Core
- AX
- ADR
- RFC
- Glossary

Additional domains may be added without changing the overall navigation model.

---

## Cross Navigation

Users shall always be able to discover:

- related artifacts
- parent artifacts
- child artifacts
- referenced artifacts
- superseded artifacts

Navigation shall reflect the knowledge graph.

---

## Search

Search is a primary navigation mechanism.

Users shall not be required to know where information is stored.

---

## Scalability

The information architecture shall support repositories containing millions of artifacts without changing the conceptual navigation model.


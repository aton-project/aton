# AX-0004 — Navigation

## Purpose

This document defines the navigation experience within ATON.

Navigation shall help users understand engineering knowledge rather than locate files.

Every navigation element shall reduce cognitive effort.

---

## Design Goals

Navigation shall:

- remain predictable
- expose relationships
- minimize user actions
- reveal context
- support exploration

---

## Navigation Principles

Users navigate knowledge.

Users do not navigate directories.

Navigation shall always reflect the engineering knowledge graph.

---

## Primary Navigation

Primary navigation shall expose the major knowledge domains.

Examples:

- Getting Started
- Concepts
- Specifications
- Reference
- Tutorials
- Community

Primary navigation shall remain stable over time.

---

## Secondary Navigation

Secondary navigation provides local context.

Examples include:

- parent artifact
- child artifacts
- related artifacts
- references
- backlinks

---

## Context Navigation

Every artifact shall expose its surrounding context.

Users shall always understand:

- where they are
- why the artifact exists
- how it relates to other artifacts

---

## Cross Navigation

Cross references shall be directly navigable.

Relationships shall be visible without requiring manual search.

---

## Breadcrumbs

Breadcrumbs communicate conceptual hierarchy.

They shall represent knowledge structure rather than filesystem paths.

---

## Navigation Stability

Navigation shall remain stable even if repositories evolve.

Moving artifacts shall not significantly alter the user experience.

---

## Scalability

Navigation shall remain efficient for repositories containing millions of artifacts.

The conceptual navigation model shall remain unchanged regardless of repository size.

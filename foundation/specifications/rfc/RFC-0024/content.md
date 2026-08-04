# RFC-0024 — Docusaurus Renderer

## Status

Draft

---

## Abstract

This RFC defines the first ATON renderer implementation.

The Docusaurus Renderer transforms Foundation artifacts into a static documentation website.

The renderer is a presentation layer.

It shall not modify engineering knowledge.

---

## Motivation

The Foundation is the single source of truth for ATON engineering knowledge.

Documentation websites shall be generated automatically from Foundation artifacts.

Manual duplication of documentation shall be avoided.

---

## Scope

Version 1 of the renderer shall support:

- Constitution
- AX Specifications
- RFC Specifications
- ADR Specifications
- Glossary Entries

Future versions may support additional artifact types.

---

## Input

The renderer consumes artifacts stored under the Foundation repository.

Each artifact consists of:

- metadata
- content
- relations (optional)

The renderer shall never require renderer-specific information inside Foundation artifacts.

---

## Output

The renderer generates documentation suitable for Docusaurus.

Generated documentation shall include:

- Markdown pages
- Category index pages
- Navigation structure
- Sidebar configuration

Generated files shall be reproducible.

---

## Design Principles

The renderer shall:

- preserve engineering knowledge
- avoid manual duplication
- remain deterministic
- remain idempotent
- separate content from presentation

---

## Out of Scope

Version 1 does not include:

- graph visualization
- backlink generation
- ontology visualization
- PDF generation
- AI-specific rendering

These capabilities may be added by future RFCs.

---

## Architecture

The renderer is part of the presentation layer.

```text
Foundation
        │
        ▼
Docusaurus Renderer
        │
        ▼
Generated Documentation
```

The renderer consumes Foundation artifacts but never modifies them.

---

## Rationale

Separating engineering knowledge from presentation enables multiple renderers to consume the same Foundation without introducing duplicate sources of truth.

The Docusaurus Renderer serves as the reference implementation of the ATON rendering architecture.

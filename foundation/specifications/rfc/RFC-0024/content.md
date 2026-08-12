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

The renderer SHALL consume the canonical Engineering Knowledge Model through the applicable loading and translation boundary.

The renderer SHALL NOT interpret repository layout, persistence-specific metadata or physical artifact structure as engineering semantics.

The renderer SHALL NOT require renderer-specific information inside Foundation artifacts.

---

## Canonical Input Boundary

The Docusaurus Renderer SHALL operate on the canonical Engineering Knowledge
Model.

Physical Foundation representations SHALL be translated into the canonical
domain model before renderer-specific processing occurs.

The renderer SHALL NOT derive engineering semantics directly from:

- repository paths;
- directory structures;
- Git-specific metadata;
- persistence-specific fields; or
- renderer-specific conventions.

The renderer MAY use physical representation information where required for
presentation or provenance, provided that such information does not redefine
the semantics of the Engineering Knowledge Model.

The canonical domain model SHALL remain the authoritative source for all
engineering semantics rendered by the Docusaurus Renderer.

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
Physical Foundation Representations
                │
                ▼
        Loader / Translation
                │
                ▼
   Canonical Engineering Knowledge Model
                │
                ▼
       Docusaurus Renderer
                │
                ▼
       Docusaurus Documentation
```

The renderer consumes Foundation artifacts but never modifies them.

---

## Rationale

Separating engineering knowledge from presentation enables multiple renderers to consume the same Foundation without introducing duplicate sources of truth.

The Docusaurus Renderer serves as the reference implementation of the ATON rendering architecture.

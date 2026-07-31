# NOTE-0004 — Canonical Serialization of Engineering Artifacts

## Context

ADR-0002 defines Markdown as the canonical authoring format for engineering
content.

The review identified that engineering artifacts consist of multiple components,
but only the serialization of the content is currently specified.

---

## Problem Statement

An engineering artifact consists of more than its textual content.

The canonical serialization of metadata, relations and future artifact
components has not yet been defined.

Without a normative definition, artifact serialization may become inconsistent
across tools and implementations.

---

## Questions

The engineering community should evaluate:

- Which serialization formats are canonical?
- Which artifact components are normative?
- Which components are mandatory?
- Which components are optional?
- How are future artifact components introduced?
- Which exchange formats may be generated from the canonical representation?

---

## Expected Outcome

Define the canonical serialization model for all Engineering Knowledge
artifacts.

The result should become part of the Engineering Knowledge Model and provide a
normative basis for future engineering artifacts.

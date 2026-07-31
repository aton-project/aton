# NOTE-0003 — Supported Markdown Profile

## Context

ADR-0002 defines Markdown as the canonical authoring format for engineering
content.

The review identified that the supported Markdown profile is currently
unspecified.

---

## Problem Statement

Different Markdown implementations support different syntax and extensions.

Without a normative definition, engineering artifacts may render or behave
differently across tools.

---

## Questions

The engineering community should evaluate:

- Which Markdown specification is canonical?
- Which extensions are permitted?
- Which extensions are mandatory?
- Which extensions are prohibited?
- How should future extensions be standardized?

---

## Expected Outcome

Define a normative Markdown profile for ATON that ensures interoperability,
long-term maintainability and implementation independence.

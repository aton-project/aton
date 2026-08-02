# NOTE-0014 — Logical and Physical Artifact Representation

## Context

The review of ADR-0005 identified that the Engineering Knowledge Model
distinguishes logical engineering concepts, while their physical
representation is not yet defined.

---

## Problem Statement

The Foundation currently separates engineering content, metadata and
relationships as logical concepts.

However, the relationship between these logical concepts and their physical
representation is unspecified.

Without a clear separation, implementations may incorrectly couple the
Engineering Knowledge Model to specific storage technologies or file
structures.

---

## Questions

The engineering community should evaluate:

- What constitutes the logical Engineering Knowledge Model?
- What constitutes the physical artifact representation?
- Which physical representations are supported?
- Which aspects are normative?
- Which aspects are implementation-specific?
- Can multiple physical representations describe the same logical artifact?
- How is consistency between logical and physical representations ensured?

---

## Expected Outcome

Define the relationship between the logical Engineering Knowledge Model and
its physical representations while preserving implementation independence.

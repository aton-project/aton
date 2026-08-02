# NOTE-0017 — Logical Engineering Knowledge Graph and Physical Representations

## Context

The review of ADR-0006 identified that the Engineering Knowledge Graph is
defined as the canonical logical structure of engineering knowledge.

However, the relationship between this logical model and its physical
representations is not yet defined.

---

## Problem Statement

The Engineering Knowledge Graph is a logical model.

Engineering artifacts, files, databases, APIs, and rendered views are
physical representations.

The Engineering Knowledge Model currently does not define how these
representations relate to the logical graph.

Without a clear separation, implementations may incorrectly couple the
conceptual model to specific storage technologies or representation formats.

---

## Questions

The engineering community should evaluate:

- What constitutes the logical Engineering Knowledge Graph?
- What constitutes a physical representation?
- Which representations are normative?
- Which representations are implementation-specific?
- Can multiple physical representations represent the same logical graph?
- How is consistency between the logical graph and physical representations
  ensured?

---

## Expected Outcome

Define the relationship between the logical Engineering Knowledge Graph and
its physical representations while preserving implementation independence.

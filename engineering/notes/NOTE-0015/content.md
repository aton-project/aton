# NOTE-0015 — Temporal Metadata Semantics

## Context

The review of ADR-0005 identified that temporal metadata is currently
persisted although equivalent information may already exist in Git history or
may be derived from the Engineering Knowledge Graph.

---

## Problem Statement

The Engineering Knowledge Model does not yet define the normative semantics of
temporal metadata.

Without clear rules, temporal information may become redundant, inconsistent,
or implementation-dependent.

---

## Questions

The engineering community should evaluate:

- Which temporal metadata shall be persisted?
- Which temporal metadata shall be derived from Git?
- Which temporal metadata shall be derived from the Engineering Knowledge
  Graph?
- Which timestamps are normative?
- Which timestamps are informative?
- How should derived temporal metadata be exposed to users and tools?

---

## Expected Outcome

Define a normative model for temporal metadata that ensures consistency while
avoiding redundant persistence.

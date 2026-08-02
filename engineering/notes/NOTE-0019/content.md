# NOTE-0019 — Temporal Metadata Semantics

## Context

The review of ADR-0006 identified that temporal metadata is currently
persisted although equivalent information may already exist in Git history or
may be derived from the Engineering Knowledge Graph.

---

## Problem Statement

The Engineering Knowledge Model currently does not define the normative
semantics of temporal metadata.

Without clear rules, temporal metadata may become redundant, inconsistent or
implementation-dependent.

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
- How should temporal metadata participate in traceability?

---

## Expected Outcome

Define a normative model for temporal metadata that ensures consistency while
avoiding redundant persistence.

# NOTE-0011 — Persisted and Derived Metadata

## Context

The review of ADR-0004 identified that artifact metadata may duplicate
information already available from Git or the Engineering Knowledge Graph.

---

## Problem Statement

The Engineering Knowledge Model currently does not distinguish between
persisted metadata and metadata that can be derived deterministically.

Without normative rules, redundant metadata may become inconsistent and
increase maintenance effort.

---

## Questions

The engineering community should evaluate:

- Which metadata shall be persisted?
- Which metadata shall be derived from Git?
- Which metadata shall be derived from the Engineering Knowledge Graph?
- Which metadata may be cached?
- Which metadata is normative?
- Which metadata is informative?

---

## Expected Outcome

Define a normative classification of persisted and derived metadata within the
Engineering Knowledge Model.

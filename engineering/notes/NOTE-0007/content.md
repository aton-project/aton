# NOTE-0007 — Derived Artifact Metadata

## Context

The review of ADR-0003 identified that temporal metadata is duplicated between
artifact metadata and Git history.

---

## Problem Statement

The Engineering Knowledge Model currently does not distinguish between persisted
metadata and metadata that can be derived deterministically from Git or the
Engineering Knowledge Graph.

Without clear rules, redundant metadata may become inconsistent.

---

## Questions

The engineering community should evaluate:

- Which metadata shall be persisted?
- Which metadata shall be derived from Git?
- Which metadata shall be derived from the Engineering Knowledge Graph?
- How should derived metadata be exposed to tools?
- What are the normative rules for persisted versus derived metadata?

---

## Expected Outcome

Define a normative metadata model distinguishing persisted metadata from derived
metadata.

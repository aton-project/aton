# NOTE-0005 — Architecture Decision Lifecycle

## Context

The review of ADR-0002 identified that the lifecycle of Architecture Decision
Records is currently undefined.

As a consequence, ADRs may appear as "accepted" although they are still under
review.

---

## Problem Statement

The Engineering Knowledge Model does not define a normative lifecycle for
Architecture Decision Records.

Without a defined lifecycle, the meaning of the ADR status is ambiguous and
cannot be interpreted consistently across tools and engineering processes.

---

## Questions

The engineering community should evaluate:

- Which lifecycle states exist for an ADR?
- Which transitions are permitted?
- Which engineering activities trigger a transition?
- Which roles are authorized to change the lifecycle state?
- Which lifecycle information should be stored explicitly?
- Which lifecycle information can be derived from the Engineering Knowledge
  Graph?

---

## Expected Outcome

Define a normative lifecycle model for Architecture Decision Records.

The lifecycle shall support engineering governance while avoiding redundant
metadata that can be derived from Git or the Engineering Knowledge Graph.

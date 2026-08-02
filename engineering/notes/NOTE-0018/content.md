# NOTE-0018 — Engineering Knowledge Navigation

## Context

The review of ADR-0006 identified that engineering knowledge shall be
navigable independently of any document structure.

However, the architectural meaning of navigation is currently undefined.

---

## Problem Statement

Navigation is a fundamental capability of the Engineering Knowledge Graph.

The Foundation does not currently define what navigation means, which
navigation concepts exist, or whether navigation is a property of the graph,
its representations, or the tools interacting with it.

Without a common understanding, implementations may provide inconsistent
navigation behaviour.

---

## Questions

The engineering community should evaluate:

- What is engineering knowledge navigation?
- Which navigation concepts are part of the Foundation?
- Which navigation capabilities are mandatory?
- Which navigation capabilities are implementation-specific?
- How does navigation relate to engineering relationships?
- How does navigation interact with different views?
- Which navigation concepts support traceability and impact analysis?

---

## Expected Outcome

Define the architectural concepts and semantics of engineering knowledge
navigation independently of any specific user interface or implementation.

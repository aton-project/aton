# NOTE-0006 — Engineering Semantics of Git Commits

## Context

The review of ADR-0003 identified that Git commits currently have only a
technical interpretation.

The engineering semantics associated with commits are not yet defined.

---

## Problem Statement

Git records changes, but the Engineering Knowledge Model does not define the
engineering meaning of a commit.

Without a common semantic interpretation, engineering history cannot be
interpreted consistently across projects and tools.

---

## Questions

The engineering community should evaluate:

- What engineering meaning does a Git commit represent?
- Does one commit correspond to one engineering activity?
- How should merge commits be interpreted?
- How should rebases and cherry-picks affect engineering traceability?
- Which engineering information belongs in commit messages?

---

## Expected Outcome

Define the engineering semantics of Git commits and their role within the
Engineering Knowledge Model.

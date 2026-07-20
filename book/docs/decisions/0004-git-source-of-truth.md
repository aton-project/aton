---
title: "0004 - Git as the Source of Truth"
description: Decision to use Git as the primary persistence and versioning technology.
---

# 0004 - Git as the Source of Truth

## Status

Accepted

## Date

2026-07-19

## Context

Engineering projects require complete traceability, reproducibility and collaboration.

Traditional engineering tools often implement proprietary repositories and custom versioning mechanisms.

ATON aims to build upon proven open technologies instead of replacing them.

Git already provides:

- distributed collaboration
- immutable history
- branching
- merging
- tagging
- proven scalability

Rather than introducing another repository, ATON integrates with Git.

---

## Decision

Git shall be the primary source of truth for persisted engineering knowledge.

Engineering artifacts are stored in a Git repository.

Git is responsible for file versioning and repository history.

ATON builds engineering semantics on top of Git.

---

## Consequences

### Positive

- Proven and mature technology
- Excellent collaboration support
- Offline-first workflow
- No proprietary repository
- Easy integration with existing development processes

### Negative

- Git versions files, not engineering concepts
- Additional mapping between Git commits and engineering versions is required

---

## Notes

Git does not replace the ATON Version model.

Git records changes to persisted data.

The ATON Version model records the evolution of engineering knowledge.

Both concepts complement each other.

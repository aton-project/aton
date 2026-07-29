# ADR-0003 — Git as the Version Control System

## Status

Accepted

---

## Context

Engineering knowledge evolves continuously throughout the lifecycle of a
system.

Every modification shall be traceable, reviewable, and reproducible.

The Foundation therefore requires a version control system that supports
distributed collaboration, complete history, branching, merging, and
long-term preservation of engineering knowledge.

---

## Decision

Git SHALL be the version control system for the Foundation.

All normative engineering knowledge SHALL be version controlled using Git.

Every change to the Foundation SHALL be represented by one or more Git
commits.

The Git history SHALL be considered part of the engineering knowledge.

The Foundation SHALL remain compatible with standard Git tooling.

---

## Consequences

This decision provides:

- complete change history
- distributed collaboration
- peer review through pull requests
- reproducible baselines
- branching and merging
- immutable historical revisions

Engineering knowledge becomes fully traceable over time.

---

## Rationale

Git is the de facto standard for distributed version control.

Its proven scalability, ecosystem, and tooling make it well suited for
managing engineering knowledge over long time periods.

Treating Git history as part of the engineering knowledge preserves the
rationale and evolution of engineering decisions.

---

## Alternatives Considered

### Centralized Version Control Systems

Rejected because centralized systems reduce flexibility and offline
collaboration.

### Database-only Storage

Rejected because version history becomes implementation dependent and less
transparent.

### Proprietary Version Control Systems

Rejected because they create unnecessary vendor dependencies.

---

## Architectural Principle

> Git is the canonical version control system of the Foundation.

> Engineering knowledge evolves through version-controlled changes.

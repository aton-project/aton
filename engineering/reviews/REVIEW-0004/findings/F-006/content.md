# F-006 — Redundant temporal metadata

## Observation

The artifact metadata contains creation and update timestamps.

## Problem

These values duplicate information available from Git.

## Recommendation

Remove redundant temporal metadata from the artifact model.

## Assessment

### Decision

Accepted

### Rationale

Temporal metadata should be addressed consistently across the Engineering
Knowledge Model rather than individually for each Architecture Decision
Record.

### Classification

Category: metadata

### Disposition

Create NOTE

### Execution

Verification: Pending

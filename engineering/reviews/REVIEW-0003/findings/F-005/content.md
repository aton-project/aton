# F-005 — Redundant temporal metadata

## Observation

The artifact metadata contains creation and update timestamps.

## Problem

These values duplicate information that can be derived from the Git history.

## Recommendation

Remove redundant temporal metadata from the artifact model.

## Assessment

### Decision

Accepted

### Rationale

The handling of temporal metadata affects the complete artifact model rather
than a single Architecture Decision Record.

### Classification

Category: metadata

### Disposition

Create NOTE

### Execution

Target: NOTE-0007

Verification: Pending

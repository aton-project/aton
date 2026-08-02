# F-006 — Redundant temporal metadata

## Observation

The artifact metadata contains temporal information.

## Problem

Temporal metadata can be derived from Git and should therefore not be
persisted redundantly.

## Recommendation

Review the necessity of persisted temporal metadata.

## Assessment

### Decision

Accepted

### Rationale

The treatment of temporal metadata requires dedicated engineering work.

### Classification

Category: metadata

### Disposition

Create NOTE

### Execution

Verification: Pending

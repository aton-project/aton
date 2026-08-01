# F-006 — Redundant temporal metadata

## Observation

The artifact metadata contains temporal information.

## Problem

Temporal metadata can be derived from Git and should therefore not be
persisted redundantly.

## Recommendation

Review the necessity of persisted temporal metadata.

# F-005 — Redundant temporal metadata

## Observation

The artifact metadata contains creation and update timestamps.

## Problem

These values duplicate information that can be derived from the Git history.

## Recommendation

Remove redundant temporal metadata from the artifact model.

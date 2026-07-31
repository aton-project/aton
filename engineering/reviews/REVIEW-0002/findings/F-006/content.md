# F-006 — Redundant Temporal Metadata

## Observation

The artifact metadata contains creation and update timestamps.

## Problem

These values can be derived deterministically from the Git history and therefore
duplicate information already maintained by the version control system.

## Recommendation

Remove temporal metadata from the artifact model and derive it from Git.

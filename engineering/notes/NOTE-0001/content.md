# Embedded Artifacts

## Context

During the review of ADR-0001 it was observed that Findings were modeled as standalone artifacts.

## Problem Statement

A Finding only exists within the context of a Review. This raises the question whether the Engineering Knowledge Model should distinguish between standalone artifacts and embedded artifacts.

## Discussion

Potential benefits include:

- clearer ownership
- context-local identifiers
- simpler repository structure
- reduced number of globally managed artifacts

Potential drawbacks and alternative solutions need to be evaluated.

## Questions

- Should embedded artifacts become a first-class concept in the EKM?
- Which artifact types could be embedded?
- What are the implications for traceability and versioning?

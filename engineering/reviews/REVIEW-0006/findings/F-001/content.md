# F-001 — Entity and Artifact are not distinguished

## Observation

ADR-0006 describes the Engineering Knowledge Graph as a graph of artifacts.

## Problem

The current Engineering Knowledge Model distinguishes between engineering
entities and engineering artifacts.

It is therefore unclear which concept represents the nodes of the
Engineering Knowledge Graph.

## Recommendation

Avoid binding the Engineering Knowledge Graph to artifacts until the
Engineering Knowledge Model defines the relationship between entities and
artifacts.

## Assessment

### Decision

Accepted

### Rationale

The distinction between engineering entities and engineering artifacts should
be reflected consistently within the Engineering Knowledge Graph.

### Classification

Category: architecture

### Disposition

Direct Implementation

### Execution

Verification: Pending

# Canonical Relation Model Required

## Summary

During the implementation of the Foundation verification subsystem an
architectural inconsistency regarding relation handling was discovered.

The issue is not located in the verification subsystem itself but in the
absence of a canonical internal representation for relations.

## Observations

Three different relation serialization formats currently exist within the
Foundation.

### Legacy list format

```yaml
[]
```

### Mapping format

```yaml
references:
  - RFC-0001

dependsOn:
  - ADR-0003
```

### Embedded object format

```yaml
relations:
  - type: refines
    target: AX-0001
```

Each format is currently interpreted differently by the kernel.

As a consequence, kernel components started to depend on serialization details
instead of a stable domain model.

## Root Cause

The loader currently imports serialized relation structures without converting
them into a canonical kernel representation.

Therefore every downstream component must understand persistence formats.

This violates separation of concerns.

## Consequences

Kernel components should never interpret serialized file structures.

Instead they should operate exclusively on a canonical relation domain model.

Normalization belongs into the loader.

The loader therefore becomes the Anti-Corruption Layer between persistent
storage and the kernel.

## Proposed Direction

Introduce a dedicated Relation domain object.

The loader shall normalize all supported serialization formats into this
canonical representation.

Subsequently the verification subsystem, renderer and future reasoning
components operate exclusively on the Relation domain model.

## Expected Benefits

- One canonical kernel representation
- Strict separation between persistence and domain model
- Simpler verification implementation
- Stable API for renderer and AI components
- Easier import of external formats (ReqIF, JSON, GitHub, ...)

## Follow-up

This observation motivates a future Architecture Decision Record defining the
Canonical Domain Model as a kernel design principle.

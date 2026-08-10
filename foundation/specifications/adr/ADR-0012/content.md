# Engineering Version and Baseline Semantics

## Context

ATON engineering knowledge evolves over time.

This evolution can be observed at several different levels, including
engineering entities, engineering artifacts, physical representations, Git
revisions, baselines and releases.

These concepts are related but have different semantic meanings.

Without an explicit distinction, implementations may incorrectly treat a Git
revision as an engineering version, an artifact revision as an engineering
release, or a baseline as merely a Git tag.

ATON therefore requires a version model that is independent of any particular
version-control or persistence implementation.

## Problem Statement

The Engineering Knowledge Model does not yet define the semantic relationship
between:

- engineering identity;
- engineering versions;
- artifact revisions;
- Git revisions;
- baselines; and
- releases.

These concepts must be distinguished so that engineering knowledge can evolve
while preserving identity, traceability and reproducibility.

## Decision

ATON SHALL distinguish engineering identity, engineering versions, artifact
revisions, technical revisions, baselines and releases.

An engineering identity SHALL represent the persistent identity of an
engineering concept across its evolution.

An engineering version SHALL represent a distinct semantic state of an
engineering concept.

An artifact revision SHALL represent a revision of a physical or logical
artifact representation.

A Git revision SHALL represent a technical revision recorded by Git.

A baseline SHALL represent an explicitly defined and reproducible selection
of engineering knowledge at a particular state.

A release SHALL represent an explicitly released engineering state or
baseline.

These concepts SHALL NOT be treated as interchangeable.

## Engineering Identity

Engineering identity SHALL remain stable across versions of the same
engineering concept.

A change to an engineering concept SHALL NOT automatically create a new
identity.

A new identity SHALL be created when the engineering meaning changes such
that the resulting concept is no longer considered the same engineering
concept.

The rules for determining identity are part of the semantic model and SHALL
NOT depend on physical file names or repository paths.

## Engineering Version

An engineering version SHALL represent a distinct semantic state of an
engineering concept.

A new engineering version SHALL be created when the engineering meaning or
normative state of the concept changes in a way that is relevant to its
engineering identity.

An engineering version SHALL be independent of the number or identity of Git
commits used to produce it.

Multiple Git revisions MAY contribute to one engineering version.

A single Git revision MAY contain changes affecting multiple engineering
versions.

## Artifact Revision

An artifact revision SHALL represent a change to an artifact or its physical
representation.

Artifact revision and engineering version SHALL NOT be assumed to have a
one-to-one relationship.

A physical artifact MAY change without changing the semantic engineering
version.

Conversely, one engineering version MAY require changes to multiple physical
artifacts.

## Git Revisions

Git revisions SHALL be treated as technical historical records.

A Git commit or revision MAY provide evidence about the evolution of
engineering knowledge.

A Git revision SHALL NOT automatically constitute an engineering version.

Git tags SHALL NOT automatically constitute engineering releases or
baselines.

Git-specific concepts SHALL remain implementation-specific unless explicitly
mapped into the canonical Engineering Knowledge Model.

## Baselines

A baseline SHALL represent an explicitly defined and reproducible state of
engineering knowledge.

A baseline MAY contain multiple engineering entities, artifacts or versions.

The identity of a baseline SHALL refer to its selected engineering state and
not merely to the physical representation used to store it.

A baseline SHALL be reproducible from the authoritative engineering
information from which it was created.

A baseline MAY be represented by a Git revision, Git tag or another technical
mechanism, but that representation SHALL NOT by itself define the semantic
meaning of the baseline.

## Releases

A release SHALL represent an explicitly released engineering state.

A release SHALL identify the engineering state that has been released.

A release SHOULD reference a baseline or equivalent reproducible engineering
state.

A release SHALL therefore be distinguishable from a Git tag or other
technical marker.

A technical marker MAY be used to identify or retrieve a release, but the
technical marker is not itself the release semantics.

## Immutability

Engineering versions, baselines and releases SHALL be immutable once they
have been formally established as authoritative engineering states.

New engineering changes SHALL result in new versions or new baselines rather
than silently modifying an established state.

Physical representations MAY evolve independently, provided that previously
established engineering states remain reproducible.

## Temporal Information

Temporal information and version semantics SHALL remain distinct.

A timestamp records information about an event or state in time.

A version identifies a semantic engineering state.

Therefore, the existence of a newer timestamp SHALL NOT by itself imply the
existence of a new engineering version.

Temporal metadata SHALL be governed by the canonical metadata model.

## Traceability

Changes between engineering versions SHOULD remain traceable through the
Engineering Knowledge Graph and the applicable relation model.

Traceability MAY include links between:

- engineering versions;
- artifact revisions;
- Git revisions;
- baselines;
- releases; and
- engineering decisions.

Such traceability SHALL preserve the distinction between semantic
engineering states and technical implementation history.

## Consequences

### Positive

- Engineering versions are independent of Git.
- Alternative persistence and version-control systems can be supported.
- Baselines and releases have explicit semantic meaning.
- Git history can provide useful technical evidence without becoming the
  domain model.
- Engineering states can be reproduced independently of a particular
  physical representation.
- Traceability can distinguish semantic evolution from implementation
  history.

### Negative

- Implementations must maintain explicit version semantics.
- Version, baseline and release concepts require additional domain modeling.
- Mapping between technical revisions and engineering states requires explicit
  rules.
- Reproducibility of baselines requires sufficient authoritative information
  to be retained.

## Relationship to Other Decisions

ADR-0010 defines the canonical metadata model and establishes the distinction
between canonical metadata and derived information.

ADR-0011 defines the separation between the logical Engineering Knowledge
Model and its physical representations.

The canonical relation model and semantic relation constraints define how
versioned engineering concepts may participate in traceability.

## Alternatives Considered

### Treat Git revisions as engineering versions

Rejected.

Git revisions are technical history and do not necessarily correspond to
semantic engineering states.

### Treat Git tags as releases

Rejected.

A Git tag is a technical marker. Release semantics require an explicit
engineering state.

### Treat baselines as Git commits

Rejected.

A Git commit may be used to reproduce a baseline in a Git-based
implementation, but the semantic definition of a baseline must remain
independent of Git.

### Use timestamps to identify versions

Rejected.

Temporal information does not by itself define semantic engineering change.

## Expected Outcome

ATON SHALL provide a version model in which engineering identity, engineering
versions, artifact revisions, technical revisions, baselines and releases
have distinct semantic meanings.

Engineering state SHALL remain independent of the persistence and version
control mechanisms used to represent it.

Git MAY provide technical history and reproducibility mechanisms, but SHALL
NOT define the semantics of engineering versions, baselines or releases.

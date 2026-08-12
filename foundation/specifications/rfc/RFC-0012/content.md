# RFC-0012 — Engineering Version Semantics

## Status

Draft

## Summary

This RFC defines the normative version semantics of the ATON Engineering
Knowledge Model.

Engineering knowledge evolves over time. The Engineering Knowledge Model
therefore requires a distinction between an engineering concept and the
different states in which that concept exists during its lifecycle.

This RFC defines:

- Engineering Versions;
- version identity;
- version relationships;
- immutable engineering states;
- the relationship between versions and artifacts;
- the relationship between versions and Git revisions;
- provenance of engineering versions; and
- the distinction between versions, baselines and releases.

A Git revision SHALL NOT automatically constitute an Engineering Version.

An Engineering Version represents a semantic engineering state, while Git
provides version-control and provenance information for the physical
representation of that state.

## Motivation

Engineering artifacts evolve over time.

A requirement may change, an architecture decision may be superseded, a
relation may be added, or metadata may be corrected.

Git already records physical changes to the repository, but Git commits alone
do not provide the complete semantic model required by the Engineering
Knowledge Model.

In particular, the following concepts must remain distinguishable:

- engineering identity;
- engineering version;
- Git revision;
- baseline;
- release;
- engineering activity.

Without this distinction, tools may incorrectly treat technical repository
events as engineering states.

## Goals

This RFC SHALL:

- define the semantics of an Engineering Version;
- preserve stable engineering identity across versions;
- define how versions relate to engineering artifacts;
- distinguish versions from Git revisions;
- define provenance relationships between versions and Git;
- support immutable historical engineering states;
- provide a foundation for baselines and releases;
- support traceability across engineering evolution; and
- remain independent of a particular persistence implementation.

## Non-Goals

This RFC does not define:

- Git itself;
- Git branching strategies;
- Git workflow conventions;
- release management processes;
- approval processes;
- engineering review processes;
- organizational roles;
- semantic versioning schemes such as major/minor/patch;
- baseline selection procedures;
- release approval procedures; or
- a specific user interface for version navigation.

These concerns may be defined by separate process or governance models.

## Engineering Identity

An Engineering Entity represents a stable engineering concept.

Its identity SHALL remain stable across changes to its content, metadata or
relations unless the applicable domain model explicitly defines the entity as
a new engineering concept.

For example, changing the wording of a requirement SHALL NOT automatically
create a new requirement identity.

The identity of an entity SHALL therefore be distinct from the identity of
any individual version of that entity.

## Engineering Version

An Engineering Version represents a distinct semantic state of an
Engineering Entity.

A version SHALL describe the state of the entity at a particular point in
its engineering evolution.

Two versions of the same entity SHALL share the same engineering identity
while representing different engineering states.

A version MAY differ from another version in:

- content;
- metadata;
- relations;
- lifecycle state; or
- other versioned properties defined by the applicable domain model.

## Version Identity

An Engineering Version SHALL be uniquely identifiable within the applicable
Engineering Knowledge Model scope.

A version identifier SHALL NOT be derived solely from:

- a file path;
- a Git branch;
- a Git commit hash;
- a document title;
- a timestamp; or
- a repository directory.

A conforming implementation MAY use a Git revision as part of a version
identifier or provenance record, but such usage SHALL NOT make Git identity
the semantic definition of the Engineering Version.

## Version Relationships

Versions of the same Engineering Entity SHALL be ordered or related by
explicit version relationships.

A version MAY identify:

- a predecessor version;
- a successor version;
- a parent version; or
- other applicable version relationships.

The exact representation of these relationships SHALL be defined by the
applicable domain model.

A version history SHALL preserve the distinction between different states of
the same Engineering Entity.

## Version Immutability

An established Engineering Version SHALL be immutable.

Once a version has been established as an engineering state, its semantic
content SHALL NOT be modified in place.

A change to an established version SHALL result in a new Engineering Version.

This requirement preserves historical reproducibility.

Physical persistence mechanisms MAY represent immutable versions through
different technical mechanisms, provided that the semantic immutability is
preserved.

## Current State

The current state of an Engineering Entity SHALL be represented by its
applicable current Engineering Version.

The current version MAY evolve as new versions are established.

The current state SHALL NOT invalidate historical versions.

A tool MAY provide a convenient "current" view, but such a view SHALL NOT
replace the historical version model.

## Version Creation

A new Engineering Version SHALL be created when the semantic state of an
Engineering Entity changes in a manner that is relevant to the Engineering
Knowledge Model.

Examples include:

- a substantive content change;
- a change to normative metadata;
- a change to a semantic relation;
- a lifecycle state transition; or
- another change defined by the applicable domain specification.

A purely technical change that does not alter the semantic engineering state
MAY be recorded in version-control history without creating a new Engineering
Version.

## Version and Artifact

An Engineering Artifact is a logical engineering representation according
to RFC-0010.

An Engineering Version represents the semantic state of an Engineering
Entity.

An Engineering Artifact MAY represent information belonging to one or more
Engineering Versions over its lifecycle.

A physical artifact representation SHALL NOT be treated as the Engineering
Version itself.

Artifact Revision and Engineering Version semantics SHALL remain distinct.

## Version and Git

Git records revisions of the physical repository representation.

A Git commit identifies a repository state and its parent relationships.

A Git commit SHALL NOT automatically be interpreted as an Engineering
Version.

A Git commit MAY provide provenance for an Engineering Version when the
version is represented by the repository state associated with that commit.

The relationship is therefore:

    Engineering Entity
            |
            +-- Engineering Version
                    |
                    +-- provenance --> Git Revision

This relationship allows ATON to retain engineering version semantics without
requiring Git as the persistence mechanism.

## Git Commit Semantics

A Git commit SHALL be interpreted as a technical version-control event.

A commit may provide evidence that a physical representation changed.

A commit MAY correspond to one or more engineering activities.

A commit MAY contain changes to one or more Engineering Entities.

A commit MAY also contain changes that have no direct engineering semantic
meaning.

Therefore:

- one commit does not necessarily correspond to one Engineering Activity;
- one commit does not necessarily correspond to one Engineering Version;
- one Engineering Activity may produce multiple commits; and
- one Engineering Version may be represented by changes across multiple
  commits.

A conforming implementation SHALL NOT infer engineering activity semantics
solely from commit boundaries.

## Commit Provenance

Git commits MAY be associated with Engineering Versions as provenance
evidence.

Such provenance MAY identify:

- the Git repository;
- the Git commit;
- the relevant path or artifact;
- the relationship between the commit and the engineering version; and
- additional provenance information.

Provenance SHALL remain distinguishable from semantic version identity.

A Git commit hash SHALL therefore be treated as a technical identifier and
not as the canonical identifier of an Engineering Version.

## Merge Commits

A merge commit represents a Git operation combining repository histories.

A merge commit SHALL NOT automatically represent:

- a new Engineering Version;
- an Engineering Activity;
- an architectural decision; or
- a baseline.

An implementation MAY associate a merge commit with engineering provenance
when appropriate.

The semantic meaning of the resulting engineering state SHALL be determined
by the Engineering Knowledge Model rather than by the fact that the Git
operation was a merge.

## Rebases

A Git rebase rewrites technical repository history.

A rebased commit may therefore receive a different Git identity while
representing substantially the same engineering change.

Engineering Version identity SHALL NOT depend solely on Git commit identity.

A conforming implementation SHOULD preserve engineering provenance where
possible when Git history is rewritten.

## Cherry-Picks

A cherry-pick creates a new Git commit containing changes derived from
another commit.

The resulting commit SHALL be treated as a new technical Git revision.

It SHALL NOT automatically create a new Engineering Version unless the
resulting engineering state constitutes a new semantic version according to
the versioning rules.

## Version Provenance

Engineering Version provenance MAY include information from:

- Git commits;
- engineering activities;
- reviews;
- process instances;
- verification results;
- external systems; or
- other engineering evidence.

Provenance information SHALL explain or support the origin of an Engineering
Version.

Provenance SHALL NOT replace the explicit identity or semantics of the
Engineering Version.

## Version Comparison

Two Engineering Versions MAY be compared to determine their semantic
differences.

Comparison MAY include:

- content changes;
- metadata changes;
- relation changes;
- lifecycle changes; and
- other versioned properties.

A Git diff MAY provide technical evidence for such comparison but SHALL NOT
be assumed to represent the complete semantic difference between Engineering
Versions.

## Version History

The Engineering Knowledge Model SHALL preserve the ability to reconstruct
the relevant history of an Engineering Entity.

Version history SHOULD allow tools to determine:

- which versions existed;
- their order or relationships;
- their semantic state;
- their provenance; and
- which version was current at a relevant point in engineering history.

Historical versions SHALL remain addressable where required for traceability,
auditability or reproducibility.

## Versions and Relations

Relations MAY change between versions.

A relation that exists in one Engineering Version SHALL NOT automatically be
assumed to exist in another version.

Relation history SHALL therefore be interpreted in the context of the
relevant Engineering Version.

The canonical relation model defines relation semantics independently of
versioning.

Version semantics determine the state in which those relations exist.

## Versions and Lifecycle

Lifecycle state and Engineering Version are distinct concepts.

A lifecycle transition MAY create a new Engineering Version when the
transition changes the semantic state of the Engineering Entity.

A lifecycle state SHALL NOT itself be treated as a version identifier.

The applicable lifecycle model determines the semantic meaning of lifecycle
states.

## Versions and Baselines

A Baseline represents a defined collection or state of Engineering
Knowledge.

A Baseline MAY reference Engineering Versions, Engineering Entities,
Engineering Artifacts or other canonical Engineering Knowledge objects as
defined by the applicable Baseline model.

A Baseline SHALL identify the engineering state it represents rather than
being defined merely by arbitrary Git commits.

Git information MAY provide provenance for the state from which a Baseline
was constructed.

Baseline semantics are defined separately by RFC-0013.

## Versions and Releases

A Release represents a defined engineering state made available according to
an applicable release model.

A Release MAY reference:

- Engineering Versions;
- a Baseline;
- Git revisions; or
- other provenance information.

A Release SHALL NOT be defined solely by a Git tag or commit unless the
applicable release specification explicitly establishes such a mapping.

Release semantics are defined separately from Engineering Version semantics.

## Persistence Independence

The Engineering Version model SHALL remain independent of the persistence
technology.

Git is the canonical version-control system for the current ATON Foundation
implementation according to ADR-0003.

However, the Engineering Knowledge Model SHALL NOT require Git in order to
express Engineering Versions.

An alternative persistence implementation MAY provide equivalent provenance
information using another version-control or persistence mechanism.

## Verification

ATON MAY verify version consistency.

Verification MAY detect:

- duplicate version identifiers;
- invalid version relationships;
- modification of immutable versions;
- missing version references;
- inconsistent provenance;
- invalid baseline membership; or
- inconsistent historical state.

Verification rules SHALL operate on canonical domain concepts rather than
repository-specific implementation details.

## Migration

Existing engineering artifacts may not have explicit Engineering Version
identifiers.

A migration implementation MAY reconstruct version history from available
repository and artifact information.

Git history MAY provide provenance evidence during migration.

Migration SHALL NOT assume that every Git commit represents a distinct
Engineering Version.

Where semantic version boundaries cannot be determined reliably, the
implementation SHALL preserve the uncertainty rather than invent semantic
version information.

## Consequences

### Positive

- Engineering versions remain independent of Git.
- Historical engineering states are explicitly represented.
- Git commits can provide useful provenance without becoming domain
  concepts.
- Baselines and releases can build on explicit Engineering Versions.
- Alternative persistence implementations remain possible.
- Version history can support traceability and reproducibility.

### Negative

- Engineering Version identity must be maintained explicitly.
- Version boundaries may require engineering or process semantics.
- Git history alone may not be sufficient to reconstruct complete semantic
  version history.
- Additional provenance information may be required for high-assurance
  engineering environments.

## Alternatives

### Treat every Git commit as an Engineering Version

Rejected.

Git commits represent technical repository states and do not necessarily
correspond to semantic engineering changes.

### Use Git commit hashes as Engineering Version identifiers

Rejected.

This would make the domain model dependent on Git and would not support
alternative persistence implementations.

### Treat the physical artifact as the version

Rejected.

A physical artifact is a representation of engineering knowledge and may
change over time.

### Derive all version information from Git

Rejected.

Git provides technical history but does not necessarily provide semantic
engineering boundaries.

### Use timestamps as version identity

Rejected.

Timestamps do not provide stable semantic identity and may not uniquely
identify engineering states.

## Open Questions

The following topics remain outside the normative scope of this RFC and may
be addressed by future specifications:

- version numbering conventions;
- version labels;
- automatic version detection;
- version branching semantics;
- detailed provenance models;
- cross-repository version identity;
- version equivalence;
- version merging;
- detailed baseline construction rules; and
- release management semantics.

## Acceptance Criteria

A conforming implementation SHALL:

1. distinguish Engineering Entity identity from Engineering Version identity;
2. treat established Engineering Versions as immutable;
3. distinguish Engineering Versions from Git commits;
4. permit Git commits to provide version provenance;
5. avoid interpreting every commit as an Engineering Version;
6. preserve version history;
7. permit relation state to vary between versions;
8. keep version semantics independent of persistence technology;
9. distinguish versions from baselines and releases; and
10. avoid inventing semantic version information when historical evidence is
    insufficient.

## References

- ADR-0003 Git as the Version Control System
- ADR-0012 Engineering Version and Baseline Semantics
- ADR-0011 Logical Engineering Knowledge Model and Physical Representations
- RFC-0013 Baselines
- RFC-0023 Traceability
- NOTE-0006 Engineering Semantics of Git Commits
- NOTE-0009 Engineering Version Semantics

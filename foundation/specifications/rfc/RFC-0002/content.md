# RFC-0002 — Engineering Identity Model

## Status

Draft

## Summary

This RFC defines the canonical identity model for engineering knowledge within
ATON.

An Engineering Identity represents the persistent identity of an engineering
concept across its evolution.

Engineering Identity SHALL remain distinct from Engineering Version, Artifact
Revision, Git Revision and physical representation.

The identity model provides the stable semantic reference required for
traceability, versioning, navigation and historical engineering knowledge.

## Motivation

Engineering knowledge evolves over time.

An engineering concept may change its content, metadata, relationships or
physical representation while remaining the same engineering concept.

Conversely, a change may alter the engineering meaning sufficiently that the
resulting concept is no longer considered the same engineering concept.

Without a stable identity model, implementations may incorrectly derive
identity from:

- file names;
- repository paths;
- Git commits;
- version numbers;
- database identifiers;
- document locations; or
- other physical representations.

Such an approach would make engineering identity dependent on implementation
details and would prevent reliable traceability across changes and
representations.

ATON therefore requires an implementation-independent semantic identity model.

## Goals

This RFC SHALL:

- define Engineering Identity;
- define the stability of Engineering Identity;
- distinguish Engineering Identity from Engineering Version;
- distinguish Engineering Identity from Artifact Revision;
- distinguish Engineering Identity from Git Revision;
- define requirements for identity identifiers;
- preserve identity across physical representation changes;
- support historical traceability;
- support version-aware engineering knowledge; and
- remain independent of persistence and version-control technology.

## Non-Goals

This RFC does not define:

- Engineering Version semantics in detail;
- Artifact Revision semantics in detail;
- Baseline semantics;
- Release semantics;
- Git workflow conventions;
- repository layout;
- physical serialization formats;
- database identifiers;
- user-interface behaviour;
- naming conventions for engineering concepts; or
- project-specific identity policies.

Engineering Version semantics are defined separately by RFC-0012.

Physical representation semantics are defined separately by RFC-0015.

## Engineering Identity

An Engineering Identity SHALL represent the persistent identity of an
engineering concept across its semantic evolution.

The identity SHALL identify the engineering concept rather than a particular
representation of that concept.

An Engineering Identity SHALL remain stable while the engineering concept
continues to be considered the same concept.

A change to the content, metadata, relationship set or physical representation
of an engineering concept SHALL NOT by itself create a new Engineering
Identity.

A new Engineering Identity SHALL be created when the engineering meaning has
changed to the extent that the resulting concept is no longer considered the
same engineering concept.

The determination of whether two concepts represent the same Engineering
Identity is a semantic engineering decision and SHALL NOT be determined solely
by physical representation.

## Identity Identifier

Each Engineering Identity SHALL have a unique identifier within the applicable
Engineering Knowledge scope.

An identity identifier SHALL be:

- stable;
- unique within its applicable scope;
- persistent across Engineering Versions;
- independent of physical storage location; and
- independent of Git revision identity.

An identity identifier SHOULD be opaque with respect to the semantic meaning
of the identified concept.

An implementation MAY use UUIDs or another suitable identifier mechanism,
provided that the resulting identifier satisfies the requirements of this
RFC.

An identity identifier SHALL NOT be reused for a different Engineering
Identity after the original identity has been established.

## Identity and Engineering Versions

An Engineering Identity MAY have multiple Engineering Versions.

An Engineering Version represents a distinct semantic state of an Engineering
Identity.

Conceptually:

    Engineering Identity
            |
            +-- Engineering Version
            |
            +-- Engineering Version
            |
            +-- Engineering Version

The Engineering Identity remains stable while the Engineering Versions
represent its evolution.

A new Engineering Version SHALL NOT automatically create a new Engineering
Identity.

A new Engineering Identity MAY be created when the semantic change is
sufficient to establish a different engineering concept.

The detailed semantics of Engineering Versions are defined by RFC-0012.

## Identity and Artifact Revisions

An Engineering Identity MAY be represented by one or more physical or logical
artifacts.

An Artifact Revision represents a revision of such a representation.

An Artifact Revision SHALL NOT by itself define the Engineering Identity.

The same Engineering Identity MAY therefore be represented by multiple
artifacts or artifact revisions.

Conversely, a single physical artifact MAY represent information associated
with multiple Engineering Identities.

Physical representation SHALL therefore remain distinct from semantic
identity.

## Identity and Git

Git provides technical identity for repository objects and revisions.

A Git commit hash SHALL NOT be treated as the canonical identifier of an
Engineering Identity.

A Git revision MAY provide provenance for an Engineering Identity or one of its
Engineering Versions.

Changing Git history through operations such as rebase or cherry-pick SHALL
NOT inherently change Engineering Identity.

A Git repository MAY therefore contain different technical representations of
the same Engineering Identity.

Git-specific identity SHALL remain implementation-specific unless explicitly
mapped into the canonical Engineering Knowledge Model.

## Identity and Physical Representation

An Engineering Identity SHALL remain independent of physical representation.

The following SHALL NOT determine Engineering Identity:

- repository path;
- file name;
- directory location;
- serialization format;
- database key;
- URL;
- generated document location; or
- rendering technology.

A physical representation MAY change while preserving the same Engineering
Identity.

An Engineering Identity MAY also be represented simultaneously by multiple
physical representations.

The mapping between an Engineering Identity and its physical representations
SHALL be handled at the representation boundary defined by the applicable
architecture.

## Identity and Relationships

Engineering relationships SHALL reference Engineering Knowledge according to
the canonical domain model.

Where a relationship is associated with an Engineering Identity, the identity
SHALL remain distinguishable from a particular Engineering Version or
physical representation.

A relationship associated with one Engineering Version SHALL NOT
automatically be assumed to exist in every other version of the same
Engineering Identity.

Version-specific relationship semantics SHALL be governed by the applicable
version and relation models.

## Identity and Historical Knowledge

Established Engineering Identities SHALL remain addressable throughout their
preserved engineering history.

Superseding an Engineering Identity with another concept SHALL NOT require
the historical identity to be deleted.

Historical engineering knowledge MAY therefore continue to reference an
Engineering Identity even when that identity is no longer current.

This preserves traceability across engineering evolution.

## Identity Changes

A change in engineering meaning SHALL be evaluated semantically.

The following changes do not automatically require a new Engineering Identity:

- correction of an error;
- modification of descriptive text;
- metadata changes;
- physical file relocation;
- migration to another serialization format;
- migration to another repository;
- changes to rendering technology; or
- creation of a new Engineering Version.

A new Engineering Identity SHOULD be established when the resulting concept
has a materially different engineering meaning or purpose and is no longer
considered the same engineering concept.

Identity changes SHALL preserve traceability to the preceding engineering
knowledge where such traceability is meaningful.

## Identity and Deletion

Deletion of a physical representation SHALL NOT automatically delete the
Engineering Identity.

If an Engineering Identity is no longer active, its historical identity MAY
be preserved as part of the Engineering Knowledge Model.

The semantic state of an identity, including whether it is active, obsolete,
superseded or otherwise no longer current, SHALL be represented through the
applicable lifecycle and relation semantics rather than by destroying its
identity.

## Identity Scope

Identity SHALL be unique within the applicable Engineering Knowledge scope.

An implementation MAY define scopes such as:

- a project;
- an Engineering Knowledge repository;
- an organization; or
- another explicitly defined knowledge domain.

The scope SHALL be explicit where identity resolution crosses persistence or
organizational boundaries.

Two identifiers that are identical as strings SHALL NOT automatically be
assumed to identify the same Engineering Identity when they belong to
different identity scopes.

External identity mappings MAY be established when engineering knowledge is
integrated across scopes.

## Identity Resolution

A conforming implementation SHALL be able to resolve an Engineering Identity
from its canonical identifier within the applicable identity scope.

Identity resolution SHALL be independent of the physical location of the
representation.

An unresolved identity SHALL remain distinguishable from an invalid or
non-existent identity reference.

External identity resolution MAY be supported where the applicable
persistence or integration mechanism provides such capability.

## Immutability of Identity

The identity identifier of an established Engineering Identity SHALL be
immutable.

Changes to the engineering concept SHALL be represented through Engineering
Versions or, where appropriate, through a new Engineering Identity.

An implementation SHALL NOT silently reassign an established identity
identifier to another engineering concept.

## Migration

Existing engineering artifacts that do not have explicit Engineering
Identities SHALL be assigned identities during migration.

Migration SHALL attempt to preserve existing semantic continuity.

A migration SHALL NOT assume that:

- every file represents one Engineering Identity;
- every Git commit represents one Engineering Identity;
- every version number represents an Engineering Identity; or
- every repository path represents an Engineering Identity.

Where identity cannot be established unambiguously, the implementation SHOULD
record the ambiguity rather than silently creating an incorrect identity
mapping.

Existing physical identifiers MAY be retained as provenance or aliases, but
they SHALL NOT replace the canonical Engineering Identity.

## Consequences

### Positive

- Engineering identity remains stable across semantic evolution.
- Engineering Versions can evolve without changing identity.
- Physical representation can change without changing identity.
- Git remains separate from the semantic identity model.
- Historical traceability can be preserved.
- Alternative persistence mechanisms remain possible.
- Identity can support navigation, versioning and traceability.

### Negative

- Implementations must maintain explicit identity information.
- Determining whether a change preserves identity requires semantic judgment.
- Cross-repository identity resolution requires explicit scope and mapping.
- Migration of existing artifacts may require manual decisions where identity
  cannot be inferred reliably.

## Alternatives Considered

### Use file paths as Engineering Identity

Rejected.

File paths are physical representation details and may change independently
of engineering meaning.

### Use file names as Engineering Identity

Rejected.

File names are not guaranteed to be unique, stable or semantically
authoritative.

### Use Git commit hashes as Engineering Identity

Rejected.

Git commits represent technical repository history rather than persistent
engineering concepts.

### Use Engineering Version identifiers as Engineering Identity

Rejected.

An Engineering Identity must remain stable across multiple Engineering
Versions.

### Generate a new identity for every modification

Rejected.

This would prevent stable traceability across the evolution of an engineering
concept.

## Relationship to Other Specifications

ADR-0012 establishes the distinction between Engineering Identity and
Engineering Version.

RFC-0012 defines Engineering Version semantics.

RFC-0015 defines the separation between logical Engineering Knowledge and
physical representations.

RFC-0025 defines the canonical Relation domain model.

RFC-0029 defines semantic constraints for relations.

The Entity and Artifact model further defines the concepts that may carry or
refer to Engineering Identity.

## Acceptance Criteria

A conforming implementation SHALL:

1. provide a stable identifier for each established Engineering Identity;
2. preserve identity across Engineering Versions;
3. keep identity independent of physical file paths and repository structure;
4. keep identity independent of Git commit identity;
5. prevent reuse of an established identity identifier for another concept;
6. distinguish unresolved identities from non-existent identities; and
7. preserve historical identity where the applicable engineering knowledge is
   retained.

## Open Questions

The following questions remain open for future specifications:

- Should ATON standardize UUID as the canonical identifier format?
- What is the default identity scope for distributed Engineering Knowledge?
- How should identity mappings between independent Engineering Knowledge
  domains be represented?
- Should identity aliases be standardized?

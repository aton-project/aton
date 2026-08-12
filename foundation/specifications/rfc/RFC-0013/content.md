# RFC-0013 — Engineering Baseline Semantics

## Status

Draft

## Summary

This RFC defines the canonical semantics of Engineering Baselines within the
ATON Engineering Knowledge Model.

A Baseline represents an explicitly defined and reproducible selection of
engineering knowledge at a particular engineering state.

A Baseline is distinct from:

- an Engineering Entity;
- an Engineering Version;
- an Artifact Revision;
- a Git Revision; and
- a Release.

A Baseline MAY be represented by a technical persistence mechanism such as a
Git revision or Git tag, but its semantic identity SHALL remain independent
of that mechanism.

## Motivation

Engineering projects require stable reference states.

A project may need to identify the exact engineering knowledge used for:

- a review;
- a verification activity;
- a design milestone;
- a qualification activity;
- a delivery;
- a release; or
- another engineering purpose.

A Git commit can provide a technically reproducible repository state, but it
does not by itself define which engineering knowledge is authoritative or
why that state was selected.

ATON therefore requires an explicit semantic Baseline model.

## Goals

This RFC SHALL:

- define the semantics of a Baseline;
- define Baseline identity;
- define Baseline membership;
- preserve reproducibility;
- preserve immutability;
- distinguish Baselines from Engineering Versions;
- distinguish Baselines from Git revisions;
- distinguish Baselines from Releases;
- support traceability to the Engineering Knowledge Model; and
- remain independent of a particular persistence implementation.

## Non-Goals

This RFC does not define:

- release management processes;
- review processes;
- approval workflows;
- organizational responsibilities;
- Git branching strategies;
- Git tagging conventions;
- version numbering schemes;
- project-specific baseline selection procedures;
- configuration management processes; or
- user-interface behaviour.

These concerns may be defined by applicable process or governance models.

## Baseline

A Baseline SHALL represent an explicitly defined and reproducible selection
of Engineering Knowledge at a particular engineering state.

A Baseline SHALL be understood as a semantic state selection rather than
merely as a collection of engineering artifacts.

The meaning of a Baseline is determined by the engineering knowledge selected
and the versions and relationships applicable to that selection.

A Baseline MAY contain:

- Engineering Entities;
- Engineering Versions;
- Engineering Artifacts;
- Artifact Revisions;
- relations;
- metadata; or
- other engineering information required to reconstruct the selected state.

The exact membership model SHALL be defined by the applicable domain model.

A Baseline SHALL identify the engineering state that has been selected.

The physical representation used to store or retrieve that state SHALL NOT
itself define the semantic meaning of the Baseline.

## Baseline Identity

A Baseline SHALL have an explicit identity.

Baseline identity SHALL NOT be derived solely from:

- a Git commit hash;
- a Git tag;
- a repository path;
- a directory name;
- a timestamp; or
- a generated archive name.

A technical identifier MAY be associated with a Baseline for retrieval or
provenance.

Such a technical identifier SHALL remain distinguishable from the
canonical Baseline identity.

## Baseline Membership

A Baseline SHALL explicitly determine which Engineering Knowledge belongs to
the selected engineering state.

Baseline membership SHOULD be expressed through references to canonical
Engineering Knowledge objects, including Engineering Versions where
applicable.

Where an Engineering Entity has multiple versions, the Baseline SHALL
identify the Engineering Version applicable to the Baseline state.

A Baseline MAY additionally reference:

- Engineering Entities;
- Engineering Artifacts;
- Artifact Revisions; or
- other canonical domain objects

when such references are required to make the selected state explicit or
reproducible.

A Baseline SHALL NOT depend on an implicit interpretation of the latest
available version.

## Explicit Selection

Baseline membership SHALL be explicit or deterministically derivable from
authoritative information.

A Baseline SHALL NOT be defined merely as:

    "everything currently present in the repository"

unless the applicable Baseline definition explicitly establishes that
selection rule and the resulting state is reproducible.

The meaning of a Baseline SHALL remain stable after it has been established.

## Reproducibility

A Baseline SHALL be reproducible from authoritative Engineering Knowledge.

Given the same authoritative information and Baseline definition, a
conforming implementation SHOULD be able to reconstruct the same semantic
engineering state.

Reproducibility SHALL include sufficient information to determine:

- Baseline identity;
- Baseline membership;
- applicable Engineering Versions;
- applicable artifact state; and
- relevant semantic relations.

A technical repository snapshot MAY provide part or all of the information
required for reconstruction.

## Baseline Immutability

A formally established Baseline SHALL be immutable.

Its membership SHALL NOT be silently changed after establishment.

If a different engineering state is required, a new Baseline SHALL be
created.

A change to the metadata describing an established Baseline SHALL NOT change
the semantic membership or selected engineering state of that Baseline unless
such metadata is itself part of the Baseline's canonical state definition.

A technical implementation MAY store Baseline information in a mutable
database or repository, but the semantic model SHALL preserve the
immutability of established Baselines.

## Baseline and Engineering Versions

A Baseline selects Engineering Versions.

An Engineering Version represents the state of one Engineering Entity.

A Baseline represents a selected engineering state involving potentially
many Engineering Entities.

Therefore:

    Engineering Entity
            |
            +-- Engineering Version
                         |
                         +------+
                                |
                                ▼
                           Baseline
                                |
                         +------+------+
                         |      |      |
                         ▼      ▼      ▼
                      Version Version Version

A Baseline SHALL NOT replace the identity or history of its member
Engineering Versions.

## Baseline and Artifact Revisions

A Baseline MAY identify Artifact Revisions required to reconstruct the
selected engineering state.

Artifact Revisions and Engineering Versions SHALL remain distinct.

A physical artifact revision MAY be included in a Baseline without being
itself the semantic definition of the Baseline.

## Baseline and Relations

Relations SHALL be interpreted in the context of the Engineering Versions
selected by the Baseline.

A relation that exists in one version SHALL NOT automatically be assumed to
exist in another version.

A Baseline therefore represents not only a collection of entities but a
defined state of their applicable semantic relationships.

A Baseline SHALL NOT create, modify or delete canonical relations merely by
including or excluding engineering knowledge from the selected state.

The canonical Relation Model remains defined independently of Baseline
semantics.

## Baseline and Git

Git MAY provide a technical representation of a Baseline.

For example, a Git commit or tag MAY identify the repository state from which
a Baseline can be reconstructed.

However:

    Git Commit != Baseline

and:

    Git Tag != Baseline

The Git object provides technical provenance or retrieval information.

The Baseline provides the semantic definition of the selected engineering
state.

## Git Commit as Baseline Evidence

A Git commit MAY provide evidence that a particular physical repository
state existed.

A commit MAY therefore be associated with a Baseline.

Such an association SHALL NOT imply that every commit is a Baseline.

A Baseline MAY correspond to:

- one Git commit;
- multiple Git commits;
- a repository state reconstructed from several sources; or
- a persistence mechanism other than Git.

## Baseline and Release

A Baseline and a Release SHALL remain distinct concepts.

A Baseline identifies a reproducible engineering state.

A Release identifies an engineering state that has been explicitly released
according to the applicable release semantics.

A Release SHOULD reference a Baseline or equivalent reproducible state.

The relationship may therefore be represented as:

    Engineering Knowledge
            |
            ▼
         Baseline
            |
            ▼
         Release

A Baseline does not automatically constitute a Release.

A Release does not automatically create a new Baseline.

Release semantics are outside the scope of this RFC.

## Baseline Purpose

A Baseline MAY be established for different engineering purposes.

Examples include:

- architecture review;
- requirements verification;
- system verification;
- qualification;
- delivery;
- contractual reference;
- release preparation; or
- historical reference.

The purpose of a Baseline MAY be recorded as metadata.

The Baseline model SHALL NOT prescribe which purposes a project must use.

## Baseline Description

A Baseline SHOULD provide sufficient descriptive information to explain why
the selected engineering state was established.

Such information MAY include:

- purpose;
- creation information;
- responsible context;
- applicable project context;
- referenced versions;
- provenance;
- verification information; and
- external references.

The exact metadata model is governed by the canonical metadata specification.

## Baseline Provenance

A Baseline MAY contain provenance information identifying the sources from
which it was constructed.

Provenance MAY include:

- Git revisions;
- repository identifiers;
- artifact revisions;
- Engineering Versions;
- process instances;
- verification results;
- external configuration records; or
- other authoritative evidence.

Provenance SHALL support reproducibility without replacing Baseline
semantics.

## Baseline Verification

A conforming implementation MAY verify Baseline consistency.

Verification MAY detect:

- missing Baseline members;
- unknown Engineering Versions;
- invalid version references;
- inconsistent artifact revisions;
- invalid relation references;
- unavailable provenance;
- non-reproducible technical representations; or
- modifications to an established Baseline.

Verification SHALL distinguish between:

- semantic Baseline validity; and
- technical ability to reconstruct the physical representation.

A technically unavailable repository state does not automatically change the
semantic identity of the Baseline.

## Baseline Comparison

Two Baselines MAY be compared to determine their engineering differences.

Comparison MAY identify:

- added Engineering Entities;
- removed Engineering Entities;
- changed Engineering Versions;
- changed relations;
- changed metadata; and
- changed artifact representations.

Baseline comparison SHALL operate on canonical engineering semantics where
possible.

A raw Git diff MAY provide technical evidence but SHALL NOT be assumed to be
a complete semantic Baseline comparison.

## Baseline History

Baselines MAY form a historical sequence.

A later Baseline MAY be derived from an earlier Baseline.

Such derivation SHALL NOT modify the earlier Baseline.

If explicit relationships between Baselines are required, those relationships
SHALL be represented by the canonical relation or applicable Baseline model.

## Baseline Construction

A Baseline SHALL be constructed from authoritative engineering information.

The construction process MAY be automated.

Automation SHALL NOT change the semantic requirement that the resulting
Baseline represents an explicit and reproducible engineering state.

A tool MAY create a Baseline from:

- selected Engineering Versions;
- a validated repository state;
- a configuration selection;
- a project-defined selection rule; or
- another authoritative source.

The selection mechanism SHALL remain distinguishable from the resulting
Baseline semantics.

## Persistence Independence

The Baseline model SHALL remain independent of persistence technology.

Git is the canonical version-control system for the current ATON Foundation
implementation according to ADR-0003.

Nevertheless, the Engineering Knowledge Model SHALL be capable of representing
Baselines when engineering knowledge is persisted by another mechanism.

An alternative persistence implementation MAY use:

- another version-control system;
- a database;
- an artifact repository;
- an object store; or
- another suitable persistence mechanism.

The persistence mechanism SHALL provide sufficient information to reconstruct
the Baseline.

## Migration

Existing repository states MAY be migrated into the Baseline model.

A migration implementation MAY use Git history as technical evidence.

A migration SHALL NOT automatically interpret arbitrary historical Git
commits as Baselines.

Where historical Baseline boundaries are unknown, the implementation SHALL
preserve that uncertainty rather than invent historical Baselines.

New Baselines MAY be established once the required engineering state can be
identified reproducibly.

## Consequences

### Positive

- Baselines have explicit engineering semantics.
- Baselines remain independent of Git.
- Engineering Versions remain reusable across different Baselines.
- Historical states can be reproduced.
- Releases can reference stable engineering states.
- Alternative persistence implementations remain possible.
- Technical repository history remains useful as provenance.

### Negative

- Baseline membership must be explicitly maintained.
- Reproducibility requires sufficient authoritative information.
- Baseline construction may require additional tooling.
- Historical repositories may not contain enough information to reconstruct
  old Baselines reliably.

## Alternatives

### Treat every Git commit as a Baseline

Rejected.

Most Git commits represent intermediate technical changes rather than
deliberately selected engineering states.

### Treat Git tags as Baselines

Rejected.

A Git tag is a technical marker. Baseline semantics require an explicit
engineering state.

### Treat the repository state as implicitly authoritative

Rejected.

An implicit "current repository state" does not provide sufficient semantic
clarity for reproducible engineering reference states.

### Store only physical files in a Baseline

Rejected.

A Baseline must represent engineering semantics rather than merely a
collection of physical files.

### Make Baselines mutable

Rejected.

Changing an established Baseline would destroy reproducibility and
historical traceability.

## Open Questions

The following topics remain outside the normative scope of this RFC and may
be addressed by future specifications:

- Baseline numbering conventions;
- Baseline naming conventions;
- detailed Baseline metadata;
- Baseline approval workflows;
- Baseline creation process;
- automated Baseline selection;
- cross-repository Baselines;
- Baseline equivalence;
- Baseline dependency semantics;
- configuration management integration; and
- detailed Release semantics.

## Acceptance Criteria

A conforming implementation SHALL:

1. represent Baselines as explicit engineering states;
2. distinguish Baselines from Engineering Versions;
3. distinguish Baselines from Git revisions;
4. distinguish Baselines from Releases;
5. preserve Baseline immutability after establishment;
6. provide sufficient information for Baseline reproducibility;
7. explicitly identify Baseline membership;
8. preserve the semantic meaning of relations within a Baseline;
9. permit technical persistence mechanisms to provide Baseline provenance;
10. avoid treating arbitrary Git commits or tags as Baselines;
11. remain independent of a particular persistence implementation; and
12. preserve uncertainty when historical Baselines cannot be reconstructed
    reliably.

## References

- ADR-0012 Engineering Version and Baseline Semantics
- ADR-0011 Logical Engineering Knowledge Model and Physical Representations
- ADR-0003 Git as the Version Control System
- RFC-0012 Engineering Version Semantics
- RFC-0023 Traceability

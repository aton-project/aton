# RFC-0011 — Repository Layout

## Status

Draft

## Summary

This RFC defines the canonical repository layout for an ATON Foundation
repository.

The repository is a physical representation of the Engineering Knowledge
Model.

The repository layout SHALL provide a predictable organization for canonical
engineering representations while remaining distinct from the semantic
structure of the Engineering Knowledge Model.

Repository directories and file paths SHALL NOT define the semantic identity
or meaning of engineering concepts.

## Motivation

ATON uses Git and human-readable files as a primary physical representation
of engineering knowledge.

A predictable repository structure is therefore required so that:

- engineering knowledge can be located consistently;
- tools can discover canonical representations;
- loaders can identify artifact classes;
- contributors can understand the repository;
- Git can provide version-controlled persistence; and
- the Foundation can remain interoperable across implementations.

At the same time, the repository is only a physical representation.

The semantic Engineering Knowledge Model SHALL remain independent of
repository structure.

## Goals

This RFC SHALL:

- define the purpose of the ATON repository layout;
- define the canonical top-level organization of the Foundation repository;
- distinguish semantic organization from physical organization;
- provide predictable locations for engineering artifacts;
- support deterministic discovery by tooling;
- support human navigation of the repository;
- preserve compatibility with Git-based workflows;
- preserve the separation between logical engineering knowledge and physical
  representation; and
- provide a stable basis for loaders and repository tooling.

## Non Goals

This RFC does not define:

- the semantic Engineering Knowledge Model;
- Engineering Entity semantics;
- Engineering Artifact semantics;
- relation semantics;
- ontology semantics;
- Engineering Version semantics;
- Baseline semantics;
- a database schema;
- a user-interface navigation model;
- a mandatory Git branching strategy;
- project-specific directory structures outside the Foundation;
- semantic relationships based on directory containment; or
- a requirement that every physical representation use a Git repository.

## Proposal

### Repository

An ATON Repository SHALL be a physical persistence boundary containing
representations of engineering knowledge and supporting repository
information.

The repository MAY contain:

- canonical engineering representations;
- repository configuration;
- tooling;
- generated representations;
- documentation;
- validation configuration; and
- other implementation-specific resources.

Only the canonical engineering representations participate directly in the
canonical Engineering Knowledge Model.

### Repository Layout

The Foundation repository SHALL use a predictable top-level organization.

The canonical Foundation layout SHALL distinguish engineering knowledge from
implementation and tooling resources.

A conforming repository SHOULD provide structures equivalent to:

    engineering/
    foundation/
    tools/
    generated/

The exact physical organization MAY evolve as implementation requirements
change, provided that the semantic distinction remains preserved.

### Engineering Knowledge

The `engineering/` area SHALL contain engineering knowledge that is
represented according to the canonical ATON artifact model.

Engineering content MAY be organized physically into directories such as:

    engineering/
      requirements/
      specifications/
      architecture/
      verification/
      notes/
      processes/

These directories are physical organizational mechanisms.

They SHALL NOT by themselves define semantic relationships between the
contained engineering concepts.

### Foundation Specifications

The `foundation/` area SHALL contain the normative ATON Foundation itself.

It MAY contain structures such as:

    foundation/
      decisions/
      specifications/
      ontology/
      profiles/

The Foundation specifications SHALL define the normative semantics and rules
of ATON.

### Repository Tooling

Repository tooling MAY be stored separately from engineering knowledge.

For example:

    tools/

may contain:

- validation tools;
- loaders;
- migration tools;
- repository utilities;
- generation tools; or
- development scripts.

Tooling SHALL NOT become part of the Engineering Knowledge Model merely
because it is stored in the repository.

### Generated Representations

Generated content MAY be stored separately from canonical engineering
representations.

For example:

    generated/

may contain:

- generated documentation;
- rendered views;
- generated diagrams;
- indexes;
- reports; or
- other derived representations.

Generated representations SHALL NOT silently replace canonical engineering
knowledge.

### Artifact Directory Structure

A physical artifact MAY be represented by a directory containing multiple
files.

For example:

    RFC-0011/
      content.md
      metadata.yaml
      relations.yaml

Such a directory is a physical representation of an Engineering Artifact.

The directory itself SHALL NOT define the semantic identity of the artifact.

The semantic identity SHALL be provided by the canonical domain model and
applicable identity metadata.

### Canonical Artifact Files

Where the ATON artifact representation uses separated content, metadata and
relations, the repository MAY contain:

    content.md
    metadata.yaml
    relations.yaml

`content.md` SHALL contain canonical engineering content where applicable.

`metadata.yaml` SHALL contain canonical metadata where applicable.

`relations.yaml` SHALL contain serialized relations where applicable.

The physical separation of these files SHALL NOT change their semantic
ownership.

Loaders SHALL normalize these representations into the canonical domain
model.

### Markdown

Markdown SHALL be the canonical authoring and serialization format for
engineering content in accordance with ADR-0002.

Repository tooling MAY support additional formats for import, exchange or
generation.

Such formats SHALL NOT redefine the semantics of the Engineering Knowledge
Model.

### Metadata

Canonical metadata SHALL be represented according to the canonical metadata
model.

A metadata file is a physical representation of canonical metadata.

The file path, YAML structure or filename SHALL NOT itself define metadata
semantics.

### Relations

Relations SHALL be represented through the canonical relation serialization
defined by the applicable Foundation specifications.

The repository representation SHALL be treated as serialized data.

Kernel components SHALL operate on canonical Relation domain objects rather
than repository-specific serialization structures.

### Repository Paths

Repository paths SHALL be considered physical identifiers or access
mechanisms unless explicitly defined otherwise.

A path such as:

    foundation/specifications/rfc/RFC-0011/

does not itself define the semantic identity of RFC-0011.

The canonical identity is determined by the Engineering Knowledge Model.

A repository MAY therefore move an artifact to another physical location
without necessarily changing its semantic identity.

### Directory Containment

Directory containment SHALL NOT automatically constitute an Engineering
Relation.

For example:

    engineering/
      requirements/
        REQ-0001/
        REQ-0002/

does not imply any semantic relationship between `REQ-0001` and `REQ-0002`.

Likewise, placing an RFC inside the `rfc/` directory does not create a
semantic relationship between that RFC and other RFCs in the directory.

Semantic relationships SHALL be represented explicitly through canonical
relations or other applicable semantic mechanisms.

### Repository Discovery

Repository tooling MAY use directory structure and filenames to discover
physical representations.

Discovery SHALL be treated as a physical lookup operation.

After discovery, the representation SHALL be loaded and normalized into the
canonical domain model.

Repository discovery SHALL therefore remain distinct from semantic
interpretation.

### Loading

A repository loader SHALL translate physical repository representations into
canonical domain objects.

The loader MAY use:

- directory structure;
- filenames;
- file extensions;
- repository conventions; and
- serialization formats

to locate and interpret physical representations.

The resulting canonical domain objects SHALL NOT inherit semantic meaning
merely from these physical properties.

### Repository Validation

Repository validation MAY verify:

- required directories;
- required files;
- valid filenames;
- valid serialization;
- unique physical locations;
- artifact discoverability;
- metadata structure;
- relation serialization; and
- other repository constraints.

Repository validation SHALL remain distinguishable from semantic verification.

A repository may be physically well-formed while containing semantically
invalid engineering knowledge.

Conversely, semantic identity SHALL not be inferred solely from physical
repository structure.

### Repository Independence

The Engineering Knowledge Model SHALL remain independent of repository
layout.

An alternative persistence implementation MAY represent the same engineering
knowledge using:

- another directory structure;
- a database;
- an API;
- an artifact repository;
- an object store; or
- another persistence mechanism.

The semantic meaning of the engineering knowledge SHALL remain unchanged.

### Repository Portability

A repository SHOULD be portable across supported environments.

Repository layout SHALL avoid unnecessary dependencies on:

- operating-system-specific paths;
- absolute filesystem locations;
- proprietary tooling;
- local user directories; or
- environment-specific configuration.

Where environment-specific information is required, it SHOULD remain outside
the canonical engineering representation.

### Git

Git MAY be used as the version-control and persistence mechanism for the
repository.

Git provides technical history for the physical repository representation.

Git commits, branches and tags SHALL NOT automatically become semantic
engineering concepts.

Associations between Git objects and engineering concepts MAY be explicitly
represented according to applicable versioning and provenance semantics.

### Generated Content

Generated content SHOULD be distinguishable from canonical engineering
content.

Generated content MAY be recreated from canonical engineering knowledge and
therefore SHALL NOT automatically be considered authoritative.

A generated representation MAY be committed to Git for convenience,
publication or reproducibility.

Its presence in the repository SHALL NOT make it the semantic authority.

### Repository Configuration

Repository-specific configuration MAY be stored in the repository.

Configuration files MAY control:

- tooling;
- validation;
- generation;
- CI/CD;
- rendering;
- development environments; or
- other implementation concerns.

Such configuration SHALL NOT become engineering knowledge unless explicitly
represented as a canonical engineering artifact.

## Consequences

### Positive

- Repository structure becomes predictable.
- Tooling can discover artifacts consistently.
- Human contributors can navigate the physical repository easily.
- Canonical engineering knowledge remains independent of repository layout.
- Alternative persistence implementations remain possible.
- Generated content can be separated from authoritative knowledge.
- Git remains useful without becoming the semantic model.

### Negative

- Repository conventions must be maintained.
- Loaders require explicit knowledge of physical layout.
- Physical and semantic validation remain separate concerns.
- Moving artifacts may require repository tooling updates even when semantic
  identity remains unchanged.

## Alternatives

### Use the Repository Hierarchy as the Engineering Knowledge Model

Rejected.

Repository hierarchy is a physical organization mechanism and cannot express
all semantic relationships within engineering knowledge.

### Allow Directory Containment to Define Relations

Rejected.

Physical containment does not provide sufficient semantic information to
define engineering relationships.

### Store Every Engineering Concept as a Single File

Rejected.

Some engineering artifacts require multiple physical representations,
including separated content, metadata and relations.

### Allow Each Project to Define an Arbitrary Layout

Rejected as the Foundation default.

Some implementation freedom remains useful, but a predictable canonical
Foundation layout is required for interoperability and tooling.

### Make Git the Semantic Authority

Rejected.

Git describes the history of physical representations. It does not define
the semantics of engineering knowledge.

## Migration

Existing repositories SHOULD be migrated incrementally.

Migration SHOULD:

1. identify existing engineering artifacts;
2. distinguish canonical engineering content from tooling and generated
   content;
3. establish the canonical repository areas;
4. move physical representations into the appropriate locations;
5. preserve artifact identity;
6. preserve canonical metadata;
7. preserve canonical relations;
8. update physical references where required;
9. validate the resulting repository structure; and
10. verify the resulting canonical Engineering Knowledge Model.

Migration SHALL NOT create semantic relationships merely because artifacts are
placed into the same directory.

Repository moves SHALL NOT automatically create new Engineering Entities,
Engineering Artifacts or Engineering Versions.

## Open Questions

The following questions remain subject to further specification:

- Which repository directories SHALL be mandatory for all ATON repositories?
- Which directories are Foundation-specific?
- Which repository conventions should be normative versus recommended?
- How should external artifacts be represented?
- How should repository mounts or multiple repositories be handled?
- How should artifacts spanning multiple repositories be represented?
- How should repository-local configuration be distinguished from engineering
  knowledge?
- Which generated representations should be permitted in the canonical
  repository?
- How should repository migrations preserve physical provenance?
- Which repository discovery rules should be standardized for tooling?

## References

- ADR-0002 — Markdown as the Canonical Authoring Format
- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- RFC-0010 — Engineering Artifact Model
- RFC-0015 — Logical Engineering Knowledge and Physical Representations
- NOTE-0014 — Logical and Physical Artifact Representation
- NOTE-0017 — Logical Engineering Knowledge Graph and Physical Representations

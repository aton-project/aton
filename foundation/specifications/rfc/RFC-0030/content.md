# RFC-0030 Canonical Engineering Artifact Serialization

## Status

Proposed

## Abstract

This RFC defines the canonical persistence representation of ATON
Engineering Artifacts.

The canonical Engineering Knowledge Model is independent of persistence and
serialization.

An Engineering Artifact may contain engineering content, metadata and
relations. This RFC defines how these components are represented in the
canonical ATON repository representation.

The canonical representation uses separate files for:

- engineering content;
- artifact metadata; and
- engineering relations.

Markdown is the canonical serialization format for engineering content as
defined by ADR-0002.

YAML is used for the canonical serialization of structured metadata and
relations.

This RFC defines the persistence representation without redefining the
semantics of the underlying domain model.

## Motivation

ATON engineering artifacts are stored in a Git repository and must remain:

- human-readable;
- version-control friendly;
- implementation-independent;
- structurally deterministic;
- machine-processable; and
- compatible with different tooling implementations.

A canonical persistence representation prevents different implementations
from creating incompatible physical representations of the same logical
Engineering Artifact.

## Design Principle

The logical Engineering Knowledge Model SHALL remain independent of its
physical representation.

The canonical persistence representation SHALL provide a deterministic
mapping between physical artifact data and the canonical domain model.

The loader SHALL perform this mapping.

Kernel components SHALL operate on the canonical domain model and SHALL NOT
depend on persistence-specific file structures.

## Canonical Artifact Representation

A canonical Engineering Artifact SHALL be represented by an artifact
directory.

The canonical artifact representation consists of the following files:

- content.md
- metadata.yaml
- relations.yaml

The artifact directory name SHALL identify the artifact within the
persistence representation.

The canonical engineering identity SHALL be defined by the artifact metadata
and SHALL NOT depend solely on the directory name.

## Content

The `content.md` file SHALL contain the human-authored engineering content
of the artifact.

Markdown SHALL be the canonical serialization format for engineering content
in accordance with ADR-0002.

The content file SHALL NOT contain canonical artifact metadata that belongs in
`metadata.yaml`.

The content file SHALL NOT be required to contain canonical relation data that
belongs in `relations.yaml`.

Presentation-specific information MAY be generated from the canonical
content.

## Metadata

The `metadata.yaml` file SHALL contain the explicitly persisted metadata of
the Engineering Artifact.

Metadata SHALL use YAML as its canonical serialization format.

Metadata SHALL contain the artifact identity and other persisted properties
required by the applicable domain model.

Metadata SHALL NOT be used to duplicate information that is defined as
derived by another normative specification.

ATON SHALL prefer explicit persisted engineering metadata where the
information is part of the canonical engineering state.

Information available from Git, a database, an index or another persistence
mechanism SHALL NOT automatically become canonical engineering metadata.

A persistence implementation MAY expose derived information as additional
information, but such information SHALL remain distinguishable from
persisted canonical metadata.

## Relations

The `relations.yaml` file SHALL contain the explicitly persisted relations of
the Engineering Artifact.

Relation instances SHALL use the canonical structural relation model defined
by RFC-0025.

Semantic applicability of predicates SHALL be determined according to the
ontology and RFC-0029.

Relation instances SHALL NOT contain duplicated semantic predicate
constraints.

The persistence representation of a relation SHALL be normalized by the
loader into the canonical Relation domain model before being consumed by
kernel components.

## Relation Serialization

The canonical persistence representation SHALL use the mapping form for
named relation collections.

For example:

references:
  - RFC-0029

dependsOn:
  - RFC-0025

supersedes: []

supersededBy: []

relatedTo: []

Each relation collection SHALL contain target identifiers.

The mapping keys identify relation predicates or relation collections
defined by the applicable canonical relation model.

An implementation MAY accept legacy relation representations during
migration, but such representations SHALL NOT become additional canonical
domain representations.

The loader SHALL normalize supported legacy representations into the
canonical Relation domain model.

## Empty Relation Collections

An artifact with no relations MAY represent empty relation collections
explicitly.

The canonical representation SHALL use an empty YAML sequence for an empty
relation collection.

For example:

references: []

dependsOn: []

supersedes: []

supersededBy: []

relatedTo: []

An implementation SHALL interpret an explicitly empty collection as having no
relations of that predicate.

## Required Components

The canonical artifact representation SHALL contain:

- `metadata.yaml`;
- `content.md`; and
- `relations.yaml`.

The existence of all three files provides a deterministic artifact
representation even when one of the logical components is empty.

An artifact MAY contain additional physical files when permitted by the
applicable domain specification.

Additional files SHALL NOT alter the semantics of the canonical components.

## Optional Content

The content of an Engineering Artifact MAY be empty when the applicable
artifact type permits an artifact without authored engineering content.

The physical `content.md` representation SHALL nevertheless remain present
in the canonical artifact representation.

## Optional Metadata

Individual metadata properties MAY be optional according to the applicable
domain model.

The metadata file itself SHALL remain part of the canonical artifact
representation.

Required metadata properties SHALL be defined by the applicable artifact
type or schema.

## Optional Relations

An artifact MAY have no relations.

The canonical representation SHALL still contain `relations.yaml`.

Empty relation collections SHALL be represented explicitly.

## Identity

Artifact identity SHALL be represented explicitly in `metadata.yaml`.

The artifact identifier SHALL be unique within the applicable Engineering
Knowledge Model scope.

Identity SHALL NOT be derived from:

- file names;
- directory names;
- Git paths;
- document headings; or
- physical location.

A physical move or rename of an artifact SHALL therefore not inherently
change its engineering identity.

## Domain Type

The semantic type of an artifact SHALL be represented explicitly by its
canonical metadata or applicable domain model.

A Markdown heading SHALL NOT be used as the authoritative semantic type of an
artifact.

The physical directory structure SHALL NOT define the semantic type.

## Canonical Serialization and Domain Model

The canonical persistence representation is a serialization of the logical
Engineering Knowledge Model.

It SHALL NOT be interpreted as the domain model itself.

The following distinction SHALL therefore be maintained:

Logical model:

Engineering Entity
Engineering Artifact
Metadata
Relation

Physical representation:

artifact directory
content.md
metadata.yaml
relations.yaml

A loader SHALL convert the physical representation into canonical domain
objects.

## Loader Boundary

The loader SHALL act as the boundary between persistence and the kernel.

The loader SHALL:

- locate artifact representations;
- parse `metadata.yaml`;
- parse `relations.yaml`;
- load `content.md`;
- validate the physical representation;
- normalize supported serialization variants;
- construct canonical domain objects.

Kernel components SHALL NOT directly parse artifact files.

The renderer, verifier and reasoning components SHALL operate exclusively on
canonical domain objects.

## Determinism

The canonical persistence representation SHALL be deterministic.

Equivalent engineering artifacts SHALL use the same canonical representation
when serialized by a conforming implementation.

Serialization SHALL NOT depend on:

- operating system;
- local path conventions;
- user interface;
- editor;
- database engine; or
- implementation-specific object ordering.

## Ordering

The semantic meaning of relation collections SHALL NOT depend on YAML sequence
ordering unless the applicable predicate specification explicitly defines
ordering semantics.

Implementations SHOULD preserve stable ordering when serializing relation
collections to minimize unnecessary Git changes.

## Additional Files

An artifact MAY contain additional files when required by an applicable
domain specification.

Examples include:

- diagrams;
- generated representations;
- attachments;
- test evidence; or
- domain-specific supporting data.

Additional files SHALL NOT silently become part of the canonical semantic
model.

Their semantics SHALL be explicitly defined by the applicable specification.

## Generated Representations

Rendered or generated representations MAY be produced from canonical
artifact data.

Generated representations SHALL NOT replace the canonical persistence
representation unless explicitly defined by a future normative
specification.

Examples include:

- HTML;
- PDF;
- diagrams;
- graph representations;
- API representations.

## Exchange Formats

External exchange formats MAY be generated from the canonical domain model.

Examples include:

- JSON;
- ReqIF;
- XML;
- API-specific representations.

Exchange formats SHALL NOT redefine the canonical ATON domain model.

Importers SHALL normalize external representations into the canonical domain
model before the data is used by kernel components.

## Version Control

The canonical persistence representation SHALL be suitable for Git version
control.

Changes to engineering content, metadata or relations SHOULD remain
independently visible in version history.

A change to one component SHALL NOT require modification of unrelated
components.

Git history SHALL remain a technical representation of repository evolution.
Engineering version semantics are defined separately by the applicable
architecture decisions.

## Validation

The physical artifact representation SHALL be structurally verifiable.

Validation MAY include:

- required file presence;
- valid YAML;
- valid Markdown;
- valid artifact identity;
- valid metadata;
- valid relation serialization;
- duplicate identity detection;
- relation target resolution.

Semantic relation validation SHALL follow the canonical ontology and
predicate constraints.

Physical validation SHALL remain separate from semantic validation.

## Schema

Machine-readable schemas MAY be provided for canonical artifact components.

Such schemas SHALL implement the normative rules defined by this RFC and the
applicable domain specifications.

A schema SHALL NOT silently introduce semantics that are not defined by the
normative Engineering Knowledge Model.

The canonical schemas are:

- `artifact.schema.yaml`
- `entity.schema.yaml`
- `metadata.schema.yaml`
- `relation.schema.yaml`

The schemas SHALL remain implementation aids for deterministic validation
while the normative semantics remain defined by the applicable Foundation
specifications and RFCs.

## Migration

ATON MAY support legacy physical representations during migration.

A conforming loader MAY accept legacy representations and normalize them into
the canonical domain model.

Migration SHALL NOT require kernel components to support legacy persistence
formats.

Once migration is complete, legacy representations MAY be removed from the
loader.

Removal of a legacy representation SHALL NOT change the canonical domain
model.

## Compatibility

The canonical serialization defined by this RFC is compatible with:

- ADR-0002 Markdown authoring;
- ADR-0005 separation of content, metadata and relations;
- ADR-0010 canonical metadata semantics;
- ADR-0011 logical and physical model separation;
- ADR-0013 entity and artifact semantics;
- ADR-0014 canonical semantic relations;
- RFC-0025 canonical Relation domain model; and
- RFC-0029 semantic relation constraints.

This RFC does not redefine any of those domain semantics.

## Consequences

### Positive

- Engineering artifacts have one canonical persistence structure.
- Content, metadata and relations remain independently manageable.
- The kernel remains independent of persistence.
- Git provides useful and readable change history.
- Alternative persistence and exchange formats remain possible.
- Validation can operate deterministically.
- Future artifact components can be introduced without changing the existing
  semantic model.

### Negative

- Every canonical artifact contains multiple files.
- Implementations require a loader boundary.
- Additional artifact components require explicit specification.
- Legacy persistence formats may need migration support.

## Out of Scope

This RFC does not define:

- the semantics of individual metadata properties;
- the semantics of relation predicates;
- ontology concepts;
- engineering process semantics;
- Markdown syntax extensions;
- versioning semantics;
- user interface behaviour;
- graph traversal semantics; or
- external exchange format schemas.

Those concerns are defined by their respective specifications.

## Acceptance Criteria

A conforming implementation SHALL:

1. represent canonical artifacts using the defined physical structure;
2. persist engineering content in `content.md`;
3. persist canonical artifact metadata in `metadata.yaml`;
4. persist canonical relations in `relations.yaml`;
5. preserve explicit artifact identity;
6. normalize persistence data into canonical domain objects;
7. keep kernel components independent of persistence structure;
8. support empty relation collections;
9. preserve the distinction between persisted and derived information;
10. permit additional representations without changing canonical semantics;
11. support deterministic structural validation; and
12. preserve compatibility with the canonical Relation model.

## References

- ADR-0002 Markdown as the Canonical Authoring Format
- ADR-0005 Separation of Content, Metadata and Relations
- ADR-0010 Canonical Metadata Domain Model
- ADR-0011 Logical Engineering Knowledge Model and Physical Representations
- ADR-0013 Entity and Artifact Semantics
- ADR-0014 Canonical Semantic Relation Model
- RFC-0025 Canonical Relation Model
- RFC-0029 Canonical Semantic Relation Constraint Model
- NOTE-0004 Canonical Serialization of Engineering Artifacts

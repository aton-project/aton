# RFC-0010 — Engineering Artifact Model

## Status

Draft

## Summary

This RFC defines the semantic model of Engineering Artifacts within the ATON
Engineering Knowledge Model.

An Engineering Artifact is a logical engineering representation that provides
or carries engineering information.

An Engineering Artifact is distinct from an Engineering Entity and from the
physical representation used to persist or exchange it.

An Engineering Entity represents an engineering concept.

An Engineering Artifact represents an engineering representation associated
with engineering knowledge.

A physical representation such as a Markdown file, YAML document, database
record or API resource may represent an Engineering Artifact, but the
physical representation is not itself the semantic definition of the
artifact.

Artifact revisions represent the evolution of an artifact representation and
remain distinct from Engineering Versions.

## Motivation

Engineering knowledge is represented through different kinds of engineering
objects and their representations.

A Requirement is an engineering concept.
A specification document may represent information about that concept.
A Markdown file may physically represent the specification artifact.

These concepts must not be conflated.

Without an explicit distinction between Engineering Entities, Engineering
Artifacts and physical representations, implementations may incorrectly:

- treat files as engineering concepts;
- assign semantic identity to repository paths;
- confuse artifact revision with engineering version;
- assume one artifact corresponds to exactly one entity;
- prevent multiple representations of the same engineering knowledge; or
- couple the Engineering Knowledge Model to a particular persistence format.

ATON therefore requires an explicit semantic model for Engineering Artifacts.

## Goals

This RFC SHALL:

- define the semantic meaning of an Engineering Artifact;
- distinguish Engineering Artifacts from Engineering Entities;
- distinguish Engineering Artifacts from physical representations;
- define the relationship between artifacts and engineering knowledge;
- permit multiple physical representations of an artifact;
- permit an artifact to represent information about multiple engineering
  concepts where applicable;
- distinguish Artifact Revisions from Engineering Versions;
- preserve artifact identity independently of physical file paths;
- support traceability involving artifacts;
- remain independent of persistence and serialization technology; and
- provide the semantic foundation for artifact serialization and physical
  representation.

## Non Goals

This RFC does not define:

- the complete Engineering Entity model;
- the canonical metadata model;
- the canonical Relation domain representation;
- physical repository layout;
- a specific serialization format;
- a specific document format;
- Git workflow conventions;
- the complete Engineering Version model;
- the complete Baseline model;
- rendering or user-interface behaviour;
- artifact-specific ontology definitions; or
- project-specific artifact classification.

The logical and physical representation boundary is defined more generally
by RFC-0015.

Engineering Version, Artifact Revision, Baseline and Release semantics are
defined separately.

## Proposal

### Engineering Artifact

An Engineering Artifact SHALL represent a logical engineering representation
that carries, describes or organizes engineering knowledge.

An artifact has semantic identity independent of the physical mechanism used
to represent it.

Examples MAY include:

- a requirements specification;
- an architecture specification;
- a test specification;
- a verification record;
- an engineering decision record;
- a model;
- a dataset;
- an engineering report; or
- another artifact type defined by the applicable ontology.

An artifact SHALL NOT be defined solely by its file name, repository path or
serialization format.

### Engineering Entity

An Engineering Entity SHALL represent an engineering concept within the
Engineering Knowledge Model.

An Engineering Artifact and an Engineering Entity SHALL therefore remain
distinct concepts.

An artifact MAY represent information about one or more engineering
entities.

An engineering entity MAY be represented through one or more artifacts.

The applicable ontology determines the semantic relationship between an
entity and an artifact.

### Artifact and Entity Representation

An artifact MAY:

- represent an Engineering Entity;
- describe multiple Engineering Entities;
- contain information about multiple Engineering Entities;
- provide evidence concerning an Engineering Entity; or
- organize engineering information without representing a single entity.

The existence of an artifact SHALL NOT automatically imply the existence of
a corresponding Engineering Entity.

Likewise, an Engineering Entity SHALL NOT require exactly one artifact.

### Artifact Identity

An Engineering Artifact SHALL have a semantic identity independent of its
physical representation.

Artifact identity SHALL NOT depend solely on:

- file name;
- file path;
- repository location;
- database record location;
- URL;
- serialization format; or
- rendering location.

Moving an artifact between repositories or changing its physical
representation SHALL NOT inherently create a new Engineering Artifact.

A new artifact identity MAY be established when the engineering meaning of
the artifact itself changes such that it is no longer considered the same
artifact.

### Artifact Content

An artifact MAY contain or provide:

- engineering information;
- references to engineering entities;
- metadata;
- relations;
- structured data;
- unstructured content;
- models;
- evidence; or
- other information defined by its artifact type.

The semantic interpretation of such information SHALL be determined by the
applicable Engineering Knowledge Model and ontology.

### Artifact Type

An artifact MAY have an artifact type.

The artifact type SHALL define the semantic classification of the artifact.

Examples MAY include:

- specification;
- requirement document;
- architecture description;
- test specification;
- verification evidence;
- decision record;
- model; or
- other artifact types defined by the applicable ontology.

Artifact type semantics SHALL remain independent of physical serialization.

### Artifact Revision

An Artifact Revision SHALL represent a revision of an Engineering Artifact
or of its physical representation.

An Artifact Revision is distinct from an Engineering Version.

An artifact MAY undergo physical revisions without creating a new semantic
Engineering Version.

Conversely, a change to an Engineering Version MAY require changes to
multiple artifacts.

Artifact Revision semantics SHALL therefore not be assumed to have a
one-to-one relationship with Engineering Version semantics.

### Artifact Revision and Physical Representation

A physical representation MAY change while the semantic artifact remains the
same.

For example, an artifact may be:

1. represented as Markdown;
2. converted to another exchange format; or
3. stored in a database.

Such changes MAY constitute physical or artifact revisions without
necessarily changing the semantic identity of the Engineering Artifact.

The applicable revision semantics determine whether a particular change
constitutes a new Artifact Revision.

### Artifact and Engineering Version

Engineering Versions represent semantic engineering states.

Artifact Revisions represent revisions of artifact representations.

These concepts SHALL remain distinct.

A change to an artifact MAY contribute to a new Engineering Version when the
engineering meaning represented by the change is semantically relevant.

A physical artifact change that does not affect the semantic engineering
state SHALL NOT automatically create a new Engineering Version.

Engineering Version semantics are defined separately by RFC-0012.

### Artifact and Baseline

A Baseline MAY include Engineering Artifacts and Artifact Revisions required
to reproduce a selected engineering state.

The inclusion of an artifact in a Baseline SHALL NOT redefine the semantic
identity of the artifact.

Baseline semantics are defined separately.

### Artifact and Release

A Release MAY include or reference Engineering Artifacts required to
represent the released engineering state.

A Release SHALL NOT redefine the semantic identity of its artifacts.

Release semantics are defined separately.

### Artifact and Relations

Engineering Artifacts MAY participate in canonical Engineering Relations.

Relations MAY connect:

- artifacts to artifacts;
- artifacts to entities;
- entities to artifacts; or
- other combinations permitted by the applicable ontology.

The semantic validity of a relation SHALL be determined by the applicable
predicate and semantic constraints.

An artifact's physical location SHALL NOT itself create an Engineering
Relation.

### Artifact and Traceability

Artifacts MAY provide important traceability information.

Traceability MAY traverse relationships involving artifacts, entities,
versions, baselines or other engineering concepts.

A physical hyperlink between artifacts SHALL NOT automatically constitute
semantic traceability.

Canonical traceability is defined separately by RFC-0023.

### Multiple Physical Representations

An Engineering Artifact MAY have multiple physical representations.

For example, the same artifact MAY be represented through:

- a Markdown file;
- a YAML representation;
- a database record;
- an API resource;
- an exchange format; or
- another supported representation.

Multiple physical representations SHALL NOT automatically create multiple
Engineering Artifacts.

The relationship between logical artifacts and their physical
representations is defined generally by RFC-0015.

### Physical Representation

A Physical Representation SHALL be a persistence, exchange or presentation
representation of an Engineering Artifact or other canonical engineering
knowledge.

Examples include:

- files;
- Git objects;
- database records;
- API resources;
- generated documents;
- rendered views; or
- exchange documents.

A Physical Representation SHALL NOT define the semantic identity of the
Engineering Artifact.

### Representation Consistency

Where multiple physical representations describe the same Engineering
Artifact, implementations SHOULD ensure that they remain consistent with
the authoritative canonical engineering information.

A conflict between representations SHALL NOT silently redefine the canonical
artifact.

The applicable loading, verification and governance mechanisms SHALL
determine how such conflicts are handled.

### Artifact Metadata

Metadata describing an Engineering Artifact SHALL remain distinguishable from
metadata describing:

- an Engineering Entity;
- an Artifact Revision;
- a Physical Representation; or
- another engineering concept.

Metadata ownership is determined by the logical concept being described.

Canonical metadata semantics are defined by ADR-0010 and RFC-0003.

### Artifact Serialization

Artifact serialization defines how an Engineering Artifact is physically
represented for persistence or exchange.

Serialization SHALL NOT redefine the semantic artifact model.

The canonical serialization of engineering artifacts is specified separately
by RFC-0030 and the ATON Markdown Profile by RFC-0031 where applicable.

### Artifact and Git

Git MAY provide physical storage and revision history for Engineering
Artifacts.

A Git commit SHALL represent a technical repository revision and SHALL NOT
automatically constitute an Artifact Revision or Engineering Version.

A Git revision MAY provide provenance for an Artifact Revision.

Git semantics remain separate from the semantic artifact model.

### Artifact Portability

An Engineering Artifact SHOULD remain portable between supported persistence
implementations.

Moving an artifact between persistence mechanisms SHALL NOT inherently change
its semantic identity.

An implementation MAY create new physical representations during such a
migration.

### Artifact Verification

Implementations MAY verify artifact integrity.

Verification MAY identify:

- missing artifact identity;
- invalid artifact type;
- invalid metadata;
- invalid relations;
- unresolved references;
- inconsistent physical representations;
- invalid revision relationships; or
- other violations defined by applicable specifications.

Artifact verification SHALL operate on canonical artifact semantics rather
than relying solely on physical file structure.

## Consequences

### Positive

- Engineering concepts and their representations remain clearly separated.
- Files are no longer confused with engineering artifacts.
- Multiple representations of the same artifact are possible.
- Artifact revisions remain distinct from Engineering Versions.
- Artifacts can participate in canonical traceability.
- Persistence mechanisms can evolve independently of artifact semantics.
- Git remains useful for provenance without defining artifact semantics.

### Negative

- Implementations must maintain explicit artifact identity.
- Translation between logical artifacts and physical representations requires
  explicit boundaries.
- Multiple representations require consistency management.
- Artifact Revision and Engineering Version semantics require separate
  modeling.

## Alternatives

### Treat files as Engineering Artifacts

Rejected.

Files are physical representations and do not provide a
persistence-independent semantic model.

### Treat Engineering Artifacts and Engineering Entities as identical

Rejected.

An artifact may represent multiple entities, and an entity may be represented
by multiple artifacts.

### Require exactly one artifact per Engineering Entity

Rejected.

Engineering knowledge may require multiple artifacts to represent an entity
and individual artifacts may contain information about multiple entities.

### Treat every artifact revision as an Engineering Version

Rejected.

Physical artifact changes do not necessarily change the semantic engineering
state.

### Derive artifact identity from repository paths

Rejected.

Repository paths are physical representation details and may change without
changing engineering identity.

## Migration

Existing physical engineering files and documents SHALL be classified
according to their semantic role.

Migration SHOULD:

1. identify existing artifacts;
2. distinguish artifacts from Engineering Entities;
3. establish stable artifact identity where required;
4. identify physical representations of each artifact;
5. identify applicable artifact types;
6. identify Artifact Revisions where historical information exists;
7. preserve existing semantic relationships;
8. distinguish physical revisions from Engineering Versions; and
9. normalize physical representations into the canonical domain model.

Migration SHALL NOT assume that every file represents exactly one Engineering
Entity.

Migration SHALL NOT assume that every file revision constitutes a new
Engineering Version.

Existing repository structure MAY provide migration evidence but SHALL NOT
define artifact semantics.

## Open Questions

The following questions remain subject to further specification:

- Which artifact types belong to the ATON Foundation ontology?
- Which artifact types are required to have persistent identity?
- How should artifact identity be established during migration?
- How should Artifact Revisions be identified?
- Which changes constitute a new Artifact Revision?
- How should artifact branching and merging be represented?
- How should artifact provenance be modeled?
- How should multiple physical representations be synchronized?
- Which artifact properties are mandatory for individual artifact types?
- How should artifact lifecycle semantics interact with Engineering Versions?
- How should generated artifacts be distinguished from authoritative
  artifacts?

These questions MAY be addressed by subsequent artifact, serialization,
ontology and versioning specifications.

## References

- ADR-0004 — Artifact-Based Knowledge Organization
- ADR-0005 — Separation of Content, Metadata and Relations
- ADR-0006 — Engineering Knowledge Graph
- ADR-0010 — Canonical Metadata Domain Model
- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- RFC-0003 — Metadata Model
- RFC-0012 — Engineering Version Semantics
- RFC-0015 — Logical Engineering Knowledge and Physical Representations
- RFC-0023 — Engineering Traceability
- RFC-0030 — Canonical Engineering Artifact Serialization
- RFC-0031 — ATON Markdown Profile
- NOTE-0008 — Entity and Artifact Semantics
- NOTE-0014 — Logical and Physical Artifact Representation
- NOTE-0017 — Logical Engineering Knowledge Graph and Physical Representations

# RFC-0015 — Logical Engineering Knowledge and Physical Representations

## Status

Proposed

## Summary

This RFC defines the canonical relationship between the logical Engineering
Knowledge Model and its physical representations.

The Engineering Knowledge Model defines the semantic meaning of engineering
knowledge.

A physical representation is a representation of that knowledge for purposes
such as persistence, exchange, transport, rendering or interaction.

Physical representations SHALL NOT define or redefine the semantics of the
logical Engineering Knowledge Model.

The canonical domain model provides the architectural boundary between logical
engineering knowledge and physical representations.

## Motivation

ATON represents engineering knowledge through entities, artifacts, metadata,
relations, predicates, versions and other semantic concepts.

These concepts have meaning independently of how they are stored or presented.

The same engineering knowledge MAY be represented through:

- Markdown files;
- YAML metadata;
- Git repositories;
- databases;
- APIs;
- exchange formats;
- generated documents;
- rendered views;
- or other physical representations.

Without a clear distinction between logical knowledge and physical
representation, implementations may accidentally make repository structures,
file formats or rendering technologies part of the semantic model.

ATON therefore requires an explicit representation boundary.

## Scope

This RFC defines:

- logical engineering knowledge;
- physical representations;
- canonical domain representations;
- representation boundaries;
- loading and normalization;
- export and rendering;
- representation identity;
- multiple representations of the same knowledge;
- representation consistency;
- representation independence.

This RFC does not define:

- a specific persistence technology;
- a specific file format;
- a specific repository layout;
- a specific database;
- a specific API;
- a specific renderer;
- a specific user interface;
- or a project-specific workflow.

## Logical Engineering Knowledge

The logical Engineering Knowledge Model SHALL define the semantic meaning of
engineering knowledge.

The logical model MAY contain concepts such as:

- Engineering Entities;
- Engineering Artifacts;
- Metadata;
- Relations;
- Predicates;
- Ontology Concepts;
- Engineering Versions;
- Baselines;
- Releases;
- Engineering Processes;
- Process Instances;
- Views;
- and other concepts defined by the applicable Foundation specifications.

The logical model SHALL remain independent of the mechanism used to persist,
transport or present it.

The semantic identity of an engineering concept SHALL therefore not depend on:

- a file name;
- a repository path;
- a directory;
- a database row;
- a URL;
- a Markdown heading;
- or another physical location.

## Canonical Domain Representation

ATON SHALL provide canonical domain representations for engineering concepts
handled by the kernel.

A canonical domain representation SHALL represent the semantic model required
by kernel components.

Kernel components SHALL operate on canonical domain representations rather
than persistence-specific structures.

A canonical domain representation SHALL therefore provide the boundary between
the logical Engineering Knowledge Model and physical representations.

## Physical Representation

A Physical Representation SHALL be a concrete representation of engineering
knowledge for a particular technical purpose.

Physical representations MAY include:

- persistent files;
- repository structures;
- database records;
- API resources;
- exchange documents;
- generated documentation;
- rendered views;
- cached data;
- or other technical representations.

A physical representation MAY contain information required by its technical
purpose that is not part of the canonical semantic model.

Such information SHALL remain distinguishable from canonical engineering
semantics.

A physical representation SHALL NOT silently introduce semantic information
that is absent from the applicable logical model.

## Representation Boundary

ATON SHALL maintain an explicit boundary between physical representations and
the canonical domain model.

For imported or persisted representations, a loader or corresponding
translation component SHALL transform the physical representation into the
canonical domain representation.

Conceptually:

    Physical Representation
             |
             v
        Loader / Adapter
             |
             v
    Canonical Domain Model
             |
             v
    Engineering Knowledge Model

The kernel SHALL operate on the canonical domain representation.

Kernel components MUST NOT depend on the internal serialization structure of a
physical representation.

## Loading and Normalization

A loader SHALL be responsible for translating supported physical
representations into canonical domain representations.

A loader MAY:

- parse serialized data;
- resolve identifiers;
- normalize alternative serialization forms;
- validate structural constraints;
- resolve relationships;
- construct canonical domain objects;
- and provide provenance information.

Normalization SHALL preserve the semantics of the engineering knowledge.

Different physical representations of equivalent engineering knowledge SHALL
normalize to semantically equivalent canonical representations.

## Export and Rendering

Physical representations MAY also be generated from the canonical domain
model.

Exporters and renderers SHALL derive their semantic content from canonical
domain representations.

Conceptually:

    Engineering Knowledge Model
             |
             v
    Canonical Domain Model
             |
             v
       Exporter / Renderer
             |
             v
    Physical Representation

A renderer SHALL NOT become the semantic authority for the engineering
knowledge it presents.

Generated documentation, diagrams, web pages and other views are therefore
representations of engineering knowledge rather than definitions of that
knowledge.

## Multiple Representations

Multiple physical representations MAY represent the same logical engineering
knowledge.

For example, the same engineering concept MAY be represented simultaneously
as:

- a Markdown artifact;
- a YAML metadata representation;
- an API resource;
- a database record;
- and a rendered documentation page.

These representations SHALL NOT constitute independent semantic definitions.

The canonical Engineering Knowledge Model remains the semantic authority.

## Representation Identity

The identity of a physical representation SHALL remain distinct from the
identity of the engineering knowledge it represents.

A change to a physical representation SHALL NOT automatically imply a change
to the semantic engineering concept.

Conversely, a semantic change MAY require changes to multiple physical
representations.

Physical identity MAY depend on implementation-specific properties such as:

- path;
- URI;
- database identifier;
- storage location;
- or representation format.

Such identifiers SHALL NOT replace canonical engineering identity.

## Representation-Specific Information

A physical representation MAY contain information required only by that
representation.

Examples include:

- rendering directives;
- cache information;
- database indexing information;
- transport metadata;
- formatting information;
- repository-specific information.

Representation-specific information SHALL NOT automatically become part of the
logical Engineering Knowledge Model.

If such information has engineering meaning, it SHALL be represented through
the applicable canonical engineering concept or property.

## Consistency

A physical representation intended to represent canonical engineering
knowledge SHALL be consistent with the applicable canonical domain model.

An implementation MAY detect inconsistencies between physical representations
and canonical engineering knowledge.

Examples include:

- missing required metadata;
- invalid identifiers;
- conflicting relation information;
- stale generated output;
- unresolved references;
- or incompatible serialized structures.

Consistency verification SHALL operate according to the applicable canonical
semantic and structural specifications.

## Provenance

A physical representation MAY provide provenance information about the
engineering knowledge it represents.

Provenance MAY identify:

- source representations;
- generating tools;
- generating revisions;
- timestamps;
- transformations;
- imports;
- exports;
- or other technical history.

Provenance information SHALL remain distinguishable from the semantic identity
of the engineering knowledge.

Technical provenance SHALL NOT redefine engineering semantics.

## Canonical Serialization and Representation

ATON MAY define canonical serialization formats for particular classes of
physical representation.

A canonical serialization format defines how a semantic model is represented
physically.

It SHALL NOT change the semantic meaning of that model.

For example, a canonical Markdown profile MAY define how engineering content is
serialized, while the Engineering Knowledge Model remains independent of
Markdown.

Likewise, canonical YAML schemas MAY define metadata or relation
serialization without making YAML itself part of the engineering semantics.

## Repository Representation

The ATON Foundation currently uses a repository-based physical
representation.

This representation MAY be normative for the Foundation where explicitly
specified.

However, repository paths, directory structures and file organization SHALL
remain physical representation concerns unless a Foundation specification
explicitly assigns semantic meaning to them.

A repository location SHALL NOT become the semantic identity of an engineering
concept merely because the concept is stored there.

## Git Representation

Git MAY provide:

- persistence;
- technical history;
- provenance;
- version comparison;
- reproducibility;
- and other implementation capabilities.

Git revisions SHALL remain technical representations unless explicitly mapped
to canonical engineering concepts.

Engineering version, baseline and release semantics remain defined by their
respective canonical specifications.

## Exchange Representations

ATON MAY import or export engineering knowledge through external formats.

Examples include:

- JSON;
- XML;
- ReqIF;
- CSV;
- API representations;
- or other engineering exchange formats.

An exchange format SHALL be treated as a physical representation.

Import and export mechanisms SHALL map exchange representations to and from
the canonical domain model.

External format semantics SHALL NOT automatically redefine ATON semantics.

## Derived Representations

An implementation MAY generate derived physical representations from canonical
engineering knowledge.

Examples include:

- documentation;
- diagrams;
- indexes;
- navigation structures;
- search indexes;
- reports;
- traceability matrices;
- or other generated views.

Derived representations SHALL remain distinguishable from authoritative
engineering knowledge.

A derived representation MAY be regenerated without changing the semantic
identity of the engineering knowledge from which it was derived.

## Persistence Independence

ATON SHALL remain independent of any particular persistence implementation.

The Engineering Knowledge Model SHALL be representable through different
physical persistence mechanisms without requiring a competing semantic model
for each mechanism.

An implementation MAY therefore replace or supplement:

- Git;
- the filesystem;
- databases;
- APIs;
- or other persistence mechanisms

without redefining the Engineering Knowledge Model.

## Implementation Boundary

The following architectural boundary SHALL be preserved:

    Physical Representation
            |
            | translation
            v
    Canonical Domain Model
            |
            | semantic processing
            v
    ATON Kernel
            |
            | translation
            v
    Physical Representation

The kernel SHALL NOT bypass this boundary by directly interpreting
persistence-specific structures.

Exceptions MAY exist for infrastructure concerns, but such exceptions SHALL
NOT redefine the semantic domain model.

## Relationship to Other Specifications

ADR-0011 establishes the architectural separation between the logical
Engineering Knowledge Model and physical representations.

ADR-0002 establishes Markdown as the canonical authoring format for engineering
content.

ADR-0008 establishes canonical domain models as an architectural principle.

ADR-0012 defines engineering version, baseline and release semantics.

ADR-0018 defines semantic navigation.

RFC-0012 defines Engineering Version Semantics.

RFC-0013 defines Engineering Baseline Semantics.

RFC-0014 defines Engineering Knowledge Navigation.

RFC-0025 defines the canonical Relation domain model.

RFC-0029 defines semantic relation constraints.

RFC-0030 defines canonical engineering artifact serialization.

RFC-0031 defines the ATON Markdown Profile.

This RFC defines the architectural relationship between the logical model and
the physical representations used by those specifications.

## Alternatives Considered

### Treat Physical Files as the Engineering Knowledge Model

Rejected.

Files are physical representations and may vary between implementations.

### Treat the Repository Structure as Semantic

Rejected.

Repository structure is a storage concern and must not determine engineering
semantics.

### Define a Separate Semantic Model for Each Representation

Rejected.

Multiple competing semantic models would make interoperability and
consistency difficult.

### Allow Kernel Components to Interpret Serialization Directly

Rejected.

This couples domain logic to persistence and makes alternative
representations unnecessarily difficult.

### Make One Physical Representation Universally Mandatory

Rejected.

ATON defines semantic engineering knowledge independently of physical
representation.

Individual Foundation specifications MAY define canonical representations
where required for interoperability or persistence, but those representations
remain representations of the logical model.

## Migration

Existing physical representations MAY continue to be used.

Implementations SHALL progressively establish explicit translation boundaries
between physical representations and the canonical domain model.

Existing loaders MAY initially support multiple serialization forms.

Legacy representations MAY be retained during migration where necessary.

Migration SHALL preserve engineering identity and semantic meaning.

A migration between physical representations SHALL NOT by itself create new
engineering identities or semantic concepts.

## Acceptance Criteria

A conforming implementation SHALL satisfy at least the following:

1. The logical Engineering Knowledge Model is independent of physical storage.
2. Kernel components operate on canonical domain representations.
3. Physical representations are translated at explicit architectural
   boundaries.
4. Multiple physical representations may represent the same engineering
   knowledge.
5. Physical representation identity remains distinct from engineering identity.
6. Representation-specific information remains distinguishable from canonical
   engineering semantics.
7. Generated representations derive their semantic content from the canonical
   domain model.
8. Git and repository structures do not redefine engineering semantics.
9. Exchange formats can be mapped through translation boundaries.
10. Physical representation changes do not automatically imply engineering
    identity changes.
11. Canonical serialization formats do not redefine logical semantics.
12. Project-specific workflows are not prescribed by the representation model.

## References

- ADR-0002 — Markdown as the Canonical Authoring Format
- ADR-0008 — Canonical Domain Models
- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- ADR-0012 — Engineering Version and Baseline Semantics
- ADR-0018 — Engineering Knowledge Navigation
- RFC-0012 — Engineering Version Semantics
- RFC-0013 — Engineering Baseline Semantics
- RFC-0014 — Engineering Knowledge Navigation
- RFC-0025 — Canonical Relation Model
- RFC-0029 — Canonical Semantic Relation Constraint Model
- RFC-0030 — Canonical Engineering Artifact Serialization
- RFC-0031 — ATON Markdown Profile
- NOTE-0014 — Logical and Physical Artifact Representation
- NOTE-0017 — Logical Engineering Knowledge Graph and Physical Representations

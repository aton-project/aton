# RFC-0003 — Engineering Metadata Model

## Status

Draft

## Summary

This RFC defines the canonical semantic model for metadata within the ATON
Engineering Knowledge Model.

Metadata provides structured information describing engineering knowledge
without becoming the engineering content itself.

Metadata SHALL remain distinct from:

- engineering identity;
- engineering content;
- engineering relations;
- physical artifact representation; and
- derived information.

The canonical metadata model SHALL provide a stable semantic representation
that can be consumed by the ATON kernel independently of the physical
serialization format.

## Motivation

Engineering knowledge requires information describing its state, type,
ownership, lifecycle, provenance, applicability and other characteristics.

Such information is commonly stored together with engineering content.
However, metadata has a different semantic role from the content it
describes.

Without a canonical metadata model, implementations may:

- interpret YAML structures directly as domain semantics;
- mix metadata with engineering content;
- use physical file properties as canonical metadata;
- duplicate information that can be derived from other sources; or
- produce different semantic interpretations of the same engineering object.

ATON therefore requires a canonical metadata model independent of its
physical serialization.

## Goals

This RFC SHALL:

- define the semantics of engineering metadata;
- distinguish metadata from engineering content;
- distinguish metadata from engineering identity;
- distinguish canonical metadata from derived information;
- define metadata as part of the canonical Engineering Knowledge Model;
- provide a stable domain representation for metadata;
- allow metadata to be persisted independently of content;
- remain independent of YAML, Markdown, Git or other persistence formats;
- support verification of canonical metadata; and
- provide a foundation for metadata-aware navigation, versioning and
  traceability.

## Non Goals

This RFC does not define:

- the complete Engineering Entity model;
- the Engineering Identity model;
- engineering version semantics;
- relation predicate semantics;
- the complete ATON ontology;
- a mandatory metadata serialization format;
- a specific repository layout;
- a specific user interface;
- Git metadata semantics;
- project-specific metadata conventions; or
- algorithms for deriving arbitrary metadata.

## Proposal

### Metadata

Metadata SHALL represent structured information that describes an engineering
concept or engineering representation.

Metadata SHALL have semantic meaning only according to the applicable
canonical domain model.

Metadata SHALL NOT automatically become engineering content merely because it
is stored in the same physical artifact.

### Metadata and Engineering Entities

Metadata MAY describe an Engineering Entity.

For example, metadata MAY identify:

- the entity type;
- lifecycle state;
- applicable version;
- title;
- classification;
- provenance;
- applicability;
- other canonical properties.

Metadata SHALL NOT replace the canonical identity of the Engineering Entity.

The distinction is:

    Engineering Entity
            |
            +-- identity
            |
            +-- metadata
            |
            +-- content
            |
            +-- relations

Identity, metadata, content and relations SHALL remain semantically
distinguishable.

### Metadata and Identity

Metadata MAY contain information required to represent or resolve identity.

However, metadata and identity SHALL remain conceptually distinct.

A physical metadata file SHALL NOT itself become the identity of the entity.

The canonical identity model is defined by RFC-0002.

### Metadata and Content

Metadata SHALL describe engineering knowledge rather than constitute its
engineering content unless explicitly defined otherwise by the applicable
domain model.

For example:

    title: Brake System Requirement
    status: approved

describes an engineering object.

The requirement statement itself constitutes engineering content.

Changing metadata SHALL therefore not automatically imply a change to the
engineering content.

Conversely, changing engineering content SHALL not automatically imply that
every metadata property changes.

### Metadata and Relations

Relations SHALL remain separate from metadata.

A relation expresses a semantic connection between engineering concepts.

Metadata describes an engineering concept or representation.

For example:

    status: approved

is metadata, whereas:

    ```text
    Requirement --refines--> Specification
    ```

is a semantic relation.

Relations SHALL therefore not be encoded as ordinary metadata merely because
both may be physically stored in the same file.

The canonical Relation model is defined separately.

### Canonical Metadata

ATON SHALL define a canonical metadata domain model.

The canonical metadata model SHALL be independent of the serialization format
used to persist metadata.

Kernel components SHALL operate on canonical metadata representations.

Kernel components SHALL NOT depend directly on YAML, Markdown front matter,
JSON or other persistence-specific metadata structures.

### Persisted Metadata

Persisted metadata is metadata explicitly stored as part of the authoritative
engineering representation.

Persisted metadata MAY include information that must remain stable or
available independently of derived technical information.

Persisted metadata SHALL be retained when its semantic value cannot reliably
be reconstructed from authoritative information.

### Derived Metadata

Metadata MAY be derived from authoritative engineering information.

Derived metadata MAY originate from:

- Git history;
- engineering relations;
- engineering versions;
- artifact information;
- repository state;
- external systems; or
- other authoritative sources.

Derived metadata SHALL remain distinguishable from persisted canonical
metadata.

Derived information SHALL NOT silently overwrite authoritative persisted
metadata.

### Authoritative Metadata

Where multiple sources provide information describing the same property,
ATON SHALL define which source is authoritative for that property.

An implementation SHALL NOT arbitrarily select between conflicting sources.

Derived information MAY be used to augment or validate authoritative metadata,
but SHALL NOT redefine its semantic authority.

### Temporal Metadata

Temporal information MAY be represented as metadata.

A timestamp SHALL describe an event or temporal state.

A timestamp SHALL NOT by itself define an Engineering Version.

For example:

- creation time;
- modification time;
- review time; or
- release time

may be temporal metadata.

Version semantics remain defined independently by the Engineering Version
model.

### Metadata and Physical Representation

Metadata MAY be physically represented through:

- YAML;
- Markdown front matter;
- JSON;
- database records;
- APIs;
- Git structures; or
- other supported formats.

The physical representation SHALL NOT define the semantic meaning of the
metadata.

Multiple physical representations MAY represent the same canonical metadata.

### Metadata Normalization

Loaders SHALL normalize supported physical metadata representations into the
canonical metadata domain model.

The normalization boundary SHALL separate persistence concerns from kernel
semantics.

The kernel SHALL consume canonical metadata rather than interpreting
serialization-specific structures.

### Metadata Validation

The verification subsystem SHOULD verify canonical metadata.

Verification MAY identify:

- missing mandatory metadata;
- invalid metadata types;
- invalid values;
- conflicting metadata;
- invalid references;
- invalid lifecycle states;
- invalid version references; or
- other violations defined by the applicable ontology.

Verification SHALL operate on canonical metadata representations.

### Metadata and Ontology

The applicable ontology SHALL define the semantic meaning and constraints of
metadata properties where required.

A metadata property SHALL NOT acquire canonical semantic meaning merely because
a particular physical representation contains a field with that name.

Ontology definitions MAY specify:

- property names;
- value types;
- allowed values;
- applicability;
- cardinality;
- default semantics; and
- other constraints.

### Metadata Evolution

Metadata MAY evolve independently of engineering content.

A metadata change SHALL create a new Engineering Version only when the changed
metadata constitutes a semantic change relevant to the Engineering Entity's
engineering state.

A purely technical or derived metadata change SHALL NOT automatically create a
new Engineering Version.

Engineering Version semantics are defined separately.

### Metadata and Artifact Representation

An Engineering Artifact MAY contain:

- engineering content;
- metadata;
- relations; or
- combinations of these.

Physical co-location SHALL NOT imply semantic equivalence.

The canonical domain model SHALL preserve the distinction between these
concepts.

### Canonical Representation

The canonical metadata representation SHALL provide a stable interface for
kernel components.

Persistence-specific representations SHALL be transformed into this
canonical representation before being consumed by:

- verification;
- navigation;
- rendering;
- reasoning;
- traceability; or
- other kernel services.

This follows the canonical domain model principle established by the ATON
architecture.

## Consequences

### Positive

- Metadata has a stable semantic meaning.
- Metadata is independent of physical serialization.
- Persisted and derived information can be distinguished.
- The kernel remains independent of YAML and Markdown structures.
- Metadata can support verification, navigation and traceability.
- Alternative persistence mechanisms remain possible.
- Metadata evolution can be distinguished from semantic engineering change.

### Negative

- Implementations require a canonical metadata domain model.
- Loaders must normalize physical metadata.
- Sources of authority must be explicitly defined.
- Derived metadata requires provenance and conflict handling.
- Metadata changes may require explicit semantic classification.

## Alternatives

### Treat metadata as part of engineering content

Rejected.

Metadata and engineering content have different semantic roles and must remain
distinguishable.

### Treat metadata files as the domain model

Rejected.

Metadata files are physical representations of canonical metadata.

### Derive all metadata automatically

Rejected.

Some metadata represents authoritative engineering information that cannot
reliably be reconstructed from technical history or other derived sources.

### Persist all metadata

Rejected.

Persisting information that can be reliably derived may introduce redundancy,
inconsistency and unnecessary coupling to implementation details.

### Use Git metadata as canonical engineering metadata

Rejected.

Git provides technical history and provenance but does not define the
semantics of the Engineering Knowledge Model.

## Migration

Existing ATON metadata SHALL be migrated toward the canonical metadata model.

Migration SHOULD:

1. identify existing metadata properties;
2. classify each property as canonical, derived or implementation-specific;
3. identify the authoritative source for canonical properties;
4. normalize metadata into the canonical domain model;
5. preserve existing semantic information;
6. preserve provenance where applicable; and
7. remove or isolate implementation-specific metadata where appropriate.

Migration SHALL NOT assume that every existing metadata field is canonical.

Git history MAY provide evidence for deriving metadata during migration.

Derived information SHALL remain distinguishable from authoritative metadata.

## Open Questions

The following questions remain subject to further specification:

- Which metadata properties are mandatory for every Engineering Entity?
- Which metadata properties belong to the universal ATON model?
- Which metadata properties are ontology-specific?
- How are metadata conflicts resolved?
- How is metadata authority represented?
- Which derived metadata SHALL be standardized?
- How should metadata provenance be represented?
- Which metadata changes constitute semantic Engineering Version changes?
- How should external metadata sources be integrated?
- How should metadata schemas evolve over time?

These questions MAY be addressed by subsequent RFCs and ontology
specifications.

## References

- ADR-0010 — Canonical Metadata Domain Model
- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- RFC-0001 — Engineering Entity Model
- RFC-0002 — Identity Model
- RFC-0015 — Logical Engineering Knowledge and Physical Representations
- RFC-0025 — Canonical Relation Model

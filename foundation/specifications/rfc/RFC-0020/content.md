# RFC-0020 — Ontology

## Status

Draft

## Summary

This RFC defines the normative role and general semantics of ontologies
within the ATON Engineering Knowledge Model.

An ontology defines the semantic concepts used to classify and interpret
engineering knowledge.

The ontology provides the semantic vocabulary of the Engineering Knowledge
Model while remaining distinct from:

- physical artifact representation;
- persistence mechanisms;
- engineering content;
- metadata serialization;
- relation serialization; and
- implementation-specific behavior.

An ontology SHALL provide explicit semantic identity for the concepts used by
the Engineering Knowledge Model.

ATON implementations SHALL interpret ontology concepts according to their
canonical semantic definitions rather than according to physical
representation details.

This RFC defines the general ontology model. Concrete ATON ontology concepts
and predicate definitions are specified separately.

## Motivation

The Engineering Knowledge Model consists of interconnected engineering
concepts.

For these concepts to be interpreted consistently, their semantic meaning
must be defined independently of individual implementations.

Without an explicit ontology model, implementations may classify the same
engineering object differently or assign incompatible meanings to relations,
metadata or other domain concepts.

The ontology therefore provides the semantic vocabulary required to interpret
engineering knowledge consistently across ATON implementations.

The ontology also establishes a boundary between:

- semantic concept definition;
- engineering knowledge instances; and
- physical representations.

This separation allows the Engineering Knowledge Model to remain stable while
implementations and persistence mechanisms evolve.

## Goals

This RFC SHALL:

- define the general role of an ontology within the Engineering Knowledge
  Model;
- define ontology concepts as explicit semantic concepts;
- provide stable semantic identity for ontology concepts;
- distinguish ontology concepts from engineering knowledge instances;
- distinguish ontology semantics from physical representation;
- support explicit ontology typing of engineering artifacts;
- support specialization of ontology concepts;
- provide a foundation for semantic relation and predicate definitions;
- support semantic verification of engineering knowledge; and
- remain independent of a particular implementation or persistence
  technology.

## Non-Goals

This RFC does not define:

- the complete ATON ontology;
- individual ATON entity types;
- the complete set of relation predicates;
- predicate domain and range constraints;
- relation constraint enforcement rules;
- a specific ontology serialization format;
- a specific ontology language such as OWL or RDF;
- a database schema;
- a user interface for ontology navigation;
- implementation-specific type systems; or
- organizational engineering taxonomies.

Concrete ontology concepts and predicate semantics are defined by separate
Foundation specifications.

## Ontology

An ontology SHALL define semantic concepts used to describe and classify
engineering knowledge.

An ontology concept SHALL have a canonical semantic identity.

The identity of an ontology concept SHALL remain independent of:

- file paths;
- directory structures;
- database identifiers;
- programming-language types;
- serialization formats; or
- other implementation-specific representations.

An ontology concept MAY represent:

- an engineering entity type;
- an engineering artifact type;
- a metadata concept;
- a relation or predicate concept;
- a process concept;
- a lifecycle concept; or
- another semantic concept defined by the applicable ontology.

The ontology SHALL define the meaning of such concepts independently of their
physical representation.

## Ontology Concept Identity

Every ontology concept participating in the ATON semantic model SHALL have an
explicit canonical identifier.

The canonical identifier SHALL be stable within the applicable ontology
scope.

An ontology concept identifier SHALL NOT be inferred solely from:

- a file name;
- a directory name;
- a class name in implementation code;
- a database table;
- a Markdown heading; or
- another physical representation.

An implementation MAY use additional technical identifiers, but such
identifiers SHALL remain distinguishable from canonical ontology identity.

## Ontology Type

An engineering artifact that participates in the ATON semantic model SHALL
explicitly declare its canonical ontology type.

The ontology type SHALL identify the semantic concept under which the artifact
is interpreted.

Ontology type identity SHALL be represented explicitly in the canonical
Engineering Knowledge Model.

Ontology type SHALL NOT be inferred solely from physical persistence or
repository structure.

For example, the fact that an artifact is stored below an `rfc` directory
does not by itself define its semantic ontology type.

The canonical ontology declaration provides the semantic classification,
while persistence metadata describes how that classification is represented.

## Concept Specialization

An ontology MAY define specialization relationships between concepts.

A specialized ontology concept SHALL preserve the semantic meaning of the
concept from which it is specialized while adding or refining semantic
characteristics according to the applicable ontology rules.

Specialization SHALL be represented explicitly.

An implementation SHALL NOT infer semantic specialization solely from:

- naming conventions;
- directory structure;
- programming-language inheritance; or
- physical artifact organization.

Ontology specialization is a semantic relationship and SHALL therefore remain
part of the canonical semantic model.

## Ontology and Engineering Entities

An Engineering Entity is an instance of an engineering concept within the
Engineering Knowledge Model.

An ontology concept defines semantic meaning.

An Engineering Entity represents engineering knowledge that is classified
according to that meaning.

Therefore:

    Ontology Concept
           |
           | classifies
           ▼
    Engineering Entity

The ontology concept SHALL NOT be confused with the Engineering Entity itself.

Multiple Engineering Entities MAY be instances of the same ontology concept.

An Engineering Entity MAY evolve through multiple Engineering Versions without
changing its ontology type unless its semantic classification itself changes.

## Ontology and Artifacts

An Engineering Artifact is a representation of engineering knowledge according
to the applicable artifact model.

The artifact representation SHALL NOT itself define the ontology concept.

For example, a Markdown file, YAML file, database record or API object MAY
represent an engineering object classified by the same ontology concept.

The semantic classification SHALL therefore remain independent of the physical
representation.

## Ontology and Metadata

Ontology identity and metadata are distinct concepts.

Metadata MAY describe the ontology classification of an engineering object,
but the semantic meaning of the ontology concept SHALL be defined by the
ontology itself.

A metadata field containing an ontology identifier is therefore a
representation of ontology information and SHALL NOT become the semantic
definition of that ontology concept.

Canonical metadata semantics are defined separately by the metadata model.

## Ontology and Relations

Relations connect engineering knowledge according to explicitly defined
semantic predicates.

An ontology provides the semantic vocabulary required to interpret such
predicates.

The existence of a relation SHALL therefore be distinguishable from the
ontology concept that defines its semantic meaning.

For example:

    Engineering Entity A
            |
            | --predicate-->
            ▼
    Engineering Entity B

The predicate defines the semantic relationship between the participating
concepts.

The canonical Relation Model defines how relations are represented.

Predicate semantics and their semantic constraints are defined separately.

An implementation SHALL NOT assume that a syntactically valid relation is
semantically valid solely because both referenced objects exist.

Semantic validity MAY depend on the ontology types of the source and target
objects and on the applicable predicate constraints.

## Ontology and Semantic Constraints

Ontology concepts MAY participate in semantic constraints.

Such constraints MAY define:

- valid concept relationships;
- permitted predicate domains;
- permitted predicate ranges;
- specialization rules;
- required properties;
- prohibited combinations; or
- other semantic conditions.

Semantic constraints SHALL be interpreted according to their canonical
definitions.

The ontology model itself SHALL remain distinct from the mechanism used to
verify or enforce those constraints.

Detailed relation constraint semantics are defined separately.

## Ontology and Versioning

Ontology concepts SHALL remain distinct from Engineering Versions.

An Engineering Version represents a semantic state of an Engineering Entity.

An ontology concept defines the semantic classification of that entity.

Changing the content of an Engineering Entity SHALL NOT automatically create a
new ontology concept.

Likewise, changing an ontology definition SHALL NOT automatically create a
new Engineering Entity or Engineering Version unless the applicable semantic
model explicitly requires such a change.

Ontology evolution is therefore distinct from engineering knowledge
versioning.

## Ontology Evolution

An ontology MAY evolve over time.

Changes to ontology concepts SHALL preserve explicit semantic history where
required.

An ontology concept SHALL NOT silently change its semantic meaning in a way
that makes existing engineering knowledge ambiguous.

Where a semantic change is incompatible with the previous definition, the
ontology SHOULD introduce a distinct concept or an explicit evolution
mechanism.

The applicable ontology governance model SHALL determine how ontology changes
are reviewed, accepted and versioned.

## Ontology and Persistence

Ontology semantics SHALL remain independent of persistence technology.

An ontology MAY be represented using:

- YAML;
- Markdown;
- JSON;
- RDF;
- OWL;
- databases;
- APIs; or
- other physical representations.

No particular serialization format SHALL define the semantic meaning of an
ontology concept.

Loaders SHALL translate physical ontology representations into the canonical
domain model.

Kernel components SHALL operate on canonical ontology semantics rather than
persistence-specific structures.

## Ontology and Implementation

An implementation MAY map ontology concepts to programming-language types,
database schemas or other technical structures.

Such mappings SHALL NOT redefine ontology semantics.

Two implementations MAY use different internal representations while
conforming to the same ontology.

Conformance SHALL therefore be determined by semantic interpretation rather
than by implementation structure.

## Verification

ATON MAY verify ontology consistency.

Verification MAY detect:

- duplicate ontology identifiers;
- missing ontology definitions;
- invalid specialization relationships;
- unresolved ontology references;
- invalid ontology typing;
- incompatible semantic constraints; or
- other violations defined by applicable ontology specifications.

Verification SHALL operate on canonical ontology semantics.

An implementation SHALL NOT treat successful parsing or storage as evidence
of semantic validity.

## Consequences

### Positive

- Engineering knowledge receives a stable semantic vocabulary.
- Ontology identity remains independent of physical representation.
- Different implementations can interpret the same engineering concepts
  consistently.
- Semantic typing becomes explicit.
- Relation and predicate semantics can build on a common ontology model.
- Ontology evolution remains distinguishable from engineering versioning.
- Alternative persistence and implementation technologies remain possible.

### Negative

- Ontology concepts require explicit identifiers and definitions.
- Implementations must maintain a mapping between physical representations
  and canonical ontology concepts.
- Ontology evolution requires explicit semantic governance.
- Semantic verification becomes more important as the ontology grows.

## Alternatives Considered

### Infer ontology types from repository structure

Rejected.

Repository paths and directory structures are physical representations and
must not define semantic identity.

### Infer ontology types from file extensions

Rejected.

File extensions describe physical representation rather than semantic meaning.

### Use programming-language types as the ontology

Rejected.

Implementation types are technology-specific and cannot provide a stable
semantic model across implementations.

### Allow every implementation to define its own ontology

Rejected.

Independent semantic vocabularies would prevent consistent interpretation and
interoperability between ATON implementations.

### Adopt a specific ontology technology as the canonical semantic model

Rejected.

ATON requires semantic independence from particular representation and
ontology technologies. Specific technologies MAY be used as representations
or implementation mechanisms.

## Migration

Existing engineering artifacts may not explicitly declare their ontology
type.

A migration implementation MAY infer candidate ontology classifications from
existing metadata, repository structure or other available evidence.

Such inferred classifications SHALL be treated as migration information until
they are explicitly established as canonical ontology information.

Migration SHALL NOT silently convert implementation-specific classifications
into normative ontology semantics without an applicable semantic definition.

Where ontology classification cannot be determined reliably, the migration
SHALL preserve the uncertainty rather than inventing semantic information.

## Open Questions

The following topics remain outside the normative scope of this RFC and may be
addressed by future specifications:

- the complete ATON ontology;
- canonical ontology concept identifiers;
- ontology namespaces;
- ontology inheritance and specialization rules in detail;
- ontology versioning conventions;
- ontology governance;
- formal ontology languages and mappings;
- detailed predicate semantics;
- domain and range constraints;
- ontology import and composition; and
- ontology equivalence and mapping between external ontologies.

## Acceptance Criteria

A conforming implementation SHALL:

1. treat ontology concepts as explicit semantic concepts;
2. provide stable canonical identity for ontology concepts;
3. distinguish ontology concepts from Engineering Entities;
4. distinguish ontology semantics from physical representation;
5. support explicit ontology typing where required by the canonical model;
6. avoid inferring semantic identity solely from repository structure;
7. preserve the distinction between ontology concepts and Engineering Versions;
8. permit ontology concepts to provide semantic vocabulary for relations and
   predicates;
9. keep ontology semantics independent of persistence technology; and
10. avoid silently inventing normative ontology semantics during migration.

## References

- ADR-0007 — Foundation as the Engineering Knowledge Specification
- ADR-0008 — Canonical Domain Models
- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- RFC-0025 — Canonical Relation Model
- RFC-0026 — Ontological Predicates
- RFC-0027 — ATON Ontology
- RFC-0029 — Canonical Semantic Relation Constraint Model
- NOTE-0008 — Entity and Artifact Semantics
- NOTE-0010 — Engineering Relation Semantics
- NOTE-0012 — Engineering Metadata Semantics
- NOTE-0021 — Semantic Constraints for Relations

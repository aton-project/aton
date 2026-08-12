# RFC-0004 — Engineering Relation Model

## Status

Draft

## Summary

This RFC defines the canonical semantic model for relationships within the
ATON Engineering Knowledge Model.

An Engineering Relation represents an explicit semantic connection between
engineering concepts.

Relations are first-class elements of the Engineering Knowledge Model and
provide the basis for traceability, navigation, dependency analysis and
impact analysis.

This RFC defines the conceptual semantics of relations.

The canonical internal representation of relations is defined separately by
RFC-0025.

Semantic constraints governing the validity of source, predicate and target
combinations are defined separately by RFC-0029.

## Motivation

Engineering knowledge consists of interconnected concepts rather than
isolated objects.

A Requirement may refine another Requirement.
A Component may implement a Specification.
An Architecture Decision may govern a design choice.
A Finding may motivate a Note.

These connections have engineering meaning and therefore cannot be treated
merely as hyperlinks or physical references.

Without a canonical semantic relation model, implementations may:

- interpret relationships differently;
- confuse physical references with engineering relationships;
- use inconsistent directionality;
- infer relationships from storage structures;
- duplicate relationship semantics in different subsystems; or
- accept structurally representable but semantically invalid relations.

ATON therefore requires a persistence-independent semantic model for
Engineering Relations.

## Goals

This RFC SHALL:

- define the semantics of an Engineering Relation;
- establish relations as first-class elements of the Engineering Knowledge
  Model;
- define source, predicate and target semantics;
- define relation directionality;
- distinguish semantic relations from physical references;
- distinguish explicit relations from derived relations;
- define common semantic properties of relations;
- provide a foundation for traceability and navigation;
- remain independent of persistence and serialization technologies; and
- provide the semantic foundation for canonical relation representation and
  validation.

## Non Goals

This RFC does not define:

- the complete list of ATON predicates;
- the canonical internal Relation domain object;
- serialization formats for relations;
- source-to-target predicate validity constraints;
- relation cardinality rules for individual predicates;
- a specific repository structure;
- a specific user interface;
- a specific persistence technology;
- automatic semantic inference algorithms; or
- project-specific relationship conventions.

The canonical internal Relation representation is defined by RFC-0025.

Semantic relation constraints are defined by RFC-0029.

Concrete predicate definitions are defined by the applicable ontology and
predicate specifications.

## Proposal

### Engineering Relation

An Engineering Relation SHALL represent a semantic connection between two
engineering concepts.

A relation SHALL have:

- a source;
- a predicate; and
- a target.

Conceptually:

    ```text
    Source --Predicate--> Target
    ```

The source and target SHALL refer to addressable engineering concepts within
the applicable Engineering Knowledge Model.

### Source

The source SHALL identify the engineering concept from which the relation
originates.

The source provides the semantic context in which the predicate is
interpreted.

A relation SHALL NOT be interpreted independently of its source.

### Predicate

The predicate SHALL define the semantic meaning of the relationship between
source and target.

Examples MAY include:

- references;
- refines;
- governs;
- motivates;
- implements;
- dependsOn;
- contains; or
- other predicates defined by the applicable ontology.

A predicate SHALL have a defined semantic meaning before it is considered a
canonical engineering relationship.

A predicate name alone SHALL NOT establish semantic validity for arbitrary
source and target types.

### Target

The target SHALL identify the engineering concept to which the relation
connects the source.

The target SHALL be interpreted according to the semantics of the predicate.

A target reference SHALL therefore not automatically imply a valid
engineering relation merely because the target exists.

### Directionality

Engineering Relations SHALL be interpreted according to their defined
direction.

For:

    ```text
    A --references--> B
    ```

the semantic relation is from A to B.

The direction SHALL be part of the semantic interpretation of the predicate.

An implementation MAY support traversal in the inverse direction for
navigation purposes.

Inverse traversal SHALL NOT automatically create an inverse semantic
relation.

For example:

    ```text
    A --references--> B
    ```

MAY be navigated from B to A without implying:

    ```text
    B --references--> A
    ```

### Symmetry

A predicate MAY be defined as symmetric where the applicable semantic model
establishes that the relationship has equivalent meaning in both directions.

Symmetry SHALL be a semantic property of the predicate.

A relation SHALL NOT be treated as symmetric merely because an implementation
allows traversal in both directions.

### Transitivity

A predicate MAY be defined as transitive where the applicable semantic model
explicitly establishes transitivity.

For a transitive predicate P:

    ```text
    A --P--> B
    B --P--> C
    ```

may permit the inference:

    ```text
    A --P--> C
    ```

only when the semantics of P explicitly allow that inference.

Transitivity SHALL NOT be assumed for arbitrary predicates.

### Explicit Relations

Canonical Engineering Relations SHOULD be represented explicitly whenever
their existence constitutes authoritative engineering knowledge.

The existence of two engineering concepts SHALL NOT by itself establish a
relation between them.

Physical proximity, naming similarity, common containment or textual
similarity SHALL NOT automatically create an explicit Engineering Relation.

### Derived Relations

A relation MAY be derived from authoritative engineering information where
the applicable semantic model explicitly permits derivation.

Derived relations SHALL remain distinguishable from explicitly maintained
relations.

A derived relation SHALL NOT silently replace an explicitly maintained
relation.

The provenance and derivation rules for derived relations MAY be defined by
subsequent specifications.

### Relation Identity

The semantic identity of a relation SHALL be determined by its canonical
engineering meaning rather than by its physical representation.

A file path, YAML entry position, database record or URL SHALL NOT by itself
define the semantic identity of a relation.

The canonical internal representation and identity handling are defined by
the applicable domain model.

### Relation and Engineering Entities

Engineering Relations SHALL connect semantic engineering concepts.

A relation MAY connect:

- Engineering Entities;
- Engineering Artifacts;
- Engineering Versions;
- Processes;
- Findings;
- Decisions;
- Requirements;
- Tests; or
- other concepts defined by the applicable ontology.

Whether a particular combination is valid SHALL be determined by the
applicable semantic constraints.

### Relation and Engineering Versions

Relations MAY be associated with Engineering Versions.

A relation existing in one Engineering Version SHALL NOT automatically be
assumed to exist in another Engineering Version.

Version-aware relation semantics SHALL preserve the engineering state in
which the relationship was authoritative.

Engineering Version semantics are defined separately.

### Relation and Baselines

A Baseline MAY select Engineering Relations through the Engineering Knowledge
state it represents.

A Baseline SHALL NOT create new semantic relations merely by selecting
engineering knowledge.

Relations SHALL be interpreted according to the Engineering Versions and
other engineering state selected by the Baseline.

Baseline semantics are defined separately.

### Relation and Releases

A Release MAY identify an engineering state containing Engineering Relations.

A Release SHALL NOT redefine the semantic meaning of its relations.

Release semantics are defined separately from the relation model.

### Relation and Physical Representation

Engineering Relations SHALL remain independent of their physical
representation.

Relations MAY be represented through:

- YAML;
- Markdown;
- JSON;
- databases;
- APIs;
- Git repositories; or
- other supported representations.

Changing the physical representation SHALL NOT inherently change the
semantic relationship.

### Physical References

A physical reference and an Engineering Relation SHALL remain conceptually
distinct.

For example, a hyperlink between two documents does not automatically
constitute an engineering relation.

A physical reference MAY provide the mechanism through which a semantic
relation is represented or resolved.

The semantic relation SHALL remain defined by the canonical Engineering
Knowledge Model.

### Relation Constraints

A relation is semantically valid only when its source, predicate and target
satisfy the applicable semantic constraints.

These constraints MAY define:

- allowed source types;
- allowed target types;
- predicate applicability;
- cardinality;
- directionality;
- symmetry;
- transitivity;
- lifecycle constraints;
- version constraints; or
- other semantic properties.

RFC-0029 defines the canonical semantic constraint model.

### Relation Validation

Relation validation SHALL distinguish structural validity from semantic
validity.

Structural validation MAY determine whether:

- a relation is representable;
- its target exists;
- required fields are present; or
- its representation is structurally consistent.

Semantic validation MAY determine whether:

- the predicate is defined;
- the source type is permitted;
- the target type is permitted;
- the source-to-target combination is valid; or
- the relation satisfies applicable semantic constraints.

A structurally valid relation MAY therefore be semantically invalid.

### Relation and the Engineering Knowledge Graph

Engineering Relations SHALL form the semantic connections of the Engineering
Knowledge Graph.

The Engineering Knowledge Graph SHALL therefore represent engineering
knowledge through concepts and their explicit relationships.

Relations SHALL NOT form a separate parallel semantic model.

Traceability, navigation and impact analysis MAY use Engineering Relations as
their underlying semantic basis.

### Relation and Traceability

Engineering Relations provide the basis for canonical traceability.

Traceability MAY traverse:

- outgoing relations;
- incoming relations;
- selected predicates;
- multi-step relation paths;
- version-specific relations; or
- baseline-specific relations.

Traceability semantics are defined separately by RFC-0023.

### Relation and Navigation

Engineering Relations SHALL provide a primary basis for semantic navigation.

Navigation MAY traverse relations according to:

- predicate semantics;
- direction;
- applicable version;
- baseline;
- release; or
- other canonical engineering state.

Navigation SHALL NOT infer semantic relations from physical containment or
presentation structures.

Navigation semantics are defined separately.

### Canonical Domain Representation

The ATON kernel SHALL operate on a canonical internal representation of
Engineering Relations.

Physical serialization formats SHALL be normalized before relations are
consumed by kernel components.

The canonical internal Relation model is defined by RFC-0025.

Kernel components SHALL NOT depend directly on persistence-specific relation
serialization.

### Predicate Semantics

The semantic meaning of individual predicates SHALL be defined separately
from the generic relation model.

Predicate specifications MAY define:

- predicate meaning;
- direction;
- inverse semantics;
- symmetry;
- transitivity;
- allowed source concepts;
- allowed target concepts;
- cardinality;
- lifecycle behaviour; and
- derivation rules.

The generic relation model SHALL provide the common semantic foundation for
such predicate definitions.

## Consequences

### Positive

- Engineering relationships have explicit semantic meaning.
- Relations become first-class elements of the Engineering Knowledge Model.
- Traceability and navigation can use a common semantic foundation.
- Physical references are clearly separated from engineering relationships.
- Structural and semantic validation can be separated.
- Relation semantics remain independent of persistence technology.
- Predicate-specific constraints can evolve independently from the generic
  relation model.

### Negative

- Implementations must explicitly model relations.
- Predicate semantics require additional specifications.
- Semantic validation requires ontology and constraint information.
- Version-aware and baseline-aware relation handling introduces additional
  complexity.
- Derived relations require explicit provenance and derivation rules.

## Alternatives

### Treat hyperlinks as Engineering Relations

Rejected.

Hyperlinks are physical or presentation mechanisms and do not inherently
express engineering semantics.

### Treat file references as Engineering Relations

Rejected.

A file reference identifies a physical representation and does not
necessarily express a semantic engineering relationship.

### Infer all relations automatically

Rejected.

Engineering relationships are authoritative engineering knowledge and cannot
reliably be inferred solely from physical structure, names or textual
similarity.

### Define relation semantics inside the serialization format

Rejected.

Serialization formats are physical representations and must not define the
canonical Engineering Knowledge Model.

### Define all relation semantics in one generic model

Rejected.

The generic relation model defines common semantics, while individual
predicates and their constraints require separate semantic definitions.

## Migration

Existing ATON relation representations SHALL be interpreted according to the
canonical Engineering Relation model.

Migration SHOULD:

1. identify existing relation structures;
2. distinguish physical references from semantic relations;
3. identify source, predicate and target;
4. identify the applicable predicate semantics;
5. normalize relations into the canonical Relation model;
6. preserve existing semantic relationships;
7. classify derived relationships where applicable; and
8. validate semantic constraints where available.

Migration SHALL NOT assume that every existing reference is an Engineering
Relation.

Legacy relation serialization formats MAY be supported during migration.

The migration strategy for physical relation representations is defined
separately by RFC-0025 and related specifications.

## Open Questions

The following questions remain subject to further specification:

- Which predicates belong to the canonical ATON Foundation ontology?
- Which predicates are symmetric?
- Which predicates are transitive?
- Which predicates may be derived?
- Which predicates require explicit maintenance?
- Which relation properties are universal?
- How should relation provenance be represented?
- How should relation lifecycle be modeled?
- How should relation identity be represented across Engineering Versions?
- Which cardinality constraints are required by the Foundation?
- How should inferred relation paths be distinguished from explicit relations?

These questions MAY be addressed by subsequent predicate, ontology and
constraint specifications.

## References

- ADR-0004 — Artifact-Based Knowledge Organization
- ADR-0005 — Separation of Content, Metadata and Relations
- ADR-0006 — Engineering Knowledge Graph
- ADR-0014 — Canonical Semantic Relation Model
- RFC-0023 — Engineering Traceability
- RFC-0025 — Canonical Relation Model
- RFC-0029 — Canonical Semantic Relation Constraint Model
- NOTE-0010 — Engineering Relation Semantics
- NOTE-0013 — Engineering Relationship Semantics
- NOTE-0016 — Engineering Relationship Semantics

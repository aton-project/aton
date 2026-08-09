# RFC-0027 ATON Ontology

## Status

Draft

## Summary

This RFC defines the initial normative ontology of ATON.

The ontology defines the Concepts and semantic Predicates used to represent
engineering knowledge in the ATON knowledge graph.

RFC-0025 defines the canonical technical representation of relations.

RFC-0026 defines the general model and constraints for ontological
Predicates.

This RFC defines the initial ATON-specific vocabulary built on those
specifications.

## Scope

This RFC specifies:

- the initial ATON Concept taxonomy
- the initial ATON Predicate vocabulary
- allowed source-to-target Concept pairs
- inverse Predicates
- Predicate semantics
- rules for ontology validation
- rules for extending the ontology

This RFC does not define:

- implementation of the Relation domain object
- implementation of the verification engine
- reasoning or inference algorithms
- a specific ontology serialization format

## Ontological Model

The ATON ontology consists of two primary elements:

    Concept

    Predicate

A Concept defines a class of engineering knowledge.

A Predicate defines a semantically meaningful relationship between a source
Concept and a target Concept.

The combination forms a typed knowledge graph:

    Concept --Predicate--> Concept

Individual artifacts are instances of Concepts.

## Concept Model

All ATON artifacts SHALL belong to a defined Concept.

The initial Concept taxonomy is:

    Artifact
    Requirement
    Decision
    RFC
    ADR
    Note
    Review
    Finding
    Component
    Interface
    Test
    Definition
    GlossaryEntry
    View
    Collection
    Metadata
    Property
    Entity
    AX
    Constitution
    Predicate

The `Artifact` Concept is the general concept from which artifact Concepts
may derive.

### AX

`AX` (ATON Experience) is the Concept representing the specification of how
engineering knowledge is presented, explored, and understood in ATON
applications.

AX defines user experience semantics and is independent of a specific user
interface implementation.

### Constitution

`Constitution` is the Concept representing the highest architectural and
governance document of the ATON Foundation.

The Constitution establishes the enduring purpose, principles, boundaries,
and architectural foundations of ATON.

### Predicate

`Predicate` is the Concept representing a canonical semantic relationship in
the ATON ontology.

A Predicate defines a directional relationship between a source Concept and a
target Concept and SHALL define its allowed source-to-target Concept pairs.

## Concept Specialization

Concepts MAY specialize other Concepts.

For example:

    ADR
      |
      +-- specializes --> Decision

    RFC
      |
      +-- specializes --> Artifact

Concept specialization defines taxonomy.

It SHALL NOT automatically expand the applicability of Predicates.

If a Predicate is valid for one Concept, it SHALL NOT automatically become
valid for a specialized or generalized Concept unless the Predicate
definition explicitly permits that Concept.

## Predicate Model

Every normative Predicate SHALL define:

    id
    meaning
    allowed source-to-target pairs

A Predicate MAY additionally define:

    inverse
    cardinality
    symmetric
    transitive

The allowed source-to-target pairs are normative.

They define exactly which Concept combinations are valid for the Predicate.

## Allowed Source-to-Target Pairs

A Predicate SHALL NOT define independent source and target sets and assume
that every combination is valid.

Instead, the ontology SHALL define explicit allowed pairs.

For example:

    Predicate:
        motivates

    Allowed pairs:
        Note -> ADR
        Finding -> ADR

This means:

    Note -> motivates -> ADR
        valid

    Finding -> motivates -> ADR
        valid

    Note -> motivates -> Decision
        invalid

    Finding -> motivates -> Note
        invalid

The explicit pair model SHALL be used for semantic validation.

## Initial Predicate Vocabulary

The initial ATON Predicate vocabulary is defined below.

### references

Meaning:

An artifact explicitly refers to another artifact as a source of information
or context.

Allowed pairs:

    Artifact -> Artifact

Inverse:

    referencedBy

### motivates

Meaning:

A Note or Finding provides rationale, evidence, observation, or an identified
problem contributing to an architectural or engineering decision.

Allowed pairs:

    Note -> ADR
    Finding -> ADR

Inverse:

    motivatedBy

### specifies

Meaning:

An RFC defines the normative technical specification of an architectural
decision.

Allowed pairs:

    RFC -> ADR

Inverse:

    specifiedBy

### implements

Meaning:

A Component realizes or implements the behavior or specification defined by
another engineering artifact.

Allowed pairs:

    Component -> RFC
    Component -> Requirement

Inverse:

    implementedBy

### verifies

Meaning:

A Test provides verification evidence for an engineering artifact.

Allowed pairs:

    Test -> Requirement
    Test -> Component
    Test -> RFC

Inverse:

    verifiedBy

### governs

Meaning:

An artifact establishes rules, principles, or constraints governing another
artifact or artifact collection.

Allowed pairs:

    ADR -> Artifact
    ADR -> Collection

Inverse:

    governedBy

### defines

Meaning:

An artifact establishes the authoritative definition of an engineering
concept, term, property, interface, or other knowledge element.

Allowed pairs:

    Definition -> Entity
    Definition -> Property
    Definition -> Interface
    GlossaryEntry -> Entity
    GlossaryEntry -> Property
    GlossaryEntry -> Interface
    RFC -> Interface
    ADR -> Interface

Inverse:

    definedBy

### allocates

Meaning:

A requirement is allocated to a component responsible for its realization.

Allowed pairs:

    Requirement -> Component

Inverse:

    allocatedFrom

### refines

Meaning:

An artifact provides a more detailed or specialized expression of another
engineering artifact while preserving its essential intent.

Allowed pairs:

    Requirement -> Requirement
    RFC -> RFC
    ADR -> ADR
    Component -> Component
    Interface -> Interface

Inverse:

    refinedBy

### specializes

Meaning:

A Concept or artifact represents a more specific form of another Concept or
artifact.

Allowed pairs:

    Artifact -> Artifact
    Definition -> Definition
    Entity -> Entity

Inverse:

    specializedBy

### contains

Meaning:

An artifact or collection contains another artifact as a member of its
defined scope.

Allowed pairs:

    Collection -> Artifact
    Review -> Finding
    Artifact -> Artifact

Inverse:

    containedIn

## Predicate Direction

Predicates SHALL be directional.

For example:

    NOTE-0020
        |
        | motivates
        v
    ADR-0008

does not imply:

    ADR-0008
        |
        | motivates
        v
    NOTE-0020

If the inverse relationship is meaningful, it SHALL be defined explicitly.

## Inverse Predicates

Inverse Predicates SHALL be explicitly defined.

Examples:

    motivates
        inverse:
            motivatedBy

    specifies
        inverse:
            specifiedBy

    implements
        inverse:
            implementedBy

    verifies
        inverse:
            verifiedBy

An inverse Predicate SHALL preserve the semantic meaning of the original
relationship when its direction is reversed.

The existence of an inverse Predicate does not permit the original Predicate
to be used in the inverse direction.

## Predicate Identity

Predicate names SHALL be stable ontology identifiers.

A Predicate name SHALL NOT be introduced solely for convenience of a
serialization format.

Predicate names SHALL represent domain semantics.

The following generic Predicates SHALL NOT be part of the normative ATON
ontology:

    parent
    child
    related

When a relationship has a specific engineering meaning, a semantic Predicate
SHALL be used instead.

## Semantic Validation

The verification layer SHALL validate every explicit relation against the
ontology.

For each relation, verification SHALL determine:

    source artifact
        |
        v
    source Concept
        |
        v
    Predicate
        |
        v
    target Concept
        |
        v
    allowed source-to-target pairs

A relation SHALL be valid only if the exact source Concept and target Concept
combination is present in the Predicate's allowed pair set.

For example:

    Note -> motivates -> ADR

is valid if that pair is defined.

    Note -> motivates -> Decision

is invalid if that pair is not defined, even if `Decision` is a Concept
related to `ADR`.

Similarly:

    Finding -> motivates -> Note

is invalid if that pair is not explicitly defined.

## No Implicit Predicate Inheritance

Predicate applicability SHALL NOT be inherited automatically through Concept
specialization.

For example, if:

    ADR specializes Decision

and:

    Note -> motivates -> ADR

is valid,

the following relation SHALL NOT automatically become valid:

    Note -> motivates -> Decision

The ontology MUST explicitly define that pair if it is intended to be valid.

This rule prevents unintended relations from being introduced through
taxonomy inheritance.

## Cardinality

A Predicate MAY define cardinality constraints.

Cardinality SHALL describe the permitted number of targets for a given source
and Predicate.

Examples include:

    0..1
    0..*
    1..1
    1..*

Cardinality constraints are evaluated independently of source-to-target
Concept validity.

A relation MUST first satisfy the allowed source-to-target pair constraint
before cardinality is evaluated.

## Explicit Relations

An explicit relation is a relation directly represented in the Foundation.

For example:

    NOTE-0020
        |
        | motivates
        v
    ADR-0008

The relation is explicitly authored.

Explicit relations are authoritative source data.

## Derived Relations

A derived relation is a relation generated from explicitly defined relations
and ontology rules.

Derived relations SHALL remain distinguishable from explicitly authored
relations.

For example, if:

    motivates
        inverse:
            motivatedBy

then:

    Note -> motivates -> ADR

may provide the derived inverse relation:

    ADR -> motivatedBy -> Note

The mechanism for generating derived relations is outside the scope of this
RFC.

## Inferred Relations

Inference is the process of deriving knowledge from existing knowledge and
formal rules.

Inference MAY be supported by future ATON components.

Inference SHALL NOT be required for initial ontology validation.

Future specifications MAY define:

- inference rules
- transitive reasoning
- rule composition
- provenance
- derived knowledge lifecycle

## Ontology Evolution

The ATON ontology SHALL evolve under controlled specification.

A new Concept or Predicate SHALL NOT be introduced only through
implementation code.

New ontology elements SHALL be specified before normative Foundation
artifacts use them.

Changes to the meaning of an existing Predicate SHALL be treated as a
semantic change.

Changes to allowed source-to-target pairs SHALL be treated as ontology
changes and MAY require migration of existing relations.

## Compatibility

Ontology changes SHOULD preserve the semantic meaning of existing
Predicates.

Removing an allowed source-to-target pair MAY invalidate existing
Foundation relations.

Adding an allowed source-to-target pair SHALL NOT invalidate existing
relations.

Renaming a Predicate SHALL be treated as a semantic migration rather than a
simple text replacement.

## Design Principle

ATON SHALL prefer a small, precise vocabulary over a large set of overlapping
Predicates.

A new Predicate SHOULD only be introduced when an existing Predicate cannot
express the intended engineering meaning without ambiguity.

Generic structural relationships SHOULD NOT be introduced when a domain
specific semantic Predicate can express the intended relationship.

## Future Extensions

Future RFCs MAY define:

- additional Concepts
- additional Predicates
- Predicate namespaces
- additional cardinality constraints
- lifecycle constraints
- ontology serialization
- ontology versioning
- inference rules
- provenance of derived knowledge
- automated ontology validation

## References

- RFC-0025 Canonical Relation Model
- RFC-0026 Ontological Predicates

# RFC-0026 Ontological Predicates

## Status

Draft

## Summary

This RFC specifies the semantic model for predicates within the ATON
knowledge graph.

RFC-0025 defines the canonical technical representation of relations inside
the kernel.

This RFC defines the semantic meaning and validity of those relations.

A predicate SHALL represent a defined domain relationship between two
concepts.

## Scope

This RFC specifies:

- the concept of an ontological predicate
- predicate identity
- predicate semantics
- source and target constraints
- predicate direction
- inverse predicates
- cardinality
- semantic validation requirements
- the separation between explicit and derived relations

The implementation of inference and reasoning is outside the scope of this
RFC.

## Ontological Predicate

An ontological predicate defines a semantic relationship between a source
concept and a target concept.

A predicate SHALL have a defined semantic meaning.

A predicate MUST NOT be interpreted merely as an arbitrary string.

For example:

    NOTE
      |
      | motivates
      v
    ADR

The predicate `motivates` expresses a specific engineering relationship.

## Predicate Identity

Each predicate SHALL have a stable identifier.

The identifier SHALL uniquely identify the predicate within the ATON ontology.

Predicate identifiers SHOULD use a concise, human-readable form.

Examples include:

    motivates
    specifiedBy
    implements
    verifies
    governs
    defines
    allocates
    refines
    specializes
    references

The identifier alone does not define the complete semantics of a predicate.

The ontology definition SHALL provide the complete predicate specification.

## Predicate Semantics

Every predicate SHALL define its intended meaning.

The meaning SHALL be expressed independently of any particular serialization
format.

For example:

    motivates

may be defined as:

    A Note provides a rationale, observation, or identified problem that
    contributes to an architectural decision.

The semantic definition SHALL be authoritative for interpretation of the
predicate.

## Source Constraints

A predicate SHALL define the concept types that MAY act as its source.

Example:

    predicate: motivates

    source:
      - Note

This means that `motivates` MAY originate from a Note.

An artifact that is not compatible with the defined source concept SHALL NOT
use the predicate.

## Target Constraints

A predicate SHALL define the concept types that MAY act as its target.

Example:

    predicate: motivates

    source:
      - Note

    target:
      - ADR

This defines the valid direction:

    Note -> ADR

The reverse direction SHALL NOT be assumed to be valid.

## Predicate Direction

Predicates SHALL be directional.

The source and target concepts are part of the semantic definition.

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

A predicate MAY define an inverse predicate.

For example:

    motivates
        inverse:
            motivatedBy

This establishes two semantically related predicates:

    Note -> motivates -> ADR

    ADR -> motivatedBy -> Note

An inverse predicate SHALL NOT be inferred merely from naming conventions.

The ontology SHALL explicitly define inverse relationships.

## Cardinality

A predicate MAY define cardinality constraints.

Cardinality SHALL describe the permitted number of targets for a given source.

Examples include:

    0..1
    0..*
    1..1
    1..*

Cardinality constraints SHALL be interpreted by the ontology validation layer.

A missing cardinality definition SHALL mean that no cardinality constraint is
defined by this RFC.

## Predicate Specification

A complete predicate definition SHOULD contain at least:

    id
    description
    source
    target

It MAY additionally contain:

    inverse
    cardinality
    symmetric
    transitive

Example:

    id: motivates

    description:
      A Note provides rationale or an identified problem for an ADR.

    source:
      - Note

    target:
      - ADR

    inverse:
      motivatedBy

    cardinality:
      0..*

The exact serialization format for ontology definitions is outside the scope
of this RFC.

## Semantic Validation

The verification subsystem SHALL be able to validate relations against the
ontology.

At minimum, semantic validation SHALL be capable of determining:

- whether the predicate exists
- whether the source concept is permitted
- whether the target concept is permitted
- whether the relation direction is valid
- whether cardinality constraints are satisfied when defined

A relation that violates an ontology constraint SHALL be reported as a
verification issue.

## Explicit Relations

An explicit relation is a relation directly represented in the Foundation.

For example:

    NOTE-0020
        |
        | motivates
        v
    ADR-0008

The relation is explicitly stored by the author.

Explicit relations form the authoritative source data of the knowledge graph.

## Derived Relations

A derived relation is a relation that can be generated from explicitly defined
relations and ontology rules.

Derived relations SHALL NOT be treated as independently authored source data.

For example, if the ontology defines:

    motivates
        inverse:
            motivatedBy

then:

    NOTE-0020 -> motivates -> ADR-0008

may provide the derived relation:

    ADR-0008 -> motivatedBy -> NOTE-0020

The mechanism for generating derived relations is outside the scope of this
RFC.

## Inferred Relations

Inference is the process of deriving knowledge from existing knowledge and
formal rules.

Inference MAY be supported by future ATON components.

Inference SHALL NOT be considered part of the initial predicate validation
defined by this RFC.

Future specifications MAY define:

- inference rules
- transitive reasoning
- rule composition
- derived knowledge lifecycle
- provenance of inferred knowledge

## Ontology Constraints

The ontology MAY define constraints between concepts and predicates.

Examples include:

- allowed source concepts
- allowed target concepts
- cardinality
- inverse predicates
- symmetry
- transitivity
- lifecycle constraints

These constraints SHALL be machine-readable in the canonical ontology model.

## Separation of Concerns

The following responsibilities SHALL remain separate:

    Foundation serialization
        |
        v
    Canonical Relation Model
        |
        v
    Ontological Predicate
        |
        v
    Semantic Validation
        |
        v
    Future Reasoning

RFC-0025 defines the canonical relation representation.

This RFC defines predicate semantics and semantic constraints.

Future specifications MAY define reasoning and inference.

## Consequences

The ontological predicate model provides:

- semantically meaningful relations
- explicit source and target constraints
- machine-verifiable relationship semantics
- separation between technical representation and domain meaning
- a foundation for ontology-based verification
- a foundation for future knowledge graph reasoning

It prevents generic structural relationships from becoming an uncontrolled
part of the ATON knowledge model.

## Design Principle

ATON SHALL prefer semantically meaningful predicates over generic structural
relationships.

Generic relationships such as:

    parent
    child
    related

SHOULD NOT be introduced when a domain-specific semantic predicate can express
the intended relationship.

## Future Extensions

Future specifications MAY define:

- the ATON concept taxonomy
- the normative predicate catalogue
- ontology serialization
- predicate namespaces
- semantic versioning of predicates
- reasoning and inference rules
- provenance of derived knowledge
- ontology evolution and compatibility

## References

- RFC-0025 Canonical Relation Model

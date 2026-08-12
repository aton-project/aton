# RFC-0026 — Ontological Predicates

## Status

Draft

## Summary

This RFC specifies the semantic model for predicates within the ATON
Engineering Knowledge Model.

RFC-0025 defines the canonical technical representation of relations inside
the ATON kernel.

This RFC defines the semantic meaning and validity of those relations.

A Predicate SHALL represent a defined semantic relationship between two
Engineering Knowledge concepts.

## Scope

This RFC specifies:

- the concept of an ontological Predicate;
- Predicate identity;
- Predicate semantics;
- semantic source and target constraints;
- Predicate direction;
- inverse Predicates;
- cardinality semantics;
- semantic validation requirements; and
- the separation between explicit and derived relations.

The implementation of inference and reasoning is outside the scope of this
RFC.

The canonical representation of semantic constraints is defined separately by
RFC-0029.

## Ontological Predicate

An ontological Predicate defines a semantic relationship between a source
concept and a target concept.

A Predicate SHALL have a defined semantic meaning.

A Predicate MUST NOT be interpreted merely as an arbitrary string.

For example:

    Note
      |
      | motivates
      v
      ADR

The Predicate `motivates` expresses a specific engineering relationship.

## Predicate Identity

Each Predicate SHALL have a stable identifier.

The identifier SHALL uniquely identify the Predicate within the ATON ontology.

Predicate identifiers SHOULD use a concise, human-readable form.

Examples include:

- `motivates`
- `specifiedBy`
- `implements`
- `verifies`
- `governs`
- `defines`
- `allocates`
- `refines`
- `specializes`
- `references`

The identifier alone does not define the complete semantics of a Predicate.

The ontology definition SHALL provide the complete Predicate specification.

## Predicate Semantics

Every Predicate SHALL define its intended meaning.

The meaning SHALL be expressed independently of any particular serialization
format.

For example, `motivates` may be defined as:

> A Note provides rationale, observation, or an identified problem that
> contributes to an architectural decision.

The semantic definition SHALL be authoritative for interpretation of the
Predicate.

## Source Constraints

A Predicate MAY define the concept types that may act as its source.

For example:

    predicate: motivates

    permitted source:
      - Note

This means that `motivates` MAY originate from a Note.

An Engineering Knowledge object that is not compatible with the defined source
concept SHALL NOT use the Predicate in that role.

## Target Constraints

A Predicate MAY define the concept types that may act as its target.

For example:

    predicate: motivates

    permitted source:
      - Note

    permitted target:
      - ADR

This defines the valid direction:

    Note -> ADR

The reverse direction SHALL NOT be assumed to be valid.

## Predicate Direction

Predicates SHALL be directional unless their semantic definition explicitly
establishes symmetric semantics.

The source and target concepts are part of the semantic meaning of a
Predicate.

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

A Predicate MAY define an inverse Predicate.

For example:

    motivates
    inverse: motivatedBy

This establishes two semantically related Predicates:

    Note -> motivates -> ADR

    ADR -> motivatedBy -> Note

An inverse Predicate SHALL NOT be inferred merely from naming conventions.

The ontology SHALL explicitly define inverse relationships.

An inverse Predicate is a semantic relationship between Predicate definitions.
It does not imply that the inverse relation is physically stored as a
separate relation.

## Cardinality

A Predicate MAY define cardinality constraints.

Cardinality SHALL describe the permitted number of target relations for a
given source under the applicable semantic constraint model.

Examples include:

- `0..1`
- `0..*`
- `1..1`
- `1..*`

Cardinality constraints SHALL be interpreted by the ontology validation
layer.

A missing cardinality definition SHALL mean that no cardinality constraint is
defined by this RFC for that Predicate.

The canonical representation of cardinality constraints is defined by
RFC-0029.

## Predicate Specification

A canonical Predicate definition SHOULD contain at least:

- an identifier;
- a semantic description; and
- its applicable semantic constraints.

Applicable semantic constraints MAY define:

- permitted source concepts;
- permitted target concepts;
- permitted source-to-target concept pairs;
- cardinality;
- inverse Predicates;
- symmetry;
- transitivity; or
- other semantic properties defined by the ontology.

For example, a Predicate MAY be semantically defined as:

    id: motivates

    description:
      A Note provides rationale or an identified problem for an ADR.

    permitted source:
      Note

    permitted target:
      ADR

    inverse:
      motivatedBy

    cardinality:
      0..*

The example describes the semantic properties of the Predicate. It does not
define the canonical physical serialization of those properties.

The canonical representation and validation model for semantic constraints is
defined by RFC-0029.

The exact serialization format for ontology definitions is outside the scope
of this RFC.

## Semantic Validation

The verification subsystem SHALL be able to validate relations against the
ontology.

At minimum, semantic validation SHALL be capable of determining:

- whether the Predicate exists;
- whether the source concept is permitted;
- whether the target concept is permitted;
- whether the relation direction is valid; and
- whether cardinality constraints are satisfied when defined.

A relation that violates an ontology constraint SHALL be reported as a
verification issue.

Semantic validation SHALL operate on the canonical Relation model defined by
RFC-0025 and the applicable semantic constraints defined by RFC-0029.

## Explicit Relations

An explicit relation is a relation directly represented in the Foundation.

For example:

    NOTE-0020
        |
        | motivates
        v
    ADR-0008

The relation is explicitly stored by the author.

Explicit relations form authoritative source data of the Engineering Knowledge
Model.

## Derived Relations

A derived relation is a relation that can be generated from explicitly defined
relations and ontology rules.

Derived relations SHALL NOT be treated as independently authored source data.

For example, if the ontology defines:

    motivates
    inverse: motivatedBy

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

Inference SHALL NOT be considered part of the initial Predicate validation
defined by this RFC.

Future specifications MAY define:

- inference rules;
- transitive reasoning;
- rule composition;
- derived knowledge lifecycle; and
- provenance of inferred knowledge.

## Ontology Constraints

A Predicate MAY define semantic constraints that restrict its valid use.

Such constraints MAY define:

- permitted source concepts;
- permitted target concepts;
- permitted source-to-target concept pairs;
- cardinality;
- inverse Predicates;
- symmetry;
- transitivity; or
- other semantic properties defined by the ontology.

The semantic definition of a Predicate and the constraints applicable to that
Predicate are distinct concerns.

RFC-0029 defines the canonical semantic constraint model used to represent
and validate such constraints.

This RFC defines the semantic role and meaning of Predicates but does not
replace the canonical constraint model defined by RFC-0029.

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
    Semantic Constraint Model
            |
            v
    Semantic Validation
            |
            v
    Future Reasoning

RFC-0025 defines the canonical relation representation.

This RFC defines the semantic meaning and role of ontological Predicates.

RFC-0029 defines the canonical semantic constraint model applicable to
Predicates and relations.

Future specifications MAY define reasoning and inference.

## Consequences

The ontological Predicate model provides:

- semantically meaningful relations;
- explicit source and target constraints;
- machine-verifiable relationship semantics;
- separation between technical representation and domain meaning;
- a foundation for ontology-based verification; and
- a foundation for future knowledge graph reasoning.

It prevents generic structural relationships from becoming an uncontrolled
part of the ATON knowledge model.

## Design Principle

ATON SHALL prefer semantically meaningful Predicates over generic structural
relationships.

Generic relationships such as:

- `parent`;
- `child`; and
- `related`

SHOULD NOT be introduced when a domain-specific semantic Predicate can
express the intended relationship.

## Future Extensions

Future specifications MAY define:

- the ATON concept taxonomy;
- the normative Predicate catalogue;
- ontology serialization;
- Predicate namespaces;
- semantic versioning of Predicates;
- reasoning and inference rules;
- provenance of derived knowledge; and
- ontology evolution and compatibility.

## References

- RFC-0025 — Canonical Relation Model
- RFC-0029 — Semantic Relation Constraints
- ADR-0014 — Canonical Semantic Relation Model

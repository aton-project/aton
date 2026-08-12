# RFC-0029 — Canonical Semantic Relation Constraint Model

## Status

Proposed

## Abstract

This RFC defines the canonical semantic constraint model for ATON
relation predicates.

The model extends the structural relation model defined by RFC-0025
with ontology-level constraints that determine which source and target
Concept combinations are semantically valid for a relation predicate.

RFC-0027 defines the ATON ontology and its normative source-to-target
Concept pairs.

The purpose of this RFC is to define the canonical representation and
verification semantics required to evaluate those constraints
deterministically.

## Motivation

RFC-0025 defines the canonical structural representation of a relation.

A Relation instance consists of:

- a predicate;
- a target.

The source is provided by the Entity that owns the relation.

This representation is structurally sufficient but does not determine
whether the combination of source Concept, predicate and target Concept
is semantically valid.

RFC-0027 therefore establishes that Predicate applicability SHALL be
defined by explicit allowed source-to-target Concept pairs.

This RFC defines the canonical constraint model required to implement
that decision.

## Design Principle

Semantic relation validity SHALL be evaluated using the following model:

    Source Concept -- Predicate --> Target Concept

A Predicate therefore defines an explicit set of permitted source-to-
target Concept pairs.

The pair itself is normative.

A Predicate SHALL NOT be represented merely by independent source and
target sets whose Cartesian product implicitly defines valid
combinations.

## Terminology

### Predicate

A named semantic relation type.

Examples include:

- motivates;
- references;
- refines;
- dependsOn.

### Concept

A semantic category defined by the ATON ontology.

The initial Concept vocabulary is defined by RFC-0027.

### Allowed Pair

A pair consisting of:

- one permitted source Concept;
- one permitted target Concept.

An Allowed Pair defines one valid source-to-target combination for a
Predicate.

### Constraint

The semantic applicability definition associated with a Predicate.

### Relation Instance

A concrete occurrence of a Predicate between a source Entity and a
target Entity.

## Canonical Constraint Model

Each normative Predicate SHALL have a semantic constraint definition.

The canonical conceptual representation is:

    predicate:
      allowedPairs:
        - source: `<source-concept>`
          target: `<target-concept>`

Each entry in `allowedPairs` SHALL define exactly one permitted
source-to-target Concept combination.

A Predicate MAY define multiple allowed pairs.

A Predicate with no allowed pair SHALL NOT be considered semantically
applicable to any source-to-target Concept combination.

## Explicit Pair Semantics

The allowed source-to-target pairs SHALL be evaluated exactly as
defined.

For example:

    predicate: motivates

    allowedPairs:
      - source: Note
        target: ADR
      - source: Finding
        target: ADR

The following relations are therefore valid:

    Note -> motivates -> ADR
    Finding -> motivates -> ADR

The following relations are invalid:

    Note -> motivates -> Decision
    Finding -> motivates -> Note
    Decision -> motivates -> ADR

The existence of a Concept in either position does not make an
otherwise undefined combination valid.

## No Cartesian Product Semantics

A Predicate SHALL NOT interpret its constraints as independent domain
and range sets.

For example, the following conceptual model is NOT canonical:

    predicate: motivates

    domain:
      - Note
      - Finding

    range:
      - ADR

Such a representation is ambiguous because it relies on implicit
combination semantics.

The canonical model explicitly represents:

    Note -> ADR
    Finding -> ADR

This preserves the exact semantics defined by RFC-0027.

## Concept Identity

Allowed pair entries SHALL reference canonical ontology Concept
identifiers.

For ontology Concepts represented as Foundation ontology artifacts,
the canonical identifiers are their ontology artifact IDs, for example:

    ONT-ADR
    ONT-RFC
    ONT-Requirement
    ONT-Component

Human-readable Concept titles and Markdown headings SHALL NOT be used
as semantic identifiers.

RFC-0027 may use Concept names such as `ADR`, `RFC`, `Requirement` and
`Component` in explanatory text. Such names SHALL be interpreted as the
corresponding canonical ontology Concepts.

Concepts defined by RFC-0027 but not yet represented by Foundation
ontology artifacts SHALL NOT be used by semantic verification until
their canonical ontology definitions exist.

## Relation Evaluation

For a concrete relation:

    S --P--> T

the semantic verifier SHALL perform the following evaluation:

1. Resolve the source Entity.
2. Resolve the source Concept.
3. Resolve the relation Predicate.
4. Resolve the Predicate semantic constraint.
5. Resolve the target Entity.
6. Resolve the target Concept.
7. Construct the pair:

       source Concept + target Concept

8. Verify that the exact pair is contained in the Predicate's
   `allowedPairs`.

The relation is semantically valid only when the exact pair exists.

## Unknown Predicate

A relation whose Predicate has no semantic constraint definition SHALL
be treated as semantically undefined.

The verifier SHALL NOT infer semantic validity merely from the existence
of the Predicate string.

The initial implementation SHOULD report an undefined Predicate as a
warning during migration.

Once semantic constraints are mandatory, an undefined Predicate SHALL
be reported as an error.

## Unknown Source Concept

If the source Entity cannot be resolved to a canonical ontology
Concept, semantic verification SHALL report the condition.

The verifier SHALL NOT assume that an unknown source Concept satisfies
an Allowed Pair.

## Unknown Target Concept

If the target Entity cannot be resolved to a canonical ontology
Concept, semantic verification SHALL report the condition unless the
relation target is explicitly classified as an external entity.

External entity handling remains subject to the existing relation model
and ontology rules.

## Source Concept Violation

If the source Concept does not participate in any Allowed Pair for the
given Predicate, the relation SHALL be considered semantically invalid.

Example:

    motivates:
      allowedPairs:
        - source: ONT-Note
          target: ONT-ADR

Given:

    ONT-Decision --motivates--> ONT-ADR

the relation is invalid because `ONT-Decision` is not an allowed source
Concept for `motivates`.

## Target Concept Violation

If the target Concept does not form an Allowed Pair with the resolved
source Concept for the given Predicate, the relation SHALL be
considered semantically invalid.

Example:

    motivates:
      allowedPairs:
        - source: ONT-Finding
          target: ONT-ADR

Given:

    ONT-Finding --motivates--> ONT-Note

the relation is invalid because the exact pair
`ONT-Finding -> ONT-Note` is not defined.

## Exact Pair Matching

Semantic validation SHALL use exact Concept matching.

A relation SHALL NOT become valid because:

- the source Concept is related to an allowed Concept;
- the target Concept is related to an allowed Concept;
- the source Concept specializes an allowed Concept;
- the target Concept specializes an allowed Concept.

Such behavior requires explicit ontology hierarchy semantics and is
outside the scope of this RFC.

## Type Specialization

RFC-0027 defines Concept specialization as taxonomy.

Concept specialization SHALL NOT automatically expand Predicate
applicability.

For example, if:

    ONT-ADR specializes ONT-Decision

and:

    ONT-Note -> motivates -> ONT-ADR

is valid, this SHALL NOT automatically make:

    ONT-Note -> motivates -> ONT-Decision

valid.

The corresponding pair MUST be explicitly defined if it is intended to
be valid.

## Structural and Semantic Verification

The verification subsystem SHALL maintain a clear separation between structural
and semantic verification.

Structural verification includes at least:

- duplicate artifact IDs;
- missing content;
- missing titles;
- unknown relation targets;
- duplicate relations; and
- self references.

Semantic verification includes at least:

- unknown Predicates;
- unknown source Concepts;
- unknown target Concepts;
- invalid source-to-target Concept pairs; and
- violations of applicable semantic constraints.

A Relation MAY therefore pass structural verification while failing semantic
verification.

## Ontology Authority

The ontology SHALL be the authoritative source for Predicate semantic
constraints.

Individual Relation instances SHALL NOT redefine the semantic constraints of
their Predicate.

A Relation instance continues to contain only the structural relation
information defined by RFC-0025.

This prevents different instances of the same Predicate from acquiring
inconsistent semantic definitions.

## Separation from the Relation Model

The canonical Relation model defined by RFC-0025 SHALL remain unchanged at the
conceptual level.

A Relation instance continues to represent:

    predicate + target

Semantic constraints belong to the ontology and SHALL be resolved during
semantic verification.

The verifier MAY construct an internal semantic representation while
processing a Relation.

Such information SHALL NOT be duplicated into every Relation instance.

## Serialization

The semantic constraint model SHALL be serializable independently of individual
Relation instances.

The canonical conceptual serialization is:

    predicate: motivates
    allowedPairs:
      - source: ONT-Note
        target: ONT-ADR
      - source: ONT-Finding
        target: ONT-ADR

The exact file location and surrounding ontology artifact structure are
implementation concerns and SHALL NOT alter the semantic meaning of the model.

## Cardinality Constraints

A Predicate MAY define cardinality constraints.

Cardinality SHALL describe the permitted number of target Relations for a
given source and Predicate.

Examples include:

- `0..1`;
- `0..*`;
- `1..1`; and
- `1..*`.

Cardinality constraints SHALL be represented and validated according to the
canonical semantic constraint model defined by this RFC.

Cardinality SHALL be evaluated only after the source-to-target Concept pair
has been established as semantically valid.

A Relation that does not satisfy the applicable cardinality constraint SHALL
produce a semantic verification issue.

A missing cardinality constraint SHALL NOT imply an implicit cardinality
restriction.

Cardinality SHALL apply to the set of Relations sharing the same source and
Predicate within the applicable semantic scope.

## Verification Algorithm

The semantic verification algorithm SHALL conceptually implement:

    for each relation:
        resolve source Entity
        resolve source Concept
        resolve Predicate constraint
        resolve target Entity
        resolve target Concept

        pair = (source Concept, target Concept)

        verify pair ∈ allowedPairs

        evaluate applicable cardinality constraints

For each applicable source and Predicate combination, the verifier SHALL
evaluate the cardinality constraint against the complete set of Relations
sharing that source and Predicate within the applicable semantic scope.

A failure of the pair membership test SHALL produce a semantic verification
issue.

Cardinality SHALL NOT be evaluated as satisfied merely because the individual
Relation contains a valid source-to-target Concept pair.

The verifier SHALL identify:

- the source artifact;
- the Predicate;
- the target artifact;
- the resolved source Concept;
- the resolved target Concept; and
- the violated semantic constraint.

## Error Reporting

Semantic verification issues SHALL use explicit verification rule
identifiers.

The implementation SHOULD provide rules corresponding to at least:

- `unknown-relation-predicate`;
- `unknown-source-concept`;
- `unknown-target-concept`;
- `relation-concept-pair-violation`; and
- `relation-cardinality-violation`.

The exact reporting format SHALL follow the existing `VerificationReport`
model.

## Migration Strategy

Existing Relations SHALL remain valid structural artifacts during migration.

Semantic verification SHALL initially operate in migration-compatible mode.

Predicates without defined semantic constraints SHOULD produce warnings rather
than immediately invalidating the Foundation.

Once all required Predicates have semantic constraints, the project MAY
promote missing semantic definitions from warnings to errors.

Existing semantic violations SHALL be corrected by changing the affected
engineering artifacts or by changing the ontology definition through the
normal ATON governance process.

The verifier SHALL NOT silently modify engineering artifacts.

## Example

Assume the ontology defines:

    predicate: motivates
    allowedPairs:
      - source: ONT-Note
        target: ONT-ADR
      - source: ONT-Finding
        target: ONT-ADR

and the Foundation contains:

    NOTE-0020
        concept: ONT-Note

    ADR-0008
        concept: ONT-ADR

The Relation:

    NOTE-0020 --motivates--> ADR-0008

is semantically valid.

If the Foundation contains:

    ADR-0009
        concept: ONT-ADR

then:

    ADR-0009 --motivates--> ADR-0008

is semantically invalid because:

    ONT-ADR -> ONT-ADR

is not an Allowed Pair for `motivates`.

Likewise, if the Foundation contains:

    DECISION-0001
        concept: ONT-Decision

then:

    DECISION-0001 --motivates--> ADR-0008

is semantically invalid because:

    ONT-Decision -> ONT-ADR

is not an Allowed Pair for `motivates`.

## Compatibility

This RFC SHALL preserve compatibility with the canonical Relation model
defined by RFC-0025.

Existing structural Relations remain representable.

Semantic constraints are an additional ontology-level layer.

No existing Relation instance needs to contain an `allowedPairs` definition.

## Implementation Boundary

The following are in scope:

- canonical Predicate constraints;
- explicit source-to-target Concept pairs;
- semantic Relation verification;
- cardinality constraints;
- semantic verification reporting;
- migration-compatible handling of undefined Predicates; and
- canonical ontology Concept identity.

The following are out of scope:

- type inheritance;
- automatic Predicate inheritance;
- inverse Relation generation;
- transitivity;
- symmetry;
- property chains;
- reasoning over Relation graphs;
- inference; and
- automatic Relation repair.

These capabilities require separate architectural decisions or RFCs.

## Acceptance Criteria

The implementation of this RFC SHALL satisfy at least the following:

1. A Predicate can define one or more explicit allowed source-to-target
   Concept pairs.
2. A concrete Relation can be evaluated against those pairs.
3. Invalid source-to-target Concept combinations are detected.
4. Undefined Predicates can be reported.
5. Unknown source Concepts can be reported.
6. Unknown target Concepts can be reported.
7. Structural Relation validation remains independent of semantic validation.
8. Existing Relation instances do not contain duplicated semantic constraint
   definitions.
9. Verification issues identify the affected artifact and rule.
10. Concept specialization does not implicitly expand Predicate applicability.
11. Existing Foundation artifacts remain structurally loadable during
    migration.
12. The semantic model does not rely on an implicit Cartesian product of
    source and target Concept sets.
13. Cardinality constraints can be evaluated independently of
    source-to-target Concept validity.
14. Cardinality violations can be reported as semantic verification issues.

## References

- RFC-0025 — Canonical Relation Model
- RFC-0026 — Ontological Predicates
- RFC-0027 — ATON Ontology
- ADR-0009 — Semantic Constraints for Relations
- NOTE-0021 — Semantic Constraints for Relations
- ENTITY-0001 — Universal Entity Model

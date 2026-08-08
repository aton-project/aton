# RFC-0029 Canonical Semantic Relation Constraint Model

## Status

Proposed

## Abstract

This RFC defines the canonical semantic constraint model for ATON
relation predicates.

The model extends the structural relation model defined by RFC-0025
with ontology-level constraints that determine which source and target
types are semantically valid for a relation predicate.

The purpose of this RFC is to provide a deterministic foundation for
semantic relation verification without coupling semantic constraints
to individual Relation instances.

## Motivation

RFC-0025 defines the canonical structural representation of a relation.

A relation is represented by:

- a predicate;
- a target.

The source is provided by the Entity that owns the relation.

This representation is structurally sufficient but does not determine
whether the combination of source type, predicate and target type is
semantically valid.

ADR-0009 therefore establishes that relation predicates SHALL have
ontology-defined semantic constraints.

This RFC defines the canonical model required to implement that decision.

## Design Principle

Semantic relation validity SHALL be evaluated using the following model:

    Source Type -- Predicate --> Target Type

A predicate therefore defines a semantic contract consisting of:

- a domain;
- a range.

The domain defines permitted source types.

The range defines permitted target types.

A concrete relation is semantically valid only if both its source and
target satisfy the corresponding predicate constraints.

## Terminology

### Predicate

A named semantic relation type.

Examples include:

- motivates;
- references;
- refines;
- dependsOn.

### Domain

The set of ontology types that may act as the source of a predicate.

### Range

The set of ontology types that may act as the target of a predicate.

### Constraint

A semantic restriction associated with a predicate.

### Relation Instance

A concrete occurrence of a predicate between a source Entity and a
target Entity.

## Canonical Constraint Model

Each relation predicate SHALL have a semantic constraint definition.

The conceptual representation is:

    predicate:
      domain:
        - `<source-type>`
      range:
        - `<target-type>`

The domain SHALL contain one or more ontology type identifiers.

The range SHALL contain one or more ontology type identifiers.

A predicate SHALL NOT have an undefined semantic domain or range once it
is subject to semantic verification.

## Multiple Allowed Types

A predicate MAY permit multiple source types.

For example:

    predicate: motivates

    domain:
      - Finding
      - Observation

    range:
      - Note

This means that both of the following source types are permitted:

    Finding
    Observation

The same applies to the range.

A predicate MAY therefore define multiple allowed target types.

## Relation Evaluation

For a concrete relation:

    S --P--> T

the semantic verifier SHALL perform the following evaluation:

1. Resolve the source Entity.
2. Resolve the source Entity type.
3. Resolve the relation predicate.
4. Resolve the predicate semantic constraint.
5. Resolve the target Entity.
6. Resolve the target Entity type.
7. Verify that the source type is permitted by the predicate domain.
8. Verify that the target type is permitted by the predicate range.

The relation is semantically valid only when all required resolutions
succeed and both domain and range constraints are satisfied.

## Unknown Predicate

A relation whose predicate has no semantic constraint definition SHALL
be treated as semantically undefined.

The verifier SHALL NOT infer semantic validity merely from the existence
of the predicate string.

The exact verification severity for an undefined predicate SHALL be
defined by the implementation policy.

The initial implementation SHOULD report the condition as a warning
during migration and SHALL support escalation to an error once semantic
constraints become mandatory.

## Unknown Source Type

If the source Entity cannot be resolved to an ontology type, semantic
verification SHALL report the condition.

The verifier SHALL NOT assume that an unknown source type satisfies the
predicate domain.

## Unknown Target Type

If the target Entity cannot be resolved to an ontology type, semantic
verification SHALL report the condition unless the relation target is
explicitly classified as an external entity.

External entity handling remains subject to the existing relation model
and ontology rules.

## Domain Violation

If the source Entity type is not contained in the predicate domain, the
relation SHALL be considered semantically invalid.

Example:

    motivates:
      domain:
        - Finding
      range:
        - Note

Given:

    Note --motivates--> Note

the relation is structurally representable but semantically invalid.

## Range Violation

If the target Entity type is not contained in the predicate range, the
relation SHALL be considered semantically invalid.

Example:

    motivates:
      domain:
        - Finding
      range:
        - Note

Given:

    Finding --motivates--> Decision

the relation is structurally representable but semantically invalid.

## Structural and Semantic Verification

The renderer SHALL maintain a clear separation between structural and
semantic verification.

Structural verification includes at least:

- duplicate artifact IDs;
- missing content;
- missing titles;
- unknown relation targets;
- duplicate relations;
- self references.

Semantic verification includes at least:

- unknown predicates;
- unknown source types;
- unknown target types;
- domain violations;
- range violations.

A relation MAY therefore pass structural verification while failing
semantic verification.

## Ontology Authority

The ontology SHALL be the authoritative source for predicate semantic
constraints.

Individual relation instances SHALL NOT redefine their predicate's
domain or range.

This prevents different instances of the same predicate from acquiring
inconsistent semantic definitions.

## Separation from the Relation Model

The canonical Relation model defined by RFC-0025 SHALL remain unchanged
by this RFC at the conceptual level.

A Relation instance continues to represent:

    predicate + target

Semantic constraints belong to the ontology and are resolved during
semantic verification.

The verifier MAY construct an internal semantic representation during
processing, but such information SHALL NOT become duplicated into every
Relation instance.

## Type Identity

Domain and range entries SHALL reference canonical ontology type
identifiers.

They SHALL NOT depend on:

- display titles;
- Markdown headings;
- file paths;
- human-readable descriptions.

This ensures that semantic validation remains stable when presentation
information changes.

## Type Specialization

The initial implementation SHALL support exact type matching.

For example:

    domain:
      - Entity

A source of type `Entity` satisfies the constraint.

A source of a specialized type SHALL NOT automatically satisfy the
constraint until ontology type specialization and inheritance rules have
been explicitly defined.

Future RFCs MAY introduce type hierarchy semantics.

## Cardinality

This RFC defines domain and range constraints only.

It does not define:

- minimum relation counts;
- maximum relation counts;
- mandatory relations;
- uniqueness beyond duplicate relation detection.

Cardinality constraints MAY be introduced by a future RFC.

## Inverse Relations

This RFC does not require inverse predicate definitions.

For example:

    refines
    refinedBy

may exist as independent predicates.

An explicit inverse relation model MAY be introduced separately.

## Serialization

The semantic constraint model SHALL be serializable independently of
individual relation instances.

The canonical serialization format SHALL be defined by the ontology
artifact model and implementation.

The following conceptual representation is normative:

    predicate:
      domain:
        - TypeA
        - TypeB
      range:
        - TypeC
        - TypeD

The exact file location and artifact type are implementation concerns
and SHALL not alter the semantic meaning of the model.

## Verification Algorithm

The semantic verification algorithm SHALL conceptually implement:

    for each relation:
        resolve source
        resolve predicate constraint
        resolve target

        verify source type ∈ domain
        verify target type ∈ range

A failure of either membership test SHALL produce a semantic
verification issue.

The verifier SHALL identify:

- the source artifact;
- the predicate;
- the target artifact;
- the violated constraint.

## Error Reporting

Semantic verification issues SHALL use explicit verification rule
identifiers.

The implementation SHOULD provide rules corresponding to at least:

    unknown-relation-predicate
    unknown-source-type
    unknown-target-type
    relation-domain-violation
    relation-range-violation

The exact reporting format SHALL follow the existing
VerificationReport model.

## Migration Strategy

Existing relations SHALL remain valid structural artifacts during
migration.

Semantic verification SHALL initially operate in migration-compatible
mode.

Predicates without defined constraints SHOULD produce warnings rather
than immediately invalidating the Foundation.

Once all required predicates have semantic constraints, the project MAY
promote missing semantic definitions from warnings to errors.

Existing semantic violations SHALL be corrected by changing the affected
engineering artifacts or by changing the ontology definition through the
normal ATON governance process.

The verifier SHALL NOT silently modify engineering artifacts.

## Example

Assume the ontology defines:

    motivates:
      domain:
        - Finding
      range:
        - Note

and the Foundation contains:

    FINDING-0001
    type: Finding

    NOTE-0001
    type: Note

The relation:

    FINDING-0001 --motivates--> NOTE-0001

is semantically valid.

If the Foundation contains:

    DECISION-0001
    type: Decision

then:

    DECISION-0001 --motivates--> NOTE-0001

is semantically invalid because `Decision` is not in the domain of
`motivates`.

Likewise:

    FINDING-0001 --motivates--> DECISION-0001

is semantically invalid because `Decision` is not in the range of
`motivates`.

## Compatibility

This RFC SHALL preserve compatibility with the canonical Relation model
defined by RFC-0025.

Existing structural relations remain representable.

Semantic constraints are an additional ontology-level layer.

No existing Relation instance needs to contain a domain or range
definition.

## Implementation Boundary

The following are in scope:

- canonical predicate constraints;
- domain constraints;
- range constraints;
- semantic relation verification;
- semantic verification reporting;
- migration-compatible handling of undefined predicates.

The following are out of scope:

- type inheritance;
- cardinality;
- inverse relations;
- transitivity;
- symmetry;
- property chains;
- reasoning over relation graphs;
- automatic relation repair.

These capabilities require separate architectural decisions or RFCs.

## Acceptance Criteria

The implementation of this RFC SHALL satisfy at least the following:

1. A predicate can define one or more allowed source types.
2. A predicate can define one or more allowed target types.
3. A concrete relation can be evaluated against these constraints.
4. Domain violations are detected.
5. Range violations are detected.
6. Undefined predicates can be reported.
7. Structural relation validation remains independent of semantic
   validation.
8. Existing Relation instances do not contain duplicated semantic
   constraint definitions.
9. Verification issues identify the affected artifact and rule.
10. Existing Foundation artifacts remain structurally loadable during
    migration.

## References

- ADR-0009 Semantic Constraints for Relations
- NOTE-0021 Semantic Constraints for Relations
- RFC-0025 Canonical Relation Model
- ENTITY-0001 Universal Entity Model

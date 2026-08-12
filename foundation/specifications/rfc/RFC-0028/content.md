# RFC-0028 Relation Migration and Legacy Predicate Resolution

## Status

Draft

## Summary

This RFC defines the migration strategy for existing ATON relations and the
resolution of legacy relation predicates.

RFC-0025 defines the canonical Relation Model.

RFC-0026 defines the general model for ontological Predicates.

RFC-0027 defines the ATON ontology and its normative Predicate vocabulary.

Existing Foundation artifacts may contain relations that predate the
canonical ontology.

Those relations SHALL NOT be assigned new semantic meaning automatically.

A relation whose intended semantics are not established SHALL remain
unresolved until an explicit architectural or specification decision defines
its meaning.

## Scope

This RFC specifies:

- classification of existing relation predicates
- migration states
- canonical Predicate adoption
- legacy Predicate handling
- unresolved relations
- external relation targets
- semantic migration
- verification behavior during migration
- migration completion criteria

This RFC does not define new domain semantics for unresolved relations.

## Migration Principle

Migration SHALL preserve meaning.

A relation SHALL NOT be migrated from a legacy Predicate to a canonical
Predicate merely because the names appear similar.

For example:

    children

MUST NOT automatically become:

    refines

or:

    specializes

without an explicit semantic decision.

The same rule applies to:

    related
    relatedTo
    parent
    child

and any other generic or legacy relationship.

## Migration States

Every existing relation predicate SHALL be classified into one of the
following states:

    canonical
    inverse
    deprecated
    unresolved

### Canonical

A canonical Predicate is defined by the ATON ontology and may be used by
normative Foundation artifacts.

Examples:

    references
    refines
    specializes
    governs

### Inverse

An inverse Predicate is the explicitly defined directional inverse of a
canonical Predicate.

Examples:

    references
        inverse:
            referencedBy

    refines
        inverse:
            refinedBy

The inverse SHALL have explicit ontology semantics.

### Deprecated

A deprecated Predicate is known to be obsolete but its semantics are
sufficiently understood to permit controlled migration.

Deprecated Predicates SHOULD NOT be introduced in new Foundation artifacts.

Existing uses SHALL be migrated according to an explicit migration decision.

### Unresolved

An unresolved Predicate is a relation whose intended semantic meaning has not
yet been established.

An unresolved Predicate SHALL NOT be automatically mapped to a canonical
Predicate.

Unresolved relations SHALL remain distinguishable from valid canonical
relations.

## Initial Legacy Classification

The following classification applies to the currently observed Foundation
relations.

### references

Status:

    canonical

The Predicate is retained as defined by RFC-0027.

### referenced-by

Status:

    deprecated

The canonical inverse Predicate SHALL be:

    referencedBy

Existing `referenced-by` relations SHALL be migrated only by changing the
Predicate identifier, provided that their source and target semantics match
the inverse relation defined by the ontology.

### dependsOn

Status:

    unresolved

The semantic meaning of existing `dependsOn` relations has not been
established by the current ATON ontology.

RFC-0027 does not define `dependsOn` as a canonical Predicate.

Existing `dependsOn` relations SHALL therefore remain unresolved until an
explicit ontology decision defines their semantics and allowed source-to-target
Concept pairs.

The existence of `dependsOn` relations SHALL NOT be interpreted as evidence
that `dependsOn` is a canonical Predicate.

### refines

Status:

    canonical

The Predicate is retained as defined by RFC-0027.

### specializes

Status:

    canonical

The Predicate is retained as defined by RFC-0027.

### governs

Status:

    canonical

The Predicate is retained as defined by RFC-0027.

### children

Status:

    unresolved

The semantic meaning of existing `children` relations SHALL NOT be inferred.

Possible interpretations MAY include:

    refines
    specializes
    supersedes
    contains

but none of these interpretations is authoritative until explicitly
decided.

### related

Status:

    unresolved

The semantic meaning of existing `related` relations SHALL NOT be inferred.

The generic term does not provide sufficient semantic information to determine
the intended engineering relationship.

### relatedTo

Status:

    unresolved

The semantic meaning of existing `relatedTo` relations SHALL NOT be inferred.

The generic term does not provide sufficient semantic information to
determine the intended engineering relationship.

## No Automatic Semantic Migration

The migration process SHALL distinguish between syntactic normalization and
semantic migration.

Syntactic normalization changes representation without changing meaning.

Example:

    referenced-by
        ->
    referencedBy

Semantic migration changes the meaning or ontology classification of a
relation.

Example:

    children
        ->
    refines

Semantic migration SHALL require an explicit decision.

## Migration Decision

A migration decision SHALL establish:

    legacy Predicate
    source Concept
    target Concept
    canonical Predicate
    semantic justification

For example:

    legacy:
        children

    source:
        ADR

    target:
        ADR

    canonical:
        refines

    justification:
        The original relation explicitly represents a decision refining
        another decision.

Only after such a decision is established MAY the relation be migrated.

## Source and Target Validation

A migration SHALL validate the complete source-to-target Concept pair
according to the semantic constraint model defined by RFC-0029.

A Predicate SHALL NOT be considered valid merely because its source Concept
and target Concept are individually permitted.

The exact pair SHALL be permitted by the ontology.

For example:

    Note -> motivates -> ADR

may be valid.

The following relation is not automatically valid:

    Note -> motivates -> Decision

unless that exact pair is defined by the ontology.

## External Targets

A relation target MAY refer to an Entity that is not an ATON Foundation
artifact.

Examples include:

    ietf:rfc:2119
    foundation

Such targets SHALL be represented as explicit non-artifact Entities in the
canonical relation model.

An external target SHALL NOT be reported as an unknown artifact merely because
it does not exist in the Foundation artifact repository.

The exact representation of external Entities is defined by the canonical
model and future ontology specifications.

## Migration of External References

Existing external references SHALL be preserved during migration.

For example:

    RFC-0000 -> references -> ietf:rfc:2119

SHALL retain its semantic target.

The migration process SHALL NOT attempt to create a local Foundation artifact
for an external Entity unless explicitly required.

## Verification During Migration

The verification system SHALL distinguish at least the following conditions:

    valid
    unresolved
    deprecated
    invalid
    unknown

### Valid

The relation uses a canonical Predicate and satisfies its applicable ontology
constraints as defined by RFC-0027 and represented according to RFC-0029.

### Unresolved

The relation uses a Predicate whose semantic meaning has not yet been
resolved.

An unresolved relation SHALL be reported separately from an invalid relation.

### Deprecated

The relation uses a Predicate that is understood but no longer permitted for
new use.

Deprecated relations SHOULD produce a verification warning.

### Invalid

The Predicate is known, but the relation violates an ontology constraint.

Examples include:

    invalid source Concept
    invalid target Concept
    invalid source-to-target pair

Invalid relations SHALL produce a verification error.

### Unknown

The relation uses a Predicate that is not known to the ontology or migration
registry.

Unknown Predicates SHALL produce a verification error.

## Migration Order

Migration SHALL proceed in the following order:

    1. Inventory existing relations
    2. Classify Predicates
    3. Resolve semantics
    4. Define canonical Predicate mapping
    5. Validate source-to-target pairs
    6. Migrate relation representations
    7. Verify the migrated Foundation
    8. Remove deprecated usage

No step SHALL implicitly perform a later step.

## Architecture Board Input

Unresolved relations SHALL be treated as architectural or semantic questions
when their meaning affects the ATON ontology.

The migration process SHALL NOT resolve such questions by implementation
convention.

Where necessary, an unresolved relation SHALL result in:

    observation
        ->
    Note
        ->
    Architecture Board decision
        ->
    ADR
        ->
    RFC or ontology update
        ->
    implementation

This preserves the distinction between identifying a problem and deciding
its solution.

## Existing Foundation Relations

The currently observed Foundation contains the following relation classes:

    children
    dependsOn
    governs
    referenced-by
    references
    refines
    related
    relatedTo
    specializes

The migration state defined by this RFC is:

    canonical:
        governs
        references
        refines
        specializes

    inverse:
        referencedBy

    deprecated:
        referenced-by

    unresolved:
        dependsOn
        children
        related
        relatedTo

This classification does not define the final semantic resolution of the
unresolved relations.

## Migration Safety

A migration SHALL NOT silently change the meaning of existing engineering
knowledge.

Before a semantic migration is performed:

- the affected relations SHALL be identified
- the target Predicate SHALL be identified
- the source and target Concepts SHALL be validated
- the semantic justification SHALL be recorded
- the resulting Foundation SHALL pass verification

## Rollback

A semantic migration SHOULD be reversible until the migration has been
accepted as part of the normative Foundation.

The migration process SHOULD preserve sufficient history to determine:

    original Predicate
    original source
    original target
    migration decision
    resulting Predicate

Git history provides the primary technical mechanism for preserving this
history.

## Completion Criteria

A relation migration is complete only when:

- every migrated relation uses a canonical Predicate
- every Predicate satisfies its ontology constraints
- every source-to-target pair is valid
- all deprecated usages have been removed or explicitly accepted
- no unresolved relation remains without an explicit disposition
- the Foundation verification succeeds

## Consequences

This migration model provides:

- preservation of existing semantics
- explicit handling of legacy relations
- controlled ontology evolution
- separation of syntactic and semantic migration
- deterministic verification
- protection against accidental semantic reinterpretation

It also means that some existing relations may remain unresolved for a period
of time.

That is intentional.

Uncertainty in the domain model SHALL be represented explicitly rather than
hidden by an implementation assumption.

## Future Extensions

Future RFCs MAY define:

- a machine-readable migration registry
- automated migration tooling
- ontology compatibility checks
- migration reports
- migration provenance
- external Entity serialization
- automated detection of semantic migration candidates

## References

- RFC-0025 — Canonical Relation Model
- RFC-0026 — Ontological Predicates
- RFC-0027 — ATON Ontology
- RFC-0029 — Semantic Relation Constraints

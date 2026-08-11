# Canonical Semantic Relation Model

## Context

Relations are a fundamental part of the ATON Engineering Knowledge Model.

They provide the semantic connections required for traceability, navigation,
impact analysis and engineering reasoning.

During implementation of the Foundation verification subsystem it became
apparent that relation information had previously been represented in
multiple persistence formats.

RFC-0029 established the need for canonical semantic constraints for
Predicates, while ADR-0008 established the principle that the kernel shall
operate on canonical domain models rather than persistence-specific
representations.

The existing Predicate validation implementation provides the first
enforcement mechanism for these semantic constraints.

A unified architectural definition of the canonical relation model is
therefore required.

## Problem Statement

A relation is not sufficiently defined by a predicate and a target alone.

The semantic validity of a relation depends on:

- its source;
- its predicate;
- its target;
- the semantic types of source and target;
- the definition of the predicate; and
- the constraints applicable to that predicate.

A structurally valid relation may therefore still be semantically invalid.

The Engineering Knowledge Model must distinguish structural relation
representation from semantic relation validity.

## Decision

ATON SHALL represent relations in the kernel as canonical domain objects.

A canonical Relation SHALL contain at least:

- a predicate;
- a target;
- the source artifact or entity in which the relation is represented.

The source SHALL be determined by the artifact or entity owning the
relation.

The kernel SHALL NOT depend on the physical serialization format used to
represent a relation.

The loader SHALL normalize supported persistence representations into the
canonical Relation domain model.

## Predicate Semantics

A Predicate SHALL define the semantic meaning of a relation.

A Predicate MAY define semantic constraints restricting which source and
target ontology Concepts may participate in that relation.

A relation SHALL be semantically valid only when its source and target satisfy
the constraints defined by its Predicate.

Predicate existence alone SHALL NOT imply that every source-to-target
combination is valid.

## Semantic Validation

ATON verification SHALL distinguish between structural and semantic
validation.

Structural validation SHALL establish properties such as:

- relation representation is syntactically valid;
- predicate is known or explicitly classified;
- target can be resolved according to the applicable resolution rules;
- duplicate relations are detected;
- self references are detected where prohibited.

Semantic validation SHALL establish whether the relation is permitted by the
semantic definition of its Predicate.

Semantic validation SHALL use the canonical ontology types of the source and
target.

Ontology type SHALL be obtained from the explicit canonical ontology
identity of the participating artifact or entity.

Ontology type SHALL NOT be inferred from repository paths, directory names,
file names or persistence classifications.

## Canonical Predicate Constraints

Predicate constraints SHALL be represented independently of individual
relations.

A Predicate MAY define one or more permitted source-to-target Concept pairs.

Each permitted pair SHALL identify:

- one source Concept;
- one target Concept.

A relation SHALL satisfy at least one applicable permitted pair when the
Predicate defines semantic constraints.

A Predicate without applicable permitted pairs SHALL NOT be assumed to be
semantically valid for arbitrary source and target Concepts.

## Relation Direction

Relations SHALL be directional unless their Predicate explicitly defines
symmetric semantics.

The source and target of a Relation SHALL therefore remain distinct concepts.

An inverse relation MAY be defined explicitly by the ontology or Predicate
model.

An inverse relation SHALL NOT be inferred merely because two relations happen
to reference one another.

## Relation Identity

Within the canonical model, a relation SHALL be identifiable by its source,
predicate and target.

Two relations with the same source, predicate and target SHALL represent the
same semantic relation unless an explicit future extension defines additional
identity components.

Physical serialization details SHALL NOT participate in relation identity.

## Relation Persistence

A Relation MAY be serialized using different physical representations.

Examples include:

- mapping-based YAML;
- embedded relation objects;
- JSON;
- database records;
- external exchange formats.

These representations SHALL be normalized into the canonical Relation domain
model before being consumed by kernel components.

The kernel SHALL NOT interpret persistence-specific relation structures
directly.

## External Targets

A relation MAY target an entity that is not physically stored in the current
Foundation or repository.

External target resolution SHALL therefore be treated separately from
semantic predicate validation.

The absence of a locally persisted target SHALL NOT automatically imply that
the Predicate semantics are invalid.

Resolution and semantic validation SHALL remain separate concerns.

## Legacy Predicates

Legacy or unresolved Predicates MAY exist during migration.

Such Predicates SHALL be explicitly classified according to the applicable
Predicate registry and migration rules.

An unresolved Predicate SHALL NOT silently become canonical merely because it
is encountered in persisted relation data.

Migration of legacy relations SHALL normalize them into canonical Predicate
semantics before they are treated as fully verified semantic relations.

## Kernel Boundaries

The loader SHALL act as the Anti-Corruption Layer between physical
persistence and the canonical relation model.

The verification subsystem SHALL operate on canonical Relations and Predicate
definitions.

The renderer SHALL operate on canonical Relations and SHALL NOT need to
understand persistence-specific relation serialization.

Future reasoning, navigation and analysis components SHALL likewise operate
on the canonical semantic relation model.

## Consequences

### Positive

- Relation semantics are independent of persistence.
- Structural and semantic validation are clearly separated.
- Predicate constraints provide an extensible semantic validation mechanism.
- Ontology types provide a stable basis for semantic relation validation.
- Legacy relation representations can be normalized at the loader boundary.
- Verification, rendering and reasoning can share one canonical relation
  model.
- Alternative persistence and exchange formats can be supported.

### Negative

- Predicates require explicit semantic definitions.
- Ontology Concepts and Predicate constraints must be maintained.
- Legacy relations may require migration.
- Semantic verification is more complex than structural validation.

## Relationship to Other Decisions

ADR-0008 establishes canonical domain models as the architectural boundary
between persistence and the kernel.

ADR-0009 defines the architectural basis for semantic relation constraints.

ADR-0010 defines canonical metadata semantics.

ADR-0011 defines the separation between the logical Engineering Knowledge
Model and physical representations.

ADR-0013 defines Engineering Entity and Engineering Artifact semantics.

RFC-0029 defines the canonical semantic constraint representation for
Predicates.

This ADR consolidates these principles into the canonical relation model used
by the ATON kernel.

## Alternatives Considered

### Treat relations as persistence structures

Rejected.

This would couple kernel behaviour to individual serialization formats and
prevent consistent semantics across persistence implementations.

### Validate only predicate existence

Rejected.

Predicate existence does not establish that a particular source-to-target
combination is semantically valid.

### Infer semantic types from repository structure

Rejected.

Repository structure is a physical representation detail and must not define
canonical ontology identity.

### Allow every Predicate for every source and target

Rejected.

This would prevent the ontology from expressing semantic restrictions on
relations.

## Expected Outcome

ATON SHALL provide a canonical semantic Relation domain model.

Relations SHALL be normalized by the loader, interpreted by kernel components
through the canonical model and validated against explicit Predicate and
ontology semantics.

The resulting model SHALL remain independent of physical persistence and
serialization.

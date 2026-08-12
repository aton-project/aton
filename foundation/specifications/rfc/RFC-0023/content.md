# RFC-0023 — Engineering Traceability

## Status

Draft

## Summary

This RFC defines the canonical semantics of traceability within the ATON
Engineering Knowledge Model.

Traceability is the ability to establish, navigate, inspect and verify
explicit relationships between engineering knowledge.

Traceability is a capability of the Engineering Knowledge Model. It does not
prescribe an engineering process, workflow or organizational practice.

Traceability SHALL operate on the canonical logical Engineering Knowledge
Model and SHALL remain independent of the physical persistence or rendering
technology used to represent that knowledge.

## Motivation

Engineering knowledge consists of interconnected concepts.

A Requirement may be related to a Specification.
An Architecture Decision may influence a Requirement.
A Component may implement a Specification.
A Verification activity may provide evidence for an engineering state.

These relationships provide the basis for understanding engineering
dependencies, impact and provenance.

ADR-0006 establishes the Engineering Knowledge Graph as the canonical logical
organization of engineering knowledge.

RFC-0025 defines the canonical Relation domain model.

This RFC defines how those relationships provide traceability across
engineering knowledge.

## Goals

This RFC SHALL:

- define the semantics of engineering traceability;
- define traceability as a capability of the Engineering Knowledge Model;
- support navigation across explicit relationships;
- support inspection of relationship paths;
- support verification of traceability relationships;
- support traceability across Engineering Versions;
- support traceability across Baselines;
- preserve the distinction between semantic and technical relationships;
- remain independent of persistence and rendering technologies; and
- provide a foundation for impact and dependency analysis.

## Non-Goals

This RFC does not define:

- engineering development processes;
- review processes;
- approval workflows;
- organizational responsibilities;
- project management procedures;
- configuration management processes;
- release management processes;
- a specific traceability tool;
- a specific user interface;
- a specific persistence technology;
- automatic semantic inference;
- automatic relationship creation; or
- a required traceability matrix format.

ATON provides capabilities for representing and analysing traceability.
Projects remain responsible for defining the processes in which those
capabilities are used.

## Traceability

Traceability SHALL represent the ability to determine explicit relationships
between engineering knowledge.

A traceability relationship consists of:

    source engineering knowledge
              |
              | predicate
              ▼
    target engineering knowledge

The relationship SHALL be represented using the canonical Relation model.

A traceability relationship SHALL therefore be represented by a canonical
Relation containing an explicitly represented Predicate and target.

The source is determined by the Entity that owns the Relation, according to
the canonical Relation model defined by RFC-0025.

Traceability does not introduce a separate relation type or representation.

## Explicit Traceability

Traceability SHALL be based on explicit relationships represented in the
Engineering Knowledge Model.

The existence of two related engineering concepts SHALL NOT imply a
traceability relationship unless the relationship is explicitly represented
or defined by an applicable normative semantic rule.

ATON SHALL NOT silently create traceability relationships based solely on:

- physical file location;
- naming conventions;
- textual similarity;
- Git history;
- timestamps;
- folder hierarchy; or
- other implementation-specific observations.

Such information MAY provide provenance or supporting evidence but SHALL NOT
automatically become canonical traceability.

## Semantic Traceability

A traceability relationship SHALL be interpreted according to the semantics
of its Predicate.

RFC-0025 defines the canonical Relation representation.

RFC-0029 defines semantic constraints for Predicates.

Therefore, a Relation contributes to canonical traceability only when its
structural representation is valid and its applicable semantic constraints
are satisfied.

Semantic validity SHALL be determined according to RFC-0029.

A structurally representable relation MAY nevertheless be semantically
invalid.

Semantic validation SHALL remain separate from structural relation
representation.

## Traceability and the Engineering Knowledge Graph

The Engineering Knowledge Graph provides the canonical structure through
which traceability is represented.

Traceability does not constitute a separate parallel graph.

Instead:

    Engineering Knowledge Graph
              |
              +-- Relations
              |
              +-- Versions
              |
              +-- Baselines
              |
              +-- other canonical knowledge
              |
              ▼
          Traceability

Traceability is therefore a capability derived from the relationships in the
canonical Engineering Knowledge Graph.

Views, reports and matrices MAY present traceability in different forms, but
those representations SHALL NOT replace the canonical graph.

## Traceability Navigation

A conforming implementation SHOULD support navigation from a source
engineering object to related target objects.

Navigation MAY include:

- direct outgoing relationships;
- direct incoming relationships;
- relationships of a selected Predicate;
- relationships within a selected Baseline;
- relationships associated with a selected Engineering Version; and
- multi-step relationship paths.

Navigation results SHALL be derived from the canonical Engineering Knowledge
Model.

A navigation view SHALL NOT become a second authoritative representation of
the relationships.

## Incoming and Outgoing Traceability

For a relation:

    ```text
    A --P--> B
    ```

the traceability model provides two navigational perspectives:

    ```text
    outgoing:
        A -> B

    incoming:
        B <- A
    ```

Both perspectives refer to the same canonical Relation.

An implementation MAY expose additional views such as:

- upstream traceability;
- downstream traceability;
- dependency views;
- impact views; or
- traceability matrices.

Such views SHALL remain derived representations of the canonical graph.

## Traceability Paths

Traceability MAY extend across multiple relationships.

For example:

    Requirement
        |
        | refines
        ▼
    Requirement
        |
        | implementedBy
        ▼
    Component
        |
        | verifiedBy
        ▼
    Test

The example uses only Predicate applications permitted by the ATON ontology
defined by RFC-0027.

A traceability path SHALL NOT be considered valid merely because each
individual relation is structurally representable. Each Relation SHALL satisfy
the applicable semantic constraints defined by RFC-0029.

Such a path MAY provide useful engineering traceability.

A path SHALL NOT automatically acquire a semantic meaning merely because its
individual relations are valid.

Path semantics requiring transitivity, inference or property-chain reasoning
are outside the scope of this RFC.

## Traceability and Engineering Versions

Traceability SHALL preserve Engineering Version semantics.

A relation associated with one Engineering Version SHALL NOT automatically be
assumed to exist in another Engineering Version.

Version-aware traceability MAY therefore answer questions such as:

- which engineering objects were related in a particular version;
- which relationships changed between versions;
- which downstream knowledge is affected by a version change; and
- which version provided the basis for a particular engineering state.

RFC-0012 defines Engineering Version semantics.

## Traceability and Baselines

A Baseline defines an explicitly selected and reproducible engineering state.

Traceability SHALL therefore be evaluable in the context of a Baseline.

A Baseline MAY be used to determine:

- which relationships existed in the selected state;
- which engineering objects were connected;
- which upstream knowledge was available;
- which downstream knowledge depended on the selected state; and
- how traceability changed between Baselines.

RFC-0013 defines Baseline semantics.

A Baseline SHALL NOT create new relationships merely by selecting
Engineering Knowledge.

## Traceability and Releases

A Release identifies an explicitly released engineering state.

Traceability MAY be evaluated against the engineering state represented by a
Release.

A Release MAY therefore provide a stable context for questions such as:

- which requirements were included;
- which specifications were related;
- which components were covered;
- which verification evidence was associated; and
- which engineering decisions affected the released state.

Release semantics remain outside the scope of this RFC.

## Traceability Across Artifact Representations

Traceability SHALL operate on canonical engineering knowledge rather than
physical file paths.

A physical artifact MAY represent an Engineering Entity, Engineering Version
or other canonical object.

Changing the physical representation SHALL NOT inherently change the
engineering traceability relationships.

Where an artifact is replaced by another physical representation, the
canonical engineering relationships MAY remain unchanged.

RFC-0011 defines the separation between logical Engineering Knowledge and
physical representations.

## Traceability and Persistence

Traceability SHALL remain independent of persistence technology.

A conforming implementation MAY persist engineering knowledge using:

- Git;
- a database;
- an artifact repository;
- an object store; or
- another persistence mechanism.

The persistence mechanism SHALL provide sufficient information for the
canonical Engineering Knowledge Model to reconstruct its relationships.

Git commits MAY provide technical provenance.

Git history SHALL NOT automatically become semantic traceability.

## Traceability and Git

Git history MAY provide useful technical evidence for understanding how a
physical representation changed.

However:

    Git history != Engineering Traceability

A Git commit MAY be associated with an Engineering Version, Artifact Revision,
Baseline or other engineering object.

Such an association SHALL remain distinguishable from the semantic
relationship represented by the Engineering Knowledge Graph.

## Traceability Verification

A conforming implementation SHOULD provide verification capabilities for
traceability.

Verification MAY identify:

- unknown relation targets;
- structurally invalid relations;
- duplicate relations;
- invalid self references;
- unknown Predicates;
- invalid source-to-target Concept pairs;
- violations of applicable semantic constraints;
- relationships referencing unavailable Engineering Versions;
- relationships inconsistent with a selected Baseline; or
- other violations defined by applicable semantic constraints.

Structural relation verification is defined by RFC-0025.

Semantic relation verification is defined by RFC-0029.

Traceability verification SHALL NOT silently modify engineering knowledge.

## Traceability Completeness

Traceability completeness is a property of an engineering knowledge set
relative to explicitly defined expectations.

ATON MAY provide mechanisms for determining whether expected relationships
exist.

For example, a project MAY define that every Requirement is expected to have
a relationship to one or more Specifications.

Such expectations SHALL be defined by an applicable domain, project or
process model.

ATON SHALL NOT impose universal traceability completeness requirements on
all engineering projects.

An absent relationship SHALL therefore not automatically constitute an ATON
error unless a normative constraint requires that relationship.

## Traceability Consistency

Traceability consistency concerns whether existing relationships conform to
the applicable structural and semantic rules.

Consistency MAY include:

- valid relation structure;
- valid relation targets;
- valid Predicate semantics;
- valid Concept combinations;
- valid version references; and
- valid Baseline membership.

Completeness and consistency SHALL remain distinct.

A knowledge set MAY be structurally and semantically consistent while still
being incomplete relative to a project-specific traceability expectation.

## Impact Analysis

Traceability MAY provide the basis for impact analysis.

Given a changed engineering object, an implementation MAY navigate outgoing
or incoming relationships to identify potentially affected engineering
knowledge.

Impact analysis SHALL distinguish between:

- explicit traceability;
- semantic relationship constraints; and
- inferred or heuristic results.

An implementation SHALL NOT present inferred impact as explicit traceability
unless the inference itself is represented according to an applicable
normative model.

## Dependency Analysis

Traceability MAY provide the basis for dependency analysis.

A dependency analysis MAY identify engineering objects connected through
applicable dependency relationships.

The meaning of a dependency SHALL be determined by the corresponding
Predicate semantics.

Traceability itself SHALL NOT define new dependency semantics.

## Traceability Matrices

A traceability matrix MAY be generated as a view of the Engineering
Knowledge Graph.

For example:

    Source        Predicate       Target
    Requirement   refines         Specification
    Specification implementedBy   Component
    Component     verifiedBy      Test

A traceability matrix SHALL be considered a derived presentation.

The matrix SHALL NOT become the canonical storage representation of
traceability.

Changes to a matrix SHALL NOT directly redefine engineering relationships
unless the matrix is explicitly implemented as an authoring interface whose
changes are normalized into the canonical Relation model.

## Traceability Queries

A conforming implementation SHOULD provide query capabilities over
traceability.

Queries MAY select relationships by:

- source;
- target;
- Predicate;
- Engineering Version;
- Baseline;
- Release;
- Concept;
- artifact;
- or other canonical domain properties.

The query model SHALL operate on the canonical Engineering Knowledge Model.

Query syntax and user-interface behaviour are implementation concerns.

## Traceability and Views

Views MAY present traceability according to different engineering concerns.

Examples include:

- requirement traceability;
- architecture traceability;
- verification traceability;
- dependency views;
- impact views;
- version comparison views; and
- baseline comparison views.

Views SHALL NOT define the underlying engineering relationships.

This preserves the architectural principle that knowledge is independent of
its presentation.

## Traceability Provenance

Traceability relationships MAY include provenance information through the
applicable metadata and version models.

Provenance MAY identify:

- the Engineering Version;
- the Artifact Revision;
- the Git Revision;
- the Baseline;
- the process context; or
- other authoritative evidence.

Provenance SHALL support understanding of the relationship without replacing
the canonical Relation itself.

## Migration

Existing relations SHALL remain usable as structural traceability during
migration.

Migration MAY introduce semantic verification according to RFC-0029.

Existing relations SHALL NOT be silently rewritten solely to satisfy new
traceability expectations.

Where existing relationships cannot be interpreted semantically, the
implementation SHOULD report the condition and preserve the original
relationship.

Project-specific completeness requirements MAY be introduced separately.

## Consequences

### Positive

- Traceability becomes a first-class capability of the Engineering Knowledge
  Model.
- Engineering knowledge remains navigable as a graph.
- Traceability remains independent of storage and rendering technologies.
- Version and Baseline context can be preserved.
- Structural and semantic verification remain clearly separated.
- Impact and dependency analysis can build on explicit relationships.
- Traceability matrices and other reports remain derived views.

### Negative

- Useful traceability requires explicit relationships.
- Maintaining semantic consistency requires verification.
- Version-aware and Baseline-aware traceability adds implementation
  complexity.
- Complete traceability cannot be guaranteed without project-specific
  expectations.

## Alternatives

### Store Traceability Only in Matrices

Rejected.

Matrices are presentation-oriented and cannot serve as the canonical
representation of a connected Engineering Knowledge Graph.

### Derive Traceability from Git History

Rejected.

Git describes technical repository history and does not by itself express
engineering semantics.

### Derive Traceability from File Paths

Rejected.

Physical organization is not the canonical logical organization of
engineering knowledge.

### Store Traceability in a Separate Traceability Database

Rejected as a canonical model.

A separate implementation MAY be used for indexing or query acceleration,
but it SHALL remain derived from the canonical Engineering Knowledge Model.

### Infer All Traceability Automatically

Rejected.

Implicit inference would make engineering relationships difficult to
understand, verify and govern.

Explicit relationships remain the canonical basis of traceability.

## Open Questions

The following topics may require future specifications:

- formal path semantics;
- transitive traceability;
- inverse relationship semantics;
- property-chain reasoning;
- traceability coverage metrics;
- temporal traceability queries;
- cross-project traceability;
- external-system traceability;
- traceability evidence models;
- formal impact-analysis semantics; and
- query language standardization.

These capabilities SHALL build upon the canonical Engineering Knowledge Model
rather than introducing an independent traceability model.

## Acceptance Criteria

A conforming implementation SHALL:

1. represent traceability through the canonical Relation model;
2. preserve explicit source-to-target relationships;
3. distinguish traceability from physical storage structure;
4. distinguish traceability from Git history;
5. support traceability in the context of Engineering Versions;
6. support traceability in the context of Baselines;
7. preserve the distinction between structural and semantic verification;
8. permit traceability to be presented through derived views;
9. avoid requiring a specific traceability matrix as the canonical
   representation;
10. avoid imposing universal project-specific completeness requirements;
11. preserve persistence independence; and
12. avoid silently modifying engineering relationships during verification or
    migration.

## References

- ADR-0006 Engineering Knowledge Graph
- ADR-0011 Logical Engineering Knowledge Model and Physical Representations
- ADR-0012 Engineering Version and Baseline Semantics
- RFC-0012 Engineering Version Semantics
- RFC-0013 Engineering Baseline Semantics
- RFC-0025 Canonical Relation Model
- RFC-0029 Canonical Semantic Relation Constraint Model

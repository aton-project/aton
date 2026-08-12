

# RFC-0021 — Views

## Status

Draft

## Summary

This RFC defines the normative semantics of Views within the ATON Engineering
Knowledge Model.

A View is a derived perspective on canonical engineering knowledge.

A View MAY select, filter, organize, aggregate or present engineering
knowledge according to a defined purpose.

A View SHALL NOT redefine the semantic meaning of the Engineering Knowledge
Model.

The canonical Engineering Knowledge Model remains the authoritative source of
engineering semantics. A View is derived from that model and may provide a
different perspective without creating an alternative semantic representation.

Views are therefore distinct from:

- Engineering Entities;
- Engineering Versions;
- Engineering Artifacts;
- Relations;
- Ontology concepts;
- physical representations; and
- navigation semantics.

## Motivation

Engineering knowledge may need to be presented in different ways depending on
the purpose of the user or tool.

Examples include:

- requirements views;
- architecture views;
- traceability views;
- dependency views;
- impact views;
- verification views;
- lifecycle views;
- review views;
- dashboards;
- generated documents;
- graphical representations; and
- AI-assisted views.

The same engineering knowledge may therefore be presented through multiple
views.

Without a normative View model, implementations may incorrectly treat a
particular presentation as the canonical organization or semantic definition
of engineering knowledge.

ATON therefore requires a clear distinction between the canonical Engineering
Knowledge Model and the Views derived from it.

## Goals

This RFC SHALL:

- define the semantics of a View;
- establish Views as derived perspectives on canonical engineering knowledge;
- preserve the canonical Engineering Knowledge Model as the semantic
  authority;
- allow multiple Views of the same engineering knowledge;
- allow Views to select, filter and organize engineering knowledge;
- support purpose-specific presentations;
- distinguish Views from physical representations;
- support deterministic Views where appropriate;
- support implementation-specific Views without changing canonical semantics;
  and
- remain independent of a particular rendering or presentation technology.

## Non-Goals

This RFC does not define:

- the canonical Engineering Knowledge Model itself;
- ontology semantics;
- relation semantics;
- navigation semantics;
- a specific rendering technology;
- a specific user interface;
- a document format;
- a database schema;
- a graphical notation;
- dashboard implementations;
- AI user interfaces;
- visualization styling; or
- project-specific view definitions.

Specific view types MAY be defined by separate specifications.

## View

A View SHALL represent a derived perspective on canonical engineering
knowledge.

A View MAY define:

- a selection of engineering objects;
- filtering criteria;
- ordering;
- grouping;
- projection of properties;
- traversal of relations;
- aggregation;
- contextual information;
- presentation-specific structure; or
- another deterministic or purpose-specific interpretation of canonical
  engineering knowledge.

A View SHALL NOT introduce semantic information that contradicts the
canonical Engineering Knowledge Model.

A View MAY omit information from the canonical model without implying that
the omitted information does not exist.

## View Identity

A View MAY have an explicit identity when it is itself persisted or referenced
as an engineering object.

Where a View has a canonical identity, that identity SHALL be distinct from
the identity of the engineering knowledge being viewed.

A View identifier SHALL NOT be derived solely from:

- a rendered document;
- a file path;
- a URL;
- a database query identifier;
- a UI component identifier; or
- another physical representation.

The identity of a View describes the View definition or semantic perspective,
not the identity of the objects displayed by the View.

## View Definition

A View MAY be defined by a set of rules describing how canonical engineering
knowledge is selected and presented.

A View definition MAY specify:

- object types;
- ontology types;
- relation predicates;
- metadata properties;
- version constraints;
- baseline constraints;
- lifecycle constraints;
- selection criteria;
- ordering;
- grouping;
- traversal depth;
- aggregation rules; or
- presentation hints.

A View definition SHALL remain distinguishable from the resulting physical
representation.

For example, a View MAY define that all requirements linked to a particular
system component shall be displayed together.

The resulting HTML page, diagram or API response is a physical representation
of that View and is not the View definition itself.

## View and Canonical Knowledge

A View SHALL be derived from canonical engineering knowledge.

The semantic relationship is:

    Canonical Engineering Knowledge
                |
                ▼
          View Definition
                |
                ▼
             View
                |
                ▼
      Physical Representation

The View SHALL NOT become a second source of semantic authority.

Changes made to a View SHALL NOT silently modify the canonical engineering
knowledge from which the View was derived.

If a tool provides editing through a View, the resulting semantic changes SHALL
be applied to the canonical Engineering Knowledge Model through the applicable
authoring or update mechanism.

## View and Engineering Entities

A View MAY contain or display Engineering Entities.

The Engineering Entity remains the canonical engineering concept.

A View SHALL NOT create a new Engineering Entity merely because the entity is
displayed by that View.

The same Engineering Entity MAY appear in multiple Views.

Different Views MAY organize the same Engineering Entities differently.

## View and Engineering Versions

A View MAY be evaluated against a specific Engineering Version or version
selection.

For example, a View MAY represent:

- the current versions of selected entities;
- the versions contained in a Baseline;
- historical versions at a defined point;
- differences between versions; or
- a version history.

The View SHALL identify the applicable version context where that context is
semantically relevant.

A View SHALL NOT silently mix incompatible version contexts when doing so
would produce an ambiguous engineering interpretation.

## View and Baselines

A View MAY be evaluated against a Baseline.

When a View is based on a Baseline, the View SHALL operate on the engineering
state selected by that Baseline.

A View SHALL NOT modify Baseline membership.

A View may provide a representation of a Baseline, but:

    View != Baseline

The Baseline defines the selected engineering state.

The View defines a perspective on that state.

## View and Relations

A View MAY traverse, filter, group or display canonical relations.

For example, a traceability View MAY display:

    Requirement
        |
        | satisfies
        ▼
    System Requirement
        |
        | verifiedBy
        ▼
    Verification Case

The View does not create these relations.

The canonical Relation Model remains authoritative for their semantics.

A View SHALL NOT reinterpret a relation predicate merely for presentation
purposes.

Derived navigation paths MAY be displayed by a View provided that their
derived nature remains distinguishable from canonical relations.

## View and Navigation

Navigation and Views are related but distinct concepts.

Navigation describes how engineering knowledge can be traversed or discovered.

A View describes a selected perspective on engineering knowledge.

A View MAY provide navigation mechanisms.

Navigation MAY operate across multiple Views.

Neither a View nor a navigation mechanism SHALL become the semantic source of
engineering knowledge.

The canonical Engineering Knowledge Model remains authoritative.

## View and Physical Representation

A View is a semantic or logical perspective.

A physical representation is a concrete technical representation of that
perspective.

Examples of physical representations include:

- HTML pages;
- Markdown documents;
- diagrams;
- tables;
- JSON responses;
- API responses;
- graphical interfaces;
- generated reports; and
- AI-generated presentations.

Multiple physical representations MAY represent the same View.

Likewise, the same canonical engineering knowledge MAY be represented through
multiple Views.

The physical representation SHALL NOT define the semantics of the View.

## Derived Information

A View MAY use derived information provided by an implementation.

Examples include:

- Git information;
- indexes;
- cached query results;
- search results;
- computed metrics;
- generated graph paths; or
- other implementation-specific information.

Such information MAY enrich a View.

Derived information SHALL NOT silently redefine canonical engineering
semantics.

If derived information conflicts with canonical engineering knowledge, the
canonical model SHALL remain authoritative.

## Deterministic Views

A View SHOULD be deterministic when its purpose requires reproducibility.

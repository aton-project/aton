# Engineering Knowledge Navigation

## Context

ATON engineering knowledge is represented as a logical Engineering Knowledge
Model containing entities, artifacts, metadata, versions, relations and
process information.

Engineering knowledge must be navigable independently of any particular
physical representation.

A repository directory structure, document hierarchy or user interface may
provide one possible navigation view, but none of these representations
defines the semantic structure of the Engineering Knowledge Model.

## Problem Statement

Without a common semantic definition of navigation, implementations may
interpret navigation as traversal of:

- repository directories;
- document hierarchies;
- hyperlinks;
- database structures;
- user interface elements; or
- other physical representations.

These mechanisms may be useful, but they do not provide a persistence-
independent definition of engineering knowledge navigation.

ATON therefore requires a semantic navigation model based on the canonical
Engineering Knowledge Model.

## Decision

ATON SHALL provide engineering knowledge navigation as a capability for
discovering and traversing the logical Engineering Knowledge Model.

Navigation SHALL operate on canonical engineering concepts and their
semantic relationships.

Navigation SHALL NOT depend on a particular:

- repository structure;
- file layout;
- document hierarchy;
- database schema;
- user interface; or
- physical representation.

Implementations MAY provide any user interface or technical mechanism for
navigation provided that the resulting navigation is consistent with the
canonical Engineering Knowledge Model.

## Navigation Target

A navigation target SHALL be an addressable element of the Engineering
Knowledge Model.

Targets MAY include:

- Engineering Entities;
- Engineering Artifacts;
- Engineering Versions;
- Baselines;
- Releases;
- Engineering Processes;
- Process Instances;
- Architecture Decisions;
- other domain concepts defined by the applicable ontology.

The semantic identity of a navigation target SHALL remain independent of its
physical representation.

## Navigation Path

A navigation path SHALL represent a sequence of semantically meaningful
connections between engineering concepts.

A path MAY traverse:

- canonical relations;
- entity-to-artifact relationships;
- version relationships;
- process relationships;
- provenance relationships; or
- other explicitly defined semantic connections.

Physical containment SHALL NOT automatically constitute a semantic navigation
path.

## Relation-Based Navigation

Canonical relations SHALL provide a primary basis for semantic navigation.

A navigation operation MAY traverse relations according to their predicates
and applicable directionality.

The meaning of a navigation step SHALL be determined by the semantics of the
underlying relation.

Implementations SHALL NOT infer semantic relationships merely because two
objects are physically adjacent or stored together.

## Direction and Inverse Navigation

A directional relation MAY be traversed from source to target.

An implementation MAY also provide inverse navigation when the relation
semantics support such traversal.

Inverse navigation SHALL NOT imply that an inverse engineering relation
exists.

The distinction between traversal direction and semantic relation direction
SHALL be preserved.

## Navigation Views

A navigation view SHALL be an interpretation or presentation of the
Engineering Knowledge Model for a particular purpose.

Examples include:

- traceability views;
- dependency views;
- impact analysis views;
- process views;
- version history views;
- architecture views;
- entity-centric views.

Views MAY expose only a subset of the Engineering Knowledge Model.

A view SHALL NOT redefine the semantic identity or meaning of the concepts it
presents.

## Filtering

Navigation MAY apply filters based on canonical engineering properties.

Filters MAY use:

- entity type;
- lifecycle state;
- version;
- relation predicate;
- process state;
- metadata;
- baseline membership;
- release membership; or
- other canonical properties.

Filters based solely on implementation-specific storage properties SHALL NOT
be considered part of the canonical navigation semantics.

## Traceability Navigation

ATON SHALL support navigation across engineering traceability relationships.

A user or tool MAY therefore navigate from an engineering concept to related
concepts such as:

- requirements;
- architecture decisions;
- findings;
- verification evidence;
- process activities;
- versions;
- baselines; or
- releases.

The availability of a particular navigation path depends on the relations
and concepts defined by the applicable engineering model.

ATON SHALL NOT prescribe which traceability paths a project must define.

## Impact Navigation

Navigation MAY support impact analysis by traversing relevant semantic
relations.

An implementation MAY determine affected engineering concepts by following
applicable relation predicates and version or process semantics.

Impact analysis SHALL remain an interpretation of the canonical Engineering
Knowledge Model and SHALL NOT depend on repository layout.

## Historical Navigation

ATON SHALL support navigation across historical engineering states where the
applicable model preserves those states.

Historical navigation MAY include:

- previous engineering versions;
- superseded decisions;
- previous baselines;
- released states;
- historical process instances; and
- other preserved engineering information.

Historical navigation SHALL preserve the distinction between current and
historical engineering state.

## External Navigation

A navigation target MAY refer to engineering knowledge outside the current
physical persistence boundary.

An implementation MAY resolve such targets through:

- another repository;
- a database;
- an API;
- an external engineering system; or
- another supported persistence mechanism.

External resolution SHALL remain separate from the semantic identity of the
target.

An unresolved external target SHALL therefore remain distinguishable from a
non-existent engineering concept.

## Navigation and Persistence

Navigation SHALL operate on the canonical domain model.

Loaders SHALL provide the canonical concepts and relations required for
navigation.

Persistence-specific structures MAY be used internally to implement
navigation, but SHALL NOT define its semantic behaviour.

This preserves navigation across different persistence implementations.

## Navigation and User Interfaces

ATON SHALL NOT prescribe a particular user interface for engineering
knowledge navigation.

Possible interfaces include:

- graph views;
- document views;
- tables;
- search results;
- command-line tools;
- APIs;
- interactive diagrams; or
- other representations.

All such interfaces SHALL be considered views or access mechanisms over the
canonical Engineering Knowledge Model.

## Search and Navigation

Search and navigation are related but distinct capabilities.

Search identifies candidate engineering concepts according to specified
criteria.

Navigation traverses known semantic connections between engineering
concepts.

An implementation MAY combine search and navigation, but SHALL preserve their
semantic distinction.

## Verification

ATON MAY verify navigation integrity.

Verification MAY identify conditions such as:

- references to unresolved targets;
- invalid relations;
- invalid navigation paths;
- inconsistent entity identity;
- invalid version relationships; or
- other violations of the canonical Engineering Knowledge Model.

Navigation verification SHALL operate on canonical semantics rather than
physical document structure.

## Consequences

### Positive

- Engineering knowledge can be navigated independently of storage layout.
- Different user interfaces can expose the same semantic knowledge.
- Traceability and impact analysis can use the same canonical relations.
- Historical and current engineering states can be navigated consistently.
- Alternative persistence implementations remain possible.
- Navigation semantics remain independent of Docusaurus, Git or any other
  presentation technology.

### Negative

- Implementations must provide a semantic navigation layer.
- Navigation may require resolving relations across persistence boundaries.
- Complex engineering models may produce large navigation spaces requiring
  filtering and views.

## Relationship to Other Decisions

ADR-0011 defines the separation between the logical Engineering Knowledge
Model and physical representations.

ADR-0013 defines Engineering Entity and Engineering Artifact semantics.

ADR-0014 defines the canonical semantic relation model.

ADR-0012 defines engineering version, baseline and release semantics.

ADR-0016 defines the generic Engineering Process Model.

Navigation operates across these concepts without redefining their semantics.

## Alternatives Considered

### Use repository structure as the navigation model

Rejected.

Repository structure is a physical representation and may differ between
persistence implementations.

### Use document hierarchy as the canonical navigation model

Rejected.

Engineering knowledge is not inherently organized according to document
hierarchy.

### Define navigation through a specific user interface

Rejected.

The semantic model must remain independent of presentation technology.

### Treat search and navigation as the same capability

Rejected.

Search identifies candidates while navigation traverses semantic
relationships.

## Expected Outcome

ATON SHALL provide persistence-independent semantic navigation across the
Engineering Knowledge Model.

Navigation SHALL operate on canonical engineering concepts and their
relationships while remaining independent of physical storage, repository
structure and user interface implementation.

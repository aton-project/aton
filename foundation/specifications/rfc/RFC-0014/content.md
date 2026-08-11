# RFC-0014 — Engineering Knowledge Navigation

## Status

Proposed

## Summary

This RFC defines the canonical semantic model for navigation within the ATON
Engineering Knowledge Model.

Navigation is the capability to discover and traverse engineering knowledge
through canonical engineering concepts and their semantic relationships.

Navigation is distinct from physical document structure, repository layout,
search and user-interface presentation.

The purpose of this RFC is to define navigation independently of any particular
persistence, rendering or user-interface technology.

## Motivation

ATON represents engineering knowledge as a logical Engineering Knowledge Model
containing entities, artifacts, metadata, versions, relations and other
engineering concepts.

Engineering knowledge must remain navigable independently of the physical
representation used to store or present it.

Repository directories, document hierarchies, hyperlinks, database structures
and user-interface elements may provide navigation mechanisms, but none of
these mechanisms defines the semantic structure of engineering knowledge.

A canonical navigation model is therefore required so that different ATON
implementations can provide consistent navigation over the same engineering
knowledge.

## Scope

This RFC defines:

- semantic navigation;
- navigation targets;
- navigation paths;
- relation-based navigation;
- traversal direction;
- inverse navigation;
- navigation views;
- navigation filtering;
- traceability navigation;
- impact navigation;
- historical navigation;
- external navigation;
- the relationship between navigation and persistence;
- the distinction between search and navigation;
- navigation verification.

This RFC does not define:

- a specific user interface;
- a specific rendering technology;
- repository navigation;
- document navigation;
- search algorithms;
- ranking algorithms;
- graph databases;
- a mandatory navigation workflow;
- project-specific navigation paths.

## Navigation

Navigation SHALL be a capability for discovering and traversing the logical
Engineering Knowledge Model.

Navigation SHALL operate on canonical engineering concepts and their semantic
relationships.

Navigation SHALL NOT depend on:

- repository structure;
- file layout;
- document hierarchy;
- database schema;
- user-interface structure; or
- any other physical representation.

An implementation MAY use physical representations internally to provide
navigation, provided that the resulting navigation semantics are derived from
the canonical Engineering Knowledge Model.

## Navigation Target

A Navigation Target SHALL be an addressable element of the Engineering
Knowledge Model.

Navigation Targets MAY include:

- Engineering Entities;
- Engineering Artifacts;
- Engineering Versions;
- Baselines;
- Releases;
- Engineering Processes;
- Process Instances;
- Architecture Decisions;
- Requirements;
- Findings;
- Tests;
- or other concepts defined by the applicable ontology.

The semantic identity of a Navigation Target SHALL be independent of its
physical representation.

A physical path, URL, database identifier or document location MAY provide an
access mechanism for a Navigation Target but SHALL NOT define its semantic
identity.

## Navigation Path

A Navigation Path SHALL represent a sequence of semantically meaningful
connections between engineering concepts.

A path MAY traverse:

- canonical relations;
- entity-to-artifact relationships;
- version relationships;
- process relationships;
- provenance relationships;
- or other explicitly defined semantic connections.

Physical containment SHALL NOT automatically constitute a semantic navigation
path.

For example, storing two artifacts in the same directory SHALL NOT by itself
create a semantic navigation relationship between them.

## Relation-Based Navigation

Canonical relations SHALL provide a primary basis for semantic navigation.

A navigation operation MAY traverse a relation according to its predicate and
applicable directionality.

The meaning of a navigation step SHALL be determined by the semantics of the
underlying relation.

Implementations SHALL NOT infer semantic relationships merely because two
objects are physically adjacent, stored together or linked by a presentation
mechanism.

## Direction

A directional relation MAY be traversed from source to target.

Traversal direction SHALL be distinguished from semantic relation direction.

An implementation MAY support traversal in the reverse direction when the
relation semantics permit inverse traversal.

Reverse traversal SHALL NOT imply that an inverse engineering relation exists.

For example, if:

    A --references--> B

exists as a semantic relation, an implementation MAY allow navigation from B
to A as an inverse traversal.

This SHALL NOT imply the existence of:

    B --references--> A

unless that relation is explicitly defined.

## Navigation Views

A Navigation View SHALL be an interpretation or presentation of the
Engineering Knowledge Model for a particular purpose.

Navigation Views MAY include:

- traceability views;
- dependency views;
- impact-analysis views;
- process views;
- version-history views;
- architecture views;
- entity-centric views;
- graph views;
- document views;
- tabular views.

A Navigation View MAY expose only a subset of the Engineering Knowledge Model.

A Navigation View SHALL NOT redefine the semantic identity or meaning of the
concepts it presents.

Different views MAY present the same engineering knowledge in different ways.

## Filtering

Navigation MAY apply filters based on canonical engineering properties.

Filters MAY use:

- entity type;
- lifecycle state;
- engineering version;
- relation predicate;
- process state;
- metadata;
- baseline membership;
- release membership;
- or other canonical properties.

Filters based solely on implementation-specific storage properties SHALL NOT
define canonical navigation semantics.

Filtering SHALL reduce the set of navigable concepts or relationships without
changing their semantic meaning.

## Traceability Navigation

ATON SHALL support navigation across engineering traceability relationships.

A user or tool MAY navigate from an engineering concept to related concepts
such as:

- requirements;
- architecture decisions;
- findings;
- verification evidence;
- process activities;
- engineering versions;
- baselines;
- releases;
- or other related engineering concepts.

The availability of a particular traceability path SHALL depend on the
relations and concepts defined by the applicable engineering model.

ATON SHALL NOT prescribe which traceability paths a project SHALL define.

## Impact Navigation

Navigation MAY support impact analysis by traversing relevant semantic
relations.

An implementation MAY determine potentially affected engineering concepts by
following applicable relation predicates and relevant version or process
semantics.

Impact analysis SHALL remain an interpretation of the canonical Engineering
Knowledge Model.

Impact navigation SHALL NOT depend on repository layout or document
structure.

## Historical Navigation

ATON SHALL support navigation across historical engineering states where the
applicable model preserves those states.

Historical navigation MAY include:

- previous engineering versions;
- superseded decisions;
- previous baselines;
- released states;
- historical process instances;
- historical artifacts;
- or other preserved engineering information.

Historical navigation SHALL preserve the distinction between current and
historical engineering state.

A newer state SHALL NOT implicitly erase the semantic identity or historical
existence of a preserved earlier state.

## External Navigation

A Navigation Target MAY refer to engineering knowledge outside the current
physical persistence boundary.

An implementation MAY resolve external targets through:

- another repository;
- a database;
- an API;
- an external engineering system;
- or another supported persistence mechanism.

External resolution SHALL remain separate from semantic identity.

An unresolved external target SHALL therefore remain distinguishable from a
non-existent engineering concept.

## Navigation and Persistence

Navigation SHALL operate on the canonical domain model.

Loaders or corresponding translation components SHALL provide the canonical
concepts and relationships required for navigation.

Persistence-specific structures MAY be used internally to implement navigation,
but SHALL NOT define its semantic behaviour.

This requirement preserves navigation across different persistence
implementations.

## Navigation and Search

Search and navigation are related but distinct capabilities.

Search SHALL identify candidate engineering concepts according to specified
criteria.

Navigation SHALL traverse known semantic connections between engineering
concepts.

An implementation MAY combine search and navigation, but SHALL preserve their
semantic distinction.

For example:

    Search:
        find all Requirements containing "braking"

    Navigation:
        Requirement -> satisfies -> System Function

Search identifies candidates.

Navigation traverses semantic relationships.

## Navigation and Views

Views SHALL be access mechanisms or interpretations over the canonical
Engineering Knowledge Model.

A view MAY provide:

- graph traversal;
- document traversal;
- dependency exploration;
- traceability exploration;
- historical exploration;
- process exploration;
- or other navigation capabilities.

A view SHALL NOT become the semantic authority for the engineering knowledge it
presents.

Docusaurus, a web application, a command-line interface or another user
interface MAY provide navigation without defining navigation semantics.

## Navigation Verification

ATON MAY verify navigation integrity.

Verification MAY identify conditions such as:

- unresolved navigation targets;
- invalid relations;
- invalid navigation paths;
- inconsistent entity identity;
- invalid version relationships;
- invalid external references;
- or other violations of the canonical Engineering Knowledge Model.

Navigation verification SHALL operate on canonical semantics rather than
physical document structure.

A structurally valid physical link SHALL NOT by itself establish a valid
semantic navigation relationship.

## Navigation and Ontology

Navigation SHALL respect the semantics defined by the applicable ontology.

The ontology defines the meaning of concepts and predicates.

Navigation uses these semantics to determine which relationships may be
traversed and how traversal should be interpreted.

Navigation SHALL NOT introduce new semantic relationships.

A navigation implementation MAY provide derived traversal capabilities, but
derived traversal SHALL remain distinguishable from explicitly persisted
engineering relations.

## Navigation and Versioning

Navigation MAY operate across Engineering Versions.

The semantic identity of an Engineering Version SHALL remain independent of its
physical representation.

Navigation between versions SHALL preserve the distinction between:

- engineering identity;
- engineering version;
- artifact revision;
- technical revision;
- baseline;
- and release.

A technical Git history MAY be used to provide historical navigation where
appropriate, but Git history SHALL NOT redefine engineering version semantics.

## Navigation and Processes

ATON MAY provide navigation across Engineering Processes and Process
Instances.

Such navigation SHALL expose process semantics defined by the applicable
Engineering Knowledge Model.

ATON SHALL NOT prescribe a particular engineering process or workflow through
the navigation model.

Projects MAY define their own process structures and relationships.

Navigation SHALL provide the means to describe and traverse those structures
without making a particular process mandatory.

## Canonical Navigation Model

The canonical conceptual navigation model is:

    Navigation Target
          |
          v
    semantic connection
          |
          v
    Navigation Target

A Navigation Path is therefore composed of addressable engineering concepts
connected through explicitly defined semantic relationships.

The canonical model does not require a graph database or any particular
physical graph representation.

## Consequences

### Positive

- Engineering knowledge can be navigated independently of storage layout.
- Different interfaces can expose the same semantic knowledge.
- Traceability and impact analysis can use the canonical relation model.
- Historical engineering states can remain navigable.
- Alternative persistence implementations remain possible.
- Navigation remains independent of Docusaurus, Git and other presentation
  technologies.
- Project-specific processes can be navigated without becoming mandatory ATON
  processes.

### Negative

- Implementations require a semantic navigation layer.
- Navigation may require resolving relationships across persistence
  boundaries.
- Large engineering models may require filtering and specialized views.
- External navigation may require additional resolution mechanisms.

## Relationship to Other Specifications

ADR-0011 defines the separation between the logical Engineering Knowledge Model
and physical representations.

ADR-0012 defines engineering identity, engineering versions, baselines and
releases.

ADR-0013 defines Engineering Entity and Engineering Artifact semantics.

ADR-0014 defines the canonical semantic relation model.

ADR-0016 defines the generic Engineering Process Model.

ADR-0018 establishes the architectural decision for Engineering Knowledge
Navigation.

RFC-0025 defines the canonical Relation domain model.

RFC-0029 defines semantic constraints for relation predicates.

This RFC defines how canonical engineering knowledge and its relationships are
used for semantic navigation.

## Alternatives Considered

### Use Repository Structure as the Navigation Model

Rejected.

Repository structure is a physical representation and may differ between
persistence implementations.

### Use Document Hierarchy as the Canonical Navigation Model

Rejected.

Engineering knowledge is not inherently organized according to document
hierarchy.

### Define Navigation Through a Specific User Interface

Rejected.

The semantic navigation model must remain independent of presentation
technology.

### Treat Search and Navigation as the Same Capability

Rejected.

Search identifies candidate concepts while navigation traverses semantic
relationships.

### Define a Mandatory Navigation Workflow

Rejected.

ATON provides capabilities for engineering knowledge management and does not
prescribe project-specific engineering processes.

## Migration

Existing physical navigation mechanisms MAY continue to be used.

Implementations SHALL progressively interpret navigation through the canonical
Engineering Knowledge Model.

Existing repository links, document links and user-interface navigation MAY
remain available as access mechanisms.

Where a physical navigation mechanism represents a semantic relationship, the
relationship SHOULD be represented through the canonical Engineering Knowledge
Model.

Migration SHALL NOT require a particular user interface or persistence
technology.

## Acceptance Criteria

A conforming implementation SHALL satisfy at least the following:

1. Navigation can operate on canonical engineering concepts.
2. Navigation can traverse canonical semantic relationships.
3. Navigation does not depend on repository structure.
4. Navigation does not depend on a specific user interface.
5. Navigation targets have semantic identity independent of physical location.
6. Search and navigation remain semantically distinguishable.
7. Reverse traversal does not implicitly create an inverse relation.
8. Navigation respects canonical relation semantics.
9. Historical engineering states can be navigated where they are preserved.
10. External targets remain distinguishable from non-existent targets.
11. Navigation views do not redefine engineering semantics.
12. Project-specific processes are not prescribed by the navigation model.

## References

- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- ADR-0012 — Engineering Version and Baseline Semantics
- ADR-0013 — Entity and Artifact Semantics
- ADR-0014 — Canonical Semantic Relation Model
- ADR-0016 — Engineering Process Model
- ADR-0018 — Engineering Knowledge Navigation
- RFC-0025 — Canonical Relation Model
- RFC-0029 — Canonical Semantic Relation Constraint Model
- NOTE-0018 — Engineering Knowledge Navigation

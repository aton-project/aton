# RFC-0022 — Collections

## Status

Draft

## Summary

This RFC defines the normative semantics of Collections within the ATON
Engineering Knowledge Model.

A Collection is a named and identifiable grouping of engineering knowledge
objects.

A Collection provides an organizational mechanism for grouping existing
engineering knowledge without redefining the semantic meaning of its members.

A Collection is distinct from:

- an Engineering Entity;
- an Engineering Version;
- an Engineering Artifact;
- a Baseline;
- a View;
- a Relation; and
- a physical repository structure.

Collection membership describes which engineering knowledge objects belong to
a Collection.

Membership SHALL NOT by itself change the semantic identity or meaning of a
member.

## Motivation

Engineering projects frequently need to organize engineering knowledge into
logical groups.

Examples include:

- requirements belonging to a subsystem;
- architecture elements belonging to a product area;
- engineering objects belonging to a project;
- documents grouped for a review;
- objects associated with a work package; or
- objects selected for a particular engineering activity.

Repository directories and physical file structures can provide such
organization, but they are implementation-specific and cannot serve as the
canonical semantic model.

ATON therefore requires a semantic mechanism for grouping engineering
knowledge independently of physical storage.

Collections provide this mechanism.

## Goals

This RFC SHALL:

- define the semantics of a Collection;
- define Collection identity;
- define Collection membership;
- allow engineering knowledge to belong to multiple Collections;
- distinguish Collections from Engineering Entities;
- distinguish Collections from Baselines;
- distinguish Collections from Views;
- keep Collection semantics independent of physical repository structure;
- support explicit and deterministic membership; and
- preserve the identity and semantics of Collection members.

## Non-Goals

This RFC does not define:

- project management structures;
- organizational hierarchies;
- repository directory structures;
- Baseline construction;
- Release management;
- View semantics;
- relation predicate semantics;
- process semantics;
- access-control groups;
- user groups;
- database schemas;
- a specific Collection serialization format; or
- user-interface behavior.

Project-specific grouping rules MAY be defined by applicable domain or process
specifications.

## Collection

A Collection SHALL represent a logical grouping of engineering knowledge
objects.

A Collection MAY contain references to:

- Engineering Entities;
- Engineering Versions;
- Engineering Artifacts;
- other Collections; or
- other canonical Engineering Knowledge objects where explicitly permitted
  by the applicable domain model.

A Collection SHALL NOT contain a physical copy of an engineering object merely
for the purpose of establishing membership.

Membership SHALL be represented as a semantic reference to the member.

The semantic identity of a member SHALL remain independent of the Collection
in which it appears.

## Collection Identity

A Collection SHALL have an explicit identity when it participates in the
canonical Engineering Knowledge Model.

Collection identity SHALL NOT be derived solely from:

- a directory path;
- a file name;
- a repository location;
- a database identifier;
- a generated list;
- a timestamp; or
- a user-interface element.

A technical identifier MAY be used for persistence or retrieval.

Such a technical identifier SHALL remain distinguishable from the canonical
Collection identity.

## Collection Membership

Collection membership SHALL identify the engineering knowledge objects that
belong to the Collection.

Membership MAY be explicitly represented or deterministically derived from
authoritative information.

Where membership is derived, the applicable selection rule SHALL be
unambiguous and reproducible.

A Collection SHALL NOT rely on an implicit interpretation such as "all objects
currently present in this directory" unless that rule is explicitly defined
as the authoritative membership rule.

Membership SHALL therefore be a semantic property of the Collection rather
than an accidental consequence of physical storage.

## Multiple Membership

An Engineering Knowledge object MAY belong to multiple Collections.

Membership in one Collection SHALL NOT prevent membership in another
Collection.

For example, the same Engineering Entity MAY belong simultaneously to:

- a subsystem Collection;
- a project Collection; and
- a verification Collection.

Such membership does not create multiple Engineering Entities.

The member retains one canonical identity while participating in multiple
logical groups.

## Collection Membership and Identity

Collection membership SHALL NOT alter the identity of a member.

Moving an Engineering Entity from one Collection to another SHALL therefore
not automatically create a new Engineering Entity.

Likewise, adding or removing Collection membership SHALL NOT automatically
create a new Engineering Version unless the applicable versioning model
defines the membership change as part of the versioned semantic state.

The semantic effect of membership changes SHALL be determined by the
applicable domain model.

## Collections and Engineering Versions

A Collection MAY contain Engineering Versions.

If a Collection is intended to represent a specific engineering state, its
membership SHALL identify the applicable Engineering Versions explicitly.

A Collection SHALL NOT implicitly select the latest version of an Engineering
Entity where multiple versions exist.

For example:

    Collection
        |
        +-- Entity A
        |     |
        |     +-- Version 3
        |
        +-- Entity B
              |
              +-- Version 7

The Collection therefore identifies the selected members rather than merely
their current physical representations.

## Collections and Baselines

A Collection and a Baseline SHALL remain distinct concepts.

A Collection represents a logical grouping of engineering knowledge.

A Baseline represents a defined and reproducible engineering state.

Therefore:

    Collection != Baseline

A Baseline MAY use a Collection as part of its selection mechanism.

A Collection MAY also contain objects that are not part of any Baseline.

Membership in a Collection SHALL NOT automatically establish a Baseline.

Likewise, creating a Baseline SHALL NOT automatically create a Collection.

Baseline semantics are defined separately by RFC-0013.

## Collections and Views

A Collection and a View SHALL remain distinct concepts.

A Collection defines membership.

A View defines a perspective on canonical engineering knowledge.

Therefore:

    Collection != View

A View MAY display a Collection.

A View MAY also use Collection membership as part of its selection criteria.

However, the View SHALL NOT redefine Collection membership merely by
displaying or filtering its members.

View semantics are defined separately by RFC-0021.

## Collections and Relations

Collection membership SHALL remain distinct from ordinary semantic relations.

A Collection MAY reference an Engineering Entity without creating an ordinary
domain relation between the Collection and that entity unless the applicable
relation model explicitly defines such a relation.

Collection membership therefore SHALL NOT automatically be interpreted as a
canonical engineering relation.

Where Collection membership itself requires a canonical semantic relation,
the applicable relation model SHALL define that relation explicitly.

## Nested Collections

Collections MAY contain other Collections where hierarchical organization is
required.

If nested Collections are supported, the membership semantics SHALL be
explicit.

A child Collection SHALL remain independently identifiable.

Membership in a parent Collection SHALL NOT automatically change the semantic
identity of the child Collection.

Implementations SHOULD avoid assuming that nested membership implies
membership of every object contained by the child Collection unless the
applicable Collection model explicitly defines transitive membership.

## Collection Membership Semantics

A Collection MAY define different membership semantics according to its
purpose.

Membership MAY represent:

- explicit selection;
- deterministic selection by rule;
- organizational grouping;
- project association;
- domain classification;
- process-related grouping; or
- another explicitly defined semantic purpose.

The purpose of a Collection SHOULD be identifiable where different
interpretations of membership are possible.

A Collection SHALL NOT silently change the semantic interpretation of its
members.

## Dynamic Collections

A Collection MAY be dynamic.

A dynamic Collection MAY determine its membership from an explicit selection
rule.

For example, a Collection MAY contain all Engineering Entities satisfying a
defined semantic condition.

A dynamic Collection SHALL provide sufficient information to determine its
membership according to the applicable rule.

If the underlying Engineering Knowledge changes, the membership of a dynamic
Collection MAY change.

Such changes SHALL NOT modify the identity or semantic meaning of the member
objects.

## Static Collections

A Collection MAY have explicitly persisted membership.

A static Collection SHALL preserve its defined membership until an explicit
membership change is made according to the applicable governance or domain
rules.

If historical reproducibility is required, the Collection SHOULD reference
immutable Engineering Versions or equivalent stable engineering states.

## Collection Comparison

Two Collections MAY be compared.

Comparison MAY identify:

- added members;
- removed members;
- common members;
- changed member versions; or
- other membership differences.

Collection comparison SHALL operate on canonical engineering identities where
possible.

A comparison of the physical representations of two Collections SHALL NOT
automatically be treated as a semantic Collection comparison.

## Collection History

Collection membership MAY evolve over time.

Changes to Collection membership SHALL NOT implicitly modify the historical
identity of member objects.

Where Collection history is required, the applicable versioning or historical
model SHALL preserve sufficient information to reconstruct relevant
membership states.

A Collection history SHOULD distinguish between:

- changes to the Collection itself; and
- changes to the Engineering Knowledge objects that are members of the
  Collection.

## Collection and Physical Representation

A Collection MAY be physically represented through:

- YAML;
- Markdown;
- JSON;
- database records;
- APIs;
- repository files;
- generated documents; or
- other persistence mechanisms.

The physical representation SHALL NOT define the semantic meaning of the
Collection.

In particular, a repository directory SHALL NOT automatically be considered
a canonical Collection.

A directory MAY provide a physical representation of Collection membership
when an applicable mapping explicitly establishes that relationship.

## Collection and Repository Structure

ATON repositories MAY use directories to organize physical artifacts.

Such directories are physical representations and SHALL remain distinct from
canonical Collections.

For example:

    repository/
        requirements/
        architecture/
        verification/

does not by itself establish three canonical Collections.

A Collection MAY be mapped to such directories, but the mapping SHALL be
explicit and SHALL NOT cause repository structure to become the semantic
definition of the Collection.

## Collection Verification

ATON MAY verify Collection consistency.

Verification MAY detect:

- duplicate Collection identifiers;
- missing Collection members;
- unresolved member references;
- invalid member types;
- invalid version references;
- inconsistent dynamic selection rules;
- invalid nested Collection relationships; or
- other violations defined by applicable Collection specifications.

Verification SHALL operate on canonical Collection semantics.

Successful storage or rendering SHALL NOT by itself establish semantic
validity.

## Persistence Independence

The Collection model SHALL remain independent of persistence technology.

A conforming implementation MAY persist Collections in:

- Git;
- databases;
- object stores;
- APIs;
- other repositories; or
- alternative persistence systems.

The persistence mechanism SHALL NOT determine the semantic identity or
membership semantics of a Collection.

## Consequences

### Positive

- Engineering knowledge can be organized independently of physical storage.
- The same engineering object can participate in multiple logical groups.
- Collections can support project, subsystem and process-specific
  organization.
- Collection membership remains distinct from semantic identity.
- Collections can be used by Views and Baselines without replacing them.
- Alternative

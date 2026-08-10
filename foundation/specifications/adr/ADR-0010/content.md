# Canonical Metadata Domain Model

## Context

ATON engineering artifacts contain metadata describing their identity, semantic classification, lifecycle and other engineering properties.

Some information may also be available from persistence systems such as Git, databases or external engineering systems.

The ATON domain model must remain independent of the availability, capabilities and implementation details of any particular persistence system.

In particular, canonical engineering metadata must remain available when an artifact is moved between different persistence implementations.

## Problem Statement

The ATON architecture requires a canonical metadata model that is independent of physical persistence and representation.

Canonical metadata must therefore be explicitly represented as part of the Engineering Knowledge Model.

Information that can be derived from Git, the Engineering Knowledge Graph, persistence systems or other sources may be useful to ATON, but such information must not be required for the existence or semantic validity of the canonical model.

## Decision

ATON SHALL define canonical metadata as explicitly represented metadata belonging to the Engineering Knowledge Model.

Every canonical metadata value SHALL be explicitly represented in the canonical model or in its authoritative persisted representation.

Canonical metadata SHALL NOT depend on information that is available only from a particular persistence implementation.

The absence of a particular persistence system or its derived information SHALL NOT make an otherwise valid ATON artifact semantically incomplete.

## Canonical Metadata

Canonical metadata SHALL describe semantic properties of engineering knowledge.

Examples include:

- engineering identity
- title
- ontology type
- lifecycle status
- other metadata explicitly defined as normative by the Foundation

Canonical metadata SHALL have a defined semantic meaning independent of its physical serialization.

The physical location of a metadata value SHALL NOT determine its semantic meaning.

## Explicit Representation

Canonical metadata SHALL be explicitly represented.

For example, an artifact may explicitly contain identity, title, lifecycle status and ontology type as part of its canonical metadata.

These values are part of the canonical engineering representation.

They SHALL remain available independently of whether the artifact is stored in Git, a database, an API-backed repository or another persistence system.

## Derived Information

ATON implementations MAY derive additional information from authoritative external or technical sources.

Possible sources include:

- Git history
- the Engineering Knowledge Graph
- databases
- external engineering systems
- persistence-specific metadata

Derived information MAY be used for:

- navigation
- analysis
- reporting
- search
- views
- diagnostics
- caching
- other non-canonical purposes

Derived information SHALL NOT replace canonical metadata.

Derived information SHALL NOT be required for an artifact to constitute a valid canonical ATON representation.

If derived information is unavailable because a persistence implementation does not provide it, the canonical Engineering Knowledge Model SHALL remain valid.

## Materialization

An implementation MAY materialize derived information as explicit engineering metadata.

Once materialized as canonical metadata, the value SHALL be governed by the same semantic and persistence rules as other canonical metadata.

Materialization SHALL therefore be an explicit architectural operation and SHALL NOT occur implicitly merely because an implementation can derive a value.

## Temporal Information

Temporal information SHALL follow the same distinction.

A timestamp may describe:

- an engineering event
- a Git event
- a database event
- a physical representation event
- another implementation-specific event

These meanings SHALL NOT be conflated.

For example, a file modification timestamp is a property of a physical representation and SHALL NOT automatically become the modification time of the corresponding engineering artifact.

Git timestamps MAY provide useful derived information, but SHALL NOT automatically define canonical engineering timestamps.

Temporal semantics belonging to the canonical Engineering Knowledge Model MUST therefore be explicitly represented.

Temporal metadata SHALL remain separate from engineering version semantics.

## Metadata Authority

Every canonical metadata value SHALL have a defined source of authority.

The authoritative value SHALL be the value represented by the canonical Engineering Knowledge Model.

A derived value from another source SHALL NOT silently override canonical metadata.

If an implementation detects a conflict between canonical metadata and derived information, the conflict SHALL be reported or otherwise handled according to the applicable verification or governance rules.

The implementation SHALL NOT silently redefine the canonical metadata based on a derived value.

## Persistence Independence

Canonical metadata SHALL be portable between persistence implementations.

The canonical metadata SHALL remain semantically equivalent when an artifact is transferred between different persistence implementations.

A persistence implementation MAY provide additional derived information, but the availability of such information SHALL NOT change the semantics of the canonical model.

## Metadata and Physical Representation

Metadata semantics SHALL be independent of serialization.

A YAML field, Markdown front matter field, database column or API property is a physical representation of metadata rather than its semantic definition.

Loaders SHALL translate persisted metadata into the canonical domain model.

Renderers and exporters SHALL derive physical metadata representations from the canonical domain model.

Kernel components SHALL operate on canonical metadata semantics rather than on persistence-specific structures.

## Metadata Ownership

Metadata SHALL belong to the logical engineering concept that it describes.

An implementation MAY store metadata together with a physical artifact, but physical co-location SHALL NOT change metadata ownership.

Metadata describing an engineering entity SHALL therefore remain distinguishable from metadata describing a physical representation.

## Consequences

### Positive

- Canonical metadata remains portable across persistence implementations.
- The ATON model does not depend on Git-specific information.
- Alternative persistence systems do not need to reproduce Git semantics.
- Derived information can still enrich navigation, analysis and tooling.
- The distinction between semantic information and technical information remains explicit.
- Canonical artifacts remain valid even when supplemental derived information is unavailable.

### Negative

- Some useful information must be explicitly represented rather than inferred.
- Implementations must distinguish canonical metadata from derived information.
- Conflicts between canonical metadata and derived information must be detected and handled explicitly.
- Additional persistence systems may require explicit mapping of canonical metadata.

## Relationship to Other Decisions

ADR-0011 defines the separation between the logical Engineering Knowledge Model and its physical representations.

This decision defines the canonical semantic treatment of metadata within that model.

Engineering version, baseline and release semantics are defined separately from the metadata model.

Relation semantics and predicate constraints are defined by the canonical relation architecture and corresponding Foundation specifications.

## Alternatives Considered

### Derive canonical metadata from persistence

Rejected.

This would make the semantic completeness of the ATON model dependent on the capabilities of a particular persistence implementation.

### Treat all persisted metadata as authoritative

Rejected.

Physical persistence does not by itself determine semantic authority.

### Allow implementations to choose which metadata is canonical

Rejected.

This would prevent consistent interpretation across ATON implementations.

### Store both explicit and derived values as equally authoritative

Rejected.

Canonical metadata requires a single semantic authority. Derived information may supplement the model but must not silently redefine it.

## Expected Outcome

ATON SHALL provide a canonical metadata domain model in which canonical metadata is explicitly represented and independent of physical persistence.

Implementations MAY provide derived information as supplemental information, but the absence of such information SHALL NOT invalidate or alter the canonical Engineering Knowledge Model.

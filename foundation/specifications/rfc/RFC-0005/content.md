# RFC-0005 — Property Model

## Status

Draft

## Summary

This RFC defines the generic semantic concept of a Property within the ATON
Engineering Knowledge Model.

A Property represents a named characteristic or value associated with an
engineering concept.

Properties provide a generic mechanism for describing engineering concepts
without coupling their semantic meaning to a particular physical
representation.

Canonical metadata is a specific semantic use of properties and is governed
by RFC-0003 and ADR-0010.

This RFC therefore defines the generic Property concept while avoiding a
second, competing metadata model.

## Motivation

Engineering concepts have characteristics that describe their identity,
classification, state and other semantic properties.

Examples include:

- title;
- lifecycle status;
- ontology type;
- engineering identity;
- configuration attributes; or
- other domain-specific characteristics.

These characteristics may be represented physically as YAML fields, Markdown
front matter, database columns, API fields or other structures.

The physical representation must not define the semantic meaning of the
property.

ATON therefore requires a generic semantic concept for properties that is
independent of persistence and serialization.

## Goals

This RFC SHALL:

- define the semantic concept of a Property;
- define the relationship between a Property and an engineering concept;
- distinguish property semantics from physical representation;
- distinguish canonical properties from derived information;
- support typed property values;
- provide a foundation for canonical metadata;
- preserve persistence independence; and
- allow domain-specific property definitions.

## Non Goals

This RFC does not define:

- the complete set of canonical ATON metadata;
- metadata ownership rules;
- the canonical metadata model;
- a specific serialization format;
- a specific database schema;
- a specific API representation;
- ontology-specific property definitions;
- property validation rules for individual domains;
- derived information algorithms; or
- a user-interface representation of properties.

Canonical metadata semantics are defined by ADR-0010 and RFC-0003.

## Proposal

### Property

A Property SHALL represent a named semantic characteristic of an engineering
concept.

Conceptually:

    Engineering Concept
            |
            +-- Property
                    |
                    +-- name
                    +-- value

A Property SHALL have a semantic definition independent of its physical
representation.

### Property Name

A Property SHALL have a name identifying the characteristic it represents.

The semantic meaning of a property name SHALL be defined by the applicable
domain model, ontology or specification.

A property name alone SHALL NOT determine the complete semantic contract of a
property where additional constraints are required.

### Property Value

A Property SHALL have a value unless the applicable property definition
explicitly permits a value-less property.

Property values MAY represent:

- strings;
- numbers;
- booleans;
- identifiers;
- enumerated values;
- dates or timestamps;
- structured values;
- collections; or
- other types defined by the applicable domain model.

The semantic type of a property value SHALL be determined by the property
definition rather than by its physical serialization.

### Property Ownership

A Property SHALL belong semantically to the engineering concept that it
describes.

Physical co-location SHALL NOT determine property ownership.

For example, a property stored in a physical artifact does not necessarily
describe the physical artifact itself.

The property may instead describe:

- an Engineering Entity;
- an Engineering Version;
- an Engineering Artifact;
- a Process;
- a Baseline;
- a Release; or
- another canonical engineering concept.

### Property Semantics

The meaning of a Property SHALL be determined by its semantic definition.

The same physical field name MAY have different meanings in different
contexts unless the applicable ontology explicitly defines them as the same
property.

Implementations SHALL therefore not infer semantic equivalence solely from
identical field names.

### Canonical Properties

A Property MAY be designated as canonical by the applicable ATON domain model.

A canonical Property SHALL be explicitly represented in the authoritative
Engineering Knowledge Model.

Canonical properties SHALL remain semantically available independently of
the persistence mechanism.

Canonical metadata is governed by ADR-0010.

### Metadata as Semantic Properties

Canonical metadata SHALL be treated as a defined class of semantic
properties.

Examples include:

- engineering identity;
- title;
- ontology type;
- lifecycle status; or
- other metadata explicitly defined as normative.

RFC-0003 defines the canonical Metadata Model.

This RFC does not redefine metadata semantics.

### Derived Properties

An implementation MAY derive additional properties from authoritative
engineering information or technical sources.

Possible sources include:

- Git;
- the Engineering Knowledge Graph;
- databases;
- external engineering systems; or
- physical representations.

Derived properties SHALL remain distinguishable from canonical properties
unless they are explicitly materialized as canonical information.

A derived property SHALL NOT silently replace a canonical property.

### Materialized Properties

An implementation MAY materialize a derived property as canonical
engineering information.

Such materialization SHALL be explicit.

Once materialized as canonical information, the property SHALL be governed by
the semantic and authority rules applicable to canonical properties.

### Property Type

A Property definition MAY specify an expected value type.

The value type MAY constrain:

- permitted value forms;
- comparison semantics;
- ordering;
- units;
- allowed enumerations;
- cardinality; or
- other applicable semantic characteristics.

Property type semantics SHALL be defined by the applicable property or
ontology specification.

### Property Multiplicity

A Property definition MAY specify whether a property accepts:

- a single value;
- multiple values; or
- a structured value.

Multiplicity SHALL be a semantic property of the Property definition.

An implementation SHALL NOT infer multiplicity solely from the physical
serialization format.

### Property Units

A Property definition MAY specify a unit or unit system for numerical values.

Where units are semantically relevant, the unit SHALL be part of the semantic
interpretation of the property value.

A physical representation SHALL NOT change the semantic unit of a Property.

### Property Constraints

A Property definition MAY specify constraints such as:

- value type;
- allowed values;
- value ranges;
- cardinality;
- units;
- formatting;
- lifecycle applicability;
- version applicability; or
- other domain-specific constraints.

Property constraints SHALL be defined separately from the generic Property
concept.

### Property and Engineering Versions

Properties MAY vary between Engineering Versions.

A change to a canonical property MAY therefore contribute to the creation of
a new Engineering Version when the change affects the semantic engineering
state.

The existence of a changed property value SHALL NOT by itself determine
whether a new Engineering Version is required.

Engineering Version semantics are defined separately by RFC-0012.

### Property and Physical Representation

A Property SHALL remain independent of its physical representation.

A Property MAY be represented through:

- YAML;
- Markdown;
- JSON;
- a database;
- an API;
- a Git repository; or
- another persistence mechanism.

A YAML field, database column or API attribute is a physical representation
of a property and is not itself the semantic definition of the property.

### Property and Serialization

Different physical serialization formats MAY represent the same semantic
Property.

For example, the following representations MAY describe the same semantic
property:

    title: Braking System

or:

    {
      "title": "Braking System"
    }

The serialization mechanism SHALL NOT alter the semantic meaning of the
Property.

### Property Identity

The semantic identity of a Property SHALL be independent of:

- file path;
- field position;
- database column;
- serialization format;
- repository location; or
- user-interface representation.

Where a Property itself requires a persistent identity, that identity SHALL
be defined by the applicable domain model.

### Property Verification

Implementations MAY verify properties against their applicable definitions.

Verification MAY identify:

- unknown properties;
- missing required properties;
- invalid value types;
- invalid values;
- invalid multiplicity;
- invalid units;
- conflicting canonical and derived values; or
- other property constraint violations.

Property verification SHALL operate on canonical property semantics rather
than physical serialization structures.

### Property and the Canonical Domain Model

The ATON kernel SHALL operate on canonical semantic properties rather than
persistence-specific property structures.

Loaders SHALL normalize physical property representations into the canonical
domain model.

Renderers and exporters SHALL derive physical property representations from
the canonical domain model.

## Consequences

### Positive

- Property semantics are independent of persistence.
- Metadata can be defined as a specialized semantic use of properties.
- Physical serialization does not determine semantic meaning.
- Typed and constrained properties can be supported.
- Derived information remains distinguishable from canonical information.
- Different persistence and exchange formats can represent the same property.

### Negative

- Property definitions require explicit semantic modeling.
- Implementations must distinguish canonical and derived properties.
- Typed and constrained properties require additional validation logic.
- Property evolution may interact with Engineering Version semantics.

## Alternatives

### Treat every physical field as a Property

Rejected.

A physical field is a representation mechanism and does not necessarily have
canonical semantic meaning.

### Treat Properties and Metadata as completely separate concepts

Rejected.

Canonical metadata describes semantic characteristics of engineering
concepts and is therefore naturally modeled as a defined class of properties.

### Derive all Properties from persistence

Rejected.

This would make the semantic completeness of the Engineering Knowledge Model
dependent on a particular persistence implementation.

### Define all properties directly in the serialization format

Rejected.

Serialization formats must remain physical representations of the canonical
model rather than defining its semantics.

### Make every property globally applicable

Rejected.

Property applicability depends on the engineering concept and the applicable
domain model or ontology.

## Migration

Existing metadata and property-like fields SHALL be classified according to
their semantic role.

Migration SHOULD:

1. identify existing property-like information;
2. determine its semantic owner;
3. determine whether it is canonical or derived;
4. identify its semantic definition;
5. identify its value type where applicable;
6. preserve existing canonical information;
7. normalize physical representations into the canonical model; and
8. validate applicable property constraints.

Existing physical fields SHALL NOT automatically become canonical properties
merely because they are persisted.

Existing canonical metadata SHALL be migrated according to the canonical
metadata model defined by ADR-0010 and RFC-0003.

## Open Questions

The following questions remain subject to further specification:

- Which property types are required by the ATON Foundation?
- How are property definitions identified?
- Which property constraints belong to the generic model?
- How should structured property values be represented canonically?
- How should property inheritance be modeled, if required?
- How should property values evolve across Engineering Versions?
- Which ontology mechanisms define property applicability?
- How should property provenance be represented?
- How should units and unit conversions be modeled?
- Which properties are mandatory for individual engineering concepts?

These questions MAY be addressed by subsequent ontology, metadata and domain
specifications.

## References

- ADR-0010 — Canonical Metadata Domain Model
- ADR-0011 — Logical Engineering Knowledge Model and Physical Representations
- RFC-0003 — Metadata Model
- RFC-0012 — Engineering Version Semantics
- RFC-0015 — Logical Engineering Knowledge and Physical Representations

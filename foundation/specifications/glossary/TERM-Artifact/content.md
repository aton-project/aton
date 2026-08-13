# Artifact

## Definition

An Engineering Artifact is a persisted or otherwise addressable representation
of engineering information within ATON.

An Artifact may contain engineering content, canonical metadata, relations or
other explicitly defined artifact components.

An Artifact provides a representation of engineering information but does not
automatically constitute the semantic identity of an Engineering Entity.

## Role in ATON

Artifact is a fundamental term of the ATON Engineering Knowledge Model.

Artifact identity and Engineering Entity identity SHALL remain conceptually
distinct.

An Engineering Entity MAY be represented by one or more Artifacts.

An Artifact MAY represent one or more Engineering Entities when the artifact
format explicitly supports such representation.

The relationship between an Entity and an Artifact SHALL NOT be inferred
solely from physical location.

## Persistence Independence

The physical representation of an Artifact MAY change without changing the
identity of the Engineering Entity represented by that Artifact.

An Artifact MAY therefore be replaced, transformed, migrated or regenerated
without necessarily creating a new Engineering Entity.

## Relationship to the Artifact Model

The normative Artifact ontology concept is defined by ONT-Artifact.

The Glossary Entry defines the terminology used to refer to this concept. It
does not replace or redefine the normative Artifact model.

## Related Terms

- Entity
- Engineering Knowledge
- Engineering Knowledge Model
- Artifact Revision

## References

- ADR-0013 — Entity and Artifact Semantics
- ONT-Artifact

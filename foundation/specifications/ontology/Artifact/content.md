# Artifact

## Status

Draft

## Definition

An Engineering Artifact is a persisted or otherwise addressable representation
of engineering information within ATON.

An Artifact may contain engineering content, canonical metadata, relations or
other explicitly defined artifact components.

An Artifact provides a representation of engineering information but does not
automatically constitute the semantic identity of an Engineering Entity.

## Role in ATON

This ontology concept defines the semantic category of Engineering Artifacts
within the ATON Foundation.

An Artifact is part of the physical or addressable representation of the
Engineering Knowledge Model.

Artifact identity and Engineering Entity identity SHALL remain conceptually
distinct. In the normal one-Entity/one-Artifact case, they MAY use the
same identifier value without requiring a second technical Artifact ID.

`artifactType`, when applicable, classifies the Engineering Artifact.
`ontologyType` classifies the Engineering Entity represented by it. Physical
co-location in `metadata.yaml` SHALL NOT change their semantic ownership.

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

## References

- ADR-0013 — Entity and Artifact Semantics
- ENTITY-0001 — Universal Entity Model

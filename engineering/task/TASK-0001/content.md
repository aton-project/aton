# TASK-0001 — Analyze Entity, Artifact and Physical Representation

## Status

Draft

## Purpose

Analyze and clarify the semantic distinction between:

- Entity
- Artifact
- Physical Representation

within the ATON architecture.

## Context

ATON currently contains multiple definitions and models concerning
Entities, Artifacts, physical repository representations, identity,
versioning, metadata, relations and ontology typing.

The analysis shall determine whether these concepts are consistently
distinguished across the ATON Foundation and identify contradictions,
ambiguities and unresolved semantic questions.

## Established Working Decision

For the purpose of this task, ATON shall distinguish:

- Entity
- Artifact
- Physical Representation

These concepts shall not be treated as interchangeable.

This task does not, by itself, establish that Entity and Artifact are
disjoint categories, nor does it establish a mandatory cardinality
between them.

## Scope

The analysis shall examine, at minimum:

- the ATON Constitution
- relevant accepted ADRs
- relevant proposed ADRs
- the Universal Entity Model
- Entity and Artifact ontology definitions
- relevant RFCs
- relevant glossary definitions
- identity and versioning definitions
- relation and predicate definitions
- metadata definitions
- the canonical repository representation
- relevant tooling where it affects the semantic model

## Questions

The analysis shall determine:

1. What is an Entity?
2. What is an Artifact?
3. What is a Physical Representation?
4. How are the three concepts related?
5. Which identities belong to which level?
6. How are versions and revisions related to the three levels?
7. What is the role of `ontologyType`?
8. How are relations affected by the distinction?
9. What is the role of metadata at each level?
10. How is the canonical ATON repository representation related to
    Artifacts and Physical Representations?
11. Which existing definitions support the distinction?
12. Which existing definitions conflict with or leave the distinction
    ambiguous?
13. Which questions require explicit architectural decisions?

## Constraints

This task is analytical.

No normative Foundation definition, ADR, RFC, ontology definition,
schema or tooling implementation shall be modified as part of this task.

Draft and Proposed documents shall not be treated as accepted
architecture.

The analysis shall distinguish documented facts, supported
interpretations, open questions and proposed clarifications.

## Expected Result

The resulting analysis shall be stored separately from this Task.

The analysis shall be written in English and explicitly marked as
non-normative engineering analysis.

The analysis shall preserve the original repository state on which it
was based.

## Execution

A concrete execution order for Codex shall be derived from this Task.

The Codex execution may create, commit and push the resulting
unreviewed analysis.

The original agent result shall subsequently be reviewed separately.

Review corrections shall not amend the original analysis commit.

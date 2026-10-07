Review and correct the Foundation's ontologyType ownership

Objective

Review the ATON Foundation for all definitions and statements concerning
`ontologyType` and ensure that they are consistent with the following
architectural decision:

- `ontologyType` belongs to the Engineering Entity.
- `artifactType` belongs to the Engineering Artifact.
- The physical co-location of these values in `metadata.yaml` does not
  change their semantic ownership.
- Entity Identity and Artifact Identity are semantically distinct, but
  may use the same identifier value for the normal one-entity/one-artifact
  case.

Tasks

1. Search the complete Foundation for all occurrences and definitions of
   `ontologyType`.

2. Identify every place where `ontologyType` is currently assigned to,
   defined as belonging to, or otherwise semantically associated with an
   Engineering Artifact rather than an Engineering Entity.

3. Correct those inconsistencies so that `ontologyType` is consistently
   defined as an Entity-level classification.

4. Review the corresponding use of `artifactType`.
   Where the Foundation already defines or requires an Artifact Type,
   ensure that it is clearly associated with the Engineering Artifact
   rather than the Engineering Entity.

5. Pay particular attention to:
   - ADR-0008
   - RFC-0020
   - ENTITY-0001
   - RFC-0010
   - RFC-0030
   - ontology definitions
   - schemas
   - glossary entries
   - other Foundation artifacts referencing ontologyType or artifactType

6. Do not invent new ontology concepts, predicates, relations, identifiers,
   or semantics.

7. Do not redesign the Entity/Artifact model beyond what is required to
   make the existing Foundation consistent with the architectural
   decision above.

8. Preserve the distinction between:
   - Engineering Entity
   - Engineering Artifact
   - Physical Representation

9. Check whether existing examples or schemas contradict the corrected
   semantics and correct them where necessary.

10. Run the repository's applicable validation/tests after the changes.

11. Produce a concise analysis of:
    - all affected files,
    - the inconsistency found,
    - the correction made,
    - any remaining ambiguity that cannot be resolved from the existing
      Foundation.

Constraints

- Work only on branch `development`.
- Do not modify unrelated content.
- Do not change existing artifact IDs or Entity IDs.
- Do not introduce a second technical Artifact ID merely to distinguish
  Entity and Artifact identities.
- Do not add new predicates to solve this issue.
- Do not modify historical commits.
- Keep the changes reviewable and limited to the semantic correction.

Expected result

The Foundation shall consistently express:

    Entity
      └── ontologyType

    Artifact
      └── artifactType (when applicable)

with both potentially being physically serialized together in the
canonical artifact representation's `metadata.yaml`.

The final result must make this distinction explicit without confusing
physical serialization with semantic ownership.

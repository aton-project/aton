Perform a complete semantic review of the entire ATON Foundation repository with particular focus on the consistent distinction between:

- Engineering Entity
- Engineering Artifact
- Physical Representation

and on the semantic ownership of:

- `ontologyType`
- `artifactType`
- Metadata
- Properties
- Relations
- Predicates
- Content
- Identity
- Revision
- Version

The review shall be performed against the actual current repository state on branch `development`.

Architectural basis

Use the following decisions as the current review basis:

Entity
  └── ontologyType

Artifact
  └── artifactType (when applicable)

Physical Representation
  └── concrete technical manifestation

Entity Identity and Artifact Identity are
semantically distinct, but may use the same
identifier value in the normal one-entity/
one-artifact case.

Physical co-location in metadata.yaml does
not determine semantic ownership.

Also preserve the distinction between:

logical semantic model
        ↓
Engineering Entity / Engineering Artifact
        ↓
Physical Representation
        ↓
content.md / metadata.yaml / relations.yaml

Scope

Review all files below `foundation/`.

Do not limit the review to previously identified ADRs/RFCs.

The review shall include, where applicable:

- Constitution
- ADRs
- RFCs
- ENTITY-0001
- ontology definitions
- glossary entries
- predicates
- predicate constraints
- schemas
- templates
- Foundation README/reference material
- AX material
- examples

Search dimensions

Do not perform only a literal keyword search.

Also inspect semantic usage involving concepts such as:

Entity
Artifact
Physical Representation
representation
file
document
directory
repository
serialization
persistence
content
metadata
property
relation
predicate
identity
revision
version
type
classification
generated
rendered
exchange
database
API
Git

Determine from context what semantic layer each statement actually refers to.

Classification

For every relevant inconsistency or ambiguity, classify it as:

- CONTRADICTION — incompatible with the current architectural model
- AMBIGUITY — wording permits conflicting interpretations
- CONSISTENT — compatible with the current model
- HISTORICAL / NON-NORMATIVE — documents an earlier analysis or state and should not be changed merely for consistency

For every finding record:

1. file
2. section / relevant passage
3. semantic interpretation
4. affected concept/layer
5. classification
6. explanation
7. whether a correction appears necessary
8. dependencies on other Foundation statements, if identifiable

Important

Do not resolve contradictions yourself.

Do not modify existing Foundation semantics.

Do not modify any existing Foundation artifact.

Do not modify:

- ADRs
- RFCs
- ontology definitions
- glossary entries
- schemas
- templates
- metadata
- relations
- AX documents
- Constitution
- any other existing Foundation file

Do not change existing IDs or versions.

Do not add predicates.

Do not introduce new ontology concepts.

Do not modify historical commits.

Do not refer to this analysis as K2.

The identifier K2 is already assigned to `engineering/analysis/terminology/ATON-Terminology-Inventory.md` and SHALL NOT be reused or implicitly referenced.

Only permitted repository change

The only permitted repository change is creation of the review report itself.

Create:

engineering/analysis/architecture/Foundation-Semantic-Review.md

The report shall contain the original complete analysis result produced by this task.

Do not subsequently rewrite, summarize, normalize or correct the report.

The report itself is an analysis artifact and is not normative.

Validation

After creating the report:

- run applicable repository validation if practical;
- verify that no existing repository files were modified;
- verify that the only change is the new report.

Then create a dedicated commit, for example:

docs(analysis): add Foundation semantic review

Push the commit to:

origin/development

Expected result

A committed and pushed report providing a complete, repository-wide semantic inventory of the current Foundation regarding:

Entity
Artifact
Physical Representation
ontologyType
artifactType
Metadata
Property
Relation
Predicate
Content
Identity
Revision
Version

The report must explicitly distinguish confirmed contradictions from mere ambiguities and must not modify the Foundation itself.

TASK-0005 — Consolidate Foundation Semantic Decisions

Objective

Create a dedicated ATON decision artifact that consolidates the decisions made during the semantic review of the ATON Foundation.

The primary source for the review findings is:

"engineering/analysis/architecture/Foundation-Semantic-Review.md"

First, inspect the current repository, branch, existing task artifacts, identifier conventions, ontology definitions, and relevant Foundation specifications.

Determine the appropriate location, identifier, and physical representation for a general Decision Entity based on the conventions actually established in the repository. Do not assume that a "DEC-" identifier scheme or a particular directory structure already exists. If the conventions do not support an unambiguous choice, stop and report the issue without creating a speculative artifact.

Scope and Constraints

- Create only the consolidated decision artifact and the files required for its physical representation.
- Do not modify any existing Foundation artifact.
- Do not modify the semantic review report.
- Do not modify existing tasks or previous commits.
- Do not create correction tasks at this stage.
- Do not implement any Foundation corrections.
- Do not introduce new ontology concepts, predicates, identifier schemes, or model rules.
- Do not silently resolve questions that remain undecided.
- Clearly distinguish agreed decisions, implementation implications, and unresolved questions.
- Use only existing, valid relation predicates. Do not invent new predicates.
- Follow the repository's established artifact structure and metadata conventions. If the required representation depends on an unresolved model decision, stop and report the issue.

Decisions to Consolidate

1. Entity and Identity

1. An Entity is an independently identifiable object of the ATON Engineering Model.
2. Entity identity is independent of file names, directory paths, formats, and physical representations.
3. Every Entity MUST have exactly one primary canonical "ontologyType". This rule applies universally, including to ontology concepts and Foundation artifacts.
4. An unknown or missing type during migration represents incomplete data, not an exception to the model.
5. A specification may aggregate or reference other Entities. It is not necessarily the smallest independently identifiable unit of engineering knowledge.

2. Entity, Artifact, and Physical Representation

1. An Entity is an identifiable engineering object.
2. An Artifact is a logically identifiable representation. It may represent one Entity, multiple Entities, or organize information without representing a particular Entity.
3. A Physical Representation is the concrete technical manifestation of an Artifact, such as files, Git objects, database records, API resources, or generated documents.
4. An Entity may have multiple Artifacts, and an Artifact may represent multiple Entities.
5. Entity identity and Artifact identity are semantically distinct, although they may use the same identifier value in the normal one-to-one case.
6. Do not introduce a second Artifact identifier solely to distinguish these semantic roles.
7. "ontologyType" classifies an Entity. "artifactType", when applicable, classifies an Artifact. Storing both values in the same "metadata.yaml" file does not change their semantic ownership.
8. Artifact Type remains optional unless required by the relevant domain.
9. Artifact components do not automatically become Entities.

3. Properties, Metadata, and Physical Files

1. Properties represent domain-specific, substantive information. Metadata represents administrative information.
2. "content.md" contains substantive content.
3. "properties.yaml" stores substantive properties.
4. "metadata.yaml" stores administrative metadata.
5. "relations.yaml" stores relations.
6. The physical location of a value does not determine its semantic ownership. Properties and metadata may belong to Entities or other model objects where the model defines such ownership.
7. The canonical physical representation requires all mandatory files, including "relations.yaml" when no relations exist. An empty relation collection may be represented as "[]".
8. The nine directories identified in finding F65 must ultimately be brought into conformity: AX-0004 through AX-0010, the ontology AX artifact, and the ontology Constitution artifact. This task MUST NOT modify those directories.

4. Relation Semantics and Serialization

1. Relations express engineering semantics between Entities. A Predicate defines the type of a relation.
2. Neither a Relation nor a Predicate is itself an Entity.
3. A canonical Relation MUST always contain explicit "source", "predicate", and "target" values.
4. A physical serialization may omit "source" only when an explicit and unambiguous serialization rule makes it uniquely reconstructable.
5. If an Artifact represents multiple Entities, the source Entity of each semantic relation MUST be explicit.
6. The loader reconstructs the complete canonical Relation, and the validator checks it. An ambiguous source is an error and MUST NOT be guessed.
7. A relation physically stored in an Artifact does not make that Artifact the semantic endpoint.
8. The "references" Predicate represents a semantic Entity-to-Entity relation. Initially, no Entity-type combinations are excluded unless an explicit constraint defines that exclusion.
9. Technical references between files or Artifacts are distinct from semantic relations between Entities.
10. Predicate definitions are the authoritative source of rules governing valid source and target types. Specialization or inheritance applies only where explicitly defined. Explicit exceptions are permitted; arbitrary implicit combinations are not.
11. The Predicate rule mechanism, concrete Predicate constraints, and validator behavior MUST be aligned.
12. Serialization examples and historical migration candidates do not implicitly establish new canonical Predicates.
13. In particular, "dependsOn", "relatedTo", "supersedes", and "supersededBy" MUST NOT become canonical merely because they appear in examples.

5. Versioning, Lifecycle, and Review

1. An Engineering Version is determined by the substantive engineering state, not by every file change.
2. Changes to "content.md" or "properties.yaml" require a new Engineering Version and a substantive engineering review.
3. Administrative changes to "metadata.yaml" do not automatically require an Engineering Version increment.
4. An administrative lifecycle-status change does not automatically invalidate an existing substantive engineering review.
5. Relation changes require an Engineering Version increment or review when they materially change the substantive engineering state and are not already covered by a valid review.
6. Adding a Downlink does not automatically require another review of the Entity containing it if the corresponding Uplink is already covered by a valid review. For example, a System Requirement may gain a Downlink to a Software Requirement whose Uplink has already been reviewed.
7. Lifecycle status belongs exclusively in "metadata.yaml". It MUST NOT appear as a status field or section in "content.md". Conflicting status values MUST NOT be resolved by precedence; status in "content.md" is prohibited.
8. A substantive change to an Entity representing an ontology definition follows the general rules for Engineering Versioning and review.
9. Changing an ontology definition does not automatically version every instance classified by that definition. Instances require review or adjustment when the change affects their substantive meaning or validity.
10. Existing Engineering Versions MUST NOT be renumbered retroactively merely because these rules have been clarified.
11. Canonical values MUST be explicitly available as required by the model contract. The fact that a canonical value can be reconstructed does not, by itself, justify omitting it. Supplemental derived information may remain unpersisted if no other normative rule requires it.

Engineering Versions, Artifact Revisions, and Git history are distinct concepts and MUST NOT be treated as interchangeable.

6. Examples and Historical Material

1. Examples should accurately represent the current model.
2. Examples may illustrate proposed or unsupported relations only when explicitly marked as non-normative and proposed.
3. Examples do not implicitly introduce Predicates or expand constraints.
4. Historical migration observations, rejected alternatives, and hypothetical mappings remain historical or non-normative unless an operative rule explicitly adopts them.
5. Historical material MUST NOT be rewritten automatically merely to normalize its terminology.
6. Successful verification or rendering tests do not, by themselves, prove complete semantic coherence.

7. Entity Types and Ontology Concepts

The following are treated as Entity types or specialized Entities in the agreed model:

- Requirement
- Specification
- Component
- Interface
- Decision
- ADR
- Baseline
- Test Case
- Test Procedure
- Test Result
- Note
- RFC
- Finding
- Review
- GlossaryEntry
- Constitution
- Definition
- Collection
- View

The following are not Entities in this model:

- Artifact
- Physical Representation
- Property
- Metadata
- Relation
- Predicate
- Test Execution
- AX

Further clarifications:

1. Finding, Review, and Note are Entities. Their corresponding ontology concepts define their types.
2. A Note may exist without a relation to another Entity.
3. A Finding is tied to a specific review context. The same factual observation in another Review is represented by a new Finding. Different Reviews MUST NOT refer to the same Finding.
4. Review is an independently managed engineering object, not an Activity. Activities may include Inspection or Check.
5. Test Case, Test Procedure, and Test Result are Entities. Test Execution provides the context for producing a result and is not automatically a separate Entity.
6. A Baseline is an Entity when managed by ATON. Its core semantic content is a frozen, reproducible state of selected Entity versions. It is not automatically a Collection.
7. A Collection is an Entity. Changes to its membership do not change its identity.
8. A View is an Entity. Changing its presentation from a table to a graph does not change its identity. A View is a defined view of a Collection; its rendered table or graph is a Physical Representation.
9. An RFC is an Entity with its own identity, status, version, and lifecycle. It may motivate a Decision.
10. A general Decision is an engineering Decision Entity. An ADR is a specialized Decision Entity for architecture.
11. A GlossaryEntry is an Entity identified by its term, such as "TERM-Artifact". It is distinct from the ontology concept it defines or describes.
12. A Definition is an independently identifiable semantic object that defines a term, concept, property, or interface. It is not identical to the object it defines.
13. A Constitution is an Entity with its own identity, version, lifecycle, and normative content.
14. AX is an experience and presentation model, not an Entity.

8. Concrete Semantic Examples

1. A Requirement such as "REQ-0042" is a concrete engineering Entity. In the normal one-to-one case, its Artifact may use the same identifier value.
2. A Component such as "CMP-0017" describes a technical object and relates to one or more technical representations.
3. Logical components such as “Door Control Left” and “Interior Light Left” may be Entities jointly realized by the physical component “Bodycontroller Left”. Where already validly defined, the "realized-by" relation expresses semantics between Entities, not between a logical Entity and a Physical Representation. Moving a logical component may change its realization relation without changing the logical Entity's identity.
4. An Interface such as "IF-0023 CAN Interface Bodycontroller" may be an Entity.
5. A GlossaryEntry such as "TERM-Artifact" defines or describes the term or concept Artifact; it is not the concept itself.
6. A generated Traceability Report may be an Artifact that organizes information about multiple Entities without representing a single Entity. If a Verification Report is itself a managed engineering object, it may instead be modeled as an Entity.

9. AX Terminology and Provenance

1. In search results and other AX presentations, "ontologyType" denotes the substantive type of an Entity; "artifactType" denotes the type of an Artifact.
2. Engineering Versions, Artifact Revisions, and Git history are distinct concepts and MUST be presented as such.
3. Substantive engineering provenance and technical change history MUST be distinguishable.
4. These are semantic requirements for future AX implementation, not decisions about the concrete user interface design.

Requirements for the Decision Artifact

- Consolidate the decisions above without changing their meaning.
- Clearly distinguish decisions, rationale, implications, and unresolved questions.
- Reference relevant findings from "Foundation-Semantic-Review.md" where possible.
- Do not claim that any Foundation correction has already been implemented.
- Do not convert a proposal or unresolved detail into an accepted decision.
- Do not invent missing Predicates, schemas, identifiers, or rules.
- Follow the repository's actual artifact conventions and use only fields supported by those conventions.
- Preserve the original review report and its commit unchanged.

Validation and Output

After creating the artifact:

1. Inspect the diff and confirm that only the new decision artifact has been added.
2. Run relevant existing validation commands, provided they can be executed without modifying unrelated files.
3. Report the selected path and identifier, the files created, validation results, any unresolved convention questions, and the exact Git commands the user can use to inspect and commit the changes.

Do not commit or push unless explicitly instructed.

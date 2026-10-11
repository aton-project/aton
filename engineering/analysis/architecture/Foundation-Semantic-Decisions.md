# Foundation Semantic Decisions

## Purpose and authority

This dedicated documentary Artifact consolidates the agreed decisions supplied
in revised TASK-0005, including the subsequent Decision Entity / ADR Artifact
clarification. The review findings are evidence and rationale, not the source
of acceptance. The revised task supplies the agreed determinations.

This record does not amend Foundation specifications or assert that corrections
have been implemented. Agreed decisions below must be distinguished from current
Foundation wording, proposed repository conventions and unresolved questions.
No lifecycle status is assigned in this document.

Sources and provenance:

- [Revised TASK-0005](../../task/TASK-0005/content.md), Decisions to Consolidate.
- [Original Foundation Semantic Review](Foundation-Semantic-Review.md), findings F01–F72;
  preserved review commit `6f87942`.
- Repository branch at creation: `development`; basis commit `bfe7de581675c6bf4ccc23a532bde3a707898e7d`.
- The initial task execution created no files. The revised task is already
  committed in the inspected repository and is not modified by this work.

## Representation and convention analysis

The selected physical location is
`engineering/analysis/architecture/Foundation-Semantic-Decisions.md`.
The document locator is `Foundation-Semantic-Decisions.md`; this is not a newly
assigned canonical Entity identifier. No canonical Decision Entity identifier
or separate documentary Artifact identifier is assigned by this record.

Existing evidence:

- The original review and the adjacent K1 analyses establish standalone Markdown
  documents in this directory without metadata or relation sidecars. This record
  uses that existing documentary pattern as an interim representation.
- `foundation/specifications/adr/ADR-0001` through `ADR-0018` establish ADR-numbered
  directories. ADR-0013 metadata uses `id: ADR-0013` and
  `ontologyType: ONT-ADR`. That observed representation does not establish separate
  Decision and ADR identities under the newly clarified semantics.
- `foundation/specifications/ontology/Decision/metadata.yaml` identifies the concept
  as `ONT-Decision`. It does not identify an individual Decision.
- ENTITY-0001, Identity and Type, requires stable identity and exactly one primary
  conceptual type. RFC-0002, Identity Identifier, permits suitable identity
  mechanisms and leaves standardization open; it does not establish a Decision
  prefix or allocation procedure.
- RFC-0030, Canonical Artifact Representation and Required Components, specifies
  `content.md`, `metadata.yaml`, and `relations.yaml`; mandatory relation files
  remain present even for an empty relation collection. Applicable domain rules
  determine required metadata. The schema YAML files are currently empty and do
  not supply a missing Decision registration contract.

This standalone documentary representation is a task-specific, minimally
invasive choice, not a new normative Decision storage convention. It does not
claim completed RFC-0030 canonical-profile conformance or registration as a
canonical Decision Entity. Creating that canonical representation is the part
blocked by unresolved identity and ownership conventions. No incomplete
canonical directory, speculative metadata fields or semantic relations are
created. Links in this document are technical source citations, not serialized
`references` relations.

## Agreed decisions

The following determinations reproduce the revised task's decisions. Their
agreement does not imply that existing Foundation wording already conforms.

### 1. Entity and Identity

1. An Entity is an independently identifiable object of the ATON Engineering Model.
2. Entity identity is independent of file names, directory paths, formats, and physical representations.
3. Every Entity MUST have exactly one primary canonical "ontologyType". This rule applies universally, including to ontology concepts and Foundation artifacts.
4. An unknown or missing type during migration represents incomplete data, not an exception to the model.
5. A specification may aggregate or reference other Entities. It is not necessarily the smallest independently identifiable unit of engineering knowledge.

### 2. Entity, Artifact, and Physical Representation

1. An Entity is an identifiable engineering object.
2. An Artifact is a logically identifiable representation. It may represent one Entity, multiple Entities, or organize information without representing a particular Entity.
3. A Physical Representation is the concrete technical manifestation of an Artifact, such as files, Git objects, database records, API resources, or generated documents.
4. An Entity may have multiple Artifacts, and an Artifact may represent multiple Entities.
5. Entity identity and Artifact identity are semantically distinct, although they may use the same identifier value in the normal one-to-one case.
6. Do not introduce a second Artifact identifier solely to distinguish these semantic roles.
7. "ontologyType" classifies an Entity. "artifactType", when applicable, classifies an Artifact. Storing both values in the same "metadata.yaml" file does not change their semantic ownership.
8. Artifact Type remains optional unless required by the relevant domain.
9. Artifact components do not automatically become Entities.

### 3. Properties, Metadata, and Physical Files

1. Properties represent domain-specific, substantive information. Metadata represents administrative information.
2. "content.md" contains substantive content.
3. "properties.yaml" stores substantive properties.
4. "metadata.yaml" stores administrative metadata.
5. "relations.yaml" stores relations.
6. The physical location of a value does not determine its semantic ownership. Properties and metadata may belong to Entities or other model objects where the model defines such ownership.
7. The canonical physical representation requires all mandatory files, including "relations.yaml" when no relations exist. An empty relation collection may be represented as "[]".
8. The nine directories identified in finding F65 must ultimately be brought into conformity: AX-0004 through AX-0010, the ontology AX artifact, and the ontology Constitution artifact. This task MUST NOT modify those directories.

### 4. Relation Semantics and Serialization

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

### 5. Versioning, Lifecycle, and Review

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

### 6. Examples and Historical Material

1. Examples should accurately represent the current model.
2. Examples may illustrate proposed or unsupported relations only when explicitly marked as non-normative and proposed.
3. Examples do not implicitly introduce Predicates or expand constraints.
4. Historical migration observations, rejected alternatives, and hypothetical mappings remain historical or non-normative unless an operative rule explicitly adopts them.
5. Historical material MUST NOT be rewritten automatically merely to normalize its terminology.
6. Successful verification or rendering tests do not, by themselves, prove complete semantic coherence.

### 7. Entity Types and Ontology Concepts

The following are treated as Entity types or specialized model concepts in the agreed model. Their classification as Entities or Artifacts must follow the specific distinctions below rather than assuming that every named item is an Entity.

- Requirement
- Specification
- Component
- Interface
- Decision
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

1. A Decision is an independently identifiable engineering Entity with its own identity and lifecycle.
2. An ADR is an Artifact that documents a Decision. It is not itself a specialized Decision Entity.
3. The Decision and its ADR are semantically distinct. Their identifiers MUST NOT be assumed to be identical merely because the ADR documents that Decision.
4. A Decision may have an Artifact that represents its documentation. The general Entity-to-Artifact rules apply.
5. Finding, Review, and Note are Entities. Their corresponding ontology concepts define their types.
6. A Note may exist without a relation to another Entity.
7. A Finding is tied to a specific review context. The same factual observation in another Review is represented by a new Finding. Different Reviews MUST NOT refer to the same Finding.
8. Review is an independently managed engineering object, not an Activity. Activities may include Inspection or Check.
9. Test Case, Test Procedure, and Test Result are Entities. Test Execution provides the context for producing a result and is not automatically a separate Entity.
10. A Baseline is an Entity when managed by ATON. Its core semantic content is a frozen, reproducible state of selected Entity versions. It is not automatically a Collection.
11. A Collection is an Entity. Changes to its membership do not change its identity.
12. A View is an Entity. Changing its presentation from a table to a graph does not change its identity. A View is a defined view of a Collection; its rendered table or graph is a Physical Representation.
13. An RFC is an Entity with its own identity, status, version, and lifecycle. It may motivate a Decision.
14. A GlossaryEntry is an Entity identified by its term, such as "TERM-Artifact". It is distinct from the ontology concept it defines or describes.
15. A Definition is an independently identifiable semantic object that defines a term, concept, property, or interface. It is not identical to the object it defines.
16. A Constitution is an Entity with its own identity, version, lifecycle, and normative content.
17. AX is an experience and presentation model, not an Entity.

### 8. Concrete Semantic Examples

1. A Requirement such as "REQ-0042" is a concrete engineering Entity. In the normal one-to-one case, its Artifact may use the same identifier value.
2. A Component such as "CMP-0017" describes a technical object and relates to one or more technical representations.
3. Logical components such as “Door Control Left” and “Interior Light Left” may be Entities jointly realized by the physical component “Bodycontroller Left”. Where already validly defined, the "realized-by" relation expresses semantics between Entities, not between a logical Entity and a Physical Representation. Moving a logical component may change its realization relation without changing the logical Entity's identity.
4. An Interface such as "IF-0023 CAN Interface Bodycontroller" may be an Entity.
5. A GlossaryEntry such as "TERM-Artifact" defines or describes the term or concept Artifact; it is not the concept itself.
6. A generated Traceability Report may be an Artifact that organizes information about multiple Entities without representing a single Entity. If a Verification Report is itself a managed engineering object, it may instead be modeled as an Entity.
7. An ADR is a documentary Artifact for a Decision Entity. Whether one ADR may document multiple Decisions, or whether each ADR must document exactly one Decision, is an unresolved modeling question. Do not silently choose either rule.

### 9. AX Terminology and Provenance

1. In search results and other AX presentations, "ontologyType" denotes the substantive type of an Entity; "artifactType" denotes the type of an Artifact.
2. Engineering Versions, Artifact Revisions, and Git history are distinct concepts and MUST be presented as such.
3. Substantive engineering provenance and technical change history MUST be distinguishable.
4. These are semantic requirements for future AX implementation, not decisions about the concrete user interface design.

## Rationale and review traceability

Finding numbers below refer to headings in the original review, not separately
registered Finding Entities. They connect the decisions to observed issues;
they do not claim that the review decided the resolutions.

| Decision group | Relevant review findings | Rationale |
| --- | --- | --- |
| 1. Entity and Identity | F23; F47–F49 | Mandatory classification and definition/instance distinctions prevent migration gaps and storage conventions from redefining identity. |
| 2. Entity, Artifact, Physical Representation | F14; F35–F40 | Separating semantic objects from their documentary representations permits multiple representations without inventing additional identities. |
| 3. Properties, Metadata, Physical Files | F05; F27; F34; F65 | Semantic ownership survives physical placement; the canonical file profile must be applied explicitly. F65 identifies the nine missing relation files. |
| 4. Relations and Serialization | F15; F44–F46; F49–F50; F58; F63 | Semantic endpoints and authoritative Predicate rules must agree with reconstruction and validation. Storage ownership alone cannot determine a multi-Entity source. |
| 5. Versioning, Lifecycle, Review | F27; F47; F51–F55 | Administrative state, substantive state and technical history have different meanings and review consequences. |
| 6. Examples and History | F56–F60; F64; F66; F68; F71–F72 | Examples and historical observations cannot silently become operative semantics; passing tooling checks has limited evidentiary scope. |
| 7–8. Types and Concrete Examples | F14; F35–F40; F48–F49 | Instances, defining concepts and records must remain distinguishable. The revised task adds the explicit Decision/ADR clarification and leaves ADR cardinality open. |
| 9. AX Terminology and Provenance | F67; F69–F70 | Presentations must preserve semantic classification and distinguish engineering provenance from technical history. |

The Decision/ADR clarification is subsequent task-supplied agreement. It must
not be attributed to a finding that already settled it. In particular, existing
ONT-ADR classification and ADR-0017 lifecycle wording require future
reconciliation; this record does not reinterpret or modify them automatically.

## Implementation implications — future work only

- Foundation definitions, examples and file profiles will require reconciliation
  against these decisions. The nine F65 directories remain untouched.
- Loader source reconstruction, Predicate contracts and validators will need to
  agree. The existing `references` prose and constraints are part of the reviewed
  conflict; this record does not fix them or instantiate disputed semantic pairs.
- Versioning and review policies will need to distinguish substantive changes
  from administrative changes, including the reviewed Uplink/Downlink case.
  Existing Engineering Versions must remain unchanged retrospectively.
- Decision Entity identity, lifecycle and `ontologyType` will need to be stored
  without transferring ownership to the ADR documenting it. Artifact Revision
  and Git history must remain separate from Engineering Version.
- AX implementations will need the stated semantic terminology and provenance
  distinctions. No concrete user-interface design is selected here.

No correction tasks, Foundation corrections, migration mappings, new Predicates
or automatic historical rewrites are implemented or authorized by this record.

## Proposed conventions — unresolved and not adopted

A suitable future approach is to approve separate identity allocation contracts
for managed Decision Entities and their documentary Artifacts, with an explicit
representation mapping at the serialization boundary. Entity classification
would reference the existing `ONT-Decision` concept. Artifact classification
would follow an approved documentary profile, where required. This proposal
introduces no field, identifier format, Predicate or approved directory.

The rationale is to preserve the newly agreed distinction without assuming that
an ADR number identifies its Decision. Independently allocated identifiers are
one option; an explicitly approved shared value in an appropriate one-to-one
case is another. The general permission for shared values does not establish
an ADR-specific identity rule.

Alternatives considered:

- Use the next ADR directory and its number as the Decision's identifier. This
  would apply an unresolved identity mapping and existing ONT-ADR classification
  to the new semantics; it is not adopted.
- Introduce a Decision prefix and directory by analogy with NOTE and REVIEW.
  This could support independent management, but would create conventions that
  have not been approved; no prefix or directory is selected.
- Use an opaque identifier under RFC-0002. This satisfies a general identity
  option but does not settle allocation, metadata ownership or physical mapping;
  it is not adopted.
- Use the existing standalone documentary pattern for this consolidation.
  This is the selected interim physical representation. It preserves the agreed
  content while canonical Entity registration remains incomplete; it does not
  supply the missing canonical identity contract.

## Unresolved questions and specific remaining blocker

1. What identifier allocation and identity scope should apply to an individual
   Decision and to an ADR documenting it? No Decision prefix, ADR-to-Decision
   identity equivalence or separate Artifact identifier rule is approved here.
2. Where should canonical Decision representations and documentary ADR Artifacts
   be stored, and which existing metadata fields express their ownership and
   mapping? A general canonical directory profile exists, but the clarified
   Decision/ADR registration contract is still missing.
3. May one ADR document multiple Decisions, or must each ADR document exactly
   one Decision? Both remain open. The nine groups in this record organize
   supplied statements; they do not allocate nine Entities or assert that all
   statements constitute exactly one Decision Entity.
4. How should existing ONT-ADR usage and ADR lifecycle specifications be reconciled
   with an ADR being an Artifact? No classification or lifecycle migration is
   selected here.
5. How will the general Predicate rule mechanism, concrete constraints and
   validator enforce the agreed Entity-to-Entity semantics consistently?
   No implicit specialization, new Predicate or unsupported pair is introduced.
6. Which concrete persisted version/review/provenance fields and policies satisfy
   the general model contract? Engineering Version, Artifact Revision and Git
   history remain distinct; no new numbering or review schema is selected.

The specific remaining blocker is canonical registration of the represented
Decision Entity or Entities and their documentary mapping, not consolidation
of the agreed statements. This record preserves the consolidation for review
without pretending that the registration questions have been settled.

# Foundation Semantic Review

This is the original analysis result of the repository-wide review requested on 2026-10-08. It is an analysis artifact, not a normative Foundation specification or architectural decision. It records discrepancies without deciding their resolution. No Foundation content, identifiers, versions, predicates or ontology concepts are changed or proposed as adopted semantics by this report.

## Reviewed state and method

Reviewed branch: `development`. Reviewed commit: `b442d615a17e83d239c3239480e06bda91d2a341`. The working tree was clean at review start. Scope: every file below `foundation/`, including `.gitignore`, all sidecars, empty files and placeholder reference areas: 265 files. The file inventory below records exact source hashes and attaches each file to its substantive review records. Missing files are distinguished from existing empty files.

The review used complete contextual reading of the Constitution, every ADR and RFC, ENTITY-0001, every ontology and glossary definition, every concrete predicate and constraint file, every metadata and relation serialization, and the README, schema, template, reference, example and AX material. Search and enumeration supported coverage; keyword matches were not treated as semantic conclusions. Context, operative modality, examples, rejected alternatives, migration rules, instance/type distinctions and physical representation boundaries were assessed separately. Tooling outside Foundation was inspected only to identify practical validation; its implementation is not part of this Foundation semantic inventory.

The current user-supplied architectural basis governs this analysis, including where repository decisions have Draft or Proposed status. That review basis does not make those documents accepted. Accepted, draft, proposed, historical and illustrative statements are distinguished; an operative draft rule can conflict with the review basis without being an accepted architectural constraint. Old date, low version, or draft status alone does not make a passage historical.

Classification meanings:

- **CONTRADICTION**: an operative statement or executable definition is incompatible with the current review basis or another explicit Foundation rule identified in the record. Conditional representation conformance conflicts are marked as such.
- **AMBIGUITY**: more than one semantic interpretation remains possible, including a compatible one; no incompatible interpretation is assumed to be the actual intent.
- **CONSISTENT**: compatible in context, sometimes conditional on an explicitly identified domain definition or mapping.
- **HISTORICAL / NON-NORMATIVE**: an earlier problem analysis, illustrative scenario, rejected alternative or descriptive placeholder; it should not be rewritten merely to align vocabulary.

“Correction necessary” below describes whether future clarification or reconciliation appears needed. It does not authorize a correction, select a replacement model, or instruct changes to any existing artifact. Dependencies are semantic dependencies visible in the Foundation, not invented relations. A record may concern multiple explicitly listed files with the same passage and interpretation; the inventory maps every affected file back to that record.

## Ownership interpretation used for review

| Concept | Semantic interpretation / owner | Physical representation and limits |
| --- | --- | --- |
| Engineering Entity | Identifiable logical engineering concept; owns Entity Identity and Entity-level classification. | Neither a file nor a directory defines it; one Entity can have multiple Artifacts. |
| Engineering Artifact | Logical/addressable engineering representation; owns Artifact Identity and applicable Artifact Type. | Can represent one or more Entities when supported; can have multiple technical manifestations. |
| Physical Representation | Concrete persistence, exchange or presentation manifestation. | File, directory, YAML, Markdown, Git object, database record, API resource or rendered output; can have technical identity and technical history. |
| `ontologyType` | Engineering Entity property referencing a canonical ontology Concept. | May be serialized in `metadata.yaml`; storage does not transfer classification to the Artifact. |
| `artifactType` | Engineering Artifact classification where applicable. | Optional unless a domain requires it; absence is not inherently a defect. Cannot substitute for `ontologyType`. |
| Metadata | Describes the logical concept to which a value pertains. | Entity, Artifact, version/revision and technical metadata must remain distinguishable even when stored together. Canonical authority is defined semantically. |
| Property | Named characteristic of its described engineering concept. | A physical field is not automatically a canonical Property; metadata is a defined semantic use of Properties. |
| Relation | Occurrence of a defined Predicate between identified semantic endpoints; canonical source/predicate/target identity. | Serialization ownership is not necessarily source ownership, especially for a compound Artifact. Technical links do not automatically become engineering relations. |
| Predicate | Ontology-level relationship meaning, direction and applicability contract. | A Predicate definition may itself be represented as an Entity by an Artifact; constraints belong to the definition, not each relation occurrence. |
| Content | Engineering knowledge expressed by an Entity and carried by an Artifact representation. | `content.md` serializes authored content; presentation syntax does not create semantic identity or relations. Content is not confined to a particular file in the abstract model. |
| Identity | Entity Identity and Artifact Identity have distinct referents. | The same `id` value may serve both in the normal one-Entity/one-Artifact case. No additional technical ID is inherently required. Technical representation identity is a third concern. |
| Revision | Artifact Revision describes change to the Artifact or its representation; Git Revision is technical history. | Neither is automatically an Engineering Version. A revision identifier or manifest is not defined merely by a Git hash. |
| Version | Semantic engineering state of an Engineering Entity. | Independent of timestamps and commit counts; immutable established states, baseline selections and released states remain distinct. |

The layer sequence preserved throughout this review is:

```text
logical semantic model
        ↓
Engineering Entity / Engineering Artifact
        ↓
Physical Representation
        ↓
content.md / metadata.yaml / relations.yaml
```

The final three names are components of the canonical repository manifestation, not three new ontology concepts. A canonical domain object is the kernel's representation of the logical semantics, not a competing semantic authority. A normative file profile can prescribe a physical format without making its paths or serialization structure semantic owners.

## Overall assessment

The current state has substantial explicit alignment: ENTITY-0001, ADR-0008, ADR-0010, ADR-0013, RFC-0010, RFC-0020, RFC-0027, RFC-0030, ONT-Entity, ONT-Artifact and the Entity/Artifact glossary entries now explicitly distinguish `ontologyType` from `artifactType` and preserve shared identifier values without equating identities. The Constitution, logical/physical boundary decisions, version model and rendering boundary generally reinforce this architecture.

The confirmed conflicts are concentrated in operative definitions or cross-specification contracts: universal metadata wording in ADR-0005, optional Entity typing in RFC-0001, classification of semantic Findings/Reviews/Notes as Artifacts in ontology definitions, Predicate prose versus machine constraints, and stale source-less Relation claims in RFC-0029 versus current RFC-0025. These are distinguished below from the wider set of ambiguities around shorthand “physical artifact”, metadata scopes, polymorphic relation endpoints, type-level versus instance-level relationships, field authority, and evolution semantics.

Passing current verification is not proof that the entire Foundation is semantically coherent. A verifier can accept wildcard constraints while the predicate prose rejects the same pairs. Conversely, unresolved migration predicates are explicitly unresolved, not automatically contradictory or semantically invalid. Missing canonical files are conditional physical-profile conformance issues, not evidence that an Entity lacks semantic identity. This report does not infer new identities or semantic versions from the current repository state or Git history.

## Detailed review records

### F01 — CONSISTENT

- **File(s):** `foundation/constitution/CONSTITUTION/content.md`.
- **Section / passage:** Preamble; I.3; II.3; III.1–3,7; IV.2–4; VI.3.
- **Semantic interpretation:** The Constitution defines semantic independence, explicit relationships, traceable evolution and layered realization; the highest architectural document governs lower specifications.
- **Affected concept/layer:** Logical model / Physical Representation.
- **Classification:** CONSISTENT.
- **Explanation:** The Constitution does not equate engineering objects with files or Git objects, and does not assign classification or identity to serialization. Its document status does not turn its representation into an Entity definition.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0004, ADR-0006, ADR-0011; RFC-0015. Canonical authoring and Git decisions are representation policies, assessed in F03.

### F02 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0001/content.md`.
- **Section / passage:** Decision; Architectural Principle.
- **Semantic interpretation:** Foundation concepts are described using their own knowledge model and artifacts.
- **Affected concept/layer:** Entity / Artifact / self-hosting.
- **Classification:** CONSISTENT.
- **Explanation:** Self-hosting requires representations of the Foundation concepts, not identity between a concept and its file. The decision can be satisfied with separate semantic owners.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0004, ENTITY-0001, RFC-0010, RFC-0030.

### F03 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0002/content.md`; `foundation/specifications/adr/ADR-0003/content.md`; `foundation/specifications/adr/ADR-0007/content.md`.
- **Section / passage:** Decisions; Architectural Principles; boundaries.
- **Semantic interpretation:** Markdown authoring, Git control and normative Foundation scope are explicit Foundation representation/governance policies.
- **Affected concept/layer:** Content / Physical Representation / technical Revision.
- **Classification:** CONSISTENT.
- **Explanation:** Markdown is explicitly serialization of independent semantics. Git history is engineering evidence, not automatically an Engineering Version. No executable logic appears under Foundation; specifications about implementations are knowledge, not executable implementations. Technology independence of the semantic model does not forbid a canonical representation profile for this Foundation.
- **Correction appears necessary:** No; broader policy scope may need clarification only if these rules are applied to all alternative persistence implementations.
- **Dependencies:** Constitution II.3 and III.7; ADR-0011/0012; RFC-0011/0012/0015/0030/0031.

### F04 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0004/content.md`.
- **Section / passage:** Decision; Rationale; Alternatives.
- **Semantic interpretation:** Knowledge is organized as Entities represented by uniquely identifiable and independently versionable Artifacts; views present knowledge.
- **Affected concept/layer:** Entity / Artifact / Version.
- **Classification:** CONSISTENT.
- **Explanation:** Explicit Entity-to-Artifact distinction is preserved. Independently versionable can be implemented as Artifact Revisions under the later version model; the phrase does not expressly equate those revisions with Entity Versions. File-centric and document-centric alternatives are rejected in context.
- **Correction appears necessary:** No confirmed correction; revision terminology could be clarified for readers.
- **Dependencies:** ADR-0012/0013; RFC-0010/0012.

### F05 — CONTRADICTION

- **File(s):** `foundation/specifications/adr/ADR-0005/content.md`.
- **Section / passage:** Decision: “Metadata SHALL describe engineering artifacts and SHALL NOT contain engineering knowledge”; Architectural Principle.
- **Semantic interpretation:** A universal metadata rule assigns metadata description to Artifacts and excludes all engineering knowledge from it.
- **Affected concept/layer:** Metadata / Entity vs Artifact ownership.
- **Classification:** CONTRADICTION.
- **Explanation:** The literal universal exclusion conflicts with canonical metadata as semantic properties of engineering knowledge, including Entity identity, ontology classification and lifecycle. It cannot accommodate Entity-owned metadata without qualification. Merely placing it in an artifact component does not repair the rule. Content/metadata logical separation is compatible; the universal ownership/exclusion is not.
- **Correction appears necessary:** Yes, reconciliation appears necessary; no replacement wording is decided.
- **Dependencies:** ADR-0010 Canonical Metadata and Metadata Ownership; ENTITY-0001 Metadata; RFC-0003; RFC-0005; RFC-0030 Metadata; ONT-Metadata.

### F06 — AMBIGUITY

- **File(s):** `foundation/specifications/adr/ADR-0005/content.md`.
- **Section / passage:** Decision: content intended for human understanding; independently evolving logical components.
- **Semantic interpretation:** Content, metadata and relations are independent logical components carried by an Artifact.
- **Affected concept/layer:** Content / Metadata / Relation.
- **Classification:** AMBIGUITY.
- **Explanation:** This is compatible as a separation of authoring concerns. “Only ... intended for human understanding” may exclude machine-consumed structured engineering content allowed in RFC-0010. The text does not say whether human-readable and machine-processable content can overlap. It also does not distinguish canonical relation data from explanatory relation examples in content.
- **Correction appears necessary:** Clarification appears useful; no confirmed need to remove examples or structured content.
- **Dependencies:** ADR-0002; RFC-0010 Artifact Content; RFC-0030 Content; AX-0002 human/AI equality.

### F07 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0006/content.md`.
- **Section / passage:** Decision; Alternatives Considered.
- **Semantic interpretation:** The logical graph consists of engineering concepts connected by explicit first-class relations independently of views.
- **Affected concept/layer:** Entity / Relation / Physical Representation.
- **Classification:** CONSISTENT.
- **Explanation:** Folders, database schemas and views are correctly separated from conceptual graph organization. “Concepts” here describes represented knowledge, not a requirement that every edge be a taxonomy edge.
- **Correction appears necessary:** No.
- **Dependencies:** ENTITY-0001; RFC-0004/0025; ADR-0014.

### F08 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0008/content.md`.
- **Section / passage:** Decision; Explicit Ontology Type Identity.
- **Semantic interpretation:** Canonical boundary normalization; exactly one explicit Entity-owned `ontologyType`; applicable Artifact-owned `artifactType`.
- **Affected concept/layer:** ontologyType / artifactType / Physical Representation.
- **Classification:** CONSISTENT.
- **Explanation:** The text directly implements the supplied basis and excludes path, serialization and artifact classification inference. Co-located values keep their owners. Concept specialization does not create multiple primary types.
- **Correction appears necessary:** No.
- **Dependencies:** ENTITY-0001; RFC-0020/0027/0030; ONT-Entity. Governance status discrepancy is F52.

### F09 — AMBIGUITY

- **File(s):** `foundation/specifications/adr/ADR-0009/content.md`.
- **Section / passage:** Decision; Architectural Separation; Source and Target Semantics.
- **Semantic interpretation:** Source and target types are constrained at ontology level separately from the structural Relation model.
- **Affected concept/layer:** Predicate / Relation / ontologyType.
- **Classification:** AMBIGUITY.
- **Explanation:** The general principle is compatible. Independent domain/range satisfaction does not specify an exact allowed-pair contract and could be read as accepting a Cartesian product. Later RFC-0027/0029 require explicit pairs; individual satisfaction alone is insufficient for multiple asymmetric pairs. The ADR defers detailed rules and does not explicitly mandate Cartesian expansion.
- **Correction appears necessary:** Clarification of the dependency on exact pair semantics appears useful, not automatic invalidation of the ADR.
- **Dependencies:** RFC-0027 Allowed Source-to-Target Pairs; RFC-0029 No Cartesian Product Semantics; ADR-0014.

### F10 — HISTORICAL / NON-NORMATIVE

- **File(s):** `foundation/specifications/adr/ADR-0009/content.md`.
- **Section / passage:** Context and Invalid Relations: conditional Finding → motivates → Note examples.
- **Semantic interpretation:** Earlier analysis illustrates why syntactic representability is not semantic validity.
- **Affected concept/layer:** Predicate / historical examples.
- **Classification:** HISTORICAL / NON-NORMATIVE.
- **Explanation:** “May” and “if ... defined” do not establish Finding → Note as a current allowed pair. Current motivates permits Note/Finding → ADR. Conditional diagnostic examples should be preserved as analysis, not rewritten into current normative pair lists.
- **Correction appears necessary:** No consistency correction to the historical or conditional examples.
- **Dependencies:** RFC-0027; PRED-motivates; RFC-0029.

### F11 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0010/content.md`.
- **Section / passage:** Canonical Metadata; Explicit Representation; Authority; Temporal Information; Ownership.
- **Semantic interpretation:** Canonical values are explicit, portable and semantically owned by their described logical concept; technical timestamps remain technical.
- **Affected concept/layer:** Metadata / Property / ontologyType / artifactType / Version.
- **Classification:** CONSISTENT.
- **Explanation:** Entity ontology classification and Artifact classification may share storage. Canonical authority is not Git availability or YAML location. Materialization is explicit. Temporal metadata is not Engineering Version semantics.
- **Correction appears necessary:** No.
- **Dependencies:** RFC-0003/0005/0010/0030; ADR-0011/0012/0013.

### F12 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0011/content.md`.
- **Section / passage:** Decision; Logical Engineering Knowledge; Physical Representations.
- **Semantic interpretation:** Logical model and canonical domain objects are separated from files, repositories, database/API/exchange/rendered representations.
- **Affected concept/layer:** All layers.
- **Classification:** CONSISTENT.
- **Explanation:** Explicit normative representation profiles are permitted without redefining underlying semantics. Artifacts are listed among logical concepts, so the document does not make all Artifacts synonymous with files.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0008/0010/0013; RFC-0010/0015/0030.

### F13 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0012/content.md`; `foundation/specifications/adr/ADR-0013/content.md`.
- **Section / passage:** Identity; Versioning; Artifact Revision; Git Revisions; Derived Representations.
- **Semantic interpretation:** Entity Identity, Entity Versions, Artifact Identity, Artifact Revisions and Git history are distinct; shared identifier values are allowed.
- **Affected concept/layer:** Identity / Revision / Version / authority.
- **Classification:** CONSISTENT.
- **Explanation:** Many-to-many representation is permitted; one Entity per Artifact is not a universal kernel assumption. Technical or generated changes do not automatically create Entities or become authoritative. No second technical Artifact ID is inherently required.
- **Correction appears necessary:** No.
- **Dependencies:** ENTITY-0001; RFC-0002/0010/0012/0013; TERM-Artifact; ONT-Artifact.

### F14 — AMBIGUITY

- **File(s):** `foundation/specifications/adr/ADR-0013/content.md`; `foundation/specifications/ontology/Artifact/content.md`; `foundation/specifications/glossary/TERM-Artifact/content.md`.
- **Section / passage:** Engineering Artifact; Role in ATON; Persistence Independence; “physical or addressable representation”.
- **Semantic interpretation:** Artifact is described using persistence/addressability language, while its physical representation is separately variable.
- **Affected concept/layer:** Artifact / Physical Representation.
- **Classification:** AMBIGUITY.
- **Explanation:** A compatible reading is a logical, addressable representation embodied technically. Another reading collapses Artifact into the concrete manifestation, particularly “part of the physical ... representation” and successive Markdown/database/API artifacts. RFC-0010 explicitly distinguishes the layers. The identity/type clauses here remain consistent and prevent an outright collapse conclusion.
- **Correction appears necessary:** Clarification of “representation” and “physical artifact” appears useful; no replacement model is selected.
- **Dependencies:** RFC-0010 Summary, Multiple Physical Representations and rejected Treat files as Engineering Artifacts; RFC-0015; ADR-0011.

### F15 — AMBIGUITY

- **File(s):** `foundation/specifications/adr/ADR-0014/content.md`.
- **Section / passage:** Decision: source artifact or entity “in which the relation is represented”; source determined by owner.
- **Semantic interpretation:** Representation container may supply the semantic source.
- **Affected concept/layer:** Relation / Identity / Entity vs Artifact.
- **Classification:** AMBIGUITY.
- **Explanation:** This is compatible for an expressly Artifact-originating relation or a mapped one-Entity/one-Artifact case. It is ambiguous for a compound Artifact: the physical/container owner cannot unambiguously select a represented Entity. Semantic Validation correctly uses each participating Entity’s ontologyType, but the source clause does not distinguish representation owner from semantic owner.
- **Correction appears necessary:** Yes, source ownership and mapping need clarification for compound representations.
- **Dependencies:** ADR-0013 Entity-to-Artifact Relationship; RFC-0025 source; ENTITY-0001 Relationships; TERM-Relation; RFC-0030 Relations.

### F16 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0014/content.md`.
- **Section / passage:** Predicate Semantics; Semantic Validation; Relation Identity; Persistence; External Targets.
- **Semantic interpretation:** Canonical source/predicate/target identity, explicit Entity types, independent constraints and external resolution.
- **Affected concept/layer:** Relation / Predicate / ontologyType / Identity.
- **Classification:** CONSISTENT.
- **Explanation:** Physical positions do not form relation identity; unresolved local persistence is separated from semantic invalidity. The explicit type ownership clause matches the review basis.
- **Correction appears necessary:** No for these sections; F15 remains.
- **Dependencies:** RFC-0025/0027/0028/0029; ONT-Relation; TERM-Relation.

### F17 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0015/content.md`.
- **Section / passage:** Decision; Contextual Identity; Artifact Representation; Findings and Reviews; Versioning.
- **Semantic interpretation:** Independent semantic Findings can be contextual Entities regardless of embedding, with explicit context and their own identity/state.
- **Affected concept/layer:** Entity / Artifact / Content / Metadata / Identity / Version.
- **Classification:** CONSISTENT.
- **Explanation:** Physical containment, deletion or a context change does not automatically determine Entity identity, lifecycle or version. Shared documents are supported without creating a new fundamental kind of Entity.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0013/0014/0012; ONT-Finding/Review conflict in F35; Review Process is referenced but not specified under Foundation.

### F18 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0016/content.md`.
- **Section / passage:** Inputs and Outputs; Process Constraints; Execution; Knowledge Integration.
- **Semantic interpretation:** Processes can reference Entities, Artifacts, versions, relations and metadata; expected input is distinct from its concrete fulfillment.
- **Affected concept/layer:** Entity / Artifact / Metadata / Relation / Version.
- **Classification:** CONSISTENT.
- **Explanation:** Definition and execution are distinct and process semantics remain independent of physical workflow implementation. Describing Activity changes to Artifacts does not deny changes to Entity state.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0010/0012/0013/0014; Constitution process independence.

### F19 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0017/content.md`.
- **Section / passage:** Decision; Accepted; Versioning; Traceability; Historical Preservation.
- **Semantic interpretation:** Architecture Decision lifecycle is explicit Entity state; review/Git evidence does not establish acceptance automatically.
- **Affected concept/layer:** Metadata / Identity / Version / Revision.
- **Classification:** CONSISTENT.
- **Explanation:** Existence of an ADR Artifact is not acceptance. Terminal history preserves identity. State and version are distinguished; substantive changes may create versions. Whether every lifecycle transition creates a version is not fully settled across version passages (F54).
- **Correction appears necessary:** No for layer separation; lifecycle/version triggers deserve clarification in F54.
- **Dependencies:** ADR-0012; RFC-0012; F52 status serialization.

### F20 — CONSISTENT

- **File(s):** `foundation/specifications/adr/ADR-0018/content.md`; `foundation/specifications/rfc/RFC-0014/content.md`.
- **Section / passage:** Targets; Paths; inverse navigation; views; history; external resolution.
- **Semantic interpretation:** Navigation crosses explicit logical connections including Entity-to-Artifact mappings; interfaces and physical paths are access mechanisms.
- **Affected concept/layer:** Entity / Artifact / Relation / Identity / Version / Physical Representation.
- **Classification:** CONSISTENT.
- **Explanation:** Inverse traversal is not an authored inverse relation; views do not redefine concepts. Navigation supports both Artifacts and Entities without identifying them. Storage filters are separate from canonical semantic filters.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0011/0013/0014; RFC-0015/0021/0023/0025/0029.

### F21 — CONSISTENT

- **File(s):** `foundation/specifications/entity/ENTITY-0001/content.md`.
- **Section / passage:** Identity; Type; Content; Metadata; Relationships; Persistence Independence.
- **Semantic interpretation:** Universal Entity identity and exactly one explicit ontologyType; separate applicable Artifact Type and shared IDs.
- **Affected concept/layer:** Entity / ontologyType / artifactType / Metadata / Content / Relation / Identity.
- **Classification:** CONSISTENT.
- **Explanation:** Core current ownership statements directly match the review basis; content serialization is identity-independent. A normative/descriptive content capability does not imply that metadata, relations or their files own Entity classification.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0008/0013; RFC-0025; ONT-Entity; TERM-Entity. Broader metadata definitions examined in F34.

### F22 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0000/content.md`.
- **Section / passage:** Proposal; Non Goals.
- **Semantic interpretation:** RFC instances have identities and a three-file canonical document manifestation.
- **Affected concept/layer:** Identity / Content / Metadata / Relation / Physical Representation.
- **Classification:** CONSISTENT.
- **Explanation:** Within document conventions, “contain ... file” is a physical authoring rule, not a claim that an RFC’s semantic identity is the directory. It explicitly does not define the ontology or data model.
- **Correction appears necessary:** No.
- **Dependencies:** RFC-0030; ADR-0002; RFC-0002.

### F23 — CONTRADICTION

- **File(s):** `foundation/specifications/rfc/RFC-0001/content.md`.
- **Section / passage:** Entity Type: “An Engineering Entity MAY have an applicable semantic type”.
- **Semantic interpretation:** A conforming Engineering Entity may lack an applicable semantic type.
- **Affected concept/layer:** Entity / ontologyType.
- **Classification:** CONTRADICTION.
- **Explanation:** The permissive typing rule conflicts with ENTITY-0001 and ADR-0008: every participating Entity has exactly one explicitly declared canonical ontologyType. Migration uncertainty is separately permitted, but this Proposal clause is not restricted to migration.
- **Correction appears necessary:** Yes, the modality/applicability contract needs reconciliation; no correction is made.
- **Dependencies:** ENTITY-0001 Type; ADR-0008 Explicit Ontology Type Identity; RFC-0020 Ontology Type; RFC-0030 Domain Type.

### F24 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0001/content.md`.
- **Section / passage:** Summary; Entity and Artifact; Entity and Physical Representation; Containment; Migration.
- **Semantic interpretation:** Entity concepts, representations, versioning and canonical loading remain distinct.
- **Affected concept/layer:** Entity / Artifact / Identity / Content / Version / Physical Representation.
- **Classification:** CONSISTENT.
- **Explanation:** Multiple Entities may share an Artifact and one Entity may have several Artifacts. Physical sections/containment do not establish Entities or relations. Metadata cannot redefine identity without an explicit normative rule.
- **Correction appears necessary:** No for these passages; F23 is independent.
- **Dependencies:** RFC-0002/0010/0015; ADR-0013/0015.

### F25 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0002/content.md`.
- **Section / passage:** Identity; Identifiers; Scope; Resolution; Git; Migration.
- **Semantic interpretation:** Stable scoped Entity identity, versions and representation revisions are distinct.
- **Affected concept/layer:** Identity / Revision / Version.
- **Classification:** CONSISTENT.
- **Explanation:** String equality across scopes does not establish identical Entities. Opaque identifiers are a SHOULD, so current semantic prefixes are not a confirmed violation. Physical aliases are not automatic canonical identity. The universal immutability rule concerns semantic identity, not byte-level representations.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0012/0013; RFC-0010/0012/0015; TERM-Entity/Artifact.

### F26 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0003/content.md`.
- **Section / passage:** Metadata and Entities/Identity/Content/Relations; Canonical/Persisted/Derived; Authority; Physical Representation; Evolution.
- **Semantic interpretation:** Metadata describes the appropriate concept or representation; identity and relations retain distinct meanings.
- **Affected concept/layer:** Metadata / Property / Content / Identity / Version.
- **Classification:** CONSISTENT.
- **Explanation:** Identity information may be serialized in metadata without equating the file with identity. Relations are not ordinary metadata merely because of storage. Derived values cannot silently overwrite authority; technical metadata change is not automatically a version change.
- **Correction appears necessary:** No for these sections.
- **Dependencies:** ADR-0010; RFC-0002/0005/0010/0012/0030.

### F27 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0003/content.md`.
- **Section / passage:** Alternatives: “Persist all metadata” rejected; Persisted Metadata retained when not reconstructable.
- **Semantic interpretation:** Reliably derivable values may be excluded from persistence.
- **Affected concept/layer:** Metadata / canonical authority.
- **Classification:** AMBIGUITY.
- **Explanation:** A compatible reading applies the rejection only to supplemental derived information. A conflicting reading makes reconstructability sufficient to omit a canonical semantic value, contrary to ADR-0010 explicit canonical availability and explicit materialization. The RFC otherwise preserves authoritative metadata, so this is not a confirmed universal replacement rule.
- **Correction appears necessary:** Clarification of canonical versus supplemental scope appears necessary.
- **Dependencies:** ADR-0010 Explicit Representation, Derived Information and Materialization; RFC-0005 Canonical Properties; RFC-0030 Metadata.

### F28 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0004/content.md`.
- **Section / passage:** Source; Predicate; Target; Explicit/Derived Relations; Identity; Physical References; Versions.
- **Semantic interpretation:** Relations connect semantic knowledge with defined predicates; hyperlinks, containment and physical reference identities are separate.
- **Affected concept/layer:** Relation / Predicate / Identity / Version.
- **Classification:** CONSISTENT.
- **Explanation:** The generic model permits Artifact endpoints only when an ontology constraint permits them; it does not equate them with their represented Entities. Inverse traversal is not reverse relation creation. Explicit provenance and derivation are separate.
- **Correction appears necessary:** No for these passages; polymorphic endpoint mapping remains F49.
- **Dependencies:** ADR-0014; RFC-0025/0026/0029; ONT-Relation; TERM-Relation.

### F29 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0001/content.md`; `foundation/specifications/rfc/RFC-0003/content.md`; `foundation/specifications/rfc/RFC-0004/content.md`; `foundation/specifications/rfc/RFC-0014/content.md`; `foundation/specifications/rfc/RFC-0021/content.md`; `foundation/specifications/rfc/RFC-0023/content.md`.
- **Section / passage:** Examples: Requirement → refines → Specification; Finding may motivate Note; satisfies/verifiedBy chains; traceability matrix.
- **Semantic interpretation:** Illustrative engineering edges use some undeclared or currently disallowed combinations.
- **Affected concept/layer:** Relation / Predicate / examples.
- **Classification:** AMBIGUITY.
- **Explanation:** RFC-0001 and RFC-0003 use Requirement→Specification for refines, whereas current constraints allow Requirement→Requirement and no ONT-Specification exists. RFC-0004 Motivation says Finding may motivate Note, disallowed by current motivates. RFC-0023 Paths is compatible with RFC-0027 inverse vocabulary, but its matrix reintroduces Requirement→Specification and Specification→Component. RFC-0014 and RFC-0021 examples use satisfies and other conceptual names without concrete Foundation definitions. These are illustrative content, not persisted edges or additions to the predicate catalogue, but their unqualified appearance can imply valid canonical applications.
- **Correction appears necessary:** Clarify illustrative status or dependencies where examples imply current validity; do not infer new predicates or modify historical examples by default.
- **Dependencies:** RFC-0027 vocabulary; RFC-0029 exact matching; constraints/refines and motivates. No new concepts or predicates are selected here.

### F30 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0005/content.md`.
- **Section / passage:** Property Ownership; Canonical/Derived/Materialized; Metadata as Semantic Properties; Identity; Physical Representation.
- **Semantic interpretation:** Properties belong to the described concept, not the field or storage location; metadata is a semantic class of properties.
- **Affected concept/layer:** Property / Metadata / Entity / Artifact / Version.
- **Classification:** CONSISTENT.
- **Explanation:** Artifact, Entity, Process, Baseline and Release owners are permitted. Identical physical field names need not identify the same semantic property. A Property is independently identifiable only when its domain definition requires that.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0010; RFC-0003/0010/0012/0015; ONT-Property scope examined in F34.

### F31 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0010/content.md`.
- **Section / passage:** Summary; Artifact Identity/Type; Multiple Physical Representations; Artifact Metadata; Git; Serialization.
- **Semantic interpretation:** Logical Artifact carries knowledge, distinct from Entity and concrete manifestation, with Artifact-owned classification and identity.
- **Affected concept/layer:** Artifact / artifactType / ontologyType / Identity / Revision / Content / Metadata.
- **Classification:** CONSISTENT.
- **Explanation:** The clearest three-layer Artifact definition in Foundation. An Artifact has no required second technical ID in one-to-one representation. Git commits are not automatically Artifact Revisions or Entity Versions. Generated/physical representations do not multiply logical Artifacts automatically.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0010/0011/0013; RFC-0015/0030/0031; F14 notes older wording.

### F32 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0011/content.md`.
- **Section / passage:** Repository; Artifact Directory Structure; Canonical Files; Paths; Discovery/Loading; Generated Content.
- **Semantic interpretation:** Repository organization is physical; canonical discovery is distinct from interpretation.
- **Affected concept/layer:** Physical Representation / Identity / Content / Metadata / Relation.
- **Classification:** CONSISTENT.
- **Explanation:** A three-file directory is explicitly a representation of an Artifact, not its identity. Canonical metadata/relations retain ownership. Git is implementation provenance. The opening aim that loaders “identify artifact classes” is read with the later prohibition on inheriting meaning merely from paths.
- **Correction appears necessary:** No; path-based class identification should be read only as discovery, not ontology inference.
- **Dependencies:** ADR-0008/0011; RFC-0015/0030; F47 legacy classification fields.

### F33 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0012/content.md`; `foundation/specifications/rfc/RFC-0013/content.md`.
- **Section / passage:** Identity; Version Creation/Immutability; Baseline Membership/Identity; Git; Provenance; Migration.
- **Semantic interpretation:** Semantic version states and reproducible explicit Baseline selections are distinguished from physical snapshots.
- **Affected concept/layer:** Identity / Version / Revision / Metadata / Relation.
- **Classification:** CONSISTENT.
- **Explanation:** Technical changes and commits do not automatically create engineering states. Baselines can reference Entity Versions and Artifact Revisions without identifying those concepts. Migration explicitly preserves uncertainty rather than inventing history. Version and lifecycle trigger ambiguity is separately recorded in F54; exclusionary “distinct from Entity” wording in F40.
- **Correction appears necessary:** No for the separation and provenance rules.
- **Dependencies:** ADR-0012; RFC-0002/0010/0015/0023.

### F34 — AMBIGUITY

- **File(s):** `foundation/specifications/ontology/Metadata/content.md`; `foundation/specifications/ontology/Property/content.md`; `foundation/specifications/entity/ENTITY-0001/content.md`.
- **Section / passage:** Definition / Metadata.
- **Semantic interpretation:** Metadata and Properties are defined primarily as describing an Entity.
- **Affected concept/layer:** Metadata / Property / semantic owner.
- **Classification:** AMBIGUITY.
- **Explanation:** Compatible when describing Entity-specific uses. Read as exhaustive universal definitions, they exclude Artifact/revision/representation metadata and Properties explicitly allowed by ADR-0010, RFC-0003, RFC-0005 and RFC-0010. They do not explicitly prohibit other owners, so a narrowing ambiguity is recorded rather than a confirmed exclusion.
- **Correction appears necessary:** Clarify universal versus Entity-specific scope.
- **Dependencies:** ADR-0010 Metadata Ownership; RFC-0003 Metadata; RFC-0005 Property Ownership; RFC-0010 Artifact Metadata.

### F35 — CONTRADICTION

- **File(s):** `foundation/specifications/ontology/Finding/content.md`; `foundation/specifications/ontology/Review/content.md`; `foundation/specifications/ontology/Note/content.md`.
- **Section / passage:** Opening definitions: “A Finding/Review/Note is an engineering artifact”.
- **Semantic interpretation:** Semantic observations, examinations and notes are classified directly as Artifacts.
- **Affected concept/layer:** Entity / Artifact / ontologyType vs artifactType.
- **Classification:** CONTRADICTION.
- **Explanation:** Finding has explicit Entity semantics in ADR-0015; Review and Finding are Entity examples in RFC-0001; Note/Finding/Review are ontology classes used for Entity-typed relation constraints. The unqualified definitions identify these semantic concepts as Artifacts, rather than distinguishing them from their records/representations. This conflicts with the supplied Entity/Artifact model. A record Artifact representing a Finding or Review would be compatible, but that is not what the current “is” definition distinguishes.
- **Correction appears necessary:** Yes, semantic referents/type ownership need architectural reconciliation; no new concept or corrected definition is introduced.
- **Dependencies:** ADR-0013/0015; RFC-0001/0010/0020/0027; PRED-motivates constraints; contains Review→Finding in RFC-0027.

### F36 — AMBIGUITY

- **File(s):** `foundation/specifications/ontology/Note/content.md`.
- **Section / passage:** “Notes ... are not part of the ATON Foundation ontology itself”.
- **Semantic interpretation:** Note instances may be outside ontology definitions, or the Note Concept may be excluded from the ontology.
- **Affected concept/layer:** Ontology Concept / Entity instance / Artifact.
- **Classification:** AMBIGUITY.
- **Explanation:** The instance reading is compatible: a project Note is not itself a Concept definition. A type-level reading conflicts with the existence of ONT-Note and RFC-0027 initial vocabulary. This sentence follows an Artifact definition, so the distinction is not explicit.
- **Correction appears necessary:** Clarification appears necessary; deleting ONT-Note or excluding Notes is not decided.
- **Dependencies:** RFC-0020 Ontology and Engineering Entities; RFC-0027 Concept Model; PRED-motivates.

### F37 — CONSISTENT

- **File(s):** `foundation/specifications/ontology/Entity/content.md`; `foundation/specifications/glossary/TERM-Entity/content.md`; `foundation/specifications/glossary/TERM-Artifact/content.md`.
- **Section / passage:** Definitions; Role; Identity; Persistence Independence.
- **Semantic interpretation:** Entity classification and identity are distinct from Artifact classification/identity and concrete representation.
- **Affected concept/layer:** Entity / Artifact / ontologyType / artifactType / Identity.
- **Classification:** CONSISTENT.
- **Explanation:** Explicit current clauses match the review basis, with shared ID values permitted and physical co-location irrelevant. Glossary entries point to model definitions rather than substituting different identities. Artifact representation-language ambiguity is confined to F14.
- **Correction appears necessary:** No for these explicit ownership clauses.
- **Dependencies:** ENTITY-0001; ADR-0013; ONT-Artifact; RFC-0010.

### F38 — CONSISTENT

- **File(s):** `foundation/specifications/ontology/Predicate/content.md`; `foundation/specifications/glossary/TERM-Predicate/content.md`; `foundation/specifications/ontology/Relation/content.md`; `foundation/specifications/glossary/TERM-Relation/content.md`.
- **Section / passage:** Definitions; constraints; identity; persistence independence.
- **Semantic interpretation:** Predicate supplies meaning; Relation is its occurrence between Entities, identified by source/predicate/target.
- **Affected concept/layer:** Predicate / Relation / Identity / ontologyType.
- **Classification:** CONSISTENT.
- **Explanation:** Ontology Predicate “Concept→Concept” describes applicability at class level; glossary Entity endpoints describe instances. They can coexist as long as this distinction is maintained. Predicate as Entity explicitly owns ontologyType; its representing Artifact does not. Relation identity is independent of serialization.
- **Correction appears necessary:** No; broader Artifact endpoint applicability is examined in F49.
- **Dependencies:** RFC-0025/0026/0027/0029; ADR-0014.

### F39 — CONSISTENT

- **File(s):** `foundation/specifications/ontology/ADR/content.md`; `foundation/specifications/ontology/AX/content.md`; `foundation/specifications/ontology/Collection/content.md`; `foundation/specifications/ontology/Component/content.md`; `foundation/specifications/ontology/Constitution/content.md`; `foundation/specifications/ontology/Decision/content.md`; `foundation/specifications/ontology/Definition/content.md`; `foundation/specifications/ontology/GlossaryEntry/content.md`; `foundation/specifications/ontology/Interface/content.md`; `foundation/specifications/ontology/RFC/content.md`; `foundation/specifications/ontology/Requirement/content.md`; `foundation/specifications/ontology/Test/content.md`; `foundation/specifications/ontology/Thing/content.md`; `foundation/specifications/ontology/View/content.md`.
- **Section / passage:** Definition; Role in ATON; References where present.
- **Semantic interpretation:** Ontology categories define decisions, experience, groupings, building blocks, governance, definitions, terms, interfaces, specifications, requirements, tests, general things and projections.
- **Affected concept/layer:** Ontology Concept / Entity / View / Content.
- **Classification:** CONSISTENT.
- **Explanation:** None makes a filename, path or format the semantic identity. ADR and Constitution use document vocabulary but describe semantic decisions/governance, not an imposed file identity. Test can represent an activity or specification without asserting a technical file type. Collection is explicitly logical; View is a projection rather than source authority. The category definitions alone do not provide an adopted specialization taxonomy.
- **Correction appears necessary:** No confirmed correction to these definitions.
- **Dependencies:** ENTITY-0001; RFC-0020/0027; Collection and View modeling ambiguity F40.

### F40 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0013/content.md`; `foundation/specifications/rfc/RFC-0021/content.md`; `foundation/specifications/rfc/RFC-0022/content.md`.
- **Section / passage:** Summary: Baseline/View/Collection “distinct from ... Engineering Entity”; RFC-0022 Goals.
- **Semantic interpretation:** Specialized addressable engineering concepts may be distinct types, or excluded from the universal Entity model.
- **Affected concept/layer:** Entity / ontology classification / Identity.
- **Classification:** AMBIGUITY.
- **Explanation:** Differentiating a Baseline, Collection or View from a generic Entity is compatible as specialized semantics or definition/output distinction. Read as categorical exclusion, it conflicts with ENTITY-0001 all engineering objects and RFC-0001 Baseline/Release Entity examples. ONT-Collection and ONT-View exist, yet their instance relationship to Entity is not explicit here.
- **Correction appears necessary:** Clarify specialization, object identity and definition/output boundaries; do not introduce new fundamental kinds.
- **Dependencies:** ENTITY-0001; ONT-Collection/View; RFC-0001; RFC-0020/0027.

### F41 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0015/content.md`; `foundation/specifications/rfc/RFC-0024/content.md`.
- **Section / passage:** Physical Representation; boundaries; loading/export; canonical input; architecture/output.
- **Semantic interpretation:** Technical manifestations are normalized into canonical domain semantics; renderer output is derived, non-authoritative.
- **Affected concept/layer:** Physical Representation / Artifact / Content / Metadata / Relation / Identity.
- **Classification:** CONSISTENT.
- **Explanation:** Database/API/exchange/Git/generated forms are technical mechanisms. Normative serialization profiles can coexist with model independence. Canonical input prevents renderer-specific fields or layout becoming semantics. “Foundation artifacts” at the render boundary can mean domain representations of those artifacts; this is explained by the input boundary.
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0008/0011; RFC-0010/0030/0031; AX presentation model.

### F42 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0020/content.md`.
- **Section / passage:** Ontology Type; Concepts/Entities/Artifacts; Metadata; Evolution; Persistence.
- **Semantic interpretation:** Ontology Concepts classify Engineering Entities explicitly; Artifact Type is separate even in shared metadata.
- **Affected concept/layer:** ontologyType / artifactType / Entity / Artifact / Predicate.
- **Classification:** CONSISTENT.
- **Explanation:** Concept definitions, instance classification and serialized identifiers are separated. An Artifact containing multiple Entities cannot transfer one ontologyType to them all automatically. Technical type systems do not define the ontology.
- **Correction appears necessary:** No for explicit ownership. Ontology evolution and self-description are addressed in F48/F55.
- **Dependencies:** ADR-0008; ENTITY-0001; RFC-0010/0027/0029/0030.

### F43 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0026/content.md`; `foundation/specifications/rfc/RFC-0027/content.md`.
- **Section / passage:** Predicate identity/direction; constraints; ontology model; Concept specialization; explicit/derived/inferred relations.
- **Semantic interpretation:** Predicates have canonical semantic contracts; Entity Concept classification differs from Artifact classification; specialization does not inherit pair validity.
- **Affected concept/layer:** Predicate / Relation / ontologyType / artifactType / Identity.
- **Classification:** CONSISTENT.
- **Explanation:** Predicate names identify relationship definitions, not arbitrary YAML conveniences. Inverse definitions are explicit and do not imply storing inverse instances. Independent constraints in RFC-0026 are illustrative semantic descriptions and defer to the exact pair model; no competing physical schema is adopted there.
- **Correction appears necessary:** No for these principles; concrete conflicts are F44–F46.
- **Dependencies:** RFC-0025/0029; ADR-0014; ONT-Predicate; TERM-Predicate.

### F44 — CONTRADICTION

- **File(s):** `foundation/specifications/predicates/references/content.md`; `foundation/specifications/predicates/references/constraints.yaml`; `foundation/specifications/rfc/RFC-0027/content.md`.
- **Section / passage:** PRED-references Allowed Pairs/Semantic Validation; RFC-0027 references; ANY-CONCEPT pair.
- **Semantic interpretation:** Human-readable predicate permits only Artifact→Artifact; executable constraint permits every valid Concept combination.
- **Affected concept/layer:** Predicate / Relation / Entity vs Artifact classification.
- **Classification:** CONTRADICTION.
- **Explanation:** The prose explicitly forbids other combinations and specialization-based expansion. ANY-CONCEPT×ANY-CONCEPT is an explicit wildcard pair and admits ONT-RFC→ONT-ADR, ONT-GlossaryEntry→ONT-Entity, etc. RFC-0029 authorizes the pattern mechanism, but does not itself redefine the references contract. These current definitions are incompatible irrespective of serialization ownership.
- **Correction appears necessary:** Yes, reconciliation between normative meaning and allowed-pair contract is necessary; neither narrowing nor broadening is selected.
- **Dependencies:** RFC-0029 Constraint Patterns/Exact Pair Matching; RFC-0027 Initial Predicate Vocabulary; TERM-Relation; actual references in sidecars (F50).

### F45 — CONTRADICTION

- **File(s):** `foundation/specifications/predicates/governs/constraints.yaml`; `foundation/specifications/predicates/refines/constraints.yaml`; `foundation/specifications/rfc/RFC-0027/content.md`.
- **Section / passage:** governs/refines Allowed Pairs; initial vocabulary.
- **Semantic interpretation:** Concrete constraints add Constitution governance and AX refinement pairs absent from the initial exact-pair catalogue.
- **Affected concept/layer:** Predicate / ontologyType / Relation.
- **Classification:** CONTRADICTION.
- **Explanation:** governs constraints include ONT-Constitution→ONT-Artifact/Collection, whereas RFC-0027 governs lists only ADR sources. refines constraints add ONT-AX→ONT-AX, absent from RFC-0027. Because the catalogue asserts exact allowed pairs with no implicit inheritance, the contracts differ. Adding pairs is a semantic ontology change, not merely physical serialization. A current expansion may be intended but no aligned catalogue rule identifies it.
- **Correction appears necessary:** Yes, the definition authority and exact pair sets need reconciliation.
- **Dependencies:** RFC-0027 Allowed Source-to-Target Pairs and Ontology Evolution; RFC-0029; AX-0002/0003 persisted refines relations; Constitution governs foundation.

### F46 — AMBIGUITY

- **File(s):** `foundation/specifications/predicates/governs/content.md`; `foundation/specifications/predicates/motivates/content.md`; `foundation/specifications/predicates/references/content.md`; `foundation/specifications/predicates/refines/content.md`.
- **Section / passage:** Meaning/Direction: “artifact” source/target; allowed Concept pairs.
- **Semantic interpretation:** Predicate meanings often use Artifact shorthand while validation classifies semantic Entity endpoints.
- **Affected concept/layer:** Predicate / Relation / Entity / Artifact.
- **Classification:** AMBIGUITY.
- **Explanation:** refines includes Component and Interface semantic Concepts and motivates includes Note/Finding. “Artifact” can mean their logical engineering representations, but may instead transfer relations and typing to Artifacts. Exact pairs are coherent for motivates/refines except F45; endpoint ownership is not explained in the meaning paragraphs. Constraint YAML itself uses canonical ONT identifiers and does not classify physical files.
- **Correction appears necessary:** Clarify endpoint referents where prose says Artifact; do not automatically recast every such use as contradiction.
- **Dependencies:** ADR-0013/0014; ENTITY-0001; RFC-0020/0027; ONT-Finding/Review/Note F35.

### F47 — AMBIGUITY

- **File(s):** `foundation/constitution/CONSTITUTION/metadata.yaml`; `foundation/specifications/adr/ADR-0001/metadata.yaml`; `foundation/specifications/adr/ADR-0002/metadata.yaml`; `foundation/specifications/adr/ADR-0003/metadata.yaml`; `foundation/specifications/adr/ADR-0004/metadata.yaml`; `foundation/specifications/adr/ADR-0005/metadata.yaml`; `foundation/specifications/adr/ADR-0006/metadata.yaml`; `foundation/specifications/adr/ADR-0007/metadata.yaml`; `foundation/specifications/ax/AX-0001/metadata.yaml`; `foundation/specifications/ax/AX-0002/metadata.yaml`; `foundation/specifications/ax/AX-0003/metadata.yaml`; `foundation/specifications/glossary/TERM-Artifact/metadata.yaml`; `foundation/specifications/glossary/TERM-Entity/metadata.yaml`; `foundation/specifications/glossary/TERM-Predicate/metadata.yaml`; `foundation/specifications/glossary/TERM-Relation/metadata.yaml`; `foundation/specifications/ontology/ADR/metadata.yaml`; `foundation/specifications/ontology/AX/metadata.yaml`; `foundation/specifications/ontology/Artifact/metadata.yaml`; `foundation/specifications/ontology/Collection/metadata.yaml`; `foundation/specifications/ontology/Component/metadata.yaml`; `foundation/specifications/ontology/Constitution/metadata.yaml`; `foundation/specifications/ontology/Decision/metadata.yaml`; `foundation/specifications/ontology/Definition/metadata.yaml`; `foundation/specifications/ontology/Entity/metadata.yaml`; `foundation/specifications/ontology/Finding/metadata.yaml`; `foundation/specifications/ontology/GlossaryEntry/metadata.yaml`; `foundation/specifications/ontology/Interface/metadata.yaml`; `foundation/specifications/ontology/Metadata/metadata.yaml`; `foundation/specifications/ontology/Note/metadata.yaml`; `foundation/specifications/ontology/Predicate/metadata.yaml`; `foundation/specifications/ontology/Property/metadata.yaml`; `foundation/specifications/ontology/RFC/metadata.yaml`; `foundation/specifications/ontology/Relation/metadata.yaml`; `foundation/specifications/ontology/Requirement/metadata.yaml`; `foundation/specifications/ontology/Review/metadata.yaml`; `foundation/specifications/ontology/Test/metadata.yaml`; `foundation/specifications/ontology/Thing/metadata.yaml`; `foundation/specifications/ontology/View/metadata.yaml`; `foundation/specifications/predicates/governs/metadata.yaml`; `foundation/specifications/predicates/motivates/metadata.yaml`; `foundation/specifications/predicates/references/metadata.yaml`; `foundation/specifications/predicates/refines/metadata.yaml`; `foundation/specifications/rfc/RFC-0000/metadata.yaml`; `foundation/specifications/rfc/RFC-0001/metadata.yaml`; `foundation/specifications/rfc/RFC-0002/metadata.yaml`; `foundation/specifications/rfc/RFC-0003/metadata.yaml`; `foundation/specifications/rfc/RFC-0004/metadata.yaml`; `foundation/specifications/rfc/RFC-0005/metadata.yaml`; `foundation/specifications/rfc/RFC-0010/metadata.yaml`; `foundation/specifications/rfc/RFC-0011/metadata.yaml`; `foundation/specifications/rfc/RFC-0012/metadata.yaml`; `foundation/specifications/rfc/RFC-0013/metadata.yaml`; `foundation/specifications/rfc/RFC-0014/metadata.yaml`; `foundation/specifications/rfc/RFC-0015/metadata.yaml`; `foundation/specifications/rfc/RFC-0020/metadata.yaml`; `foundation/specifications/rfc/RFC-0021/metadata.yaml`; `foundation/specifications/rfc/RFC-0022/metadata.yaml`; `foundation/specifications/rfc/RFC-0023/metadata.yaml`; `foundation/specifications/rfc/RFC-0029/metadata.yaml`; `foundation/specifications/rfc/RFC-0030/metadata.yaml`; `foundation/specifications/rfc/RFC-0031/metadata.yaml`.
- **Section / passage:** `type` / `entityType` fields alongside or without ontologyType.
- **Semantic interpretation:** Legacy representation classifications have no explicit current mapping to artifactType.
- **Affected concept/layer:** artifactType / ontologyType / Metadata / Property.
- **Classification:** AMBIGUITY.
- **Explanation:** ADR-0001–0007 and Constitution use type; early AX use type; many RFCs/glossary and all ontology/predicate metadata use entityType. They can be legacy physical classifications without owning Entity semantics. Naming entityType, however, can imply a second primary Entity classification. No Foundation schema or domain definition establishes an alias to artifactType, and the review must not silently create one. Their presence is not proof of extra Entity types.
- **Correction appears necessary:** Clarify field meaning/authority in future work. Do not rename fields or infer artifactType here.
- **Dependencies:** ADR-0008; RFC-0010 Artifact Type; RFC-0020/0030; empty schemas. Exact fields per file are included in the inventory.

### F48 — AMBIGUITY

- **File(s):** `foundation/specifications/ontology/ADR/metadata.yaml`; `foundation/specifications/ontology/AX/metadata.yaml`; `foundation/specifications/ontology/Artifact/metadata.yaml`; `foundation/specifications/ontology/Collection/metadata.yaml`; `foundation/specifications/ontology/Component/metadata.yaml`; `foundation/specifications/ontology/Constitution/metadata.yaml`; `foundation/specifications/ontology/Decision/metadata.yaml`; `foundation/specifications/ontology/Definition/metadata.yaml`; `foundation/specifications/ontology/Entity/metadata.yaml`; `foundation/specifications/ontology/Finding/metadata.yaml`; `foundation/specifications/ontology/GlossaryEntry/metadata.yaml`; `foundation/specifications/ontology/Interface/metadata.yaml`; `foundation/specifications/ontology/Metadata/metadata.yaml`; `foundation/specifications/ontology/Note/metadata.yaml`; `foundation/specifications/ontology/Predicate/metadata.yaml`; `foundation/specifications/ontology/Property/metadata.yaml`; `foundation/specifications/ontology/RFC/metadata.yaml`; `foundation/specifications/ontology/Relation/metadata.yaml`; `foundation/specifications/ontology/Requirement/metadata.yaml`; `foundation/specifications/ontology/Review/metadata.yaml`; `foundation/specifications/ontology/Test/metadata.yaml`; `foundation/specifications/ontology/Thing/metadata.yaml`; `foundation/specifications/ontology/View/metadata.yaml`.
- **Section / passage:** All 23 Concept-definition metadata files: id/ title/ entityType ontology / status; no ontologyType.
- **Semantic interpretation:** Concept identity is explicit; classification of the Entity representing the Concept definition is unspecified.
- **Affected concept/layer:** Ontology Concept / Entity / ontologyType / Identity.
- **Classification:** AMBIGUITY.
- **Explanation:** ONT identifiers establish Concept identity, not necessarily the ontologyType of a self-describing definition Entity. All 23 ontology metadata files omit ontologyType. If these are ordinary Engineering Entities, this fails universal explicit typing; if the ontology construct layer has distinct self-description rules, those rules are not stated. RFC-0020 distinguishes Concepts from instances and RFC-0027 protects ontology constructs from ordinary Artifact assumptions. Therefore the absence is a confirmed fact but its semantic violation is conditional, not an invented need for a new ontology metatype.
- **Correction appears necessary:** Clarify self-description applicability and mapping; do not add an ontology Concept or infer ONT-Thing/ONT-Entity.
- **Dependencies:** ADR-0001/0008; ENTITY-0001; RFC-0020 Ontology and Engineering Entities; RFC-0027 Concept Model; ONT-Predicate.

### F49 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0004/content.md`; `foundation/specifications/rfc/RFC-0010/content.md`; `foundation/specifications/adr/ADR-0014/content.md`; `foundation/specifications/ontology/Relation/content.md`; `foundation/specifications/glossary/TERM-Relation/content.md`; `foundation/specifications/rfc/RFC-0029/content.md`.
- **Section / passage:** Artifact relation endpoints vs Entity-only Relation definition/evaluation.
- **Semantic interpretation:** Canonical relations may connect Artifacts and other canonical objects, but typing/evaluation generally resolves Engineering Entities.
- **Affected concept/layer:** Relation / Predicate / artifactType / ontologyType.
- **Classification:** AMBIGUITY.
- **Explanation:** RFC-0010 allows Artifact→Artifact/Entity combinations; RFC-0004 allows Artifacts/Versions/Processes. ONT-Relation and glossary use Entity endpoints; RFC-0029 resolves Entities and their Concepts. A compatible implementation could explicitly model addressable Artifact concepts as Entity endpoints while retaining distinct referents, but Foundation does not specify that mapping or how artifactType participates. It must not simply borrow the represented Entity’s ontologyType.
- **Correction appears necessary:** Yes, polymorphic endpoint identity/type resolution needs clarification, especially for Artifact-only and compound representations.
- **Dependencies:** ADR-0013 Identity/Traceability; RFC-0020/0027/0029; F15 source ownership; F44 references.

### F50 — AMBIGUITY

- **File(s):** `foundation/constitution/CONSTITUTION/relations.yaml`; `foundation/specifications/adr/ADR-0001/relations.yaml`; `foundation/specifications/adr/ADR-0002/relations.yaml`; `foundation/specifications/adr/ADR-0003/relations.yaml`; `foundation/specifications/adr/ADR-0004/relations.yaml`; `foundation/specifications/adr/ADR-0005/relations.yaml`; `foundation/specifications/adr/ADR-0006/relations.yaml`; `foundation/specifications/adr/ADR-0007/relations.yaml`; `foundation/specifications/adr/ADR-0008/relations.yaml`; `foundation/specifications/adr/ADR-0009/relations.yaml`; `foundation/specifications/adr/ADR-0010/relations.yaml`; `foundation/specifications/adr/ADR-0011/relations.yaml`; `foundation/specifications/adr/ADR-0012/relations.yaml`; `foundation/specifications/adr/ADR-0013/relations.yaml`; `foundation/specifications/adr/ADR-0014/relations.yaml`; `foundation/specifications/adr/ADR-0015/relations.yaml`; `foundation/specifications/adr/ADR-0016/relations.yaml`; `foundation/specifications/adr/ADR-0017/relations.yaml`; `foundation/specifications/adr/ADR-0018/relations.yaml`; `foundation/specifications/ax/AX-0001/relations.yaml`; `foundation/specifications/ax/AX-0002/relations.yaml`; `foundation/specifications/ax/AX-0003/relations.yaml`; `foundation/specifications/entity/ENTITY-0001/relations.yaml`; `foundation/specifications/glossary/TERM-Artifact/relations.yaml`; `foundation/specifications/glossary/TERM-Entity/relations.yaml`; `foundation/specifications/glossary/TERM-Predicate/relations.yaml`; `foundation/specifications/glossary/TERM-Relation/relations.yaml`; `foundation/specifications/ontology/ADR/relations.yaml`; `foundation/specifications/ontology/Artifact/relations.yaml`; `foundation/specifications/ontology/Collection/relations.yaml`; `foundation/specifications/ontology/Component/relations.yaml`; `foundation/specifications/ontology/Decision/relations.yaml`; `foundation/specifications/ontology/Definition/relations.yaml`; `foundation/specifications/ontology/Entity/relations.yaml`; `foundation/specifications/ontology/Finding/relations.yaml`; `foundation/specifications/ontology/GlossaryEntry/relations.yaml`; `foundation/specifications/ontology/Interface/relations.yaml`; `foundation/specifications/ontology/Metadata/relations.yaml`; `foundation/specifications/ontology/Note/relations.yaml`; `foundation/specifications/ontology/Predicate/relations.yaml`; `foundation/specifications/ontology/Property/relations.yaml`; `foundation/specifications/ontology/RFC/relations.yaml`; `foundation/specifications/ontology/Relation/relations.yaml`; `foundation/specifications/ontology/Requirement/relations.yaml`; `foundation/specifications/ontology/Review/relations.yaml`; `foundation/specifications/ontology/Test/relations.yaml`; `foundation/specifications/ontology/Thing/relations.yaml`; `foundation/specifications/ontology/View/relations.yaml`; `foundation/specifications/predicates/governs/relations.yaml`; `foundation/specifications/predicates/motivates/relations.yaml`; `foundation/specifications/predicates/references/relations.yaml`; `foundation/specifications/predicates/refines/relations.yaml`; `foundation/specifications/rfc/RFC-0000/relations.yaml`; `foundation/specifications/rfc/RFC-0001/relations.yaml`; `foundation/specifications/rfc/RFC-0002/relations.yaml`; `foundation/specifications/rfc/RFC-0003/relations.yaml`; `foundation/specifications/rfc/RFC-0004/relations.yaml`; `foundation/specifications/rfc/RFC-0005/relations.yaml`; `foundation/specifications/rfc/RFC-0010/relations.yaml`; `foundation/specifications/rfc/RFC-0011/relations.yaml`; `foundation/specifications/rfc/RFC-0012/relations.yaml`; `foundation/specifications/rfc/RFC-0013/relations.yaml`; `foundation/specifications/rfc/RFC-0014/relations.yaml`; `foundation/specifications/rfc/RFC-0015/relations.yaml`; `foundation/specifications/rfc/RFC-0020/relations.yaml`; `foundation/specifications/rfc/RFC-0021/relations.yaml`; `foundation/specifications/rfc/RFC-0022/relations.yaml`; `foundation/specifications/rfc/RFC-0023/relations.yaml`; `foundation/specifications/rfc/RFC-0024/relations.yaml`; `foundation/specifications/rfc/RFC-0025/relations.yaml`; `foundation/specifications/rfc/RFC-0026/relations.yaml`; `foundation/specifications/rfc/RFC-0027/relations.yaml`; `foundation/specifications/rfc/RFC-0028/relations.yaml`; `foundation/specifications/rfc/RFC-0029/relations.yaml`; `foundation/specifications/rfc/RFC-0030/relations.yaml`; `foundation/specifications/rfc/RFC-0031/relations.yaml`.
- **Section / passage:** Persisted references, refines, governs and legacy collections.
- **Semantic interpretation:** YAML stores relation instances or unresolved migration data, not Predicate definitions.
- **Affected concept/layer:** Relation / Predicate / Identity / ontologyType.
- **Classification:** AMBIGUITY.
- **Explanation:** Numerous references connect RFC, ADR, glossary, ontology and Predicate-definition Entities, not literal ONT-Artifact→ONT-Artifact pairs. Wildcard constraints accept known Concepts but the references prose does not (F44). ADR-0001 children and ADR-0002–0005 related are unresolved by RFC-0028; many dependsOn/relatedTo relations likewise remain explicitly unresolved. Empty collections create no edges. Nonempty supersedes/supersededBy are absent, so their empty keys do not adopt new Predicate semantics. AX-0002/0003 refines use embedded objects, a supported legacy representation, with ONT-AX pairs admitted only in concrete constraints (F45). No relation is silently reclassified here.
- **Correction appears necessary:** Resolve the referenced definition conflicts and preserve explicit unresolved migration status; no automatic correction of edges.
- **Dependencies:** RFC-0025 supported serialization; RFC-0028 migration; RFC-0029; concrete predicate definitions/constraints. Inventory lists exact collection targets.

### F51 — AMBIGUITY

- **File(s):** `foundation/constitution/CONSTITUTION/metadata.yaml`.
- **Section / passage:** parents/children/references/related fields; version/created/updated/type.
- **Semantic interpretation:** Legacy relation-like metadata coexists with separate relations.yaml and Entity ontologyType.
- **Affected concept/layer:** Metadata / Relation / Version / technical time.
- **Classification:** AMBIGUITY.
- **Explanation:** Nonempty related lists ADR-0001–0006 in metadata, while relations.yaml has governs foundation. If related is canonical relation data, it is mixed with ordinary metadata despite RFC-0003 separation and not covered by the relations source. If it is legacy/supplemental navigation information, it should not be treated as a verified semantic relation. created/updated do not name their event owner. Co-location is not the reason for concern: authority and relation interpretation are missing.
- **Correction appears necessary:** Clarify semantic authority and field role; do not move metadata or manufacture relations.
- **Dependencies:** ADR-0005/0010; RFC-0003 Metadata and Relations; RFC-0028 unresolved related; RFC-0030. Temporal ambiguity also F53.

### F52 — CONTRADICTION

- **File(s):** `foundation/specifications/adr/ADR-0008/content.md`; `foundation/specifications/adr/ADR-0008/metadata.yaml`; `foundation/specifications/rfc/RFC-0030/content.md`; `foundation/specifications/rfc/RFC-0030/metadata.yaml`.
- **Section / passage:** ADR-0008 Status Accepted vs metadata Draft; RFC-0030 Status Proposed vs metadata Draft.
- **Semantic interpretation:** Human-readable lifecycle claims differ from canonical status values.
- **Affected concept/layer:** Metadata / Content / lifecycle authority.
- **Classification:** CONTRADICTION.
- **Explanation:** These are actual current conflicting states, not merely different capitalization. ADR-0010/RFC-0003 canonical authority and ADR-0017 explicit Decision state require a defined interpretation. Choosing content or metadata silently would resolve a governance question the task does not authorize. This does not negate the user-supplied basis used for review.
- **Correction appears necessary:** Yes, lifecycle authority/conflicting state needs reconciliation; no state is changed.
- **Dependencies:** ADR-0010 Metadata Authority; ADR-0017 Accepted; RFC-0003 Authoritative Metadata; RFC-0031 heading/content vs metadata.

### F53 — AMBIGUITY

- **File(s):** `foundation/constitution/CONSTITUTION/metadata.yaml`; `foundation/specifications/adr/ADR-0001/metadata.yaml`; `foundation/specifications/adr/ADR-0002/metadata.yaml`; `foundation/specifications/adr/ADR-0003/metadata.yaml`; `foundation/specifications/adr/ADR-0004/metadata.yaml`; `foundation/specifications/adr/ADR-0005/metadata.yaml`; `foundation/specifications/adr/ADR-0006/metadata.yaml`; `foundation/specifications/adr/ADR-0007/metadata.yaml`; `foundation/specifications/adr/ADR-0008/metadata.yaml`; `foundation/specifications/adr/ADR-0010/metadata.yaml`; `foundation/specifications/adr/ADR-0013/metadata.yaml`; `foundation/specifications/adr/ADR-0014/metadata.yaml`; `foundation/specifications/ax/AX-0001/metadata.yaml`; `foundation/specifications/ax/AX-0002/metadata.yaml`; `foundation/specifications/ax/AX-0003/metadata.yaml`; `foundation/specifications/ax/AX-0004/metadata.yaml`; `foundation/specifications/ax/AX-0005/metadata.yaml`; `foundation/specifications/ax/AX-0006/metadata.yaml`; `foundation/specifications/ax/AX-0007/metadata.yaml`; `foundation/specifications/ax/AX-0008/metadata.yaml`; `foundation/specifications/ax/AX-0009/metadata.yaml`; `foundation/specifications/ax/AX-0010/metadata.yaml`; `foundation/specifications/entity/ENTITY-0001/metadata.yaml`; `foundation/specifications/glossary/TERM-Artifact/metadata.yaml`; `foundation/specifications/glossary/TERM-Entity/metadata.yaml`; `foundation/specifications/ontology/Artifact/metadata.yaml`; `foundation/specifications/ontology/Entity/metadata.yaml`; `foundation/specifications/ontology/Predicate/metadata.yaml`; `foundation/specifications/rfc/RFC-0000/metadata.yaml`; `foundation/specifications/rfc/RFC-0001/metadata.yaml`; `foundation/specifications/rfc/RFC-0002/metadata.yaml`; `foundation/specifications/rfc/RFC-0003/metadata.yaml`; `foundation/specifications/rfc/RFC-0004/metadata.yaml`; `foundation/specifications/rfc/RFC-0005/metadata.yaml`; `foundation/specifications/rfc/RFC-0010/metadata.yaml`; `foundation/specifications/rfc/RFC-0011/metadata.yaml`; `foundation/specifications/rfc/RFC-0012/metadata.yaml`; `foundation/specifications/rfc/RFC-0013/metadata.yaml`; `foundation/specifications/rfc/RFC-0020/metadata.yaml`; `foundation/specifications/rfc/RFC-0021/metadata.yaml`; `foundation/specifications/rfc/RFC-0022/metadata.yaml`; `foundation/specifications/rfc/RFC-0023/metadata.yaml`; `foundation/specifications/rfc/RFC-0024/metadata.yaml`; `foundation/specifications/rfc/RFC-0025/metadata.yaml`; `foundation/specifications/rfc/RFC-0027/metadata.yaml`; `foundation/specifications/rfc/RFC-0030/metadata.yaml`.
- **Section / passage:** Existing version / created / updated fields.
- **Semantic interpretation:** Persisted labels and timestamps do not by themselves identify semantic Version, Artifact Revision or engineering events.
- **Affected concept/layer:** Metadata / Identity / Revision / Version.
- **Classification:** AMBIGUITY.
- **Explanation:** No schema defines whether version is the represented Entity Version, Artifact revision label, document profile version, or another property. created/updated do not distinguish engineering events from authoring/technical events. Their explicit persistence is compatible with canonical authority, and semver-looking values alone are not a contradiction. No Git chronology or semantic version violation is inferred in this current-state review.
- **Correction appears necessary:** Clarify owner, scope and event meaning where relied on normatively; no IDs or versions should be changed by this review.
- **Dependencies:** ADR-0010 Temporal Information; ADR-0012; RFC-0010/0012; RFC-0003/0005; empty schemas.

### F54 — AMBIGUITY

- **File(s):** `foundation/specifications/adr/ADR-0012/content.md`; `foundation/specifications/adr/ADR-0017/content.md`; `foundation/specifications/rfc/RFC-0012/content.md`; `foundation/specifications/rfc/RFC-0003/content.md`; `foundation/specifications/rfc/RFC-0005/content.md`.
- **Section / passage:** Version Creation vs Versions and Lifecycle; ADR lifecycle Versioning; metadata/property version effects.
- **Semantic interpretation:** Semantic change creates a Version, but lifecycle transitions/property changes are sometimes stated only as potentially version-creating.
- **Affected concept/layer:** Version / Metadata / lifecycle / Property.
- **Classification:** AMBIGUITY.
- **Explanation:** RFC-0012 Version Creation lists lifecycle transition and normative metadata change as examples requiring a new Version, while Versions and Lifecycle says a transition MAY create a Version when it changes semantic state. ADR-0017 does not specify that every transition establishes a new Version. The texts are reconcilable if some changes are non-versioned or not established authoritative states, but the normative trigger and governed scope are not explicit. This is not evidence that existing version numbers are wrong.
- **Correction appears necessary:** Clarify version creation criteria and established-state scope, not renumber artifacts.
- **Dependencies:** ADR-0012 Engineering Version/Immutability; RFC-0003 Metadata Evolution; RFC-0005 Property and Engineering Versions; F53.

### F55 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0020/content.md`.
- **Section / passage:** Ontology and Versioning: changing ontology definition does not automatically create Entity/Version unless model requires it.
- **Semantic interpretation:** Impact on classified instances may be distinguished from evolution of the definition itself.
- **Affected concept/layer:** Ontology Concept / Entity / Version.
- **Classification:** AMBIGUITY.
- **Explanation:** Compatible when it says that changing a Concept does not automatically version every classified instance. If applied to an Entity representing the changed Concept definition itself, substantive canonical semantic change is version-relevant under ADR-0012/RFC-0012. The text does not identify which Entity is meant.
- **Correction appears necessary:** Clarify definition evolution versus instance impact; no retrospective versions or concepts are introduced.
- **Dependencies:** ADR-0001; RFC-0012; RFC-0020 Ontology Evolution; RFC-0027 Ontology Evolution; F48 self-description.

### F56 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0028/content.md`.
- **Section / passage:** Migration states; Initial Legacy Classification; External Targets; no automatic semantic migration.
- **Semantic interpretation:** Legacy relations preserve meaning and unresolved status; external Entities are not nonexistent local Artifacts.
- **Affected concept/layer:** Predicate / Relation / Identity / Entity vs Artifact.
- **Classification:** CONSISTENT.
- **Explanation:** Name similarity is not semantic authority. Canonical/inverse/deprecated/unresolved are distinct. External foundation and ietf:rfc:2119 targets need not become local Artifacts. Existing Foundation references to NOTE identifiers outside Foundation are not automatically invalid just because those targets are outside scope. Exact external ontology typing remains a future-model question, not inferred here.
- **Correction appears necessary:** No automatic migration or local artifact creation.
- **Dependencies:** ADR-0014 External Targets; RFC-0025/0029; Constitution relations; RFC-0000 references.

### F57 — HISTORICAL / NON-NORMATIVE

- **File(s):** `foundation/specifications/rfc/RFC-0028/content.md`.
- **Section / passage:** Existing Foundation Relations; Initial Legacy Classification; migration decision example.
- **Semantic interpretation:** Observed legacy classes and hypothetical mappings record earlier migration analysis.
- **Affected concept/layer:** Predicate / historical state.
- **Classification:** HISTORICAL / NON-NORMATIVE.
- **Explanation:** The observed list is not an exhaustive current file inventory. children→refines is an example of a possible explicitly justified decision, not adoption of that mapping. referenced-by is discussed historically but has no current nonempty Foundation instance. Keeping these passages does not add predicates or reinterpret existing edges.
- **Correction appears necessary:** No consistency rewrite of historical observations.
- **Dependencies:** RFC-0027/0029; actual serialized inventory F50.

### F58 — CONTRADICTION

- **File(s):** `foundation/specifications/rfc/RFC-0029/content.md`.
- **Section / passage:** Motivation; Separation from the Relation Model; Ontology Authority: “continues to represent predicate + target”.
- **Semantic interpretation:** The current canonical Relation instance is asserted to contain only predicate and target with Entity source supplied externally.
- **Affected concept/layer:** Relation / Identity / source ownership.
- **Classification:** CONTRADICTION.
- **Explanation:** RFC-0025 now requires each Relation to identify source, predicate and target, preserving all three canonical identities. RFC-0029 describes the old source-less object as unchanged current normative model. A serialization may omit source when an unambiguous semantic owner supplies it; claiming that the canonical object continues to be only predicate+target conflicts with the current canonical model.
- **Correction appears necessary:** Yes, internal-model claim/dependency needs reconciliation; no model is edited.
- **Dependencies:** RFC-0025 Relation Domain Object and Canonical Representation; ADR-0014 Relation Identity; TERM-Relation; ENTITY-0001 Relationships.

### F59 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0029/content.md`.
- **Section / passage:** Constraint Patterns; Concept Identity; exact matching; verification; cardinality; migration.
- **Semantic interpretation:** Explicit canonical Concept pairs/patterns define applicability, separately from structural Relation instances.
- **Affected concept/layer:** Predicate / Relation / ontologyType / Identity.
- **Classification:** CONSISTENT.
- **Explanation:** ANY-CONCEPT explicitly matches known canonical Concepts, not arbitrary strings or untyped physical files. Patterns are not implicit specialization inheritance. Constraints are not repeated in every relation. Cardinality is evaluated over a source/Predicate set and missing constraints do not imply a restriction. Concept artifact IDs identify Concepts without transferring Entity classification ownership to Artifacts.
- **Correction appears necessary:** No for this model; references contract mismatch remains F44 and current Relation claim F58.
- **Dependencies:** RFC-0025/0027; ADR-0009/0014; predicate constraints.

### F60 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0029/content.md`.
- **Section / passage:** Terminology Predicate examples includes dependsOn; verification diagnostics “source artifact”, “target artifact”.
- **Semantic interpretation:** A migration predicate example and artifact-oriented diagnostics may be mistaken for canonical endpoint/type semantics.
- **Affected concept/layer:** Predicate / Relation / Entity / Artifact.
- **Classification:** AMBIGUITY.
- **Explanation:** dependsOn is unresolved by RFC-0028 and absent from RFC-0027 canonical vocabulary; inclusion as a “Predicate” example should not silently canonicalize it. Diagnostics may identify the representing Artifact alongside the semantic Entity, but the verifier wording does not specify that distinction. These are not explicit new allowed pairs.
- **Correction appears necessary:** Clarify migration example status and diagnostic owner when necessary.
- **Dependencies:** RFC-0028 dependsOn; RFC-0027 Predicate Identity; ADR-0013/0014; F49.

### F61 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0023/content.md`.
- **Section / passage:** Traceability; Versions/Baselines; Across Artifact Representations; Persistence/Git; Verification; Matrices.
- **Semantic interpretation:** Traceability is a capability over canonical relations and engineering state, not a parallel physical graph or matrix authority.
- **Affected concept/layer:** Relation / Predicate / Entity / Artifact / Version / Revision.
- **Classification:** CONSISTENT.
- **Explanation:** Source is stated as Entity owner and history is technical provenance. Version-specific relations and Baseline state are preserved. Verification must not rewrite knowledge. “RFC-0011 defines separation” is an indirect dependency (repository layout contains it); the general boundary is RFC-0015/ADR-0011, so the pointer is imprecise but not a semantic contradiction. Illustrative matrix issues are F29.
- **Correction appears necessary:** No for traceability architecture; dependency wording could be clarified.
- **Dependencies:** RFC-0025/0029; ADR-0006/0011; RFC-0012/0013/0015.

### F62 — CONSISTENT

- **File(s):** `foundation/specifications/rfc/RFC-0030/content.md`.
- **Section / passage:** Metadata; Identity; Domain Type; Logical/Physical distinction; Loader Boundary.
- **Semantic interpretation:** Canonical directory files serialize separate semantic owners; id may serve both identities in the normal case.
- **Affected concept/layer:** Entity / Artifact / Physical Representation / ontologyType / artifactType / Metadata / Identity.
- **Classification:** CONSISTENT.
- **Explanation:** Explicit ownership clauses align directly with the basis. Directory identity is physical discovery, not canonical engineering identity. Canonical Metadata may describe both represented Entities and the Artifact. Empty components do not force independent Entities. Additional/generated/exchange files do not automatically define semantics.
- **Correction appears necessary:** No for these clauses.
- **Dependencies:** ADR-0008/0010/0011/0013; RFC-0010/0015/0020/0025/0029.

### F63 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0030/content.md`.
- **Section / passage:** Relations: “relations of the Engineering Artifact”; relation mapping target-only values; Canonical Artifact Representation identity via artifact metadata.
- **Semantic interpretation:** Representation ownership and semantic relation source are not explicitly separated for multiple Entities per Artifact.
- **Affected concept/layer:** Relation / Identity / Entity / Artifact.
- **Classification:** AMBIGUITY.
- **Explanation:** In the normal one-to-one case explicit id and source context can work without a second ID. In a compound Artifact, a predicate-to-target mapping alone does not choose which Entity owns each relation or distinguish Artifact-originating relations. Metadata allows multiple Entity owners but supplies no concrete multi-Entity mapping here. This is a serialization underspecification, not a reason to forbid compound Artifacts.
- **Correction appears necessary:** Yes, clarify source/owner mapping and supported multi-Entity scope; no new IDs or serialization are introduced.
- **Dependencies:** ADR-0013 many-to-many; ADR-0014 source; RFC-0025 canonical source identity; RFC-0020 multi-Entity classification; F15/F49.

### F64 — AMBIGUITY

- **File(s):** `foundation/specifications/rfc/RFC-0030/content.md`.
- **Section / passage:** Relation Serialization and Empty Relation Collections: dependsOn/supersedes/supersededBy/relatedTo examples.
- **Semantic interpretation:** Canonical mapping profile uses named collections whose Predicate semantics may be unresolved or absent.
- **Affected concept/layer:** Relation / Predicate / serialization.
- **Classification:** AMBIGUITY.
- **Explanation:** dependsOn and relatedTo are explicitly unresolved migration predicates; supersedes/supersededBy are not defined in the current RFC-0027 catalogue or concrete definitions. Empty keys instantiate no relation, so are not evidence of a newly added Predicate. Nonempty dependsOn example may imply canonical semantic permission although the RFC says it only defines persistence and defers semantics. Distinguishing relation collection names from defined Predicate names remains underspecified.
- **Correction appears necessary:** Clarify representation examples versus adopted Predicate semantics; do not add predicates or rewrite collections.
- **Dependencies:** RFC-0028; RFC-0027; RFC-0025; RFC-0029 undefined predicate migration handling.

### F65 — CONTRADICTION

- **File(s):** `foundation/specifications/ax/AX-0004/content.md`; `foundation/specifications/ax/AX-0004/metadata.yaml`; `foundation/specifications/ax/AX-0005/content.md`; `foundation/specifications/ax/AX-0005/metadata.yaml`; `foundation/specifications/ax/AX-0006/content.md`; `foundation/specifications/ax/AX-0006/metadata.yaml`; `foundation/specifications/ax/AX-0007/content.md`; `foundation/specifications/ax/AX-0007/metadata.yaml`; `foundation/specifications/ax/AX-0008/content.md`; `foundation/specifications/ax/AX-0008/metadata.yaml`; `foundation/specifications/ax/AX-0009/content.md`; `foundation/specifications/ax/AX-0009/metadata.yaml`; `foundation/specifications/ax/AX-0010/content.md`; `foundation/specifications/ax/AX-0010/metadata.yaml`; `foundation/specifications/ontology/AX/content.md`; `foundation/specifications/ontology/AX/metadata.yaml`; `foundation/specifications/ontology/Constitution/content.md`; `foundation/specifications/ontology/Constitution/metadata.yaml`.
- **Section / passage:** Absent relations.yaml in AX-0004–0010 and ontology AX/Constitution directories.
- **Semantic interpretation:** Nine represented artifacts have metadata/content but lack the third canonical file.
- **Affected concept/layer:** Physical Representation / Relation serialization.
- **Classification:** CONTRADICTION.
- **Explanation:** RFC-0030 Required Components and Optional Relations require relations.yaml even with no relations; RFC-0000 only requires RFC files and is not the direct constraint here. This is a confirmed conditional current canonical-profile conformance conflict, not proof that semantic Entities lack relations or identity. Legacy migration may allow loading these directories, so it is not a conclusion that the logical model is invalid.
- **Correction appears necessary:** Correction would be needed if these representations claim completed RFC-0030 conformance; migration disposition/authority must be established first. No missing file is created by this task.
- **Dependencies:** RFC-0030 Required Components/Optional Relations/Migration; RFC-0011 Canonical Files; AX statuses Draft.

### F66 — HISTORICAL / NON-NORMATIVE

- **File(s):** `foundation/specifications/schemas/artifact.schema.yaml`; `foundation/specifications/schemas/entity.schema.yaml`; `foundation/specifications/schemas/metadata.schema.yaml`; `foundation/specifications/schemas/relation.schema.yaml`; `foundation/specifications/templates/adr-template.md`; `foundation/specifications/templates/entity-template.md`; `foundation/specifications/templates/rfc-template.md`.
- **Section / passage:** Four zero-byte schema files and three zero-byte template files.
- **Semantic interpretation:** Named schema/template representations exist without definitions, fields, constraints or examples.
- **Affected concept/layer:** Physical Representation / all reviewed owners.
- **Classification:** HISTORICAL / NON-NORMATIVE.
- **Explanation:** They cannot validate required ontologyType, semantic ownership, revision/version fields or multi-Entity mappings. RFC-0030 says schemas MAY be provided and treats them as implementation aids, so emptiness is not itself a confirmed contradiction of the semantic model. Templates contain no counterexample and no adopted new conventions.
- **Correction appears necessary:** No consistency correction; substantive specification work would be separate.
- **Dependencies:** RFC-0030 Schema; ADR-0007 scope; ENTITY-0001. No applicable local schema validation can establish semantic conformance.

### F67 — CONSISTENT

- **File(s):** `foundation/.gitignore`; `foundation/README.md`; `foundation/book/README.md`; `foundation/examples/README.md`; `foundation/reference-model/README.md`; `foundation/specifications/README.md`; `foundation/specifications/glossary/README.md`; `foundation/tooling/README.md`.
- **Section / passage:** Foundation/specifications/glossary descriptions; TODO reference areas; ignore patterns.
- **Semantic interpretation:** Foundation declares official self-hosted specifications; glossary declares stable terminology identities; other reference areas are placeholders.
- **Affected concept/layer:** Identity / Content / Physical Representation.
- **Classification:** CONSISTENT.
- **Explanation:** Foundation README and specifications README do not define Entities as files. Glossary README TERM-CanonicalTerm stable identity is not derived from its filename; a semantic identifier may be human-readable. .gitignore is technical configuration, not an ontology or model statement. Placeholder areas contain no applicable semantics (F68).
- **Correction appears necessary:** No.
- **Dependencies:** ADR-0001/0007; RFC-0002; ENTITY-0001; glossary model references.

### F68 — HISTORICAL / NON-NORMATIVE

- **File(s):** `foundation/book/README.md`; `foundation/examples/README.md`; `foundation/reference-model/README.md`; `foundation/tooling/README.md`.
- **Section / passage:** Headings and TODO only.
- **Semantic interpretation:** These areas promise future material without current examples/reference model/schema enforcement.
- **Affected concept/layer:** Content / examples / Physical Representation.
- **Classification:** HISTORICAL / NON-NORMATIVE.
- **Explanation:** There are no substantive examples below foundation/examples and no implemented reference-model material under its area. The review therefore covers in-document examples throughout RFC/ADR/AX instead of claiming nonexistent example artifacts were analyzed. No empty area can resolve ownership ambiguities.
- **Correction appears necessary:** No consistency rewrite; new material would be separate authorized work.
- **Dependencies:** Foundation README; ADR-0007; F29 in-document examples; F66 schemas/templates.

### F69 — CONSISTENT

- **File(s):** `foundation/specifications/ax/AX-0001/content.md`; `foundation/specifications/ax/AX-0002/content.md`; `foundation/specifications/ax/AX-0003/content.md`; `foundation/specifications/ax/AX-0004/content.md`; `foundation/specifications/ax/AX-0005/content.md`; `foundation/specifications/ax/AX-0006/content.md`; `foundation/specifications/ax/AX-0007/content.md`; `foundation/specifications/ax/AX-0008/content.md`; `foundation/specifications/ax/AX-0009/content.md`; `foundation/specifications/ax/AX-0010/content.md`.
- **Section / passage:** Charter/architecture; knowledge-first; information/navigation; visual/interaction; multiple representations; AI/trust.
- **Semantic interpretation:** AX presents the same knowledge across interfaces; concepts/graph take precedence over physical directories, generated diagrams are not source authority.
- **Affected concept/layer:** Entity / Artifact / Physical Representation / Content / Relation.
- **Classification:** CONSISTENT.
- **Explanation:** AX-0001 separates UX from storage/content/rendering logic. AX-0002 human/AI equality supports shared semantic knowledge. AX-0003/0004 distinguish conceptual navigation from directory paths. AX-0005/0006 are presentation/interaction requirements. AX-0007 explicitly says changing representation must not change meaning and generated diagrams must not become independent truth. AX-0008 searches knowledge instead of filenames. AX-0009 provenance and user control govern persistent changes; the user explicitly authorized this report and commit. AX-0010 preserves unknown information and provenance. None requires files to become Entities.
- **Correction appears necessary:** No for these UX principles. F70 covers ambiguous labels/history.
- **Dependencies:** RFC-0014/0015/0021/0024; ADR-0018; Constitution semantic independence.

### F70 — AMBIGUITY

- **File(s):** `foundation/specifications/ax/AX-0002/content.md`; `foundation/specifications/ax/AX-0003/content.md`; `foundation/specifications/ax/AX-0004/content.md`; `foundation/specifications/ax/AX-0005/content.md`; `foundation/specifications/ax/AX-0007/content.md`; `foundation/specifications/ax/AX-0008/content.md`; `foundation/specifications/ax/AX-0009/content.md`; `foundation/specifications/ax/AX-0010/content.md`.
- **Section / passage:** Artifact context/navigation/scalability; Search Results “artifact type”; Trust Provenance and Version History.
- **Semantic interpretation:** UX labels use Artifact for addressable knowledge and history without distinguishing Entity semantic type or Artifact/technical history.
- **Affected concept/layer:** Artifact / Entity / artifactType / ontologyType / Metadata / Version / Revision.
- **Classification:** AMBIGUITY.
- **Explanation:** Artifact context and relationships can be compatible presentation shorthand. A search result’s artifact type may mean artifactType or ontologyType of its Entity, with different owners. Titles and relationships may describe represented knowledge. Trust creation/modification history may describe engineering events or technical provenance; “Version History” does not separate Engineering Versions, Artifact Revisions and Git history. No explicit Git=Version rule appears, so these are ambiguities, not confirmed contradictions. AI-generated authored knowledge in AX-0009 is not the same as a derived non-authoritative rendering in AX-0007.
- **Correction appears necessary:** Clarify semantic referents in product labels/provenance when implemented; no AX file is changed.
- **Dependencies:** ADR-0010/0012/0013; RFC-0010/0012/0014/0021; F53 metadata.

### F71 — HISTORICAL / NON-NORMATIVE

- **File(s):** `foundation/specifications/rfc/RFC-0021/content.md`; `foundation/specifications/rfc/RFC-0022/content.md`.
- **Section / passage:** Physical endings: Deterministic Views sentence; Consequences Positive ending “Alternative”.
- **Semantic interpretation:** Current RFC drafts are incomplete at their endings.
- **Affected concept/layer:** Content / specification completeness.
- **Classification:** HISTORICAL / NON-NORMATIVE.
- **Explanation:** RFC-0021 ends after one Deterministic Views sentence; RFC-0022 ends mid-bullet. Neither contains a completed acceptance/migration section beyond that point. This is a current completeness limitation, not evidence of semantic content that is absent or an instruction to complete the drafts during this task.
- **Correction appears necessary:** No consistency-only correction; completing drafts is separate Foundation work.
- **Dependencies:** RFC-0000 required sections; Draft metadata; F40 specialization ambiguity.

### F72 — HISTORICAL / NON-NORMATIVE

- **File(s):** `foundation/specifications/adr/ADR-0001/content.md`; `foundation/specifications/adr/ADR-0002/content.md`; `foundation/specifications/adr/ADR-0003/content.md`; `foundation/specifications/adr/ADR-0004/content.md`; `foundation/specifications/adr/ADR-0005/content.md`; `foundation/specifications/adr/ADR-0006/content.md`; `foundation/specifications/adr/ADR-0007/content.md`; `foundation/specifications/adr/ADR-0008/content.md`; `foundation/specifications/adr/ADR-0009/content.md`; `foundation/specifications/adr/ADR-0010/content.md`; `foundation/specifications/adr/ADR-0011/content.md`; `foundation/specifications/adr/ADR-0012/content.md`; `foundation/specifications/adr/ADR-0013/content.md`; `foundation/specifications/adr/ADR-0014/content.md`; `foundation/specifications/adr/ADR-0015/content.md`; `foundation/specifications/adr/ADR-0016/content.md`; `foundation/specifications/adr/ADR-0017/content.md`; `foundation/specifications/adr/ADR-0018/content.md`; `foundation/specifications/rfc/RFC-0000/content.md`; `foundation/specifications/rfc/RFC-0001/content.md`; `foundation/specifications/rfc/RFC-0002/content.md`; `foundation/specifications/rfc/RFC-0003/content.md`; `foundation/specifications/rfc/RFC-0004/content.md`; `foundation/specifications/rfc/RFC-0005/content.md`; `foundation/specifications/rfc/RFC-0010/content.md`; `foundation/specifications/rfc/RFC-0011/content.md`; `foundation/specifications/rfc/RFC-0012/content.md`; `foundation/specifications/rfc/RFC-0013/content.md`; `foundation/specifications/rfc/RFC-0014/content.md`; `foundation/specifications/rfc/RFC-0015/content.md`; `foundation/specifications/rfc/RFC-0020/content.md`; `foundation/specifications/rfc/RFC-0021/content.md`; `foundation/specifications/rfc/RFC-0022/content.md`; `foundation/specifications/rfc/RFC-0023/content.md`; `foundation/specifications/rfc/RFC-0024/content.md`; `foundation/specifications/rfc/RFC-0025/content.md`; `foundation/specifications/rfc/RFC-0026/content.md`; `foundation/specifications/rfc/RFC-0027/content.md`; `foundation/specifications/rfc/RFC-0028/content.md`; `foundation/specifications/rfc/RFC-0029/content.md`; `foundation/specifications/rfc/RFC-0030/content.md`; `foundation/specifications/rfc/RFC-0031/content.md`.
- **Section / passage:** Context, Motivation, Alternatives Considered, Migration and Open Questions throughout.
- **Semantic interpretation:** Earlier concerns, hypothetical migrations, rejected file-centric models and future questions are not current adopted semantic rules.
- **Affected concept/layer:** All layers / history / authority.
- **Classification:** HISTORICAL / NON-NORMATIVE.
- **Explanation:** Rejected alternatives such as files=Entities, all Artifacts=Entities, paths=identity, commits=Versions, Git tags=Baselines are not contradictions merely because their words occur in the repository. Migration candidate inference from paths is provisional evidence, not canonical ontology inference. Future concept/type/identifier questions are not additions. Preserve historical analysis unless an operative rule is explicitly identified separately in this report.
- **Correction appears necessary:** No automatic consistency rewrite of historical/non-normative passages.
- **Dependencies:** Current operative passages are reviewed individually above; RFC-0028 explicitly preserves uncertainty and requires semantic decisions.

## Classification summary and dependency boundaries

There are 72 review records. These are passage-level records, not counts of distinct defective artifacts; some shared issues apply to many files, and several files have both consistent and ambiguous passages.

| Classification | Records |
| --- | ---: |
| CONTRADICTION | 8 |
| AMBIGUITY | 22 |
| CONSISTENT | 36 |
| HISTORICAL / NON-NORMATIVE | 6 |

Confirmed semantic conflicts require architectural reconciliation rather than editorial normalization: F05 metadata scope; F23 Entity typing; F35 semantic objects defined as Artifacts; F44 references contract; F45 concrete versus catalogue pairs; F52 explicit lifecycle state conflicts; F58 canonical Relation source contract. F65 is separately a conditional physical-profile conformance conflict. None is resolved in this report.

The following dependencies need decisions or explicit interpretation before future corrections can safely proceed:

1. Clarify the addressable Artifact layer and definition/instance relationship before changing object definitions or relation endpoint typing (F14, F35–F40, F48–F49).
2. Establish authoritative Predicate contracts before judging all persisted references and AX refinements against a single current allowed-pair set (F44–F46, F50). Pattern support alone does not resolve semantic authority.
3. Establish relation semantic source mapping before extending three-file serialization to multi-Entity Artifacts (F15, F49, F58, F63).
4. Establish property owner, metadata authority and version/event meanings before interpreting `type`, `entityType`, `status`, `version`, `created` or `updated` as normative state (F27, F34, F47–F55).
5. Preserve legacy relation uncertainty and external resolution boundaries; empty collections, historical examples and migration observations do not adopt new Predicates or Entities (F50, F56–F60, F64, F72).

No rule here requires a second Artifact ID merely to distinguish meanings. No claim is made that absent optional `artifactType` alone is a violation. No file/directory move, timestamp, schema placeholder or Git commit is treated as semantic identity or version evidence without an explicit mapping.

## Validation evidence and preservation protocol

During analysis, the existing read-only Foundation verifier loaded 85 artifacts and returned `ok=True`, with 50 `unresolved-relation-predicate` warnings and no errors. The existing renderer test suite passed all 15 tests. These checks are narrower than this review: wildcard references are accepted by the current verifier, empty schemas are not semantic validators, and narrative ownership/state contradictions are not all checked. No claim of comprehensive semantic conformance follows from the successful checks.

Applicable checks after creating this report are the same read-only verifier and existing tests, plus `git diff --check`, exact source-hash comparison and changed-file verification. The full CI renderer writes generated documentation; executing it directly would change existing repository files. The practical validation chosen here verifies its existing loading/verification logic and tests without rendering output into this workspace. A documentation site build does not interpret this analysis report under Foundation and is not required to establish that the only repository addition is this report.

The report is created once from the complete analysis; it is not subsequently rewritten, normalized, summarized or corrected. Post-creation validation, commit and push results are reported in the task completion response rather than appended to this immutable original analysis. The reviewed commit remains the review anchor, even after the report commit becomes branch HEAD. Foundation byte hashes in the inventory permit exact comparison with that anchor.

## File-by-file scope inventory

Every existing Foundation file is listed below. `References` connects the file to the detailed records, each of which contains section, interpretation, affected layer, classification, explanation, correction assessment and dependencies. A file can have multiple classifications because its passages have different roles. File facts are descriptive observations, not implicit new semantics. Metadata entries list physical fields exactly as encountered; no semantic aliases are invented. Relation entries list serialized collection keys/targets, including unresolved and empty ones. Content headings locate the reviewed subject. SHA-256 hashes bind the inventory to the source bytes.

### `foundation/.gitignore`

- Source: 26 bytes; SHA-256 `e9ded537ce2dcc1669b5155b173216296cda59391089e85bf6daae111f18c85d`.
- Review records: F67.
- Inspected passage/physical facts: .DS_Store / .idea/ / .vscode/

### `foundation/README.md`

- Source: 154 bytes; SHA-256 `8d55684a34cb1ef8800f8ed3c96636caef229088896d8dc843a46970d87f888c`.
- Review records: F67.
- Inspected passage/physical facts: # ATON Foundation /  / ATON Foundation contains the official specifications, / ontology, schemas and reference model of ATON. /  / This repository is self-hosting.

### `foundation/book/README.md`

- Source: 13 bytes; SHA-256 `8f72a360802cec2d12c288917ec97476a2ab584517a4fa5d788dcfd9d7d2b3b6`.
- Review records: F67, F68.
- Inspected passage/physical facts: # book /  / TODO

### `foundation/constitution/CONSTITUTION/content.md`

- Source: 6792 bytes; SHA-256 `e0d18383b08457187dddd25a6bf0bd27d500fe3d08dddf003e1dd49141947fd5`.
- Review records: F01.
- Inspected passage/physical facts: ATON Constitution; Preamble; Article I — Purpose; Section 1 — Mission; Section 2 — Objectives; Section 3 — Independence; Article II — Scope; Section 1 — The Foundation; Section 2 — Responsibilities; Section 3 — Boundaries; Section 4 — Extensibility; Article III — Principles; Principle 1 — Semantic Foundation; Principle 2 — Explicit Relationships; Principle 3 — Engineering Evolution; Principle 4 — Task-Driven Engineering; Principle 5 — Traceability; Principle 6 — Process Independence; Principle 7 — Technology Independence; Principle 8 — Extensibility; Principle 9 — Open Governance; Principle 10 — Long-Term Stability; Article IV — Architecture; Section 1 — Architectural Foundation; Section 2 — Layered Architecture; Section 3 — Separation of Concerns; Section 4 — Engineering Kernel; Article V — Governance; Section 1 — Evolution; Section 2 — Engineering Governance; Section 3 — Stewardship; Section 4 — Transparency; Article VI — Evolution and Amendment; Section 1 — Evolution; Section 2 — Amendments; Section 3 — Continuity

### `foundation/constitution/CONSTITUTION/metadata.yaml`

- Source: 365 bytes; SHA-256 `88ca22a3b153076f29609e02e798c41a744978674d2daa9858583f53cbf2f2b9`.
- Review records: F51, F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: CONSTITUTION; title: ATON Constitution; type: constitution; status: accepted; version: 1.0.0; authors:; created: 2026-08-03; updated: 2026-08-03; tags:; parents: []; children: []; references: []; related:; ontologyType: ONT-Constitution

### `foundation/constitution/CONSTITUTION/relations.yaml`

- Source: 24 bytes; SHA-256 `60cc5e0ff3cda0118fc4cb19904817823a01a6b0a8b59640a77909f73dbfa0ae`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: governs: /   - foundation

### `foundation/examples/README.md`

- Source: 17 bytes; SHA-256 `e231cd75b0f0ad02cf62ae49948adc0c5fa3ad6fc43756aa741c96a8fa278053`.
- Review records: F67, F68.
- Inspected passage/physical facts: # examples /  / TODO

### `foundation/reference-model/README.md`

- Source: 24 bytes; SHA-256 `536876826b66baae6ff9d691ad5437c54e3a4a38ff17802f6fa6891eafe2fe4e`.
- Review records: F67, F68.
- Inspected passage/physical facts: # reference-model /  / TODO

### `foundation/specifications/README.md`

- Source: 108 bytes; SHA-256 `fb59599201bd82c8c8844a84aca48dee3acb98f68fa00caf33c7f2d191d42289`.
- Review records: F67.
- Inspected passage/physical facts: # Specification /  / Official specifications of ATON. /  / Contains: /  / - ADRs / - RFCs / - Ontology / - Schemas / - Glossary

### `foundation/specifications/adr/ADR-0001/content.md`

- Source: 1305 bytes; SHA-256 `2de625809c89c4ab2e8326b3729142bf2857384cafe45234a200c54b4b885b77`.
- Review records: F02, F72.
- Inspected passage/physical facts: ADR-0001 — Self-Hosting Foundation; Status; Context; Decision; Consequences; Rationale; Alternatives Considered; External Documentation; Architectural Principle

### `foundation/specifications/adr/ADR-0001/metadata.yaml`

- Source: 239 bytes; SHA-256 `b92ce2c1c49e24f2bc6e98fc35c98aef7f13347a7ad23fbdae40e764bc2cd3bc`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0001; title: Self-Hosting Foundation; type: architecture-decision; status: accepted; version: 2.0.0; authors:; created: 2026-07-28; updated: 2026-07-28; tags:; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0001/relations.yaml`

- Source: 65 bytes; SHA-256 `466160875df523b81a6df090531124a74a24ea594215bb71609747064ec5a51e`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: parents: [] /  / children: /   - ADR-0002 /  / references: [] /  / related: []

### `foundation/specifications/adr/ADR-0002/content.md`

- Source: 2637 bytes; SHA-256 `66b0617e468587b5c4d6071433669175c29b24dc134867f41b15f9e5229ba5a5`.
- Review records: F03, F72.
- Inspected passage/physical facts: ADR-0002 — Markdown as the Canonical Authoring Format; Status; Context; Decision; Consequences; Rationale; Alternatives Considered; HTML; XML; Rich Text Editors; Architectural Principle

### `foundation/specifications/adr/ADR-0002/metadata.yaml`

- Source: 266 bytes; SHA-256 `ea3a3af6e96dd24da615b7a1c703b1fef199ce20556a8cd836e809d3ac532a8c`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0002; title: Markdown as the Canonical Authoring Format; type: architecture-decision; status: accepted; version: 1.0.0; authors:; created: 2026-07-28; updated: 2026-07-28; tags:; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0002/relations.yaml`

- Source: 78 bytes; SHA-256 `cf85dc1d013b1ac7eefe1d03515989a2f21d86050cfc18e68c6c5cbb8830ecc9`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: parents: [] /  / children: [] /  / references: [] /  / related: /   - ADR-0003 /   - ADR-0005

### `foundation/specifications/adr/ADR-0003/content.md`

- Source: 1962 bytes; SHA-256 `b23259fe30476158a2d6352ded4c05537b1d4f716676cfc7803cfd822a577c27`.
- Review records: F03, F72.
- Inspected passage/physical facts: ADR-0003 — Git as the Version Control System; Status; Context; Decision; Consequences; Rationale; Alternatives Considered; Centralized Version Control Systems; Database-only Storage; Proprietary Version Control Systems; Architectural Principle

### `foundation/specifications/adr/ADR-0003/metadata.yaml`

- Source: 258 bytes; SHA-256 `cde6d868f5c4e6f7ece6e99b75cb495883dcbfdf5d1ca252186974d995c343ee`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0003; title: Git as the Version Control System; type: architecture-decision; status: accepted; version: 1.0.0; authors:; created: 2026-07-28; updated: 2026-07-28; tags:; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0003/relations.yaml`

- Source: 78 bytes; SHA-256 `86286743d549fe1da689f9d5d338244f8677e864f591e56b32dab5a21a33d40b`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: parents: [] /  / children: [] /  / references: [] /  / related: /   - ADR-0002 /   - ADR-0006

### `foundation/specifications/adr/ADR-0004/content.md`

- Source: 2959 bytes; SHA-256 `baba515b8c11ff034862a529cd4759e2cd841c7596749eaf87f333f1c62ca9e4`.
- Review records: F04, F72.
- Inspected passage/physical facts: ADR-0004 — Artifact-Based Knowledge Organization; Status; Context; Decision; Consequences; Rationale; Alternatives Considered; Document-Centric Organization; File-Centric Organization; Database Records; Architectural Principle

### `foundation/specifications/adr/ADR-0004/metadata.yaml`

- Source: 273 bytes; SHA-256 `cb4d4fcf6ecc147ff0c01d62dcdcee08b9b8df090b6af5cf9ef3896d7f3e8825`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0004; title: Artifact-Based Knowledge Organization; type: architecture-decision; status: accepted; version: 1.0.0; authors:; created: 2026-07-28; updated: 2026-07-28; tags:; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0004/relations.yaml`

- Source: 78 bytes; SHA-256 `776098bb8f2137d221db04753d954b29e18ef70743209748773e45c7357e84b5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: parents: [] /  / children: [] /  / references: [] /  / related: /   - ADR-0005 /   - ADR-0006

### `foundation/specifications/adr/ADR-0005/content.md`

- Source: 2134 bytes; SHA-256 `27ee0f8685e0bd07ee061ef3a0eff63b9a8df1c93cce01ecbd17b8509fde584e`.
- Review records: F05, F06, F72.
- Inspected passage/physical facts: ADR-0005 — Separation of Content, Metadata and Relations; Status; Context; Decision; Consequences; Rationale; Alternatives Considered; Single Document Structure; Embedded Metadata; Implicit Relationships; Architectural Principle

### `foundation/specifications/adr/ADR-0005/metadata.yaml`

- Source: 280 bytes; SHA-256 `c896d00cf39601bfa4725bfd875a6dc9b9270d296c28f19f7a1556647575ebf9`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0005; title: Separation of Content, Metadata and Relations; type: architecture-decision; status: accepted; version: 1.0.0; authors:; created: 2026-07-28; updated: 2026-07-28; tags:; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0005/relations.yaml`

- Source: 78 bytes; SHA-256 `ef3ef43016047c097d42441095af19825d8adfc9f2b52de04f4d5341a0aad098`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: parents: [] /  / children: [] /  / references: [] /  / related: /   - ADR-0004 /   - ADR-0006

### `foundation/specifications/adr/ADR-0006/content.md`

- Source: 2378 bytes; SHA-256 `4e5fe42e6e46fdeef34a59673772694eef003f5f828c59496dbd94997e0621ae`.
- Review records: F07, F72.
- Inspected passage/physical facts: ADR-0006 — Engineering Knowledge Graph; Status; Context; Decision; Consequences; Rationale; Alternatives Considered; Hierarchical Structures; Folder-Based Organization; Relational Database Models; Architectural Principle

### `foundation/specifications/adr/ADR-0006/metadata.yaml`

- Source: 275 bytes; SHA-256 `dd473feb60625ce60a103bc219fee473fedfb69a5ce55edd554105b0608dd429`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0006; title: Engineering Knowledge Graph; type: architecture-decision; status: accepted; version: 1.0.0; authors:; created: 2026-07-28; updated: 2026-07-28; tags:; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0006/relations.yaml`

- Source: 14 bytes; SHA-256 `c03b8bc4aa3ad13877bb34b5aee4bfaeeaeb664b2718c6ddefe017fee7de98ba`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: relations: []

### `foundation/specifications/adr/ADR-0007/content.md`

- Source: 2991 bytes; SHA-256 `8d963bf9b9be460ae484135a671401e19ca5d4d082c6939e54033123680ba088`.
- Review records: F03, F72.
- Inspected passage/physical facts: ADR-0007 — Foundation as the Normative Engineering Knowledge Base; Status; Context; Decision; Consequences; Rationale; Alternatives Considered; Foundation as Project Documentation; Foundation Embedded in the Source Code; Independent Standard Outside ATON; Architectural Principle

### `foundation/specifications/adr/ADR-0007/metadata.yaml`

- Source: 304 bytes; SHA-256 `31ab1f70a4df2f8afee06542a4f292334a549c77886f4e932608507972ffd1f8`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0007; title: Foundation as the Normative Engineering Knowledge Base; type: architecture-decision; status: accepted; version: 1.0.0; authors:; created: 2026-07-28; updated: 2026-07-28; tags:; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0007/relations.yaml`

- Source: 55 bytes; SHA-256 `c64c23b8b2517b3f38b0c5d27b316f86ddd4d1ce8a7c233c61b7f0e70def1ac6`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: parents: [] /  / children: [] /  / references: [] /  / related: []

### `foundation/specifications/adr/ADR-0008/content.md`

- Source: 3293 bytes; SHA-256 `bfe947ada5d2ce49c76c25ee85e3f72d1112a6b908e035669b8deb844b73cef0`.
- Review records: F08, F52, F72.
- Inspected passage/physical facts: ADR-0008 Canonical Domain Models; Status; Context; Decision; Rationale; Consequences; Initial Application; Explicit Ontology Type Identity; Alternatives Considered; Preserve multiple internal representations; Normalize inside each subsystem; References

### `foundation/specifications/adr/ADR-0008/metadata.yaml`

- Source: 95 bytes; SHA-256 `27b802149df4c3698574c37843ac56810c1f678b6af32779978f74893fbc6097`.
- Review records: F52, F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0008; title: Canonical Domain Models; status: Draft; version: 1.1.0; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0008/relations.yaml`

- Source: 66 bytes; SHA-256 `cf37a4930ec41ac51029860cc419c898fa7531bce5059d89628fbf65bfc17612`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: parents: [] /  / children: [] /  / references: /   - NOTE-0020 /  / related: []

### `foundation/specifications/adr/ADR-0009/content.md`

- Source: 6313 bytes; SHA-256 `0e355162a3a9172ad655300abf5a079d879e64a91321cdec8364b00acdea8dc8`.
- Review records: F09, F10, F72.
- Inspected passage/physical facts: ADR-0009 Semantic Constraints for Relations; Status; Context; Decision; Architectural Separation; Relation Model; Ontology; Verification; RFC; Source and Target Semantics; Invalid Relations; Consequences; Positive; Negative; Migration; Alternatives Considered; Constraints inside the Relation object; Constraints only in application code; Predicate name without domain and range; Decision Boundary; References

### `foundation/specifications/adr/ADR-0009/metadata.yaml`

- Source: 94 bytes; SHA-256 `4934697d884625ec5c88b7ff005558049d005860c6b737db268669b162715385`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0009; title: Semantic Constraints for Relations; status: Accepted; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0009/relations.yaml`

- Source: 119 bytes; SHA-256 `8cf5f16943ed8913ba739055b72bfabef92b1627406317537f8cc0874bf4fb37`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - NOTE-0021 /   - RFC-0025 /   - ENTITY-0001 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/adr/ADR-0010/content.md`

- Source: 9027 bytes; SHA-256 `b7d0799188bab744703648ab36403fa63f4c6c8b5c130f1079b39469c0fe5a74`.
- Review records: F11, F72.
- Inspected passage/physical facts: Canonical Metadata Domain Model; Context; Problem Statement; Decision; Canonical Metadata; Explicit Representation; Derived Information; Materialization; Temporal Information; Metadata Authority; Persistence Independence; Metadata and Physical Representation; Metadata Ownership; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Derive canonical metadata from persistence; Treat all persisted metadata as authoritative; Allow implementations to choose which metadata is canonical; Store both explicit and derived values as equally authoritative; Expected Outcome

### `foundation/specifications/adr/ADR-0010/metadata.yaml`

- Source: 103 bytes; SHA-256 `1d30022ae5c09dbcb96e7f5540a8523ee00febb22af0af968b26445a153214ab`.
- Review records: F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0010; title: Canonical Metadata Domain Model; status: Draft; version: 0.2.0; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0010/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0011/content.md`

- Source: 5778 bytes; SHA-256 `bffc1cdafebafb0a494a85e48eb88de3b85d7c58a3f68d4ec3d50403b299a4bb`.
- Review records: F12, F72.
- Inspected passage/physical facts: Logical Engineering Knowledge Model and Physical Representations; Context; Problem Statement; Decision; Representation Boundary; Logical Engineering Knowledge; Physical Representations; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Treat the repository structure as the domain model; Allow kernel components to interpret persistence formats directly; Define a separate domain model for every representation; Expected Outcome

### `foundation/specifications/adr/ADR-0011/metadata.yaml`

- Source: 124 bytes; SHA-256 `7843da8d93b75a6f44eb39da2b479e2d0bdf1d7847336951108ad54218165cd6`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0011; title: Logical Engineering Knowledge Model and Physical Representations; status: Proposed; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0011/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0012/content.md`

- Source: 8385 bytes; SHA-256 `743d0e6366420dc7de9445acf3185640296c9f6c4b06a50f25b483b1091a822a`.
- Review records: F13, F54, F72.
- Inspected passage/physical facts: Engineering Version and Baseline Semantics; Context; Problem Statement; Decision; Engineering Identity; Engineering Version; Artifact Revision; Git Revisions; Baselines; Releases; Immutability; Temporal Information; Traceability; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Treat Git revisions as engineering versions; Treat Git tags as releases; Treat baselines as Git commits; Use timestamps to identify versions; Expected Outcome

### `foundation/specifications/adr/ADR-0012/metadata.yaml`

- Source: 102 bytes; SHA-256 `66cb068c2b25ceb18f72081fdd90a366a85c520642996cfeb9a0cd34ea586646`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0012; title: Engineering Version and Baseline Semantics; status: Proposed; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0012/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0013/content.md`

- Source: 8125 bytes; SHA-256 `c9102d5e821fb7bc2aef38ab331c089e7ae1e2217f7bd5ee58b6cfa33c320bf0`.
- Review records: F13, F14, F72.
- Inspected passage/physical facts: Entity and Artifact Semantics; Context; Problem Statement; Decision; Engineering Entity; Engineering Artifact; Entity-to-Artifact Relationship; Artifact Components; Identity; Persistence Independence; Versioning; Traceability; Derived Representations; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Treat every artifact as an engineering entity; Treat entities as purely derived from artifacts; Require exactly one artifact per entity; Expected Outcome

### `foundation/specifications/adr/ADR-0013/metadata.yaml`

- Source: 101 bytes; SHA-256 `9c2cd14538bf95d99efed6b223944b810b01b83af9d386fdd8f9df3119493b2a`.
- Review records: F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0013; title: Entity and Artifact Semantics; status: Draft; version: 0.2.0; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0013/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0014/content.md`

- Source: 8810 bytes; SHA-256 `216f730f47fc31a9a31f4a15530847a617b348db418e38c217b2cdbf90b86b68`.
- Review records: F15, F16, F49, F72.
- Inspected passage/physical facts: Canonical Semantic Relation Model; Context; Problem Statement; Decision; Predicate Semantics; Semantic Validation; Canonical Predicate Constraints; Relation Direction; Relation Identity; Relation Persistence; External Targets; Legacy Predicates; Kernel Boundaries; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Treat relations as persistence structures; Validate only predicate existence; Infer semantic types from repository structure; Allow every Predicate for every source and target; Expected Outcome

### `foundation/specifications/adr/ADR-0014/metadata.yaml`

- Source: 105 bytes; SHA-256 `50a17ba6c674b4cf5c6a9aad5be61a4e662108a67cb15df5cecc9d0aa59f08e1`.
- Review records: F53, F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0014; title: Canonical Semantic Relation Model; status: Draft; version: 0.2.0; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0014/relations.yaml`

- Source: 85 bytes; SHA-256 `ec1c1e736833e57f738a0159ffc822ff7b22f8eeb8033a2e9a6334ba92ea6678`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0029 / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0015/content.md`

- Source: 7256 bytes; SHA-256 `29562768ee32ac07dc37e4bdd536f499381dab5ebfc074d4b1d13f9a5cb905e2`.
- Review records: F17, F72.
- Inspected passage/physical facts: Embedded and Contextual Engineering Entities; Context; Problem Statement; Decision; Contextual Identity; Context Relationship; Artifact Representation; Traceability; Versioning; Lifecycle; Findings and Reviews; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Model contextual concepts only as embedded artifacts; Make every contextual concept globally independent; Infer context from repository structure; Expected Outcome

### `foundation/specifications/adr/ADR-0015/metadata.yaml`

- Source: 104 bytes; SHA-256 `50bba086fc813975f3f2aa2ee4b088855c7da2f66e360ccbdef75b9cabf54bfe`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0015; title: Embedded and Contextual Engineering Entities; status: Proposed; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0015/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0016/content.md`

- Source: 9270 bytes; SHA-256 `96f274a07c967abe2d08c8a8d7c96d1c787d01f358ac881472fc250e2e530f4b`.
- Review records: F18, F72.
- Inspected passage/physical facts: Engineering Process Model; Context; Problem Statement; Decision; Process; Activity; Process State; Transitions; Roles and Responsibilities; Inputs and Outputs; Process Constraints; Verification; Process Execution and Tracking; Process Definition and Process Instance; Process Independence; Engineering Knowledge Integration; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Define a mandatory ATON development process; Define a mandatory review process; Provide only workflow execution; Leave process semantics entirely to implementations; Expected Outcome

### `foundation/specifications/adr/ADR-0016/metadata.yaml`

- Source: 85 bytes; SHA-256 `2206659642b41be4cef7ebf5d03d3ac42f9b3cc39591a48d27906a5eca01b157`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0016; title: Engineering Process Model; status: Proposed; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0016/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0017/content.md`

- Source: 8547 bytes; SHA-256 `7ac5df900bb29b3415534a5fa57d65c5f7f5dcd92bcd98ca094e2a4698f02906`.
- Review records: F19, F54, F72.
- Inspected passage/physical facts: Architecture Decision Lifecycle; Context; Problem Statement; Decision; Proposed; Accepted; Superseded; Rejected; Withdrawn; Lifecycle Transitions; Versioning; Process Independence; Governance; Traceability; Verification; Historical Preservation; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Derive ADR state from Git branches; Derive acceptance from review completion; Allow arbitrary lifecycle states without Foundation semantics; Delete decisions when they are no longer current; Expected Outcome

### `foundation/specifications/adr/ADR-0017/metadata.yaml`

- Source: 91 bytes; SHA-256 `5c77499450bb5558f6e817d0fa73275d5207470ed54c0fb6d48ec22e819d4fbd`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0017; title: Architecture Decision Lifecycle; status: Proposed; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0017/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/adr/ADR-0018/content.md`

- Source: 9918 bytes; SHA-256 `89a6ba1f56a08d90f057afb4699e0f1b2ce94d6bb8a929aa465b92d1fafe9c2e`.
- Review records: F20, F72.
- Inspected passage/physical facts: Engineering Knowledge Navigation; Context; Problem Statement; Decision; Navigation Target; Navigation Path; Relation-Based Navigation; Direction and Inverse Navigation; Navigation Views; Filtering; Traceability Navigation; Impact Navigation; Historical Navigation; External Navigation; Navigation and Persistence; Navigation and User Interfaces; Search and Navigation; Verification; Consequences; Positive; Negative; Relationship to Other Decisions; Alternatives Considered; Use repository structure as the navigation model; Use document hierarchy as the canonical navigation model; Define navigation through a specific user interface; Treat search and navigation as the same capability; Expected Outcome

### `foundation/specifications/adr/ADR-0018/metadata.yaml`

- Source: 92 bytes; SHA-256 `3b4408341fa4171d657b6af3c8b26c02ea908357ba3b2fcf2712202ddabdf0a6`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: ADR-0018; title: Engineering Knowledge Navigation; status: Proposed; ontologyType: ONT-ADR

### `foundation/specifications/adr/ADR-0018/relations.yaml`

- Source: 75 bytes; SHA-256 `9a0532acee0d8611c51a3dffabd087d5f503cd685618ebf99d67f1ea89ec21c5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/ax/AX-0001/content.md`

- Source: 1031 bytes; SHA-256 `fe71f5bd5d34a58a661d00c224d2400d425b5291e8a6029ee1eba51c416641c6`.
- Review records: F69.
- Inspected passage/physical facts: AX-0001 — AX Charter; Purpose; Mission; Vision; Core Principle; Goals; Non Goals; Architecture Position

### `foundation/specifications/ax/AX-0001/metadata.yaml`

- Source: 153 bytes; SHA-256 `0eef9af4f5fd6584c26b733e47a3ec13288d3005833ae57bbc188825496f8992`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0001; title: AX Charter; type: ax; status: draft; version: 0.1.0; authors:; created: 2026-07-26; updated: 2026-07-26; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0001/relations.yaml`

- Source: 14 bytes; SHA-256 `c03b8bc4aa3ad13877bb34b5aee4bfaeeaeb664b2718c6ddefe017fee7de98ba`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: relations: []

### `foundation/specifications/ax/AX-0002/content.md`

- Source: 1371 bytes; SHA-256 `2e01876d58975c8539057ed187dfc0507cb4638c46a181a228133053c1b9b941`.
- Review records: F69, F70.
- Inspected passage/physical facts: AX-0002 — Design Principles; Purpose; Principle 1 — Clarity First; Principle 2 — Knowledge First; Principle 3 — Progressive Disclosure; Principle 4 — Consistency; Principle 5 — Graph Native; Principle 6 — Context Everywhere; Principle 7 — Accessibility; Principle 8 — AI and Human Equality

### `foundation/specifications/ax/AX-0002/metadata.yaml`

- Source: 160 bytes; SHA-256 `77572b7ee30e4efe9d04918ddc3097dc61c014f3f9aee8097283615fa682c357`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0002; title: Design Principles; type: ax; status: draft; version: 0.1.0; authors:; created: 2026-07-26; updated: 2026-07-26; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0002/relations.yaml`

- Source: 49 bytes; SHA-256 `4e0bde7f490983aac81db9e26281813f55bdc6a8f8f4c6601356074cf61c17b2`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: relations: /   - type: refines /     target: AX-0001

### `foundation/specifications/ax/AX-0003/content.md`

- Source: 1506 bytes; SHA-256 `ae2921d3b131e26a11ad6752040eb2db82036e1e89bb4c591aea4870340ecc3b`.
- Review records: F69, F70.
- Inspected passage/physical facts: AX-0003 — Information Architecture; Purpose; Design Goals; Navigation Principles; Top-Level Structure; Specification Structure; Cross Navigation; Search; Scalability

### `foundation/specifications/ax/AX-0003/metadata.yaml`

- Source: 167 bytes; SHA-256 `63ef32c121398abdb79dd11a45be2fb87cfad4a175037fc3f06fd2bce9bd39bc`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0003; title: Information Architecture; type: ax; status: draft; version: 0.1.0; authors:; created: 2026-07-26; updated: 2026-07-26; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0003/relations.yaml`

- Source: 49 bytes; SHA-256 `81ff43184425892cb3767be6219f454e28a4a30deb40e50b066dfcbde6a4f4fb`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: relations: /   - type: refines /     target: AX-0002

### `foundation/specifications/ax/AX-0004/content.md`

- Source: 1791 bytes; SHA-256 `bc3f351b12c0c693fd4103c4394cdd158ab14319e0f07d63f44c50b2d3793b1f`.
- Review records: F65, F69, F70.
- Inspected passage/physical facts: AX-0004 — Navigation; Purpose; Design Goals; Navigation Principles; Primary Navigation; Secondary Navigation; Context Navigation; Cross Navigation; Breadcrumbs; Navigation Stability; Scalability

### `foundation/specifications/ax/AX-0004/metadata.yaml`

- Source: 109 bytes; SHA-256 `7ce629897fcbdb2ecd20e9e4b1b34ec9c0e73e7a47ef1769951626266d528a9a`.
- Review records: F65, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0004; title: Navigation; status: draft; version: 0.1.0; authors:; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0005/content.md`

- Source: 1777 bytes; SHA-256 `fa84a5cca381cca1ef5eff5e4a5b2606a2177f181f234fab2422352a2b20ee94`.
- Review records: F65, F69, F70.
- Inspected passage/physical facts: AX-0005 — Visual Language; Purpose; Design Goals; Core Principles; Typography; Color; Icons; Spacing; Visual Hierarchy; Consistency; Scalability

### `foundation/specifications/ax/AX-0005/metadata.yaml`

- Source: 114 bytes; SHA-256 `476051dfe9ca01a49e5e4c8ca740a3bb5c321c957804b7c77b323570d1d8a200`.
- Review records: F65, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0005; title: Visual Language; status: draft; version: 0.1.0; authors:; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0006/content.md`

- Source: 1619 bytes; SHA-256 `5b8d71c52379a2f9f15dc7360aff28c484745263f15c3fc1ad44cf7700fdb171`.
- Review records: F65, F69.
- Inspected passage/physical facts: AX-0006 — Interaction Model; Purpose; Design Goals; Core Principles; Feedback; Discoverability; Predictability; Reversibility; Efficiency; Responsiveness; Scalability

### `foundation/specifications/ax/AX-0006/metadata.yaml`

- Source: 116 bytes; SHA-256 `9acc3302a8fbd83b13950405a378928dcb28eadab5bfdb5b342ae5f146d5ca5a`.
- Review records: F65, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0006; title: Interaction Model; status: draft; version: 0.1.0; authors:; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0007/content.md`

- Source: 1884 bytes; SHA-256 `7e34b55477bb21519ae2e3f8bb87dfaad2f8fc05c43533b3a96ad72fab672fd0`.
- Review records: F65, F69, F70.
- Inspected passage/physical facts: AX-0007 — Knowledge Visualization; Purpose; Design Goals; Core Principles; Multiple Representations; Relationship Visualization; Graph Visualization; Diagrams; Traceability; Consistency; Scalability

### `foundation/specifications/ax/AX-0007/metadata.yaml`

- Source: 122 bytes; SHA-256 `2a032490c34faeed2ce4f8837152c95ecc7fb5327b1a0207737421e874ac422d`.
- Review records: F65, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0007; title: Knowledge Visualization; status: draft; version: 0.1.0; authors:; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0008/content.md`

- Source: 1815 bytes; SHA-256 `1adb5fb99ab15183e23d0de0bbbea774c04fcc0d48eff4e48d83287ce01335e0`.
- Review records: F65, F69, F70.
- Inspected passage/physical facts: AX-0008 — Search Experience; Purpose; Design Goals; Core Principles; Search Scope; Search Results; Progressive Refinement; Relationship Discovery; Ranking; Consistency; Scalability

### `foundation/specifications/ax/AX-0008/metadata.yaml`

- Source: 116 bytes; SHA-256 `c692725d4ebb76c60a19602b06d218d13d3fa4ce7a797c59c96056205d6e1a6c`.
- Review records: F65, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0008; title: Search Experience; status: draft; version: 0.1.0; authors:; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0009/content.md`

- Source: 1803 bytes; SHA-256 `f5c7e416df0516fc01dbf9b576c160106fd60c4a443c739ab6549ef79b499ca3`.
- Review records: F65, F69, F70.
- Inspected passage/physical facts: AX-0009 — AI Experience; Purpose; Design Goals; Core Principles; Shared Knowledge; Transparency; Human Control; Explainability; Collaboration; Trust; Scalability

### `foundation/specifications/ax/AX-0009/metadata.yaml`

- Source: 112 bytes; SHA-256 `80dcc44c911d1d82ae2bccc907e2565941ffc367a9520e7f58ed7d637b09d36e`.
- Review records: F65, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0009; title: AI Experience; status: draft; version: 0.1.0; authors:; ontologyType: ONT-AX

### `foundation/specifications/ax/AX-0010/content.md`

- Source: 1695 bytes; SHA-256 `5be5baac9f5f8d57b23e50f96d05fe92b18b7a2a00603b85221272fb3cfbff33`.
- Review records: F65, F69, F70.
- Inspected passage/physical facts: AX-0010 — Trust & Transparency; Purpose; Design Goals; Core Principles; Provenance; Version History; Traceability; AI Transparency; Consistency; User Confidence; Scalability

### `foundation/specifications/ax/AX-0010/metadata.yaml`

- Source: 119 bytes; SHA-256 `3cfd8e54eb16871542eac37cd0565299bf8b44d4343fa1291f104a85c9bcfa2a`.
- Review records: F65, F53, F08, F62, F11.
- Inspected passage/physical facts: id: AX-0010; title: Trust & Transparency; status: draft; version: 0.1.0; authors:; ontologyType: ONT-AX

### `foundation/specifications/entity/ENTITY-0001/content.md`

- Source: 3000 bytes; SHA-256 `28246ecf7d900fa617b144cb0741c0f8c1feb873537111af0f4500004ff4d6bd`.
- Review records: F21, F34.
- Inspected passage/physical facts: ENTITY-0001 Universal Entity Model; Status; Purpose; Definition; Identity; Type; Content; Metadata; Relationships; Persistence Independence; Specialization; Consequences; References

### `foundation/specifications/entity/ENTITY-0001/metadata.yaml`

- Source: 100 bytes; SHA-256 `218affa00094cf77e29e062479ecef35986808a739a8c7da780fad81e217f107`.
- Review records: F53, F08, F62, F11.
- Inspected passage/physical facts: id: ENTITY-0001; title: Universal Entity Model; status: Draft; version: 0.2.0; ontologyType: ONT-Entity

### `foundation/specifications/entity/ENTITY-0001/relations.yaml`

- Source: 79 bytes; SHA-256 `eacb3f87ad1bfa2af6b632fef8742cf3f98691ddebd61109e2406941d776f60d`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: [] /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/glossary/README.md`

- Source: 893 bytes; SHA-256 `eb5c2775132c6dc13308905acffb804b75b13db831c68fe0c82dda6c4a0a9618`.
- Review records: F67.
- Inspected passage/physical facts: # Glossary - Core Terminology /  / ## Purpose /  / This glossary defines the normative terminology used throughout the / ATON Foundation. /  / Every term SHALL have exactly one normative definition. /  / No specification SHALL redefine an existing term. /  / ## Glossary Entry Identity /  / Every Glossary Entry SHALL have a stable identifier using the following form: /  / \`TERM-<CanonicalTerm>\` /  / The \`<CanonicalTerm>\` SHALL identify the canonical terminology item represented / by the Glossary Entry. /  / Examples include: /  / - \`TERM-Entity\` / - \`TERM-Artifact\` / - \`TERM-Predicate\` / - \`TERM-Relation\` /  / Glossary Entry identifiers SHALL be stable and SHALL NOT depend on: /  / - file names; / - directory locations; / - serialization formats; or / - rendered documentation. /  / The canonical term represented by a Glossary Entry SHALL remain stable unless / the terminology itself is intentionally changed through the applicable / governance process.

### `foundation/specifications/glossary/TERM-Artifact/content.md`

- Source: 1979 bytes; SHA-256 `6a440d720fe699ecee714b0128ad12697186ad67866930b19179911b20310e44`.
- Review records: F14, F37.
- Inspected passage/physical facts: Artifact; Definition; Role in ATON; Persistence Independence; Relationship to the Artifact Model; Related Terms; References

### `foundation/specifications/glossary/TERM-Artifact/metadata.yaml`

- Source: 122 bytes; SHA-256 `a4d7f68ee5f14c5c39ebc3a904bf91286815923f9b221ba92835b97486d3076b`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: TERM-Artifact; title: Artifact; entityType: glossary-entry; status: Draft; version: 0.2.0; ontologyType: ONT-GlossaryEntry

### `foundation/specifications/glossary/TERM-Artifact/relations.yaml`

- Source: 106 bytes; SHA-256 `650d30342deaba64a3387ad3d570111e3ad7686df5d4c78199f4de0b6d847d0d`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ONT-Artifact /   - ADR-0013 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/glossary/TERM-Entity/content.md`

- Source: 1191 bytes; SHA-256 `9dbadddbc9f1befcb390c36d3a1112df2e3e0244a536c8b6dd4aa057ca6a4e21`.
- Review records: F37.
- Inspected passage/physical facts: Entity; Definition; Role in ATON; Relationship to the Entity Model; Related Terms; References

### `foundation/specifications/glossary/TERM-Entity/metadata.yaml`

- Source: 118 bytes; SHA-256 `d10d5a0bc0db4d829b20859569297acbc65c4cf387d2bf302d270eb83f3c8fd7`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: TERM-Entity; title: Entity; entityType: glossary-entry; status: Draft; version: 0.2.0; ontologyType: ONT-GlossaryEntry

### `foundation/specifications/glossary/TERM-Entity/relations.yaml`

- Source: 88 bytes; SHA-256 `2ac8998576fcd9a3f05815f1b60e504921415d5f808737ac752443ffd691be20`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ENTITY-0001 / dependsOn: [] / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/glossary/TERM-Predicate/content.md`

- Source: 1613 bytes; SHA-256 `e610ff1e1860b97ecf382706d8fce992837e6ef9e4023ca44a2dfa2eced6e71f`.
- Review records: F38.
- Inspected passage/physical facts: Predicate; Definition; Role in ATON; Relationship to Relations; Relationship to Constraints; Direction; Related Terms; References

### `foundation/specifications/glossary/TERM-Predicate/metadata.yaml`

- Source: 109 bytes; SHA-256 `8b4e51606e03cbf0c192ce266d233b1c02d9fca8f4666fc99cdbdae5ebe834a2`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: TERM-Predicate; title: Predicate; entityType: glossary-entry; status: Draft; ontologyType: ONT-GlossaryEntry

### `foundation/specifications/glossary/TERM-Predicate/relations.yaml`

- Source: 149 bytes; SHA-256 `ff572e6b8ecff9750beab635e43b944ab524793d02311266f58122a1ea9cfa8c`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - PRED-governs /   - PRED-motivates /   - PRED-references /   - PRED-refines /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/glossary/TERM-Relation/content.md`

- Source: 1786 bytes; SHA-256 `48f7fe4184d20a5efce9cddd476078639b93ce487b71b49a3e19bdc7dd191c3e`.
- Review records: F38, F49.
- Inspected passage/physical facts: Relation; Definition; Role in ATON; Relationship to the Relation Model; Relationship to Predicate; Direction; Identity; Persistence Independence; Related Terms; References

### `foundation/specifications/glossary/TERM-Relation/metadata.yaml`

- Source: 107 bytes; SHA-256 `5c04919acff92a7fa60446bc977f65020786eb6b598f65a484aa00033247769e`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: TERM-Relation; title: Relation; entityType: glossary-entry; status: Draft; ontologyType: ONT-GlossaryEntry

### `foundation/specifications/glossary/TERM-Relation/relations.yaml`

- Source: 122 bytes; SHA-256 `fecf70502ddc0b128c282414350d55ab08ff4f5c21a91704d54611d59067e961`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ONT-Relation /   - ENTITY-0001 /   - ADR-0014 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/ontology/ADR/content.md`

- Source: 436 bytes; SHA-256 `724d4c5ac02c9fa561d63f2c4bf2e6e28657ac4ffd4b41611507ca5bafe13a3c`.
- Review records: F39.
- Inspected passage/physical facts: Architecture Decision Record; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/ADR/metadata.yaml`

- Source: 83 bytes; SHA-256 `230923e70c7ac6e527ed9b57d3212987ff72d276f6e8217034e7f2780eba69cb`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-ADR; title: Architecture Decision Record; entityType: ontology; status: Draft

### `foundation/specifications/ontology/ADR/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/AX/content.md`

- Source: 265 bytes; SHA-256 `49e21d0fee98db21aea98559397b1704f25a9ad86ffeddd99cde04c5c61784da`.
- Review records: F39, F65.
- Inspected passage/physical facts: AX

### `foundation/specifications/ontology/AX/metadata.yaml`

- Source: 69 bytes; SHA-256 `1d16ac8a15a9005022c79f37b8a5ae3e645b096dcfb537c08530da78b830abdc`.
- Review records: F48, F65, F47, F11.
- Inspected passage/physical facts: id: ONT-AX; title: ATON Experience; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Artifact/content.md`

- Source: 1812 bytes; SHA-256 `36ce9974e28437b1a4c14441330388bddf0ad09fb60bab217a8f53fb4c7aa36b`.
- Review records: F14.
- Inspected passage/physical facts: Artifact; Status; Definition; Role in ATON; Persistence Independence; References

### `foundation/specifications/ontology/Artifact/metadata.yaml`

- Source: 83 bytes; SHA-256 `a929181cf6a2c8352481686101bd5fc28743b6114e364e2346e89948b866aa90`.
- Review records: F48, F47, F53, F11.
- Inspected passage/physical facts: id: ONT-Artifact; title: Artifact; entityType: ontology; status: Draft; version: 0.2.0

### `foundation/specifications/ontology/Artifact/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Collection/content.md`

- Source: 414 bytes; SHA-256 `baa6e00963679af4f62cca423935947f59683f8d13bd567dd3eff71914d06b3c`.
- Review records: F39.
- Inspected passage/physical facts: Collection; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Collection/metadata.yaml`

- Source: 72 bytes; SHA-256 `d1fea7f4837b0313beeb0df3df310bf92dfa32b8a30eb99724fe6e73f45d83f8`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Collection; title: Collection; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Collection/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Component/content.md`

- Source: 427 bytes; SHA-256 `eebb511f7a63206c2b95d688b55136ae99817bb9396ac4d999c5e1886303ffb9`.
- Review records: F39.
- Inspected passage/physical facts: Component; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Component/metadata.yaml`

- Source: 70 bytes; SHA-256 `1273d3ad30f95e2160c8a269a13d02da8c56d5f0a17e1fa0c7792f25cc360953`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Component; title: Component; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Component/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Constitution/content.md`

- Source: 246 bytes; SHA-256 `3835b13f3bd55966f506130f98e0cd8ef3215e8647ba457d5f6bac01ec56e269`.
- Review records: F39, F65.
- Inspected passage/physical facts: Constitution

### `foundation/specifications/ontology/Constitution/metadata.yaml`

- Source: 76 bytes; SHA-256 `11ba0f86084188c6453f428298a2b64ff65b5b1002b23caccfbfa7940c5748c9`.
- Review records: F48, F65, F47, F11.
- Inspected passage/physical facts: id: ONT-Constitution; title: Constitution; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Decision/content.md`

- Source: 409 bytes; SHA-256 `e8afc07d44f858a3b03bc210fda818b19bdff7e6e6c5f0d89b68d26695a8e071`.
- Review records: F39.
- Inspected passage/physical facts: Decision; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Decision/metadata.yaml`

- Source: 68 bytes; SHA-256 `1dd7bbf2c4f4431bd24fce9ed33d66a7f4c54e53458d8c65e7010885d781ffef`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Decision; title: Decision; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Decision/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Definition/content.md`

- Source: 424 bytes; SHA-256 `26439c07060e8f8864a48514493589ab40988ea67b02a613fb4473d87f4edd79`.
- Review records: F39.
- Inspected passage/physical facts: Definition; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Definition/metadata.yaml`

- Source: 72 bytes; SHA-256 `dee564a37178228b8537f6513c0ae90fbce62b199ca676bbac0901aa148da87f`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Definition; title: Definition; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Definition/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Entity/content.md`

- Source: 670 bytes; SHA-256 `f5dc7c8581ed4925a83d0f94cad7749388934ecc7c660384b99c49c5f1b8952b`.
- Review records: F37.
- Inspected passage/physical facts: Entity; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Entity/metadata.yaml`

- Source: 79 bytes; SHA-256 `83493a3096b083be9be7fd74fb7c01824284bd0b998455f2c1ec9d964dfe23e5`.
- Review records: F48, F47, F53, F11.
- Inspected passage/physical facts: id: ONT-Entity; title: Entity; entityType: ontology; status: Draft; version: 0.2.0

### `foundation/specifications/ontology/Entity/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Finding/content.md`

- Source: 287 bytes; SHA-256 `8bd6bce3be3a8a8393e3678909e76e03d448bcb964a844f4c93fd60b44c40011`.
- Review records: F35.
- Inspected passage/physical facts: Finding

### `foundation/specifications/ontology/Finding/metadata.yaml`

- Source: 66 bytes; SHA-256 `33974059c4fb354574a8cb654e2fea81534fbceb915657422ff2385a9c8bd1d7`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Finding; title: Finding; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Finding/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/GlossaryEntry/content.md`

- Source: 419 bytes; SHA-256 `94c3de012b706b949b37ed2cde6704c46ea08ea0c2a51814c4feaa5c080bebb6`.
- Review records: F39.
- Inspected passage/physical facts: Glossary Entry; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/GlossaryEntry/metadata.yaml`

- Source: 79 bytes; SHA-256 `073d69f5dcee3223fc82f81ab0b1509b9ad9b0e3e4bad6da359a161d50350b1e`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-GlossaryEntry; title: Glossary Entry; entityType: ontology; status: Draft

### `foundation/specifications/ontology/GlossaryEntry/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Interface/content.md`

- Source: 406 bytes; SHA-256 `2c2b86360207e78a3348480d751caa1e94e6d637bdc05647d5dbee8aa49b68f3`.
- Review records: F39.
- Inspected passage/physical facts: Interface; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Interface/metadata.yaml`

- Source: 70 bytes; SHA-256 `6bf562d57d41608ff9d4d36df4a6e3b144613f384e5f647d4db25662fca2cb5b`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Interface; title: Interface; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Interface/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Metadata/content.md`

- Source: 449 bytes; SHA-256 `2250609c974692f5d7166f559e82da9d5f0ea8f5dc7d2a1816f2862b643c6b98`.
- Review records: F34.
- Inspected passage/physical facts: Metadata; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Metadata/metadata.yaml`

- Source: 68 bytes; SHA-256 `1b8c8a17548c4da2d186bfd542303dd9db387548d124620655f61a5fae87b2b6`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Metadata; title: Metadata; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Metadata/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Note/content.md`

- Source: 341 bytes; SHA-256 `fb698adc4a2ac174d2ee569dca2c564abf80b49ad1d795fe77f6744f326813d0`.
- Review records: F35, F36.
- Inspected passage/physical facts: Note

### `foundation/specifications/ontology/Note/metadata.yaml`

- Source: 60 bytes; SHA-256 `ce92c5bd2a12351950aa5c9eeb4e8648cdc4a0ec3fc40456f961bfe9f7b851a3`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Note; title: Note; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Note/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Predicate/content.md`

- Source: 494 bytes; SHA-256 `d4556962e3839e910b2b739b61ef7ff2496e7d660715d74d2fec649825346e1e`.
- Review records: F38.
- Inspected passage/physical facts: Predicate

### `foundation/specifications/ontology/Predicate/metadata.yaml`

- Source: 85 bytes; SHA-256 `aabc7ff157b66a93371250b38f3e1a9f346529d851ce47cf069023e750301791`.
- Review records: F48, F47, F53, F11.
- Inspected passage/physical facts: id: ONT-Predicate; title: Predicate; entityType: ontology; status: Draft; version: 0.2.0

### `foundation/specifications/ontology/Predicate/relations.yaml`

- Source: 115 bytes; SHA-256 `9bd9acaded76e98672375a014830c0738f14dbfcc6508f62778a1148de0da802`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0026 /   - RFC-0027 /   - RFC-0029 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/ontology/Property/content.md`

- Source: 381 bytes; SHA-256 `e8498115db95a4d2dc25dbfc74aaef776ee1858c5f0b12d6198707bc1a6b072a`.
- Review records: F34.
- Inspected passage/physical facts: Property; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Property/metadata.yaml`

- Source: 68 bytes; SHA-256 `c8545ec7c0a901a8014199058dab2af60c4752d5703cca48567a6ecb90171829`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Property; title: Property; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Property/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/RFC/content.md`

- Source: 454 bytes; SHA-256 `101f39beaae8b3019d15a47f3541500640bf23015e615093f0739b785d622e7b`.
- Review records: F39.
- Inspected passage/physical facts: Request for Comments; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/RFC/metadata.yaml`

- Source: 75 bytes; SHA-256 `e8a4c9d46211423b02faede57708c4983e2cfe45147ed2e029c9fd9311d7866a`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-RFC; title: Request for Comments; entityType: ontology; status: Draft

### `foundation/specifications/ontology/RFC/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Relation/content.md`

- Source: 424 bytes; SHA-256 `86ead09be6f8aacf9cbd6f2e3f5e9b87caa571e8967154aa82e36ea07919732d`.
- Review records: F38, F49.
- Inspected passage/physical facts: Relation; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Relation/metadata.yaml`

- Source: 68 bytes; SHA-256 `8256f1d7753073832f92b0aeb1126893966fc4f1e058916bdef7b02ac18100ba`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Relation; title: Relation; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Relation/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Requirement/content.md`

- Source: 434 bytes; SHA-256 `022f6614c9f32059572bb74a894a00e981e7ce5baca96d3596e2ae96a1057d81`.
- Review records: F39.
- Inspected passage/physical facts: Requirement; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Requirement/metadata.yaml`

- Source: 74 bytes; SHA-256 `fe3e5993ab04a50ff729daa0906bb579e5b8129bfa5b8e18807208dbc428f5a3`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Requirement; title: Requirement; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Requirement/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Review/content.md`

- Source: 198 bytes; SHA-256 `1f7eb30925619299b24dce799233bb251192ee5083a2465a84dc1ec0e1ffbf9e`.
- Review records: F35.
- Inspected passage/physical facts: Review

### `foundation/specifications/ontology/Review/metadata.yaml`

- Source: 64 bytes; SHA-256 `8bc3d3fc16dafa1783c5b1cb620ce96475974172cbe6289e947c27b521f59ac8`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Review; title: Review; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Review/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Test/content.md`

- Source: 426 bytes; SHA-256 `ddf795366e28c99fe095ae9b6cfde20b12daa31897ce164bb2dd8e8e41122e60`.
- Review records: F39.
- Inspected passage/physical facts: Test; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Test/metadata.yaml`

- Source: 60 bytes; SHA-256 `e10285edbf72b730ee8d1824e1b75463eee7b225cd735e4256dffb173bf79c3b`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Test; title: Test; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Test/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/Thing/content.md`

- Source: 459 bytes; SHA-256 `47d7a88bd222c2ceb28c685c0ee8c6ea6c5015fb10f8da1582062327cd1d2cfa`.
- Review records: F39.
- Inspected passage/physical facts: Thing; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/Thing/metadata.yaml`

- Source: 62 bytes; SHA-256 `77fb65a6757934f709bbfe021e56272fb9e000deca4254764f681c23f8fcf757`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-Thing; title: Thing; entityType: ontology; status: Draft

### `foundation/specifications/ontology/Thing/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/ontology/View/content.md`

- Source: 418 bytes; SHA-256 `d1870f76787cef5c3470de1729769ff475e2a4cef62ea34c96b64b08e0ee9434`.
- Review records: F39.
- Inspected passage/physical facts: View; Status; Definition; Role in ATON; References

### `foundation/specifications/ontology/View/metadata.yaml`

- Source: 60 bytes; SHA-256 `a9c86e8fb3edc6049e478b3c263932a24e6331cc400a400b7068c57034e860d6`.
- Review records: F48, F47, F11.
- Inspected passage/physical facts: id: ONT-View; title: View; entityType: ontology; status: Draft

### `foundation/specifications/ontology/View/relations.yaml`

- Source: 15 bytes; SHA-256 `4aa0dd6a1242e306276192cffdd32fa3a7ad368051716c9125be548c85cf4def`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: []

### `foundation/specifications/predicates/governs/constraints.yaml`

- Source: 216 bytes; SHA-256 `d6435387621aff314515ae4fb95387da1af9486eb3be8202cf8b7bc635ddd0e1`.
- Review records: F45.
- Inspected passage/physical facts: allowedPairs: /   - source: ONT-ADR /     target: ONT-Artifact /   - source: ONT-ADR /     target: ONT-Collection /   - source: ONT-Constitution /     target: ONT-Artifact /   - source: ONT-Constitution /     target: ONT-Collection

### `foundation/specifications/predicates/governs/content.md`

- Source: 412 bytes; SHA-256 `117d6ca9415e929b03c37998380f4f4dde63742823d1dfecd80024d45d1f9c8c`.
- Review records: F46.
- Inspected passage/physical facts: governs; Meaning; Direction; Allowed Pairs; Inverse

### `foundation/specifications/predicates/governs/metadata.yaml`

- Source: 96 bytes; SHA-256 `fb7aa7af96a2a9b327f772c6c40ff9a1b166ad689e24b5fc005f0a178eac1ae8`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: PRED-governs; title: governs; entityType: predicate; ontologyType: ONT-Predicate; status: Draft

### `foundation/specifications/predicates/governs/relations.yaml`

- Source: 102 bytes; SHA-256 `bd35e8a26be833aa83ec771ec443f46d2e49ad2cdc3843e9b15c6f11a09f9dc5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0027 /   - RFC-0029 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/predicates/motivates/constraints.yaml`

- Source: 99 bytes; SHA-256 `52494fadd48094c5b9435622a5d2f6ae115517655be1856925341c2e9880a46b`.
- Review records: .
- Inspected passage/physical facts: allowedPairs: /   - source: ONT-Note /     target: ONT-ADR /   - source: ONT-Finding /     target: ONT-ADR

### `foundation/specifications/predicates/motivates/content.md`

- Source: 1669 bytes; SHA-256 `022e3019a70ed387da3efa7ec34a74a9c4971f29efbdf35c29362808a278e0f4`.
- Review records: F46.
- Inspected passage/physical facts: motivates; Meaning; Allowed Pairs; Inverse; Direction; Semantic Validation; Cardinality

### `foundation/specifications/predicates/motivates/metadata.yaml`

- Source: 100 bytes; SHA-256 `2f318760ec7cb66e542e90dbb5de4cb11318485d27aec7a3c4c68e478f4ec0a8`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: PRED-motivates; title: motivates; entityType: predicate; status: Draft; ontologyType: ONT-Predicate

### `foundation/specifications/predicates/motivates/relations.yaml`

- Source: 112 bytes; SHA-256 `e8ee2cbd679cad9e118fb4372686937d25e00fa31b7aca4e95b835ee951fc338`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0027 /   - RFC-0029 /  / dependsOn: /   - RFC-0029 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/predicates/references/constraints.yaml`

- Source: 92 bytes; SHA-256 `cfbf96816143b41d995070201d72fb29631ac8bfe6dcefb546f465934d111934`.
- Review records: F44.
- Inspected passage/physical facts: allowedPairs: /   - source: /       pattern: ANY-CONCEPT /     target: /       pattern: ANY-CONCEPT

### `foundation/specifications/predicates/references/content.md`

- Source: 1392 bytes; SHA-256 `3fb677bbeed80356459916bcff9dab9d55edef4a65ef01755aa0b053c6e0d09a`.
- Review records: F44, F46.
- Inspected passage/physical facts: references; Meaning; Allowed Pairs; Inverse; Direction; Semantic Validation; Cardinality

### `foundation/specifications/predicates/references/metadata.yaml`

- Source: 102 bytes; SHA-256 `0ef0abfd0750981249bd525caf3a3b5bb16dd91c20d15e71f1be3456d55b511d`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: PRED-references; title: references; entityType: predicate; status: Draft; ontologyType: ONT-Predicate

### `foundation/specifications/predicates/references/relations.yaml`

- Source: 112 bytes; SHA-256 `e8ee2cbd679cad9e118fb4372686937d25e00fa31b7aca4e95b835ee951fc338`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0027 /   - RFC-0029 /  / dependsOn: /   - RFC-0029 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/predicates/refines/constraints.yaml`

- Source: 292 bytes; SHA-256 `19773c938c570a77d0c3486909af2d94bd61928adbcdda986b53270ebef9d62c`.
- Review records: F45.
- Inspected passage/physical facts: allowedPairs: /   - source: ONT-Requirement /     target: ONT-Requirement /   - source: ONT-RFC /     target: ONT-RFC /   - source: ONT-ADR /     target: ONT-ADR /   - source: ONT-Component /     target: ONT-Component /   - source: ONT-Interface /     target: ONT-Interface /   - source: ONT-AX /     target: ONT-AX

### `foundation/specifications/predicates/refines/content.md`

- Source: 433 bytes; SHA-256 `c3d5dbe010731f852a240e86f4044aa1541917eb9eccb65da1eca4c20de03a5a`.
- Review records: F46.
- Inspected passage/physical facts: refines; Meaning; Direction; Allowed Pairs; Inverse

### `foundation/specifications/predicates/refines/metadata.yaml`

- Source: 96 bytes; SHA-256 `6451d33d85af2cd4f54801defd7bd686e7abed132dd7f22e0d01e5d82e9fd150`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: PRED-refines; title: refines; entityType: predicate; ontologyType: ONT-Predicate; status: Draft

### `foundation/specifications/predicates/refines/relations.yaml`

- Source: 102 bytes; SHA-256 `bd35e8a26be833aa83ec771ec443f46d2e49ad2cdc3843e9b15c6f11a09f9dc5`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0027 /   - RFC-0029 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0000/content.md`

- Source: 1554 bytes; SHA-256 `d42bf389167c2f661b68217e33fd75c36a4e0f658e71f98e022e9fa1b5c81845`.
- Review records: F22, F72.
- Inspected passage/physical facts: RFC-0000 – Document Conventions; Summary; Motivation; Goals; Non Goals; Proposal; Required Sections; Language; Consequences; Advantages; Disadvantages; Alternatives; Migration; Open Questions

### `foundation/specifications/rfc/RFC-0000/metadata.yaml`

- Source: 267 bytes; SHA-256 `5d301eb8d3dc0b3aaa1ddcc1204c05a0439464d815da1f0b447ccb4e3779e4b7`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0000; title: Document Conventions; entityType: rfc; status: Accepted; version: 1.0.0; author: Marco Kachelrieß; created: 2026-07-23; updated: 2026-07-23; language: en; tags:; reviewers: []; approvers: []; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0000/relations.yaml`

- Source: 208 bytes; SHA-256 `d3012acabba15aa8074c7331f745f37a912050626f5968f604c46eaeae600bf2`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ietf:rfc:2119 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: /   - aton:rfc:0001 /   - aton:rfc:0002 /   - aton:rfc:0003 /   - aton:rfc:0004 /   - aton:rfc:0005 /  / children: [] /  / parents: []

### `foundation/specifications/rfc/RFC-0001/content.md`

- Source: 11835 bytes; SHA-256 `4953d04551009e02dde0c857d21c0b3c2500a86dda32b469121575e64906c769`.
- Review records: F23, F24, F29, F72.
- Inspected passage/physical facts: RFC-0001 — Engineering Entity Model; Status; Summary; Motivation; Goals; Non Goals; Proposal; Engineering Entity; Entity Identity; Entity and Artifact; Entity and Metadata; Entity and Relations; Entity and Version; Entity and Physical Representation; Entity Addressability; Entity Type; Entity Participation in the Knowledge Graph; Entity Containment; Canonical Domain Representation; Consequences; Positive; Negative; Alternatives; Treat files as Engineering Entities; Treat document sections as Engineering Entities; Define entity identity through repository paths; Define a separate entity model for each physical representation; Treat every artifact as one Engineering Entity; Migration; Open Questions; References

### `foundation/specifications/rfc/RFC-0001/metadata.yaml`

- Source: 100 bytes; SHA-256 `c4145d4581605e50f937422fb705ab73fb4dde3a1f69afdd87f4818f1f8fce95`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0001; title: Entity Model; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0001/relations.yaml`

- Source: 217 bytes; SHA-256 `e0ec68322d3cab96a0aee6b1a6c25f1f2d4cf8fd6ebe4bfe992c0f609502d61a`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0004 /   - ADR-0005 /   - ADR-0006 /   - ADR-0008 /   - ADR-0011 /   - RFC-0002 /   - RFC-0010 /   - RFC-0015 /   - RFC-0025 /   - NOTE-0008 /  / dependsOn: /   - RFC-0002 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0002/content.md`

- Source: 14332 bytes; SHA-256 `6a9a2f48cb2dc301c6929d14dec0551dd14e649022bac8cd528d52b0c44455ef`.
- Review records: F25, F72.
- Inspected passage/physical facts: RFC-0002 — Engineering Identity Model; Status; Summary; Motivation; Goals; Non-Goals; Engineering Identity; Identity Identifier; Identity and Engineering Versions; Identity and Artifact Revisions; Identity and Git; Identity and Physical Representation; Identity and Relationships; Identity and Historical Knowledge; Identity Changes; Identity and Deletion; Identity Scope; Identity Resolution; Immutability of Identity; Migration; Consequences; Positive; Negative; Alternatives Considered; Use file paths as Engineering Identity; Use file names as Engineering Identity; Use Git commit hashes as Engineering Identity; Use Engineering Version identifiers as Engineering Identity; Generate a new identity for every modification; Relationship to Other Specifications; Acceptance Criteria; Open Questions

### `foundation/specifications/rfc/RFC-0002/metadata.yaml`

- Source: 102 bytes; SHA-256 `a809cd59f4bf9f2a0361be6ba8ded5e1fd11680c84a6dd8777667f60fd9b4b90`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0002; title: Identity Model; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0002/relations.yaml`

- Source: 155 bytes; SHA-256 `65c249d436a4240f45caed8a867300f52f417a6af64689079e42934caa70416e`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0012 /   - RFC-0012 /   - RFC-0015 /   - RFC-0025 /   - RFC-0029 /   - NOTE-0009 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0003/content.md`

- Source: 12994 bytes; SHA-256 `891d542cbab28a2a888ebacd210792377dc49c0981ab673760e487e2ee091ca8`.
- Review records: F26, F27, F29, F54, F72.
- Inspected passage/physical facts: RFC-0003 — Engineering Metadata Model; Status; Summary; Motivation; Goals; Non Goals; Proposal; Metadata; Metadata and Engineering Entities; Metadata and Identity; Metadata and Content; Metadata and Relations; Canonical Metadata; Persisted Metadata; Derived Metadata; Authoritative Metadata; Temporal Metadata; Metadata and Physical Representation; Metadata Normalization; Metadata Validation; Metadata and Ontology; Metadata Evolution; Metadata and Artifact Representation; Canonical Representation; Consequences; Positive; Negative; Alternatives; Treat metadata as part of engineering content; Treat metadata files as the domain model; Derive all metadata automatically; Persist all metadata; Use Git metadata as canonical engineering metadata; Migration; Open Questions; References

### `foundation/specifications/rfc/RFC-0003/metadata.yaml`

- Source: 102 bytes; SHA-256 `cccc5b487280ba250ddc5995951b8f24447f9200e36e4c2de836f8a2a0d9787c`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0003; title: Metadata Model; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0003/relations.yaml`

- Source: 205 bytes; SHA-256 `50d998bb3b6135759384773de4652ebf09316565457f011a4a9cff79655fe319`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0010 /   - ADR-0011 /   - RFC-0001 /   - RFC-0002 /   - RFC-0015 /   - RFC-0025 /   - NOTE-0011 /   - NOTE-0012 /  / dependsOn: /   - RFC-0001 /   - RFC-0002 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0004/content.md`

- Source: 16273 bytes; SHA-256 `ffc9116f46790f46c25cf45628c38e362e6ac379de816ded99f19c72025738db`.
- Review records: F28, F29, F49, F72.
- Inspected passage/physical facts: RFC-0004 — Engineering Relation Model; Status; Summary; Motivation; Goals; Non Goals; Proposal; Engineering Relation; Source; Predicate; Target; Directionality; Symmetry; Transitivity; Explicit Relations; Derived Relations; Relation Identity; Relation and Engineering Entities; Relation and Engineering Versions; Relation and Baselines; Relation and Releases; Relation and Physical Representation; Physical References; Relation Constraints; Relation Validation; Relation and the Engineering Knowledge Graph; Relation and Traceability; Relation and Navigation; Canonical Domain Representation; Predicate Semantics; Consequences; Positive; Negative; Alternatives; Treat hyperlinks as Engineering Relations; Treat file references as Engineering Relations; Infer all relations automatically; Define relation semantics inside the serialization format; Define all relation semantics in one generic model; Migration; Open Questions; References

### `foundation/specifications/rfc/RFC-0004/metadata.yaml`

- Source: 102 bytes; SHA-256 `26acb4872b82a14f92be8d0a99095872463dc0c0688673ec5805cdcaaa975071`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0004; title: Relation Model; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0004/relations.yaml`

- Source: 219 bytes; SHA-256 `650d4a15e6b0eb54bf6f5477e36a79ee7f3dc210da6618135cf1174b55a7a523`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0004 /   - ADR-0005 /   - ADR-0006 /   - ADR-0014 /   - RFC-0023 /   - RFC-0025 /   - RFC-0029 /   - NOTE-0010 /   - NOTE-0013 /   - NOTE-0016 /  / dependsOn: /   - RFC-0001 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0005/content.md`

- Source: 12924 bytes; SHA-256 `43c6efd6dfbf72aeebb742bf09c3ab9d74579f4ffb7055a78feb8278a2ae1719`.
- Review records: F30, F54, F72.
- Inspected passage/physical facts: RFC-0005 — Property Model; Status; Summary; Motivation; Goals; Non Goals; Proposal; Property; Property Name; Property Value; Property Ownership; Property Semantics; Canonical Properties; Metadata as Semantic Properties; Derived Properties; Materialized Properties; Property Type; Property Multiplicity; Property Units; Property Constraints; Property and Engineering Versions; Property and Physical Representation; Property and Serialization; Property Identity; Property Verification; Property and the Canonical Domain Model; Consequences; Positive; Negative; Alternatives; Treat every physical field as a Property; Treat Properties and Metadata as completely separate concepts; Derive all Properties from persistence; Define all properties directly in the serialization format; Make every property globally applicable; Migration; Open Questions; References

### `foundation/specifications/rfc/RFC-0005/metadata.yaml`

- Source: 102 bytes; SHA-256 `144e2ae341dc720443734192ae924a8d567a4d99a683c14250e4a486bc858885`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0005; title: Property Model; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0005/relations.yaml`

- Source: 151 bytes; SHA-256 `f149a01ed05b1a017c0a5333f50fdb4b0c851b0af3d107e3a6349d8ea17f2601`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0010 /   - ADR-0011 /   - RFC-0003 /   - RFC-0012 /   - RFC-0015 /  / dependsOn: /   - RFC-0003 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0010/content.md`

- Source: 17424 bytes; SHA-256 `6d31a4d1eed765cf6c2fae0d7114a2c2429135696dc1f877e3cb28c89c4d9358`.
- Review records: F31, F49, F72.
- Inspected passage/physical facts: RFC-0010 — Engineering Artifact Model; Status; Summary; Motivation; Goals; Non Goals; Proposal; Engineering Artifact; Engineering Entity; Artifact and Entity Representation; Artifact Identity; Artifact Content; Artifact Type; Artifact Revision; Artifact Revision and Physical Representation; Artifact and Engineering Version; Artifact and Baseline; Artifact and Release; Artifact and Relations; Artifact and Traceability; Multiple Physical Representations; Physical Representation; Representation Consistency; Artifact Metadata; Artifact Serialization; Artifact and Git; Artifact Portability; Artifact Verification; Consequences; Positive; Negative; Alternatives; Treat files as Engineering Artifacts; Treat Engineering Artifacts and Engineering Entities as identical; Require exactly one artifact per Engineering Entity; Treat every artifact revision as an Engineering Version; Derive artifact identity from repository paths; Migration; Open Questions; References

### `foundation/specifications/rfc/RFC-0010/metadata.yaml`

- Source: 102 bytes; SHA-256 `831f20bd592a1a509b31d7088a0e86ee76c8cafd38a5569ecaf5a2828247d33a`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0010; title: Artifact Model; entityType: rfc; status: Draft; version: 0.2.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0010/relations.yaml`

- Source: 271 bytes; SHA-256 `54200575224dbb08edec2bf67cc71f7b1a2ab363b1d409225a4562c48ed018aa`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0004 /   - ADR-0005 /   - ADR-0006 /   - ADR-0010 /   - ADR-0011 /   - RFC-0003 /   - RFC-0012 /   - RFC-0015 /   - RFC-0023 /   - RFC-0030 /   - RFC-0031 /   - NOTE-0008 /   - NOTE-0014 /   - NOTE-0017 /  / dependsOn: /   - RFC-0003 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0011/content.md`

- Source: 15004 bytes; SHA-256 `078c6e3cbef24b5e8ef8232195012fc185c2b881351b08f245dd61f8c9b9e9d6`.
- Review records: F32, F72.
- Inspected passage/physical facts: RFC-0011 — Repository Layout; Status; Summary; Motivation; Goals; Non Goals; Proposal; Repository; Repository Layout; Engineering Knowledge; Foundation Specifications; Repository Tooling; Generated Representations; Artifact Directory Structure; Canonical Artifact Files; Markdown; Metadata; Relations; Repository Paths; Directory Containment; Repository Discovery; Loading; Repository Validation; Repository Independence; Repository Portability; Git; Generated Content; Repository Configuration; Consequences; Positive; Negative; Alternatives; Use the Repository Hierarchy as the Engineering Knowledge Model; Allow Directory Containment to Define Relations; Store Every Engineering Concept as a Single File; Allow Each Project to Define an Arbitrary Layout; Make Git the Semantic Authority; Migration; Open Questions; References

### `foundation/specifications/rfc/RFC-0011/metadata.yaml`

- Source: 105 bytes; SHA-256 `40c0ee9fec03c27bd4200e4ff0cc8f04f2b046157dd155e9c0560b4af109064d`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0011; title: Repository Layout; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0011/relations.yaml`

- Source: 179 bytes; SHA-256 `dcf927c9290fdda7bb732310494037c532b8f1fc6b8d448e2fd35e3af02f07e9`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0002 /   - ADR-0011 /   - RFC-0010 /   - RFC-0015 /   - NOTE-0014 /   - NOTE-0017 /  / dependsOn: /   - RFC-0010 /   - RFC-0015 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0012/content.md`

- Source: 17367 bytes; SHA-256 `fb88d1fd42bff5b0671b522a22be314fc73353a88a97211137489f06047ae991`.
- Review records: F33, F54, F72.
- Inspected passage/physical facts: RFC-0012 — Engineering Version Semantics; Status; Summary; Motivation; Goals; Non-Goals; Engineering Identity; Engineering Version; Version Identity; Version Relationships; Version Immutability; Current State; Version Creation; Version and Artifact; Version and Git; Git Commit Semantics; Commit Provenance; Merge Commits; Rebases; Cherry-Picks; Version Provenance; Version Comparison; Version History; Versions and Relations; Versions and Lifecycle; Versions and Baselines; Versions and Releases; Persistence Independence; Verification; Migration; Consequences; Positive; Negative; Alternatives; Treat every Git commit as an Engineering Version; Use Git commit hashes as Engineering Version identifiers; Treat the physical artifact as the version; Derive all version information from Git; Use timestamps as version identity; Open Questions; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0012/metadata.yaml`

- Source: 98 bytes; SHA-256 `1b28490fb5f81258b568d9b0953017d05a2aaf77b9cab083874abced10d97b56`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0012; title: Versioning; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0012/relations.yaml`

- Source: 129 bytes; SHA-256 `ca437380ad3bff828e3b27d37589bfa4c98088387a4d879dfd77fd4e72fbcfa3`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0012 /   - RFC-0013 /   - RFC-0023 /   - NOTE-0006 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0013/content.md`

- Source: 16540 bytes; SHA-256 `422bc58063491044cd27dd31784a5e3d74cccd3fda95c76b76ad68bfff4408a8`.
- Review records: F33, F40, F72.
- Inspected passage/physical facts: RFC-0013 — Engineering Baseline Semantics; Status; Summary; Motivation; Goals; Non-Goals; Baseline; Baseline Identity; Baseline Membership; Explicit Selection; Reproducibility; Baseline Immutability; Baseline and Engineering Versions; Baseline and Artifact Revisions; Baseline and Relations; Baseline and Git; Git Commit as Baseline Evidence; Baseline and Release; Baseline Purpose; Baseline Description; Baseline Provenance; Baseline Verification; Baseline Comparison; Baseline History; Baseline Construction; Persistence Independence; Migration; Consequences; Positive; Negative; Alternatives; Treat every Git commit as a Baseline; Treat Git tags as Baselines; Treat the repository state as implicitly authoritative; Store only physical files in a Baseline; Make Baselines mutable; Open Questions; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0013/metadata.yaml`

- Source: 97 bytes; SHA-256 `1b33b292ddcfecd76e790575c2f380f6c187154e715b26a69b238571cab21f25`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0013; title: Baselines; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0013/relations.yaml`

- Source: 165 bytes; SHA-256 `9197b51a776b19945515b8fe4cdd67d77228ea1de42c4a0ee9d46e44dc6c71d8`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0012 /   - ADR-0003 /   - RFC-0012 /   - RFC-0015 /   - RFC-0023 /   - NOTE-0009 /  / dependsOn: /   - RFC-0012 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0014/content.md`

- Source: 16693 bytes; SHA-256 `b21e7d1d4949d8213ed798b550ecd0da26bf61c0d174442b75bd57445bad47d1`.
- Review records: F20, F29, F72.
- Inspected passage/physical facts: RFC-0014 — Engineering Knowledge Navigation; Status; Summary; Motivation; Scope; Navigation; Navigation Target; Navigation Path; Relation-Based Navigation; Direction; Navigation Views; Filtering; Traceability Navigation; Impact Navigation; Historical Navigation; External Navigation; Navigation and Persistence; Navigation and Search; Navigation and Views; Navigation Verification; Navigation and Ontology; Navigation and Versioning; Navigation and Processes; Canonical Navigation Model; Consequences; Positive; Negative; Relationship to Other Specifications; Alternatives Considered; Use Repository Structure as the Navigation Model; Use Document Hierarchy as the Canonical Navigation Model; Define Navigation Through a Specific User Interface; Treat Search and Navigation as the Same Capability; Define a Mandatory Navigation Workflow; Migration; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0014/metadata.yaml`

- Source: 108 bytes; SHA-256 `589ef66c5b3e37c46ab01220fddcdb5b29e4d82b1a43dcf74b059e00deac5eba`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0014; title: Engineering Knowledge Navigation; entityType: rfc; status: Proposed; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0014/relations.yaml`

- Source: 243 bytes; SHA-256 `9ea9dcffb4192a6734294856a06f502be214de339f9898c3ef1b5aee29f0c1e4`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0011 /   - ADR-0012 /   - ADR-0013 /   - ADR-0014 /   - ADR-0016 /   - ADR-0018 /   - RFC-0025 /   - RFC-0029 /   - NOTE-0018 /  / dependsOn: /   - RFC-0012 /   - RFC-0013 /   - RFC-0025 /   - RFC-0029 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0015/content.md`

- Source: 16734 bytes; SHA-256 `f6a8d5b0def07258b291e3816d2a928a78ddb6dbefb58efdd4bddb9239ab7c6f`.
- Review records: F41, F72.
- Inspected passage/physical facts: RFC-0015 — Logical Engineering Knowledge and Physical Representations; Status; Summary; Motivation; Scope; Logical Engineering Knowledge; Canonical Domain Representation; Physical Representation; Representation Boundary; Loading and Normalization; Export and Rendering; Multiple Representations; Representation Identity; Representation-Specific Information; Consistency; Provenance; Canonical Serialization and Representation; Repository Representation; Git Representation; Exchange Representations; Derived Representations; Persistence Independence; Implementation Boundary; Relationship to Other Specifications; Alternatives Considered; Treat Physical Files as the Engineering Knowledge Model; Treat the Repository Structure as Semantic; Define a Separate Semantic Model for Each Representation; Allow Kernel Components to Interpret Serialization Directly; Make One Physical Representation Universally Mandatory; Migration; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0015/metadata.yaml`

- Source: 134 bytes; SHA-256 `56aaabe3fe963ac6ae1746d511fe36321b269f6cf5752b2288447eab52e69b9e`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0015; title: Logical Engineering Knowledge and Physical Representations; entityType: rfc; status: Proposed; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0015/relations.yaml`

- Source: 283 bytes; SHA-256 `513c87f625503a35d5781e9b60edc11d1c440d41a66d0d75d77131b4cac031fa`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0002 /   - ADR-0008 /   - ADR-0011 /   - ADR-0012 /   - ADR-0018 /   - RFC-0012 /   - RFC-0013 /   - RFC-0014 /   - RFC-0025 /   - RFC-0029 /   - RFC-0030 /   - RFC-0031 /   - NOTE-0014 /   - NOTE-0017 /  / dependsOn: /   - RFC-0012 /   - RFC-0013 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0020/content.md`

- Source: 16650 bytes; SHA-256 `fdd944e932512f2ee3fbddfb5792556ba279bd55d914124a9e87b31311b86994`.
- Review records: F42, F55, F72.
- Inspected passage/physical facts: RFC-0020 — Ontology; Status; Summary; Motivation; Goals; Non-Goals; Ontology; Ontology Concept Identity; Ontology Type; Concept Specialization; Ontology and Engineering Entities; Ontology and Artifacts; Ontology and Metadata; Ontology and Relations; Ontology and Semantic Constraints; Ontology and Versioning; Ontology Evolution; Ontology and Persistence; Ontology and Implementation; Verification; Consequences; Positive; Negative; Alternatives Considered; Infer ontology types from repository structure; Infer ontology types from file extensions; Use programming-language types as the ontology; Allow every implementation to define its own ontology; Adopt a specific ontology technology as the canonical semantic model; Migration; Open Questions; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0020/metadata.yaml`

- Source: 96 bytes; SHA-256 `b75bd44fc3df80f8c6ab8eb4c7cdc113599f01436bc97ce8ca749306b04610c0`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0020; title: Ontology; entityType: rfc; status: Draft; version: 0.2.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0020/relations.yaml`

- Source: 213 bytes; SHA-256 `0e257ab62ff2e1fbdd6b95c8961ceb34801c6bc96ada21a003a30aa589db313e`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0007 /   - ADR-0008 /   - ADR-0011 /   - NOTE-0008 /   - NOTE-0010 /   - NOTE-0012 /   - NOTE-0021 / dependsOn: /   - RFC-0025 / supersedes: [] / supersededBy: [] / relatedTo: /   - RFC-0026 /   - RFC-0027 /   - RFC-0029

### `foundation/specifications/rfc/RFC-0021/content.md`

- Source: 9209 bytes; SHA-256 `2ae61d1a2c12f8cf48b8f25a6b012cea6b4e918f9772e63b47c7adf2bc46c5d6`.
- Review records: F29, F40, F71, F72.
- Inspected passage/physical facts: RFC-0021 — Views; Status; Summary; Motivation; Goals; Non-Goals; View; View Identity; View Definition; View and Canonical Knowledge; View and Engineering Entities; View and Engineering Versions; View and Baselines; View and Relations; View and Navigation; View and Physical Representation; Derived Information; Deterministic Views

### `foundation/specifications/rfc/RFC-0021/metadata.yaml`

- Source: 93 bytes; SHA-256 `75f998fd17d7d930f73a03516945489d7dd61d9453cba1007a6d079a7a3ea8ba`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0021; title: Views; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0021/relations.yaml`

- Source: 280 bytes; SHA-256 `0bdc4a26b336a6da435dc47477890a6cb04b5f3ab4031fbb9e8533fa126ed54b`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0004 /   - ADR-0006 /   - ADR-0008 /   - ADR-0011 /   - RFC-0014 /   - RFC-0015 /   - RFC-0025 /   - RFC-0026 /   - RFC-0029 /   - NOTE-0017 /   - NOTE-0018 /  / dependsOn: /   - RFC-0025 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: /   - RFC-0014 /   - RFC-0015 /   - RFC-0026 /   - RFC-0029

### `foundation/specifications/rfc/RFC-0022/content.md`

- Source: 13122 bytes; SHA-256 `16dcd9a002a858f463ea9cebf290944242fe140ac82c9b721a241f45cf28d20b`.
- Review records: F40, F71, F72.
- Inspected passage/physical facts: RFC-0022 — Collections; Status; Summary; Motivation; Goals; Non-Goals; Collection; Collection Identity; Collection Membership; Multiple Membership; Collection Membership and Identity; Collections and Engineering Versions; Collections and Baselines; Collections and Views; Collections and Relations; Nested Collections; Collection Membership Semantics; Dynamic Collections; Static Collections; Collection Comparison; Collection History; Collection and Physical Representation; Collection and Repository Structure; Collection Verification; Persistence Independence; Consequences; Positive

### `foundation/specifications/rfc/RFC-0022/metadata.yaml`

- Source: 99 bytes; SHA-256 `888504c79a7dbf0ac39af6566393b6a5bebff45ce988995618c14c1dc0db5b42`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0022; title: Collections; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0022/relations.yaml`

- Source: 204 bytes; SHA-256 `f46f71ee23ffcadbe0324cdd77749bc0c2fbf373e21ee2928560bc83fa85e46e`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0004 /   - ADR-0006 /   - ADR-0008 /   - ADR-0011 /   - RFC-0013 /   - RFC-0021 /   - RFC-0025 /   - RFC-0029 /   - NOTE-0018 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: /   - RFC-0014

### `foundation/specifications/rfc/RFC-0023/content.md`

- Source: 19503 bytes; SHA-256 `8a81ae931721f05d47acde75979dacd579f40221247f7eee189b50397cefe2a9`.
- Review records: F29, F61, F72.
- Inspected passage/physical facts: RFC-0023 — Engineering Traceability; Status; Summary; Motivation; Goals; Non-Goals; Traceability; Explicit Traceability; Semantic Traceability; Traceability and the Engineering Knowledge Graph; Traceability Navigation; Incoming and Outgoing Traceability; Traceability Paths; Traceability and Engineering Versions; Traceability and Baselines; Traceability and Releases; Traceability Across Artifact Representations; Traceability and Persistence; Traceability and Git; Traceability Verification; Traceability Completeness; Traceability Consistency; Impact Analysis; Dependency Analysis; Traceability Matrices; Traceability Queries; Traceability and Views; Traceability Provenance; Migration; Consequences; Positive; Negative; Alternatives; Store Traceability Only in Matrices; Derive Traceability from Git History; Derive Traceability from File Paths; Store Traceability in a Separate Traceability Database; Infer All Traceability Automatically; Open Questions; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0023/metadata.yaml`

- Source: 100 bytes; SHA-256 `db9c2f92653e50959936548a931964bfeab41075a800261ac25fe70d9008ba8a`.
- Review records: F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0023; title: Traceability; entityType: rfc; status: Draft; version: 0.1.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0023/relations.yaml`

- Source: 190 bytes; SHA-256 `d68cb4b11c9408cb0e3625cb44c75387d851da54b67363cd611227b59c9e9f0e`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0006 /   - ADR-0011 /   - ADR-0012 /   - RFC-0012 /   - RFC-0013 /   - RFC-0025 /   - RFC-0029 /  / dependsOn: /   - RFC-0025 /   - RFC-0029 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0024/content.md`

- Source: 3322 bytes; SHA-256 `3cd69691487a6d84297528a7bcfc724911dc51f2b5ad1759bb8650430ab4463c`.
- Review records: F41, F72.
- Inspected passage/physical facts: RFC-0024 — Docusaurus Renderer; Status; Abstract; Motivation; Scope; Input; Canonical Input Boundary; Output; Design Principles; Out of Scope; Architecture; Rationale

### `foundation/specifications/rfc/RFC-0024/metadata.yaml`

- Source: 120 bytes; SHA-256 `d9d21f1bfcb2e86e108fb903a796756c8c03fe4fca0e1ae1e453b1ce48253604`.
- Review records: F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0024; title: Docusaurus Renderer; status: draft; version: 0.1.0; authors:; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0024/relations.yaml`

- Source: 77 bytes; SHA-256 `08c821903778ad68716e3663ddb5965036ba35e36e33c1238dec9199863707ce`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0002 /   - ADR-0008 /   - ADR-0011 /   - RFC-0015 /   - RFC-0021

### `foundation/specifications/rfc/RFC-0025/content.md`

- Source: 5729 bytes; SHA-256 `c0954f3fc11b7849f19c63c5753c1e44d750154e61eda4b4f512cc4eacfb8d46`.
- Review records: F72.
- Inspected passage/physical facts: RFC-0025 Canonical Relation Model; Status; Summary; Scope; Relation Domain Object; Supported Serialization Formats; Legacy List Format; Mapping Format; Embedded Relation Object Format; Canonical Representation; Loader Requirements; Verification Requirements; Predicate Semantics; Migration Strategy; Phase 1; Phase 2; Phase 3; Consequences; Future Extensions; References

### `foundation/specifications/rfc/RFC-0025/metadata.yaml`

- Source: 96 bytes; SHA-256 `5ba6ce18acd2820796d89cd305afb7a6ce56f4bd1964f51d734bb03bf8014a84`.
- Review records: F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0025; title: Canonical Relation Model; status: Draft; version: 0.2.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0025/relations.yaml`

- Source: 115 bytes; SHA-256 `d207ac82fb06c273493a612dafdacc5cea7c4eab2fcba2b2cc0605c60dc34339`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0008 /   - ADR-0014 /   - RFC-0029 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0026/content.md`

- Source: 10049 bytes; SHA-256 `684fa191498cb8712aefb82a0688893086e39e6dd33f6e61a9f0baaed3ef0dbc`.
- Review records: F43, F72.
- Inspected passage/physical facts: RFC-0026 — Ontological Predicates; Status; Summary; Scope; Ontological Predicate; Predicate Identity; Predicate Semantics; Source Constraints; Target Constraints; Predicate Direction; Inverse Predicates; Cardinality; Predicate Specification; Semantic Validation; Explicit Relations; Derived Relations; Inferred Relations; Ontology Constraints; Separation of Concerns; Consequences; Design Principle; Future Extensions; References

### `foundation/specifications/rfc/RFC-0026/metadata.yaml`

- Source: 79 bytes; SHA-256 `9aba62948242c9aa7f64c634d2703f4f649de42aac34bb765b8e063ef5573e99`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0026; title: Ontological Predicates; status: Draft; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0026/relations.yaml`

- Source: 115 bytes; SHA-256 `203a3ee28172df6ccc525e66630faf76995a0cc1d0aca96d23f7ebc4dacc24e6`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0014 /   - RFC-0025 /   - RFC-0029 /  / dependsOn: [] /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0027/content.md`

- Source: 14860 bytes; SHA-256 `404dc2e82f3954b042e42543c89687b669dace475e3c7b0793432b6d60a7712b`.
- Review records: F43, F44, F45, F72.
- Inspected passage/physical facts: RFC-0027 — ATON Ontology; Status; Summary; Scope; Ontological Model; Concept Model; AX; Constitution; Predicate; Concept Specialization; Predicate Model; Allowed Source-to-Target Pairs; Initial Predicate Vocabulary; references; motivates; specifies; implements; verifies; governs; defines; allocates; refines; specializes; contains; Predicate Direction; Inverse Predicates; Predicate Identity; Semantic Validation; No Implicit Predicate Inheritance; Cardinality; Explicit Relations; Derived Relations; Inferred Relations; Ontology Evolution; Compatibility; Design Principle; Future Extensions; References

### `foundation/specifications/rfc/RFC-0027/metadata.yaml`

- Source: 85 bytes; SHA-256 `040c3bb2ba671b94370ef3550fbf33f20cdcc358e591e1b4d7fdc6a4eb995776`.
- Review records: F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0027; title: ATON Ontology; status: Draft; version: 0.2.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0027/relations.yaml`

- Source: 123 bytes; SHA-256 `2e66abdfa3f45153d0f380130e95a89ec014b0d527fe7915efad68f6e22323d9`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0026 /   - RFC-0029 /   - ADR-0014 /  / dependsOn: /   - RFC-0025 /  / supersedes: [] / supersededBy: [] / relatedTo: []

### `foundation/specifications/rfc/RFC-0028/content.md`

- Source: 11933 bytes; SHA-256 `62d8e09a94f433933ec595f13d7ab9676335b71a372ccb81e14646377c8628e7`.
- Review records: F56, F57, F72.
- Inspected passage/physical facts: RFC-0028 Relation Migration and Legacy Predicate Resolution; Status; Summary; Scope; Migration Principle; Migration States; Canonical; Inverse; Deprecated; Unresolved; Initial Legacy Classification; references; referenced-by; dependsOn; refines; specializes; governs; children; related; relatedTo; No Automatic Semantic Migration; Migration Decision; Source and Target Validation; External Targets; Migration of External References; Verification During Migration; Valid; Unresolved; Deprecated; Invalid; Unknown; Migration Order; Architecture Board Input; Existing Foundation Relations; Migration Safety; Rollback; Completion Criteria; Consequences; Future Extensions; References

### `foundation/specifications/rfc/RFC-0028/metadata.yaml`

- Source: 107 bytes; SHA-256 `6e4c22c1b97150424ad5d8d4a6ffeb4b80ea6e7c1ea0d6b1b8c323d667c04170`.
- Review records: F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0028; title: Relation Migration and Legacy Predicate Resolution; status: Draft; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0028/relations.yaml`

- Source: 151 bytes; SHA-256 `051d15f621d9c1014bbbb2cfd57244b2b7284feddca6f63655e8a78cc751fbda`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - RFC-0025 /   - RFC-0026 /   - RFC-0027 /   - RFC-0029 /  / dependsOn: /   - RFC-0027 /   - RFC-0029 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0029/content.md`

- Source: 17692 bytes; SHA-256 `30378b3ea62955dfc38d39de864009dee04cb852dce4e97798fd47b1543d0546`.
- Review records: F49, F58, F59, F60, F72.
- Inspected passage/physical facts: RFC-0029 — Canonical Semantic Relation Constraint Model; Status; Abstract; Motivation; Design Principle; Terminology; Predicate; Concept; Allowed Pair; Constraint; Relation Instance; Canonical Constraint Model; Constraint Patterns; Explicit Pair Semantics; No Cartesian Product Semantics; Concept Identity; Relation Evaluation; Unknown Predicate; Unknown Source Concept; Unknown Target Concept; Source Concept Violation; Target Concept Violation; Exact Pair Matching; Type Specialization; Structural and Semantic Verification; Ontology Authority; Separation from the Relation Model; Serialization; Cardinality Constraints; Verification Algorithm; Error Reporting; Migration Strategy; Example; Compatibility; Implementation Boundary; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0029/metadata.yaml`

- Source: 120 bytes; SHA-256 `18eeabfee65d4ec53afc125e83dd92e1b64093ed9e16acef7b83451a22a4d242`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0029; title: Canonical Semantic Relation Constraint Model; entityType: rfc; status: Proposed; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0029/relations.yaml`

- Source: 142 bytes; SHA-256 `2e8a5494d37b69e5f34dc420e826b3d86dd01adb207a32df8f33e4e4044c2b09`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0009 /   - NOTE-0021 /   - RFC-0025 /   - ENTITY-0001 /  / dependsOn: /   - RFC-0025 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0030/content.md`

- Source: 15671 bytes; SHA-256 `63188e61cc93531217b075c97e35c409d43fb68159bfc0ffcf82d67a234d54ba`.
- Review records: F52, F62, F63, F64, F72.
- Inspected passage/physical facts: RFC-0030 Canonical Engineering Artifact Serialization; Status; Abstract; Motivation; Design Principle; Canonical Artifact Representation; Content; Metadata; Relations; Relation Serialization; Empty Relation Collections; Required Components; Optional Content; Optional Metadata; Optional Relations; Identity; Domain Type; Canonical Serialization and Domain Model; Loader Boundary; Determinism; Ordering; Additional Files; Generated Representations; Exchange Formats; Version Control; Validation; Schema; Migration; Compatibility; Consequences; Positive; Negative; Out of Scope; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0030/metadata.yaml`

- Source: 132 bytes; SHA-256 `0975cc13914dd7f5e0e0c782067be449e70778cb757dc4d3daf447bfcc48dd13`.
- Review records: F52, F47, F53, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0030; title: Canonical Engineering Artifact Serialization; entityType: rfc; status: Draft; version: 0.2.0; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0030/relations.yaml`

- Source: 204 bytes; SHA-256 `dfbc13e40a1fcef2ff4fee5dc64a1351f0af139f36214b94e88aa0f102aaf517`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0002 /   - ADR-0005 /   - ADR-0010 /   - ADR-0011 /   - ADR-0013 /   - ADR-0014 /   - RFC-0025 /   - RFC-0029 /   - NOTE-0004 /  / dependsOn: /   - RFC-0025 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/rfc/RFC-0031/content.md`

- Source: 15278 bytes; SHA-256 `9d6048be4c9e5733025fcc85fe9fea6c89ffee925475b11f58857e71aa02ff12`.
- Review records: F72.
- Inspected passage/physical facts: RFC-0031 ATON Markdown Profile; Status; Abstract; Motivation; Design Principle; Canonical Markdown; Document Structure; Headings; Paragraphs; Lists; Emphasis; Code; Links; Images; Tables; Task Lists; Raw HTML; MDX and Embedded Components; Directives and Admonitions; Mathematics; Diagrams; Front Matter; HTML Comments; Escaping; Character Encoding; Line Endings; Whitespace; Deterministic Rendering; Markdown and Engineering Semantics; Markdown and Artifact Identity; Markdown and Traceability; Extensions; Conformance Levels; Core Conformance; Extended Conformance; Rendering Extensions; Validation; Compatibility; Consequences; Positive; Negative; Out of Scope; Acceptance Criteria; References

### `foundation/specifications/rfc/RFC-0031/metadata.yaml`

- Source: 97 bytes; SHA-256 `66d4c69f3affa8d875ead59443fd06b2c03eb3dff51f1dd37a64157066c0c377`.
- Review records: F47, F08, F62, F11.
- Inspected passage/physical facts: id: RFC-0031; title: ATON Markdown Profile; entityType: rfc; status: Proposed; ontologyType: ONT-RFC

### `foundation/specifications/rfc/RFC-0031/relations.yaml`

- Source: 139 bytes; SHA-256 `d1fbe57467699fc1d988eb0977b7a4d92516d761cf2b9a75a53c7848581c4f7f`.
- Review records: F50, F56, F59.
- Inspected passage/physical facts: references: /   - ADR-0002 /   - RFC-0030 /   - NOTE-0003 /  / dependsOn: /   - ADR-0002 /   - RFC-0030 /  / supersedes: [] /  / supersededBy: [] /  / relatedTo: []

### `foundation/specifications/schemas/artifact.schema.yaml`

- Source: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Review records: F66.
- Inspected passage/physical facts: Empty: no executable schema or constraints.

### `foundation/specifications/schemas/entity.schema.yaml`

- Source: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Review records: F66.
- Inspected passage/physical facts: Empty: no executable schema or constraints.

### `foundation/specifications/schemas/metadata.schema.yaml`

- Source: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Review records: F66.
- Inspected passage/physical facts: Empty: no executable schema or constraints.

### `foundation/specifications/schemas/relation.schema.yaml`

- Source: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Review records: F66.
- Inspected passage/physical facts: Empty: no executable schema or constraints.

### `foundation/specifications/templates/adr-template.md`

- Source: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Review records: F66.
- Inspected passage/physical facts: Empty: no content or conventions.

### `foundation/specifications/templates/entity-template.md`

- Source: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Review records: F66.
- Inspected passage/physical facts: Empty: no content or conventions.

### `foundation/specifications/templates/rfc-template.md`

- Source: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Review records: F66.
- Inspected passage/physical facts: Empty: no content or conventions.

### `foundation/tooling/README.md`

- Source: 16 bytes; SHA-256 `452abe7df6c74b7de62ee1f04205bdd5a0fc778ff522289e0aca042bc331e167`.
- Review records: F67, F68.
- Inspected passage/physical facts: # tooling /  / TODO


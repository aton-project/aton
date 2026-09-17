# K1 — Entity, Artifact and Physical Representation

## Status

Draft

## Analysis Type

Engineering Analysis

> This document is an engineering analysis artifact.
> It is non-normative and does not define ATON semantics.

## Decision Under Analysis

For this analysis, the following decision is established by the task:

> ATON SHALL distinguish between Entity, Artifact, and Physical Representation.

This premise is not a claim that all three levels have already been accepted or consistently specified in the repository. This report evaluates the existing sources against that premise. Recommendations below are proposals for subsequent human-governed work, not amendments, acceptance decisions, or new normative requirements.

The working hypothesis is that an Entity is a semantically identifiable unit of engineering knowledge, an Artifact is an independent representation of a state or expression of an Entity, and a Physical Representation is its concrete technical representation or persistence. The hypothesis is tested rather than imposed where it is narrower than the sources.

## Analysis Basis

- Git commit: `7a664c8598ed90c74b9413307411e04e742bf508`.
- Analysis date: 2026-09-17, Europe/Berlin.
- Repository: `/opt/projects/aton`.
- Configured remote: `origin`, `git@github.com:aton-project/aton.git`.
- Branch at analysis start: `development`.
- Working tree at analysis start: clean.
- Method: repository file inspection, reference following, targeted Foundation searches, inspection of metadata and relation sidecars, and a limited static inspection of renderer code. No external sources are required to establish what this repository says.
- Scope limitation: this is a semantic and architectural assessment, not a full implementation conformance audit or a reconstruction of historical acceptance events. Source statements are cited by repository-relative path and exact section heading; those locators refer to the basis commit.

### Sources examined

The following inventory is the complete relevant source set examined. File-set notation is explicit: **C** means `content.md`, **M** means `metadata.yaml`, **R** means `relations.yaml`, and **K** means `constraints.yaml`, each relative to the directory in the table. “Where present” is used only for sets with missing relation sidecars. “Focused” means relevant sections or search excerpts were inspected rather than every paragraph; it does not claim a complete review of those documents. All listed M and available R files in the ADR, RFC, ontology, entity, glossary-term, predicate, and note rows were inspected.

| Directory or exact file | Files and coverage |
| --- | --- |
| `foundation/constitution/CONSTITUTION/` | C, M, R; complete |
| `foundation/specifications/adr/ADR-0001/` | C, M, R; self-hosting |
| `foundation/specifications/adr/ADR-0002/` | C, M, R; Markdown and semantics |
| `foundation/specifications/adr/ADR-0003/` | C, M, R; Git |
| `foundation/specifications/adr/ADR-0004/` | C, M, R; knowledge organization |
| `foundation/specifications/adr/ADR-0005/` | C, M, R; logical components |
| `foundation/specifications/adr/ADR-0006/` | C, M, R; graph |
| `foundation/specifications/adr/ADR-0007/` | C, M, R; Foundation authority |
| `foundation/specifications/adr/ADR-0008/` | C, M, R; domain models and ontology type |
| `foundation/specifications/adr/ADR-0009/` | C focused: Decision, Architectural Separation, Source and Target Semantics, Invalid Relations; M, R |
| `foundation/specifications/adr/ADR-0010/` | C, M, R; metadata ownership and materialization |
| `foundation/specifications/adr/ADR-0011/` | C, M, R; logical/physical boundary |
| `foundation/specifications/adr/ADR-0012/` | C, M, R; identity, revision and version |
| `foundation/specifications/adr/ADR-0013/` | C, M, R; Entity/Artifact |
| `foundation/specifications/adr/ADR-0014/` | C focused: Decision, Predicate Semantics, Semantic Validation and related sections; M, R |
| `foundation/specifications/adr/ADR-0015/` | C, M, R; contextual Entities |
| `foundation/specifications/adr/ADR-0016/` | C focused: Inputs and Outputs and artifact/entity references; M, R |
| `foundation/specifications/adr/ADR-0017/` | C, M, R; decision lifecycle |
| `foundation/specifications/adr/ADR-0018/` | C focused: Navigation Target, Navigation Path and representation references; M, R |
| `foundation/specifications/entity/ENTITY-0001/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0000/` | C, M, R; document conventions |
| `foundation/specifications/rfc/RFC-0001/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0002/` | C, M, R; identity requirements, scope, migration and open questions |
| `foundation/specifications/rfc/RFC-0003/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0004/` | C focused: Engineering Relation, Source, Predicate, Target and semantic references; M, R |
| `foundation/specifications/rfc/RFC-0005/` | C focused: Property Name, Value, Ownership, Semantics, Canonical Properties; M, R |
| `foundation/specifications/rfc/RFC-0010/` | C, M, R; complete, central evidence |
| `foundation/specifications/rfc/RFC-0011/` | C focused: artifact directories/files, metadata, paths, discovery, validation, Git, migration; M, R |
| `foundation/specifications/rfc/RFC-0012/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0013/` | C, M, R; baseline definition, membership, reproducibility, versions, revisions, provenance, migration |
| `foundation/specifications/rfc/RFC-0014/` | C focused: Navigation Target and identity/version/representation references; M, R |
| `foundation/specifications/rfc/RFC-0015/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0020/` | C focused: Ontology, Concept Identity, Ontology Type, Entities, Artifacts, Versioning, Persistence; M, R |
| `foundation/specifications/rfc/RFC-0021/` | C focused: View, View Identity, View and Physical Representation, Derived Information; M, R |
| `foundation/specifications/rfc/RFC-0022/` | C focused: Collection, Identity, Membership and representation/version references; M, R |
| `foundation/specifications/rfc/RFC-0023/` | C focused: Traceability, Explicit Traceability, Semantic Traceability, graph and version references; M, R |
| `foundation/specifications/rfc/RFC-0024/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0025/` | C: relation object, serialization, normalization, verification, predicate semantics; M, R |
| `foundation/specifications/rfc/RFC-0026/` | C focused: Summary, Scope, Ontological Predicate, Identity, Semantics; M, R |
| `foundation/specifications/rfc/RFC-0027/` | C, M, R; taxonomy and predicate vocabulary |
| `foundation/specifications/rfc/RFC-0028/` | C focused: Summary, Scope, Migration Principle, Migration States; M, R |
| `foundation/specifications/rfc/RFC-0029/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0030/` | C, M, R; complete |
| `foundation/specifications/rfc/RFC-0031/` | C, M, R; complete |
| `foundation/specifications/ontology/` | C, M, R where present for every concept named below |
| `foundation/specifications/glossary/TERM-Entity/` | C, M, R |
| `foundation/specifications/glossary/TERM-Artifact/` | C, M, R |
| `foundation/specifications/glossary/TERM-Relation/` | C, M, R |
| `foundation/specifications/glossary/TERM-Predicate/` | M, R; inventory/reference inspection only |
| `foundation/specifications/glossary/README.md` | Terminology authority and identity |
| `foundation/specifications/predicates/governs/` | C, M, R, K |
| `foundation/specifications/predicates/motivates/` | C, M, R, K |
| `foundation/specifications/predicates/references/` | C, M, R, K |
| `foundation/specifications/predicates/refines/` | C, M, R, K |
| `foundation/specifications/ax/AX-0001/` through `AX-0010/` | Focused search of C and metadata for artifact, identity, version and representation language; AX-0010 C read completely |
| `foundation/specifications/schemas/artifact.schema.yaml` | Inspected; empty |
| `foundation/specifications/schemas/entity.schema.yaml` | Inspected; empty |
| `foundation/specifications/schemas/metadata.schema.yaml` | Inspected; empty |
| `foundation/specifications/schemas/relation.schema.yaml` | Inspected; empty |
| `foundation/specifications/templates/adr-template.md` | Inspected; empty |
| `foundation/specifications/templates/entity-template.md` | Inspected; empty |
| `foundation/specifications/templates/rfc-template.md` | Inspected; empty |
| `foundation/README.md`, `foundation/specifications/README.md`, `foundation/book/README.md` | Orientation and documentation status |
| `engineering/notes/NOTE-0004/`, `NOTE-0006/`, `NOTE-0008/`, `NOTE-0009/`, `NOTE-0011/`, `NOTE-0012/`, `NOTE-0014/`, `NOTE-0017/`, `NOTE-0020/` | C, M, R; historical analysis, not normative authority |
| `tooling/docusaurus-renderer/README.md` | Renderer usage |
| `tooling/docusaurus-renderer/model.py` | Artifact and Relation dataclasses |
| `tooling/docusaurus-renderer/loader.py` | Focused: `load_artifact`, `load_foundation`, normalization-related code |
| `tooling/docusaurus-renderer/verification.py` | Focused: `resolve_concept` and constraint-pattern matching |
| `tooling/docusaurus-renderer/artifact_repository.py` | Artifact lookup and concept/predicate selection |
| `tooling/docusaurus-renderer/knowledge_model.py` | Loaded model container |
| `tooling/docusaurus-renderer/writer.py` | Destinations, generated front matter and output |
| `CONTRIBUTING.md` | Repository contribution guidance; not treated as Foundation semantics |

The exact ontology directory names examined under `foundation/specifications/ontology/` are: `ADR`, `AX`, `Artifact`, `Collection`, `Component`, `Constitution`, `Decision`, `Definition`, `Entity`, `Finding`, `GlossaryEntry`, `Interface`, `Metadata`, `Note`, `Predicate`, `Property`, `RFC`, `Relation`, `Requirement`, `Review`, `Test`, `Thing`, and `View`. Each contains C and M; R is absent for `AX` and `Constitution`. The required Entity and Artifact ontology directories both have all three files. A repository inventory found no Physical Representation glossary entry or ontology directory.

### Source authority and interpretation

The Constitution identifies itself as the highest architectural document (Article VI, Section 3). ADR-0007 identifies the Foundation as the normative knowledge base; this does not establish that every proposed text has been accepted. ADR-0001 establishes self-hosting, making discrepancies in the Foundation's own metadata and relations relevant evidence.

The required-source status observations are:

| Sources | Recorded status |
| --- | --- |
| Constitution; ADR-0004 | `accepted` in metadata; ADR-0004 also says Accepted in content |
| ADR-0008; ADR-0009 | Accepted |
| ADR-0010, ADR-0011, ADR-0012, ADR-0013 | Proposed in metadata |
| ENTITY-0001; ONT-Entity; ONT-Artifact; TERM-Entity; TERM-Artifact | Draft |
| RFC-0001; RFC-0010; RFC-0012; RFC-0013 | Draft |
| RFC-0015; RFC-0029; RFC-0030; RFC-0031 | Proposed |

ADR-0017, itself Proposed, explicitly says a Proposed decision has not become accepted and should not be treated as authoritative absent another governance mechanism (`content.md`, Proposed and Accepted). It corroborates the distinction but is not used to manufacture an accepted lifecycle rule. This analysis reports normative wording in drafts as **documented requirements in draft/proposed sources**, not proof of accepted conformance obligations. No acceptance or supersession is inferred from Git presence, ordering, titles, or the task premise.

## Executive Summary

The Foundation substantially supports the three-level decision. The strongest evidence is **explicit**, not merely implicit: RFC-0010 defines a logical Engineering Artifact, distinguishes it from both Entity and Physical Representation, gives it representation-independent semantic identity, and permits several physical representations of the same Artifact. RFC-0030 explicitly places Entity and Artifact on the logical side and the directory plus its three files on the physical side.

The architecture is nevertheless not semantically closed. ADR-0013 establishes only the Entity/Artifact distinction in its Decision and protects Entity identity through physical changes without equally specifying continuity of Artifact identity. Its “physical or addressable” Artifact wording, reproduced in ONT-Artifact and TERM-Artifact, overlaps with the third level. These texts do not explicitly equate every file with an Artifact; most of that mismatch is ambiguous terminology or an incomplete definition, rather than a proven logical contradiction.

More substantive conflicts concern universal Entity scope, relation endpoint scope, metadata ownership, and the interpretation of ontology types. ENTITY-0001 treats every engineering object as an Entity; RFC-0010 permits logical Artifacts without an automatically corresponding Entity. Entity-only relation definitions coexist with explicitly Artifact-capable definitions. Some older wording treats metadata as exclusively describing Artifacts; later sources assign ownership to the logical object described. These cannot safely be resolved by renaming files or fields.

The proposed mappings for Engineering Identity and Engineering Version are well supported at the Entity level. Artifact Identity belongs to the logical Artifact in RFC-0010. Artifact Revision is explicitly broader than an exclusively logical change: it can revise an Artifact **or its physical representation**. Git commits are technical revisions and provenance, not automatically Artifact Revisions or Engineering Versions. `ontologyType` denotes semantic classification, but its owner is not consistently disambiguated between Entity and Artifact.

The example Requirement Entity → Requirement Artifact → three files is a valid illustrative case, not the universal cardinality model. Sources allow an Artifact to describe several Entities, provide evidence, or organize knowledge without one corresponding Entity; Physical Representation also covers other canonical knowledge and generated views. Neither UUID adoption nor a separate mandatory technical identifier for every physical representation is established.

## 1. Existing Semantic Model

### 1.1 Semantic knowledge, logical representation and technical representation

Documented statements establish three related distinctions:

1. The Constitution separates semantics from representation and implementation (Article III, Principles 1 and 7).
2. ADR-0004 separates Engineering Entities, their canonical Artifacts, and presentation Views (Decision and Rationale).
3. RFC-0010 separates Entity, logical Artifact and Physical Representation (Summary; Engineering Artifact; Multiple Physical Representations; Physical Representation).

ADR-0011 and RFC-0015 additionally distinguish the logical Engineering Knowledge Model from the **canonical domain representation used by kernel components**. This is an implementation boundary, not evidence that the requested three levels should be replaced with “logical model / in-memory model / file.” Entity and Artifact are logical concepts; canonical domain objects express them for processing.

“Physical” is broader than a filesystem object. RFC-0010 and RFC-0015 include APIs, exchange documents, generated documentation, rendered views and caches. A Physical Representation need not be durable or independently managed as an Artifact.

### 1.2 Entity model responsibilities

`foundation/specifications/entity/ENTITY-0001/content.md`, Definition through Relationships, assigns Entity identity, conceptual type, content, metadata and applicable Entity relationships. Its content is engineering knowledge; metadata describes identification, lifecycle, classification and processing. The representation of content is explicitly independent of identity.

`foundation/specifications/rfc/RFC-0001/content.md`, Engineering Entity, Entity Identity, Entity and Version, and Canonical Domain Representation, further assigns semantic meaning, canonical addressability, ontology classification, continuity across versions, graph participation and persistence-independent processing to Entities. Contextual ownership is semantic where defined; physical containment alone is not (`Entity Containment`; ADR-0015, Context Relationship).

Analytical conclusion: Entity content, metadata and relations are logical properties or connections. Their existence on the Entity level does not make `content.md`, `metadata.yaml` and `relations.yaml` Entity-level objects. A serialized value can describe an Entity while residing in a Physical Representation of an Artifact.

### 1.3 Hypothesis assessment

| Hypothesis | Assessment against the sources |
| --- | --- |
| Entity = identifiable engineering knowledge | Supported. “Smallest” in ENTITY-0001/glossary needs contextual interpretation, not physical granularity. |
| Artifact = independent representation of an Entity state/expression | Supported as a case, too restrictive as an exhaustive definition: RFC-0010 permits evidence, organization of information, multiple Entities and information belonging to multiple Engineering Versions over its lifecycle. |
| Physical Representation = technical persistence of an Artifact | Supported as a case, too restrictive if persistence or Artifact mediation is mandatory: RFC-0010 also says “other canonical engineering knowledge”; RFC-0015 includes exchange and presentation. |
| Exactly one Entity → one Artifact → three files | Valid example only. ADR-0013 prohibits assuming one-to-one Entity/Artifact correspondence; RFC-0010 permits multiple physical representations. |
| An Artifact is an immutable Entity snapshot | Not established. Artifact identity persists across revisions; precise binding between revisions and Entity versions remains open. |

The three-level distinction does not, by itself, establish disjoint ontology classes, universal containment, minimum cardinalities, or a mandatory representation chain for every model object.

## 2. Evidence Supporting the Three-Level Model

| Evidence | Precise source | Documented statement and analytical significance |
| --- | --- | --- |
| S1 | `foundation/constitution/CONSTITUTION/content.md`, Article I Section 3; Article III Principles 1 and 7 | Semantics are independent of persistence and implementation. Supports the boundary, but does not name all three concepts. |
| S2 | `foundation/specifications/adr/ADR-0004/content.md`, Decision; Alternatives Considered / File-Centric Organization | Entities organize knowledge; Artifacts represent Entities and are uniquely identifiable and independently versionable; files are implementation artifacts. Supports a logical representation level without defining its complete identity contract. |
| S3 | `foundation/specifications/adr/ADR-0005/content.md`, Decision | Content, metadata and relationships are independent **logical components** of one Artifact. Three logical components need not imply three independently identified Artifacts. |
| S4 | `foundation/specifications/adr/ADR-0008/content.md`, Decision and Consequences | External serialization is normalized at the boundary; kernel components use canonical domain models. Supports separation from technical persistence. |
| S5 | `foundation/specifications/adr/ADR-0011/content.md`, Logical Engineering Knowledge; Physical Representations | Entities and Artifacts are included in the logical model; Markdown, YAML, Git, APIs and rendered views are physical representations. Strong complementary support to ADR-0013. |
| S6 | `foundation/specifications/adr/ADR-0013/content.md`, Identity; Entity-to-Artifact Relationship; Artifact Components | Engineering identity belongs to Entities; Artifact identity is distinct; the kernel cannot assume one-to-one; components do not automatically become Entities. Establishes the first boundary and protects Entity identity across the second. |
| S7 | `foundation/specifications/rfc/RFC-0010/content.md`, Summary; Engineering Artifact; Artifact Identity | Artifact is explicitly logical and distinct from Entity and physical representation; its semantic identity survives changes of physical mechanism. Direct three-level evidence. |
| S8 | `foundation/specifications/rfc/RFC-0010/content.md`, Multiple Physical Representations; Alternatives / Treat files as Engineering Artifacts | Several physical representations need not create several Artifacts; treating files as Artifacts is explicitly rejected. |
| S9 | `foundation/specifications/rfc/RFC-0010/content.md`, Artifact Metadata | Metadata for Artifact, Entity, Artifact Revision and Physical Representation must remain distinguishable; ownership follows the described concept. |
| S10 | `foundation/specifications/rfc/RFC-0011/content.md`, Artifact Directories; `foundation/specifications/rfc/RFC-0030/content.md`, Canonical Serialization and Domain Model | Directory is a physical Artifact representation; RFC-0030 lists both Entity and Artifact as logical, with directory and three files as physical. |
| S11 | `foundation/specifications/rfc/RFC-0012/content.md`, Engineering Version; Version and Artifact; Version and Git | Entity state, logical Artifact, physical representation and technical Git history are distinguished. |
| S12 | `foundation/specifications/rfc/RFC-0013/content.md`, Baseline and Artifact Revisions; Baseline and Git; Baseline Verification | Artifact Revisions can support reconstruction; commit/tag is not a Baseline; semantic validity differs from technical reconstructability. |
| S13 | `foundation/specifications/rfc/RFC-0015/content.md`, Representation Identity; Export and Rendering | Physical identity may use paths/URIs/storage details; generated output has no automatic semantic authority. |
| S14 | `foundation/specifications/glossary/TERM-Entity/content.md`, Role in ATON; `foundation/specifications/glossary/TERM-Artifact/content.md`, Role in ATON and Persistence Independence | Entity is conceptual and storage independent; Artifact identity differs from Entity identity; physical representation of an Artifact can change. Support is incomplete at the Artifact/Physical Representation boundary. |

These observations support adoption and consolidation of existing work rather than invention of an entirely new architecture. Their status remains as recorded in Analysis Basis.

## 3. Contradictions

### 3.1 Classification rules

An **actual semantic contradiction** means incompatible meanings or requirements for the same subject under the stated reading. A **terminology ambiguity** permits competing readings without proving incompatibility. A **missing definition** leaves a semantic rule undecided. **Missing documentation only** means a rule is already expressed elsewhere but a local explanation or reference is absent. A draft/accepted conflict is reported as a textual conflict, not as two equally accepted obligations.

### 3.2 Findings requiring semantic resolution

| ID | Classification | Evidence and conflict | Consequence |
| --- | --- | --- | --- |
| C1 | Semantic scope conflict under the universal reading; unresolved taxonomy | ENTITY-0001, Purpose/Definition, and ONT-Entity, Definition, say every engineering object represented by the Foundation is an Entity. RFC-0010, Engineering Artifact and Artifact and Entity Representation, makes Artifacts logical engineering representations and says existence of an Artifact does not automatically imply a corresponding Entity. | If “every engineering object” includes logical Artifacts themselves, universal Entity membership conflicts with treating them as an independently existing non-Entity category. A narrower meaning of “engineering object,” or a distinction between an Artifact and an Entity *about* that Artifact, can reconcile the texts, but neither is specified. Mere conceptual distinction does not prove disjointness. |
| C2 | Actual endpoint-domain conflict if Entity excludes Artifact | ONT-Relation and TERM-Relation, Definition, define Entity-to-Entity connections; RFC-0029, Relation Instance and Relation Evaluation, also requires Entities. RFC-0010, Artifact and Relations, permits Artifact-to-Artifact and mixed relations; ADR-0014, Decision, explicitly permits an Artifact or Entity owner. | With distinct endpoint domains, the Entity-only definition excludes permitted logical Artifact relations. If Entity is a supertype, the conflict changes into C1's missing taxonomy. The report does not decide that taxonomy. |
| C3 | Actual metadata ownership conflict under an exclusive reading; otherwise ambiguity | ADR-0005, Decision, says metadata SHALL describe Artifacts and SHALL NOT contain engineering knowledge. ENTITY-0001, Metadata, and ONT-Metadata, Definition, describe Entity metadata; ADR-0010, Canonical Metadata/Metadata Ownership, and RFC-0010, Artifact Metadata, include semantic properties and multiple owners. | Reading all metadata as Artifact-owned conflicts with Entity-owned or representation-owned properties. Reading “engineering knowledge” in ADR-0005 as primary authored content avoids the broader prohibition, but the wording needs narrowing. ONT-Metadata is correspondingly too narrow for the expanded model. |
| C4 | Actual textual type-requirement mismatch | ENTITY-0001, Definition/Type, requires exactly one conceptual/primary type; RFC-0001, Entity Type, says an Entity MAY have an applicable semantic type. | The universal requirement is stronger than the RFC's optional formulation. They can coexist only if the RFC is expressly subordinate or “applicable” has a qualified meaning; the texts do not explain this. Do not relax mandatory typing through implementation inference. |
| C5 | Actual predicate applicability contradiction, adjacent to the level issue | `foundation/specifications/predicates/references/content.md`, Allowed Pairs, permits only Artifact → Artifact and explicitly no other pair. Its `constraints.yaml` declares `ANY-CONCEPT` → `ANY-CONCEPT`; RFC-0029 defines this as any valid canonical ontology Concept. RFC-0027, references, also lists Artifact → Artifact. | The serialized constraint is broader than the prose. Replacing “artifact” with “entity” would not resolve the conflict. A decision on endpoint meaning and intended applicability is required. |
| C6 | Actual related vocabulary divergence | RFC-0027, governs/refines, lists narrower pairs than `predicates/governs/constraints.yaml` (adds Constitution pairs) and `predicates/refines/constraints.yaml` (adds AX → AX). | Existing semantic revalidation must reconcile authoritative pair sources, independently of introducing the third level. These are not consequences caused by K1, but affect any migration of typing and relations. |

C1 and C2 are deliberately qualified: the sources do not settle whether the ontology categories are disjoint. It would be inaccurate to assert an unconditional contradiction solely because two concepts are called distinct.

### 3.3 Level mixing that is not a proven contradiction

| ID | Classification | Evidence | Required treatment |
| --- | --- | --- | --- |
| A1 | Terminology ambiguity and incomplete Artifact definition | ADR-0013, Decision/Expected Outcome; ONT-Artifact, Definition/Role; TERM-Artifact, Definition, describe Artifacts as persisted, addressable or physical representations. RFC-0010 instead explicitly defines the logical Artifact. | “Persisted or otherwise addressable” can describe a logical object available through an address; it does not necessarily mean file identity. Align the definitions and explicitly protect Artifact identity across physical changes. |
| A2 | Terminology ambiguity | RFC-0001, Entity and Artifact, says “physical or logical representation”; RFC-0002, Identity and Artifact Revisions, says “physical or logical artifacts”; ADR-0013, Traceability, says “physical artifacts.” | Identify whether each occurrence means logical Artifact, physical representation, or an intentionally general representation term. |
| A3 | Missing revision definition, not a denial of the distinction | ADR-0012, Artifact Revision, and RFC-0010, Artifact Revision, include revision of an Artifact or its physical representation. | Decide how physical change is mapped to Artifact Revision; separate identity does not require all revision categories to be disjoint. |
| A4 | Missing identity/type ownership schema | RFC-0030, Canonical Artifact Representation, refers to canonical engineering identity in metadata; Metadata/Identity require Artifact identity. Actual files generally expose a single `id`. | Define how multiple logical identities and their owners are represented. A shared serialized string does not prove conceptual identity equality. |
| A5 | Missing documentation only, where the content already supplies the rule | ADR-0013 and ONT-Artifact have empty relation reference collections despite prose references; TERM-Entity references ENTITY-0001 but not the wider representation model. | Add governed cross-references later; do not treat an empty R file as negating prose semantics. |
| A6 | Historical non-normative contradiction with the current hypothesis | `engineering/notes/NOTE-0017/content.md`, Problem Statement, explicitly groups Engineering Artifacts with files and APIs as physical representations. | Preserve as historical evidence; do not import this old premise into RFC-0010 or silently rewrite the Note as current truth. |

No inspected core source requires the equation Entity = file. ADR-0004's title “Artifact-Based Knowledge Organization” does not contradict its Entity-oriented Decision. Requiring a canonical directory layout also does not make a directory a semantic Artifact.

## 4. Ambiguities

The following terms cannot safely be mapped by word replacement alone:

| Term or statement | Ambiguity |
| --- | --- |
| “Engineering object,” “engineering concept,” “smallest independently identifiable” | Whether Entity is a universal supertype or a specific first-level concept; whether “smallest” excludes compound/contextual Entities. ADR-0015 supports contextual identity without requiring global independence. |
| “Artifact” / “physical artifact” | Logical document/evidence/model, an addressable serialized object, or a loose label for a represented Entity. The intended level varies across RFC-0010, ADR-0013 and the ontology. |
| “Representation itself” in ADR-0013 Identity | Logical Artifact identity or a concrete representation identifier; RFC-0010 supplies the stronger logical reading but ADR-0013 alone does not. |
| “Canonical representation” | Canonical logical semantics, canonical domain object, authoritative persisted data, or canonical serialization profile. These are related but not interchangeable sources of authority. |
| `id` | Often used for lookup of the represented knowledge object; not accompanied by distinct Entity and Artifact identifier slots in the inspected examples. |
| `type`, `entityType`, `ontologyType` | Storage/authoring classification, semantic Entity type, or semantic Artifact type. ADR-0008 explicitly separates classification from ontology identity. |
| `version: 0.1.0` / `version: 1.0.0` | A label exists; no universal rule makes it an Engineering Version identifier, an Artifact Revision identifier, or a physical revision. |
| “content,” “metadata,” “relations” | Logical components or their serialized files. The files do not determine ownership. |
| “Generated artifact” | Independently identified logical Artifact generated by engineering work, or another physical output of the same Artifact. ADR-0013 permits generation but does not give a universal identity test. |
| “View” | Semantic perspective/definition versus rendered output. RFC-0021 explicitly distinguishes these; ONT-View's shorter definition needs that context. |
| “Materialization” | ADR-0010 explicitly promotes derived information into canonical metadata. Using the word for merely writing or caching bytes would conflate a semantic authority operation with serialization. |
| “Provenance” | Can record technical retrieval/transformations or semantic engineering events and reviews; it is not a synonym for Git history or a semantic identity. |

Metadata examples expose a self-description issue: `ENTITY-0001/metadata.yaml` declares `ontologyType: ONT-Entity`, while it is a specification *of* the universal Entity model. Ontology definition artifacts declare their own `id: ONT-*` and `entityType: ontology` but lack `ontologyType`. TERM-Entity and TERM-Artifact instead correctly distinguish the entry's type (`ONT-GlossaryEntry`) from the term being defined. Whether ENTITY-0001's classification is intentional cannot be derived from the field alone.

This is a type-of-definition versus type-defined question, not proof that every such file is wrongly typed. It becomes significant when an ontology definition is itself represented as an Entity or Artifact.

## 5. Identity Model

### 5.1 Ownership and identifiers

| Identity or locator | Supported level | Evidence and limit |
| --- | --- | --- |
| Engineering Identity | Entity | ADR-0013, Identity, is explicit; RFC-0002, Engineering Identity and Identity Identifier, requires stability, scope and non-reuse. |
| Artifact Identity | Logical Artifact | RFC-0010, Artifact Identity, explicitly grants semantic identity independent of physical representation. ADR-0013 only identifies “the representation itself,” leaving this less precise. |
| Engineering Version identity | A particular Entity state | RFC-0012, Version Identity; distinct from stable Entity identity and not solely derived from commit/path/timestamp. |
| Artifact Revision identifier | Revision of the Artifact or its representation | RFC-0010 leaves identification and triggering rules open. No prescribed identifier format was found. |
| Technical Physical Representation identity | Concrete representation/access context | RFC-0015, Representation Identity, permits path, URI, database identity, location or format. No mandatory universal representation UUID is specified. |
| UUID | Identifier mechanism, not an architectural level | RFC-0002, Identity Identifier, permits UUIDs or alternatives; Open Questions leaves standardization open. UUID syntax cannot tell whether a value identifies an Entity, Artifact, revision or storage object. |
| Git commit hash | Technical Git revision/object and provenance | RFC-0002, Identity and Git; RFC-0012, Commit Provenance; RFC-0010, Artifact and Git. A commit may cover many representations and logical objects. |
| Git path | Physical locator, optionally part of provenance | RFC-0011, Repository Paths; RFC-0012, Commit Provenance. It is not an enduring Entity or Artifact identifier. |
| Filename | Local physical name or generated presentation name | ENTITY-0001, Identity; RFC-0010, Artifact Identity; RFC-0031, Markdown and Artifact Identity. `content.md` is repeated across directories and has no global semantic uniqueness. |
| `ONT-*` identifier | Canonical ontology Concept identity | RFC-0029, Concept Identity. This names a semantic category, not the particular Requirement instance classified by it. |

Analytical consequence: a historical Git lookup generally needs a repository context, revision and relevant path or component selection. A path alone does not identify historical bytes; a commit alone does not select one Artifact. This is a retrieval observation, not a proposed mandatory ATON identity tuple. The sources do not define a universal physical identity schema.

### 5.2 What actual metadata proves

The required metadata files contain explicit human-readable IDs such as `RFC-0010`, `ADR-0013`, `ONT-Artifact` and `TERM-Entity`; they do not establish UUID use. Their directory names commonly match those IDs. Equality of names is a persistence convention, not proof that identity is derived from the directory.

RFC-0030 requires Artifact identity in `metadata.yaml` and says canonical engineering identity is defined by Artifact metadata. It does not specify a complete Entity/Artifact identity mapping schema, including compound Artifacts. The four named schemas are empty at the analysis basis and cannot resolve that omission.

A later migration therefore needs a decision on the semantic owner of each legacy ID, alias preservation, scope and references. It would be unjustified to generate new IDs for all files, duplicate every existing ID into two fields, or assume a one-to-one mapping. RFC-0002, Migration, explicitly requires preserving ambiguity where identity cannot be established reliably.

### 5.3 Continuity tests

A path move or serialization conversion does not inherently change Entity identity (ADR-0013) or logical Artifact identity (RFC-0010). Replacing an Artifact with a different logical representation may change Artifact identity while retaining the represented Entity. Changing the engineering concept sufficiently may require a new Entity identity (RFC-0002). The precise criteria for “same Artifact” versus “new Artifact” remain dependent on engineering meaning and applicable ontology; no file comparison decides them universally.

## 6. Version and Revision Model

### 6.1 Documented distinctions

`foundation/specifications/rfc/RFC-0012/content.md`, Engineering Version, explicitly defines an Engineering Version as a distinct semantic state of an Entity. ADR-0013, Versioning, likewise assigns versions to Entities. Thus “primarily Entity” is weaker than these specific sources: they provide an Entity-owned definition, although ADR-0012 uses the broader expression “engineering concept.”

An established Engineering Version is immutable. It may differ in content, metadata, relations, lifecycle state or domain-defined properties. Technical changes that do not change the semantic state need not create a new Engineering Version. Relation state must be interpreted for the relevant version, not read from the latest file and assumed historically valid (RFC-0012, Version Immutability, Version Creation, Versions and Relations).

Artifact Revision is distinct from Engineering Version, but not fully separated from physical change. RFC-0010, Artifact Revision, explicitly covers “an Engineering Artifact or ... its physical representation.” Its next section says conversion between Markdown, exchange format and database may constitute physical or Artifact revisions. Whether a particular change creates an Artifact Revision is delegated to applicable revision semantics, and remains an Open Question.

A Git commit is a technical repository revision, not automatically either semantic version category (RFC-0010, Artifact and Git). RFC-0012 permits one Engineering Version to involve multiple commits and a commit to affect multiple Entities. ADR-0013 permits one Engineering Version to involve multiple Artifact Revisions and one Artifact Revision to affect multiple Entities.

### 6.2 Historical states and examples

| Change or historical event | Supported interpretation | Not derivable automatically |
| --- | --- | --- |
| Rename directory, preserve explicit IDs and values | Physical relocation; identity preserved | New Entity, new Artifact, or new Engineering Version |
| Change line endings without changing Markdown meaning | Technical serialization change; RFC-0031 Line Endings/Whitespace | New semantic version; whether an Artifact Revision is required |
| Change a Requirement's normative constraint | Candidate/new Engineering Version under RFC-0012 Version Creation when semantic state changes | One commit equals one version, or that the Requirement acquires a new identity |
| Revise a document containing several Requirements | Artifact representation change potentially affecting several Entities | All represented Entities necessarily change version |
| Regenerate documentation | Derived physical output; authority remains canonical | New logical Artifact identity or new authoritative state merely because output exists |
| Establish a Baseline | Explicit, reproducible state selection including applicable versions | A Git commit/tag alone proves baseline establishment |
| Rebase/cherry-pick | Changed technical history/provenance | Changed Entity or Engineering Version identity solely from new commit hashes |

RFC-0013, Baseline Membership, requires identifying the applicable Engineering Version when an Entity has several. Artifact Revisions can assist reconstruction but do not replace the semantic selection. Its Baseline Provenance includes not just Git but Artifact Revisions, Engineering Versions, processes, verification and external evidence.

Existing `version` metadata is not sufficient to reconstruct this model. RFC-0012 excludes a mandatory major/minor/patch scheme and leaves labels, branching, equivalence, merging and detailed provenance open. Historical boundaries that cannot be recovered reliably must remain uncertain (RFC-0012 and RFC-0013, Migration). This report's basis commit is provenance for the inspected repository state, not a claim that it is an ATON Engineering Version or Baseline.

## 7. Ontology and Type Identity

### 7.1 What `ontologyType` currently means

ADR-0008, Explicit Ontology Type Identity, requires each participating Artifact to declare exactly one canonical ontology type through `ontologyType`, referencing a canonical Concept identifier. It prohibits inference from path, filename, persistence format or artifact classification. RFC-0020, Ontology Type, repeats the Artifact-oriented ownership wording.

ENTITY-0001 instead requires a primary conceptual type for each Entity; RFC-0001 says its concrete semantic type is determined by the ontology. RFC-0020 explicitly allows ontology concepts for both Entity types and Artifact types, then describes an Entity as an instance of a concept. RFC-0010 separately provides Artifact Type. ADR-0014, Semantic Validation, allows the ontology identity of a participating Artifact **or Entity**.

Therefore the mapping `ontologyType` → semantic typing is supported. The stronger mapping `ontologyType` → exclusively Entity typing is **not established** and is challenged by explicit Artifact-oriented text. Conversely, interpreting it exclusively as Artifact typing cannot explain all Entity relation evaluation without an additional mapping. It is certainly not simply the Markdown/YAML format or a storage directory classification.

### 7.2 Concrete concepts and metamodel levels

ONT-Requirement describes a necessary capability, condition or constraint; ONT-Component describes an identifiable building block; ONT-Interface describes an interaction boundary. These support Entity-oriented concepts. ONT-ADR describes a documented decision; ONT-RFC a formal specification/proposal; ONT-Review, ONT-Finding and ONT-Note explicitly call their subjects Artifacts. ADR-0015 specifically treats meaningful Findings as contextual Entities. The taxonomy does not explain when such names identify engineering concepts versus independently managed representations of them.

RFC-0027, Concept Specialization, gives RFC → Artifact and ADR → Decision as examples, but its Concept Model leaves exact relationships to explicit ontology definition. The inspected ontology R files do not supply a complete specialization graph. These examples cannot be extrapolated into a settled Entity/Artifact inheritance tree.

Three distinct questions must be kept apart:

1. What Concept classifies the represented Requirement or decision?
2. What Concept classifies its logical specification/record Artifact?
3. What identity/type describes the ontology definition object that defines those Concepts?

For example, TERM-Artifact is classified as `ONT-GlossaryEntry`; it defines the word Artifact rather than thereby becoming an instance of ONT-Artifact. ONT-Artifact's own metadata has `id: ONT-Artifact` and `entityType: ontology` with no `ontologyType`. The renderer's `resolve_concept` returns an ontology artifact's own ID. That is an observed implementation convention for resolving the represented Concept, not a normative decision that every Concept is an instance of itself.

### 7.3 Consequences for relation validation

RFC-0029 evaluates source/target Concepts and exact allowed pairs or explicit patterns. It does not infer applicability through specialization. Consequently, reclassifying an existing `ONT-RFC` endpoint as `ONT-Artifact`, or separating an Entity from its record Artifact, can change which relations validate. The `references` prose/constraint conflict demonstrates why this cannot be an editorial substitution.

The required follow-up is to define type ownership and endpoint identity explicitly, including compound Artifacts and ontology-definition objects, then revalidate affected relations. Neither a new field name nor a new type hierarchy is selected here. Semantic classification of a technical representation as an explicitly modeled engineering subject is possible only through an applicable definition; physical existence alone does not confer ontology membership (RFC-0029, Constraint Patterns).

## 8. Artifact and Physical Representation

### 8.1 RFC-0010 is explicit

RFC-0010 already contains substantially the intended Artifact model. Its Summary, Engineering Artifact and Artifact Identity define a logical, semantically identified representation. Multiple Physical Representations explicitly permits several technical representations of the same Artifact. Alternatives rejects treating files as Artifacts. Artifact Metadata distinguishes metadata owners at all relevant levels. These passages are stronger than ADR-0013's protection of only Entity identity across physical changes.

Its remaining gaps are not absence of the three levels. They are the unspecified persistent identifier contract, revision triggers and revision identity, branching/merging, provenance schema, synchronization and authority decisions, and required properties by Artifact type. The Open Questions section acknowledges these. Its question “Which artifact types are required to have persistent identity?” also needs reconciliation with the general Artifact Identity requirement: it may concern persistence of an identifier rather than existence of semantic identity, but this is not explained.

The wording “independent representation” should be interpreted cautiously. A logical Artifact can have its own identity and revisions while containing information about multiple Entities. This does not establish that it is semantically independent of context or complete by itself for reconstructing an Engineering Version.

### 8.2 The three-file structure

```text
artifact/
├── metadata.yaml
├── content.md
└── relations.yaml
```

RFC-0030, Canonical Artifact Representation and Required Components, defines this as the canonical repository representation, with all three files present even when a logical component is empty. Artifact Directories in RFC-0011 explicitly calls the directory a Physical Representation of an Engineering Artifact. RFC-0030's Canonical Serialization and Domain Model explicitly classifies the directory and files as physical.

| Physical component | Serialized role | Logical ownership |
| --- | --- | --- |
| `content.md` | Human-authored engineering content, in canonical Markdown | May express Entity knowledge or Artifact content according to the model; not independently an Entity solely because it is a file |
| `metadata.yaml` | Explicit persisted metadata, including required identity data | Owner is the Entity, Artifact, revision or representation described; current serialization lacks a complete ownership mapping |
| `relations.yaml` | Explicit relations normalized by the loader | Source/predicate/target belong to the semantic model; the file's directory cannot settle ownership for multiple represented Entities |
| `artifact/` | Discovery and grouping in the repository representation | Technical grouping does not define logical identity, containment or cardinality |

Analytical conclusion: together the files constitute a composite Physical Representation of an Artifact in the canonical repository profile. Each is also a physical component representing a logical component. Neither “only content.md is the Artifact” nor “three files necessarily mean three Artifacts” follows from the sources.

RFC-0011, Alternatives / one file per artifact, uses “multiple physical representations” for separated components, whereas RFC-0030 describes their aggregate as one representation. This is a granularity ambiguity, not a contradiction about logical identity. A future definition should distinguish a composite representation, its component files and alternative complete representations.

### 8.3 Canonical profile versus universal semantics

RFC-0030 permits additional files when the domain specification permits them; predicate `constraints.yaml` is a concrete example. Such files do not automatically add new canonical concepts. RFC-0031 limits front matter in the canonical authoring representation, while renderers may generate presentation metadata in output.

The actual Foundation is not uniformly in the complete three-file form: ONT-AX and ONT-Constitution lack R files, and several AX directories also lack them. Older ADR sidecars contain legacy relation keys and the Constitution metadata contains relation-like `parents`, `children`, `references` and `related` fields. These are observed serialization/migration differences against RFC-0030 and RFC-0003, not evidence that files have a different semantic level. RFC-0030 is Proposed; it would be inaccurate to report every missing file as a breach of an accepted universal artifact rule.

No structural migration is necessary merely to express the three-level distinction in prose. Identity, metadata-owner and relation-source serialization changes may later be needed to support cases beyond a single represented object per directory.

## 9. Impact on Existing Foundation Artifacts

“Mandatory” below means a semantic inconsistency or missing contract must be resolved before claiming a coherent three-level specification. It does not authorize edits, require changing every listed file regardless of the selected solution, or imply that this analysis can mandate acceptance. “Likely required” means dependent alignment or revalidation. “Optional/editorial” means existing semantics already support the distinction.

| Priority | Existing artifacts potentially affected | Reason and change class |
| --- | --- | --- |
| Mandatory | `foundation/specifications/adr/ADR-0013/content.md` and its M/R | Explicitly establish both boundaries and Artifact identity continuity, or link to an accepted complementary decision. Semantic/governance work; update status/references only through governance. |
| Mandatory | `foundation/specifications/ontology/Artifact/content.md`; `foundation/specifications/glossary/TERM-Artifact/content.md` | Align the logical Artifact definition with RFC-0010 and distinguish physical realization. Semantic clarification; related R files need corresponding references. |
| Mandatory | `foundation/specifications/entity/ENTITY-0001/content.md`; `foundation/specifications/rfc/RFC-0001/content.md`; `foundation/specifications/ontology/Entity/content.md`; `foundation/specifications/glossary/TERM-Entity/content.md` | Resolve universal Entity scope, meaning of “smallest,” conceptual typing and Entity/Artifact taxonomy. Model decision followed by terminology alignment. |
| Mandatory | `foundation/specifications/adr/ADR-0008/content.md`; `foundation/specifications/rfc/RFC-0020/content.md`; `foundation/specifications/rfc/RFC-0027/content.md` | Resolve owner of `ontologyType`, type-of-definition distinction and concrete type taxonomy. Semantic, not just storage-field renaming. |
| Mandatory | `foundation/specifications/adr/ADR-0012/content.md`; `foundation/specifications/rfc/RFC-0010/content.md` | Clarify Artifact Revision versus physical revision while retaining established Entity Version distinction. Choose ownership, identity and triggers or explicit delegation. |
| Mandatory | `foundation/specifications/rfc/RFC-0030/content.md` with `foundation/specifications/rfc/RFC-0002/content.md` | Define how canonical Entity and Artifact identities are carried and resolved; distinguish engineering identity from representation identity. A schema cannot invent this missing contract. |
| Mandatory | `foundation/specifications/adr/ADR-0005/content.md`; `foundation/specifications/ontology/Metadata/content.md`; `foundation/specifications/rfc/RFC-0003/content.md` | Resolve exclusive Artifact/Entity metadata formulations and ownership across levels, consistent with ADR-0010. |
| Mandatory | `foundation/specifications/ontology/Relation/content.md`; `foundation/specifications/glossary/TERM-Relation/content.md`; `foundation/specifications/rfc/RFC-0029/content.md`; `foundation/specifications/adr/ADR-0014/content.md` | Resolve Entity-only versus Artifact-capable relation scope and source ownership. Coordinate with RFC-0010 and the chosen taxonomy. |
| Mandatory for consistent affected relation semantics | `foundation/specifications/predicates/references/content.md` and `constraints.yaml`; RFC-0027 references definition | Resolve contradictory allowed-pair meanings; retain separation from mere representation links. |
| Likely required | ADR-0009; RFC-0004; RFC-0023; RFC-0025; RFC-0026; RFC-0028, each at `foundation/specifications/{adr,rfc}/<ID>/content.md` | Align owning Entity/Artifact and endpoint resolution with the selected semantic contract; preserve meaning during migration. |
| Likely required | `foundation/specifications/predicates/governs/`, `motivates/`, `refines/` C/M/R/K | Revalidate concrete endpoint types. Resolve governs/refines vocabulary divergence with RFC-0027; no automatic inheritance expansion. |
| Likely required | ADR-0010; ADR-0011; RFC-0015 C/M/R | Their architecture supports the model; add explicit cross-references and distinguish serialization, generation and canonical metadata materialization. No need to replace the boundary principle. |
| Likely required | RFC-0012; RFC-0013 C/M/R | Bind Entity versions and Baseline reconstruction to clarified Artifact revisions/provenance; avoid inventing historical states. |
| Likely required | `foundation/specifications/ontology/ADR/`, `RFC/`, `Decision/`, `Requirement/`, `Component/`, `Interface/`, `Finding/`, `Review/`, `Note/`, `Test/` C/M/R where present | Clarify engineering concept versus document/record/specification and align taxonomy. Findings/Reviews have especially explicit competing Entity/Artifact language. |
| Likely required | `foundation/specifications/ontology/Predicate/`, `Property/`, `Definition/`, `GlossaryEntry/`, `Collection/`, `View/`, `Thing/`, `AX/`, `Constitution/` C/M/R where present | Check universal Entity scope, represented Concept versus definition type, logical View versus output, and scope of property/group membership. Not every definition necessarily needs substantive change. |
| Likely required after semantic decisions | All inspected Foundation M/R files, especially ENTITY-0001 M, ontology M, and Constitution M | Audit owner of `id`, `ontologyType`, `version`, lifecycle and relations. Preserve established references; do not mechanically assign two identities or infer types from directories. |
| Likely required when validation is implemented | `foundation/specifications/schemas/artifact.schema.yaml`, `entity.schema.yaml`, `metadata.schema.yaml`, `relation.schema.yaml` | Empty implementation aids; populate only after semantics are specified. Absence is an enforcement gap, not a competing model. |
| Likely required | ADR-0015; ADR-0016; ADR-0017; ADR-0018; RFC-0014; RFC-0021; RFC-0022 C/M/R | Preserve contextual identity, process inputs/outputs, decision lifecycle, navigation targets, logical views and collection membership when Entity and Artifact resolution diverge. Most boundary principles already fit. |
| Likely required / editorial depending on clarified profile | RFC-0000; RFC-0011; RFC-0031 C/M/R | Qualify physical file conventions and aggregate/component representation terminology; preserve identity-independent Markdown and discovery. |
| Optional/editorial | RFC-0024 C/M/R | Already requires canonical input and output separation; examples may need clearer Entity/Artifact labels. Implementation changes are separate. |
| Optional/editorial | AX-0001 through AX-0010 C/M/R where present | Audit experience wording for original artifact, navigation, search scope, provenance and history. AX-0010 should distinguish engineering evolution from technical revision when presenting both. |
| Optional/editorial | Constitution; ADR-0001; ADR-0002; ADR-0003; ADR-0004; ADR-0006; ADR-0007 C/M/R | Existing semantic independence, self-hosting, representation and graph principles support K1. No Constitution amendment is demonstrated as necessary. Clarify Git's implementation scope or references if needed. |
| Optional/editorial | `foundation/specifications/glossary/README.md`; TERM-Predicate; three templates; Foundation README files | Harmonized references/examples after decisions. Empty templates contain no conflicting definitions to replace. |

Directory notation in this table resolves to the concrete paths in Analysis Basis. The impact is Foundation-wide at the metadata/reference audit level because of self-hosting, but this is not a recommendation to rewrite every artifact. The table covers all existing ADR/RFC identifiers and ontology definitions inventoried for this assessment, distinguishing direct changes from dependent checks.

A Physical Representation glossary addition is required for a self-contained three-term glossary; it is a new terminology artifact for later work, not an existing file to modify in this task. Whether a separate ontology Concept for Physical Representation is necessary remains a semantic decision: mentioning the term does not require every file/cache/API response to become a canonical graph node.

## 10. ADR Assessment

ADR-0013 is **not sufficient by itself** to establish the complete three-level distinction normatively in the repository.

First, its metadata says Proposed. Its existence and normative wording do not demonstrate acceptance. The task establishes an analysis premise, not an acceptance transition for that ADR.

Second, the Decision explicitly distinguishes only Engineering Entity and Engineering Artifact. It defines an Artifact as a persisted/addressable representation. Later sections mention the physical representation of an Artifact, but the guaranteed identity preservation is that of the **Entity**. Artifact identity is described as identity of “the representation itself,” without unambiguously excluding path-, record- or format-bound identity. The Expected Outcome returns to “physical or addressable representations.” It does not define the third level as a separate concept with its own identity role.

Third, its references to ADR-0011 and ADR-0012 provide complementary boundaries and evolution concepts, not the missing Artifact continuity contract in ADR-0013 itself. ADR-0011 includes Artifacts in the logical model; RFC-0010 supplies explicit three-level semantics. Read together they offer strong support, but proposed/draft texts do not demonstrate a fully accepted, harmonized decision set.

The additional semantic decision needed is narrowly identifiable: make the logical Artifact/Physical Representation boundary explicit, preserve logical Artifact identity independently of technical representation changes, define the role and scope of physical representation, and designate the authoritative models for mapping, ownership and revision rules. It should also settle or explicitly delegate the Entity/Artifact taxonomy and type/endpoint questions so that no one-to-one or disjointness assumption is accidentally imposed.

Humans may amend/consolidate ADR-0013 or establish a complementary accepted decision and align its dependents. This report does not select an ADR number, write a new ADR, or decide the governance vehicle. A decision need not specify filenames, UUID algorithms, databases or API designs; those belong to subsequent profiles and specifications.

## 11. Glossary Assessment

TERM-Entity's conceptual, persistence-independent definition is useful, but “smallest” and “every engineering object” need consistency with compound/contextual knowledge and logical Artifacts. Its reference to ENTITY-0001 explicitly avoids replacing the normative model. Adding wording without first settling Entity scope would create a competing definition.

TERM-Artifact distinguishes Entity identity and permits multiple Entity/Artifact mappings. Its persistence section protects Entity identity, not explicitly Artifact identity, across technical transformations. It should align with the logical Artifact definition in RFC-0010 and make clear that a file is a representation of that logical Artifact rather than its semantic definition. It should not narrow Artifacts to a single Entity state when RFC-0010 permits broader information organization.

There is no `TERM-PhysicalRepresentation` (nor another Physical Representation entry) in the inventoried glossary. RFC-0010, Physical Representation, and RFC-0015, Physical Representation, already provide substantive definitions. The glossary therefore has a **missing entry**, not a complete absence of the concept from ATON. A later entry should cover persistence, exchange and presentation, distinguish technical identity, and address composite/component granularity without inventing a mandatory ontology object for every representation.

The glossary README requires exactly one normative definition per term and prohibits redefinition by specifications. The existing glossary/model role statements should be coordinated with that rule: repeated summaries need a clear authoritative source rather than competing independent definitions.

Additional glossary coverage is likely useful for Engineering Identity, Artifact Identity, Engineering Version, Artifact Revision, serialization, materialization, canonical domain representation and provenance. However, Artifact Revision and materialization distinctions should be resolved in their models before glossary text claims a settled interpretation. Git commit/path and filename need only cross-references or implementation explanations unless ATON intentionally standardizes their technical usage.

## 12. Tooling and Serialization Implications

### 12.1 Documented architecture

ADR-0008 and ADR-0011 require normalization into canonical domain representations at the loader boundary. RFC-0030 specifies loading the three files, validating physical structure and constructing canonical domain objects. RFC-0024 requires the Docusaurus renderer to consume canonical engineering knowledge and permits physical information only for presentation/provenance without redefining semantics.

Thus a coherent implementation must retain the meaning and owner of identity/type/relation information across loading and export. If several Entities are represented by one Artifact, source resolution cannot rely solely on the enclosing directory. If several physical representations refer to one Artifact, loading both cannot automatically create two logical identities. These are logically necessary consequences of the documented cardinalities; no particular class hierarchy or database schema follows.

Docusaurus output is a Physical Representation. RFC-0030, Generated Representations, and RFC-0015, Export and Rendering, do not make generated output authoritative merely by existence. RFC-0021 further distinguishes a logical View definition from the physical page that displays it. The three-level decision does not require replacing Docusaurus, introducing a new renderer, or promoting each generated page to a new Artifact.

### 12.2 Limited implementation evidence

The inspected renderer code shows partial architectural support and important representational limits:

- `tooling/docusaurus-renderer/model.py`, `Artifact`, combines `id`, classification `type`, `ontology_type`, title/status, content, metadata and relations with `source_dir` and file paths. There are no separate Entity, Artifact Revision or Physical Representation objects in this file. Keeping technical data on a loaded object is not inherently a semantic violation; the unresolved issue is whether one identity slot can represent the required multiple owners.
- `loader.py`, `load_artifact`, constructs one Artifact for each metadata directory, reads the content and optional relations, takes `ontologyType` explicitly, and falls back from missing `id` to the directory name. The fallback is unsafe as canonical semantic identity under RFC-0002/RFC-0010/RFC-0030; it may serve a migration/discovery role only if distinguished from an established identity. This is static evidence, not a claim that a missing-ID case was executed.
- The same loader uses a path-based `determine_type` result separately from `ontology_type`. Path-based presentation classification is permitted in principle; it must not substitute for ontology semantics. The inspected code does keep separate fields.
- `knowledge_model.py` contains a list of Artifacts; `artifact_repository.py` looks them up by one ID and recognizes ontology definitions by `entityType: ontology`. This is insufficient evidence of a complete many-Entity/many-Artifact mapping mechanism. It does not prove that no other repository component could provide one.
- `verification.py`, `resolve_concept`, returns the explicit ontology type for normal Artifacts and the own ID for ontology definition artifacts. This reveals the concept-definition/instance issue discussed in Section 7. Tool behavior cannot settle its normative semantics.
- `writer.py`, `destination` and `render_markdown`, generates output paths from loaded IDs/types and generates title front matter. Such presentation metadata is distinct from canonical authoring metadata. Its existence is not a conflict with RFC-0031's prohibition on canonical front matter.

No renderer was run for this analysis because its writer deletes and regenerates `book/docs/generated`; that would create unrelated output changes. No runtime compliance verdict is claimed. A later implementation task should test identity continuity across moves/conversions, one Artifact represented in multiple formats, compound Artifacts, relation-owner resolution, historical version retrieval and ambiguous legacy migration after the semantic contracts are resolved.

### 12.3 Serialization, materialization and provenance

**Serialization** maps logical information to a technical persistence/exchange form (RFC-0010, Artifact Serialization; RFC-0015, Canonical Serialization and Representation). It should preserve semantics, with the declared profile governing deterministic structure. The canonical three-file format is a physical profile, not the complete semantic model.

**Materialization**, as specifically documented in ADR-0010, is an explicit operation that makes derived information canonical metadata, after which normal semantic and persistence rules govern it. A cache refresh, generated HTML page or merely saving derived data does not automatically perform that operation. Whether ATON also wants a separately named technical materialization operation is open; no such broader normative meaning is assumed here.

**Provenance** spans multiple levels. RFC-0015 records transformations, sources, tools, imports/exports and technical revisions for physical representations. RFC-0012 allows activities, reviews and verification evidence for Engineering Versions. RFC-0013 uses several kinds of evidence for reproducibility. Git is one provider. Provenance must identify what it describes and cannot silently become semantic identity, version boundaries or authority.

Git-based persistence remains compatible with K1. ADR-0003 requires Git for the Foundation; RFC-0012 and RFC-0013 describe Git as the current Foundation implementation's canonical version-control system while retaining model independence. Constitution-level technology independence is best reconciled by keeping the Foundation repository profile separate from universal model semantics. No switch away from Git is required by the distinction.

## 13. Open Semantic Questions

| ID | Question not unambiguously settled by the sources | Why it matters |
| --- | --- | --- |
| Q1 | Is Entity a universal supertype of all semantic objects, a separate disjoint category from Artifact, or a role that can coexist with Artifact identity? | Determines ontology membership, relation endpoints and interpretation of ENTITY-0001. Distinguishing concepts alone does not decide this. |
| Q2 | Can an Artifact exist without representing any particular Entity, and what is the minimum representation relationship? | RFC-0010 permits information organization without a corresponding single Entity; the hypothesis is narrower. |
| Q3 | Must every Physical Representation mediate through an Artifact, or may it represent other canonical knowledge directly? | RFC-0010/RFC-0015 support the broader scope; a strict chain would be a new restriction. |
| Q4 | What preserves Artifact identity across replacement, generation, translation, splitting or merging? | RFC-0010 gives a semantic principle but not domain-independent decision criteria. |
| Q5 | Does Artifact Revision identify logical Artifact state, physical state, or an explicitly mapped combination? | Needed for migration, version comparison, synchronization and historical retrieval. |
| Q6 | How are Entities, Artifacts, their versions/revisions, physical representations and ontology definition objects identified in canonical metadata? | Existing `id` and empty schemas do not specify all these owners or their scopes. |
| Q7 | Which concept owns `ontologyType`, and how are both Entity and Artifact classification expressed when needed? | A compound Artifact cannot transfer one document type to all its represented Entities. |
| Q8 | Which canonical relation endpoints are permitted, and how is source ownership represented inside compound Artifacts? | Entity-only definitions conflict with broader Artifact-capable models. |
| Q9 | What constitutes one complete Physical Representation versus its components or an alternative representation? | Three files form an aggregate but are also physical components; synchronization and identity need a defined granularity. |
| Q10 | Which representation is authoritative for which properties, and how are conflicts or lossy transformations handled? | Persistence or successful rendering alone does not confer authority. |
| Q11 | How are Artifact Revisions bound to Engineering Versions and Baselines, including historical relations and cross-repository data? | Technical history alone cannot reliably establish semantic boundaries. |
| Q12 | Which existing `version` fields are labels, normative state identifiers or legacy metadata? | A version-shaped string is not a defined identity contract. |
| Q13 | Should technical representations be explicitly modeled as typed graph subjects, and when? | Physical existence need not create a new Entity or Artifact; provenance may still need addressability. |
| Q14 | Which predicate source is authoritative where prose and `constraints.yaml` disagree? | Exact semantic validation cannot choose silently between incompatible pairs. |
| Q15 | What governance action makes the aligned decision set accepted, and how are supersession/dependencies recorded? | Proposed/draft files and empty relation sidecars cannot prove normative closure. |

## 14. Proposed Change Strategy

1. **Review this analysis as a preserved initial result.** Confirm or correct evidence classifications and scope. Keep the established three-level premise separate from still-open cardinality, taxonomy and ownership choices.
2. **Resolve the smallest semantic contracts first.** Decide Q1–Q8 and the authority/revision boundaries needed for a coherent model. Consolidate ADR-0013 with ADR-0011/RFC-0010 through the chosen governance mechanism; do not draft policy indirectly through schema or code.
3. **Align Entity, Artifact and Physical Representation definitions.** Reconcile ENTITY-0001, RFC-0001, RFC-0010, ontology and glossary. Add the missing Physical Representation glossary coverage; preserve broader Artifact and representation cases unless an explicit decision changes them.
4. **Align identity, types, properties and relations together.** Specify owners and references, including self-description and compound Artifacts. Resolve contradictory predicate pair definitions and revalidate affected relations. Do not infer entity-to-artifact or containment relationships from directories.
5. **Clarify evolution and authority.** Specify Artifact Revision identification/triggers and bindings to Engineering Versions and Baselines; distinguish semantic establishment, provenance, regeneration and metadata materialization.
6. **Map the contracts to serialization.** Update RFC-0030 and dependent profiles/schema aids only after logical meanings are clear. Audit actual M/R fields and missing components under the chosen compatibility policy. Preserve legacy aliases and uncertainty where necessary.
7. **Adapt tooling in a separate task.** Implement the agreed normalization, identity resolution, metadata ownership, relation validation and provenance boundaries. Verify supported multi-representation and compound cases without making implementation structures normative.
8. **Complete editorial consistency and governance links.** Align examples, experience wording and cross-references, preserve historical Notes as historical records, and explicitly record acceptance or supersession rather than assuming it from a commit.

The strategy proposes an order of work, not an ATON engineering process mandate. No step above is performed by this analysis artifact.

## 15. Conclusions

The three-level decision is strongly supported by existing Foundation writing. RFC-0010 explicitly establishes the logical Artifact distinction; RFC-0011 and RFC-0030 explicitly identify the three-file directory as a physical Artifact representation. Entity semantics are independently developed in ENTITY-0001 and RFC-0001. Architectural independence and normalization principles provide a compatible foundation.

The decisive gaps are coherence and acceptance, not lack of any three-level model. ADR-0013 alone is incomplete and Proposed; the Artifact glossary/ontology retain broader two-level language. Identity and type ownership, Entity universality, relation endpoints, revision granularity and legacy serialization need explicit resolution. Predicate prose/constraint discrepancies are concrete adjacent semantic conflicts that must not be concealed by a terminology update.

The user mappings are therefore mostly valid with qualifications: Engineering Identity and Engineering Version belong to Entities in the specific models; logical Artifact Identity is separately supported; Artifact Revision still includes physical change; Git supplies technical representation/provenance; `ontologyType` is semantic but its owner remains unresolved; and the three files are physical components of a canonical composite representation. The example must not become an unsupported one-to-one or universally mandatory chain.

No Foundation artifact, glossary entry, ontology definition, ADR or RFC is changed by this document. No new normative artifact or decision is created. The analysis basis identifies the inspected technical repository state, not an accepted semantic baseline.

## 16. Human Decisions Required

The distinction among Entity, Artifact and Physical Representation is already fixed for this analysis and does not require reconfirmation. Human decisions remain necessary for:

- Entity/Artifact taxonomy and permitted representation cardinalities, including Artifacts without a single corresponding Entity and direct representations of other canonical knowledge.
- Stable identity ownership and scopes, legacy-ID continuity, optional UUID standardization, and classification of ontology definition objects.
- Ownership of `ontologyType`, semantic metadata and relation sources/targets across the levels.
- Artifact Revision boundaries, physical revision mapping, version/baseline bindings, and preservation of uncertain history.
- Representation authority, conflict handling, composite/component granularity and explicit canonical metadata materialization.
- Resolution of contradictory predicate prose and constraints, with semantic migration and revalidation where needed.
- The governance vehicle, acceptance status and sequencing for harmonizing the existing Foundation sources.

These decisions should precede dependent schema or tooling choices. This report supplies evidence and a proposed change strategy for that review; it does not decide those questions on behalf of ATON.

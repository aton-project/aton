# Decision and ADR Ontology Analysis

## 1. Purpose, scope and authority

TASK-0007 asks how the generic Decision concept and ADR should relate in the
ATON Foundation. This report evaluates the current definitions, taxonomy,
Entity/Artifact boundary, Predicate contracts and practical consequences. It
does not implement an ontology change.

The governing task intent is that Decision is generic, existing ADRs document
architectural decisions without additional separate Decision instances, and
future specialized decision concepts remain possible. The formal relationship
between Decision and ADR is open. Neither specialization nor a new Predicate
is a starting assumption.

**Recommendation:** explicitly decide that `ONT-ADR` classifies a documented
architectural decision as an Entity-level specialization of `ONT-Decision`,
while its documentary Artifact remains a representation with distinct
identity semantics. Retain one existing ADR Entity and its primary
`ontologyType: ONT-ADR`; do not allocate duplicate Decision instances. This is
a proposed resolution, not an adopted taxonomy or an implemented correction.
The alternative interpretation of ADR as solely a documentary form is viable,
but requires an explicit classification/mapping migration and resolution of
current ADR endpoint and lifecycle semantics.

Full paths are repository-relative; shortened `ontology/` and `predicates/`
paths are relative to `foundation/specifications/`. **Source fact** below means a statement or
observable declaration in the inspected repository; **interpretation** means
an inference from those sources; **recommendation** means a proposed future
choice. Normative wording within a Draft or Proposed source is analyzed as
written without promoting that source to Accepted status.

## 2. Repository state and sources examined

Inspection date: 2026-10-21. Branch: `development`. Basis commit:
`f7b67e48c8889e4707735eb6a737a42b5c63ac03`. The initial working tree and index
were clean. No `AGENTS.md` was found by searching the parent project tree.
Repository contribution guidance and the validation workflow were inspected;
the task's explicit report-only commit and direct push govern this delivery.

| Source | Examined material and relevance |
| --- | --- |
| `foundation/specifications/ontology/{Decision,ADR,Entity,Artifact}/` | `content.md`, `metadata.yaml`, `relations.yaml`: definitions, canonical IDs, classification ownership and actual declarations. |
| `foundation/specifications/ontology/` | Specialization search across all definitions and sidecars; Requirement, RFC and Thing definitions for comparison. |
| `foundation/specifications/entity/ENTITY-0001/` | Content and metadata; Definition, Identity, Type, Relationships and Specialization. |
| `foundation/specifications/rfc/RFC-0010/content.md` | Summary; Proposal: Engineering Artifact, Engineering Entity, Artifact and Entity Representation, Artifact Identity, Artifact Type, Artifact and Relations; Migration and Open Questions. |
| `foundation/specifications/rfc/{RFC-0020,RFC-0027,RFC-0029}/` | Content and metadata: ontology semantics, taxonomy, exact pairs, patterns, evolution and validation. |
| `foundation/specifications/adr/{ADR-0013,ADR-0014,ADR-0017}/` | Content and metadata: representation distinction, canonical relations and architectural-decision lifecycle. |
| `foundation/specifications/adr/ADR-0008/content.md` | Explicit Ontology Type Identity: one primary type; specialization belongs in the ontology. |
| `foundation/specifications/adr/*/metadata.yaml` | Classification census of all 18 existing ADRs. |
| `foundation/specifications/rfc/RFC-0025/content.md` | Relation Domain Object, Canonical Representation and Predicate Semantics. |
| `foundation/specifications/predicates/{motivates,references,governs,refines}/` | Content, metadata and constraints: four concrete Predicate contracts. |
| `engineering/analysis/architecture/Foundation-Semantic-Review.md` | Purpose, ownership model, overall assessment; F08, F14–F15, F19, F39, F43–F49, F52 and F58–F60. Historical review findings checked against relevant current sources. |
| `engineering/analysis/architecture/Foundation-Semantic-Decisions.md` | Purpose and authority; representation analysis; agreed groups 7–8 and documentary assumptions. |
| `engineering/analysis/architecture/Decision-ADR-Relationship-Analysis.md` | Prior TASK-0006 analysis, particularly premises, source inventory, Predicate assessment and recommendation. Historical context only. |
| `tooling/docusaurus-renderer/{loader.py,verification.py,predicate_registry.py,render.py,knowledge_model.py,verification_report.py,README.md}` | Current loading, exact/pattern matching, registry and verification/rendering boundary. |
| `.github/workflows/validate.yml`, `CONTRIBUTING.md` | Practical checks and repository workflow guidance. |

All minimum requested sources exist. A concrete specialization declaration for
ADR under Decision was not found; this is a missing declaration rather than a
missing RFC. A concrete `specializes` Predicate directory is also absent from
the four-Predicate inventory. No new identifier, relation or constraint is
introduced by this report.

## 3. Source facts

### 3.1 The two concepts actually defined

`ontology/Decision/content.md`, Definition, describes an intentional selection
among alternatives together with the resulting determination. Its metadata
declares `id: ONT-Decision`, `entityType: ontology`, `status: Draft` and an empty
references list. Nothing in the definition restricts decisions to architecture.

`ontology/ADR/content.md`, Definition, describes a documented architectural
decision, its rationale and consequences. Its metadata declares
`id: ONT-ADR`, title Architecture Decision Record, `entityType: ontology`,
`status: Draft` and an empty references list. It does not explicitly say
whether the classified object is the decision or its documentary form.

Both concepts' Role in ATON requires consistent interpretation across kernel,
Foundation artifacts and tooling; both cite ENTITY-0001. Their relation
sidecars contain only `references: []`. Neither declares specialization.
Neither concept-definition metadata file has an `ontologyType`; its `ONT-`
identifier identifies the concept and is not a separate Decision instance.

### 3.2 Entity, Artifact and existing ADR usage

ENTITY-0001, Definition and Type, requires stable identity and exactly one
primary conceptual type explicitly declared through `ontologyType`. It names
Architecture Decisions among specialized Entity types. Specialization adds
domain semantics without redefining fundamental identity. ADR-0008, Explicit
Ontology Type Identity, says specialization is represented in the ontology,
not as multiple type values on an Entity.

ADR-0013, Decision, Entity-to-Artifact Relationship and Identity, distinguishes
the logical Entity from its addressable representation. An Entity may have
multiple Artifacts; an Artifact may represent multiple Entities where its
format supports that. Distinct identity meanings may use the same identifier
value in the normal one-Entity/one-Artifact case. A second technical Artifact
ID is not mandatory. Location alone does not establish representation.

RFC-0010 and `ontology/Artifact/content.md` preserve that boundary.
`ontologyType` belongs to the Entity; applicable `artifactType` belongs to the
Artifact, even if serialized together. RFC-0010 explicitly says an Artifact's
existence does not automatically imply a corresponding Entity. Thus the
boundary does not prescribe a separate Decision Entity for every ADR file.

All 18 existing ADR metadata files, ADR-0001 through ADR-0018, declare
`ontologyType: ONT-ADR`. No `ontologyType: ONT-Decision` declaration occurs
under Foundation. ADR-0013 and ADR-0014 metadata status is Draft; ADR-0017 is
Proposed. This report does not treat their presence or publication as proof
of acceptance.

ADR-0017, Context, states that ADRs represent explicit engineering decisions.
Decision and Accepted define the lifecycle of the Architecture Decision
itself, with acceptance independent of the mere existence of an ADR Artifact.
Versioning also speaks of the lifecycle state of an ADR; Relationship to Other
Decisions calls its subject the specific Architecture Decision entity. This
supports an Entity reading of current ADR usage but leaves terminology mixed.
Rejected, Withdrawn and Proposed are meaningful historical states; existence
as a Decision subtype could not imply acceptance or governing authority.

### 3.3 Taxonomy is permitted but not established by an example

RFC-0020, Concept Specialization, permits explicit specialization only when
the specialized concept preserves the parent's semantic meaning while adding
or refining characteristics. Naming, folders, programming inheritance and
physical organization cannot establish it. Ontology Evolution prohibits
silent semantic reinterpretation. Ontology and Engineering Entities
distinguishes concepts from their instances; Ontology and Artifacts separates
Entity classification from Artifact representation.

RFC-0027, Concept Model, says exact relationships, including specialization,
shall be explicitly defined. Concept Specialization gives **examples** of ADR
specializing Decision and RFC specializing Artifact. No Implicit Predicate
Inheritance uses an **if** ADR-specializes-Decision example. RFC-0029, Type
Specialization, likewise uses a conditional example. These passages explain
semantics; they do not settle the taxonomy in the concept definitions.

No `specializ` declaration was found anywhere in
`foundation/specifications/ontology/`. In particular, its empty Decision and
ADR sidecars cannot turn the RFC example into an explicit canonical edge.
Nor does Thing's description as the most general category supply unrecorded
parent declarations.

RFC-0027, Initial Predicate Vocabulary / specializes, separately lists
Artifact → Artifact, Definition → Definition and Entity → Entity pairs for
the `specializes` Predicate. These exact pairs are not a license to connect
any subtype instance or any pair of `ONT-` IDs. The Foundation does not resolve
the concrete representation of the proposed concept-level taxonomy edge.
Its definition artifacts' own instance typing is also incomplete. A future
decision must resolve the representation rather than force an instance
relation through a convenient pair.

### 3.4 Predicate applicability is independent of taxonomy

RFC-0027, Allowed Source-to-Target Pairs, Semantic Validation and No Implicit
Predicate Inheritance, requires complete, explicit pairs. Applicability does
not propagate to specialized or generalized concepts. RFC-0029, Canonical
Constraint Model, Exact Pair Matching and Type Specialization, repeats this:
concrete IDs match exactly; no allowed pairs means no applicability.

RFC-0029, Constraint Patterns, permits explicit `ANY-CONCEPT` in either pair
position. It matches valid canonical concepts, excluding unknown types,
arbitrary strings and unclassified physical artifacts. A declared pattern is
not inheritance or an inferred Cartesian product. Cardinality concerns a
source/Predicate target set, is checked after pair validity, and is unrestricted
where no constraint is defined. None of the four concrete constraint files defines
cardinality.

| Predicate source | Actual allowed pairs (names abbreviate `ONT-` IDs) | Consequence for this analysis |
| --- | --- | --- |
| `predicates/motivates/{content.md,constraints.yaml}` | Note → ADR; Finding → ADR | Meaning refers to contributing to a Decision, but Decision targets are expressly prohibited. Specialization would make that wording easier to interpret without adding a pair. |
| `predicates/governs/constraints.yaml` | ADR → Artifact/Collection; Constitution → Artifact/Collection, each a separate pair | No Decision source. RFC-0027 lists only the two ADR-source pairs. |
| `predicates/refines/constraints.yaml` | Requirement → Requirement; RFC → RFC; ADR → ADR; Component → Component; Interface → Interface; AX → AX | No Decision pair. RFC-0027 omits AX → AX. Refinement between instances is distinct from concept taxonomy. |
| `predicates/references/content.md` and `constraints.yaml` | Prose permits only Artifact → Artifact; YAML declares explicit ANY-CONCEPT → ANY-CONCEPT | A genuine conflicting contract; wildcard acceptance does not establish documentary semantics or an adopted Decision/ADR association. |

RFC-0027 also lists `specifies` as RFC → ADR and the other initial vocabulary
(`implements`, `verifies`, `defines`, `allocates`, `specializes`, `contains`).
None requires duplicate Decision instances or supplies an unambiguous
decision/documentation mapping. Motivation, governance, refinement, reference
and specification express different meanings. The four concrete directories
must be distinguished from the wider RFC vocabulary.

RFC-0027, Ontology Evolution, Compatibility and Design Principle, requires
specified, controlled changes, recognizes pair changes as ontology changes
and favors a small precise vocabulary. It does not require a new Predicate
merely because two concepts need analysis. A taxonomy relationship is not an
authored relation between a Decision instance and a second ADR instance.

### 3.5 Historical analysis and remaining conflicts

The Semantic Review is explicitly analysis, not a normative decision. F39
notes that document vocabulary does not alone impose file identity or adopt
a taxonomy; F43 and F59 affirm exact pairs and classification separation.
F44–F46 record the same Predicate discrepancies and endpoint ambiguities
observed above. F47–F49 discuss typing/representation gaps. F52 records status
conflicts; acceptance must not be guessed by selecting one source silently.

The Semantic Decisions record, Purpose and authority, explicitly says it
does not amend Foundation specifications. Group 7, clarifications 1–4, treats
Decision as an independently identified Entity and ADR solely as its Artifact,
expressly excluding specialized Decision Entity status. Group 8.7 leaves
documentary cardinality open. That earlier agreed framing conflicts with
current ADR Entity typing and with the possibility now explicitly reopened
by TASK-0007. This report records the conflict without rewriting the record.

The prior Relationship Analysis starts from TASK-0006 premises requiring
separate independently allocated Decision identities and a documentary
association. Its conclusion about the lack of a suitable existing Predicate
answers that narrower premise. TASK-0007 supersedes the separate-instance
requirement, so that conclusion cannot establish that a new Predicate is
necessary here. Prefix, registration and exactly-one association requirements
from that report are not carried into this task. The historical file remains
unchanged.

Other relevant gaps remain even if the taxonomy is resolved:

- RFC-0029, Motivation and Separation from the Relation Model, describes a
  predicate/target object whose source comes from its owner; RFC-0025, Relation
  Domain Object, requires source, predicate and target. ADR-0014 identifies
  relations by the triple but uses artifact-or-entity ownership wording.
  Semantic source reconstruction for compound representations is unresolved
  (Semantic Review F15 and F58). This analysis selects no silent reconciliation.
- RFC-0010, Artifact and Relations, permits Artifact/Entity combinations subject
  to ontology constraints; ADR-0014 semantic validation and RFC-0029 Relation
  Instance use Entity ontology types. Reclassifying ONT-ADR solely as an
  Artifact concept therefore requires an explicit endpoint contract.
- No source establishes a complete generic Decision lifecycle or a formal
  taxonomy serialization contract applicable to this proposed edge. ADR-0017's
  architecture-specific lifecycle should not automatically be imposed on all
  future decisions.

## 4. Interpretation and viable options

The current sources support both a semantic decision reading and a documentary
reading of ADR. Current instance typing, ENTITY-0001 and ADR-0017 favor the
first; the title, representation terminology and earlier decision record
favor the second. The distinction is **formally unresolved**, not an already
adopted subtype hierarchy. The following choices are evaluated against the
task's single existing decision identity requirement.

| Option | Meaning and identity | Existing ADR and extension impact | Constraints, validation and rendering |
| --- | --- | --- | --- |
| A. Explicit ADR specialization under Decision | ADR means a documented architectural decision as a semantic Entity subtype. Its Artifact carries the record. One Entity keeps ONT-ADR as its primary type. | Existing IDs and type values can remain; no extra Decision instances. Future decision kinds may specialize Decision without becoming ADRs. Requires explicit semantic clarification and taxonomy declaration. | Existing ADR exact pairs remain applicable; Decision pairs do not propagate. Taxonomy validation and decision-category navigation need explicit support. Artifact presentation stays distinct from Entity lifecycle and identity. |
| B. Keep ADR solely as documentary concept/form | Decision is the logical subject; ADR classifies its documentary Artifact. Existing ADR identity may continue to identify the already documented decision, with Entity/Artifact identity meanings kept distinct and shared values allowed where appropriate. No second Decision is created. | Requires deliberate remapping of current ONT-ADR Entity classifications to a selected decision classification and an explicit representation contract. Does not follow merely from the folder name or an artifactType value. Future decisions may use different documentation forms. | Existing ADR-source/target pairs cannot silently follow retyped Entities. Must decide whether relations address the decision or record, revise affected pairs/endpoint rules and preserve links. Rendering needs distinct decision and documentary classifications without duplicate results. |
| C. Keep ADR a separate Entity concept without specialization | ADR denotes a managed decision record Entity carrying the architectural decision content; Decision remains a separate generic category with no formal subtype claim. The existing record is the sole identified object for this case. | Preserves IDs and existing ONT-ADR types; requires explicitly stating how the architectural decision is represented without a second Entity. Future Decision specializations remain separate categories. | Existing pairs remain; generic Decision queries cannot include ADR by taxonomy. Reusing decision lifecycle on record Entities needs clarification. A new Predicate does not fix the semantic categorization unless there are distinct meaningful endpoints. |
| D. Defer formal relationship | Preserve the current model pending a decision. | Meets the immediate no-implementation restriction and avoids migration now; leaves classification and future extensions ambiguous. | Exact pairs remain unchanged; tooling must not assume a hierarchy or generic Decision coverage. This is an interim state rather than a resolved ontology. |

An ADR Artifact, understood purely as representation, is not an intentional
selection among alternatives. Specializing that representation under Decision
would violate meaning preservation and the Entity/Artifact boundary. In
contrast, a documented architectural decision includes the selection and
determination plus architectural scope, rationale and consequences. Under
that Entity reading, option A can preserve both definitions. Documentary
requirements refine what knowledge is recorded without making a Markdown
file the decision or making every decision an ADR.

There is a subtle limitation: ADR-0017 includes Proposed, Rejected and
Withdrawn decisions, while Decision's short definition emphasizes a resulting
determination. The explicit architectural decision must clarify that the
decision subject can be proposed or historical and does not imply an accepted
outcome. Otherwise specialization would hide a lifecycle ambiguity rather
than satisfy RFC-0020's meaning-preservation rule.

Option B better separates documentation as an independent classification
axis, particularly if many decision kinds can use the same record form. It
does not require duplicate Entities: one existing documented decision can
retain semantic identity while its representation is classified separately.
However, present ONT-ADR typing is Entity-owned, so treating it as already
an artifactType would contradict the explicit current declarations. The
necessary type choice, mapping, endpoint semantics and migration cannot be
invented in this analysis. General Entity-to-Artifact representation may be
the appropriate mechanism; an ordinary Predicate is not automatically needed.

Option C is possible if a record is independently managed semantic knowledge,
but needs more explanation of how a category defined as a documented
architectural decision excludes Decision taxonomy. It also makes generic
decision discovery depend on a separately specified categorization rule.
Creating a separate Decision Entity just to connect it to that record would
violate this task's agreed intent and is excluded from all options.

## 5. Recommendation and consequences

Recommend **option A**, subject to an explicit architectural decision on its
Entity meaning and lifecycle compatibility. It most directly fits the actual
ADR definition, current ONT-ADR classifications, ENTITY-0001's Architecture
Decision type and ADR-0017's lifecycle subject. The RFC-0027 example is useful
supporting evidence for feasibility, not evidence of adoption. The decisive
reason is semantic fit with a documented decision and preservation of existing
identity, rather than a desire to obtain Predicate inheritance.

Decision remains generic. ADR adds architectural scope and documented rationale
and consequences. A future specialized decision need not use an ADR record,
inherit ADR lifecycle rules, or receive a second Entity identity. Whether
documentation form should eventually become an independent classification
axis remains a legitimate future question; it should not be silently encoded
as a new concept or field here.

For existing ADRs, the intended outcome is one semantic decision identity
represented by its current record. Keep exactly one primary `ontologyType`;
do not add ONT-Decision as a second type. Artifact identity, revisions and
physical rendering remain distinct from Entity identity, Engineering Versions
and decision lifecycle. Normal shared identifier values are compatible with
ADR-0013 and do not mean the two identity concepts are equal. This does not
impose universal one-Entity/one-Artifact cardinality.

For relations, adding the taxonomy alone would preserve existing exact ADR
pairs and would authorize no additional Decision or future subtype pairs.
Any future applicability expansion must be specified explicitly, with
revalidation where constraints change. Existing references and catalogue
contradictions remain independent issues; this recommendation does not cure
them. No new Predicate is needed to link two copies of the same decision.

For validation, future work would need to check explicit taxonomy references,
meaning preservation, cycles and primary typing according to an approved
taxonomy contract. These are proposed validation needs, not claims of existing
constraints. Current `verification.py`, `matches_constraint`, implements
exact IDs and explicit patterns, not specialization expansion.
`verify_semantic_relations` skips ontology documentation references and uses
the Predicate registry plus concrete PRED definitions. The registry includes
specializes but no concrete definition exists; it omits motivates despite
its concrete definition. Passing that verifier cannot demonstrate that the
proposed taxonomy is present, adopted or semantically coherent.

For rendering and navigation, ADR pages can continue to show decision content,
rationale, consequences and lifecycle. A future Decision category view could
include ADRs using an explicitly supported taxonomy query, while preserving
their primary ADR labels. That category query must not expand allowed pairs.
Option B instead requires rendering both decision classification and record
form after an approved remapping. In either case, generated output remains
representation, and displayed acceptance must come from explicit semantic
state. `render.py` couples verification with `write_all`; it is not a read-only
check and was not run for this report.

## 6. Explicit decision still required

Before implementation, an authorized architecture decision must settle:

1. Does ONT-ADR classify the documented architectural decision Entity (option A),
   or the documentary form/record (options B/C)? If A, explicitly adopt the
   specialization and clarify Proposed, Rejected and Withdrawn subjects under
   the generic Decision definition. Mere record existence must not imply
   acceptance.
2. How is the concept-level specialization represented canonically, with
   concept identity distinguished from instance typing and ordinary instance
   Predicate applicability? Existing examples and empty sidecars are insufficient.
3. How should the earlier Semantic Decisions group 7 and TASK-0006 premises be
   explicitly superseded in future authoritative material while their historical
   records remain intact? This task settles no duplicate Decision instances;
   it does not itself adopt this report's preferred taxonomy.
4. If a documentary-only interpretation is chosen, how are existing identities,
   primary Entity classifications, Artifact classification, lifecycle ownership
   and ADR relation endpoints mapped without duplicate Decision instances or
   silent reinterpretation? What representation association is actually required?
5. Which decision-kind semantics and lifecycle rules are shared by future
   specializations, and which are specific to architectural decisions? No new
   specialized concepts, IDs or universal documentation cardinalities are
   allocated here.

Predicate prose/constraint authority, endpoint ownership and canonical source
reconstruction also need explicit reconciliation before implementation relies
on the conflicting passages. They do not justify choosing a convenient
precedence in this report. There is no blocker to delivering this analysis;
formal adoption and implementation remain outside its scope.

## 7. Validation and change boundary

No Foundation changes were made. No existing analysis report or decision
record was modified. No Decision instances, Predicates, ontology declarations,
RFCs, ADRs, schemas, validators, renderers or tests were created or changed.
The only intended repository addition is this report.

Read-only loading and `verification.verify` processed 85 artifacts and returned
`ok: True`, with zero errors and 50 `unresolved-relation-predicate` warnings.
Python bytecode writing was disabled and `write_all` was not called. The
declaration census confirmed all 18 ADRs use ONT-ADR, no Foundation YAML declares
an ONT-Decision instance type, and no ontology file contains a specialization
declaration. Initial status showed only the new report; the diff of Foundation
and the three existing analysis/decision records was empty. The full new-file
diff was inspected; `git diff --check` found no tracked whitespace errors.

Additional checks and their executed results are recorded in the task completion summary:
source/declaration census, read-only Foundation loading and verification,
report citation checks, complete diff and staging-scope inspection, and final
commit/push/work-tree checks. A successful implementation verifier is limited
to its implemented rules; it does not resolve the source conflicts above.

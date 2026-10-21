# Decision and ADR Architecture Decision Preparation

## 1. Purpose, authority and decision requested

This report executes `engineering/task/TASK-0008/content.md`. It prepares a
choice about what `ONT-ADR` classifies and how it relates to `ONT-Decision`.
It is analysis and a proposed decision statement, not an accepted decision,
canonical taxonomy declaration or authorization to implement one.

**Recommendation:** choose option A, subject to the explicit premises in
section 7: ADR classifies the documented architectural decision Entity and
explicitly specializes Decision. Preserve the existing ADR identities and
their single primary `ontologyType: ONT-ADR`; distinguish their documentary
Artifacts and physical representations. Clarify that the generic category
includes formulated decision subjects before acceptance and in historical
states. This interpretation needs an authoritative decision and subsequent
specification; the present short Decision definition does not settle it.

**Strongest counterargument:** an Architecture Decision Record names a
documentation form, whereas architectural scope is a property of the decision.
Combining those axes in a subtype can make documenting a previously generic
decision appear to change its conceptual type. Option B separates the axes
more cleanly and may support future decision kinds better. Option A is preferred
for its fit with current definitions, ADR Entity typing and lifecycle usage,
not because document/decision equivalence is already established.

The task's established intent governs this preparation: Decision is generic;
future specialized decisions remain possible; existing ADRs need no additional
Decision instances; existing identities and history must survive; Entity and
Artifact meanings remain distinct; record existence is not acceptance. No
Predicate is needed merely to connect duplicate representations.

## 2. Repository state, evidence and limits

Inspected branch: `development`; basis commit:
`06c23362945e48e71bc5ca5e724981a682c035ee`; date: 2026-10-21.
Initial working tree and index were clean. No `AGENTS.md` was found in the
parent project tree. All required sources listed in TASK-0008 exist.

The references below use repository-relative paths and identify the passages
used. Braces abbreviate multiple actual paths. **Fact** means repository
evidence; **interpretation** means a reasoned reading; **proposal** means a
choice awaiting owner approval. Draft/Proposed text is evaluated as written,
without claiming acceptance from its normative wording or physical presence.

| Evidence | Concrete passages and observed state |
| --- | --- |
| `foundation/specifications/ontology/Decision/{content.md,metadata.yaml,relations.yaml}` | Definition: intentional selection among alternatives with the resulting determination. Metadata identifies ONT-Decision, entityType ontology, Draft; no ontologyType. Sidecar only references: []. |
| `foundation/specifications/ontology/ADR/{content.md,metadata.yaml,relations.yaml}` | Definition: documented architectural decision, rationale and consequences. Metadata identifies ONT-ADR, title Architecture Decision Record, entityType ontology, Draft; no ontologyType. Sidecar only references: []. |
| `foundation/specifications/ontology/Entity/content.md` and `foundation/specifications/entity/ENTITY-0001/content.md` | Entity Definition; ENTITY-0001 Definition, Identity, Type and Specialization: independently identifiable engineering knowledge, one primary ontologyType, Architecture Decisions among specialized Entity types, persistence-independent identity. |
| `foundation/specifications/ontology/Artifact/content.md` | Definition, Role in ATON and Persistence Independence: representation is not automatically Entity identity; Entity ontologyType and Artifact artifactType have different owners. |
| `foundation/specifications/adr/ADR-0008/content.md` | Decision and Explicit Ontology Type Identity: canonical models, explicit Entity typing, no path inference, specialization belongs in ontology rather than multiple instance type values. |
| `foundation/specifications/adr/ADR-0013/content.md` | Decision, Entity-to-Artifact Relationship, Identity, Versioning and Traceability: separate semantic owners, general many-to-many representation when supported, shared ID values permitted in the normal one-to-one case. |
| `foundation/specifications/adr/ADR-0014/content.md` | Decision, Semantic Validation, Relation Identity and Kernel Boundaries: canonical relation source/predicate/target, explicit Entity ontologyType for semantic validation, loader normalization. |
| `foundation/specifications/adr/ADR-0017/content.md` | Context; Decision; Proposed, Accepted, Rejected, Withdrawn, Superseded; Lifecycle Transitions; Versioning; Governance; Historical Preservation: lifecycle belongs to architectural decision; existence is not acceptance. |
| `foundation/specifications/rfc/RFC-0010/content.md` | Summary; Proposal / Engineering Entity, Artifact and Entity Representation, Artifact Identity, Artifact Type, Artifact Revision, Artifact and Engineering Version, Artifact and Relations: Entity, Artifact and physical representation are distinct. |
| `foundation/specifications/rfc/RFC-0020/content.md` | Concept Specialization; Ontology and Engineering Entities; Ontology and Artifacts; Ontology Evolution: explicit meaning-preserving specialization, concept/instance boundary, independent representation, no silent reinterpretation. |
| `foundation/specifications/rfc/RFC-0027/content.md` | Concept Model; Concept Specialization; Allowed Source-to-Target Pairs; Initial Predicate Vocabulary; No Implicit Predicate Inheritance; Ontology Evolution: illustrative ADR taxonomy, explicit pairs, controlled evolution. |
| `foundation/specifications/rfc/RFC-0029/content.md` | Canonical Constraint Model; Constraint Patterns; Exact Pair Matching; Type Specialization; Cardinality Constraints: explicit exact pairs/patterns, no inheritance, cardinality independent of pair validity. |
| `foundation/specifications/adr/ADR-0012/content.md` | Decision, Engineering Identity, Engineering Version, Artifact Revision, Git Revisions and Immutability: identity, semantic version, representation revision and Git revision differ. Additional evidence for lifecycle analysis. |
| `foundation/specifications/predicates/{motivates,references,governs,refines}/{content.md,constraints.yaml,metadata.yaml}` | Meaning, allowed pairs and actual constraints; all four definitions Draft, typed ONT-Predicate. Pair discrepancies detailed in section 4. |
| `engineering/analysis/architecture/Decision-ADR-Ontology-Analysis.md` | Sections 3–6: TASK-0007 evidence, options, conditional option A recommendation, lifecycle and taxonomy questions. Proposal only. |
| `engineering/analysis/architecture/Decision-ADR-Relationship-Analysis.md` | Sections 1, 4, 6–7: TASK-0006's separate Decision/ADR premises, Predicate assessment and required documentary association. Historical premises superseded for this task. |
| `engineering/analysis/architecture/Foundation-Semantic-Review.md` | Purpose; F19, F39, F44–F46, F52, F58–F60: lifecycle distinctions, absent adopted taxonomy, Predicate and source-model conflicts. Review, not adoption. |
| `engineering/analysis/architecture/Foundation-Semantic-Decisions.md` | Purpose and authority; group 7 clarifications 1–4; group 8 example 7: earlier documentary-only ADR interpretation, independent Decision identity, unresolved cardinality. Not an amendment to Foundation. |
| `tooling/docusaurus-renderer/verification.py` and `tooling/docusaurus-renderer/predicate_registry.py` | matches_constraint, resolve_concept, verify_semantic_relations, PREDICATE_STATES: exact/pattern matching, ontology-reference skip, registry/definition gaps. |
| `tooling/docusaurus-renderer/render.py` | main invokes verification then write_all; full rendering writes output and is not a read-only check. |

**Fact:** the census of `foundation/specifications/adr/*/metadata.yaml` finds
18 ADRs, ADR-0001 through ADR-0018, all with `ontologyType: ONT-ADR`.
Foundation YAML contains no `ontologyType: ONT-Decision` declaration. Searching
every file under `foundation/specifications/ontology/` finds no specialization
declaration or even a specialization mention. The RFC-0027 example and
RFC-0029 conditional example are not a concrete canonical taxonomy edge.

**Limit:** ONT-ADR's definition supports both a documented decision reading
and a documentary reading; neither definition explicitly selects a semantic
owner for every use of “ADR.” No complete generic Decision lifecycle or
concrete serialization contract for this taxonomy edge is established by
these sources. Canonical concept identifiers do not themselves identify
Decision instances or provide the instance typing of concept definitions.

RFC-0010, RFC-0020 and RFC-0027 metadata statuses are Draft; RFC-0029 and
ADR-0017 are Proposed. ADR-0013/0014 metadata is Draft. ADR-0008 content says
Accepted while metadata says Draft, as recorded in review F52. This report
does not resolve that status conflict by choosing an authority implicitly.

## 3. What is being classified?

| Semantic subject | Source fact | Interpretation relevant to the decision |
| --- | --- | --- |
| A decision as engineering knowledge | ONT-Decision Definition describes selection and determination; ENTITY-0001 requires identity and one primary type. | The decision subject is logical engineering knowledge, not its file. Its alternatives, rationale and outcome can be recorded without allocating a second Entity for that content. |
| An architectural decision | ENTITY-0001 Type names Architecture Decisions as specialized Entity types; ADR-0017 governs the Architecture Decision entity. | Architectural scope can refine generic decision semantics. There is no separately declared architectural-decision concept in the required sources to insert between ONT-ADR and ONT-Decision. This report creates none. |
| Architecture Decision Record as documentary form | ONT-ADR Definition includes documented decision, rationale and consequences; RFC-0010 Artifact Type lists decision record among examples. | A record form can classify a representation independently of the represented decision. That alone does not establish ONT-ADR as an artifactType or reassign current ontologyType values. |
| Artifact representing an Entity | ADR-0013 Entity-to-Artifact Relationship and RFC-0010 Artifact and Entity Representation permit multiple representations and supported compound artifacts. | An Artifact carries engineering knowledge; its identity and revisions differ from the represented Entity's. A physical Markdown manifestation is a further representation concern. |

There are two distinctions to preserve: concept versus classified instance
(RFC-0020), and Entity versus Artifact versus physical manifestation (RFC-0010).
An ADR directory's location cannot establish type, semantic source or identity.
An ONT-ADR Entity can be represented by an ADR Artifact under option A without
making the Artifact itself an intentional selection. Under option B the same
existing engineering decision would instead receive a deliberately chosen
Entity classification and a separate documentary classification contract.
Neither requires an extra Decision instance alongside the existing subject.

## 4. Common relation rules and contradictions

**Facts:** RFC-0027 No Implicit Predicate Inheritance and RFC-0029 Exact Pair
Matching/Type Specialization prohibit expanding pairs through taxonomy in
either direction. Explicit ANY-CONCEPT patterns match valid canonical concepts
only. Missing pairs mean no semantic applicability; missing cardinality means
no implicit restriction, not exactly one. None of the four concrete constraints
defines cardinality. Thus no universal ADR/Decision documentary cardinality
can be inferred from them.

| Contract | Actual pairs or discrepancy | Implication for the options |
| --- | --- | --- |
| motivates, content Allowed Pairs/Semantic Validation and constraints.yaml | ONT-Note → ONT-ADR; ONT-Finding → ONT-ADR. ONT-Decision targets explicitly excluded. Meaning speaks of contribution to a Decision. | A retains these ADR endpoint types; B cannot retype them to Decision and keep validity by inheritance. Motivation is not a representation mapping. |
| governs/constraints.yaml | ONT-ADR → ONT-Artifact; ONT-ADR → ONT-Collection; ONT-Constitution → ONT-Artifact; ONT-Constitution → ONT-Collection. | RFC-0027 governs lists only the ADR-source pairs. Retaining ADR typing preserves exact matches but does not resolve the catalogue discrepancy. |
| refines/constraints.yaml | Requirement, RFC, ADR, Component, Interface and AX each to the same concept, with ONT- IDs. | RFC-0027 refines omits AX → AX. Refinement between instance knowledge is not the formal ADR/Decision taxonomy. |
| references/content.md versus constraints.yaml | Prose permits only ONT-Artifact → ONT-Artifact; YAML permits explicit ANY-CONCEPT → ANY-CONCEPT. | Broad executable acceptance is not evidence of documentary meaning or authority to choose a mapping. Contradiction remains under every option. |
| RFC-0027 Initial Predicate Vocabulary / specifies and specializes | specifies: RFC → ADR. specializes: Artifact → Artifact, Definition → Definition, Entity → Entity. | These are exact named concept pairs, not automatic matches for all Entity subtypes or all concept-definition IDs. Concept taxonomy serialization still needs specification. |

The four concrete Predicate directories exclude specializes, although the
registry marks it canonical. The registry omits motivates although its
definition exists. `verify_semantic_relations` requires registry resolution
and a PRED definition, and skips ontology documentation references.
`matches_constraint` compares concrete IDs exactly or checks explicit patterns.
Current successful verification therefore cannot establish taxonomy adoption
or validate the intended concept-level edge merely from its illustration.

ADR-0014 Semantic Validation obtains types from Engineering Entity ontologyType.
RFC-0010 Artifact and Relations permits Artifact/Entity endpoint combinations
subject to ontology rules. The endpoint classification contract for a purely
documentary ADR is incomplete across these passages. RFC-0029 Motivation and
Separation from the Relation Model describe a predicate/target canonical
object with an external owner source, while
`foundation/specifications/rfc/RFC-0025/content.md`, Relation Domain Object,
requires source/predicate/target. Review F58 records that contradiction;
ADR-0014 also uses artifact-or-entity ownership wording. These are outstanding
source conflicts, not definitions silently repaired by a modeling option.

## 5. Lifecycle analysis and proposed resolution

**Facts:** ADR-0017 Proposed describes a formulated decision not yet accepted;
Accepted means an authoritative architectural decision; Rejected means
considered but not accepted; Withdrawn means a proposal removed from
consideration without previous authority. Superseded preserves a previously
accepted decision's historical identity. Lifecycle Transitions specifies
Proposed → Accepted/Rejected/Withdrawn and Accepted → Superseded; terminal
states remain historically addressable. Governance leaves authorization to
the applicable process or governance model. No new states or transitions are
needed to analyze this choice.

**Interpretation:** the generic Decision definition is insufficiently explicit
for the whole lifecycle. “Resulting determination” can mean a candidate
determination rather than an approved one, which accommodates Proposed and
Rejected subjects. But it can also mean a completed selection, which need
not exist when a proposal is Withdrawn. Rejection is a determination about
the proposed choice, not necessarily adoption of that choice. Treating it as
a new rejection Decision would change the modeled subject and needlessly
multiply identities. The sources do not resolve these readings.

Consequently, specialization is meaning-preserving only if the owner confirms
that Decision denotes an identifiable formulated decision subject whose
selection/determination can be proposed, accepted or historically disposed of.
This is a **proposed clarification**, not a claim that the current definition
already mandates that interpretation. If the owner instead requires a
completed selection as a condition of membership, option A cannot cover all
ADR-0017 states without a deliberate generic-definition change. Option B, C
or D must then be chosen or reconsidered; storing Proposed records does not
solve the generic category problem by itself.

| Concern | Meaning and consequence |
| --- | --- |
| Existence | An identifiable subject or record exists. Neither Git presence nor an Artifact alone proves a semantic decision was accepted. Under A, a formulated subject may exist before acceptance. |
| Decision state | Explicit semantic lifecycle of the architectural decision under ADR-0017. Proposed, Rejected and Withdrawn have no accepted authority by default; Superseded retains historical authority context. |
| Acceptance or approval | Accepted is a semantic state transition. Who may cause it and what approval evidence is needed belong to governance. Review completion and a push are not substitutes (ADR-0017 Accepted, Governance, Alternatives Considered). |
| Artifact lifecycle/revision | Changes to the documentary representation and its own applicable lifecycle, if defined. RFC-0010 Artifact Revision distinguishes these from Entity versions; the sources do not define a new generic Artifact state machine here. |
| Engineering Version | A semantic state of the underlying Entity, distinct from identity and from Artifact/Git revisions (ADR-0012 Engineering Version; ADR-0013 Versioning). A substantive change may require a new version; this report assigns none. |

ADR-0017 Versioning distinguishes lifecycle from version and says substantive
changes may create a version. ADR-0012 Engineering Version requires a new
version for relevant engineering meaning or normative-state change. Acceptance
may be such a change, but these passages do not provide a complete trigger
contract for every transition. Preserve the distinction and require an
explicit mapping before lifecycle/version automation; do not declare that
every transition always, or never, creates a version. Documentation edits,
semantic content changes and governance transitions must remain distinguishable.

For future decision kinds, the generic category's lifecycle compatibility
does not automatically impose ADR-0017's architecture-specific lifecycle.
There is no evidence for a complete generic Decision state machine in the
inspected sources, and none is introduced here.

## 6. Options and consequences of acceptance

### A. ADR explicitly specializes Decision and classifies the decision Entity

**Meaning and compatibility:** the documented architectural decision preserves
selection/determination semantics and adds scope, rationale and consequences.
ENTITY-0001, ONT-ADR's Definition and ADR-0017 support this reading. An Artifact
is still its representation; an Artifact itself does not become a Decision.
Validity depends on section 5's lifecycle clarification.

**Existing 18 ADRs and migration:** retain existing IDs, ONT-ADR primary types,
content, links, history and revisions; no second ONT-Decision value or Decision
instance. Accepting A would require future explicit taxonomy and definition
alignment, plus supersession of the historical documentary-only assumption.
Existing revisions remain historical; no automatic renumbering or version
allocation follows from accepting a taxonomy. The general representation
model remains potentially many-to-many, not universally one-to-one.

**Relations and implementation consequences:** existing exact ADR pairs remain
unchanged; generic Decision/future subtype pairs need their own explicit
permission. Proposed/Rejected/Withdrawn subjects retain identity without
authority. Future taxonomy validation and navigation can include ADRs in a
Decision category, but must not broaden Predicate checks. Rendering should
label the primary ADR category and explicit lifecycle while distinguishing
document revision from Engineering Version. Main risks are a documentation
axis disguised as taxonomy and lifecycle meaning mismatch. Taxonomy
serialization, cycle/reference validation and discovery behavior require
approved specifications; they are not implemented capabilities claimed here.
No new Predicate is needed to link two instances of the same decision.

### B. ADR is a documentary concept/form with an explicit contract

**Meaning and compatibility:** classify the semantic decision independently
from its documentary form. RFC-0010 Artifact Type and ADR-0013 strongly support
the separation, but current ONT-ADR Entity typing is not already that contract.
The existing identified decision can retain its identity and be reclassified
deliberately; no additional Decision instance is required. Shared Entity and
Artifact identifier values are permitted in suitable one-to-one cases without
equating their meanings. This is conceptual migration, not a directory rename.

**Existing 18 ADRs and migration:** explicitly choose their Entity concept,
the documentary classification's owner and allowed value, identity mapping,
source reconstruction and handling of historical type declarations. Do not
invent another architectural-decision ID or repurpose ontologyType as
artifactType automatically. Preserve original records, revisions and
addressability through an approved compatibility mechanism. Migration is
larger than A because all 18 current Entity classifications are implicated.

**Lifecycle, relations and presentation:** architectural-decision state must
remain on the decision subject, including Proposed, Accepted, Rejected and
Withdrawn; record revisions/lifecycle remain separate. Retyping to Decision
would invalidate restricted ADR endpoint matches unless contracts are
explicitly changed. Decide whether each existing edge refers to the decision
or documentary Artifact; broad references constraints do not decide this.
Validation must distinguish both owners and representation mapping. Rendering
and navigation should show one decision result with its documentation,
separating kind and form. Future specialized decisions can reuse documentation
forms without becoming ADR subtypes. Main risks are endpoint migration,
identity loss and accidental duplicate results. A representation contract is
required, but **no new Predicate is inherently required**: the appropriate
canonical representation mechanism is itself an explicit future choice, not
a link between duplicated Decisions.

### C. ADR remains a separately managed Entity concept without specialization

**Meaning and compatibility:** the sole existing identified knowledge object
is a managed decision record carrying the decision content. This fits one
primary type and can keep an Artifact distinct, but requires clarifying why
the documented architectural decision is outside the formal Decision taxonomy.
A documentary-only Artifact must not become an Entity merely because it is
a file (ADR-0013 Alternatives Considered).

**Existing 18 ADRs and migration:** keep IDs, ONT-ADR values, historical content,
revisions and links; clarify the record Entity's semantic subject rather than
allocate a separate Decision. Specify whether ADR-0017 state describes the
record's decision content or the record itself. Acceptance of a decision must
not be confused with approval of a document. Preserve Proposed, Rejected and
Withdrawn records without inferring acceptance; an independently accepted
document can still record a rejected choice.

**Relations and implementation consequences:** existing ADR pairs keep exact
typing, subject to the common source conflicts. Generic Decision navigation
cannot include ADR by specialization; any cross-category presentation rule
needs explicit semantics. Validation cannot claim that ADR instances satisfy
Decision constraints. Future specialized Decision kinds stay separate from
ADR; overlapping categories risk inconsistent queries and lifecycle logic.
No new Predicate is required without genuinely distinct semantic endpoints.
Main migration burden is semantic/lifecycle clarification and explicit
navigation policy, rather than type replacement; its cost grows if future
consumers need a unified Decision category.

### D. Defer the formal relationship

**Meaning and compatibility:** retain existing definitions and classify no
unrecorded hierarchy as canonical. This is the honest current implementation
position while contracts remain open, not a completed ontological answer.

**Existing 18 ADRs and migration:** retain IDs, ONT-ADR declarations, links,
historical content and revisions unchanged; no migration or extra Decision
instances. Continue to distinguish lifecycle from existence using ADR-0017's
written rules, while explicitly documenting status-authority conflicts.
Proposed/Rejected/Withdrawn do not become accepted by waiting or publication.

**Relations and implementation consequences:** keep exact pair rules and
existing checks without taxonomy expansion. Rendering can preserve current
ADR pages, but cannot assert that a generic Decision view includes them.
Future specialized decisions should wait for the shared classification
contract rather than assume inherited permissions or lifecycle. No new
Predicate is required. The principal risk is prolonged inconsistency across
tooling and future extensions. Accepting D should name an owner and review
trigger: resolution of Decision lifecycle coverage and the concept/Artifact
classification and taxonomy-representation contracts. No invented deadline
or future task identifier is assigned here.

## 7. Recommended choice, premises and strongest objection

Recommend A as the semantic target; defer its implementation until an
authoritative decision and representation contract exist. This is not option D
as a substitute recommendation: A chooses the meaning, while implementation
still needs its own approved scope. Retaining current implementation during
preparation does not adopt the taxonomy.

A best preserves the present 18 Entity classifications and ADR-0017 lifecycle
subject with the smallest identity and relation migration. It also permits
future decision subtypes while leaving exact Predicate applicability intact.
RFC-0027's example supports feasibility, but does not decide the choice.

The choice is valid only if the owner explicitly accepts these **premises**:

1. ONT-ADR classifies the documented architectural decision as semantic
   engineering knowledge, not only the documentary form or physical record.
2. Decision membership includes a formulated proposed determination and its
   rejected/withdrawn/historical states, without implying acceptance. The
   generic definition must be made explicit before specialization is implemented.
3. Each existing ADR's already identified subject can continue as the same
   Entity with one ONT-ADR primary type. No duplicate Decision registrations,
   forced new identifier values or automatic history rewrite are needed.
4. Taxonomy and representation are separate: the Artifact's classification,
   identity and revisions are not inherited from Entity ontologyType merely
   because their metadata is co-located.
5. Concept-level specialization will be specified explicitly; instance pairs,
   lifecycle governance and Engineering Version triggers will not be inferred
   from the taxonomy.

The strongest objection is substantive: if decision kind and documentation
form must be independent axes, “documented” is a poor differentiator for a
subtype. A decision may exist before its record, have multiple forms or use
an ADR form while belonging to a future specialized kind. With exactly one
primary type, A alone does not specify every combination. This report does
not invent multiple inheritance or a second architectural-decision concept
to solve that. If the owner requires reusable form independent of kind as
the primary model, B is the better choice despite its greater migration cost.
If lifecycle coverage or classification ownership cannot yet be decided,
D is preferable to silently adopting A. C remains viable only with explicit
record-subject and navigation semantics.

## 8. Earlier assumptions and what must be superseded

`engineering/analysis/architecture/Foundation-Semantic-Decisions.md`, Purpose
and authority, records earlier task agreements but says it does not amend the
Foundation. Group 7 clarification 2 excludes ADR as a specialized Decision
Entity and treats it solely as the Decision's Artifact; clarifications 1, 3
and 4 discuss separate semantic identities and documentation. Group 8 example
7 repeats the documentary reading and leaves cardinality open.

These passages conflict with proposed A's Entity meaning and current
ONT-ADR Entity-level declarations. Separate Entity/Artifact meanings remain
valid under A; the documentary-only classification and exclusion of
specialization would need explicit supersession. “Different meanings” must
not be reinterpreted as a requirement for two Decision Entities or universally
different identifier values; ADR-0013 Identity permits shared values.

The prior Relationship Analysis, section 1, explicitly assumed standalone
Decision identities with DEC- identifiers and an explicit ADR association;
sections 6–7 pursued exactly-one documentary association under that task.
Those premises are historical. TASK-0008 supersedes the separate-instance
requirement and does not adopt that registration or cardinality contract.
The report's Predicate assessment is evidence about its narrower premises,
not proof that the current choice needs a new Predicate. TASK-0007's option A
recommendation is likewise a proposal, not a later authoritative adoption.

An eventual decision should cite these specific historical passages, state
which semantic assumptions are superseded and which Entity/Artifact principles
remain, and define prospective compatibility. The original records should
remain intact. This report makes no such authoritative amendment itself.

## 9. Exact questions for the project owner

These are decision inputs, not requests to pause this analysis task.

1. Should ONT-ADR classify the architectural decision Entity (A), a documentary
   form with separately chosen Entity classification (B), or a managed record
   Entity outside Decision taxonomy (C), or should the choice be deferred (D)?
2. Does generic Decision include a formulated subject with a candidate
   determination before acceptance, and retain membership after rejection or
   withdrawal? If not, which option should accommodate ADR-0017's states?
3. Under A, is documented architectural scope an intrinsic refinement of the
   decision category, accepting that the model does not yet express every
   independent kind/form combination? Or is kind/form independence required now?
4. Can all existing ADR identities and ONT-ADR primary types remain under A,
   with no additional Decision instances, renumbering or retrospective status
   changes? Under B/C, what exact identity and subject mapping should replace
   that interpretation while preserving history?
5. Which authoritative concept/instance contract and serialized form will
   express taxonomy, without treating its declaration as an arbitrary
   instance specializes edge or adding a second ontologyType to instances?
6. Should Artifact classification remain independently specified where
   applicable, with no universal documentary cardinality implied by this
   decision? If B is selected, what owns the documentary classification and
   what canonical representation mapping is required?
7. Which source governs conflicting lifecycle/status declarations such as
   ADR-0008, what governance authorizes acceptance, and when does a lifecycle
   transition require an Engineering Version? Which of these rules must be
   settled before automation rather than inferred by implementers?
8. Will the authoritative decision explicitly supersede the documentary-only
   exclusion in Semantic Decisions group 7 and the separate-registration
   premises of TASK-0006, preserving their historical files?
9. Which follow-up specification scope will resolve taxonomy validation,
   relation-source ownership and Predicate contract discrepancies before
   affected validation/rendering changes? If D is chosen, who owns that work
   and what completed contracts trigger reconsideration?

## 10. Proposed decision statement — not adopted

The owner may accept, reject or revise the following statement. Its wording
describes the proposed future architecture; it creates no canonical declaration
or instance and assigns no lifecycle status to this report.

> Select option A. Decision is the generic semantic category for an identifiable
> formulated decision subject, including its proposed determination and its
> accepted, rejected, withdrawn or historical states; membership does not imply
> acceptance. ONT-ADR classifies a documented architectural decision Entity,
> including its rationale and consequences, and is to specialize ONT-Decision
> explicitly in the ontology. The existing ADR Entities retain their identities,
> identifiers and single primary ONT-ADR classification; no additional Decision
> instances are required. Their Artifacts and physical manifestations remain
> representations with distinct identity, classification and revision semantics.
> ADR-0017's architectural-decision lifecycle remains distinct from Artifact
> revision, Engineering Version and process approval; no new lifecycle or
> universal version-trigger rule is introduced by this choice. Specialization
> changes neither exact Predicate applicability nor relation cardinality.
> Future specialized decision concepts require explicit definitions and pairs
> where applicable. Supersede the earlier documentary-only exclusion of ADR
> specialization and the requirement for separately registered Decision
> instances, while preserving those historical records and the Entity/Artifact
> distinction. Specify the concept-level taxonomy representation, lifecycle
> definition alignment and affected compatibility contracts before implementing
> this choice. Introduce no Predicate merely to associate duplicate
> representations of the same decision.

If premise 1 or 2 in section 7 is rejected, this statement must be revised
or rejected rather than partially implemented with an implied taxonomy.
Owner acceptance would still need to be recorded through the project's
authoritative decision/governance mechanism; this analysis commit and push
do not constitute acceptance or authorize Foundation implementation.

## 11. Validation and change boundary

Executed during this task: initial Git status/branch/basis inspection; required
source reading; declaration census; and read-only Foundation loading followed
by `verification.verify`, with `PYTHONDONTWRITEBYTECODE=1` and no writer call.
The loader processed 85 artifacts. Verification returned `ok: True`, zero
errors and 50 warnings, all `unresolved-relation-predicate`. The census found
18 ONT-ADR declarations among 18 ADRs, zero Foundation ONT-Decision instance
type declarations, no ontology specialization mentions, and exactly four
concrete Predicate directories. These checks do not establish semantic
coherence, taxonomy adoption or lifecycle conformance beyond implemented rules.

Report source-path and whitespace checks, complete diff and staged-scope
inspection, and commit/push/final-status checks are recorded with their actual
results in the completion summary. Full rendering/build was not used as a
read-only check because it writes output. No tests were changed or added.

No Foundation file, existing report, decision record, task file, schema,
validator, renderer or test was modified. No Decision instance, ADR, RFC,
Predicate, relation or ontology declaration was created. The sole new file is
this decision-preparation report. Open architectural questions affect future
adoption and implementation, not completion of this analysis task.

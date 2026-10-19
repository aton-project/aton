# Decision/ADR Relationship Analysis

## 1. Purpose and scope

TASK-0006 asks whether the current ATON Foundation can explicitly associate an
independently identified Decision Entity with the ADR Artifact documenting it,
using an existing canonical Predicate without changing its semantics or
constraints. This report analyzes repository state at commit
`3a4911a4e76d0f80ba30cabbc5d65aa94d06d685`.

**Conclusion:** no existing Predicate has a coherent documented contract for
this association. `motivates` explicitly prohibits Decision-to-ADR;
`references` has conflicting prose and constraints and does not express the
specific documentary relationship. A separate model decision is necessary.

The task-supplied agreements are premises: a standalone canonical Decision
Entity has an independently allocated sequential `DEC-` identifier; an ADR is
a distinct Artifact documenting exactly one Decision; and their association
must be explicit. These agreements supersede earlier unresolved statements
about Decision prefixes and ADR-to-Decision cardinality. They do not establish
that Foundation definitions have already been reconciled with them.

This analysis does not amend the Foundation, register a Decision Entity,
implement an association, select a new Predicate, or authorize an extension.

## 2. Sources and their authority

All paths below are relative to the repository root. Section names identify
verifiable passages; source status is reported rather than silently promoted
to acceptance.

| Source | Relevant sections and role |
| --- | --- |
| `foundation/specifications/adr/ADR-0013/content.md` | Decision; Entity-to-Artifact Relationship; Identity; Persistence Independence: distinction and explicit representation relationship. |
| `foundation/specifications/adr/ADR-0014/content.md` | Decision; Predicate Semantics; Semantic Validation; Canonical Predicate Constraints; Relation Identity; Legacy Predicates: canonical Relations and explicit Entity typing. |
| `foundation/specifications/entity/ENTITY-0001/content.md` | Identity; Type; Relationships: independently identifiable Entities, explicit primary `ontologyType`, Entity endpoints. |
| `foundation/specifications/rfc/RFC-0020/content.md` | Summary; Ontology and Engineering Entities: ontology Concepts versus instances and physical representations. |
| `foundation/specifications/rfc/RFC-0025/content.md` | Relation Domain Object; Canonical Representation; Loader Requirements; Verification Requirements; Predicate Semantics: structural contract (Draft). |
| `foundation/specifications/rfc/RFC-0026/content.md` | Predicate Semantics; Source Constraints; Target Constraints; Predicate Direction; Inverse Predicates; Cardinality; Semantic Validation; Explicit Relations; Derived Relations: semantic contract (Draft). |
| `foundation/specifications/rfc/RFC-0027/content.md` | Ontological Model; Concept Specialization; Predicate Model; Allowed Source-to-Target Pairs; Initial Predicate Vocabulary; No Implicit Predicate Inheritance; Ontology Evolution: initial normative vocabulary within a Draft RFC. |
| `foundation/specifications/rfc/RFC-0029/content.md` | Canonical Constraint Model; Constraint Patterns; Concept Identity; Relation Evaluation; Source Concept Violation; Exact Pair Matching; Cardinality Constraints; Verification Algorithm: explicit constraint model (Proposed). |
| `foundation/specifications/rfc/RFC-0030/content.md` | Canonical Artifact Representation; Required Components; Relations; Relation Serialization: canonical physical profile and normalization. |
| `foundation/specifications/rfc/RFC-0028/content.md` | Migration Principle; Migration States; Initial Legacy Classification; No Automatic Semantic Migration: legacy usage is not authorization. |
| `foundation/specifications/predicates/{motivates,references,governs,refines}/` | Each `metadata.yaml`, `content.md`, `constraints.yaml`, and `relations.yaml`: the four concrete Predicate definitions, all Draft, and their exact constraints. |
| `foundation/specifications/ontology/{Decision,ADR,Entity,Artifact,Note,Finding,RFC,Predicate}/` | Definitions in `content.md` and actual declarations in `metadata.yaml`: Concept identity and classification evidence. |

Analysis context, not automatic Foundation amendments:

- `engineering/analysis/architecture/Foundation-Semantic-Review.md`, F44–F46
  records Predicate contradictions and endpoint terminology; F47–F49 addresses
  classification; F50 and F58–F60 addresses usages, source reconstruction and
  constraints; F63–F64 addresses serialization ambiguity and examples.
- `engineering/analysis/architecture/Foundation-Semantic-Decisions.md`, Purpose
  and authority; agreed groups 2, 4, 7–8; Implementation implications;
  Proposed conventions; Unresolved questions. It explicitly says it does not
  amend specifications. Its group 8.7 and unresolved question 3 leave ADR
  cardinality open; TASK-0006 now settles that question. Its unresolved prefix
  and standalone-registration questions are likewise partly superseded by
  TASK-0006, without supplying a concrete storage path or relation contract.

Examples and migration observations are distinguished from operative rules
throughout. The normative wording above is analyzed as the current contract,
including inconsistencies; no assumption is made that Draft/Proposed material
constitutes a completed, conflict-free implementation.

## 3. Current Relation and Predicate rules

### 3.1 Semantic roles and representation

RFC-0025, Relation Domain Object, requires source, predicate and target. The
source is the originating Engineering Knowledge object; the Predicate
identifies the semantic relationship; the target is the object it points to.
ADR-0014, Relation Identity, identifies a relation by that triple, independent
of physical serialization. RFC-0026 makes the semantic definition authoritative;
a name or structurally representable edge is insufficient.

The loader normalizes supported YAML forms into the canonical Relation model.
RFC-0030, Relation Serialization, specifies a mapping from relation collection
names to target identifiers. RFC-0025 also supports legacy empty lists and
embedded relation objects. These physical forms do not define semantics.

There is a source-representation tension: RFC-0029, Motivation and Separation
from the Relation Model, describes `predicate + target` with source supplied
by the owning Entity; RFC-0025 explicitly requires the complete triple;
ADR-0014, Decision, refers to the owning artifact or entity. The agreed
analysis context, group 4, clarifies that a canonical Relation has an explicit
semantic source; omission in serialization requires unambiguous reconstruction,
and multi-Entity representations require explicit source identification.
Physical ownership of an ADR file cannot itself establish a Decision source
or make the documentary Artifact an Entity endpoint.

### 3.2 Type resolution and pair evaluation

ADR-0014, Semantic Validation, requires the explicit canonical `ontologyType`
of each participating Engineering Entity. Paths, filenames and persistence
classifications cannot supply that type. ENTITY-0001, Type, requires exactly
one primary conceptual type; `artifactType`, when applicable, classifies the
Artifact separately. These declarations retain their ownership even when
co-located in `metadata.yaml`.

RFC-0027 and RFC-0029 require explicit allowed pairs, not independent source
and target sets with an implied Cartesian product. Resolve both endpoints,
their canonical Concepts, the Predicate and its constraint; accept the pair
only if both positions match one complete allowed entry. Concrete Concept
identifiers match exactly. No allowed pair means no semantic applicability;
an unknown Predicate or unresolved Concept cannot be accepted by guessing.
RFC-0029 distinguishes external-target resolution from ordinary local checks.

RFC-0029, Constraint Patterns, expressly permits `ANY-CONCEPT` at a declared
position. It matches valid canonical ontology Concepts, not unknown strings,
undefined types or an untyped physical artifact. Pattern matching is explicit
and does not establish inheritance. RFC-0027, Concept Specialization and No
Implicit Predicate Inheritance, and RFC-0029, Type Specialization, prohibit
implicit expansion to specialized or generalized Concepts. The illustrative
ADR-specializes-Decision taxonomy does not equate their identities or permit
new endpoint combinations.

Relations are directional unless explicitly symmetric. An explicitly defined
inverse preserves meaning in the reverse direction; it does not permit the
original Predicate to be reversed. Explicit relations are authored source
data; derived relations and future inference do not replace the required
explicit documentary association (RFC-0026, Explicit/Derived/Inferred Relations).

Structural checks include endpoint resolution, duplicates, content/title
presence and self-references. Semantic checks cover Predicate existence,
Concept resolution, direction, complete pair matching and defined cardinality.
RFC-0029 requires cardinality evaluation across the applicable source/Predicate
relation set after pair validity. A missing cardinality restriction implies no
restriction, not exactly one.

### 3.3 Current classification and usage evidence

`ontology/Decision/metadata.yaml` defines the Concept ID `ONT-Decision`;
`ontology/ADR/metadata.yaml` defines `ONT-ADR`. The first definition describes
an intentional selection among alternatives; the second describes a documented
architectural decision with rationale and consequences. These are Concept
definitions, not individual Decisions or an approved documentary association.

All eight ontology definition metadata files listed in section 2 have
`entityType: ontology` and **no `ontologyType` declaration**. Their IDs are not
self-declared instance types. By contrast, all 18 existing
`foundation/specifications/adr/ADR-0001` through `ADR-0018/metadata.yaml` files
declare `ontologyType: ONT-ADR`; all four Predicate metadata files declare
`ontologyType: ONT-Predicate`. RFC-0026/0027/0029 metadata declares `ONT-RFC`.
No Foundation declaration `ontologyType: ONT-Decision` or `DEC-` instance was
found. Existing ADR classifications do not establish a separately registered
Decision under the task's clarified model.

ADR-0017, Context and Decision, mixes ADR wording with the lifecycle of the
Architecture Decision; Accepted explicitly says ADR existence is insufficient
for acceptance. Together with current ONT-ADR usage, this requires future
reconciliation, not an automatic transfer of Decision identity to an ADR.

`foundation/examples/README.md` contains only a TODO. RFC-0026's Note-to-ADR
example illustrates motivation; ADR-0009's Context/validation examples discuss
Finding-to-Note and Note-to-Decision, and RFC-0004, Motivation, mentions a
Finding motivating a Note. None overrides the later explicit allowed pairs.
RFC-0029, Terminology, lists `dependsOn` as an example, and RFC-0030 shows
legacy collection names. RFC-0028 prevents these occurrences from establishing
new canonical semantics. No persisted `motivates` edge was found in Foundation
relation sidecars; the example text is not evidence of a documentary mapping.

## 4. Existing Predicate candidates

### 4.1 Concrete canonical definitions

The following pairs transcribe the actual constraints. Abbreviated Concept
names in tables denote their `ONT-` identifiers, not inferred supertypes.
The Predicate IDs are `PRED-` followed by their displayed names.

| Candidate | Definition and allowed combinations | Suitability for Decision Entity and ADR Artifact |
| --- | --- | --- |
| `motivates` | `predicates/motivates/content.md`, Meaning: Note/Finding supplies rationale, evidence, observation or a problem contributing to a Decision. Allowed Pairs and `constraints.yaml`: Note → ADR; Finding → ADR only. Inverse: `motivatedBy`. No cardinality defined. | **Not permitted.** Decision is not an allowed source. The prose mentioning Decision does not broaden the target. RFC-0029, Explicit Pair Semantics and Source Concept Violation, expressly declares Decision → motivates → ADR invalid. Motivation is not documentation. Making Decision the motivator or substituting its ADR for the Decision would misstate their roles. |
| `references` | `predicates/references/content.md`, Meaning: one artifact explicitly refers to another for information/context. Allowed Pairs and Semantic Validation permit only Artifact → Artifact. RFC-0027 agrees. Actual `constraints.yaml`: explicit `ANY-CONCEPT` → `ANY-CONCEPT`. Inverse: `referencedBy`. No cardinality defined. | **Constraint-compatible for resolved Concepts, but not a coherent documentary contract.** The wildcard could accept ONT-Decision → ONT-ADR if both endpoints were typed instances. The prose explicitly excludes that pair; moreover, the agreed ADR Artifact is not thereby an Entity with an `ontologyType`. Assigning it one merely to pass the check conflates layers. A generic contextual reference between distinct objects also fails to identify which ADR documents which Decision. |
| `governs` | `predicates/governs/content.md`, Meaning: establishes rules/principles/constraints governing an artifact or collection. Actual constraints: ADR → Artifact; ADR → Collection; Constitution → Artifact; Constitution → Collection. Inverse: `governedBy`. | **Not permitted and wrong meaning.** No Decision source, and no reverse ADR → Decision pair. Governance would not express documentary representation. RFC-0027 lists only the two ADR-source pairs; the Constitution additions conflict with that catalogue, but neither version supports this association. |
| `refines` | `predicates/refines/content.md`, Meaning: a more detailed/specialized expression preserving essential intent. Actual constraints: Requirement → Requirement; RFC → RFC; ADR → ADR; Component → Component; Interface → Interface; AX → AX. Inverse: `refinedBy`. | **Not permitted and wrong meaning.** No Decision/ADR combination in either direction. Recasting the Decision as an ADR to use ADR → ADR loses the agreed distinction. RFC-0027 omits the AX addition; that discrepancy does not create a Decision pair. |

Sources for each row are the named Predicate's `content.md`, `metadata.yaml`
and `constraints.yaml`, plus RFC-0027, Initial Predicate Vocabulary. No
cardinality field exists in any of the four constraint files.

**Interpretation of the `references` discrepancy:** broad pair acceptance is a
confirmed fact, not proof of suitability. RFC-0029 authorizes the wildcard
mechanism but does not redefine the meaning of `references`. The analysis
context's agreed group 4.8 calls for Entity-to-Entity reference semantics;
its Implementation implications explicitly leaves reconciliation pending.
Even that intended interpretation does not identify an Entity-to-Artifact
documentary relationship or enforce the task's cardinality. Selecting a
precedence silently, or claiming that a validator pass amends the definition,
would be unjustified. Distinct IDs alone preserve two identities but cannot
supply missing relationship semantics.

### 4.2 Remaining initial vocabulary

RFC-0027 also defines the following candidates or nearby relationships.
There are no corresponding concrete Predicate directories under
`foundation/specifications/predicates/` for these seven names. Their normative
RFC vocabulary must be distinguished from availability of canonical constraint
artifacts to the current verifier.

| Predicate | RFC-0027 meaning and complete listed pairs | Assessment |
| --- | --- | --- |
| `specifies` | RFC normatively specifies an architectural decision; RFC → ADR. | Specification is not documentary representation; Decision → ADR and ADR → Decision are absent. |
| `defines` | Authoritative definition of a concept, term, property, interface or knowledge element; Definition → Entity/Property/Interface; GlossaryEntry → Entity/Property/Interface; RFC → Interface; ADR → Interface. | An ADR documenting a Decision does not turn it into a Definition Entity. No relevant pair; Entity is an exact Concept, not every Entity subtype. |
| `specializes` | A more specific form of a Concept or artifact; Artifact → Artifact; Definition → Definition; Entity → Entity. | Taxonomy is not documentation. Decision/ADR is not an explicit pair; inheritance cannot expand Entity → Entity. |
| `contains` | Membership in defined scope; Collection → Artifact; Review → Finding; Artifact → Artifact. | Storage/membership does not express documentation. Neither direction has the required explicit pair. |
| `implements` | Component realizes behavior/specification; Component → RFC; Component → Requirement. | Wrong semantics and endpoints. |
| `verifies` | Test provides verification evidence; Test → Requirement; Test → Component; Test → RFC. | Wrong semantics and endpoints. |
| `allocates` | Requirement allocated to responsible component; Requirement → Component. | Wrong semantics and endpoints. |

Using these as defined does not equate identities, but none supplies the
required association. Changing endpoint classifications or treating an ADR as
a specialized Decision to force applicability would violate the task's
Entity/Artifact distinction. Their explicitly listed inverses in RFC-0027
reverse these same meanings and pairs; none yields a documentary relation.
An inverse name does not create a concrete constraint definition.

### 4.3 Tooling limits

`tooling/docusaurus-renderer/predicate_registry.py`, `PREDICATE_STATES`, marks
references, refines, specializes and governs canonical; it omits motivates
although `PRED-motivates` exists. Only `referencedBy` is registered as an
inverse. `verification.py`, `verify_semantic_relations`, first consults this
registry, then requires a `PRED-<name>` artifact. Thus vocabulary, concrete
artifacts and registry are not fully aligned: for example, a persisted
motivates edge is classified unknown by this implementation, and specializes
lacks its required artifact. These implementation gaps neither authorize nor
invalidate the normative meaning by themselves.

The verifier resolves Entity types and evaluates concrete/pattern pairs,
skips ontology-definition documentation references, and tolerates unresolved
legacy Predicates as warnings. Passing it demonstrates its implemented checks,
not full semantic consistency, documentary endpoint support, or the required
exactly-one constraint. No proposed association is instantiated in this report.

## 5. Evidence-based outcome

**Confirmed:** motivates excludes the pair expressly; other concrete restricted
Predicates and the remaining RFC vocabulary supply neither the required pair
nor documentary meaning. references has an executable wildcard but incompatible
prose. Current semantic validation resolves Entity ontology types, while the
required association connects an Entity to a distinct documentary Artifact.
ADR-0013 requires explicit modeling where necessary without defining the
specific Predicate or serialized mapping.

**Interpretation:** the supported outcome is that a deliberate model extension
is necessary. Reusing an existing Predicate would require an explicit semantic
change and/or permitted-pair change and, for this cross-layer relationship,
resolution of the endpoint model. Simply broadening motivates would still
express motivation, not documentation. Broad references acceptance alone is
insufficient. The gap is an explicit, typed, unambiguous documentary association
between an independently identified Decision Entity and its ADR Artifact,
with the agreed per-ADR exactly-one Decision requirement.

This conclusion does not decide whether the eventual extension should revise
an existing contract, add a separately specified relationship, or introduce an
explicit representation-mapping mechanism. Those are separate model choices;
no Predicate name, ID, allowed pair or new constraint is adopted here.

## 6. Identity and cardinality implications

The agreed model is consistent with ADR-0013's distinct Entity and Artifact
identities and persistence independence, but its concrete registration and
association contract remains incomplete in current Foundation material.

- A standalone Decision has its own sequential `DEC-` identifier, for example
  `DEC-0001`. `ONT-Decision` identifies its Concept, not the individual Decision.
  The task authorizes the prefix; this report allocates no instance ID.
- An ADR keeps its independent Artifact identity. Its number must not determine
  or be assumed to equal the Decision number. General permission in ADR-0013
  for shared values in normal one-to-one cases does not override this task's
  independently allocated Decision/ADR identities.
- Every ADR documents exactly one Decision. This is the task's agreed
  restriction on the general multiple-Entity representation permission in
  ADR-0013; it is not evidence that current Predicate constraints enforce it.
- Exactly one Decision per ADR does **not** establish exactly one ADR per
  Decision. Whether a Decision must have one ADR, may have several, or permits
  multiple revisions/representations of the same ADR remains to be specified.
- A future explicit mapping must identify both independent objects and their
  documentary roles. A generic link that may denote any contextual reference
  is not unambiguous documentation ownership.
- RFC-0029 defines cardinality by source and Predicate. If the approved
  association is oriented from Decision to ADR, outgoing counts alone cannot
  ensure each ADR documents exactly one Decision; the appropriate reverse
  uniqueness/mandatory coverage semantics and scope must be decided. Even
  outgoing cardinality evaluation must detect ADRs with no association.
- Directory proximity, embedded content, YAML file ownership, Markdown links,
  serialization, and a shared physical representation do not by themselves
  establish the canonical semantic association. Moving an ADR must not change
  which Decision it documents (ADR-0013, Entity-to-Artifact Relationship and
  Persistence Independence; RFC-0025, Canonical Representation).

## 7. Recommendation and open questions

Recommend a separate architecture/model decision defining the documentary
association contract before canonical registration or migration. It should
preserve the already agreed identities and exactly-one Decision per ADR,
resolve Entity-versus-Artifact endpoint typing, and align authoritative
semantics, constraints, serialization and verification. It should explicitly
choose whether this belongs in the existing Entity-relation mechanism or a
representation mapping. RFC-0027, Ontology Evolution and Compatibility,
requires deliberate semantic evolution rather than example-driven adoption.

The following questions remain open; the Decision prefix and one-Decision-per-ADR
rule are settled premises and should not be reopened as repository uncertainty:

1. How can a distinct ADR Artifact be addressed and classified as a documentary
   endpoint without borrowing the represented Decision's `ontologyType` or
   inventing an ADR Entity? How should existing `ONT-ADR` usages and lifecycle
   wording be reconciled?
2. Which mechanism and direction will express documentary representation, and
   what constitutes its explicit canonical persisted form and unambiguous
   source reconstruction? No existing file field is selected here.
3. How many ADR Artifacts may or must document a Decision, and how are Artifact
   revisions and alternate Physical Representations distinguished from multiple
   documentary Artifacts?
4. What validation scope, mandatory coverage and uniqueness rules enforce exactly
   one Decision for every ADR, including an ADR with no relation?
5. How will references prose, wildcard constraints, the initial vocabulary and
   the Predicate registry be reconciled? No broad or narrow interpretation is
   silently adopted by this report.
6. What concrete location, allocation procedure and canonical metadata contract
   will register standalone `DEC-` Entities and their independently identified
   ADR Artifacts under RFC-0030? The task settles standalone storage, but not
   these implementation details or a migration plan for existing ADRs.

Resolving these questions requires a separately authorized model decision.
This report records the gap and supports that decision without implementing it.

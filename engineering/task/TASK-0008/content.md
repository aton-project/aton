# TASK-0008: Decision and ADR Architecture Decision Preparation

## Objective

Prepare a decision-ready architectural analysis of the relationship between the ontology concepts `Decision` and `ADR`.

The task builds on the findings of TASK-0007 and prepares the explicit architectural decision that must precede any Foundation implementation.

This is an analysis and decision-preparation task only. It MUST NOT implement or adopt an ontology change.

## Agreed Architectural Intent

The following intent is established:

- `Decision` is a generic ontology concept for decisions.
- Existing ADRs document architectural decisions and do not require additional separate Decision instances.
- More specialized decision concepts may be introduced in the future.
- The current formal relationship between `ONT-Decision` and `ONT-ADR` remains unresolved.
- Existing ADR instances and their historical records must be preserved.
- Entity identity and Artifact representation have distinct semantics.
- The existence of an ADR does not imply that its decision has been accepted.
- No new Predicate is to be introduced merely to associate duplicate representations of the same decision.

The recommendation in TASK-0007 to specialize ADR under Decision is a proposal, not an adopted architectural decision.

## Sources to Examine

Inspect the current repository state and use the following sources as primary evidence:

- `engineering/analysis/architecture/Decision-ADR-Ontology-Analysis.md`
- `engineering/analysis/architecture/Decision-ADR-Relationship-Analysis.md`
- `engineering/analysis/architecture/Foundation-Semantic-Review.md`
- `engineering/analysis/architecture/Foundation-Semantic-Decisions.md`
- `foundation/specifications/ontology/Decision/`
- `foundation/specifications/ontology/ADR/`
- `foundation/specifications/ontology/Entity/`
- `foundation/specifications/ontology/Artifact/`
- `foundation/specifications/entity/ENTITY-0001/`
- RFC-0010, RFC-0020, RFC-0027, RFC-0029
- ADR-0008, ADR-0013, ADR-0014 and ADR-0017
- Relevant Predicate definitions, constraints and validation rules.

Verify all paths and claims against the current repository. If a source is absent or its contents do not support a claim, state that limitation explicitly.

Treat earlier assumptions that every ADR requires a separate Decision Entity as superseded by the agreed intent above. Preserve earlier reports as historical records.

## Required Analysis

### 1. Semantic meaning

Determine precisely what each concept classifies:

- A decision as an engineering knowledge object.
- An architectural decision as a specialized decision.
- An Architecture Decision Record as a documentary form.
- An Artifact representing an Entity.

Distinguish the semantic decision from its documentation and physical representation. Do not assume that a filename, directory or Markdown file determines the ontology classification.

### 2. Evaluate the modeling options

Evaluate at least these options:

A. `ONT-ADR` explicitly specializes `ONT-Decision` and classifies the architectural decision Entity.

B. `ONT-ADR` represents a documentary concept or form distinct from the Decision Entity, with an explicit representation and classification contract.

C. `ONT-ADR` remains a separately managed Entity concept without a formal specialization relationship.

D. Defer the formal relationship until the ontology's concept and representation contracts are sufficiently explicit.

For each option, evaluate:

- Semantic consistency with the existing definitions.
- Compatibility with ENTITY-0001 and the Entity/Artifact distinction.
- Treatment of the existing 18 ADRs and their `ontologyType: ONT-ADR`.
- Preservation of identity, identifiers, historical records and revisions.
- Decision lifecycle semantics, including Proposed, Accepted, Rejected and Withdrawn.
- Compatibility with current relation endpoint rules and exact Predicate constraints.
- Consequences for validation, rendering, navigation and future specialized decision concepts.
- Migration requirements and risks.
- Whether the option requires a new Predicate, and why.

Do not assume that Predicate applicability is inherited through specialization. Follow the explicit rules in RFC-0027 and RFC-0029.

### 3. Resolve the lifecycle question

Analyze whether the generic Decision definition adequately accommodates decisions that are proposed, rejected or withdrawn.

Distinguish:

- The existence of a decision or decision record.
- The state of the decision.
- Acceptance or approval.
- The lifecycle and revision of an Artifact.
- The Engineering Version of the underlying Entity.

Do not silently equate these concepts or introduce a new lifecycle model without evidence.

### 4. Review previous assumptions

Identify the conflict between the current analysis and earlier documentary assumptions in `Foundation-Semantic-Decisions.md`.

Explain what an eventual authoritative decision must clarify or supersede. Do not edit that record and do not erase its historical context.

### 5. Produce an actionable decision proposal

Conclude with:

- A recommended option and its rationale.
- The strongest counterargument to that recommendation.
- Explicit premises required for the choice to be valid.
- The consequences of accepting each viable option.
- A list of exact questions the project owner must answer.
- A proposed decision statement that can be accepted, rejected or revised by the project owner.
- A clear separation between source facts, interpretation and recommendation.

The proposal MUST NOT be presented as already adopted.

## Required Output

Create exactly one new file:

`engineering/analysis/architecture/Decision-ADR-Architecture-Decision-Preparation.md`

The report must be self-contained and decision-ready. Include repository-relative source paths and relevant section names or identifiers. Cite concrete source passages through precise references; do not rely on unsupported summaries.

Do not create a canonical Decision Entity, ADR, RFC, Predicate, ontology declaration or any other Foundation artifact.

## Restrictions

- Do NOT modify any file under `foundation/`.
- Do NOT modify existing analysis reports or decision records.
- Do NOT change task files, schemas, validators, renderers or tests.
- Do NOT create separate Decision instances for existing ADRs.
- Do NOT introduce a new Predicate or relation to connect duplicate representations.
- Do NOT silently reconcile contradictory source definitions.
- Do NOT amend, rewrite or reset existing commits.
- Do NOT stage unrelated files.
- Do NOT claim that the proposed taxonomy is canonical or adopted.

## Validation

Before committing:

1. Inspect the working-tree status and complete diff.
2. Confirm that the only new file is the required report.
3. Confirm that no Foundation files or existing reports changed.
4. Run suitable read-only checks where practical.
5. Record the actual checks and their results.
6. Do not claim successful checks that were not executed.

## Git and Publication

After the report is complete and its scope has been verified:

1. Stage only:
   `engineering/analysis/architecture/Decision-ADR-Architecture-Decision-Preparation.md`
2. Commit with exactly this message:
   `analysis: prepare Decision ADR architecture decision`
3. Push to `origin development`.

The report commit and push are explicitly authorized for this task.

If unrelated changes exist, preserve them and exclude them from the commit. If the push fails, report the failure and do not claim publication.

## Completion Summary

Report:

- The new report path.
- The recommended option and principal rationale.
- The strongest counterargument and unresolved questions.
- The checks actually executed and their results.
- The commit hash and commit message.
- The push result.
- The final working-tree status.

No Foundation implementation is authorized by this task.

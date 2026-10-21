# TASK-0007: Decision and ADR Ontology Analysis

## Objective

Analyze how the ontology concepts `Decision` and `ADR` should be
related in the ATON Foundation.

Produce a reasoned recommendation based on the current Foundation,
without modifying the Foundation or implementing the recommendation.

## Agreed Architectural Intent

The following intent is established and MUST be respected:

- `Decision` is a generic ontology concept for decisions.
- Existing ADRs document architectural decisions and do not require
  additional, separate Decision instances.
- More specialized kinds of decisions may be introduced in the future.
- The relationship between the generic concept `Decision` and the
  concept `ADR` has not yet been formally resolved.
- The analysis MUST NOT assume that `ADR` specializes `Decision`,
  nor assume that they must be connected by a new Predicate.
  These possibilities must be evaluated against the existing model.

## Scope of Investigation

Inspect the current repository and, at minimum, examine:

- The ontology definitions and metadata for `Decision` and `ADR`.
- `ENTITY-0001` and the current Entity and Artifact model.
- RFC-0020, RFC-0027 and RFC-0029.
- Relevant existing ADRs, including ADR-0013, ADR-0014 and ADR-0017
  where present.
- Existing ontology specialization declarations and their semantics.
- Existing Predicate definitions, constraints and applicable-pair rules.
- The existing Foundation semantic review and decision records.
- The previous analysis report
  `engineering/analysis/architecture/Decision-ADR-Relationship-Analysis.md`,
  if present.

Treat the earlier assumption that every ADR needs a separate Decision
Entity as superseded by the agreed architectural intent above.
The previous report is historical analysis and MUST remain unchanged.

## Questions to Answer

1. What do the current `Decision` and `ADR` ontology definitions
   actually state?
2. Does the current model treat `ADR` as a kind of decision, a
   documentation form, or leave this distinction unresolved?
3. Would formal specialization of `ADR` under `Decision` preserve
   the meaning of both concepts and the Entity/Artifact distinction?
4. Would keeping `ADR` as a separate concept better represent its
   documentation role? If so, how should its relationship to
   architectural decisions be understood without creating duplicate
   Decision instances?
5. What do RFC-0020, RFC-0027 and RFC-0029 permit or prohibit regarding
   specialization and Predicate applicability?
6. Does the current model contain contradictions, ambiguities or
   missing definitions relevant to this question?
7. What are the consequences of each viable option for existing ADRs,
   future specialized decision concepts, relation constraints,
   validation and rendering?
8. Which option is recommended, why, and what explicit architectural
   decision is still needed before implementation?

## Required Report

Create exactly one new report:

`engineering/analysis/architecture/Decision-ADR-Ontology-Analysis.md`

The report MUST include:

- Purpose and scope.
- Repository state and relevant files examined.
- Findings grounded in the actual source definitions, with paths and
  section names or identifiers wherever possible.
- A clear distinction between source facts, interpretation and
  recommendation.
- A comparison of the viable modeling options.
- Impacts on existing ADRs and future ontology extensions.
- A recommended option and the rationale.
- Open questions requiring an explicit decision.
- A statement that no Foundation changes were made.

Do not claim that a proposal is already canonical or adopted unless
the repository explicitly supports that conclusion.

## Restrictions

- Do NOT modify files under `foundation/`.
- Do NOT modify existing analysis reports or decision records.
- Do NOT create Decision instances for existing ADRs.
- Do NOT create or modify Predicates, ontology concepts, RFCs or ADRs.
- Do NOT change repository schemas, validators, renderers or tests.
- Do NOT silently reconcile conflicting source definitions.
- Do NOT invent missing concepts, identifiers, relations or constraints.
- Do NOT rewrite or amend existing commits.
- Do NOT commit any file other than the new report.

If a required source is missing, record that fact in the report instead
of fabricating its contents.

## Validation

Before committing:

1. Inspect `git status` and the complete diff.
2. Confirm that the only new file is the required report.
3. Confirm that no Foundation file or existing analysis report changed.
4. Run appropriate read-only checks where practical.
5. Record checks and results in the report or final summary.
6. Do not report a check as passed unless it was actually executed.

## Git and Publication

After the report is complete and the restrictions have been verified:

1. Stage only:
   `engineering/analysis/architecture/Decision-ADR-Ontology-Analysis.md`
2. Commit with exactly this message:
   `analysis: clarify Decision and ADR ontology`
3. Push the commit to:
   `origin development`

The push is explicitly authorized for this task.

Do not use `git add .` or stage unrelated changes.
If the working tree contains unrelated changes, preserve them and do
not include them in the commit.
If the push fails, report the failure and do not claim that the report
was published.

## Completion Summary

Report:

- The created report path.
- The main findings and recommendation.
- Checks actually executed and their results.
- The commit hash.
- The push result.
- The final working-tree status.
- Any unresolved questions or blockers.

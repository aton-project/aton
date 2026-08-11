# Architecture Decision Lifecycle

## Context

Architecture Decision Records represent explicit engineering decisions within
the ATON Engineering Knowledge Model.

An Architecture Decision evolves through a lifecycle from its initial
proposal to an established decision and, where necessary, to its replacement
or withdrawal.

The lifecycle of an Architecture Decision is distinct from the engineering
process used to create or review that decision.

ATON SHALL therefore define the semantic lifecycle of an Architecture
Decision without prescribing the process by which an organization reaches
that decision.

## Problem Statement

Without a normative lifecycle, the status of an Architecture Decision is
ambiguous.

In particular, it must be possible to distinguish between:

- a decision that is still being formulated;
- a decision that has been accepted;
- a decision that is no longer current;
- a decision that has been rejected; and
- a decision that has been withdrawn.

The lifecycle must preserve the historical identity of decisions and must
not confuse lifecycle state with Git history or process execution state.

## Decision

An Architecture Decision SHALL have an explicit lifecycle state.

The lifecycle state SHALL describe the semantic state of the Architecture
Decision itself.

Lifecycle state SHALL NOT be inferred solely from:

- Git branches;
- Git commits;
- file names;
- repository locations;
- review activity;
- timestamps; or
- other technical or process information.

The lifecycle SHALL support at least the following states:

- Proposed
- Accepted
- Superseded
- Rejected
- Withdrawn

An implementation MAY support additional states when required by a domain or
process model, provided that their semantics do not conflict with the
Foundation lifecycle.

## Proposed

Proposed indicates that an Architecture Decision has been formulated but has
not yet become an accepted architectural decision.

A Proposed decision MAY be reviewed, modified or withdrawn.

A Proposed decision SHALL NOT be treated as an authoritative architectural
constraint unless another explicit governance mechanism defines such
behaviour.

## Accepted

Accepted indicates that the Architecture Decision has become an authoritative
architectural decision.

An Accepted decision SHALL be considered part of the normative architectural
knowledge of the applicable ATON scope.

Acceptance SHALL be a semantic state transition and SHALL NOT be inferred
merely from the existence of an ADR artifact.

## Superseded

Superseded indicates that an Architecture Decision was previously accepted
but has been replaced by another Architecture Decision.

A Superseded decision SHALL remain part of the historical Engineering
Knowledge Model.

Supersession SHALL NOT delete or invalidate the historical identity of the
original decision.

The superseding decision SHOULD be explicitly traceable through the canonical
relation model.

## Rejected

Rejected indicates that an Architecture Decision was considered but was not
accepted as an authoritative architectural decision.

A Rejected decision SHALL remain available as engineering history.

A Rejected decision SHALL NOT be treated as an authoritative architectural
constraint.

## Withdrawn

Withdrawn indicates that a Proposed Architecture Decision has been removed
from consideration without becoming an accepted architectural decision.

A Withdrawn decision SHALL remain available as engineering history.

Withdrawal SHALL NOT imply that the decision was previously authoritative.

## Lifecycle Transitions

The Foundation SHALL define the following normative transitions:

- Proposed to Accepted
- Proposed to Rejected
- Proposed to Withdrawn
- Accepted to Superseded

An Accepted decision SHALL NOT transition back to Proposed.

A Superseded, Rejected or Withdrawn decision SHALL be terminal with respect to
the Foundation lifecycle.

A future Foundation extension MAY define additional transitions, but SHALL
preserve the semantic distinction between current and historical decisions.

## Versioning

Lifecycle state and engineering version SHALL remain distinct.

Changing the lifecycle state of an ADR does not necessarily create a new
engineering identity.

A change to the substantive architectural decision MAY create a new
engineering version according to the applicable version semantics.

Lifecycle state SHALL therefore not be used as a substitute for version
information.

## Process Independence

The lifecycle defines the semantic states of an Architecture Decision.

It does not define:

- who must approve a decision;
- how many reviewers are required;
- how reviews are conducted;
- which meeting or workflow is required;
- how long a decision may remain Proposed;
- which organizational role performs acceptance; or
- which engineering methodology must be used.

Those aspects belong to the applicable Engineering Process Model or
organizational governance model.

## Governance

A process or governance model MAY define which roles are authorized to cause
lifecycle transitions.

Such authorization SHALL remain separate from the semantic definition of the
lifecycle states.

The Foundation therefore defines what a lifecycle state means, while a
process or governance model may define who and under which conditions a
transition may occur.

## Traceability

Lifecycle transitions SHOULD remain traceable.

Traceability MAY reference:

- engineering activities;
- process instances;
- reviews;
- findings;
- other Architecture Decisions;
- Git revisions; or
- other engineering evidence.

Such evidence provides provenance for the transition but SHALL NOT itself
define the lifecycle state.

## Verification

ATON MAY verify lifecycle consistency.

Verification MAY detect conditions such as:

- an invalid lifecycle transition;
- an Accepted decision without required governance evidence;
- a Superseded decision without a superseding decision;
- conflicting lifecycle information; or
- invalid relations associated with a lifecycle transition.

The exact verification rules MAY be defined by the applicable governance or
process model.

## Historical Preservation

Architecture Decisions SHALL remain historically addressable after their
lifecycle becomes terminal.

Superseded, Rejected and Withdrawn decisions SHALL NOT be physically removed
merely because they are no longer current.

Historical decisions may provide important engineering context, rationale and
traceability.

## Consequences

### Positive

- ADR lifecycle semantics are unambiguous.
- Architectural decisions remain historically traceable.
- Lifecycle state is independent of Git and process implementation.
- Organizations can define their own approval and review processes.
- ATON can verify lifecycle consistency without prescribing governance.
- Supersession can be represented explicitly.

### Negative

- Lifecycle state must be maintained explicitly.
- Governance processes must define how transitions are authorized.
- Historical decisions remain part of the knowledge model and therefore
  require appropriate navigation and filtering.

## Relationship to Other Decisions

ADR-0012 defines engineering version semantics.

ADR-0014 defines the canonical semantic relation model used for traceability
between Architecture Decisions and other engineering entities.

ADR-0016 defines the generic Engineering Process Model.

This ADR defines the semantic lifecycle of the specific Architecture Decision
entity and does not define a general engineering process.

## Alternatives Considered

### Derive ADR state from Git branches

Rejected.

Git branches describe technical version-control state and do not provide the
semantic lifecycle of an Architecture Decision.

### Derive acceptance from review completion

Rejected.

Review completion is process information. Acceptance is an architectural
lifecycle state.

### Allow arbitrary lifecycle states without Foundation semantics

Rejected.

A common minimum lifecycle is required for interoperable interpretation of
Architecture Decisions.

### Delete decisions when they are no longer current

Rejected.

Historical decisions provide important engineering context and traceability.

## Expected Outcome

ATON SHALL define a normative semantic lifecycle for Architecture Decisions
while leaving approval procedures, roles and review methods to the applicable
Engineering Process and governance models.

Architecture Decision lifecycle state SHALL remain explicit, historically
traceable and independent of persistence and process implementation.

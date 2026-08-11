# Engineering Process Model

## Context

Engineering activities are performed according to processes.

Different engineering organizations, projects, domains and standards may use
different processes.

ATON is intended to provide engineering infrastructure rather than prescribe
a particular engineering methodology.

ATON therefore requires a generic model that can represent engineering
processes independently of any specific process definition.

The review process used during the development of ATON is one example of an
engineering process. It is not itself part of the ATON Foundation.

## Problem Statement

Without a generic process model, ATON cannot consistently represent or reason
about:

- engineering activities;
- process states;
- process transitions;
- roles and responsibilities;
- process inputs and outputs;
- required conditions;
- process results;
- verification activities; and
- process compliance.

At the same time, embedding a specific process into the Foundation would make
ATON prescriptive and reduce its applicability across engineering domains.

## Decision

ATON SHALL provide a generic domain model for describing, tracking and
verifying engineering processes.

ATON SHALL NOT prescribe a particular engineering process, methodology,
workflow or organizational procedure.

A project, organization or engineering domain MAY define its own processes
using the ATON process model.

The semantics of a specific process SHALL be defined by the process
specification using the capabilities provided by ATON.

## Process

A Process SHALL represent a defined set of engineering activities and the
relationships between them.

A Process MAY define:

- activities;
- states;
- transitions;
- roles;
- inputs;
- outputs;
- constraints;
- dependencies;
- entry criteria;
- completion criteria; and
- verification conditions.

The ATON Foundation SHALL define the semantics of these concepts without
requiring a particular process structure.

## Activity

An Activity SHALL represent an identifiable unit of engineering work within a
Process.

An Activity MAY:

- consume engineering information;
- produce engineering information;
- modify engineering artifacts;
- change engineering state;
- require specified conditions;
- be assigned to a role; and
- require verification.

The meaning and granularity of an Activity SHALL be determined by the process
definition.

ATON SHALL NOT prescribe a universal activity decomposition.

## Process State

A Process State SHALL represent a defined condition of a Process or Activity.

States MAY be used to represent lifecycle progression, completion,
approval, verification or other process-specific conditions.

The set of states and their semantics SHALL be defined by the applicable
process model.

ATON SHALL provide the capability to represent state without prescribing a
universal state machine.

## Transitions

A Transition SHALL represent a permitted change between process states.

A process MAY define conditions under which a transition is permitted.

These conditions MAY depend on:

- completed activities;
- required artifacts;
- relation constraints;
- verification results;
- role authorization;
- other process-defined conditions.

ATON SHALL provide the means to represent and verify such conditions without
defining which transitions a particular process must contain.

## Roles and Responsibilities

A Process MAY define roles and associate responsibilities with activities,
transitions or verification conditions.

ATON SHALL represent roles and their relationships to process elements where
required by a process definition.

ATON SHALL NOT prescribe organizational roles or responsibilities.

A process MAY therefore define different role models according to its
engineering context.

## Inputs and Outputs

A Process or Activity MAY define expected inputs and outputs.

Inputs and outputs MAY reference Engineering Entities, Engineering Artifacts,
relations or other engineering information defined by the applicable domain
model.

The existence of an input or output requirement SHALL be distinguishable from
the actual engineering artifact or entity fulfilling that requirement.

This allows process specifications to define expectations independently of
specific physical representations.

## Process Constraints

A Process MAY define constraints that must be satisfied for an Activity,
Transition or Process State.

Constraints MAY concern:

- required artifacts;
- required relations;
- metadata;
- engineering states;
- predecessor activities;
- verification results;
- role authorization;
- other domain-specific conditions.

ATON SHALL provide mechanisms for representing and evaluating such
constraints.

The semantics of a constraint SHALL be defined by the applicable process or
domain specification.

## Verification

ATON SHALL provide the capability to verify whether process-defined
conditions are satisfied.

Verification MAY evaluate:

- existence of required engineering information;
- validity of relations;
- metadata constraints;
- process state;
- activity completion;
- required outputs;
- traceability;
- other explicitly defined conditions.

A verification result SHALL be distinguishable from the process definition
itself.

ATON SHALL therefore support verification of a process without making the
verification rules specific to any single process methodology.

## Process Execution and Tracking

ATON MAY record the execution state of a Process or Activity.

Execution information MAY include:

- current state;
- completed activities;
- responsible roles;
- produced artifacts;
- verification results;
- timestamps;
- references to engineering events.

Such information SHALL remain distinguishable from the process definition.

A process definition describes what is expected.

Process execution describes what has occurred.

## Process Definition and Process Instance

A Process Definition SHALL describe the structure and semantics of an
engineering process.

A Process Instance SHALL represent the execution of a Process Definition for
a particular engineering context.

A Process Definition MAY therefore be reused across multiple projects or
engineering activities.

A Process Instance SHALL retain the relationship to the Process Definition
against which it is executed.

## Process Independence

The ATON Foundation SHALL remain independent of specific engineering
methodologies.

ATON SHALL therefore not require:

- a specific development lifecycle;
- a specific review methodology;
- a specific requirements process;
- a specific safety process;
- a specific organizational structure; or
- a specific compliance framework.

Such processes MAY be represented using the ATON process model.

## Engineering Knowledge Integration

Processes SHALL be able to reference the canonical Engineering Knowledge
Model.

Process elements MAY therefore relate to:

- Engineering Entities;
- Engineering Artifacts;
- Engineering Versions;
- Baselines;
- Relations;
- Metadata;
- Verification results.

Process information SHALL remain part of the Engineering Knowledge Model
rather than becoming an implementation-specific workflow structure.

## Consequences

### Positive

- ATON remains process-agnostic.
- Different engineering methodologies can be represented.
- Project-specific processes can be modeled without changing the Foundation.
- Process execution can be tracked separately from process definition.
- Process compliance can be verified against explicit conditions.
- The ATON development process can itself be represented using ATON.
- Engineering processes can use the same knowledge model as other ATON
  engineering information.

### Negative

- A generic process model is more abstract than a predefined workflow.
- Concrete processes require their own specifications.
- Implementations must support process definitions in addition to process
  execution.
- Verification rules may become domain- or process-specific.

## Relationship to Other Decisions

ADR-0013 defines Engineering Entity and Engineering Artifact semantics.

ADR-0012 defines engineering version and baseline semantics.

ADR-0014 defines the canonical semantic relation model.

ADR-0010 defines canonical metadata semantics.

The Engineering Process Model uses these concepts but does not redefine them.

## Alternatives Considered

### Define a mandatory ATON development process

Rejected.

The process used to develop ATON is an application of ATON and must not become
a Foundation requirement.

### Define a mandatory review process

Rejected.

Different engineering domains require different review methods.

### Provide only workflow execution

Rejected.

ATON must represent process definitions and their engineering semantics, not
merely execute workflows.

### Leave process semantics entirely to implementations

Rejected.

ATON requires a common domain model so that process information can remain
portable, interoperable and verifiable.

## Expected Outcome

ATON SHALL provide a generic Engineering Process Model that allows projects
and organizations to define, execute, track and verify their own engineering
processes.

The ATON Foundation SHALL define the capabilities and semantics of the model
without prescribing a particular engineering process.

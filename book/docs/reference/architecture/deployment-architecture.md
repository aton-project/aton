# Deployment Architecture

## Goals

The deployment architecture of ATON shall provide:

- Reproducible deployments
- Separation of test and production environments
- Immutable releases
- Fast rollback capability
- Traceability between Git commits and deployed releases
- Simple command-line interface

## Architecture

ATON uses an immutable release-based deployment architecture.

The deployment process separates source development, test deployment,
validation and production publication.

### Deployment Flow

```text
Git Repository
      |
      v
aton deploy test
      |
      v
Immutable Test Release
      |
      v
current-test
      |
      v
Validation
      |
      v
aton publish
      |
      v
Immutable Production Release
      |
      v
current-prod
```

The Git repository is the authoritative source for the ATON Foundation
and documentation.

`aton deploy test` creates an immutable release for the test environment.

`current-test` identifies the release currently deployed to the test
environment.

The test release is validated before it can be published to production.

`aton publish` publishes the validated release to the production
environment.

`current-prod` identifies the release currently deployed to production.

A production release SHALL only originate from a successfully validated
release.

### Deployment Properties

The deployment architecture provides:

- immutable releases
- deterministic deployments
- separation of test and production
- explicit validation before production
- fast rollback capability
- traceability between releases and Git commits

## Directory Structure

ATON stores immutable releases separately from the active deployment
pointers.

```text
/opt/projects/aton/
|
+-- book/
    |
    +-- releases/
        |
        +-- <release-001>/
        +-- <release-002>/
        +-- <release-003>/
        +-- ...
        |
        +-- current-test
        |
        +-- current-prod
```

Each release directory is immutable after creation.

`current-test` identifies the release currently deployed to the test
environment.

`current-prod` identifies the release currently deployed to production.

The active pointers SHALL NOT contain mutable release content.

### Release Lifecycle

```text
Git commit
    |
    v
Test release
    |
    v
Validation
    |
    +---- failed ----> rejected
    |
    v
Production release
    |
    v
current-prod
```

A rollback SHALL be performed by changing the active production pointer
to a previously validated immutable release.

The immutable release itself SHALL NOT be modified during rollback.

## Principles

- A release is immutable.
- Production always points to a tested release.
- Publishing never rebuilds the project.
- Rollback only changes a symbolic link.

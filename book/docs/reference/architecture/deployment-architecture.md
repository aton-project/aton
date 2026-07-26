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

Git Repository
        │
        ▼
aton deploy test
        │
        ▼
Release
        │
        ▼
current-test
        │
    Validation
        │
        ▼
aton publish
        │
        ▼
current-prod

## Directory Structure

/opt/projects/aton
├── book/
├── releases/
├── current-test
└── current-prod

## Principles

- A release is immutable.
- Production always points to a tested release.
- Publishing never rebuilds the project.
- Rollback only changes a symbolic link.

# Coding Guidelines

These guidelines define the coding standards for ATON.

The goal is consistency, readability and maintainability.

---

# General Principles

Code should be:

- readable
- simple
- maintainable
- testable
- deterministic

Prefer clarity over cleverness.

---

# General Rules

- Keep functions small.
- Keep classes focused.
- Avoid unnecessary abstractions.
- Avoid duplicated code.
- Prefer composition over inheritance.
- Prefer immutable objects whenever practical.

---

# Naming

Use meaningful names.

Good:

```
ArtifactRepository
VersionHistory
RelationshipType
```

Avoid:

```
Manager
Helper
Utils
Data
Object
```

---

# Classes

A class should have one clear responsibility.

Large classes should be split.

---

# Methods

Methods should:

- perform one task
- have descriptive names
- avoid excessive nesting
- return early when possible

---

# Variables

Prefer local variables.

Avoid mutable global state.

Avoid abbreviations unless universally understood.

---

# Constants

Replace magic numbers with named constants.

Example:

```
MAX_RELATION_DEPTH
DEFAULT_TIMEOUT
```

---

# Error Handling

Never silently ignore errors.

Provide meaningful exception messages.

Fail early.

---

# Logging

Log meaningful events.

Avoid excessive logging.

Never log secrets or credentials.

---

# Documentation

Document:

- public APIs
- architectural decisions
- complex algorithms

Do not document obvious code.

---

# Comments

Comments should explain:

- why

Code should explain:

- what

Remove outdated comments.

---

# Formatting

Use consistent formatting.

Do not optimize for compactness.

Whitespace should improve readability.

---

# Dependencies

Only introduce dependencies when they provide clear value.

Minimize transitive dependencies.

---

# Testing

Every bug fix should include a test whenever practical.

Prefer automated tests.

Tests should be readable.

---

# Generated Code

Generated code must never be modified manually.

Changes belong in the source model.

---

# Architecture

Implementation must follow the documented architecture.

Never implement functionality that contradicts the Book or ADRs.

---

# Documentation

Documentation and implementation evolve together.

A feature is not complete until both are updated.

---

# Review Checklist

Before submitting code, verify:

- Code compiles
- Tests pass
- Documentation updated
- No unnecessary dependencies
- No dead code
- No commented-out code
- Naming is consistent
- Issue referenced

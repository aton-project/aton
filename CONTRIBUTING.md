# Contributing to ATON

Thank you for your interest in contributing to ATON.

ATON is an Open Engineering Operating System built around a versioned Engineering Knowledge Graph. Our goal is to establish a solid architectural foundation before implementing functionality.

## Before You Start

Please read the following documents before contributing:

- Project README
- The ATON Book
- Architecture Decision Records (ADRs)

Understanding the architecture is essential before implementing new features.

---

# Development Philosophy

ATON follows a documentation-driven development process.

The development workflow is always:

> **Book → Architecture → Model → Implementation → Tests**

The Book is the authoritative specification of the project.

---

# Architecture First

ATON is an architecture-driven project.

New functionality should only be implemented after the corresponding concepts have been documented in the Book.

If no architectural specification exists, it should be created before implementation begins.

Architecture drives implementation—not the other way around.

---

# Contribution Workflow

1. Create or select an Issue.
2. Discuss the proposed solution if necessary.
3. Create a feature branch.
4. Implement the change.
5. Update the documentation.
6. Add or update tests.
7. Submit a Pull Request.

---

# Coding Principles

Contributors should follow the project design principles.

- Everything is an Artifact.
- Relationships are First-Class.
- Everything is Versioned.
- Knowledge over Documents.
- Git is the Source of Truth.
- Keep the Kernel Small.
- API First.
- Open by Design.

---

# Documentation

Every architectural change must be reflected in the Book.

Documentation is not optional.

If the implementation changes, the documentation must be updated accordingly.

---

# Definition of Done

An Issue may only be closed when:

- all acceptance criteria are fulfilled;
- the implementation is complete;
- the documentation has been updated;
- tests have been added or updated where applicable;
- related ADRs are referenced where appropriate;
- the corresponding Issue is linked from the commit or pull request.

---

# Pull Requests

Pull Requests should:

- have a clear purpose;
- reference the related Issue;
- include documentation updates where applicable;
- keep changes focused and easy to review.

Whenever possible, use GitHub keywords such as:

- `Closes #<issue>`
- `Fixes #<issue>`
- `Resolves #<issue>`

to automatically close completed Issues.

---

# Code of Conduct

Please follow the project's Code of Conduct.

---

# Thank You

Thank you for helping build ATON.

Together we are building an open foundation for managing engineering knowledge.

# Development Guide

This document describes the development process, environment and workflow for ATON.

---

# Development Philosophy

ATON is developed using a documentation-driven approach.

The development order is always:

Book → Architecture → Domain Model → Implementation → Tests

The Book is the authoritative specification.

Architecture drives implementation—not the other way around.

---

# Development Process

Every new feature follows the same lifecycle:

1. Create or select an Issue
2. Define the architecture
3. Document the solution in the Book
4. Create or update ADRs if required
5. Define or update the domain model
6. Implement the solution
7. Add or update tests
8. Update documentation
9. Submit a Pull Request
10. Close the Issue

---

# Repository Structure

```
aton/
├── .github/
├── book/
├── aton-model/
├── aton-kernel/
├── aton-git/
├── aton-rest/
├── aton-web/
├── aton-ai/
├── examples/
├── README.md
├── DEVELOPMENT.md
├── CODING_GUIDELINES.md
└── ...
```

---

# Development Environment

## Required Software

- Git
- Java LTS
- Maven
- Node.js LTS
- npm
- Docker
- Docker Compose

Recommended

- Visual Studio Code
- Eclipse Modeling Framework (EMF)

---

# Clone Repository

```bash
git clone https://github.com/aton-project/aton.git
cd aton
```

---

# Book

The Book contains the official specification.

Start the documentation:

```bash
cd book
npm install
npm start
```

Create a production build:

```bash
npm run build
```

---

# Architecture

Every architectural change must first be documented.

Architecture Decisions are documented using ADRs.

The Book always reflects the current architecture.

---

# Domain Model

The engineering domain model is technology independent.

Workflow:

Book

↓

UML

↓

Engineering.ecore

↓

Generated Java Model

↓

Kernel Services

Generated code must never be modified manually.

---

# Kernel

The Kernel represents the core engineering concepts.

The Kernel must remain:

- small
- technology independent
- extensible
- stable

---

# Branch Strategy

Recommended branch names:

- main
- feature/<name>
- bugfix/<name>
- documentation/<name>
- refactoring/<name>

---

# Commit Messages

Recommended format:

```
Short summary

Optional explanation.

Closes #123
```

Commit messages should be concise and describe the intent.

---

# Pull Requests

Every Pull Request should:

- reference an Issue
- explain the motivation
- describe the solution
- update documentation
- include tests where applicable

---

# Testing

Every module should include automated tests whenever practical.

Recommended order:

- Unit Tests
- Integration Tests
- System Tests

---

# Documentation

Documentation is part of the implementation.

Implementation without documentation is considered incomplete.

Every architectural change must be reflected in the Book.

---

# Build Order

Development generally follows this order:

1. Book
2. ADR
3. Domain Model
4. EMF Model
5. Kernel
6. Persistence
7. REST API
8. Web UI
9. AI

---

# Documentation Hierarchy

If multiple sources differ, the following order applies:

1. Architecture Decision Records
2. ATON Book
3. Source Code
4. Module README files
5. Code Comments

---

# Questions

If an architectural decision is unclear, discuss it before implementing code.

Architecture decisions should be documented using ADRs whenever appropriate.

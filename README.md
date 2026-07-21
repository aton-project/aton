<p align="center">
  <img src="book/static/img/logos/aton-logo.png" alt="ATON Logo" width="240">
</p>

<h1 align="center">ATON</h1>

<p align="center">
  <strong>An Open Engineering Operating System</strong>
</p>

<p align="center">
  Built around a versioned Engineering Knowledge Graph.
</p>

---

## Vision

Modern engineering relies on many specialized tools for requirements management, systems modeling, testing, project management and documentation.

Although these tools often describe the same system, they maintain separate data models and repositories, making engineering knowledge fragmented and difficult to manage.

ATON provides a common engineering platform that connects engineering knowledge instead of engineering tools.

Its foundation is a versioned Engineering Knowledge Graph that enables traceability, collaboration and extensibility across engineering disciplines.

## Core Principles

- Everything is an Artifact
- Relationships are First-Class
- Everything is Versioned
- Knowledge over Documents
- Git is the Source of Truth
- Open by Design

## Architecture

ATON consists of a small Kernel that provides generic engineering infrastructure.

Engineering capabilities such as Requirements Management, MBSE, Test Management or Risk Management are implemented as extensions on top of the Kernel.

```text
                  Engineer
                      │
                      ▼
         Engineering Capabilities
──────────────────────────────────────────
 Requirements   MBSE   Tests   Risks   PM
──────────────────────────────────────────
              Kernel Services
──────────────────────────────────────────
 Artifact  Relation  Version
 Review    Baseline
──────────────────────────────────────────
     Engineering Knowledge Graph
──────────────────────────────────────────
          Git Repository Storage
```
The Kernel provides the common engineering infrastructure.

All engineering capabilities are implemented as independent extensions, allowing ATON to remain modular, extensible and technology independent.

## Project Documentation

The following documents describe the project, its architecture, development process and governance.

| Document | Purpose |
|-----------|---------|
| **README.md** | Project overview, vision, architecture and getting started. |
| **ROADMAP.md** | Planned milestones, releases and long-term project goals. |
| **CONTRIBUTING.md** | Guidelines for contributing to the project. |
| **DEVELOPMENT.md** | Development workflow, environment setup and implementation process. |
| **CODING_GUIDELINES.md** | Coding standards and best practices for all project languages. |
| **CHANGELOG.md** | History of notable changes between project releases. |
| **CODE_OF_CONDUCT.md** | Community standards and expected behavior. |
| **SECURITY.md** | Security policy and vulnerability reporting process. |

Together, these documents define how ATON is designed, developed, maintained and governed.

## Repository Structure

| Module | Description |
|---------|-------------|
| **book** | Project documentation |
| **aton-model** | Engineering domain model |
| **aton-kernel** | Kernel services |
| **aton-git** | Git persistence |
| **aton-rest** | REST API |
| **aton-web** | Web frontend |
| **aton-ai** | AI capabilities |
| **examples** | Example projects |

## Getting Started

ATON is an architecture-driven engineering platform.

Whether you want to explore the project, understand its concepts or contribute to its implementation, the following steps will help you get started.

### 1. Clone the Repository

```bash
git clone https://github.com/aton-project/aton.git
cd aton
```

### 2. Read the Documentation

Before writing code, we recommend reading:

- **README.md** – Project overview
- **The ATON Book** – Architecture and concepts
- **Architecture Decision Records (ADRs)** – Key design decisions

### 3. Start the Documentation

The Book is the authoritative specification of the project.

```bash
cd book
npm install
npm start
```

The documentation will be available at:

```
http://localhost:3000
```

### 4. Explore the Project

A good starting point is the following reading order:

1. Vision
2. Core Principles
3. Architecture
4. ADRs
5. Domain Model
6. Repository Structure

### 5. Contribute

If you would like to contribute, please read:

- **CONTRIBUTING.md**
- **DEVELOPMENT.md**
- **CODING_GUIDELINES.md**

Before implementing new functionality, ensure that the corresponding architecture is documented.

> **The Book defines the system. The implementation follows the Book.**

## Project Status

🚧 **Foundation Phase**

The architecture, documentation and domain model are currently being established before implementation begins.

Current Focus

- Documentation
- Domain Model
- Architecture Decisions
- Engineering Metamodel

Production-ready implementation has not yet started.

## Roadmap

| Release | Goal |
|---------|------|
| **v0.1** | Foundation |
| **v0.2** | Kernel |
| **v0.3** | Git Persistence |
| **v0.4** | REST API |
| **v0.5** | Web UI |
| **v0.6** | AI |

## Contributing

Contributions of all kinds are welcome, including architecture discussions, documentation improvements, bug reports and implementation.

Please read CONTRIBUTING.md before submitting Issues or Pull Requests.

## License

Licensed under the Apache License 2.0.

# ATON Book

The ATON Book is the authoritative specification of the ATON Engineering Operating System.

It documents the vision, concepts, architecture and design decisions of the project.

> The Book defines the architecture.
> The implementation follows the Book.

## Prerequisites

- Node.js 22+
- npm

## Run locally

```bash
npm install
npm start
```

The documentation is available at:

http://localhost:4000

## Build

```bash
npm run build
```

## Structure

```text
docs/
├── getting-started/
├── concepts/
├── architecture/
├── reference/
└── decisions/
```

## Documentation Principles

- Documentation is written before implementation.
- Architecture is technology independent.
- Decisions are documented as ADRs.
- The Book is the single source of truth for the domain model.

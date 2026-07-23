#!/usr/bin/env bash

set -Eeuo pipefail

ROOT="${1:-foundation}"

echo "Creating ATON Foundation in '$ROOT'..."

###############################################################################
# Directory Structure
###############################################################################

#mkdir -p "$ROOT"/{specification/{adr,rfc,glossary,ontology,schemas,templates},
#reference-model,
#examples,
#tooling,
#book,
#scripts,
#.github/workflows}
mkdir -p "$ROOT"

mkdir -p "$ROOT/specification"
mkdir -p "$ROOT/specification/adr"
mkdir -p "$ROOT/specification/rfc"
mkdir -p "$ROOT/specification/glossary"
mkdir -p "$ROOT/specification/ontology"
mkdir -p "$ROOT/specification/schemas"
mkdir -p "$ROOT/specification/templates"

mkdir -p "$ROOT/reference-model"
mkdir -p "$ROOT/examples"
mkdir -p "$ROOT/tooling"
mkdir -p "$ROOT/book"
mkdir -p "$ROOT/scripts"
mkdir -p "$ROOT/.github/workflows"

###############################################################################
# README
###############################################################################

cat > "$ROOT/README.md" <<'EOF'
# ATON Foundation

ATON Foundation contains the official specifications,
ontology, schemas and reference model of ATON.

This repository is self-hosting.
EOF

###############################################################################
# Specification README
###############################################################################

cat > "$ROOT/specification/README.md" <<'EOF'
# Specification

Official specifications of ATON.

Contains:

- ADRs
- RFCs
- Ontology
- Schemas
- Glossary
EOF

###############################################################################
# ADR-0001
###############################################################################

mkdir -p "$ROOT/specification/adr/ADR-0001"

cat > "$ROOT/specification/adr/ADR-0001/content.md" <<'EOF'
# ADR-0001 – Self Hosting Foundation

Status: Accepted

## Decision

ATON shall describe itself using ATON artifacts.

The Foundation repository is the reference implementation.
EOF

cat > "$ROOT/specification/adr/ADR-0001/metadata.yaml" <<'EOF'
id: ADR-0001
title: Self Hosting Foundation
entityType: adr
status: Accepted
version: 1.0.0
EOF

cat > "$ROOT/specification/adr/ADR-0001/relations.yaml" <<'EOF'
references: []
dependsOn: []
EOF

###############################################################################
# RFC titles
###############################################################################

declare -A RFCS

RFCS[0000]="Document Conventions"
RFCS[0001]="Entity Model"
RFCS[0002]="Identity Model"
RFCS[0003]="Metadata Model"
RFCS[0004]="Relation Model"
RFCS[0005]="Property Model"
RFCS[0010]="Artifact Model"
RFCS[0011]="Repository Layout"
RFCS[0012]="Versioning"
RFCS[0013]="Baselines"
RFCS[0020]="Ontology"
RFCS[0021]="Views"
RFCS[0022]="Collections"
RFCS[0023]="Traceability"

###############################################################################
# RFCs
###############################################################################

for ID in $(printf "%s\n" "${!RFCS[@]}" | sort)
do

DIR="$ROOT/specification/rfc/RFC-$ID"

mkdir -p "$DIR"

cat > "$DIR/content.md" <<EOF
# RFC-$ID – ${RFCS[$ID]}

Status: Draft

## Summary

TODO

## Motivation

TODO

## Goals

TODO

## Non Goals

TODO

## Proposal

TODO

## Consequences

TODO

## Alternatives

TODO

## Migration

TODO

## Open Questions

TODO
EOF

cat > "$DIR/metadata.yaml" <<EOF
id: RFC-$ID
title: ${RFCS[$ID]}
entityType: rfc
status: Draft
version: 0.1.0
EOF

cat > "$DIR/relations.yaml" <<'EOF'
references: []
dependsOn: []
supersedes: []
supersededBy: []
relatedTo: []
EOF

done

###############################################################################
# Ontology
###############################################################################

for ENTITY in \
Thing \
Entity \
Artifact \
Property \
Metadata \
Relation \
View \
Collection \
Definition \
Requirement \
Component \
Interface \
Test \
Decision \
RFC \
ADR \
GlossaryEntry
do

mkdir -p "$ROOT/specification/ontology/$ENTITY"

cat > "$ROOT/specification/ontology/$ENTITY/content.md" <<EOF
# $ENTITY

Status: Draft

Definition of $ENTITY.
EOF

cat > "$ROOT/specification/ontology/$ENTITY/metadata.yaml" <<EOF
id: ONT-$ENTITY
entityType: ontology
status: Draft
EOF

cat > "$ROOT/specification/ontology/$ENTITY/relations.yaml" <<'EOF'
references: []
EOF

done

###############################################################################
# Glossary
###############################################################################

mkdir -p "$ROOT/specification/glossary"

cat > "$ROOT/specification/glossary/README.md" <<'EOF'
# Glossary

Each glossary entry is an individual Entity.
EOF

###############################################################################
# Schemas
###############################################################################

mkdir -p "$ROOT/specification/schemas"

touch \
"$ROOT/specification/schemas/entity.schema.yaml" \
"$ROOT/specification/schemas/artifact.schema.yaml" \
"$ROOT/specification/schemas/relation.schema.yaml" \
"$ROOT/specification/schemas/metadata.schema.yaml"

###############################################################################
# Templates
###############################################################################

mkdir -p "$ROOT/specification/templates"

touch \
"$ROOT/specification/templates/entity-template.md" \
"$ROOT/specification/templates/rfc-template.md" \
"$ROOT/specification/templates/adr-template.md"

###############################################################################
# Other READMEs
###############################################################################

for D in \
reference-model \
examples \
tooling \
book
do

cat > "$ROOT/$D/README.md" <<EOF
# ${D}

TODO
EOF

done

###############################################################################
# Gitignore
###############################################################################

cat > "$ROOT/.gitignore" <<'EOF'
.DS_Store
.idea/
.vscode/
EOF

###############################################################################

echo
echo "=============================================="
echo "ATON Foundation bootstrap complete."
echo
echo "Root:"
echo "  $ROOT"
echo "=============================================="

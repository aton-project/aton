# RFC-0031 ATON Markdown Profile

## Status

Proposed

## Abstract

This RFC defines the canonical Markdown profile for ATON engineering
content.

ADR-0002 establishes Markdown as the canonical authoring and serialization
format for engineering content.

This RFC defines the subset of Markdown syntax that conforming ATON
implementations SHALL support and the restrictions that preserve
interoperability, portability and long-term maintainability.

The profile is intentionally conservative.

ATON SHALL use broadly supported Markdown constructs and SHALL NOT make
engineering knowledge dependent on a specific documentation generator,
editor or rendering framework.

## Motivation

Markdown implementations differ in their supported syntax and extensions.

A document accepted by one Markdown implementation may therefore fail to
render consistently in another implementation.

ATON requires a stable Markdown profile so that engineering content remains
portable across:

- operating systems;
- editors;
- repositories;
- renderers;
- analysis tools;
- importers;
- exporters; and
- future implementations.

The Markdown profile therefore defines the interoperable authoring language
while leaving rendering and presentation to implementations.

## Design Principle

The ATON Markdown Profile SHALL be based on broadly interoperable Markdown
syntax.

The profile SHALL define engineering content semantics only where required
for interoperability.

Presentation-specific behaviour SHALL NOT become part of the canonical
engineering content model.

A renderer MAY provide additional capabilities, but such capabilities SHALL
NOT change the semantic meaning of canonical ATON Markdown.

## Canonical Markdown

Markdown SHALL remain the canonical serialization format for engineering
content as established by ADR-0002.

The canonical Markdown representation SHALL be plain text.

The representation SHALL NOT require a proprietary editor or rendering
environment.

A conforming implementation SHALL be able to preserve canonical Markdown
without transforming it into a proprietary representation.

## Document Structure

An ATON Markdown document MAY contain:

- headings;
- paragraphs;
- emphasis;
- strong emphasis;
- ordered lists;
- unordered lists;
- block quotations;
- thematic breaks;
- inline code;
- fenced code blocks;
- links;
- reference links;
- escaped characters; and
- plain text.

These constructs SHALL retain their normal Markdown semantics.

## Headings

ATON Markdown SHALL support headings at levels one through six.

ATON engineering artifacts SHOULD use a single level-one heading as the
document title.

The document title SHALL remain presentation content and SHALL NOT replace
the canonical artifact title stored in metadata.

Heading text SHALL NOT define artifact identity.

Heading structure SHALL NOT be interpreted as an engineering relationship.

## Paragraphs

Paragraphs SHALL be supported as ordinary Markdown text blocks.

Line wrapping within a paragraph SHALL NOT alter its semantic meaning.

Implementations SHOULD preserve author-intended paragraph boundaries when
serializing Markdown.

## Lists

Ordered and unordered lists SHALL be supported.

List nesting SHALL be supported according to the capabilities of the
underlying Markdown implementation.

List ordering SHALL be preserved where ordering is semantically meaningful
to the engineering content.

## Emphasis

ATON Markdown SHALL support ordinary Markdown emphasis and strong emphasis.

Emphasis SHALL be treated as presentation of textual content and SHALL NOT
introduce engineering semantics.

## Code

Inline code SHALL be supported.

Fenced code blocks SHALL be supported.

A fenced code block MAY specify a language identifier.

Language identifiers SHALL identify the syntax of the code contained within
the block.

Language identifiers SHALL NOT create engineering semantics unless a
separate normative specification explicitly defines such semantics.

Indented code blocks MAY be supported by implementations but SHOULD NOT be
used for canonical ATON content when fenced code blocks provide an
equivalent representation.

## Links

Markdown links SHALL be supported.

Links MAY reference:

- external resources;
- local resources;
- engineering artifacts;
- sections within documents; or
- other resolvable targets.

A link SHALL NOT automatically constitute an Engineering Knowledge Model
relation.

Semantic engineering relations SHALL be represented through the canonical
relation model and SHALL NOT be inferred solely from Markdown hyperlinks.

## Images

Images are not currently part of the required canonical ATON Markdown
profile.

An implementation MAY render images or other visual resources.

If images are introduced into canonical engineering content, their semantic
and persistence rules SHALL be defined by a future normative specification.

An implementation SHALL NOT require images for the interpretation of
canonical engineering content unless the applicable artifact specification
explicitly requires them.

## Tables

Tables are not part of the required canonical ATON Markdown profile.

Implementations MAY support Markdown table syntax as a rendering extension.

A table SHALL NOT be required for the interpretation of canonical
engineering content unless a future normative specification explicitly
defines table semantics.

Engineering information that requires machine-readable semantics SHALL be
represented through the Engineering Knowledge Model rather than through
visual table structure.

## Task Lists

Task-list extensions are not part of the required canonical ATON Markdown
profile.

An implementation MAY render task lists.

Task-list state SHALL NOT be interpreted as engineering process state unless
a separate normative specification explicitly defines such semantics.

Engineering process state belongs to the applicable process model.

## Raw HTML

Raw HTML SHALL NOT be part of the canonical ATON Markdown profile.

Implementations MAY support HTML as a rendering feature, but canonical ATON
engineering content SHALL NOT depend on raw HTML.

HTML elements SHALL NOT be required for the semantic interpretation of
canonical engineering content.

This restriction preserves portability across Markdown implementations.

## MDX and Embedded Components

MDX, JSX and renderer-specific component syntax SHALL NOT be part of the
canonical ATON Markdown profile.

An implementation MAY provide MDX or component support for presentation
purposes.

Canonical engineering content SHALL remain interpretable without executing
or evaluating embedded components.

Engineering semantics SHALL NOT depend on renderer-specific components.

## Directives and Admonitions

Renderer-specific directives, admonitions and custom block syntax SHALL NOT
be part of the canonical ATON Markdown profile.

Implementations MAY provide such features as presentation extensions.

Canonical engineering meaning SHALL NOT depend on those extensions.

If a future Foundation specification requires a particular extension, that
extension SHALL be explicitly standardized before becoming part of the
canonical profile.

## Mathematics

Mathematical notation is not currently part of the required canonical ATON
Markdown profile.

Implementations MAY support mathematical extensions such as TeX or
LaTeX-based notation.

Such extensions SHALL NOT be required for interpreting canonical engineering
content unless explicitly standardized by a future specification.

## Diagrams

Diagram languages are not currently part of the required canonical ATON
Markdown profile.

An implementation MAY support fenced diagram languages such as Mermaid.

Diagram syntax SHALL remain an extension unless explicitly standardized by a
future Foundation specification.

The semantic Engineering Knowledge Model SHALL NOT depend on the visual
representation of a diagram.

Where a diagram represents engineering relationships, those relationships
SHALL remain defined by the canonical Engineering Knowledge Model rather
than by the diagram source alone.

## Front Matter

Engineering metadata SHALL NOT be embedded in Markdown front matter when
the artifact uses the canonical ATON artifact representation.

Canonical artifact metadata SHALL be stored in `metadata.yaml` according to
RFC-0030.

This separation prevents metadata semantics from becoming dependent on
Markdown parser behaviour.

Implementations MAY read front matter from external Markdown documents during
import, but imported metadata SHALL be normalized into the canonical domain
model.

## HTML Comments

HTML comments SHALL NOT be required for the semantic interpretation of
canonical ATON engineering content.

Implementations MAY preserve comments as source information where supported,
but comments SHALL NOT carry normative engineering semantics.

## Escaping

Markdown escaping SHALL be supported according to the applicable Markdown
parser semantics.

Escaping SHALL be used where required to represent Markdown control
characters as literal content.

Escaping SHALL NOT be used to encode engineering metadata or relations.

## Character Encoding

Canonical ATON Markdown SHALL use UTF-8 encoding.

Implementations SHALL preserve Unicode characters without requiring a
locale-specific character encoding.

A canonical artifact SHALL NOT depend on a platform-specific text encoding.

## Line Endings

Implementations SHOULD use UTF-8 text with a consistent line-ending
representation.

Differences in line-ending representation SHALL NOT alter the semantic
meaning of engineering content.

Git normalization MAY be used to maintain repository consistency.

## Whitespace

Whitespace differences that do not change Markdown semantics SHALL NOT alter
the semantic meaning of an engineering artifact.

Implementations SHOULD avoid unnecessary whitespace-only changes because they
create unnecessary Git revisions.

## Deterministic Rendering

A conforming renderer SHALL interpret canonical ATON Markdown according to
this profile.

Rendering MAY differ in visual appearance between implementations.

Such presentation differences SHALL NOT change the semantic meaning of the
engineering content.

## Markdown and Engineering Semantics

Markdown structure SHALL remain distinct from Engineering Knowledge Model
semantics.

For example:

- a Markdown heading is not an Entity;
- a Markdown link is not automatically a Relation;
- a list is not automatically a Collection;
- a checkbox is not automatically a Process state;
- a table is not automatically structured engineering data.

Engineering semantics SHALL be represented through the canonical domain model,
metadata and relations.

## Markdown and Artifact Identity

Markdown SHALL NOT define artifact identity.

Artifact identity SHALL be persisted explicitly according to RFC-0030.

Moving or renaming a Markdown file SHALL therefore not inherently change the
identity of the engineering artifact.

## Markdown and Traceability

Markdown MAY contain hyperlinks that help users navigate engineering
knowledge.

Such hyperlinks SHALL be considered presentation or authoring constructs
unless explicitly mapped to canonical Engineering Knowledge Model relations.

Traceability SHALL be represented through canonical relations.

This ensures that traceability remains available independently of a Markdown
renderer.

## Extensions

ATON implementations MAY support additional Markdown extensions.

An extension SHALL be considered non-canonical unless explicitly included in
the ATON Markdown Profile or another normative Foundation specification.

Non-canonical extensions:

- SHALL NOT be required for interpreting canonical engineering content;
- SHALL NOT define mandatory engineering semantics;
- SHALL NOT make the content dependent on a specific renderer; and
- SHOULD be safely ignored or represented as unsupported content by other
  implementations.

Future extensions SHALL define their syntax, semantics, interoperability
requirements and compatibility implications before becoming canonical.

## Conformance Levels

An implementation MAY provide the following capabilities:

### Core Conformance

Core conformance requires support for the canonical Markdown constructs
defined as required by this profile.

### Extended Conformance

Extended conformance MAY include standardized ATON Markdown extensions.

An extended implementation SHALL remain capable of processing Core
conformant content.

### Rendering Extensions

A renderer MAY provide additional presentation features without claiming
that those features are part of canonical ATON Markdown.

## Validation

A Markdown validator MAY verify:

- valid UTF-8 encoding;
- supported Markdown syntax;
- prohibited HTML usage;
- prohibited MDX or JSX usage;
- unsupported canonical extensions;
- structural Markdown errors; and
- profile conformance.

Markdown validation SHALL remain distinct from Engineering Knowledge Model
validation.

A document may therefore be valid Markdown while containing engineering
content that violates domain or relation constraints.

## Compatibility

This RFC is compatible with ADR-0002 because Markdown remains the canonical
format for engineering content.

This RFC is compatible with RFC-0030 because artifact metadata and relations
remain separate from Markdown content.

This RFC is compatible with the canonical domain model because Markdown is
treated as a serialization of content rather than as the domain model itself.

## Consequences

### Positive

- ATON engineering content remains highly portable.
- Canonical content does not depend on Docusaurus or MDX.
- Different Markdown renderers can process the same engineering content.
- Engineering semantics remain separate from presentation syntax.
- Metadata and relations remain independently machine-readable.
- Future Markdown extensions can be standardized explicitly.

### Negative

- Some renderer-specific Markdown features cannot be used as canonical
  engineering content.
- Rich presentation may require non-canonical extensions.
- Implementations may need separate rendering profiles for advanced
  presentation features.

## Out of Scope

This RFC does not define:

- engineering metadata;
- engineering relations;
- artifact serialization;
- ontology semantics;
- engineering process semantics;
- versioning;
- user interface behaviour;
- rendering style;
- document themes; or
- specific Markdown parser implementations.

## Acceptance Criteria

A conforming implementation SHALL:

1. support the canonical Markdown constructs defined by this profile;
2. process UTF-8 encoded canonical content;
3. preserve the distinction between Markdown content and artifact metadata;
4. preserve the distinction between Markdown links and semantic relations;
5. not require MDX or JSX for canonical content;
6. not require raw HTML for canonical content;
7. not require renderer-specific directives;
8. preserve Markdown content across supported persistence implementations;
9. allow non-canonical rendering extensions without changing canonical
   semantics; and
10. remain compatible with RFC-0030 artifact serialization.

## References

- ADR-0002 Markdown as the Canonical Authoring Format
- RFC-0030 Canonical Engineering Artifact Serialization
- NOTE-0003 Supported Markdown Profile

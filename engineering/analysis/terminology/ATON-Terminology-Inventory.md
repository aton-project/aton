> This document is an engineering analysis artifact.
> It is non-normative and does not define ATON semantics.

Analyse-Basis (Git-Commit): `692cc56bd9b141f9c10ea83dd7706d93905bc1c3`

Datum: `2026-09-16`

Der folgende Bericht wird vollständig aus der bisherigen Analyse übernommen. Aussagen über den damaligen ausschließlich lesenden Ablauf dokumentieren den Ablauf vor der Speicherung dieses Analyseartefakts. Empfehlungen und als normativ bezeichnete Aussagen geben Bewertungen beziehungsweise den Anspruch der genannten Quellen wieder; dieses Dokument selbst legt keine ATON-Semantik fest.

# ATON Terminology Inventory

**Analysierter Stand:** `692cc56 — docs(glossary): add Relation term`, Branch `development`. Das Arbeitsverzeichnis war vor und nach der Analyse sauber. Es wurden keine Dateien erzeugt oder verändert, kein Commit erstellt und kein Push ausgeführt.

Die Analyse berücksichtigt die Constitution, beide Foundation-READMEs, sämtliche Bereiche unter `foundation/specifications/` einschließlich AX sowie die vorhandenen Metadaten, Relationen und Prädikat-Constraints.

**Quellenlage:**

| Quellenbereich | Aktueller Bestand und Status |
|---|---|
| Constitution | Version 1.0.0, Accepted |
| ADRs | 9 Accepted, 9 Proposed |
| RFCs | 1 Accepted, 18 Draft, 5 Proposed |
| Ontology | 23 Definitionen, alle Draft |
| Universal Entity Model | 1 Definition, Draft |
| Konkrete Predicate-Definitionen | 4, alle Draft |
| Glossary Entries | 4, alle Draft |
| AX | 10 Dokumente, alle Draft |
| Schemas und Templates | Dateien vorhanden, aber leer |
| Foundation-Unterbereiche `book`, `examples`, `reference-model`, `tooling` | README-Platzhalter |

**Bewertungsmaßstab:** Die Constitution steht über nachgeordneten Dokumenten. Akzeptierte ADRs haben stärkeres Gewicht als Proposed/Draft-Dokumente. Ein Entwurf mit `SHALL` ist dadurch noch keine akzeptierte Entscheidung. Die nachstehenden Bedeutungsbeschreibungen geben den Quellenstand wieder; sie sind keine neuen Definitionen.

Für die Kategorien gilt:

| Kürzel | Kategorie |
|---|---|
| D | 1. Domain concepts |
| M | 2. Meta concepts |
| A | 3. Artifact/document types |
| P | 4. Properties/attributes |
| R | 5. Relations/predicates |
| G | 6. Process or governance terms |
| I | 7. Implementation terms |
| B | 8. Purely descriptive terminology |

Die Kategorie beschreibt die **Rolle des Begriffs**, nicht den Ablageort seiner Definition. Beispielsweise ist `Property` trotz vorhandener Ontologie-Definition hier Kategorie P. Bei mehrdeutigen Begriffen wird die Mehrdeutigkeit ausdrücklich genannt.

In den Tabellen bedeutet **G/O**: vorhandener Glossareintrag / vorhandene eigenständige Ontologie-Definition. `—` bedeutet jeweils „nicht vorhanden“. Alle angegebenen `ONT-*`-Definitionen und `TERM-*`-Einträge haben Status Draft.

## 1. Canonical terminology candidates

Ein eigener Eintrag erscheint sinnvoll, wenn er eine eigenständige semantische Unterscheidung sichert. **„Ja“ bedeutet eine Empfehlung für die spätere Terminologiearbeit, keine Freigabe einer bestimmten Definition.** „Nach Klärung“ bezeichnet Kandidaten, deren Bedeutung oder Abgrenzung noch eine Entscheidung erfordert.

### Semantische Grundlagen

| Term | Kat. | Bedeutung im aktuellen Quellenstand | Wichtigste Quelle / Status | G/O | Alternative Begriffe, Überschneidungen und Konflikte | Eigener Eintrag |
|---|---|---|---|---|---|---|
| ATON Foundation | M | Kanonische normative Wissensbasis und semantische Grundlage des ATON-Ökosystems. | [ADR-0007](/opt/projects/aton/foundation/specifications/adr/ADR-0007/content.md), Accepted; Constitution, Accepted | — / — | `Foundation`; nicht mit Repository, Book oder Implementierung gleichzusetzen. Schichtengrenzen: K12. | Ja |
| Engineering Operating System | M | Übergreifender ATON-Anspruch: Engineering-Konzepte, Beziehungen, Operationen und Governance unabhängig von konkreten Technologien und Prozessen. | [Constitution](/opt/projects/aton/foundation/constitution/CONSTITUTION/content.md), Accepted | — / — | Keine Betriebssystemsemantik im technischen Sinn festgelegt; Überschneidung mit Plattform und Foundation. | Ja, zur Abgrenzung |
| Engineering Knowledge | M | Das fachliche Wissen, das ATON beschreibt, verbindet, verwaltet und weiterentwickelt. | Constitution; [ADR-0004](/opt/projects/aton/foundation/specifications/adr/ADR-0004/content.md), Accepted | — / — | `engineering information` wird teilweise ähnlich verwendet; Verhältnis zu Content und Metadata nicht vollständig einheitlich, K3. | Ja |
| Engineering Knowledge Model | M | Semantisches Modell der Engineering-Konzepte und ihrer Zusammenhänge. | [ADR-0006](/opt/projects/aton/foundation/specifications/adr/ADR-0006/content.md), Accepted; ADR-0011, Proposed | — / — | `Knowledge Model`, `logical Engineering Knowledge Model`; nicht automatisch identisch mit Graph oder internem Code-Modell, K11. | Ja |
| Engineering Knowledge Graph | M | Kanonische logische Organisation von Engineering-Wissen durch explizite Beziehungen. | ADR-0006, Accepted | — / — | `knowledge graph`; Überschneidung mit Knowledge Model, aber ausdrücklich dessen graphartige Organisation. | Ja |
| Engineering Kernel | M | In der Constitution der semantische Kern aus Konzepten, Beziehungen, Operationen und Constraints. | Constitution, Accepted | — / — | `Kernel` bezeichnet in ADRs auch ausführende Softwarekomponenten. K11. | Nach Klärung |
| Entity | M | Unabhängig identifizierbare Einheit beziehungsweise logisches Konzept des Engineering-Wissens. | ADR-0004, Accepted; [ENTITY-0001](/opt/projects/aton/foundation/specifications/entity/ENTITY-0001/content.md), Draft | TERM-Entity / ONT-Entity | `Engineering Entity`; Verhältnis zu Concept, Artifact und obligatorischer Typisierung: K1, K2. | Bereits vorhanden |
| Ontology | M | Definiert die semantischen Kategorien und die Bedeutung beziehungsweise Anwendbarkeit von Prädikaten. | [ADR-0009](/opt/projects/aton/foundation/specifications/adr/ADR-0009/content.md), Accepted; [RFC-0020](/opt/projects/aton/foundation/specifications/rfc/RFC-0020/content.md), Draft | — / — | Nicht gleichbedeutend mit Schema, Ordner oder Programmiersprachen-Typsystem. | Ja |
| Concept | M | Semantische Kategorie beziehungsweise Klasse der Ontologie; konkrete Entities werden darunter interpretiert. | [RFC-0027](/opt/projects/aton/foundation/specifications/rfc/RFC-0027/content.md), Draft | — / — | `Ontology Concept`; allgemeines „engineering concept“ bezeichnet andernorts auch eine Entity. K2. | Ja, mit Abgrenzung |
| Engineering Identity | M | Persistente Identität eines Engineering-Konzepts über seine Veränderungen hinweg. | [RFC-0002](/opt/projects/aton/foundation/specifications/rfc/RFC-0002/content.md), Draft; ADR-0012, Proposed | — / — | `Entity Identity`, teils `semantic identity`; nicht Identifier, Version oder Artifact Identity. K9. | Ja |
| Engineering Version | M | Unterscheidbarer semantischer Zustand einer Entity bei gleichbleibender Engineering Identity. | [ADR-0012](/opt/projects/aton/foundation/specifications/adr/ADR-0012/content.md), Proposed; RFC-0012, Draft | — / — | `Version` nur kontextabhängig; nicht Artifact Revision oder Git Revision. K9. | Ja |
| Physical Representation | I | Konkrete Darstellung für Persistenz, Austausch oder Präsentation. Semantisch relevant als Grenze des Modells. | [ADR-0011](/opt/projects/aton/foundation/specifications/adr/ADR-0011/content.md), Proposed; RFC-0015, Proposed | — / — | `physical representation`, technische Repräsentation; nicht vorschnell mit Artifact gleichsetzen. K1. | Ja, als Grenzbegriff |

### Fachliche Konzepte und Wissensorganisation

| Term | Kat. | Bedeutung im aktuellen Quellenstand | Wichtigste Quelle / Status | G/O | Alternative Begriffe, Überschneidungen und Konflikte | Eigener Eintrag |
|---|---|---|---|---|---|---|
| Requirement | D | Aussage über eine notwendige Fähigkeit, Bedingung oder Einschränkung eines Systems oder Engineering-Objekts. | [ONT-Requirement](/opt/projects/aton/foundation/specifications/ontology/Requirement/content.md), Draft | — / ONT-Requirement | Nicht Requirement Document; „capability“ in dieser Definition nicht automatisch Architekturschicht Capability. | Ja |
| Component | D | Identifizierbarer Baustein, der zu Struktur oder Verhalten eines Systems beiträgt. | [ONT-Component](/opt/projects/aton/foundation/specifications/ontology/Component/content.md), Draft | — / ONT-Component | Überschneidung des Wortes mit UI-Komponente und Softwarekomponente; diese sind keine automatischen Synonyme. | Ja |
| Interface | D | Definierte Grenze, über die Komponenten, Systeme oder andere Entities interagieren. | [ONT-Interface](/opt/projects/aton/foundation/specifications/ontology/Interface/content.md), Draft | — / ONT-Interface | Nicht ausschließlich API oder Benutzeroberfläche. | Ja |
| Test | D | In der Ontologie Engineering-Aktivität **oder** Spezifikation zur Prüfung gegen Erwartungen. | [ONT-Test](/opt/projects/aton/foundation/specifications/ontology/Test/content.md), Draft | — / ONT-Test | Vermischt Aktivität und Dokument/Spezifikation; Verhältnis zu Testausführung und Evidence offen. K10. | Nach Klärung |
| Collection | M | Identifizierbare logische Gruppierung mit bestimmter Mitgliedschaft. | [ONT-Collection](/opt/projects/aton/foundation/specifications/ontology/Collection/content.md); [RFC-0022](/opt/projects/aton/foundation/specifications/rfc/RFC-0022/content.md), Draft | — / ONT-Collection | Nicht Verzeichnis, View oder Baseline. Mitgliedschaft ist nicht automatisch gewöhnliche Domain-Relation. K8. | Ja |
| View | M | Abgeleitete Perspektive, Projektion oder Präsentation kanonischen Wissens. | ADR-0004, Accepted; [RFC-0021](/opt/projects/aton/foundation/specifications/rfc/RFC-0021/content.md), Draft | — / ONT-View | `Navigation View` als Spezialisierung; View, View Definition und gerenderte Ausgabe unterscheiden. K11. | Ja |
| Baseline | D | Explizite, reproduzierbare Auswahl eines Engineering-Zustands. | [RFC-0013](/opt/projects/aton/foundation/specifications/rfc/RFC-0013/content.md), Draft; ADR-0012, Proposed | — / — | `Engineering Baseline`; nicht bloße Collection, Git Commit oder Tag. | Ja |
| Release | G | Explizit freigegebener Engineering-Zustand beziehungsweise eine freigegebene Baseline. | ADR-0012, Proposed | — / — | `Engineering Release`; Baseline ist Zustandsauswahl, Release fügt Freigabesemantik hinzu. Details offen. | Ja |
| Traceability | D | Fähigkeit, explizite Beziehungen zwischen Engineering-Wissen festzustellen, zu untersuchen, zu navigieren und zu prüfen. | Constitution, ADR-0006, Accepted; [RFC-0023](/opt/projects/aton/foundation/specifications/rfc/RFC-0023/content.md), Draft | — / — | Kein eigener paralleler Graph und keine bloße Matrix. | Ja |
| Engineering Knowledge Navigation | D | Entdecken und Traversieren des logischen Wissensmodells anhand semantischer Verbindungen. | ADR-0006, Accepted; [ADR-0018](/opt/projects/aton/foundation/specifications/adr/ADR-0018/content.md), Proposed | — / — | `Navigation`; Abgrenzung zu Search und Dateisystemnavigation, K13. | Ja |
| Provenance | M | Information über Herkunft, Entstehung und beitragende Quellen beziehungsweise Aktivitäten. | [RFC-0012](/opt/projects/aton/foundation/specifications/rfc/RFC-0012/content.md), Draft; AX-0010, Draft | — / — | `origin`, `history` decken jeweils nur Teile ab; nicht Identität, Autorität oder Traceability insgesamt. | Ja |

### Artifact- und Dokumenttypen

| Term | Kat. | Bedeutung im aktuellen Quellenstand | Wichtigste Quelle / Status | G/O | Alternative Begriffe, Überschneidungen und Konflikte | Eigener Eintrag |
|---|---|---|---|---|---|---|
| Artifact | A | Repräsentation von Engineering-Wissen; Quellen unterscheiden sich darin, ob diese primär physisch/adressierbar oder selbst logisch-semantisch ist. | ADR-0004, Accepted; [ONT-Artifact](/opt/projects/aton/foundation/specifications/ontology/Artifact/content.md), Draft; RFC-0010, Draft | TERM-Artifact / ONT-Artifact | `Engineering Artifact`; Konflikt K1. | Bereits vorhanden; Abstimmung erforderlich |
| Constitution | A | Höchstes Architektur- und Governance-Dokument der Foundation. | Constitution, Accepted | — / ONT-Constitution | Dokumenttyp und konkrete Instanz `CONSTITUTION` unterscheiden. | Ja |
| Specification | A | Dokument beziehungsweise Wissenselement, das normatives Verhalten oder Regeln festlegt. | Constitution, Accepted; Specifications README ohne Lifecycle-Status | — / — | Nicht automatisch synonym mit RFC; RFC kann noch Vorschlag sein. | Ja |
| Architecture Decision Record | A | Dokumentierte Architekturentscheidung mit Begründung und Konsequenzen. | [ONT-ADR](/opt/projects/aton/foundation/specifications/ontology/ADR/content.md), Draft; ADR-0017, Proposed | — / ONT-ADR | `ADR`; Architecture Decision als Entscheidung und Record als Repräsentation sind nicht sauber durchgängig getrennt. K10. | Ja |
| Request for Comments | A | Formale Spezifikation oder Vorschlag mit Regeln, Verhalten oder Schnittstellen. | [RFC-0000](/opt/projects/aton/foundation/specifications/rfc/RFC-0000/content.md), Accepted; ONT-RFC, Draft | — / ONT-RFC | `RFC`; weder Name noch Existenz bedeuten automatisch Akzeptanz. | Ja |
| Definition | M | Festlegung der präzisen Bedeutung eines Konzepts, Begriffs oder einer Property. | [ONT-Definition](/opt/projects/aton/foundation/specifications/ontology/Definition/content.md), Draft | — / ONT-Definition | Kann auch als definierendes Artifact auftreten; Verhältnis zu Glossary Entry klären, K14. | Ja |
| Glossary Entry | A | Verwalteter Terminologieeintrag mit Begriff und Bedeutung. | [ONT-GlossaryEntry](/opt/projects/aton/foundation/specifications/ontology/GlossaryEntry/content.md), Draft; Glossary README ohne Lifecycle-Status | — / ONT-GlossaryEntry | `GlossaryEntry` ist technische Schreibweise; Term und verwalteter Eintrag sind verschiedene Dinge. | Ja |
| Note | A | Aufzeichnung von Beobachtung, Problem, Idee oder Hypothese als Input für Bewertung und Entscheidungen. | [ONT-Note](/opt/projects/aton/foundation/specifications/ontology/Note/content.md), Draft | — / ONT-Note | `Engineering Note`; kein Synonym für Finding oder Decision. Widersprüchlich wirkende Aussage zur Ontologiezugehörigkeit, K10. | Ja |
| Finding | D | Identifiziertes Ergebnis, Beobachtung, Problem oder Schlussfolgerung aus Untersuchung oder Bewertung. | [ONT-Finding](/opt/projects/aton/foundation/specifications/ontology/Finding/content.md), Draft; ADR-0015, Proposed | — / ONT-Finding | Ontologie nennt es Artifact, ADR-0015 kontextuelle Entity. Nicht jede beiläufige Beobachtung ist automatisch Finding. K10. | Nach Klärung |
| ATON Experience | A | Spezifikation, wie Engineering-Wissen dargestellt, erkundet und verstanden wird. | [AX-0001](/opt/projects/aton/foundation/specifications/ax/AX-0001/content.md); ONT-AX, Draft | — / ONT-AX | `AX`; bezeichnet auch den übergreifenden Erfahrungsanspruch. Kein UI-Framework oder Theme. | Ja |
| Artifact Revision | M | Revision eines Artifacts beziehungsweise seiner Repräsentation. | ADR-0012, Proposed; [RFC-0010](/opt/projects/aton/foundation/specifications/rfc/RFC-0010/content.md), Draft | — / — | `Revision` allein ist mehrdeutig; Abgrenzung zu Engineering Version und physischer Revision folgt K1/K9. | Ja, mit Abgrenzung |

### Properties, Typisierung und Constraints

| Term | Kat. | Bedeutung im aktuellen Quellenstand | Wichtigste Quelle / Status | G/O | Alternative Begriffe, Überschneidungen und Konflikte | Eigener Eintrag |
|---|---|---|---|---|---|---|
| Property | P | Benanntes semantisches Merkmal beziehungsweise Wert eines Engineering-Konzepts. | [ONT-Property](/opt/projects/aton/foundation/specifications/ontology/Property/content.md); [RFC-0005](/opt/projects/aton/foundation/specifications/rfc/RFC-0005/content.md), Draft | — / ONT-Property | `Attribute` nicht ausdrücklich als gleichwertig definiert; nicht jedes physische Feld ist Property. | Ja |
| Metadata | P | Beschreibende Information zu Identität, Klassifikation, Lifecycle und Verarbeitung; Zielobjekt variiert zwischen Artifact und Entity. | [ADR-0005](/opt/projects/aton/foundation/specifications/adr/ADR-0005/content.md), Accepted; ONT-Metadata, Draft | — / ONT-Metadata | `Engineering Metadata`; Abgrenzung zu Content und Property, K3. | Ja |
| Canonical Metadata | P | Explizit repräsentierte, autoritative semantische Metadaten unabhängig von Persistenzsystemen. | [ADR-0010](/opt/projects/aton/foundation/specifications/adr/ADR-0010/content.md), Proposed | — / — | Nicht synonym mit sämtlichen persistierten Metadaten; Verhältnis zu Derived Metadata, K3. | Ja |
| Ontology Type | P | Explizite Zuordnung zu genau einem kanonischen Ontologie-Konzept für teilnehmende Artifacts. | [ADR-0008](/opt/projects/aton/foundation/specifications/adr/ADR-0008/content.md), Accepted | — / — | `canonical ontology type`; `ontologyType` ist Feldname. Nicht `type`/`entityType` oder Verzeichnisname. K2. | Ja |
| Identifier | P | Stabiles Kennzeichen einer Identität innerhalb des geltenden Scopes. | RFC-0002, Draft; ENTITY-0001, Draft | — / — | `ID`, `identity identifier`; Identität und ihr Kennzeichen sind nicht dasselbe. | Ja |
| Lifecycle State | P | Semantischer Zustand eines Wissenselements; bei ADRs vorgeschlagener expliziter Lebenszyklus. | [ADR-0017](/opt/projects/aton/foundation/specifications/adr/ADR-0017/content.md), Proposed | — / — | `Lifecycle Status`; `status` ist Repräsentation. Nicht Process State oder Version. K9. | Ja |
| Semantic Constraint | M | Regel, die die semantische Zulässigkeit einer Verwendung bestimmt; bei Relationen ein Prädikatvertrag. | ADR-0009, Accepted | — / — | `Constraint` ist weiter gefasst und umfasst auch Property-/Process-Constraints. K4/K5. | Ja |
| Allowed Pair | M | Eine ausdrücklich erlaubte Kombination von Source- und Target-Concept. | [RFC-0029](/opt/projects/aton/foundation/specifications/rfc/RFC-0029/content.md), Proposed | — / — | `allowed source-to-target Concept pair`; nicht zwei unabhängig kombinierbare Typmengen. K5. | Ja |
| Constraint Pattern | M | Explizite Regel zum Matching einer Position eines Allowed Pair. | RFC-0029, Proposed | — / — | Nicht selbst ein Ontologie-Konzept; `ANY-CONCEPT` ist konkretes Pattern. | Ja |
| Cardinality | P | Zulässige Zahl von Target-Relationen je Source und Predicate; Property-Multiplizität ist verwandte Verwendung. | [RFC-0026](/opt/projects/aton/foundation/specifications/rfc/RFC-0026/content.md), Draft; RFC-0029, Proposed | — / — | `Multiplicity` nur kontextabhängig; nicht Allowed-Pair-Matching. | Ja |
| Engineering Content | M | Fachlicher Inhalt eines Artifacts, getrennt von Metadaten und Beziehungen. | ADR-0005, Accepted | — / — | `Content`; nicht das gesamte Engineering Knowledge. Abgrenzung K3. | Ja |

### Relations und konkrete Predicates

Für alle nachstehenden konkreten Prädikate gilt: **kein eigener `TERM-*`-Eintrag und keine eigene Definition unter `ontology/`**. Die vier `PRED-*`-Artifacts sind eigenständige Prädikatdefinitionen vom Typ `ONT-Predicate`, keine zusätzlichen `ONT-*`-Konzepte.

| Term | Kat. | Aktuelle Bedeutung | Wichtigste Quelle / Status | Definition vorhanden | Alternative/Überschneidung/Konflikt | Eigener Eintrag |
|---|---|---|---|---|---|---|
| Relation | R | Konkrete semantische Verbindung zwischen Source und Target über ein Predicate. | ADR-0006, Accepted; ONT-Relation, Draft | TERM-Relation / ONT-Relation | `Engineering Relation`, `Relation Instance`; Typ/Instanz und Identität, K2/K9. | Bereits vorhanden |
| Predicate | R | Bedeutung und Anwendbarkeit eines Beziehungstyps. | ADR-0009, Accepted; ONT-Predicate, Draft | TERM-Predicate / ONT-Predicate | `Ontological Predicate`, kontextabhängig `Relation Type`; nicht konkrete Relation. K2/K4. | Bereits vorhanden |
| references | R | Expliziter Verweis auf eine Quelle von Information oder Kontext. | [PRED-references](/opt/projects/aton/foundation/specifications/predicates/references/content.md), Draft | PRED-references | Invers `referencedBy`; Text und Constraints widersprechen sich, K6. | Ja, nach Klärung |
| motivates | R | Note oder Finding liefert Motivation beziehungsweise Evidenz für ADR. | [PRED-motivates](/opt/projects/aton/foundation/specifications/predicates/motivates/content.md), Draft | PRED-motivates | Invers `motivatedBy`; kein beliebiger Bezug auf `Decision`. | Ja |
| governs | R | Source legt Regeln oder Constraints für Target fest. | [PRED-governs](/opt/projects/aton/foundation/specifications/predicates/governs/content.md), Draft | PRED-governs | Invers `governedBy`; Constitution-Paare fehlen in RFC-0027, K7. | Ja |
| refines | R | Detailliertere oder spezialisierte Darstellung bei Erhaltung der wesentlichen Absicht. | [PRED-refines](/opt/projects/aton/foundation/specifications/predicates/refines/content.md), Draft | PRED-refines | Invers `refinedBy`; nicht gleich `specializes`; AX-Paar nur in konkreten Constraints, K7. | Ja |
| specifies | R | RFC spezifiziert eine Architekturentscheidung; RFC → ADR. | RFC-0027, Draft | Nur RFC-Definition | Invers `specifiedBy`; nicht `defines`. | Ja, Status kenntlich machen |
| implements | R | Component realisiert RFC oder Requirement. | RFC-0027, Draft | Nur RFC-Definition | Invers `implementedBy`; Realisierung ist keine Verifikation. | Ja, Status kenntlich machen |
| verifies | R | Test liefert Verifikationsevidenz für Requirement, Component oder RFC. | RFC-0027, Draft | Nur RFC-Definition | Invers `verifiedBy`; mit Test-Semantik K10 verbunden. | Ja, nach Klärung |
| defines | R | Definition, GlossaryEntry, RFC oder ADR definiert bestimmte Wissenselemente gemäß erlaubten Paaren. | RFC-0027, Draft | Nur RFC-Definition | Invers `definedBy`; Verhältnis zur Definitionsautorität, K14. | Ja |
| allocates | R | Requirement wird dem für seine Realisierung verantwortlichen Component zugeordnet. | RFC-0027, Draft | Nur RFC-Definition | Invers `allocatedFrom`; Zuordnung ist nicht bereits Implementierung. | Ja |
| specializes | R | Spezifischere Form eines Concept oder Artifacts; Taxonomie. | RFC-0027, Draft | Nur RFC-Definition | Invers `specializedBy`; keine automatische Ausweitung der Prädikatanwendbarkeit. | Ja |
| contains | R | Semantische Mitgliedschaft beziehungsweise Zugehörigkeit, etwa Review → Finding. | RFC-0027, Draft | Nur RFC-Definition | Invers `containedIn`; nicht physische Verschachtelung. Collection-Abgrenzung K8. | Ja, nach Klärung |

Die Empfehlung für diese Prädikate beruht auf ihren **unterschiedlichen zulässigen Aussagen**, nicht auf ihrer Häufigkeit. Ein späterer Glossareintrag sollte auf die autoritative Prädikatdefinition verweisen und keine zweite unabhängige Constraint-Definition schaffen.

### Prozess, Governance und Architekturschichten

| Term | Kat. | Bedeutung im aktuellen Quellenstand | Wichtigste Quelle / Status | G/O | Alternative Begriffe, Überschneidungen und Konflikte | Eigener Eintrag |
|---|---|---|---|---|---|---|
| Decision | G | Beabsichtigte Auswahl zwischen Alternativen und daraus resultierende Festlegung. | [ONT-Decision](/opt/projects/aton/foundation/specifications/ontology/Decision/content.md), Draft | — / ONT-Decision | `Engineering Decision`; Architecture Decision ist spezieller, ADR der Record. K10. | Ja |
| Architecture Decision | G | Architekturbezogene Entscheidung mit eigener vorgeschlagener Lifecycle-Semantik. | ADR-0017, Proposed; Constitution, Accepted | — / keine separate ONT-ArchitectureDecision | Häufig mit ADR gleichgesetzt; Entscheidung versus Aufzeichnung, K10. | Nach Klärung |
| Review | G | Strukturierte Untersuchung von Engineering-Wissen; Ontologie beschreibt sie als Artifact. | [ONT-Review](/opt/projects/aton/foundation/specifications/ontology/Review/content.md), Draft; ADR-0015, Proposed | — / ONT-Review | Untersuchung, Prozessinstanz und Ergebnisaufzeichnung nicht vollständig getrennt. K10. | Nach Klärung |
| Engineering Task | G | Koordiniert und steuert Engineering-Arbeit, ohne einen konkreten Prozess vorzuschreiben. | Constitution, Accepted | — / — | `Task`; Verhältnis zu Activity nicht definiert. K12. | Ja, Definition noch unvollständig |
| Engineering Process | G | Definierte Aktivitäten und ihre Beziehungen; generisches Modell ohne verbindliche Methodik vorgeschlagen. | [ADR-0016](/opt/projects/aton/foundation/specifications/adr/ADR-0016/content.md), Proposed | — / — | `Process`; kein automatisches Synonym für Workflow oder Process Profile. K12. | Ja |
| Process Definition | G | Wiederverwendbare Struktur und Semantik eines Prozesses. | ADR-0016, Proposed | — / — | Nicht dessen konkrete Ausführung oder Process Instance. | Ja |
| Process Instance | G | Ausführung einer Process Definition in einem bestimmten Engineering-Kontext. | ADR-0016, Proposed | — / — | `process execution` beschreibt die Durchführung, nicht zwingend dasselbe Objekt. | Ja |
| Activity | G | Identifizierbare Einheit von Engineering-Arbeit innerhalb eines Prozesses. | ADR-0016, Proposed | — / — | `Engineering Activity`; Verhältnis zu Task offen. K12. | Ja, nach Abgrenzung |
| Process State | G | Definierter Zustand eines Prozesses oder einer Activity. | ADR-0016, Proposed | — / — | Nicht Entity-/ADR-Lifecycle-State. | Ja |
| Transition | G | Zulässiger Wechsel zwischen Process States; Lifecycle-Transitions sind ein anderer Kontext. | ADR-0016, Proposed; ADR-0017, Proposed | — / — | `State Transition`; kein Git- oder Dateiereignis. | Ja, kontextspezifisch |
| Verification | G | Prüfung expliziter Bedingungen; für Relationen Trennung struktureller und semantischer Gültigkeit. | ADR-0009, Accepted; ADR-0016, Proposed | — / — | `Validation` wird überlappend verwendet; keine allgemeine V&V-Abgrenzung festgelegt. | Ja |
| Profile | G | Architekturschicht für Policies und Engineering-Prozesse. | Constitution, Accepted | — / — | `Process Profile` als spezifische Verwendung; `Markdown Profile` betrifft einen anderen Gegenstand. K12. | Ja |
| Capability | M | Architekturschicht, die Engineering-Dienste bereitstellt. | Constitution, Accepted | — / — | Nicht jede erwähnte „capability“ ist dadurch ein kanonisches Capability-Objekt. | Ja |
| Application | M | Architekturschicht für Benutzerinteraktion. | Constitution, Accepted | — / — | Nicht Foundation oder Capability; konkrete UI-Technologie ist Implementierung. | Ja |
| Governance | G | Regeln und Verantwortlichkeiten für nachvollziehbare Weiterentwicklung und autorisierte Zustandsänderungen. | Constitution, Accepted; ADR-0017, Proposed | — / — | `Engineering Governance`; nicht gleich Lifecycle oder vorgeschriebener Review-Workflow. | Ja |

## 2. Supporting terminology

Diese Begriffe helfen beim Verständnis des Modells. Häufig genügt ihre Definition **innerhalb eines übergeordneten Glossareintrags oder einer Spezifikation**.

Soweit nicht anders angegeben, besitzen sie **weder Glossary Entry noch eigenständige Ontology Definition**. Alternative Bezeichnungen sind nur dort genannt, wo sie inhaltlich relevant sind; ansonsten ist kein belastbares Synonym festgestellt.

| Term | Kat. | Bedeutung und wichtigste Quelle / Status | Überschneidung oder möglicher Konflikt | Empfehlung |
|---|---|---|---|---|
| Thing | M | Allgemeinste identifizierbare konzeptionelle Kategorie; ONT-Thing, Draft. **O: ONT-Thing.** | Abgrenzung zu Entity und Concept sowie Taxonomie kaum ausgearbeitet. | Bedingt eigener Eintrag; Ontologieexistenz allein genügt nicht. |
| Canonical Domain Model / Representation | I | Einheitliche interne Repräsentation pro Domain-Konzept; ADR-0008, Accepted. | Nicht identisch mit logischer Semantik oder Serialisierung, K11. | Unterstützende Architekturterminologie; ggf. ein gemeinsamer Eintrag. |
| Artifact Identity | M | Identität des Artifacts getrennt von der repräsentierten Entity; ADR-0013, Proposed; RFC-0010, Draft. | Hängt unmittelbar von Artifact-Abgrenzung K1 ab. | Unter Artifact behandeln; Eigenständigkeit später entscheiden. |
| Version Identity | P | Kennzeichen eines bestimmten Engineering-Zustands; RFC-0012, Draft. | Nicht Engineering Identity und nicht Git Hash. | Unter Engineering Version. |
| Identity Scope | M | Geltungsbereich der Identifikatoreindeutigkeit; RFC-0002, Draft. | Foundation-weite versus verteilte Scopes noch nicht abschließend festgelegt. | Unter Engineering Identity; ggf. eigener Eintrag bei Föderation. |
| Identity Resolution | I | Auflösung einer kanonischen Identität auf zugängliches Wissen; RFC-0002, Draft. | Auflösung ist nicht Identität; externe Auflösung ist nicht automatisch Typprüfung. | Unter Identity/Representation. |
| Addressability | P | Möglichkeit, eine Entity über ihre Identität anzusprechen; RFC-0001, Draft. | URL/Pfad ist Zugriffsmittel, kein notwendiger Identitätsinhalt. | Unter Entity/Identity. |
| External Entity / External Target | M | Entity außerhalb der lokalen Artifact-Persistenz; RFC-0028, Draft. | Extern bedeutet weder unbekannt noch semantisch ungültig. Typisierung noch unvollständig. | Unterstützend; eigener Eintrag nach Festlegung des externen Modells. |
| Contextual Entity | M | Entity mit explizitem semantischem Kontext; ADR-0015, Proposed. | `Embedded Entity` beschreibt oft nur Speicherung; kein neuer fundamentaler Entity-Typ. | Unter Entity; nicht vorschnell eigener Typ. |
| Contextual Ownership / Containment | R | Bedeutungsvolle Zuordnung zu einem Kontext; ADR-0015, Proposed. | Nicht Verzeichnisverschachtelung; Abgrenzung zu `contains`, K8. | Unter Kontext/Containment; Prädikatmodell abwarten. |
| Source / Target | R | Rollen der Endpunkte einer Relation; RFC-0004, Draft. | Keine eigenständigen Entity-Typen. | Im Relation-Eintrag definieren. |
| Explicit Relation | R | Direkt repräsentierte, autoritative Beziehung; RFC-0027, Draft. | Nicht aus Darstellung oder Nähe ableiten. | Unter Relation. |
| Derived Relation / Inferred Relation | R | Aus autoritativen Daten nach definierten Regeln abgeleitete Beziehung; RFC-0004/-0027, Draft. | Nicht stillschweigend explizite Quelle; „derived“ und „inferred“ nicht überall formal getrennt. | Unter Relation; eigene Definition nur bei Ausbau des Reasoning-Modells. |
| Inverse Predicate | R | Explizit definierte Umkehrbeziehung eines Prädikats; RFC-0026, Draft. | Nicht bloße Umkehrnavigation und nicht zwingend doppelt gespeichert. | Unter Predicate; bei Bedarf eigener unterstützender Eintrag. |
| Domain / Range | P | Zulässige Source-/Target-Typen des Prädikatvertrags; ADR-0009, Accepted. | Kein unkontrolliertes kartesisches Produkt ableiten, K5. | Innerhalb Semantic Constraint/Allowed Pair. |
| Symmetry / Transitivity / Directionality | P | Semantische Eigenschaften von Prädikaten; RFC-0004/-0026, Draft. | Nicht aus Graphdarstellung, Namen oder zwei Kanten ableitbar. | Unter Predicate; keine ATON-Neudefinition allgemeiner Logikbegriffe. |
| ANY-CONCEPT | M | Constraint Pattern für jedes gültige kanonische Ontologie-Konzept; RFC-0029, Proposed. | Kein Wildcard für unbekannte Typen oder beliebige Strings; nicht ONT-Thing. | Unter Constraint Pattern, nicht als Domain Concept. |
| Structural Validity | M | Wohlgeformtheit und strukturelle Prüfbarkeit einer Relation; ADR-0009, Accepted. | Beweist keine semantische Gültigkeit. | Unter Verification. |
| Semantic Validity | M | Einhaltung des definierten Prädikatvertrags; ADR-0009, Accepted. | Predicate-/Target-Existenz allein reicht nicht. | Unter Verification. |
| Derived Information / Derived Metadata | P | Abgeleitete Zusatzinformation; ADR-0010, Proposed; RFC-0003, Draft. | Nicht automatisch canonical oder authoritative. | Im Metadata-Eintrag abgrenzen. |
| Persisted Metadata | P | Gespeicherte Metadaten; RFC-0003, Draft. | Persistenz begründet nicht allein Autorität. | Unter Metadata. |
| Metadata Authority / Authoritative Metadata | G | Festlegung der maßgeblichen Quelle eines Wertes; ADR-0010, Proposed. | Nicht „Datei existiert“ und nicht „neuester Timestamp“. | Unter Canonical Metadata/Governance. |
| Materialization | G | Explizite Überführung abgeleiteter Information in kanonische Information; ADR-0010, Proposed. | Keine bloße Cache-Erzeugung. | Unterstützender Eintrag sinnvoll, wenn diese Operation formalisiert wird. |
| Temporal Metadata | P | Zeitangaben zu genau bezeichneten Ereignissen; RFC-0003, Draft. | Engineering-, Git- und Dateiereignisse unterscheiden. | Unter Metadata/Provenance. |
| Property Name / Value / Type / Unit / Multiplicity | P | Bestandteile und Einschränkungen semantischer Properties; RFC-0005, Draft. | Physisches Feld oder Datentyp ist nicht automatisch semantische Definition. | Innerhalb Property. |
| Artifact Type / Entity Type | P | Unterschiedlich verwendete Klassifikationsbegriffe; RFC-0001/-0010, Draft; ADR-0008, Accepted. | Semantische Typisierung versus Persistenzklassifikation, K2. | Erst klären, dann ggf. getrennte Einträge. |
| Baseline Membership | R | Zugehörigkeit zum ausgewählten Engineering-Zustand; RFC-0013, Draft. | Nicht beliebige Collection Membership. | Unter Baseline. |
| Collection Membership | R | Zugehörigkeit zu einer logischen Gruppe; RFC-0022, Draft. | Kein Identitätswechsel; nicht automatisch Domain-Relation, K8. | Unter Collection. |
| Static / Dynamic Collection | M | Explizite Mitgliedschaft beziehungsweise regelbasierte Auswahl; RFC-0022, Draft. | „Static“ bedeutet nicht automatisch unveränderliche Baseline. | Unter Collection. |
| View Definition | M | Auswahl- und Darstellungsregeln einer View; RFC-0021, Draft. | Nicht deren ausgewertetes Ergebnis oder physische Ausgabe. | Unter View. |
| Navigation Target / Navigation Path | D | Adressierbares Ziel beziehungsweise Folge semantischer Verbindungen; ADR-0018, Proposed. | Physische Nachbarschaft oder Pfad im Dateisystem zählt nicht automatisch. | Unter Navigation. |
| Search | D | Kriterienbasierte Ermittlung von Kandidaten; ADR-0018, Proposed; AX-0008, Draft. | Navigation traversiert Verbindungen; AX fasst Search zugleich als Navigationsmechanismus auf, K13. | Zunächst unter Navigation abgrenzen. |
| Impact Analysis / Dependency Analysis | D | Auswertung relevanter semantischer Beziehungen auf Auswirkungen und Abhängigkeiten; RFC-0023, Draft. | Kein vollständig festgelegtes generisches Inferenzverfahren. | Unter Traceability; eigene Einträge erst bei präziserem Modell. |
| Traceability Completeness / Consistency | P | Erfüllung erwarteter Beziehungen versus Gültigkeit vorhandener Beziehungen; RFC-0023, Draft. | Vollständigkeit verlangt explizite Erwartungen, nicht bloße Kantenzahl. | Unter Traceability/Verification. |
| Evidence / Verification Result | D | Belege beziehungsweise Ergebnisse einer Prüfung; ADR-0016, Proposed; RFC-0027, Draft. | Nicht gleich Finding, Test oder Review; kein eigenständiges universelles Modell vorhanden. | Nach Abgrenzung mögliche eigene Kandidaten. |
| Role / Responsibility | G | Prozessbezogene Zuständigkeiten und Befugnisse; ADR-0016, Proposed. | Keine universellen Organisationsrollen vorgeschrieben. | Unter Process/Governance. |
| Input / Output | G | Erwartete oder tatsächliche Ein-/Ausgaben einer Activity; ADR-0016, Proposed. | Erwartung und erfüllende konkrete Entity unterscheiden. | Unter Activity/Process. |
| Entry Criteria / Completion Criteria / Process Constraint | G | Bedingungen für Prozessaktivitäten und Übergänge; ADR-0016, Proposed. | Nicht sämtlich Relation Constraints. | Unter Process/Constraint. |
| Proposed / Accepted / Superseded / Rejected / Withdrawn | G | Vorgeschlagene ADR-Lifecycle-Werte; ADR-0017, Proposed. | Keine universelle Statusliste für alle Entity-Typen. | Gemeinsam im Lifecycle-Eintrag, keine fünf isolierten Definitionen. |
| Draft | G | Verwendeter Entwurfsstatus vieler Quellen. | Nicht Teil der in ADR-0017 vorgeschlagenen Mindestliste. Keine überall einheitliche Lifecycle-Semantik dokumentiert. | Unter Quellen-/Lifecycle-Status, nicht stillschweigend normalisieren. |
| Canonical / Inverse / Deprecated / Unresolved | G | Migrationsklassen für Predicates; RFC-0028, Draft. | Andere Achse als Dokumentstatus. | Gemeinsam unter Predicate-Migration. |
| Valid / Invalid / Unknown | G | Prüfresultate im Migrations-/Verifikationskontext; RFC-0028, Draft. | „Unknown“ ist nicht „Unresolved“; letzteres kann ein bekannter ungeklärter Legacy-Fall sein. | Gemeinsam unter Verification. |
| Extension / Domain Library | M | Erweiterungsmöglichkeiten der Foundation; Constitution, Accepted. | Kaum eigenständig operationalisiert; nicht gleich Capability oder Profile. | Unterstützend; spätere eigenständige Definition möglich. |
| Policy / Process Profile | G | Regeln beziehungsweise konfigurierbare Prozessausprägung; Constitution, Accepted. | Verhältnis zu Process Definition nicht festgelegt, K12. | Unter Profile; getrennte Einträge erst nach Abgrenzung. |
| Conformance | G | Übereinstimmung mit anwendbaren normativen Regeln; ADR-0007, Accepted; RFC-0031, Proposed. | Nicht gleich bloße syntaktische Validierung. | Unterstützender übergreifender Eintrag sinnvoll. |
| Immutability / Reproducibility | P | Erhaltung etablierter Zustände beziehungsweise Rekonstruktion desselben semantischen Zustands; ADR-0012, Proposed. | Nicht notwendigerweise Byte-Gleichheit oder unveränderliche Dateipfade. | Unter Version/Baseline. |

## 3. Synonyms and aliases

**Als sprachliche Varianten gut belegt:**

| Bezeichnungen | Einordnung |
|---|---|
| ATON Foundation ↔ Foundation | Kurzform bei eindeutigem ATON-Kontext. |
| Entity ↔ Engineering Entity | Gleicher Grundbegriff in Glossar, Entity-Modell und RFC-0001. |
| Artifact ↔ Engineering Artifact | Sprachliche Varianten; die Bedeutungsabweichung zwischen Quellen bleibt trotzdem bestehen. |
| Relation ↔ Engineering Relation | Varianten desselben Grundbegriffs. |
| Relation Instance ↔ konkrete Relation | Bezeichnet die Anwendung eines Predicate zwischen konkreten Endpunkten. |
| Concept ↔ Ontology Concept | Gleichsetzbar, wenn ausdrücklich die Ontologieebene gemeint ist. |
| Predicate ↔ Ontological Predicate | Variante für den semantischen Beziehungstyp. |
| ADR ↔ Architecture Decision Record | Abkürzung. |
| RFC ↔ Request for Comments | Abkürzung. |
| AX ↔ ATON Experience | Abkürzung. |
| Baseline ↔ Engineering Baseline | Variante im ATON-Kontext. |
| GlossaryEntry ↔ Glossary Entry | Technische versus natürliche Schreibweise. |

**Nur kontextabhängig oder noch nicht als kanonische Aliase abgesichert:**

| Bezeichnungen | Warum keine pauschale Gleichsetzung |
|---|---|
| Knowledge Model ↔ Engineering Knowledge Model | Plausible Kurzform, aber generische Verwendung möglich. |
| Engineering Knowledge ↔ Engineering Information | Quellen verwenden beide, ohne ihre Grenze systematisch festzulegen. |
| Property ↔ Attribute | Kein expliziter Aliasvertrag; Attribute kann Implementierungsbegriff sein. |
| Relation ↔ Relationship ↔ Link | Relationship wird semantisch verwendet; Link kann rein physischer Hyperlink sein. |
| Predicate ↔ Relation Type | In Serialisierung und Fachmodell unterschiedliche Ebenen möglich. |
| Lifecycle State ↔ Status | Status kann auch Dokumentstatus, Process State oder Prüfresultat meinen. |
| Decision ↔ Architecture Decision ↔ ADR | Allgemeine Entscheidung, spezielle Entscheidung und Record sind nicht dieselbe Kategorie. |
| Task ↔ Activity | Beide betreffen Arbeit; ihre Beziehung ist nicht spezifiziert. |
| Version ↔ Revision | Quellen verlangen gerade die Unterscheidung. |
| Profile ↔ Process Profile ↔ Markdown Profile | Gemeinsames Wort, verschiedene fachliche Gegenstände. |
| Verification ↔ Validation | Überlappende Verwendung, keine allgemeine kanonische Gleichsetzung. |
| View ↔ Document ↔ Rendered Representation | Perspektive, Dokumenttyp und konkrete Ausgabe unterscheiden. |

**Keine Synonyme**, sondern gerichtete Gegenstücke sind:

`references/referencedBy`, `motivates/motivatedBy`, `specifies/specifiedBy`, `implements/implementedBy`, `verifies/verifiedBy`, `governs/governedBy`, `defines/definedBy`, `allocates/allocatedFrom`, `refines/refinedBy`, `specializes/specializedBy`, `contains/containedIn`.

Diese inversen Namen sind in Prädikattexten beziehungsweise RFC-0027 dokumentiert; eigenständige `PRED-*`-Verzeichnisse für sie fehlen.

## 4. Potentially deprecated terminology

**Es wurde keine akzeptierte Entscheidung gefunden, die alle folgenden Bezeichnungen verbindlich deprecatet.** Die wesentliche Migrationsquelle ist [RFC-0028](/opt/projects/aton/foundation/specifications/rfc/RFC-0028/content.md), Status Draft.

| Bezeichnung | Kat. | Quellenbefund | Konsequenz für das Inventar |
|---|---|---|---|
| `referenced-by` | R | RFC-0028 klassifiziert sie als deprecated; vorgesehenes Gegenstück ist `referencedBy`. | Potenziell abzulösender Identifier; Migration nur bei passender Source-/Target-Semantik. |
| `dependsOn` | R | RFC-0028: unresolved. Der Schlüssel kommt aktuell in Relationsdateien vor. | Keine kanonische Abhängigkeitssemantik allein aus Verwendung ableiten. |
| `children` | R | RFC-0028: unresolved. | Könnte Containment, Refinement, Specialization oder andere Bedeutung tragen; keine automatische Zuordnung. |
| `related`, `relatedTo` | R | RFC-0028: unresolved. | Unspezifische Verbindung, keine festgelegte fachliche Aussage. |
| `parent`, `child` | R | RFC-0027 schließt sie als generische normative Predicates aus. | Nicht als kanonische Engineering-Relation vorschlagen. |
| `parents` | R | Tatsächlich verwendeter Relationsschlüssel; keine gleichwertig ausgearbeitete kanonische Definition gefunden. | Nicht automatisch mit `parent`, `contains` oder `specializes` gleichsetzen. |
| `supersedes`, `supersededBy` | R | Als Relationsschlüssel vorhanden; Supersession wird im Lifecycle erklärt, aber ohne vollständigen Prädikatvertrag. | **Nicht nachweislich deprecated.** Als unvollständig spezifiziert behandeln. |
| `type`, `entityType` als Ersatz für `ontologyType` | P | ADR-0008 trennt Persistenzklassifikation von Ontologieidentität. | Die Gleichsetzung wäre problematisch; die Felder selbst sind damit nicht pauschal abgeschafft. |
| „Embedded Artifact“ als fundamentaler Entity-Sondertyp | A | ADR-0015 lehnt im Vorschlag die Ableitung eigener Grundsemantik aus physischer Einbettung ab. | Repräsentationsbegriff kann bleiben; keine unbelegte Deprecation des Wortes. |

Leere Relationslisten sind dabei **keine tatsächlichen Relationsinstanzen**. Ihr Vorhandensein belegt einen verwendeten Schlüssel, aber keinen ausgeführten semantischen Zusammenhang.

## 5. Semantic conflicts

### K1 — Entity, Artifact und Physical Representation

- **ADR-0004, Accepted:** Wissen wird als Entities organisiert und durch Artifacts repräsentiert; Artifacts sind eindeutig identifizierbar und unabhängig versionierbar.
- **ONT-Artifact und TERM-Artifact, Draft; ADR-0013, Proposed:** Artifact ist eine persistierte oder anderweitig adressierbare Repräsentation.
- **RFC-0010, Draft:** Artifact ist selbst eine logische Engineering-Repräsentation mit semantischer Identität, getrennt von der physischen Repräsentation.

Damit ist die Entity/Artifact-Unterscheidung bereits stärker gestützt als die konkrete **Zwei- oder Dreiebenenabgrenzung**. Diese betrifft Artifact Identity, Artifact Revision und die Frage, was genau eine Datei repräsentiert.

### K2 — Concept, Entity und Typisierung

- **ENTITY-0001, Draft:** Jede Entity hat genau einen primären konzeptionellen Typ.
- **ADR-0008, Accepted:** Jedes teilnehmende Artifact deklariert genau einen kanonischen `ontologyType`; keine Ableitung aus Persistenzklassifikation.
- **RFC-0001, Draft:** Eine Entity *may have* einen semantischen Typ.
- **RFC-0020, Draft:** Entity ist Instanz eines Konzepts.
- **RFC-0027, Draft:** Individuelle Artifacts sind Instanzen von Concepts.

Unklar bleibt, wie Concept, Entity und Artifact gemeinsam typisiert werden. Auch die Ontologie-Definitionsdateien selbst besitzen `entityType: ontology`, aber keinen eigenen `ontologyType`. Ihre Rolle im selbstbeschreibenden Typmodell ist nicht vollständig erklärt.

### K3 — Metadata, Property und Engineering Content

- **ADR-0005, Accepted:** Metadata beschreibt Artifacts und darf kein Engineering Knowledge enthalten.
- **ONT-Metadata / ENTITY-0001, Draft:** Metadata beschreibt Entities.
- **ADR-0010, Proposed:** Canonical Metadata beschreibt semantische Eigenschaften von Engineering Knowledge.
- **RFC-0005, Draft:** Canonical Metadata ist eine Klasse semantischer Properties.
- **RFC-0003, Draft:** Metadata beschreibt Wissen statt Content zu sein, lässt aber ausdrückliche Ausnahmen durch das Domain-Modell zu.

Hier bestehen unterschiedliche Reichweiten von „Engineering Knowledge“, „Content“ und Metadatenbesitz. Ein Glossar darf die akzeptierte Trennung nicht durch eine stillschweigende Übernahme der Entwürfe abschwächen.

### K4 — Sind Predicate-Constraints verpflichtend?

- **ADR-0009, Accepted:** Jedes Relation Predicate benötigt einen semantischen Vertrag über erlaubte Source-/Target-Typen.
- **RFC-0027, Draft; RFC-0029, Proposed:** Normative Predicates benötigen Allowed Pairs.
- **ADR-0014, Proposed; RFC-0026 und TERM-Predicate/TERM-Relation, Draft:** Teilweise optionale Formulierungen mit `MAY` beziehungsweise „may constrain“.

Der stärkere akzeptierte Stand verlangt einen Vertrag. Nicht abschließend einheitlich ist, ob die optionalen Formulierungen nur einzelne Constraint-Arten oder den Vertrag insgesamt betreffen.

### K5 — Domain/Range versus Allowed Pairs

**ADR-0009, Accepted** beschreibt Domain und Range und verlangt die Prüfung beider Endpunkttypen. **RFC-0027/RFC-0029** verlangen explizite Paare und verbieten die implizite Bildung aller Kombinationen aus unabhängigen Mengen.

Das muss kein grundlegender Widerspruch sein: Allowed Pairs können den akzeptierten Vertrag präzisieren. Eine Gleichsetzung der beiden Darstellungen wäre jedoch falsch. RFC-0026 enthält weiterhin getrennte Source-/Target-Beispiele.

### K6 — `references`: Text und konkrete Constraints widersprechen sich

- [content.md](/opt/projects/aton/foundation/specifications/predicates/references/content.md): ausschließlich Artifact → Artifact, keine anderen Paare.
- [constraints.yaml](/opt/projects/aton/foundation/specifications/predicates/references/constraints.yaml): `ANY-CONCEPT` → `ANY-CONCEPT`.
- RFC-0027 beschreibt ebenfalls Artifact → Artifact.

Das ist eine konkrete Bedeutungsabweichung innerhalb derselben Prädikatdefinition. Aus der Maschinenlesbarkeit allein folgt keine höhere semantische Autorität.

### K7 — Prädikatkatalog und konkrete Definitionen sind nicht deckungsgleich

- RFC-0027 definiert elf Prädikate; nur vier besitzen eigene Definitionen unter `predicates/`.
- Die konkreten `governs`-Constraints ergänzen Constitution als Source gegenüber RFC-0027.
- Die konkreten `refines`-Constraints ergänzen AX → AX.
- Inverse Prädikate sind textuell beschrieben, aber nicht als eigenständige Predicate-Artifacts vorhanden.

Damit sind **textuell definiert**, **als Artifact repräsentiert** und **für konkrete Verifikation vollständig verfügbar** unterschiedliche Zustände.

### K8 — Collection Membership, `contains` und Kontext

RFC-0022 unterscheidet Collection Membership von gewöhnlichen Domain-Relations, erlaubt aber eine ausdrückliche Abbildung durch das Relation-Modell. RFC-0027 definiert `contains` unter anderem für Collection → Artifact und Review → Finding. ADR-0015 verlangt explizite Kontextbeziehungen.

Das ist teilweise kompatibel, aber die Reichweiten sind nicht vollständig abgestimmt: Gruppenzugehörigkeit, kontextuelle Ownership, semantisches Containment und physische Einbettung sind keine austauschbaren Bedeutungen.

### K9 — Identität, Version, Lifecycle und Relationsidentität

ADR-0014 und TERM-Relation identifizieren eine Relation über Source, Predicate und Target. RFC-0004 und RFC-0012 verlangen zugleich versionsabhängige Beziehungen. Wie historische Relationenvorkommen voneinander abgegrenzt werden, ist nicht vollständig bestimmt.

Zudem nennen die Versionierungsquellen Lifecycle-Änderungen als mögliche relevante Zustandsänderungen, während ADR-0017 Lifecycle und Engineering Version ausdrücklich trennt. Die Bedingungen für einen neuen Versionsstand müssen präzisiert werden; „Statusänderung = neue Identität“ wäre jedenfalls nicht gedeckt.

### K10 — Konzept, Tätigkeit und Aufzeichnung

Mehrere Definitionen wechseln zwischen fachlichem Gegenstand und dessen Repräsentation:

- **Test:** Aktivität oder Spezifikation.
- **Review:** strukturierte Untersuchung, als Artifact beschrieben.
- **Finding:** Artifact in ONT-Finding, kontextuelle Entity in ADR-0015.
- **Architecture Decision / ADR:** Entscheidung und Record häufig gemeinsam behandelt.
- **Note:** Die Definition existiert in der Ontologie, sagt aber zugleich, Notes seien nicht Teil der Foundation-Ontologie selbst.

Bei Note könnte die Aussage Instanzen außerhalb der Ontologie meinen. Der Text trennt Typ und Instanzen dafür jedoch nicht ausdrücklich genug.

### K11 — Semantischer Kernel, Softwarekernel, Model und View

Die Constitution beschreibt den Engineering Kernel als semantischen Kern. ADR-0008 spricht vom Kernel als Verbraucher kanonischer Domain-Modelle mit Loader-Grenze.

Ebenso sind Engineering Knowledge Model, Engineering Knowledge Graph und Canonical Domain Representation eng verbunden, aber nicht identisch definiert. View kann sowohl Perspektive als auch Darstellung bezeichnen. Die Glossarterminologie muss diese Ebenen sichtbar halten.

### K12 — Foundation-Grenzen, Profile, Process und Task

Die Constitution:

- schließt konkrete Prozesse, Technologien, Speichermechanismen und Präsentationsformate aus ihrem semantischen Verantwortungsbereich aus;
- weist Prozesse Profiles zu;
- führt Engineering Tasks als Arbeitskoordination ein.

ADR-0016 schlägt ein generisches Process Model vor. Akzeptierte ADR-0002/-0003 legen Markdown und Git für die Foundation fest. Das kann als Trennung zwischen **semantischem Standard** und **Selbsthosting seiner autoritativen Repräsentation** verstanden werden; diese Lesart ist aber nicht überall explizit ausformuliert.

Task versus Activity sowie Process Profile versus Process Definition sind weiterhin unbestimmt.

### K13 — Search und Navigation

AX-0003/AX-0008 nennen Search einen primären Navigationsmechanismus. ADR-0018/RFC-0014 unterscheiden Suche nach Kandidaten von Traversierung bekannter semantischer Verbindungen.

Das kann eine UX-Sicht gegenüber einer Modelloperation sein. Es sollte nicht durch einen unqualifizierten Alias Search = Navigation verdeckt werden.

### K14 — Glossarautorität und Modellautorität

Die [Glossary README](/opt/projects/aton/foundation/specifications/glossary/README.md) verlangt genau eine normative Definition je Begriff und verbietet Neudefinitionen durch Spezifikationen.

Die bestehenden Einträge erklären dagegen, dass sie die normativen Entity-/Artifact-/Relation-Modelle nicht ersetzen oder neu definieren. Gleichzeitig existieren überlappende Definitionen in Glossar, Ontologie und RFCs.

Eine klare Aufteilung zwischen **Terminologie**, **Konzeptsemantik** und **operativen Modellregeln** fehlt. Dazu kommt: Glossareinträge nennen Proposed-ADRs als normative Modelle, ohne deren Reifegrad im Eintrag hervorzuheben.

## 6. Terms that should NOT become glossary entries

Die folgenden Begriffe sollten im aktuellen Stand **keine eigenständigen kanonischen ATON-Semantik-Einträge** erhalten. Das schließt technische Referenzdokumentation oder spätere Domain-Erweiterungen nicht aus.

Für alle Tabellenzeilen gilt: keine vorhandenen eigenständigen `TERM-*`- oder `ONT-*`-Definitionen für die genannten technischen beziehungsweise beschreibenden Begriffe.

| Begriffe | Kat. | Aktuelle Rolle / Quelle und Status | Warum kein eigener kanonischer Eintrag |
|---|---|---|---|
| Git, Commit, Commit Hash, Branch, Tag, Merge, Rebase, Cherry-Pick | I | Versionsverwaltung; ADR-0003, Accepted; RFC-0012, Draft. | Externe technische Konzepte. Ihre Abgrenzung gehört in Version, Revision und Provenance. |
| Markdown, YAML, JSON, XML, CSV | I | Autoren-, Serialisierungs- und Austauschformate; ADR-0002, Accepted; RFC-0015/-0030, Proposed. | Definieren keine eigenständigen Engineering-Konzepte. |
| HTML, MDX, JSX, CSS, UTF-8, Mermaid, TeX/LaTeX | I | Darstellung beziehungsweise Encoding; RFC-0031, Proposed; AX, Draft. | Technische Sprach- und Formatbegriffe. |
| Docusaurus, Docusaurus Renderer | I | Konkreter Dokumentationsrenderer; RFC-0024, Draft. | Implementierung statt allgemeiner ATON-Semantik. |
| Loader, Parser, Serializer, Exporter, Renderer, Anti-Corruption Layer | I | Übersetzung und Verarbeitung an Implementierungsgrenzen; ADR-0008, Accepted; ADR-0011/-0014, Proposed. | Architekturrollen besser in technischer Referenz erklären. |
| `content.md`, `metadata.yaml`, `relations.yaml`, `constraints.yaml` | I | Dateinamen der Repräsentation; RFC-0030, Proposed, konkrete Repository-Struktur. | Dateien sind keine zusätzlichen semantischen Konzepte. |
| `id`, `title`, `status`, `ontologyType`, `entityType`, `allowedPairs` als Feldnamen | P | Repräsentationen semantischer Angaben; Metadaten/Constraints. | Semantischen Begriff erklären, nicht jedes Serialisierungstoken als eigenen Begriff verdoppeln. |
| Dateipfad, Verzeichnis, URL, API Endpoint, Datenbankspalte, Cache, Index | I | Zugriff, Persistenz oder Beschleunigung; RFC-0011/-0015, Draft/Proposed. | Keine kanonische Engineering-Identität oder Beziehung allein durch technische Existenz. |
| Heading, Paragraph, List, Table, Code Fence, Front Matter, Whitespace | I | Markdown-Struktur; RFC-0031, Proposed. | Struktur und Formatierung schaffen nicht automatisch Engineering-Semantik. |
| Breadcrumb, Sidebar, Icon, Typography, Color, Spacing | I | UX-/Darstellungsmittel; AX-0004/-0005, Draft. | Keine eigenständigen Konzepte des Engineering-Wissensmodells. |
| Clarity, Trust, Confidence, Predictability, Discoverability, Scalability, Progressive Disclosure | B | AX-Ziele und Gestaltungsprinzipien, Draft. | Relevant als Qualitätsziele, aber ohne eigenständiges ATON-Domain-Modell. |
| Openness, Longevity, Transparency, Stability, Interoperability | B | Ziele und Prinzipien der Constitution/ADRs, Accepted. | Nicht jedes wichtige Architekturziel benötigt eine ATON-spezifische Neudefinition. |
| Rationale, Observation, Idea, Hypothesis, Context als allgemeine Wörter | B | Beschreibungen in Note/Finding/Decision. | Nicht jede Verwendung meint eine eigenständig identifizierte Entity. |
| Dataset, Report, Model, Verification Record, Requirement Document | A | Beispiele möglicher Artifacts in RFC-0010, Draft. | Erwähnung als Beispiel ist noch keine ausreichende universelle Typdefinition. |
| System Requirement, Verification Case, `satisfies` | D/R | Illustrative Beispiele, etwa in RFC-0021, Draft. | Keine ausgearbeitete eigenständige Definition im aktuellen Ontologie-/Prädikatbestand. |
| Architecture Board | G | Entscheidungsinstanz in Architektur- und Migrationsbeschreibungen; RFC-0028, Draft. | Keine universell vorgeschriebene Foundation-Rolle; Governance-Zuständigkeit ist konfigurierbar. |
| Getting Started, Concepts, Reference, Tutorials, Community | B | Navigationsrubriken in AX-0003/-0004, Draft. | Websitegliederung, keine Domain-Taxonomie. |
| `ONT-*`, `TERM-*`, `PRED-*`, `ADR-*`, `RFC-*` als Präfixe | I | Identifikationskonventionen. | Identifierkonventionen dokumentieren; keine eigenen Engineering-Konzepte pro Präfix. |

Ein **ATON Markdown Profile** kann in einer technischen Spezifikationsreferenz benannt werden. Es sollte nicht mit dem in der Constitution beschriebenen Process-/Policy-Profile zu einem gemeinsamen unqualifizierten Glossarbegriff verschmolzen werden.

## 7. Existing glossary coverage

Der aktuelle Bestand besteht aus genau diesen vier Einträgen:

| Eintrag | Status | Abdeckung | Wesentliche Grenze |
|---|---|---|---|
| [TERM-Entity](/opt/projects/aton/foundation/specifications/glossary/TERM-Entity/content.md) | Draft | Grundbegriff Entity, konzeptionelle Identität, Persistenzunabhängigkeit. | Typisierung und Verhältnis Concept/Artifact nicht umfassend geklärt. |
| [TERM-Artifact](/opt/projects/aton/foundation/specifications/glossary/TERM-Artifact/content.md) | Draft | Artifact als persistierte/adressierbare Repräsentation; Trennung von Entity Identity. | Entspricht ONT-Artifact, aber nicht vollständig der Dreiebenenbeschreibung in RFC-0010. |
| [TERM-Predicate](/opt/projects/aton/foundation/specifications/glossary/TERM-Predicate/content.md) | Draft | Bedeutung, Richtung, konkrete Prädikate, Relation als Anwendung. | Optionale Constraint-Formulierung und Concept-/Entity-Ebene. |
| [TERM-Relation](/opt/projects/aton/foundation/specifications/glossary/TERM-Relation/content.md) | Draft | Verbindung, Richtung, Source/Predicate/Target, Persistenzunabhängigkeit. | Modellautorität verweist auf Proposed ADR-0014; historische Identität bleibt offen. |

Alle vier Einträge sind als `ONT-GlossaryEntry` typisiert. Das bedeutet: **Der Glossareintrag ist ein GlossaryEntry; sein Gegenstand ist beispielsweise Entity oder Predicate.**

Die derzeitige Abdeckung konzentriert sich auf vier Grundbegriffe. Das Verhältnis „4 Glossareinträge zu 23 Ontologiekonzepten“ ist **keine Vollständigkeitsmetrik**: Manche wichtige Terminologie hat keine Ontologie-Definition, und manche Ontologie-Definition rechtfertigt noch keinen eigenen Glossareintrag.

## 8. Missing terminology

„Missing“ bedeutet hier **fehlende terminologische Absicherung**, nicht automatisch Auftrag zur Erstellung einer Datei.

| Priorität | Fehlende Absicherung | Warum semantisch erforderlich |
|---|---|---|
| Hoch | Engineering Knowledge, Engineering Knowledge Model, Engineering Knowledge Graph, Foundation | Definiert, was ATON verwaltet und welche Quellen beziehungsweise Strukturen maßgeblich sind. |
| Hoch | Ontology, Concept, Ontology Type | Verhindert Vermischung von Typen, Instanzen, Artifacts und Persistenzklassifikation. |
| Hoch | Metadata, Property, Engineering Content, Canonical Metadata | Sichert die akzeptierte Trennung der Informationsrollen und macht offene Reichweiten sichtbar. |
| Hoch | Engineering Identity, Identifier, Engineering Version, Artifact Revision | Verhindert Gleichsetzung mit Pfaden, Git Hashes und beliebigen Änderungen. |
| Hoch | Semantic Constraint, Allowed Pair, Constraint Pattern | Nötig, um gültige Relationen und `ANY-CONCEPT` konsistent zu verstehen. |
| Hoch | Baseline, Release, Lifecycle State | Unterscheidet Zustand, Auswahl, Freigabe und Governance. |
| Hoch | Definition, Glossary Entry, Specification | Klärt die Rolle terminologischer Definitionen gegenüber Modellspezifikationen. |
| Mittel | Requirement, Component, Interface, Collection, View | Bestehende Ontologiekonzepte mit klar erkennbarem Verwechslungsrisiko. |
| Mittel, Entscheidung nötig | Test, Review, Finding, Architecture Decision/ADR | Fachliches Objekt, Tätigkeit und Aufzeichnung müssen abgegrenzt werden. |
| Mittel | Traceability, Provenance, Navigation | Verhindert Gleichsetzung von Beziehungen, Herkunft und Darstellung. |
| Mittel, unvollständiges Modell | Task, Activity, Process Definition, Process Instance, Process State, Transition | Trennt Arbeit, Prozessvorlage, Ausführung und Zustand. |
| Mittel | Profile, Capability, Application, Governance | Macht die Verantwortungsgrenzen der Constitution verständlich. |
| Mittel, Konfliktauflösung nötig | Konkrete Predicates und inverse Beziehungen | Bedeutung ist teilweise definiert, aber Quellen und Repräsentationsbestand stimmen nicht überall überein. |

Darüber hinaus bestehen **Spezifikationslücken**, die ein Glossar nicht schließen darf:

- vollständige Entity-/Artifact-/Concept-Typisierung;
- festgelegtes Verhältnis von Artifact zu Physical Representation;
- universelle und typspezifische Metadaten;
- Identitätsscope und externe Identitäten;
- historische Relationsidentität;
- Task-/Activity-/Profile-Abgrenzung;
- eigenständige Review-/Finding-/Evidence-Semantik;
- vollständiger kanonischer Prädikatbestand;
- Autoritätsregel bei Widerspruch zwischen Prädikattext und Constraints;
- Verhältnis von Glossar-, Ontologie- und RFC-Definitionen.

Die leeren Schema- und Template-Dateien liefern hierfür derzeit keine zusätzliche normative Präzisierung.

## 9. Human semantic decisions required

Die folgenden Punkte benötigen eine menschliche Architektur- beziehungsweise Semantikentscheidung. Die Analyse trifft diese Entscheidungen nicht vorweg.

1. **Welche Repräsentationsebenen gelten?**  
   Entity → Artifact → Physical Representation als drei Ebenen, oder Artifact bereits als physische/adressierbare Repräsentation? Welche Identitäten und Revisionen gehören jeweils dazu?

2. **Wie werden Concepts, Entities und Artifacts typisiert?**  
   Ist der primäre Typ für jede Entity zwingend? Wie werden Ontologiekonzepte selbst im Self-Hosting-Modell klassifiziert?

3. **Wie weit reichen Engineering Knowledge und Metadata?**  
   Was bedeutet die akzeptierte Aussage, Metadata dürfe kein Engineering Knowledge enthalten, angesichts semantischer Canonical Properties?

4. **Wer besitzt Definitionsautorität?**  
   Welche Aussagen gehören ins Glossar, welche in Ontologiekonzepte, welche in RFCs? Wie werden widersprüchliche Definitionen desselben Begriffs behandelt?

5. **Welcher Vertrag gilt für `references`?**  
   Nur Artifact → Artifact oder alle gültigen Concepts über `ANY-CONCEPT`? Welche Quelle muss die andere künftig präzisieren?

6. **Wie werden allgemeiner Prädikatkatalog und konkrete Definitionen synchronisiert?**  
   Einschließlich Constitution-/AX-Paaren, inversen Predicates und bisher nur im RFC beschriebenen Prädikaten.

7. **Welche Rolle haben optionale Constraints?**  
   Wie werden die `MAY`-Formulierungen mit dem akzeptierten obligatorischen semantischen Vertrag vereinbart?

8. **Wie werden Kontext, Mitgliedschaft und Containment abgegrenzt?**  
   Insbesondere Collection Membership, `contains`, Review/Finding-Kontext und physische Einbettung.

9. **Was sind Test, Review, Finding und ADR jeweils?**  
   Domain-Objekt, Prozessaktivität, Prozessinstanz, Dokument oder Aufzeichnung? Welche davon brauchen getrennte Bezeichnungen?

10. **Wie verhalten sich Task, Activity und Process Profile zueinander?**  
    Die Constitution und ADR-0016 liefern dafür bislang keine vollständige gemeinsame Semantik.

11. **Wie werden Versionen und historische Relationen identifiziert?**  
    Wann erfordert eine Lifecycle- oder Metadata-Änderung eine neue Engineering Version? Wie wird dieselbe Relation in verschiedenen Zuständen adressiert?

12. **Wie werden Legacy-Beziehungen aufgelöst?**  
    Für `dependsOn`, `children`, `parents`, `related`, `relatedTo` und unvollständig definierte Supersession-Beziehungen sind explizite Bedeutungsentscheidungen erforderlich.

13. **Wie werden die Architekturbegriffe qualifiziert?**  
    Semantischer Engineering Kernel versus Softwarekernel; Profile versus Markdown Profile; View versus gerenderte Ausgabe.

14. **Welche zunächst nur unterstützenden Begriffe werden eigenständige Konzepte?**  
    Insbesondere Thing, Evidence, Verification Result, External Entity, Domain Library und Materialization. Dafür sollte ein eigener semantischer Vertrag ausschlaggebend sein, nicht die Zahl ihrer Erwähnungen.

**Es wurden keine Glossary Entries erstellt, erweitert oder umdefiniert.**

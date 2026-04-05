# MIN v1.1.0 — Konsolidierter Implementierungsplan

**Status:** Planungsdokument (nichts implementiert)
**Basis:** MIN v1.0.0 (13 Klassen, ~2800 Zeilen, ~120 KB)
**Ziel:** MIN v1.1.0 (15 Klassen, <800 Zeilen Axiome, <20 KB Kern-TTL)
**Autor:** Dr. Ingolf Lepenies
**Planungsdatum:** 2026-04

---

## 0. Zusammenfassung

MIN v1.1 macht vier Dinge:

1. **Epistemische Dimension** — neue 6. Forma-Kategorie `Epistemicum`
2. **Formalisierung** — causalityMode/efficacyMode als OWL-Enums
3. **Schlankung** — Prosa raus aus min.ttl, rein in min-annotations.ttl
4. **Vorbereitung** — Possibile + isQuantifiable, supersedes transitiv

Alles additiv. Kein bestehendes Axiom bricht. Alle v1.0.0-Graphen bleiben valide.

---

## 1. Scope: Was ist drin, was nicht

### v1.1.0 — DRIN

| # | Maßnahme | Typ | Begründung |
|---|----------|-----|------------|
| M1 | Epistemicum als 6. Forma-Subklasse | Neue Klasse | Löst Ingenieursprobleme (Modellvalidierung, DPP-Konfidenz) + philosophische Vollständigkeit |
| M2 | EpistemicStatus-Enum (5 Werte) | Neue Klasse + Individuals | Kontrollierte Werte statt Freitext |
| M3 | ConfidenceType-Enum (4 Werte) | Neue Klasse + Individuals | 0.8 subjektiv ≠ 0.8 statistisch |
| M4 | 6 neue Object Properties für Epistemicum | Neue Properties | holds/heldBy, about, supportedBy/supports, underminedBy/undermines |
| M5 | hasEpistemicStatus + hasConfidenceType | Neue Properties | Funktionale Properties auf Epistemicum |
| M6 | hasConfidence (Datatype Property) | Neue Property | Quantitativer Sicherheitsgrad [0..1] |
| M7 | CausalityMode als OWL-Enum | Neue Klasse + Individuals | Formalisierung von bisher Freitext-Annotation |
| M8 | EfficacyMode als OWL-Enum | Neue Klasse + Individuals | Analog zu M7 |
| M9 | hasCausalityMode / hasEfficacyMode | Neue Properties | ObjectProperties statt AnnotationProperties |
| M10 | isQuantifiable auf Possibile | Neue Datatype Property | Risiko vs. Knightsche Unsicherheit |
| M11 | supersedes wird TransitiveProperty | Axiom-Änderung | Historien-Reasoning über Epistemicum-Ketten |
| M12 | TTL-Split: min.ttl → min-core.ttl + min-annotations.ttl | Refactoring | Kern < 20 KB, Prosa separat |
| M13 | Englische Labels/Comments durchgängig | Dokumentation | Internationale Nutzbarkeit |
| M14 | Deprecation confirms/refutes | Lifecycle | Ersetzt durch supportedBy/underminedBy |
| M15 | Disjunktheitsaxiom Forma-intern erweitern | Axiom-Änderung | +Epistemicum in AllDisjointClasses |
| M16 | SHACL-Shapes für Epistemicum | Validierung | Pflicht-Properties, Wertebereiche |

### v1.1.0 — NICHT DRIN (bewusst verschoben)

| Maßnahme | Verschoben auf | Begründung |
|----------|---------------|------------|
| sdata-uncertainty.ttl (UncertaintyAssignment-Pattern) | sdata v0.2 | Eigenständiges Modul, eigener Release-Zyklus |
| Reifizierte Evidenzgewichtung (EvidenceRelation) | MIN v1.2 | Zu groß für v1.1, braucht Erfahrung mit v1.1 |
| Alignment-Module (PROV-O, QUDT, schema.org) | MIN v1.2+ | Eigener Arbeitspaket |
| Nexus-Partition explizit schließen | MIN v2.0 | Designentscheidung mit Konsequenzen |
| aboutForma / aboutNexus Subproperties | ABGELEHNT | Erzwingt unnötige Modellierungsentscheidung |
| endorsedBy Property | ABGELEHNT | Semantisch redundant mit recognizedBy |
| Axiomatic → Assumed Umbenennung | ABGELEHNT | Verschiedene Abstraktionsgrade |
| Data aufspalten (RawData/Document/Model) | MIN v2.0 | Community-Diskussion nötig |
| Agent ∩ Process klären | MIN v2.0 | Philosophische Grundsatzfrage |

---

## 2. Dateien: Vorher → Nachher

### Vorher (v1.0.0)

```
min-ontology/
  min.ttl                    ← ~120 KB, ~2800 Zeilen (Axiome + Prosa)
  min-v1.0.0.ttl             ← immutable Snapshot
  shapes/
  examples/
  docs/
```

### Nachher (v1.1.0)

```
min-ontology/
  min.ttl                    ← Alias → min-v1.1.0.ttl
  min-core.ttl               ← NUR Axiome, < 20 KB, < 800 Zeilen    [NEU]
  min-annotations.ttl        ← Prosa (designRationale, philosophicalBasis, etc.)  [NEU]
  min-v1.0.0.ttl             ← immutable (unverändert)
  min-v1.1.0.ttl             ← immutable Snapshot v1.1              [NEU]
  shapes/
    min-epistemic.shacl.ttl  ← SHACL für Epistemicum                [NEU]
  examples/
    epistemic-zugversuch.ttl ← End-to-End Beispiel                  [NEU]
  docs/
    epistemic-dimension.md   ← Designentscheidungen + Queries       [NEU]
```

### Import-Struktur

```
min.ttl (= min-v1.1.0.ttl)
  ├── enthält alles aus min-core.ttl
  └── enthält alles aus min-annotations.ttl

min-core.ttl
  └── NUR Axiome (ladbar ohne Prosa)

min-annotations.ttl
  └── owl:imports min-core.ttl
  └── Alle designRationale, philosophicalBasis, axiomRationale, etc.
```

Nutzer, die nur Axiome wollen: `owl:imports <min-core.ttl>`
Nutzer, die alles wollen: `owl:imports <min.ttl>`

---

## 3. Inventar: Alle neuen Terme in v1.1.0

### 3.1 Neue Klassen (4)

```
min:Epistemicum           rdfs:subClassOf min:Forma
min:EpistemicStatus       owl:oneOf (5 Individuals)
min:ConfidenceType        owl:oneOf (4 Individuals)
min:CausalityMode         owl:oneOf (3 Individuals)
```

EfficacyMode wird NICHT als separate Klasse eingeführt — siehe Abschnitt 4.3.

### 3.2 Neue Individuals (12)

```
Epistemischer Status:
  min:Hypothetical         "aufgestellt, weder bestätigt noch widerlegt"
  min:Confirmed            "durch Evidenz gestützt und akzeptiert"
  min:Refuted              "durch Evidenz widerlegt"
  min:Contested            "widersprüchliche Evidenz, kein Konsens"
  min:Axiomatic            "Grundannahme, nicht empirisch prüfbar"

Konfidenztyp:
  min:SubjectiveConfidence   "Experteneinschätzung"
  min:StatisticalConfidence  "aus Stichprobe (Konfidenzintervall)"
  min:BayesianConfidence     "posterior probability"
  min:HeuristicConfidence    "Erfahrungswert"

Kausalitätsmodus:
  min:Dispositional          "wirkt auch ohne Agent"
  min:Mediated               "wirkt nur über interpretierenden Agent"
  min:Relational             "wirkt nur zwischen Partnern"
```

### 3.3 Neue Object Properties (8)

```
Epistemisch:
  min:holds                Agent → Epistemicum
  min:heldBy               Epistemicum → Agent (inverse)
  min:about                Epistemicum → Entity
  min:supportedBy          Epistemicum → Nexus
  min:supports             Nexus → Epistemicum (inverse)
  min:underminedBy         Epistemicum → Nexus
  min:undermines           Nexus → Epistemicum (inverse)

Kausalität:
  min:hasCausalityMode     Nexus → CausalityMode
```

### 3.4 Neue Object Properties (funktional) (2)

```
  min:hasEpistemicStatus   Epistemicum → EpistemicStatus (functional)
  min:hasConfidenceType    Epistemicum → ConfidenceType (functional)
```

### 3.5 Neue Datatype Properties (2)

```
  min:hasConfidence        Epistemicum → xsd:double [0.0..1.0]
  min:isQuantifiable       Possibile → xsd:boolean
```

### 3.6 Geänderte bestehende Terme

```
  AllDisjointClasses (Forma-intern):
    VORHER: ( Lex, Structura, Possibile, Norma, Institutio )
    NACHHER: ( Lex, Structura, Possibile, Norma, Institutio, Epistemicum )

  min:supersedes:
    VORHER:  owl:ObjectProperty
    NACHHER: owl:ObjectProperty, owl:TransitiveProperty

  min:causalityMode (alte AnnotationProperty):
    NACHHER: deprecated, replacedBy min:hasCausalityMode

  min:efficacyMode (alte AnnotationProperty):
    NACHHER: bleibt als AnnotationProperty auf Klassenebene (siehe 4.3)

  min:confirms:
    NACHHER: deprecated, replacedBy min:supportedBy

  min:refutes:
    NACHHER: deprecated, replacedBy min:underminedBy
```

### 3.7 Entfernte Terme

```
  Keine. Alles additiv.
```

### 3.8 Zählung

```
  Neue Klassen:             4
  Neue Individuals:        12
  Neue Object Properties:  10
  Neue Datatype Properties:  2
  Geänderte Axiome:          2  (AllDisjointClasses, supersedes)
  Deprecated Terme:          3  (causalityMode, confirms, refutes)
  Gebrochene Axiome:         0
```

---

## 4. Detailentwurf

### 4.1 Epistemicum — 6. Forma-Subklasse

**Definition:** Das, was für wahr gehalten wird. Epistemische Haltung
eines Agent gegenüber einem Sachverhalt.

**Existenzkriterium:** Kann man fragen: „Gilt F laut Agent A?" — und
ist die Antwort im Wissensgraph darstellbar?

**Warum Forma:**
- Bewirkt nichts kausal → nicht Nexus
- Bestimmt, wie ein Agent Nexus interpretiert → konstitutive Bestimmung
- Passt in keine bestehende Forma-Subklasse (geprüft gegen alle 5)

**Agent-Optionalität:** heldBy hat sh:minCount 0 in SHACL.
Agent-freie Epistemicum-Instanzen modellieren institutionalisierte
epistemische Zustände: „Dieser Datensatz gilt als verifiziert."
Provenienz läuft über das bestehende originatedBy.

**Abgrenzung:**

| Verwechslungsgefahr | Unterschied |
|---|---|
| Possibile | Possibile ist eine Möglichkeit. Epistemicum ist eine Haltung gegenüber einer Möglichkeit/Lex/Norma. |
| Data | Data kodiert Information (Bytes). Epistemicum bewertet Information (Gültigkeit). |
| Norma | Norma sagt, was gelten soll. Epistemicum sagt, was für wahr gehalten wird. |

### 4.2 CausalityMode — Formalisierung

**Problem:** `min:causalityMode "dispositional"` ist Freitext.
Kein Reasoning, keine Validierung, keine Erweiterungskontrolle.

**Lösung:** Individuen + owl:oneOf + ObjectProperty.

```
min:CausalityMode
    owl:oneOf ( min:Dispositional, min:Mediated, min:Relational )

min:hasCausalityMode
    domain: min:Nexus
    range: min:CausalityMode
```

**Zuweisung auf Klassenniveau** (owl:Restriction, nicht Instanz-Property):

```
min:Object rdfs:subClassOf [ owl:onProperty min:hasCausalityMode ;
                              owl:hasValue min:Dispositional ] .
min:Process rdfs:subClassOf [ owl:onProperty min:hasCausalityMode ;
                               owl:hasValue min:Dispositional ] .
min:Data rdfs:subClassOf [ owl:onProperty min:hasCausalityMode ;
                            owl:hasValue min:Mediated ] .
min:Boundary rdfs:subClassOf [ owl:onProperty min:hasCausalityMode ;
                                owl:hasValue min:Relational ] .
```

Jede Instanz erbt den Modus automatisch per Reasoning.
Kein manuelles Setzen nötig.

### 4.3 EfficacyMode — Designentscheidung

**Problem:** efficacyMode hat 8+ Werte (dispositional, agentive, informational,
formal, lawful, structural, modal, normative, institutional, epistemic).
Diese verteilen sich über Nexus UND Forma.

**Entscheidung:** EfficacyMode wird NICHT als eigene Klasse formalisiert.

**Begründung:**
- Die Werte sind 1:1 an Subklassen gebunden (lawful = Lex, normative = Norma, etc.).
- Eine ObjectProperty `hasEfficacyMode` auf Entity wäre redundant zur Klassenstruktur.
- Der einzige Nutzen wäre: per SPARQL nach efficacyMode filtern. Aber `?x a min:Lex`
  leistet dasselbe wie `?x min:hasEfficacyMode min:Lawful`.
- Die Formalisierung würde 10+ Individuals erzeugen, die nichts Neues sagen.

**Stattdessen:** efficacyMode bleibt als AnnotationProperty auf Klassenebene.
Das ist dokumentarisch nützlich und maschinenlesbar genug.

### 4.4 isQuantifiable auf Possibile

**Problem:** MIN kann nicht unterscheiden zwischen:
- „Bauteilversagen mit 2% Wahrscheinlichkeit" (Risiko, quantifizierbar)
- „Klimawandel-Auswirkungen auf Lieferketten" (Ungewissheit, nicht quantifizierbar)

**Lösung:** Eine einzige DatatypeProperty:

```
min:isQuantifiable
    domain: min:Possibile
    range: xsd:boolean
    default: keine Annahme (open world)
```

`false` = Tiefe/Knightsche Unsicherheit. Keine Verteilung zuweisbar.
`true` = Risiko. Wahrscheinlichkeit zuweisbar (Quantifizierung in sdata-uncertainty).
Abwesend = unbekannt.

### 4.5 supersedes als TransitiveProperty

```
min:supersedes
    a owl:ObjectProperty, owl:TransitiveProperty
    domain: min:Forma       ← nicht nur Epistemicum
    range: min:Forma
```

Gilt für alle Forma: Norma supersedes Norma, Institutio supersedes Institutio,
Epistemicum supersedes Epistemicum. Transitivität ermöglicht Historien-Queries.

---

## 5. TTL-Split: min-core.ttl

### 5.1 Was in min-core.ttl gehört

```
- Ontologie-Deklaration (IRI, Version, Creator, License)
- Alle owl:Class Deklarationen mit rdfs:subClassOf
- Alle owl:equivalentClass Axiome (Entity ≡ Nexus ⊔ Forma)
- Alle owl:AllDisjointClasses
- Alle owl:ObjectProperty / owl:DatatypeProperty / owl:AnnotationProperty
- Alle owl:Restriction (auf Klassen)
- Alle owl:inverseOf, owl:TransitiveProperty, owl:FunctionalProperty
- Alle owl:oneOf (Enums)
- Alle rdfs:label (en + de)
- Alle rdfs:comment (KURZ: max 2 Sätze, en + de)
- foaf:Person Deklaration für Creator
```

### 5.2 Was in min-annotations.ttl gehört

```
- min:designRationale       (alle)
- min:philosophicalBasis    (alle)
- min:axiomRationale        (alle)
- min:criterion             (alle)
- min:definition            (alle — ausführliche Version)
- min:usageExample          (alle)
- min:counterExample        (alle)
- min:distinguishedFrom     (alle)
- min:normativeSource       (alle)
- min:rationale             (alle)
- min:definedInVersion      (alle)
- min:status                (alle)
- skos:example              (alle)
- Lange rdfs:comment Blöcke (>2 Sätze → hierher verschieben)
- ASCII-Art Diagramme
```

### 5.3 Größenschätzung

```
min-core.ttl:         ~600–800 Zeilen, ~15–20 KB
min-annotations.ttl:  ~2000+ Zeilen, ~80–100 KB
min.ttl (vereint):    ~2800+ Zeilen, ~100–120 KB (wie bisher, plus v1.1 Ergänzungen)
min-v1.1.0.ttl:       immutable Snapshot = min.ttl
```

---

## 6. SHACL-Shapes

### 6.1 EpistemicumShape

```
Zielklasse: min:Epistemicum

heldBy:
  sh:minCount 0               ← agent-frei erlaubt
  sh:class min:Agent

about:
  sh:minCount 1               ← PFLICHT
  sh:class min:Entity

hasEpistemicStatus:
  sh:minCount 1
  sh:maxCount 1               ← genau einer
  sh:class min:EpistemicStatus

hasConfidence:
  sh:maxCount 1
  sh:datatype xsd:double
  sh:minInclusive 0.0
  sh:maxInclusive 1.0

hasConfidenceType:
  sh:maxCount 1
  sh:class min:ConfidenceType

supportedBy:
  sh:class min:Nexus           ← verhindert Forma als Evidenz

underminedBy:
  sh:class min:Nexus
```

### 6.2 Konsistenzregel (SHACL-SPARQL)

```
WENN hasConfidence vorhanden → hasConfidenceType MUSS vorhanden sein.
Begründung: Nackte Konfidenz ohne Typ ist semantisch unterdefiniert.
```

### 6.3 CausalityModeShape

```
Zielklasse: min:Nexus (und Subklassen)

hasCausalityMode:
  sh:maxCount 1
  sh:class min:CausalityMode
```

---

## 7. Competency Queries (Abnahmekriterien)

### 7.1 Epistemicum-Queries

```
Q1: Alle Hypothesen eines Agents
    SELECT ?e ?gegenstand ?konfidenz WHERE {
        ?e min:heldBy ?agent ; min:about ?gegenstand ;
           min:hasEpistemicStatus min:Hypothetical ;
           min:hasConfidence ?konfidenz .
    }

Q2: Agent-freie epistemische Zustände (institutionalisiert)
    SELECT ?e WHERE {
        ?e a min:Epistemicum .
        FILTER NOT EXISTS { ?e min:heldBy ?a }
    }

Q3: Widersprüchliche Evidenz
    SELECT ?e ?pro ?contra WHERE {
        ?e min:supportedBy ?pro ; min:underminedBy ?contra .
    }

Q4: Dissens zwischen Agents
    SELECT ?forma ?a1 ?a2 WHERE {
        ?e1 min:about ?forma ; min:heldBy ?a1 ; min:hasEpistemicStatus min:Confirmed .
        ?e2 min:about ?forma ; min:heldBy ?a2 ; min:hasEpistemicStatus min:Refuted .
        FILTER (?a1 != ?a2)
    }

Q5: Epistemische Historie (transitives supersedes)
    SELECT ?latest ?earliest WHERE {
        ?latest min:supersedes+ ?earliest .
        ?latest min:about ?forma .
    }

Q6: Niedrige Konfidenz
    SELECT ?e ?c WHERE {
        ?e min:hasConfidence ?c . FILTER (?c < 0.5)
    }

Q7: Alle subjektiven Schätzungen
    SELECT ?e ?c WHERE {
        ?e min:hasConfidenceType min:SubjectiveConfidence ;
           min:hasConfidence ?c .
    }
```

### 7.2 CausalityMode-Queries

```
Q8: Alle Nexus mit dispositionalem Modus
    SELECT ?x WHERE {
        ?x min:hasCausalityMode min:Dispositional .
    }

Q9: Alle Nexus deren Modus "mediated" ist (= Data-Instanzen)
    SELECT ?x WHERE {
        ?x min:hasCausalityMode min:Mediated .
    }
```

### 7.3 Regressionstests (SPARQL ASK)

```
T1: Epistemicum ist disjunkt mit Lex
    ASK { ?x a min:Epistemicum, min:Lex . }  → false

T2: supportedBy zeigt nur auf Nexus
    ASK { ?x min:supportedBy ?y . ?y a min:Forma . }  → false

T3: Jedes Epistemicum mit Konfidenz hat einen Typ
    ASK { ?x min:hasConfidence ?c .
          FILTER NOT EXISTS { ?x min:hasConfidenceType ?t } }  → false

T4: supersedes ist transitiv
    Gegeben: A supersedes B, B supersedes C
    ASK { A min:supersedes C . }  → true (nach Reasoning)

T5: Object hat automatisch CausalityMode Dispositional
    Gegeben: ex:X a min:Object .
    ASK { ex:X min:hasCausalityMode min:Dispositional . }  → true (nach Reasoning)
```

---

## 8. Beispiel-Graph: Zugversuch mit Epistemicum

```
Szenario:
  Ingenieur Müller glaubt, dass Hooke für DC04 bis 200 MPa gilt.
  Er führt einen Zugversuch durch.
  Messdaten stützen die Hypothese.
  Konfidenz steigt von 0.8 (subjektiv) auf 0.95 (statistisch).
  Zweiter Versuch bei 300 MPa widerlegt die Hypothese.

Knoten:
  2 Agents (Müller, Zugprüfmaschine)
  3 Objects (Blech, Probe, Probe_nach)
  2 Processes (Zugversuch_1, Zugversuch_2)
  3 Data (Messdaten_1, Messdaten_2, Prüfprotokoll)
  3 Epistemicum (Hypothese_v1, Hypothese_v2, Hypothese_widerlegt)
  1 Lex (Hooke)
  1 Norma (Rm ≥ 270 MPa)

Relationen: ~30

Demonstriert:
  - holds/heldBy
  - about (→ Lex)
  - supportedBy / underminedBy (→ Data)
  - hasEpistemicStatus (Hypothetical → Confirmed → Refuted)
  - hasConfidence + hasConfidenceType (0.8 Subjective → 0.95 Statistical)
  - supersedes (Hypothese_v2 supersedes Hypothese_v1)
  - hasCausalityMode (Object: Dispositional, Data: Mediated)
```

---

## 9. Dokumentation

### 9.1 Zu ändernde Seiten

```
docs/min-model.md
  - Forma-Branch: 6 Subklassen statt 5
  - Abschnitt "Epistemic dimension" ergänzen
  - Abschnitt "Causality formalization" ergänzen

docs/class-catalog.md
  - +Epistemicum Eintrag
  - +EpistemicStatus Eintrag (mit allen 5 Werten)
  - +ConfidenceType Eintrag (mit allen 4 Werten)
  - +CausalityMode Eintrag (mit allen 3 Werten)

docs/property-catalog.md
  - +Sektion "6. Epistemic relations" (holds, about, supportedBy, underminedBy)
  - +Sektion "7. Causality properties" (hasCausalityMode)
  - +Sektion "8. Possibile properties" (isQuantifiable)
  - Deprecation-Hinweise für confirms, refutes, causalityMode (alt)

docs/examples.md
  - +Epistemicum-Beispiel (Zugversuch)

docs/changelog.md
  - v1.1.0 Eintrag

docs/versioning.md
  - min-core.ttl / min-annotations.ttl Split erklären
```

### 9.2 Neue Seiten

```
docs/epistemic-dimension.md
  - Motivation (Ingenieur + Philosophie)
  - Klassifikationsprüfung (warum Forma?)
  - Abgelehnte Alternativen (mit Begründung)
  - EpistemicAxis vs. EpistemicStatus (Orthogonalität zu sdata)
  - Competency Queries

docs/uncertainty-architecture.md
  - Übersicht 17 Unsicherheitstypen
  - Mapping auf MIN/sdata-Konstrukte
  - Was v1.1 abdeckt vs. was sdata-uncertainty abdeckt
  - Verweis auf sdata-uncertainty.ttl (geplant für sdata v0.2)

docs/migration-v1.0-to-v1.1.md
  - Rückwärtskompatibilitätsgarantie
  - Deprecation-Liste (causalityMode, confirms, refutes)
  - min-core.ttl Import-Anleitung
```

---

## 10. Abgelehnte Alternativen (Entscheidungsregister)

| Vorschlag | Status | Begründung |
|-----------|--------|------------|
| aboutForma / aboutNexus Subproperties | ABGELEHNT | Erzwingt unnötige Modellierungsentscheidung. SPARQL filtert über `?x a min:Forma`. |
| endorsedBy neben heldBy | ABGELEHNT | Semantisch redundant mit recognizedBy (Institutio ← Agent). heldBy optional reicht. |
| Axiomatic → Assumed | ABGELEHNT | Assumed existiert als sdata SKOS-Wert. Axiomatic meint prinzipiell nicht prüfbare Grundannahmen. |
| Evidenz-Gewichtung in v1.1 | VERSCHOBEN v1.2 | Evidenzstärke gehört zur Beziehung, nicht zum Epistemicum. Reifizierung nötig, zu groß für v1.1. |
| EfficacyMode als OWL-Enum | ABGELEHNT | Werte sind 1:1 an Subklassen gebunden. `?x a min:Lex` = `?x hasEfficacyMode Lawful`. Redundant. |
| min:Uncertainty als Klasse | ABGELEHNT | 17 Typen haben fundamental verschiedene Ontologien. Kein einheitliches Ding. Verteilung auf Epistemicum + Possibile + sdata-uncertainty. |
| Data aufspalten (RawData/Document/Model) | VERSCHOBEN v2.0 | Braucht Community-Diskussion. |
| Nexus-Partition schließen | VERSCHOBEN v2.0 | Konsequenzen für Erweiterbarkeit unklar. |

---

## 11. Abhängigkeiten und Reihenfolge

```
Phase 1: TTL-Split (M12)
  ├── min-core.ttl extrahieren
  └── min-annotations.ttl extrahieren
  Voraussetzung für alles Weitere (saubere Arbeitsbasis)

Phase 2: CausalityMode-Formalisierung (M7, M8, M9)
  ├── CausalityMode-Klasse + 3 Individuals
  ├── hasCausalityMode Property
  ├── owl:Restriction auf Object, Process, Data, Boundary
  └── Alte causalityMode AnnotationProperty deprecaten
  Kann unabhängig von Phase 3 implementiert werden

Phase 3: Epistemische Dimension (M1–M6, M10, M11, M14, M15)
  ├── Epistemicum-Klasse
  ├── EpistemicStatus + ConfidenceType Enums
  ├── 8 Properties (holds, about, supportedBy, underminedBy, ...)
  ├── hasConfidence + isQuantifiable
  ├── supersedes → TransitiveProperty
  ├── Disjunktheitsaxiom erweitern
  └── confirms/refutes deprecaten
  Größter Block, aber atomar implementierbar

Phase 4: SHACL + Tests (M16)
  ├── EpistemicumShape
  ├── CausalityModeShape
  ├── Konsistenzregel Konfidenz→Typ
  └── 5 SPARQL-ASK Regressionstests

Phase 5: Beispiel-Graph
  └── Zugversuch-Szenario (~15 Knoten, ~30 Relationen)

Phase 6: Dokumentation (M13)
  ├── Englische Labels prüfen (alle Klassen + Properties)
  ├── 3 bestehende Seiten aktualisieren
  ├── 3 neue Seiten erstellen
  └── Changelog + Migration Guide

Phase 7: Release
  ├── min-v1.1.0.ttl erstellen (immutable Snapshot)
  ├── min.ttl → min-v1.1.0.ttl aktualisieren
  ├── Versionierung in Ontologie-Header
  └── GitHub Release + Tag
```

---

## 12. Aufwandsschätzung

| Phase | Deliverable | Aufwand |
|---|---|---|
| 1 — TTL-Split | min-core.ttl + min-annotations.ttl | 2 Tage |
| 2 — CausalityMode | Klasse + Individuals + Property + Restrictions | 1 Tag |
| 3 — Epistemische Dimension | 1 Klasse + 2 Enums + 10 Properties + 2 DatatypeProps | 3 Tage |
| 4 — SHACL + Tests | 2 Shapes + Konsistenzregel + 5 ASK-Tests | 1.5 Tage |
| 5 — Beispiel-Graph | Zugversuch end-to-end | 1 Tag |
| 6 — Dokumentation | 6 Seiten + englische Labels | 2.5 Tage |
| 7 — Release | Snapshot + Versionierung + GitHub | 0.5 Tage |
| **Gesamt** | | **~11.5 Tage** |

---

## 13. Roadmap: Was kommt nach v1.1?

```
v1.1.0  ← DIESER PLAN
        Epistemicum, CausalityMode-Enum, TTL-Split, isQuantifiable

v1.1.1  Bugfixes, SHACL-Verfeinerung nach erstem Einsatz

v1.2.0  Reifizierte Evidenz (EvidenceRelation mit Typ + Gewicht)
        Alignment-Module (PROV-O, QUDT, schema.org) als separate TTL

v2.0.0  Grundsatzentscheidungen:
        - Nexus-Partition offen oder geschlossen?
        - Data aufspalten?
        - Agent ∩ Process klären?
        - MIN-Namespace-Strategie (# vs /)

sdata v0.2.0 (parallel, eigener Release-Zyklus):
        - sdata-uncertainty.ttl (UncertaintyAssignment-Pattern, 15-Typen SKOS)
        - EpistemicAxis in sdata-material-state
        - Facades für Epistemicum
        - DPP-Profil (sdata-dpp.ttl)
        - DT-Profil (sdata-dt.ttl)
```

---

## 14. Erfolgskriterien

```
MIN v1.1.0 ist erfolgreich, wenn:

1. Alle v1.0.0 Graphen unverändert valide bleiben.
2. min-core.ttl < 20 KB und ohne Prosa ladbar ist.
3. SPARQL Q1–Q9 korrekte Ergebnisse auf dem Beispiel-Graph liefern.
4. Alle 5 SPARQL-ASK Tests bestehen (T1–T5).
5. SHACL-Validierung des Beispiel-Graphs fehlerfrei durchläuft.
6. Kein OWL-DL Profil-Verstoß in min-core.ttl (Protégé/robot verify).
7. Ein Ingenieur ohne Ontologie-Vorwissen den Beispiel-Graph
   in 30 Minuten lesen und eine Query modifizieren kann.
```

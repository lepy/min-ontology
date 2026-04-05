# MIN v1.1.0 — Bereinigter Implementierungsplan (Rev. 4, Baseline v1.0.1)

**Baseline:** MIN v1.0.1, sdata-ontology v0.2.0 (10 Module), sdata-experiments
**Datum:** 2026-04
**Vorgaenger:** Rev. 3 (min-v1.1-plan-rev3-baseline-v1.0.1.md)

---

## 0. Aenderungen gegenueber Rev. 3

| # | Rev. 3 | Rev. 4 | Begruendung |
|---|--------|--------|-------------|
| 1 | confirms/refutes deprecaten zugunsten supportedBy/underminedBy | confirms/refutes BEHALTEN; supportedBy/underminedBy als NEUE komplementaere Properties | Nicht semantisch erhaltend — Traegerklasse (Process vs. Epistemicum), Zielklasse (Forma/Possibile vs. Nexus) und Richtung aendern sich. Beide Muster werden gebraucht. |
| 2 | EM_Epistemic als neues EfficacyMode-Individual | GESTRICHEN | EfficacyMode bildet die Art der Bestimmung ab (1:1 an Subklassen). Epistemicum bestimmt nichts, es bewertet. hasEpistemicStatus und hasConfidenceType erfassen die epistemische Dimension korrekt. |
| 3 | supersedes → owl:TransitiveProperty | supersedes BLEIBT nicht-transitiv | v1.0.1 deklariert "Not transitive" (min.ttl:542). Begruendung gilt weiter. SPARQL Property Paths (supersedes+) liefern Query-Time-Transitivitaet ohne ontologische Umdeutung. |
| 4 | sdata-ontology: 6 Module genannt | Korrigiert auf 10 Module | sdata-structure, sdata-degradation, sdata-assessment, sdata-sustainability fehlten. Gerade sdata-assessment ist epistemisch relevant (EvidenceRecord, ComplianceAssessment). |
| 5 | Forma-Partition Risiko "gering" | Risiko "kontrollierter Breaking Change" | sdata-experiments nutzt Forma aktiv. Erweiterung ist monoton, aber Reasoner muessen aktualisiert werden. Migrationsdoku noetig. |
| 6 | Object Properties (8) — listet 9 | Korrekte Zaehlung: 7 neue Object Properties | holds/heldBy, about, supportedBy/supports, underminedBy/undermines = 7. Dazu 2 funktionale (hasEpistemicStatus, hasConfidenceType) = 9 gesamt. |
| 7 | heldBy: sh:minCount 0 | Entfernt (tautologisch) | sh:minCount 0 ist keine SHACL-Einschraenkung. Agent-Optionalitaet wird ueber Dokumentation + Abwesenheit einer minCount-Regel ausgedrueckt. |
| 8 | sms:EpistemicAxis als bestehend referenziert | Als NEU ZU SCHAFFEN gekennzeichnet | Existiert noch nicht in sdata-material-state.ttl. Inhaltlich eine Provenienzachse, keine epistemische. |

---

## 1. Was v1.0.1 bereits erledigt hat

| Massnahme | Status in v1.0.1 |
|---|---|
| TTL-Split (min.ttl + min-docs.ttl) | erledigt |
| CausalityMode als OWL-Enum (3 Individuals) | erledigt |
| EfficacyMode als OWL-Enum (10 Individuals) | erledigt |
| hasCausalityMode / hasEfficacyMode als ObjectProperty | erledigt |
| owl:hasValue Restrictions auf Klassen | erledigt |
| Nexus-Partition geschlossen | erledigt |
| Forma-Partition geschlossen (5 Subklassen) | erledigt |
| constrainedBy inverse ergaenzt | erledigt |
| Datatype Properties → Dublin Core aligned | erledigt |
| owns Range → Entity | erledigt |
| Agent ∩ Process disjunkt | erledigt |
| startedAt / endedAt auf Process | erledigt |
| Englische Labels/Comments durchgaengig | erledigt |
| SHACL-Shapes vollstaendig (49 Object Properties) | erledigt |
| Epistemic Relations im Property Catalog dokumentiert | erledigt |
| Forma-Entscheidungsbaum | erledigt |
| 7 Alignment-Module (PROV-O, BFO, schema.org, SOSA, DOLCE, QUDT, dcterms) | erledigt |
| DPP-Use-Case (dpp-coil.ttl) | erledigt |

**Fazit:** v1.0.1 hat 18 von 18 Non-Epistemicum-Massnahmen implementiert,
einschliesslich Dinge, die der urspruengliche Plan erst fuer v2.0 vorgesehen hatte
(geschlossene Partitionen, Agent⊥Process). v1.1 ist ein fokussiertes Release:
**nur Epistemicum.**

---

## 2. Downstream-Kontext

### sdata-ontology v0.2.0 — vollstaendiges Modulbild

```
Modularer Layer (10 Module):

  sdata-measurements       → Messungen, Messergebnisse
  sdata-equipment          → Pruefgeraete, Kalibrierung
  sdata-protocols          → Versuchsplaene, Verfahren
  sdata-specimens          → Probenkoerper, Probenahme
  sdata-processes          → Verarbeitungsschritte
  sdata-materials          → Werkstoffdaten, Legierungen
  sdata-structure          → Gefuege, Mikrostruktur
  sdata-degradation        → Schaedigung, Alterung, Verschleiss
  sdata-assessment         → Bewertung, Konformitaet, Evidenz   ← epistemisch relevant
  sdata-sustainability     → Nachhaltigkeit, Oekobilanz

Zusaetzlich:
  sdata-core               → Mittelschicht (Facades zu MIN)
  sdata-material-state     → Zustandsraum (13 Achsen, erweiterbar)
  sdata-quantities         → Physikalische Groessen
```

**Epistemische Relevanz:** `sdata-assessment` enthaelt `ComplianceAssessment`,
`Nonconformity`, `EvidenceRecord` — die Epistemicum-Facades muessen gegen
dieses Modul geprueft werden, um Ueberlappungen zu vermeiden.

### sdata-experiments

45 Commits. Aktive Nutzung des Forma-Zweigs:

```
sdt:TestFormalModel        a sdata:Structura
sdt:TestAcceptanceCriterion a sdata:Norma
sdt:TestGoverningLaw       a sdata:Lex
```

Nicht in Gebrauch: min:confirms, min:refutes, min:supersedes, min:Possibile (nur
in Kommentaren), min:Institutio (nicht referenziert).

---

## 3. Forma-Partition: Kontrollierter Breaking Change

v1.0.1 deklariert:

```
Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio
```

v1.1.0 erweitert:

```
Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio ⊔ Epistemicum
```

**Auswirkung:** Die Erweiterung ist monoton — was vorher in Forma war, bleibt
in Forma. Aber jeder Reasoner, der gegen die geschlossene 5er-Partition
inferiert, muss aktualisiert werden. sdata-experiments nutzt den Forma-Zweig
aktiv.

**Risikobewertung:** Mittel. Es ist ein kontrollierter Breaking Change.
Die Erweiterung selbst ist semantisch sauber, aber Migrationsdokumentation
ist Pflicht.

**Mitigationsmassnahmen:**
- Migration Guide (docs/migration-v1.0-to-v1.1.md)
- CHANGELOG-Eintrag mit explizitem Hinweis
- sdata-core Facade-Update gleichzeitig bereitstellen

---

## 4. Verbleibender Scope v1.1.0

### 4.1 Massnahmen

| # | Massnahme | Typ |
|---|----------|-----|
| E1 | Epistemicum als 6. Forma-Subklasse | Neue Klasse |
| E2 | EpistemicStatus-Enum (5 Individuals) | Neue Klasse + Individuals |
| E3 | ConfidenceType-Enum (4 Individuals) | Neue Klasse + Individuals |
| E4 | holds / heldBy (Agent ↔ Epistemicum) | Neue Properties |
| E5 | about (Epistemicum → Entity) | Neue Property |
| E6 | supportedBy / supports (Epistemicum ↔ Nexus) | Neue Properties |
| E7 | underminedBy / undermines (Epistemicum ↔ Nexus) | Neue Properties |
| E8 | hasEpistemicStatus (functional, Epistemicum → EpistemicStatus) | Neue Property |
| E9 | hasConfidenceType (functional, Epistemicum → ConfidenceType) | Neue Property |
| E10 | hasConfidence (Epistemicum → xsd:double [0..1]) | Neue Property |
| E11 | isQuantifiable (Possibile → xsd:boolean) | Neue Property |
| E12 | Forma-Partition erweitern (+ Epistemicum) | Axiom-Aenderung |
| E13 | AllDisjointClasses Forma-intern erweitern (+ Epistemicum) | Axiom-Aenderung |
| E14 | SHACL: EpistemicumShape + Konsistenzregel Konfidenz→Typ | Validierung |
| E15 | SHACL: sh:class min:Nexus auf supportedBy/underminedBy | Validierung |
| E16 | Beispiel-Graph (Zugversuch mit Epistemicum) | Beispiel |
| E17 | Competency Queries (10 SPARQL) | Test |
| E18 | Regressionstests (SPARQL ASK) | Test |
| E19 | Dokumentation (class-catalog, property-catalog, epistemic-dimension.md) | Doku |
| E20 | Migration Guide (v1.0 → v1.1) | Doku |

### 4.2 Explizit NICHT in v1.1.0

| Massnahme | Status | Begruendung |
|----------|--------|-------------|
| EM_Epistemic in EfficacyMode | GESTRICHEN | Kategorienverwechslung; EfficacyMode = Art der Bestimmung, Epistemicum bestimmt nicht |
| Deprecation confirms/refutes | GESTRICHEN | Anderes Muster (Process → Forma) als supportedBy (Epistemicum ← Nexus) |
| supersedes → TransitiveProperty | GESTRICHEN | Widerspricht expliziter Baseline-Entscheidung; SPARQL Property Paths genuegen |
| Reifizierte Evidenzgewichtung | VERSCHOBEN v1.2 | Zu gross; braucht Erfahrung mit v1.1 |
| sdata-uncertainty.ttl | VERSCHOBEN sdata v0.4.0 | Eigenstaendiges Modul, eigener Release |

---

## 5. Detailentwurf

### 5.1 Epistemicum — 6. Forma-Subklasse

```turtle
min:Epistemicum a owl:Class ;
    rdfs:subClassOf min:Forma ;
    rdfs:label "Epistemicum"@en , "Epistemicum"@de ;
    rdfs:comment "That which is held to be true. Epistemic stance of an
        agent towards a state of affairs."@en .
```

**Existenzkriterium:** Kann man fragen: "Gilt F laut Agent A?" — und ist
die Antwort im Wissensgraph darstellbar?

**Warum Forma:**
- Bewirkt nichts kausal → nicht Nexus
- Bestimmt, wie ein Agent Nexus interpretiert → konstitutive Bestimmung
- Passt in keine bestehende Forma-Subklasse (geprueft gegen alle 5)

**Agent-Optionalitaet:** heldBy hat keine SHACL-Mindestkardinalitaet.
Agent-freie Epistemicum-Instanzen modellieren institutionalisierte
epistemische Zustaende: "Dieser Datensatz gilt als verifiziert."
Provenienz laeuft ueber das bestehende originatedBy.

**Kein EfficacyMode:** Epistemicum bekommt KEIN eigenes EfficacyMode-Individual.
EfficacyMode bildet die Art der Bestimmung ab (lawful, structural, modal,
normative, institutional). Epistemicum bestimmt nichts — es bewertet.
Die epistemische Dimension wird durch hasEpistemicStatus und hasConfidenceType
als eigene orthogonale Achsen abgebildet.

**Abgrenzung:**

| Verwechslungsgefahr | Unterschied |
|---|---|
| Possibile | Possibile ist eine Moeglichkeit. Epistemicum ist eine Haltung gegenueber einer Moeglichkeit/Lex/Norma. |
| Data | Data kodiert Information (Bytes). Epistemicum bewertet Information (Gueltigkeit). |
| Norma | Norma sagt, was gelten soll. Epistemicum sagt, was fuer wahr gehalten wird. |

### 5.2 Enums

```turtle
# --- EpistemicStatus ---

min:EpistemicStatus a owl:Class ;
    rdfs:label "Epistemic Status"@en ;
    owl:oneOf ( min:ES_Hypothetical min:ES_Confirmed min:ES_Refuted
                min:ES_Contested min:ES_Axiomatic ) .

min:ES_Hypothetical  a min:EpistemicStatus ; rdfs:label "hypothetical"@en .
min:ES_Confirmed     a min:EpistemicStatus ; rdfs:label "confirmed"@en .
min:ES_Refuted       a min:EpistemicStatus ; rdfs:label "refuted"@en .
min:ES_Contested     a min:EpistemicStatus ; rdfs:label "contested"@en .
min:ES_Axiomatic     a min:EpistemicStatus ; rdfs:label "axiomatic"@en .

# --- ConfidenceType ---

min:ConfidenceType a owl:Class ;
    rdfs:label "Confidence Type"@en ;
    owl:oneOf ( min:CT_Subjective min:CT_Statistical
                min:CT_Bayesian min:CT_Heuristic ) .

min:CT_Subjective    a min:ConfidenceType ; rdfs:label "subjective"@en .
min:CT_Statistical   a min:ConfidenceType ; rdfs:label "statistical"@en .
min:CT_Bayesian      a min:ConfidenceType ; rdfs:label "bayesian"@en .
min:CT_Heuristic     a min:ConfidenceType ; rdfs:label "heuristic"@en .
```

**Namenskonvention:** Praefix ES_ und CT_ analog zu CM_ und EM_ in v1.0.1.
Verhindert Namenskollisionen mit allgemeinen Termen.

### 5.3 Properties

**Neue Object Properties (7):**

| Property | Domain | Range | Inverse | Semantik |
|---|---|---|---|---|
| holds | Agent | Epistemicum | heldBy | Agent vertritt epistemische Haltung |
| heldBy | Epistemicum | Agent | holds | Inverse |
| about | Epistemicum | Entity | — | Epistemicum bezieht sich auf Sachverhalt |
| supportedBy | Epistemicum | Nexus | supports | Evidenz stuetzt Haltung |
| supports | Nexus | Epistemicum | supportedBy | Inverse |
| underminedBy | Epistemicum | Nexus | undermines | Evidenz schwaecht Haltung |
| undermines | Nexus | Epistemicum | underminedBy | Inverse |

**Neue funktionale Object Properties (2):**

| Property | Domain | Range | Semantik |
|---|---|---|---|
| hasEpistemicStatus | Epistemicum | EpistemicStatus | Genau ein Status |
| hasConfidenceType | Epistemicum | ConfidenceType | Genau ein Typ (wenn Konfidenz angegeben) |

**Neue Datatype Properties (2):**

| Property | Domain | Range | Semantik |
|---|---|---|---|
| hasConfidence | Epistemicum | xsd:double [0.0..1.0] | Quantitativer Sicherheitsgrad |
| isQuantifiable | Possibile | xsd:boolean | Risiko (true) vs. Knightsche Unsicherheit (false) |

**Gesamtzaehlung:** 7 + 2 + 2 = 11 neue Properties.

### 5.4 Verhaeltnis zu bestehenden epistemischen Relationen

Die bestehenden epistemischen Relationen in v1.0.1 BLEIBEN unveraendert:

```
BESTEHEND (v1.0.1 — prozesszentrisch, Poppersch):
  confirms      Process → Forma       "Prozess bestaetigt Forma als tragfaehig"
  confirmedBy   Forma → Process       (inverse)
  refutes       Process → Possibile   "Prozess widerlegt Possibile"
  refutedBy     Possibile → Process   (inverse)
  entails       Forma → Forma         "Logische Implikation" (transitiv)
  supersedes    Forma → Forma         "Abloesung" (NICHT transitiv)
  supersededBy  Forma → Forma         (inverse)
  justifiedBy   Institutio → Forma    "Epistemische Begruendung"
  justifies     Forma → Institutio    (inverse)

NEU (v1.1.0 — epistemicum-zentrisch, evidenzbasiert):
  supportedBy   Epistemicum → Nexus   "Stance gestuetzt durch Nexus"
  supports      Nexus → Epistemicum   (inverse)
  underminedBy  Epistemicum → Nexus   "Stance geschwaecht durch Nexus"
  undermines    Nexus → Epistemicum   (inverse)
```

**Warum beide Muster:**

Das Poppersche Muster (confirms/refutes) drueckt aus, dass ein **Prozess**
als Pruefinstanz fungiert — der Zugversuch bestaetigt das Hooke'sche Gesetz.
Traeger der epistemischen Handlung ist der Prozess.

Das Evidenzmuster (supportedBy/underminedBy) drueckt aus, dass eine
**epistemische Haltung** durch Evidenz gestuetzt oder geschwaecht wird —
die Hypothese wird durch Messdaten gestuetzt. Traeger der epistemischen
Haltung ist das Epistemicum.

In einem Zugversuch-Szenario braucht man beides:

```turtle
# Poppersch: Prozess als Pruefinstanz
ex:Zugversuch_1  min:confirms  ex:Hooke .

# Evidenzbasiert: Stance gestuetzt durch Data
ex:Hypothese_v1  min:supportedBy  ex:Messdaten_1 .
ex:Hypothese_v1  min:about  ex:Hooke .
ex:Hypothese_v1  min:heldBy  ex:Mueller .
ex:Hypothese_v1  min:hasEpistemicStatus  min:ES_Confirmed .
```

### 5.5 supersedes bleibt nicht-transitiv

v1.0.1 deklariert supersedes als nicht-transitiv (min.ttl:542). Diese
Entscheidung wird in v1.1.0 beibehalten.

**Begruendung:** A supersedes B und B supersedes C impliziert nicht,
dass A direkt C abloest. Zwischenversionen koennen Kontext aendern
(z.B. Normversionen, die aufeinander aufbauen).

**Fuer Historien-Queries:** SPARQL Property Paths liefern Query-Time-
Transitivitaet:

```sparql
SELECT ?latest ?earliest WHERE {
    ?latest min:supersedes+ ?earliest .
}
```

**Falls ontologischer Mechanismus gewuenscht:** Eine abgeleitete
Super-Property ist sauberer als die Umdeutung von supersedes:

```turtle
# OPTION (nicht in v1.1.0, ggf. v1.2.0):
min:historicallySupersedes a owl:ObjectProperty, owl:TransitiveProperty ;
    rdfs:subPropertyOf min:supersedes ;
    rdfs:comment "Transitive closure over supersedes chains." .
```

### 5.6 Axiom-Aenderungen

```
Forma ≡ ... ⊔ Epistemicum               (Partition erweitern)
AllDisjointClasses ( ... Epistemicum )    (Disjunktheit erweitern)
```

Keine weiteren Axiom-Aenderungen. supersedes und EfficacyMode bleiben
unveraendert.

---

## 6. SHACL-Shapes

### 6.1 EpistemicumShape (min-instance.shacl.ttl erweitern)

```
Zielklasse: min:Epistemicum

about:
  sh:minCount 1                ← PFLICHT
  sh:class min:Entity

heldBy:
  sh:class min:Agent           ← keine Mindestkardinalitaet (agent-frei erlaubt)

hasEpistemicStatus:
  sh:minCount 1
  sh:maxCount 1                ← genau einer
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
Begruendung: Nackte Konfidenz ohne Typ ist semantisch unterdefiniert.
```

### 6.3 Bestehende Shapes

ClassLabelShape muss um Epistemicum, EpistemicStatus, ConfidenceType
erweitert werden (+3 Klassen). ObjectPropertyDomainRangeShape deckt
die neuen Properties automatisch ab.

---

## 7. Competency Queries

### 7.1 Epistemicum-Queries

```sparql
Q1: Alle Hypothesen eines Agents
    SELECT ?e ?gegenstand ?konfidenz WHERE {
        ?e min:heldBy ?agent ; min:about ?gegenstand ;
           min:hasEpistemicStatus min:ES_Hypothetical ;
           min:hasConfidence ?konfidenz .
    }

Q2: Agent-freie epistemische Zustaende (institutionalisiert)
    SELECT ?e WHERE {
        ?e a min:Epistemicum .
        FILTER NOT EXISTS { ?e min:heldBy ?a }
    }

Q3: Widerspruechliche Evidenz
    SELECT ?e ?pro ?contra WHERE {
        ?e min:supportedBy ?pro ; min:underminedBy ?contra .
    }

Q4: Dissens zwischen Agents
    SELECT ?forma ?a1 ?a2 WHERE {
        ?e1 min:about ?forma ; min:heldBy ?a1 ;
            min:hasEpistemicStatus min:ES_Confirmed .
        ?e2 min:about ?forma ; min:heldBy ?a2 ;
            min:hasEpistemicStatus min:ES_Refuted .
        FILTER (?a1 != ?a2)
    }

Q5: Epistemische Historie (Property Path, KEIN transitives supersedes)
    SELECT ?latest ?earliest WHERE {
        ?latest a min:Epistemicum .
        ?latest min:supersedes+ ?earliest .
    }

Q6: Niedrige Konfidenz
    SELECT ?e ?c WHERE {
        ?e min:hasConfidence ?c . FILTER (?c < 0.5)
    }

Q7: Alle subjektiven Schaetzungen
    SELECT ?e ?c WHERE {
        ?e min:hasConfidenceType min:CT_Subjective ;
           min:hasConfidence ?c .
    }

Q8: Prozesszentrische Bestaetigung (bestehendes Muster)
    SELECT ?process ?forma WHERE {
        ?process min:confirms ?forma .
    }

Q9: Widerlegte Possibilia (bestehendes Muster)
    SELECT ?process ?possibile WHERE {
        ?process min:refutes ?possibile .
    }

Q10: Quantifizierbare vs. nicht-quantifizierbare Moeglichkeiten
     SELECT ?p ?q WHERE {
         ?p a min:Possibile ; min:isQuantifiable ?q .
     }
```

### 7.2 Regressionstests (SPARQL ASK)

```sparql
T1: Epistemicum ist disjunkt mit Lex
    ASK { ?x a min:Epistemicum, min:Lex . }  → false

T2: supportedBy zeigt nur auf Nexus
    ASK { ?x min:supportedBy ?y . ?y a min:Forma . }  → false

T3: Jedes Epistemicum mit Konfidenz hat einen Typ
    ASK { ?x min:hasConfidence ?c .
          FILTER NOT EXISTS { ?x min:hasConfidenceType ?t } }  → false

T4: supersedes ist NICHT transitiv
    # Gegeben: A supersedes B, B supersedes C
    # Ohne Reasoning darf A supersedes C NICHT inferiert werden.
    # (Property Path A supersedes+ C funktioniert trotzdem.)

T5: confirms hat weiterhin Domain Process, Range Forma
    ASK { ?x min:confirms ?y . FILTER NOT EXISTS { ?x a min:Process } }  → false

T6: Forma-Partition enthaelt Epistemicum
    ASK { min:Epistemicum rdfs:subClassOf min:Forma . }  → true
```

---

## 8. Beispiel-Graph: Zugversuch mit Epistemicum

```
Szenario:
  Ingenieur Mueller glaubt, dass Hooke fuer DC04 bis 200 MPa gilt.
  Er fuehrt einen Zugversuch durch.
  Messdaten stuetzen die Hypothese.
  Konfidenz steigt von 0.8 (subjektiv) auf 0.95 (statistisch).
  Zweiter Versuch bei 300 MPa widerlegt die Hypothese.

Knoten:
  2 Agents          (Mueller, Zugpruefmaschine)
  3 Objects         (Blech, Probe, Probe_nach)
  2 Processes       (Zugversuch_1, Zugversuch_2)
  3 Data            (Messdaten_1, Messdaten_2, Pruefprotokoll)
  3 Epistemicum     (Hypothese_v1, Hypothese_v2, Hypothese_widerlegt)
  1 Lex             (Hooke)
  1 Norma           (Rm >= 270 MPa)

Demonstriert BEIDE epistemische Muster:

  Poppersch (bestehend):
    Zugversuch_1 min:confirms Hooke .
    Zugversuch_2 min:refutes Hypothese_Hooke_bis_300 .      ← refutes Possibile

  Evidenzbasiert (neu):
    Hypothese_v1 min:supportedBy Messdaten_1 .
    Hypothese_widerlegt min:underminedBy Messdaten_2 .

  Epistemicum-Kette:
    Hypothese_v2 min:supersedes Hypothese_v1 .
    Hypothese_widerlegt min:supersedes Hypothese_v2 .

  Status + Konfidenz:
    Hypothese_v1 min:hasEpistemicStatus min:ES_Hypothetical ;
                 min:hasConfidence 0.8 ;
                 min:hasConfidenceType min:CT_Subjective .
    Hypothese_v2 min:hasEpistemicStatus min:ES_Confirmed ;
                 min:hasConfidence 0.95 ;
                 min:hasConfidenceType min:CT_Statistical .
    Hypothese_widerlegt min:hasEpistemicStatus min:ES_Refuted .

Relationen: ~35
```

---

## 9. Inventar: Alle neuen Terme in v1.1.0

```
NEUE KLASSEN:              3  (Epistemicum, EpistemicStatus, ConfidenceType)

NEUE INDIVIDUALS:          9  (5 EpistemicStatus + 4 ConfidenceType)

NEUE OBJECT PROPERTIES:    9  (holds, heldBy, about,
                               supportedBy, supports,
                               underminedBy, undermines,
                               hasEpistemicStatus, hasConfidenceType)

NEUE DATATYPE PROPERTIES:  2  (hasConfidence, isQuantifiable)

GEAENDERTE AXIOME:         2  (Forma-Partition erweitern,
                               AllDisjointClasses erweitern)

DEPRECATED:                0  (confirms/refutes bleiben)

GEBROCHENE AXIOME:         1  (Forma-Partition wird erweitert —
                               monotoner Bruch, Migrationsdoku noetig)
```

---

## 10. Abhaengigkeiten und Reihenfolge

```
Phase 1: MIN v1.1.0 — Kern
  ├── Epistemicum-Klasse
  ├── EpistemicStatus + ConfidenceType Enums (9 Individuals)
  ├── 9 Object Properties + 2 Datatype Properties
  ├── Forma-Partition erweitern
  ├── AllDisjointClasses erweitern
  └── isQuantifiable auf Possibile

Phase 2: MIN v1.1.0 — Validierung
  ├── SHACL EpistemicumShape
  ├── SHACL Konsistenzregel Konfidenz→Typ
  ├── SPARQL ASK Regressionstests
  └── Beispiel-Graph

Phase 3: MIN v1.1.0 — Dokumentation + Release
  ├── class-catalog aktualisieren (+3 Klassen)
  ├── property-catalog aktualisieren (+11 Properties)
  ├── epistemic-dimension.md neu
  ├── migration-v1.0-to-v1.1.md neu
  ├── CHANGELOG.md
  ├── min-v1.1.0.ttl immutable Snapshot
  └── min-docs.ttl aktualisieren

Phase 4: sdata v0.3.0 (eigener Release)
  ├── Epistemicum-Facades in sdata-core
  ├── Abgleich mit sdata-assessment (EvidenceRecord-Abgrenzung)
  └── min-v1.0.1.ttl → min-v1.1.0.ttl im Vendor-Ordner

Phase 5: sdata-experiments
  └── TestHypothesis-Beispiel im tensiletest (nutzt beide Muster)
```

---

## 11. sdata-Integration (sdata v0.3.0)

### 11.1 sdata-core Facades

```turtle
sdata:Epistemicum         owl:equivalentClass    min:Epistemicum .
sdata:holds               owl:equivalentProperty min:holds .
sdata:about               owl:equivalentProperty min:about .
sdata:supportedBy         owl:equivalentProperty min:supportedBy .
sdata:underminedBy        owl:equivalentProperty min:underminedBy .
sdata:hasConfidence       owl:equivalentProperty min:hasConfidence .
sdata:hasEpistemicStatus  owl:equivalentProperty min:hasEpistemicStatus .
sdata:hasConfidenceType   owl:equivalentProperty min:hasConfidenceType .
```

### 11.2 Abgleich sdata-assessment

`sdata:EvidenceRecord` (Data-Subklasse) und `min:Epistemicum` (Forma-Subklasse)
sind komplementaer, nicht redundant:

| | EvidenceRecord | Epistemicum |
|---|---|---|
| **Ontologische Kategorie** | Data (Nexus) | Forma |
| **Semantik** | Traegt Information | Bewertet Information |
| **Typisches Beispiel** | Pruefprotokoll, Messdatensatz | "Hooke gilt bis 200 MPa" |

Ein EvidenceRecord kann ueber `supportedBy` ein Epistemicum stuetzen:

```turtle
ex:Hypothese_v1  min:supportedBy  ex:Pruefprotokoll .
ex:Pruefprotokoll  a sdata:EvidenceRecord .
```

### 11.3 EvidenceProvenanceAxis (sdata-material-state, NEU ZU SCHAFFEN)

Die im frueheren Plan als "EpistemicAxis" bezeichnete Achse existiert
noch nicht in sdata-material-state.ttl. Sie beschreibt die **Herkunft
von Evidenz**, nicht den epistemischen Status:

```
Measured     — durch Messung gewonnen
Simulated    — durch Simulation erzeugt
Assumed      — angenommen ohne direkte Evidenz
Certified    — durch institutionellen Akt bestaetigt
```

Das ist eine Provenienzachse, keine epistemische. Empfohlener Name:
`sms:EvidenceProvenanceAxis` statt `sms:EpistemicAxis`.

Orthogonal zu EpistemicStatus: ein Wert kann "Measured" (Provenienz)
und gleichzeitig "ES_Contested" (Status) sein.

### 11.4 sdata-experiments: Zugversuch mit beiden Mustern

```turtle
# Bestehendes Forma-Muster:
sdt:TestFormalModel         a sdata:Structura .
sdt:TestAcceptanceCriterion a sdata:Norma .
sdt:TestGoverningLaw        a sdata:Lex .

# Neues Epistemicum-Muster:
sdt:TestHypothesis a sdata:Epistemicum ;
    sdata:about sdt:TestGoverningLaw ;
    sdata:supportedBy sdt:TestResult ;
    sdata:hasEpistemicStatus min:ES_Hypothetical .

# Poppersch (wenn Zugversuch Gesetz bestaetigt):
sdt:TensileTest_001 min:confirms sdt:TestGoverningLaw .
```

---

## 12. Aufwandsschaetzung

| Phase | Deliverable | Aufwand |
|---|---|---|
| 1 — Kern | Epistemicum + Enums + Properties + Axiome | 2 Tage |
| 2 — Validierung | SHACL + Tests + Beispiel-Graph | 1.5 Tage |
| 3 — Dokumentation + Release | Kataloge + epistemic-dimension.md + Migration Guide + Snapshot | 1.5 Tage |
| 4 — sdata v0.3.0 | Facades + Assessment-Abgleich | 1 Tag |
| 5 — sdata-experiments | TestHypothesis im tensiletest | 0.5 Tage |
| **Gesamt** | | **~6.5 Tage** |

Weniger als Rev. 3 (7 Tage), weil EM_Epistemic, Deprecation-Migrationslast
und supersedes-Aenderung entfallen.

---

## 13. Erfolgskriterien

```
1. Alle v1.0.1 Graphen bleiben valide (keine Instanz-Inkompatibilitaet).
2. confirms/refutes funktionieren weiterhin mit unveraenderter Signatur.
3. Forma-Partition ist korrekt erweitert (Reasoner findet Epistemicum als Forma).
4. SPARQL Competency Queries Q1–Q10 liefern korrekte Ergebnisse.
5. SHACL: Epistemicum ohne hasEpistemicStatus → Validation Error.
6. SHACL: hasConfidence ohne hasConfidenceType → Validation Error.
7. SHACL: supportedBy auf Forma-Instanz → Validation Error.
8. supersedes ist und bleibt nicht-transitiv.
9. EfficacyMode-Enum hat weiterhin genau 10 Individuals.
10. sdata-experiments tensiletest mit TestHypothesis besteht Round-Trip-Test.
11. Kein OWL-DL Profil-Verstoss in min.ttl.
```

---

## 14. Abgelehnte Alternativen (Entscheidungsregister)

| Vorschlag | Status | Begruendung |
|-----------|--------|-------------|
| EM_Epistemic in EfficacyMode | GESTRICHEN (Rev. 4) | EfficacyMode = Art der Bestimmung, 1:1 an Subklassen. Epistemicum bestimmt nicht, es bewertet. hasEpistemicStatus/hasConfidenceType sind die korrekte epistemische Achse. |
| Deprecation confirms/refutes | GESTRICHEN (Rev. 4) | Traegerklasse (Process), Zielklasse (Forma/Possibile) und Semantik (Popper) unterscheiden sich fundamental von supportedBy/underminedBy (Epistemicum, Nexus, Evidenz). Kein Ersatz, sondern komplementaer. |
| supersedes → TransitiveProperty | GESTRICHEN (Rev. 4) | Explizit als nicht-transitiv deklariert in v1.0.1. SPARQL Property Paths genuegen fuer Historien-Queries. Optional: min:historicallySupersedes als abgeleitete Super-Property in v1.2.0. |
| aboutForma / aboutNexus Subproperties | ABGELEHNT | Erzwingt unnoetige Modellierungsentscheidung. SPARQL filtert ueber `?x a min:Forma`. |
| endorsedBy neben heldBy | ABGELEHNT | Semantisch redundant mit recognizedBy (Institutio ← Agent). |
| Axiomatic → Assumed | ABGELEHNT | Assumed existiert als sdata SKOS-Wert. Axiomatic meint prinzipiell nicht pruefbare Grundannahmen. |
| Evidenz-Gewichtung in v1.1 | VERSCHOBEN v1.2 | Evidenzstaerke gehoert zur Beziehung, nicht zum Epistemicum. Reifizierung noetig. |
| sms:EpistemicAxis (Naming) | KORRIGIERT | Achse beschreibt Evidenz-Provenienz (Measured/Simulated/Assumed/Certified), nicht epistemischen Status. Empfohlen: sms:EvidenceProvenanceAxis. |

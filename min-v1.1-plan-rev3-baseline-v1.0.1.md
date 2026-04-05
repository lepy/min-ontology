# MIN v1.1.0 — Konsolidierter Plan (Rev. 3, Baseline v1.0.1)

**Baseline:** MIN v1.0.1, sdata-ontology v0.2.0, sdata-experiments
**Datum:** 2026-04

---

## 1. Was v1.0.1 bereits erledigt hat

Das CHANGELOG von v1.0.1 zeigt: der Großteil der ursprünglichen Kritik
ist bereits umgesetzt. Aus dem konsolidierten Plan (Rev. 2) sind diese
Punkte ERLEDIGT:

| Maßnahme | Status in v1.0.1 |
|---|---|
| TTL-Split (min.ttl + min-docs.ttl) | ✅ erledigt |
| CausalityMode als OWL-Enum (3 Individuals) | ✅ erledigt |
| EfficacyMode als OWL-Enum (10 Individuals) | ✅ erledigt (Plan hatte es abgelehnt — wurde trotzdem gemacht) |
| hasCausalityMode / hasEfficacyMode als ObjectProperty | ✅ erledigt |
| owl:hasValue Restrictions auf Klassen | ✅ erledigt |
| Nexus-Partition geschlossen (Nexus ≡ Object ⊔ Process ⊔ Data ⊔ Boundary) | ✅ erledigt |
| Forma-Partition geschlossen (Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio) | ✅ erledigt |
| constrainedBy inverse ergänzt | ✅ erledigt |
| Datatype Properties → Dublin Core aligned | ✅ erledigt |
| owns Range → Entity | ✅ erledigt |
| Agent ∩ Process disjunkt (nicht mehr erlaubt) | ✅ erledigt |
| startedAt / endedAt auf Process | ✅ erledigt |
| Englische Labels/Comments durchgängig | ✅ erledigt |
| SHACL-Shapes vollständig (49 Object Properties) | ✅ erledigt |
| Epistemic Relations im Property Catalog dokumentiert | ✅ erledigt |
| Forma-Entscheidungsbaum | ✅ erledigt |
| Alignment PROV-O | ✅ erledigt |
| Alignment BFO 2020 | ✅ erledigt |
| Alignment schema.org | ✅ erledigt |
| Alignment SOSA | ✅ erledigt |
| Alignment DOLCE | ✅ erledigt |
| Alignment QUDT | ✅ erledigt |
| Alignment dcterms | ✅ erledigt |
| DPP-Use-Case (dpp-coil.ttl) | ✅ erledigt |

**Fazit:** Von den 16 Maßnahmen im ursprünglichen Plan sind 16 von 16
Non-Epistemicum-Maßnahmen bereits in v1.0.1 implementiert.
v1.0.1 hat außerdem Dinge gemacht, die der Plan erst für v2.0 vorgesehen hatte
(geschlossene Partitionen, Agent⊥Process).

---

## 2. Was sdata-ontology v0.2.0 und sdata-experiments zeigen

### sdata-ontology v0.2.0

Neue Module (referenziert aus sdata-experiments):

```
sdata-measurements    → https://w3id.org/sdata/measurements
sdata-equipment       → https://w3id.org/sdata/equipment
sdata-protocols       → https://w3id.org/sdata/protocols
sdata-specimens       → https://w3id.org/sdata/specimens
sdata-processes       → https://w3id.org/sdata/processes
sdata-materials       → https://w3id.org/sdata/materials
```

Das ist eine erhebliche Erweiterung gegenüber v0.1.0.
sdata-core ist jetzt eine Mittelschicht, darüber liegen domänenspezifische Module.

### sdata-experiments

45 Commits. Aktives Repo mit konkreter Nutzung des MIN/sdata-Stacks:

```
Import-Kette:
  MIN v1.0.1 → sdata-core → sdata-quantities
                           → sdata-measurements / equipment / protocols
                           → sdata-specimens / processes / materials
                           → sdata-testdata (core/)
                           → sdata-tensile / compression / bending / fatigue

Versuche: tensiletest, compressiontest, bendingtest, fatiguetest
Vokabulare: iso6892-1-skos.ttl, material-models.ttl, test-standards.ttl
SHACL: pro Testtyp + übergreifend
Alignment: PMDco (Platform MaterialDigital) optional
Beispiele: tensile-quality-loop.ttl mit Microstructure, Nonconformity, LCA
```

**Wichtig:** sdata-experiments nutzt den Forma-Zweig aktiv:
- `sdt:TestFormalModel` als `sdata:Structura`
- `sdt:TestAcceptanceCriterion` als `sdata:Norma`
- `sdt:TestGoverningLaw` als `sdata:Lex`
- Brückenrelationen über sdata-Facades

Das zeigt: der Forma-Zweig wird in der Praxis genutzt. Eine Erweiterung
um Epistemicum würde direkt in diesen Workflow einfließen.

---

## 3. Kritische Konsequenz: Forma-Partition ist geschlossen

v1.0.1 hat deklariert:

```
Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio
```

Das bedeutet: **Epistemicum als 6. Forma-Subklasse bricht dieses Axiom.**

Die Partition muss geöffnet werden:

```
VORHER (v1.0.1):
  Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio

NACHHER (v1.1.0):
  Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio ⊔ Epistemicum
```

Das ist ein Breaking Change an einem Axiom, das erst in v1.0.1 eingeführt
wurde. Alle Graphen, die auf der geschlossenen 5er-Partition reasoning,
müssen aktualisiert werden.

**Risikobewertung:** Gering. In der Praxis wird kaum jemand per Reasoner
geprüft haben, ob eine Forma-Instanz *nicht* in einer der 5 Klassen ist.
Die Erweiterung ist monoton: was vorher in Forma war, bleibt in Forma.
Nur neue Dinge (Epistemicum-Instanzen) kommen dazu.

---

## 4. Was v1.1.0 noch tun muss

### Verbleibender Scope (NUR Epistemische Dimension)

| # | Maßnahme | Aufwand |
|---|----------|--------|
| E1 | Epistemicum als 6. Forma-Subklasse | |
| E2 | EpistemicStatus-Enum (5 Individuals: Hypothetical, Confirmed, Refuted, Contested, Axiomatic) | |
| E3 | ConfidenceType-Enum (4 Individuals: Subjective, Statistical, Bayesian, Heuristic) | |
| E4 | holds / heldBy (Agent ↔ Epistemicum) | |
| E5 | about (Epistemicum → Entity) | |
| E6 | supportedBy / supports (Epistemicum ↔ Nexus) | |
| E7 | underminedBy / undermines (Epistemicum ↔ Nexus) | |
| E8 | hasEpistemicStatus (functional, Epistemicum → EpistemicStatus) | |
| E9 | hasConfidenceType (functional, Epistemicum → ConfidenceType) | |
| E10 | hasConfidence (Epistemicum → xsd:double [0..1]) | |
| E11 | isQuantifiable (Possibile → xsd:boolean) | |
| E12 | supersedes → owl:TransitiveProperty | |
| E13 | Forma-Partition erweitern (+ Epistemicum) | |
| E14 | AllDisjointClasses Forma-intern erweitern (+ Epistemicum) | |
| E15 | Deprecation: confirms → supportedBy, refutes → underminedBy | |
| E16 | SHACL: EpistemicumShape + Konsistenzregel Konfidenz→Typ | |
| E17 | SHACL: sh:class min:Nexus auf supportedBy/underminedBy | |
| E18 | Beispiel-Graph (Zugversuch mit Epistemicum) | |
| E19 | Competency Queries (10 SPARQL) | |
| E20 | Dokumentation (class-catalog, property-catalog, epistemic-dimension.md) | |
| E21 | Regressionstests (SPARQL ASK) | |

### Was NICHT mehr in v1.1.0 muss

Alles andere ist erledigt. Kein TTL-Split, kein CausalityMode, keine
Alignments, kein DPP-Beispiel, keine englischen Labels.
v1.1 ist ein fokussiertes Release: **nur Epistemicum.**

---

## 5. Detailentwurf (unverändert gegenüber Rev. 2, verkürzt)

### 5.1 Epistemicum

```
min:Epistemicum rdfs:subClassOf min:Forma .
Definition: "Das, was für wahr gehalten wird."
efficacyMode: EM_Epistemic (neues Individual in bestehender EfficacyMode-Enum)
heldBy: sh:minCount 0 (agent-frei erlaubt)
```

### 5.2 Enums

```
EpistemicStatus: Hypothetical | Confirmed | Refuted | Contested | Axiomatic
ConfidenceType: SubjectiveConfidence | StatisticalConfidence | BayesianConfidence | HeuristicConfidence
```

### 5.3 Properties

```
Object Properties (8):
  holds, heldBy, about, supportedBy, supports, underminedBy, undermines,
  hasEpistemicStatus, hasConfidenceType

Datatype Properties (2):
  hasConfidence, isQuantifiable
```

### 5.4 Axiom-Änderungen

```
Forma ≡ ... ⊔ Epistemicum         (Partition erweitern)
AllDisjointClasses + Epistemicum    (Disjunktheit erweitern)
supersedes → + TransitiveProperty   (Historien-Reasoning)
+ EM_Epistemic in EfficacyMode      (neues Individual)
```

### 5.5 SHACL-Konsistenzregel

```
Wenn hasConfidence vorhanden → hasConfidenceType MUSS vorhanden sein.
supportedBy/underminedBy → sh:class min:Nexus.
```

---

## 6. sdata-Integration (sdata v0.3.0)

### 6.1 sdata-core Facades

```
sdata:Epistemicum         owl:equivalentClass    min:Epistemicum
sdata:holds               owl:equivalentProperty min:holds
sdata:about               owl:equivalentProperty min:about
sdata:supportedBy         owl:equivalentProperty min:supportedBy
sdata:underminedBy        owl:equivalentProperty min:underminedBy
sdata:hasConfidence       owl:equivalentProperty min:hasConfidence
sdata:hasEpistemicStatus  owl:equivalentProperty min:hasEpistemicStatus
sdata:hasConfidenceType   owl:equivalentProperty min:hasConfidenceType
```

### 6.2 sdata-material-state: EpistemicAxis (Achse 14)

```
sms:EpistemicAxis (Measured | Simulated | Assumed | Certified)
Orthogonal zu EpistemicStatus (verschiedene Dimension).
```

### 6.3 sdata-experiments: Epistemicum im Zugversuch

sdata-experiments hat bereits einen tensiletest-Workflow mit Forma-Nutzung.
Epistemicum fügt sich dort natürlich ein:

```
sdt:TestFormalModel a sdata:Structura     ← bestehend
sdt:TestAcceptanceCriterion a sdata:Norma ← bestehend
sdt:TestGoverningLaw a sdata:Lex          ← bestehend

NEU:
sdt:TestHypothesis a sdata:Epistemicum ;
    sdata:about sdt:TestGoverningLaw ;
    sdata:supportedBy sdt:TestResult ;
    sdata:hasEpistemicStatus min:Hypothetical .
```

### 6.4 sdata-uncertainty.ttl (verschoben auf sdata v0.4.0)

Bleibt wie geplant: UncertaintyAssignment-Pattern, 15-Typen SKOS,
5 Quantifizierungsformen. Aber erst nach v0.3.0 (Epistemicum-Facades).

---

## 7. Abhängigkeiten und Reihenfolge

```
Phase 1: MIN v1.1.0 — Kern
  ├── Epistemicum-Klasse + EM_Epistemic Individual
  ├── EpistemicStatus + ConfidenceType Enums (9 Individuals)
  ├── 10 Properties
  ├── Forma-Partition erweitern
  ├── AllDisjointClasses erweitern
  ├── supersedes → TransitiveProperty
  └── confirms/refutes deprecaten

Phase 2: MIN v1.1.0 — Validierung
  ├── SHACL EpistemicumShape
  ├── SPARQL ASK Regressionstests
  └── Beispiel-Graph

Phase 3: MIN v1.1.0 — Dokumentation + Release
  ├── class-catalog, property-catalog aktualisieren
  ├── epistemic-dimension.md neu
  ├── CHANGELOG.md
  ├── min-v1.1.0.ttl immutable Snapshot
  └── min-docs.ttl aktualisieren

Phase 4: sdata v0.3.0 (eigener Release)
  ├── Epistemicum-Facades
  ├── EpistemicAxis in material-state
  └── min-v1.0.0.ttl → min-v1.1.0.ttl im Vendor-Ordner

Phase 5: sdata-experiments
  └── TestHypothesis-Beispiel im tensiletest
```

---

## 8. Aufwandsschätzung (bereinigt)

| Phase | Deliverable | Aufwand |
|---|---|---|
| 1 — Kern | Epistemicum + Enums + Properties + Axiome | 2.5 Tage |
| 2 — Validierung | SHACL + Tests + Beispiel-Graph | 1.5 Tage |
| 3 — Dokumentation + Release | 4 Seiten + Snapshot + CHANGELOG | 1.5 Tage |
| 4 — sdata v0.3.0 | Facades + EpistemicAxis | 1 Tag |
| 5 — sdata-experiments | TestHypothesis im tensiletest | 0.5 Tage |
| **Gesamt** | | **~7 Tage** |

Deutlich weniger als die 11.5 Tage im Rev. 2 Plan, weil TTL-Split,
CausalityMode, Alignments und DPP-Beispiel bereits erledigt sind.

---

## 9. Inventar: Alle neuen Terme in v1.1.0

```
NEUE KLASSEN:              3  (Epistemicum, EpistemicStatus, ConfidenceType)
NEUE INDIVIDUALS:         10  (5 Status + 4 Confidence + 1 EfficacyMode)
NEUE OBJECT PROPERTIES:    8  (holds/heldBy, about, supportedBy/supports,
                               underminedBy/undermines, hasEpistemicStatus,
                               hasConfidenceType)
NEUE DATATYPE PROPERTIES:  2  (hasConfidence, isQuantifiable)
GEÄNDERTE AXIOME:          3  (Forma-Partition, AllDisjointClasses, supersedes)
DEPRECATED:                2  (confirms, refutes)
GEBROCHENE AXIOME:         1  (Forma-Partition wird erweitert — monotoner Bruch)
```

---

## 10. Erfolgskriterien

```
1. Alle v1.0.1 Graphen bleiben valide (keine Instanz-Inkompatibilität).
2. Forma-Partition ist korrekt erweitert (Reasoner findet Epistemicum als Forma).
3. SPARQL Competency Queries Q1–Q10 liefern korrekte Ergebnisse.
4. SHACL: Epistemicum ohne hasEpistemicStatus → Validation Error.
5. SHACL: hasConfidence ohne hasConfidenceType → Validation Error.
6. SHACL: supportedBy auf Forma → Validation Error.
7. sdata-experiments tensiletest mit TestHypothesis besteht Round-Trip-Test.
8. Kein OWL-DL Profil-Verstoß in min.ttl.
```

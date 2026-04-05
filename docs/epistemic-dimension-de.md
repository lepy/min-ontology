# Epistemische Dimension (v1.1.0)

MIN v1.1.0 fuehrt `Epistemicum` als 6. Forma-Subklasse ein.

---

## Motivation

Ingenieurwissensgraphen muessen ausdruecken koennen:
- "Ingenieur Mueller glaubt, dass das Hooke'sche Gesetz fuer DC04 bis 200 MPa gilt."
- "Diese Hypothese wird durch Versuchsdaten mit 0.95 statistischer Konfidenz gestuetzt."
- "Zwei Experten sind sich uneinig, ob das Modell gueltig ist."

Vor v1.1.0 konnte MIN ausdruecken, dass ein Prozess ein Gesetz bestaetigt (`confirms`)
oder eine Moeglichkeit widerlegt (`refutes`), aber es konnte keinen epistemischen Status,
keine Konfidenz und keine Agent-Zuordnung an diese Urteile anhaengen.

---

## Designentscheidung: warum Forma?

Epistemicum ist nicht kausal wirksam (es transformiert keine Materie und
erzeugt keine Daten) — also ist es kein Nexus. Es bestimmt formal, wie ein
Agent einen Sachverhalt interpretiert — also ist es Forma.

Geprueft gegen alle bestehenden Forma-Subklassen:

| Subklasse | Warum Epistemicum anders ist |
|---|---|
| Lex | Lex gilt universell. Epistemicum ist die Haltung eines Agenten, kein Gesetz. |
| Structura | Structura formalisiert. Epistemicum bewertet. |
| Possibile | Possibile ist eine Moeglichkeit. Epistemicum ist eine Haltung *gegenueber* einer Moeglichkeit. |
| Norma | Norma schreibt vor, was gelten soll. Epistemicum beschreibt, was fuer wahr gehalten wird. |
| Institutio | Institutio existiert durch kollektive Anerkennung. Epistemicum kann von einem einzelnen Agenten vertreten werden. |

---

## Grundmechanik

Epistemicum hat fuenf Bausteine, die sich beliebig kombinieren:

- **WER** glaubt es? → `heldBy` Agent (oder agent-frei: institutionalisiert)
- **WAS** wird geglaubt? → `about` Entity (Lex, Norma, Data, Object, Process — alles)
- **WIE SICHER?** → `hasConfidence` [0..1] + `hasConfidenceType` (Subjective / Statistical / Bayesian / Heuristic)
- **WELCHER STATUS?** → `hasEpistemicStatus` (Hypothetical / Confirmed / Refuted / Contested / Axiomatic)
- **WORAUF GESTUETZT?** → `supportedBy` / `underminedBy` Nexus (Messdaten, Experimente, Berechnungen)

Aus diesen fuenf Bausteinen entstehen alle folgenden Patterns.

---

## Zwei komplementaere epistemische Muster

MIN v1.1.0 pflegt zwei verschiedene epistemische Muster:

### Muster 1: Prozesszentrisch (Poppersch, v1.0.0)

```turtle
ex:Zugversuch  min:confirms  ex:Hooke .
ex:Zugversuch  min:refutes   ex:Linearitaet_ueber_300MPa .
```

Der **Prozess** ist der Traeger. Semantik: ein Prozess bewertet einen
formalen Bestimmer als tragfaehig oder unhaltbar.

### Muster 2: Evidenzbasiert (Epistemicum, v1.1.0)

```turtle
ex:Hypothese  a min:Epistemicum ;
    min:heldBy       ex:Mueller ;
    min:about        ex:Hooke ;
    min:supportedBy  ex:Versuchsdaten ;
    min:hasEpistemicStatus  min:ES_Confirmed ;
    min:hasConfidence       0.95 ;
    min:hasConfidenceType   min:CT_Statistical .
```

Die **epistemische Haltung** ist der Traeger. Semantik: ein reifizierter
Glaube akkumuliert Evidenz, hat Status und Konfidenz.

Beide Muster werden in der Praxis gebraucht. Muster 1 ist kompakt und
genuegt fuer einfache Prozess-Aussagen. Muster 2 wird gebraucht, wenn sich
der epistemische Zustand ueber die Zeit aendert, wenn Konfidenz typisiert
werden muss, oder wenn mehrere Agenten widerspruechliche Haltungen vertreten.

---

## EpistemicStatus-Werte

| Wert | Bedeutung |
|---|---|
| ES_Hypothetical | Aufgestellt, weder bestaetigt noch widerlegt |
| ES_Confirmed | Durch Evidenz gestuetzt und akzeptiert |
| ES_Refuted | Durch Evidenz widerlegt |
| ES_Contested | Widerspruechliche Evidenz, kein Konsens |
| ES_Axiomatic | Grundannahme, nicht empirisch pruefbar |

## ConfidenceType-Werte

| Wert | Bedeutung |
|---|---|
| CT_Subjective | Experteneinschaetzung |
| CT_Statistical | Aus Stichprobe (Konfidenzintervall) |
| CT_Bayesian | A-posteriori-Wahrscheinlichkeit |
| CT_Heuristic | Erfahrungswert |

---

## Ingenieur-Patterns

**Modellvalidierung.** Ein FEM-Ingenieur modelliert: "Ich glaube, dass die Euler-Bernoulli-Balkentheorie (Structura) fuer diesen Lastfall gilt. Konfidenz 0.7 (HeuristicConfidence). Gestuetzt durch Simulationsdaten. Untergraben durch Messdaten bei hoher Last." Das ist V&V als Graph statt als Bericht.

**Materialfreigabe.** Ein Werkstoffpruefer modelliert: "Der Zugversuch (Process) bestaetigt, dass Rm >= 270 MPa (Norma) erfuellt ist. Status: Confirmed. Konfidenz 0.98 (StatisticalConfidence). Gestuetzt durch 30 Messwerte." Das Abnahmekriterium ist querybar: "Welche Norma-Instanzen am Bauteil sind Confirmed?"

**Schadensanalyse.** Ein Gutachter modelliert: "Hypothese: Korrosion (Process) hat das Versagen verursacht. Status: Contested. Agent A sagt Confirmed (gestuetzt durch Metallographie), Agent B sagt Refuted (gestuetzt durch Bruchflaechenanalyse)." Der Dissens ist sichtbar, nicht versteckt.

**Simulationskettenvertrauen.** In einer Prozesskette (Tiefziehen → Waermebehandlung → Montage) hat jeder Schritt eigene Unsicherheiten. Epistemicum erlaubt: pro Simulationsschritt eine Hypothese mit Konfidenz. Am Ende die Frage: "Welcher Schritt hat die niedrigste Konfidenz?" → dort zuerst validieren.

**Werkstoffmodellauswahl.** "Fuer PP-GF30 verwende ich das Mori-Tanaka-Modell (Structura). Status: Hypothetical. Konfidenz 0.6 (SubjectiveConfidence). Alternative: RVE-Homogenisierung (zweites Epistemicum, about selbe Structura, hoehere Konfidenz)." Entscheidungen werden begruendet und vergleichbar.

---

## DPP-Patterns (Digital Product Passport)

**Auditierbarer Recyclatanteil.** Nicht "42%", sondern: "42%, Epistemicum: Confirmed, Konfidenz 0.92 (StatisticalConfidence), supportedBy: XRF-Messdaten, heldBy: Prueflabor TUeV." Ein Auditor kann fragen: "Welche DPP-Eintraege haben Konfidenz < 0.5?" oder "Welche sind nur SubjectiveConfidence?"

**SVHC-Deklaration.** "Dieses Produkt enthaelt keine SVHC ueber 0.1%. Status: Confirmed. supportedBy: Lieferantenerklaerung (Data)." Versus: "Status: Hypothetical. supportedBy: keine." Der Unterschied ist regulatorisch relevant.

**Lieferkettenvertrauen.** Jeder Akteur in der Kette fuegt Epistemicum-Instanzen hinzu. Rohstofflieferant: "Herkunft: Virgin. Konfidenz 0.99." Recycler: "Herkunft: Recycled, 60% Anteil. Konfidenz 0.85." OEM: kann die gesamte Kette abfragen und die schwaechste Stelle identifizieren.

**DPP-Vollstaendigkeitsanalyse.** Query: "Welche Pflichtfelder im DPP haben *kein* zugehoeriges Epistemicum?" → die Luecken werden sichtbar. "Welche haben Status Assumed statt Confirmed?" → die Schwachstellen auch.

---

## Digital-Twin-Patterns

**Sensor-Glaubwuerdigkeit.** Ein Sensor (HardwareAgent) liefert Temperaturdaten (Data). Epistemicum: "Diese Daten sind korrekt. Status: Confirmed. Konfidenz 0.95." Nach Kalibrierungsdrift: "Status: Contested. Konfidenz 0.4. underminedBy: Referenzmessung." Der Digital Twin weiss, welchen Sensoren er trauen kann.

**Praediktive Wartung.** Ein ML-Modell (SoftwareAgent) sagt: "Bauteil versagt in 200 Betriebsstunden (Possibile). Konfidenz 0.72 (BayesianConfidence). supportedBy: Vibrationsdaten der letzten 30 Tage." Die Wartungsentscheidung hat eine formale Grundlage.

**Modell-Update.** Alte Hypothese: "Lineares Degradationsmodell gilt." Neue Hypothese supersedes alte, mit hoeherer Konfidenz, gestuetzt durch mehr Daten. Die Historie ist ueber Property Paths querybar: "Was haben wir vor 6 Monaten geglaubt, und warum nicht mehr?"

---

## Wissenschaftliche Patterns

**Hypothese → Experiment → Ergebnis.** Der klassische wissenschaftliche Zyklus wird zum Graph-Pattern:

1. Epistemicum (Hypothetical, about Lex)
2. Process (Experiment) generates Data
3. Data supportedBy/underminedBy Epistemicum
4. Neues Epistemicum (Confirmed/Refuted) supersedes altes

**Peer Review.** Reviewer A: Epistemicum about Paper-These, Confirmed. Reviewer B: Epistemicum about selbe These, Refuted. Status des Papers: Contested. Querybar: "Welche Thesen in meinem Forschungsprojekt sind contested?"

**Reproduzierbarkeit.** Originalstudie: Epistemicum, Confirmed, supportedBy Experiment_1. Replikationsstudie: neues Epistemicum, underminedBy Experiment_2. Der Replikationsstatus ist formalisiert.

**Meta-Analyse.** Mehrere Epistemicum-Instanzen about selbe Lex, verschiedene supportedBy-Datensaetze, verschiedene Konfidenzen. Die Meta-Frage "Wie gut ist F=ma fuer diesen Parameterbereich gestuetzt?" wird ein Aggregations-Query.

---

## Organisations-Patterns

**Wissensmanagement.** "Abteilung A glaubt, dass Verfahren X optimal ist. Abteilung B bevorzugt Y." Beides formalisiert als Epistemicum mit verschiedenen supportedBy-Evidenzen. Die Geschaeftsfuehrung kann fragen: "Wo gibt es Dissens zwischen Abteilungen?"

**Lessons Learned.** Ein Projektfehler wird als Epistemicum modelliert: "Wir haben angenommen (Axiomatic), dass Lieferant X termingerecht liefert. Status: Refuted. underminedBy: Verspaetungsdaten." Das Lesson Learned ist querybar, nicht in einem PDF begraben.

**Onboarding.** Ein neuer Mitarbeiter kann fragen: "Was gilt in unserem Wissensgraphen als Confirmed? Was ist noch Hypothetical?" Statt implizites Wissen wird der epistemische Zustand des Teams sichtbar.

---

## Normungs-Patterns

**Norm-Evolution.** DIN EN ISO 6892-1:2019 supersedes DIN EN ISO 6892-1:2009. Beide als Institutio. Die epistemische Haltung der Community: alte Version Refuted (nicht mehr gueltig), neue Confirmed. Querybar: "Welche Normen in meinem System sind deprecated?"

**Normkonformitaetsluecken.** Epistemicum: "Wir erfuellen Norma X. Status: Confirmed." Versus: "Wir erfuellen Norma Y. Status: Hypothetical, Konfidenz 0.3, supportedBy: keine." Der Unterschied zwischen "geprueft" und "behauptet" wird explizit.

---

## Knightsche / Tiefe Unsicherheit

**Known Unknowns.** `isQuantifiable = true` auf Possibile: "Bauteilversagen mit 2% Wahrscheinlichkeit." Normales Risiko, quantifizierbar.

**Unknown Unknowns.** `isQuantifiable = false` auf Possibile: "Klimawandel-Auswirkungen auf Lieferkette." Keine Verteilung zuweisbar. Das ist kein Bug, sondern eine bewusste Aussage: "Wir wissen nicht, was wir nicht wissen — aber wir wissen, *dass* wir es nicht wissen."

**Szenario-Planung.** Drei Possibile-Instanzen (Best Case, Base Case, Worst Case), jede mit eigenem Epistemicum und verschiedener Konfidenz. Querybar: "Welches Szenario hat die meiste Evidenz?"

---

## Agent-Optionalitaet

`heldBy` hat keine Mindestkardinalitaet in SHACL. Agent-freie Epistemicum-Instanzen
modellieren institutionalisierte epistemische Zustaende:

```turtle
ex:Datensatz_verifiziert  a min:Epistemicum ;
    min:about  ex:Datensatz_042 ;
    min:hasEpistemicStatus  min:ES_Confirmed .
    # Kein heldBy — institutioneller Zustand, kein persoenlicher Glaube.
```

Provenienz fuer agent-freie Instanzen laeuft ueber das bestehende `originatedBy`.

---

## Graph-Patterns (SPARQL)

```sparql
# Niedrigste Konfidenz im System — Schwachstellenanalyse
SELECT ?e ?gegenstand ?konfidenz WHERE {
    ?e a min:Epistemicum ; min:about ?gegenstand ; min:hasConfidence ?konfidenz .
} ORDER BY ASC(?konfidenz) LIMIT 10

# Dissens zwischen Agents
SELECT ?forma ?a1 ?a2 WHERE {
    ?e1 min:about ?forma ; min:heldBy ?a1 ; min:hasEpistemicStatus min:ES_Confirmed .
    ?e2 min:about ?forma ; min:heldBy ?a2 ; min:hasEpistemicStatus min:ES_Refuted .
    FILTER (?a1 != ?a2)
}

# Wissensfortschritt: Was wurde kuerzlich bestaetigt?
SELECT ?e ?forma WHERE {
    ?e min:about ?forma ; min:hasEpistemicStatus min:ES_Confirmed .
    ?e_alt min:about ?forma ; min:hasEpistemicStatus min:ES_Hypothetical .
    ?e min:supersedes ?e_alt .
}

# Schluesselexperimente: Welche Evidenz stuetzt die meisten Hypothesen?
SELECT ?evidenz (COUNT(?e) AS ?anzahl) WHERE {
    ?e min:supportedBy ?evidenz .
} GROUP BY ?evidenz ORDER BY DESC(?anzahl)

# Blinde Flecken: Nicht quantifizierbare Possibile
SELECT ?p WHERE {
    ?p a min:Possibile ; min:isQuantifiable false .
}

# Unbegruendete Annahmen: Epistemicum ohne Evidenz
SELECT ?e ?gegenstand WHERE {
    ?e a min:Epistemicum ; min:about ?gegenstand .
    FILTER NOT EXISTS { ?e min:supportedBy ?x }
    FILTER NOT EXISTS { ?e min:underminedBy ?x }
}
```

---

## Designentscheidungen

### Warum kein EM_Epistemic

EfficacyMode bildet die *Art der Bestimmung* ab — wie eine Forma-Subklasse
Nexus einschraenkt. Jedes EfficacyMode-Individual bildet 1:1 auf eine
Forma-Subklasse ab (lawful = Lex, structural = Structura, usw.).

Epistemicum *bestimmt* nicht — es *bewertet*. EM_Epistemic wuerde zwei
orthogonale Achsen vermischen. Die epistemische Dimension wird korrekt
durch `hasEpistemicStatus` und `hasConfidenceType` erfasst.

### Warum supersedes nicht-transitiv bleibt

`supersedes` wurde in v1.0.0 explizit als nicht-transitiv deklariert.
Die Begruendung gilt weiter: A supersedes B und B supersedes C impliziert
nicht, dass A direkt C abloest (Zwischenversionen koennen den Kontext aendern).

Fuer Historien-Queries genuegen SPARQL Property Paths:

```sparql
SELECT ?neueste ?aelteste WHERE {
    ?neueste min:supersedes+ ?aelteste .
}
```

---

## SHACL-Constraints

| Constraint | Schwere |
|---|---|
| `about` min 1 | Violation |
| `hasEpistemicStatus` genau 1 | Violation |
| `hasConfidence` in [0.0, 1.0] | Violation |
| `hasConfidence` vorhanden impliziert `hasConfidenceType` vorhanden | Violation |
| `supportedBy` / `underminedBy` muss auf Nexus zeigen | Violation |
| `heldBy` muss auf Agent zeigen (wenn vorhanden) | Violation |

---

## Was Epistemicum NICHT kann

**Keine Wahrheit.** Epistemicum sagt "Agent A glaubt X mit Konfidenz 0.9." Es sagt nicht "X ist wahr." Wahrheit ist kein MIN-Konzept — und das ist richtig so.

**Kein Reasoning ueber Konfidenz.** Ein Reasoner kann nicht inferieren: "Wenn Konfidenz(A) = 0.8 und Konfidenz(B) = 0.7, dann Konfidenz(A∧B) = 0.56." Bayesianische Propagation ist ein Process, kein Axiom.

**Keine Emotionen.** "Ich *fuehle*, dass das Bauteil versagt" ist kein Epistemicum. Epistemicum ist propositional: es bezieht sich auf Sachverhalte, nicht auf Gefuehle.

**Keine Selbstbezueglichkeit.** "Ich glaube, dass ich glaube" ist in OWL nicht sauber modellierbar. Epistemicum kann ueber alles im Graphen reden — ausser ueber sich selbst.

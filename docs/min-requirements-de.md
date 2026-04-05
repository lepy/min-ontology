# Was Ingenieurwissensgraphen ausdruecken muessen

**Kontext:** MIN v1.1.0 — Grundontologie fuer Ingenieure.

Ingenieurwissensgraphen stehen vor einer besonderen Herausforderung: sie
muessen nicht nur abbilden, was existiert und was geschieht, sondern auch,
was bestimmt, was geglaubt wird und was unsicher ist. MIN adressiert das
ueber sieben Achsen.

---

## Achse 1: Materialitaet — was existiert physisch?

| Frage | MIN-Konstrukt |
|---|---|
| Was ist physisch da? | Object |
| Was geschieht / wurde getan? | Process |
| Welche Daten liegen vor? | Data |
| Was entsteht nur zwischen Partnern? | Boundary |

Ein Zugversuch hat Probe (Object), Pruefvorgang (Process), Messdaten (Data),
und Kontaktreibung Probe/Einspannung (Boundary). Alle vier sind kausal
wirksam — sie bewirken etwas in der Welt.

**Zentrale Relationen:**
- `hasInput` / `hasOutput` — was geht rein, was kommt raus
- `hasComponent` — mereologische Zusammensetzung
- `generates` / `generatedBy` — Prozess erzeugt Daten
- `describes` / `describedBy` — Daten beschreiben Nexus
- `bounds` / `hasBoundary` — Grenze zwischen Partnern

---

## Achse 2: Formalitaet — was bestimmt, ohne zu wirken?

| Frage | MIN-Konstrukt |
|---|---|
| Welches Naturgesetz gilt? | Lex |
| Welches formale Modell beschreibt es? | Structura |
| Was koennte passieren? | Possibile |
| Welche Anforderung muss erfuellt sein? | Norma |
| Was wird kollektiv anerkannt (Sorte, Norm, Typ)? | Institutio |
| Was wird fuer wahr gehalten? | Epistemicum |

Ein Werkstoffingenieur braucht alle sechs: Hooke'sches Gesetz (Lex),
Johnson-Cook-Modell (Structura), Ermuedungsriss-Szenario (Possibile),
Rm >= 270 MPa (Norma), DC04-Stahlsorte (Institutio), und "Hooke gilt
hier bis 200 MPa" als bewertete Hypothese (Epistemicum).

**Zentrales Prinzip:** Forma bewirkt nichts — aber ohne Forma waere jede
Wirkung anders. Forma ist die Grammatik, Nexus sind die Saetze.

**Zentrale Relationen:**
- `governs` — Lex bestimmt Process
- `formalizes` — Structura bestimmt Nexus
- `evaluates` — Norma bewertet Nexus
- `concerns` / `alternativeTo` — Possibile bezieht sich auf Nexus
- `typifies` — Institutio bestimmt, als was ein Nexus zaehlt
- `comprises` — Institutio buendelt atomare Forma-Instanzen

---

## Achse 3: Agency — wer handelt?

| Frage | MIN-Konstrukt |
|---|---|
| Wer fuehrt aus? | Agent ∩ Object (Mensch, Maschine) |
| Welche Software entscheidet? | Agent ∩ Data (ML-Modell) |
| Welche Organisation verantwortet? | Agent ∩ Institutio |

Nicht nur Menschen. Eine CNC-Maschine, ein ML-Modell, ein Normungsgremium —
alle handeln selektiv. Agent ist eine Querkategorie unter Entity, keine
Unterkategorie von Nexus. Co-Typisierung ist Pflicht.

**Zentrale Relationen:**
- `performs` / `controls` — Agent fuehrt Prozess durch
- `actsOn` — Agent wirkt auf Object (abgeleitet ueber Property Chain)
- `owns` — Eigentumsverhaeltnis / Verantwortung
- `constitutes` / `recognizes` — Agent gruendet / anerkennt Institution

---

## Achse 4: Kausalitaet — wie haengt es zusammen?

### Innerhalb der Welt (Nexus ↔ Nexus)

- Was geht rein, was kommt raus? → `hasInput` / `hasOutput`
- Wer fuehrt den Prozess durch? → `performs` / `controls`
- Woraus besteht es? → `hasComponent`

### Zwischen Welt und Bestimmung (Nexus ↔ Forma)

Drei generische Brueckenrelationen bilden den Forma-Lebenszyklus:

| Relation | Richtung | Semantik |
|---|---|---|
| `originates` | Nexus → Forma | Nexus bringt NEUES Formales hervor |
| `realizes` | Nexus → Forma | Nexus macht BESTEHENDES Formales wirklich |
| `constrains` | Forma → Nexus | Forma schraenkt ein, was Nexus sein oder tun kann |

Dazu die Kodierungsbruecke:

| Relation | Richtung | Semantik |
|---|---|---|
| `encodes` | Data → Forma | Data traegt formalen Inhalt (DIN-Dokument kodiert Norma) |

**Zentrale Unterscheidung:**
- `realizes` veraendert die Welt (ontologisch).
- `confirms` veraendert das Wissen (epistemisch).

---

## Achse 5: Epistemik — was wissen wir, und wie sicher?

| Frage | Wie MIN es ausdrueckt |
|---|---|
| Wer glaubt es? | `heldBy` Agent (oder agent-frei) |
| Worueber? | `about` Entity |
| Wie sicher? | `hasConfidence` [0..1] + `hasConfidenceType` |
| Welcher Status? | `hasEpistemicStatus` (5 Werte) |
| Worauf gestuetzt? | `supportedBy` / `underminedBy` Nexus |
| Was galt vorher? | `supersedes` (Forma → Forma) |

Das ist der Kern, den Ingenieurwissensgraphen *vor* MIN v1.1.0 typischerweise
nicht konnten: den Unterschied zwischen "42% Recyclatanteil" und "42%
Recyclatanteil, statistisch bestaetigt mit Konfidenz 0.92 gestuetzt durch
XRF-Messdaten" formalisieren.

### Zwei komplementaere Muster

| Muster | Traeger | Semantik | Seit |
|---|---|---|---|
| Poppersch | Process | Process bestaetigt/widerlegt Forma | v1.0.0 |
| Evidenzbasiert | Epistemicum | Haltung gestuetzt/geschwaecht durch Nexus | v1.1.0 |

Beide werden gebraucht. Das Poppersche Muster ist kompakt fuer einfache
Aussagen ("der Zugversuch bestaetigt das Hooke'sche Gesetz"). Das
evidenzbasierte Muster wird gebraucht, wenn sich der epistemische Zustand
ueber die Zeit aendert, Konfidenz typisiert werden muss, oder mehrere
Agenten widerspruechliche Haltungen vertreten.

---

## Achse 6: Unsicherheit — was wissen wir nicht?

| Frage | MIN-Konstrukt |
|---|---|
| Quantifizierbares Risiko? | Possibile + `isQuantifiable` = true |
| Tiefe / Knightsche Unsicherheit? | Possibile + `isQuantifiable` = false |
| Fehlende Evidenz? | Epistemicum ohne `supportedBy` |
| Dissens? | Zwei Epistemicum, selbes `about`, verschiedene Agents, verschiedener Status |

**Known Unknowns:** "Bauteilversagen mit 2% Wahrscheinlichkeit." Normales
Risiko, eine Verteilung ist zuweisbar.

**Unknown Unknowns:** "Klimawandel-Auswirkungen auf Lieferkette." Keine
Verteilung zuweisbar. Das ist kein Bug, sondern eine bewusste Aussage.

---

## Achse 7: Provenienz — woher stammt die Information?

| Frage | MIN-Konstrukt |
|---|---|
| Wer hat die Daten erzeugt? | Data + `generatedBy` Process |
| Wer hat den formalen Inhalt kodiert? | Data + `encodes` Forma |
| Wer hat den formalen Bestimmer hervorgebracht? | Forma + `originatedBy` Nexus |
| Welche Evidenz stuetzt den Glauben? | Epistemicum + `supportedBy` Nexus |

Provenienz in MIN laeuft ueber drei komplementaere Mechanismen:
- **Data-Provenienz:** `generatedBy` verfolgt, welcher Prozess die Daten erzeugt hat.
- **Forma-Provenienz:** `originatedBy` verfolgt, welcher Nexus den formalen Bestimmer hervorgebracht hat.
- **Epistemische Provenienz:** `supportedBy` / `underminedBy` verfolgt, welche Evidenz einen Glauben stuetzt oder schwaecht.

---

## Achse 8: Temporalitaet — wann geschieht es?

| Frage | MIN-Konstrukt |
|---|---|
| Wann wurde es erfasst? | `hasTimestamp` (Entity → xsd:dateTime) |
| Wann begann der Prozess? | `startedAt` (Process → xsd:dateTime) |
| Wann endete der Prozess? | `endedAt` (Process → xsd:dateTime) |
| Welche zeitliche Abfolge? | Prozessketten ueber `hasInput` / `hasOutput` |
| Was hat was abgeloest? | `supersedes` (Forma → Forma) |

MIN bettet Temporalitaet implizit ein, statt ein separates Zeitmodell
zu verwenden. Zeitstempel haengen direkt an Entitaeten und Prozessen.
Zeitliche Ordnung ergibt sich aus Prozessketten: wenn Prozess B den
Output von Prozess A nutzt, dann geht A B voraus. Epistemische
Sukzession nutzt `supersedes` — wenn ein neues Epistemicum ein altes
ersetzt, wird die zeitliche Dimension strukturell erfasst, nicht ueber
explizite Zeitintervalle.

**Was Alignment bereitstellt:**
- OWL-Time (`alignment/min-time.ttl`): `min:Process rdfs:subClassOf time:ProperInterval` —
  Prozesse koennen von OWL-Time-Reasonern als Zeitintervalle behandelt werden.
- PROV-O (`alignment/min-prov.ttl`): `min:startedAt rdfs:subPropertyOf prov:startedAtTime` —
  Zeitstempel werden fuer PROV-O-Werkzeuge sichtbar.

**Was in die Domainschicht gehoert:**
- Zeitreihendaten (Sensorwerte im Millisekundentakt)
- Lebenszyklus-Phasenmodelle (Entwurf → Fertigung → Nutzung → Lebensende)
- Kalender- und Terminierungsbeschraenkungen
- Allen-Intervallrelationen (before, during, overlaps)

---

## Zusammenfassung: acht Achsen

```
1. Materialitaet     Was existiert physisch?                → Nexus
2. Formalitaet        Was bestimmt, ohne zu wirken?          → Forma
3. Agency             Wer handelt?                           → Agent
4. Kausalitaet        Wie haengt es zusammen?                → Relationen
5. Epistemik          Was wissen wir, wie sicher?            → Epistemicum
6. Unsicherheit       Was wissen wir nicht?                  → Possibile + isQuantifiable
7. Provenienz         Woher stammt die Information?          → Data + originatedBy + supportedBy
8. Temporalitaet      Wann geschieht es?                     → hasTimestamp + startedAt/endedAt
```

## Was MIN bewusst NICHT abdeckt

| Thema | Warum nicht | Wo stattdessen |
|---|---|---|
| Wahrheit | "X ist wahr" ist kein MIN-Konzept. Epistemicum sagt, was *geglaubt* wird, nicht was *ist*. | — |
| Bayesianische Propagation | Konfidenz-Propagation ist ein Process, kein Axiom. | Domainschicht |
| Zeitreihen | Zeitliche Aufloesung gehoert in die Domainschicht. | sdata-measurements |
| Physikalische Einheiten | Einheitensysteme sind orthogonal zur ontologischen Struktur. | QUDT-Alignment |
| Emotionen | "Ich fuehle, dass das Bauteil versagt" ist nicht propositional. | — |
| Selbstbezueglichkeit | "Ich glaube, dass ich glaube" ist in OWL nicht sauber modellierbar. | — |

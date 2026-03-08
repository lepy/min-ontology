# MIN Meta — Selbstbeschreibendes Dokumentationsvokabular

**Ontologie-IRI:** `https://w3id.org/min/meta`  
**Version:** 1.0.0  
**Version-IRI:** `https://w3id.org/min/meta/1.0.0`  
**Import:** MIN v1.0.0 (`https://w3id.org/min/1.0.0`)  
**Autor:** Dr. Ingolf Lepenies  
**Datum:** 2026-03-05  
**Lizenz:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Zweck

MIN Meta definiert die Annotation Properties, mit denen beliebige Ontologie-Entitäten — Klassen, Properties, Individuen — strukturiert dokumentiert werden, einschließlich MIN selbst. Das Vokabular umfasst **11 Properties** in **7 irreduziblen Dimensionen**.

Vorbild ist die Information Artifact Ontology (IAO) im OBO-Ökosystem, jedoch MIN-nativ, schlanker und selbstbeschreibend.

## Entwurfsprinzipien

Das Metavokabular folgt vier Prinzipien:

**Irreduzibilität** — Jede Property deckt eine Dimension ab, die keine andere abdecken kann. Nachgewiesen durch paarweise `distinguishedFrom`-Annotationen.

**Selbstbeschreibung** — Das Vokabular dokumentiert sich mit sich selbst. Jede der 11 Properties ist mit den eigenen Annotations annotiert.

**Minimalität** — Keine Property, deren Fehlen tolerierbar wäre. Keine Property, die durch Kombination anderer ersetzbar wäre.

**Universalität** — Anwendbar auf Klassen, Properties und Individuen gleichermaßen.

---

## Dimensionenübersicht

| Nr. | Dimension | Leitfrage | Properties |
|-----|-----------|-----------|------------|
| I | Intension | Was ist es? | `min:definition`, `min:criterion` |
| II | Extension | Wie sieht es aus? | `min:usageExample` |
| III | Grenze | Was ist es nicht? | `min:counterExample`, `min:distinguishedFrom` |
| IV | Herkunft | Woher kommt es? | `min:philosophicalBasis`*, `min:normativeSource` |
| V | Teleologie | Warum existiert es? | `min:rationale` |
| VI | Lebenszyklus | In welchem Zustand? | `min:definedInVersion`, `min:status`, `min:replacedBy` |
| VII | Axiom-Transparenz | Warum diese Formalia? | `min:axiomRationale` |

\* `min:philosophicalBasis` ist bereits im MIN-Hauptmodul definiert und wird im Metavokabular nur selbstbeschrieben.

---

## I. Intension — Was ist die Entität?

### `min:definition`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Definition (de) · definition (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Eine natürlichsprachliche Satz-Definition, die eine Ontologie-Entität so beschreibt, dass ein sachkundiger Leser sie ohne weitere Quellen eindeutig identifizieren kann.

**Kriterium:** Könnte ein sachkundiger Leser allein anhand dieses Satzes entscheiden, ob ein gegebenes Ding zur Klasse gehört oder nicht?

**Rationale:** Ohne eine explizite Definition bleibt die Semantik einer Klasse implizit im Label und in der Axiomatik verborgen. Das genügt für Maschinen, nicht für Menschen.

**Abgrenzung:** Nicht zu verwechseln mit `rdfs:comment`, der informell, unstrukturiert und redundant sein darf. `min:definition` ist normativ und nicht-zirkulär.

**Beispiele:**
- `min:Object min:definition "Ein Ding, das kausal wirksam ist — es kann Wirkungen empfangen oder ausüben."@de .`
- `min:Typus min:definition "Das Bündel von Bestimmungen, das eine Klasse von Nexus-Instanzen konstituiert. Typus bestimmt, ALS WAS ein Nexus zählt."@de .`

---

### `min:criterion`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Existenzkriterium (de) · criterion (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Eine operationalisierbare Ja/Nein-Frage, deren Bejahung eine Entität als Instanz der annotierten Klasse qualifiziert.

**Kriterium:** Kann die Frage prinzipiell mit Ja oder Nein beantwortet werden, und trennt sie Instanzen zuverlässig von Nicht-Instanzen?

**Rationale:** Eine Definition sagt, was etwas *ist*. Ein Kriterium sagt, wie man *entscheidet*. Beide sind irreduzibel: Eine gute Definition kann ein schlechtes Entscheidungsverfahren haben und umgekehrt.

**Abgrenzung:** `min:definition` beschreibt, was die Klasse ist. `min:criterion` beschreibt, wie man Zugehörigkeit prüft.

**Gegenbeispiel:** „Ist das Objekt wichtig?" — zu vage, nicht operationalisierbar.

**Beispiele:**
- `min:Process min:criterion "Verbraucht oder transformiert die Entität Inputs zu Outputs über die Zeit?"@de .`
- `min:Typus min:criterion "Kann man fragen: Was für ein X ist das? — und liefert die Antwort eine Wesensbestimmung?"@de .`

---

## II. Extension — Wie sieht die Entität konkret aus?

### `min:usageExample`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Verwendungsbeispiel (de) · usage example (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Ein konkretes Beispiel — als natürlichsprachliche Beschreibung oder als Turtle-Fragment — das zeigt, wie die annotierte Entität in der Praxis instanziiert oder verwendet wird.

**Kriterium:** Zeigt das Beispiel eine korrekte, nicht-triviale Verwendung der Entität in einem realistischen Kontext?

**Rationale:** Definitionen und Kriterien sind abstrakt. Beispiele verankern das Verständnis in konkreter Praxis und reduzieren Mehrdeutigkeit, die Definitionen allein nicht auflösen können.

**Abgrenzung:** `min:counterExample` zeigt, was die Entität *nicht* ist. `min:usageExample` zeigt, was sie *ist*.

**Gegenbeispiel:** „z.B. ein Auto" — zu unspezifisch, kein Verwendungskontext sichtbar.

**Beispiel:**
- `min:Agent min:usageExample "ex:Operator_01 a min:Agent ; rdfs:label \"Prüfingenieur Müller\"@de ."@de .`

---

## III. Grenze — Was ist die Entität nicht?

### `min:counterExample`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Gegenbeispiel (de) · counterexample (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Ein konkretes Beispiel einer Entität, die der annotierten Klasse nahezuliegen scheint, aber nach deren Kriterium nicht dazugehört — zusammen mit der Begründung, warum nicht.

**Kriterium:** Würde ein Nicht-Experte die genannte Entität plausibel der Klasse zuordnen, obwohl sie nicht dazugehört?

**Rationale:** Definitionen und Kriterien allein lassen Grenzfälle offen. Gegenbeispiele machen die Grenze der Klasse sichtbar, besonders dort, wo Verwechslungsgefahr besteht.

**Abgrenzung:** `min:distinguishedFrom` grenzt *Klassen* voneinander ab. `min:counterExample` nennt ein konkretes *Ding*, das nicht zur Klasse gehört.

**Beispiel:**
- `min:Agent min:counterExample "Eine CNC-Maschine ist kein Agent, da sie keine Handlungskompetenz besitzt, sondern Anweisungen ausführt. → min:Object."@de .`

---

### `min:distinguishedFrom`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Abgrenzung (de) · distinguished from (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Eine explizite Abgrenzung der annotierten Klasse gegenüber einer verwandten Klasse, die ein anderer Modellierer verwechseln oder zusammenlegen könnte.

**Kriterium:** Gibt es eine dokumentierte Verwechslungsgefahr zwischen den beiden Klassen, und macht die Abgrenzung den Unterschied operationalisierbar?

**Rationale:** Ontologien wachsen durch mehrere Beitragende. Ohne explizite Abgrenzungen driften Klassengrenzen auseinander, weil jeder Modellierer eine eigene Intuition hat.

**Abgrenzung:** `min:counterExample` nennt ein konkretes Ding. `min:distinguishedFrom` nennt eine *Klasse* und begründet die Trennung.

**Beispiele:**
- `min:Data min:distinguishedFrom "min:Object — Data ist kausal inert (kann kopiert, gelöscht werden ohne physische Wirkung). Object ist kausal wirksam."@de .`
- `min:Typus min:distinguishedFrom "min:Norma — Norma BEWERTET (Rm SOLL ≥ 270 MPa). Typus KONSTITUIERT (DC04 IST das, was C ≤ 0.08% und Rm 270–350 MPa hat)."@de .`

---

## IV. Herkunft — Woher kommt die Entität?

### `min:philosophicalBasis`

> **Hinweis:** Diese Property ist bereits im MIN-Hauptmodul (`https://w3id.org/min/`) definiert. Im Metavokabular wird sie nur selbstbeschrieben, nicht neu deklariert.

---

### `min:normativeSource`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Normative Quelle (de) · normative source (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Ein Verweis auf einen publizierten Standard, eine Spezifikation oder eine anerkannte Fachquelle, deren inhaltliche Definition die Semantik der annotierten Entität begründet oder einschränkt.

**Kriterium:** Ist die genannte Quelle ein publiziertes, zitierfähiges Dokument, das die Definition der Entität inhaltlich stützt?

**Rationale:** `min:philosophicalBasis` verweist auf die begriffliche Tradition (Aristoteles, Whitehead). Wenn aber eine Klasse aus DIN EN ISO 6892-1 abgeleitet ist, braucht man einen getrennten Verweis auf die *fachliche* Quelle. Philosophische Tradition ≠ normative Referenz.

**Abgrenzungen:**
- `min:philosophicalBasis` verweist auf philosophische Tradition und Begriffsgeschichte. `min:normativeSource` verweist auf technische oder wissenschaftliche Autoritätsquellen.
- `dcterms:source` ist ein generischer Dublin-Core-Verweis ohne die Einschränkung auf normative, definitionsstützende Quellen.

**Beispiele:**
- `sdata:TensileTest min:normativeSource "DIN EN ISO 6892-1:2019, Abschnitt 3.1"@de .`
- `ex:DC04_typus min:normativeSource "EN 10130:2006, Tabelle 3 — Chemische Zusammensetzung und mechanische Eigenschaften"@de .`

---

## V. Teleologie — Warum existiert die Entität?

### `min:rationale`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Entwurfsbegründung (de) · design rationale (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Eine natürlichsprachliche Begründung, die erklärt, welches konkrete Modellierungsproblem die annotierte Entität löst und warum keine bestehende Entität dieses Problem bereits abdeckt.

**Kriterium:** Benennt der Text ein konkretes Modellierungsproblem und erklärt, warum keine bestehende Entität es löst?

**Rationale:** `min:definition` sagt *was*, `min:philosophicalBasis` sagt *woher der Begriff stammt* — aber keines beantwortet: „Warum habt ihr das nicht einfach unter X subsumiert?" Ohne Rationale geht die Entwurfsentscheidung verloren, sobald der Autor nicht mehr verfügbar ist.

**Abgrenzungen:**
- `min:definition` beschreibt, was die Entität *ist*. `min:rationale` beschreibt, warum sie *sein muss*.
- `min:philosophicalBasis` verortet den Begriff in einer Denktradition. `min:rationale` verortet ihn im Kontext der Ontologie-Architektur.

**Gegenbeispiel:** „Weil es praktisch ist" — keine Begründung, kein Modellierungsproblem benannt.

**Beispiele:**
- `min:EnvironmentAgent min:rationale "Natürliche Prozesse (Korrosion, Alterung) haben keinen intentionalen Agenten. Ohne EnvironmentAgent müsste man Agent-Instanzen für physikalische Gesetze anlegen, was die Semantik von Agent verwässert."@de .`
- `min:Typus min:rationale "MIN kann einzelne Bestimmungen und Typzuweisungen in einem konsistenten Modell ausdrücken."@de .`

---

## VI. Lebenszyklus — In welchem Zustand ist die Entität?

### `min:definedInVersion`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Definiert in Version (de) · defined in version (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Die Versionsnummer (SemVer) der Ontologie, in der die annotierte Entität erstmals eingeführt wurde.

**Kriterium:** Ist der Wert eine gültige SemVer-Versionsnummer, und entspricht sie dem Release, in dem die Entität erstmals erschien?

**Rationale:** In einer sich entwickelnden Ontologie müssen Nutzer nachvollziehen können, ab welcher Version eine Entität verfügbar ist — insbesondere für Abwärtskompatibilität und Migration.

**Abgrenzungen:**
- `min:status` beschreibt den aktuellen Reifegrad. `min:definedInVersion` beschreibt den historischen Einführungszeitpunkt.
- `owl:versionInfo` versioniert die Ontologie als Ganzes. `min:definedInVersion` versioniert einzelne Entitäten.

---

### `min:status`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Status (de) · status (en) |
| **Range** | `xsd:string` |
| **Erlaubte Werte** | `"experimental"` · `"stable"` · `"deprecated"` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Der aktuelle Reifegrad der annotierten Entität im Lebenszyklus der Ontologie. Genau einer von drei Werten: `experimental` (kann sich ändern), `stable` (festgeschrieben), `deprecated` (nicht mehr verwenden, siehe `min:replacedBy`).

**Kriterium:** Ist der Wert exakt einer der drei erlaubten Strings?

**Rationale:** `min:definedInVersion` sagt, *wann* eine Entität eingeführt wurde, aber nicht, ob sie noch verwendet werden soll. Ohne expliziten Status weiß ein Nutzer nicht, ob er eine Klasse sicher einsetzen kann oder ob sie bald entfällt.

**Abgrenzungen:**
- `min:definedInVersion` markiert einen historischen Zeitpunkt. `min:status` beschreibt den *aktuellen* Zustand.
- `min:replacedBy` nennt den Nachfolger bei Deprecation. `min:status` markiert nur den Zustand selbst.

**Gegenbeispiel:** `"beta"` — kein erlaubter Wert. Die Dreiteilung experimental/stable/deprecated ist erschöpfend.

---

### `min:replacedBy`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Ersetzt durch (de) · replaced by (en) |
| **Range** | `rdfs:Resource` (URI) |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Ein Verweis auf die Ontologie-Entität, die die annotierte (deprecated) Entität funktional ersetzt. Der Wert ist eine URI, kein String.

**Kriterium:** Ist die annotierte Entität deprecated, und bietet die referenzierte Entität tatsächlich einen funktionalen Ersatz?

**Rationale:** Deprecation ohne Migrationspfad ist nutzlos. Nutzer müssen wissen, *wohin* sie migrieren sollen, nicht nur, dass sie migrieren müssen.

**Abgrenzung:** `min:status` markiert nur den Zustand `deprecated`. `min:replacedBy` nennt den konkreten Nachfolger.

**Gegenbeispiel:** `min:replacedBy` auf einer Entität mit `min:status "stable"` — semantisch widersprüchlich.

**Beispiel (hypothetisch):**
```turtle
min:PhysicalObject min:status "deprecated" ;
    min:replacedBy min:Object .
```

---

## VII. Axiom-Transparenz — Warum diese formalen Einschränkungen?

### `min:axiomRationale`

| | |
|---|---|
| **Typ** | `owl:AnnotationProperty` |
| **Label** | Axiom-Begründung (de) · axiom rationale (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Seit** | 1.0.0 |

**Definition:** Eine natürlichsprachliche Begründung, die erklärt, warum eine bestimmte OWL-Restriktion (Domain, Range, Kardinalität, Disjunktheit) so gewählt wurde und welche Modellierungsalternative bewusst verworfen wurde.

**Kriterium:** Benennt der Text die spezifische Restriktion, begründet die Wahl und benennt mindestens eine verworfene Alternative?

**Rationale:** OWL-Axiome sind maschinenlesbar, aber ihre Entwurfsentscheidungen sind es nicht. Die jüngste Korrektur der Process-Axiome in MIN (Öffnung für Data-Inputs neben Object-Inputs) zeigt: Ohne dokumentierte Begründung muss jeder Nachfolger die Designentscheidung neu rekonstruieren.

**Abgrenzung:** `min:rationale` begründet, warum die *Entität* existiert. `min:axiomRationale` begründet, warum eine *formale Einschränkung* auf der Entität so gewählt wurde.

**Gegenbeispiel:** „Domain ist Object, weil das sinnvoll ist." — keine Begründung, keine verworfene Alternative.

**Beispiele:**
- `min:hasInput min:axiomRationale "Range ist min:Entity (nicht nur min:Object), weil Prozesse sowohl physische Objekte als auch Daten konsumieren können."@de .`
- `min:typifies min:axiomRationale "typifies ist subPropertyOf constrains, weil Typifizierung eine spezielle Form der Bestimmung ist. Verworfene Alternative: eigenständige Top-Level-Brückenrelation."@de .`

---

## Demonstration — `min:Typus` mit vollständiger Meta-Dokumentation

Die folgende Klasse zeigt, wie alle 11 Properties zusammenwirken, um eine Klasse vollständig zu dokumentieren.

### Intension

**Definition:** Das Bündel von Bestimmungen, das eine Klasse von Nexus-Instanzen konstituiert. Typus bestimmt, ALS WAS ein Nexus zählt — nicht, was er hat (Property), nicht, was er soll (Norma), sondern, was er IST.

**Kriterium:** Kann man fragen: „Was für ein X ist das?" — und liefert die Antwort eine Wesensbestimmung (ein Bündel von Bestimmungen, das die Sorte/Art konstituiert)?

### Extension

```turtle
ex:DC04_typus a min:Typus ;
    rdfs:label "DC04"@de ;
    min:hasIdentifier "DC04" ;
    min:typifies ex:blech_042 .
```

### Grenze

**Gegenbeispiel:** Ein SKOS-Konzept „DC04" in einem Thesaurus. Es klassifiziert terminologisch, aber es bestimmt nicht die Wesensform — es hat keine Verbindung zu Structura, Lex, Norma. → `skos:Concept`, nicht `min:Typus`.

**Abgrenzungen:**

| Gegenüber | Unterschied |
|-----------|-------------|
| `min:Norma` | Norma BEWERTET (Soll). Typus KONSTITUIERT (Wesen). |
| `min:Structura` | Structura ist formal-rein (mathematische Struktur). Typus ist komposit — er BÜNDELT Structura, Norma, Lex und Properties. |
| `min:Institutio` | Institutio braucht laufende kollektive Anerkennung. Typus nicht — DC04 bleibt DC04, auch wenn das Normungsgremium aufgelöst wird. |
| `min:Lex` | Lex ist universell und ausnahmslos. Typus ist kontingent — DC04 hätte andere Grenzwerte haben können. |

### Herkunft

**Normative Quellen:** Aristoteles: Metaphysik, Buch Z (Eidos als Wesensform). Quine: Natural Kinds (1969). Putnam: The Meaning of „Meaning" (1975). Weber: Objektive Möglichkeit und adäquate Verursachung (1906, Idealtyp).

### Teleologie

MIN kann einzelne Bestimmungen aussprechen (Norma: Rm ≥ 270 MPa; Structura: bcc-Gitter) und explizite Typzuweisungen wie „Das ist ein DC04." modellieren.

### Lebenszyklus

Definiert in Version **1.0.0**, Status **stable**.

### Axiom-Transparenz

Typus ist disjunkt mit Lex, Structura, Possibile, Norma, Institutio. Typus ist komposit (bündelt andere Forma-Kategorien), während jede andere Forma-Kategorie atomar ist. Verworfene Alternative: Typus als Subklasse von Norma — aber Norma bewertet, Typus konstituiert.

`min:typifies` ist subPropertyOf `min:constrains`. Typifizierung ist eine spezielle Form der Bestimmung. Verworfene Alternative: eigenständige Top-Level-Brückenrelation. Aber Typifizierung IST Einschränkung (auf eine Art), also gehört sie unter `constrains`.

---

## Vollständigkeitsnachweis

Das Metavokabular beweist drei Eigenschaften durch Selbstbeschreibung:

**Ausdrucksstärke** — Das Vokabular kann alles beschreiben, was es beschreiben soll, einschließlich sich selbst.

**Irreduzibilität** — Keine Property ist durch Kombination der anderen ersetzbar (nachweisbar durch die paarweisen `distinguishedFrom`-Annotationen).

**Vollständigkeit** — Jede Dokumentationsfrage, die ein sachkundiger Leser stellen könnte, wird durch eine der 11 Properties beantwortet:

| Frage | Property |
|-------|----------|
| Was ist X? | `min:definition` |
| Wie entscheide ich? | `min:criterion` |
| Wie sieht das konkret aus? | `min:usageExample` |
| Was gehört nicht dazu? | `min:counterExample` |
| Wie unterscheidet sich X von Y? | `min:distinguishedFrom` |
| Auf welcher Philosophie basiert X? | `min:philosophicalBasis` |
| Aus welchem Standard kommt X? | `min:normativeSource` |
| Warum gibt es X in MIN? | `min:rationale` |
| Seit wann gibt es X? | `min:definedInVersion` |
| Kann ich X noch verwenden? | `min:status` |
| Was soll ich stattdessen nehmen? | `min:replacedBy` |
| Warum hat X diese Restriktion? | `min:axiomRationale` |

---

## Prefix-Übersicht

| Prefix | Namespace |
|--------|-----------|
| `min:` | `https://w3id.org/min/` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` |
| `dcterms:` | `http://purl.org/dc/terms/` |

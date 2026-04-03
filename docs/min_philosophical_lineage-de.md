# MIN — Die philosophische Ahnenreihe

> **Acht Denker, eine Ontologie.**
>
> MIN erfindet nicht aus dem Nichts. Es erbt, transformiert und
> rekombiniert Ideen aus einer philosophischen Tradition, die
> 2.400 Jahre umspannt. Dieses Dokument zeichnet nach, was von
> wem entlehnt wurde — und wo es in der Architektur auftaucht.

---

## Die Architektur im Überblick

```
                     Entity
                    ╱  │  ╲
               Nexus   │   Forma
              ╱│╲  ╲   │  ╱│╲ ╲ ╲
       Object │ Data   │ Lex │ Norma
        Process   │  Agent │ Institutio
             Boundary    Structura
                          Possibile
```

Zwei Zweige (Nexus, Forma), eine Querkategorie (Agent), verbunden
durch Brückenrelationen. Jedes Element dieser Architektur hat einen
philosophischen Ahnen.

---

## 1 — Aristoteles (384–322 v. Chr.)

**Entlehnt:** Hyle/Morphe, Ousia, Kinesis, Aitia, Eidos, Apodeixis.

Aristoteles ist die tiefste Schicht. MINs gesamte Zweig-Architektur
ist eine Transformation seiner Unterscheidung von Stoff und Form.

**Hyle und Morphe → Polarität.** Aristoteles' Hyle (Stoff) und Morphe
(Form) werden zu MINs Schema-Polarität: `materialProperty` und
`informationalProperty`. Jede Nexus-Instanz hat eine materiale und eine
informationale Seite. Der Topf hat Masse (Hyle) und einen Entwurf
(Morphe). Die Messdatei hat Bytes (Hyle) und Semantik (Morphe). MIN
erzwingt keine Wahl — es behandelt Polarität als Heuristik, nicht als
Partition. Properties KÖNNEN als materiale oder informationale
Subproperties deklariert werden, MÜSSEN aber nicht.

**Ousia → Entity.** Aristoteles' *to on* — „das Seiende" — wird zu
MINs `Entity`: die absolute Wurzel, unter der alles fällt, was im
Wissensgraph explizit modelliert wird. Entity ist kein metaphysischer
Anspruch darüber, was im Universum existiert; es ist ein pragmatischer
Anker für das, was einen Knoten bekommt.

**Kinesis → Process.** Aristoteles' Begriff von Bewegung und
Veränderung — das Werden des Seins — bildet sich direkt auf `Process`
ab. Process ist Transformation: er nimmt Nexus-Instanzen als Input
und erzeugt Nexus-Instanzen als Output. Die zwei Modi der
Transformation (transformativ vs. konservativ) spiegeln Aristoteles'
Unterscheidung zwischen substanzieller und akzidenteller Veränderung.

**Aitia → Kausales Denken.** Aristoteles' vier Ursachen (materiale,
formale, effiziente, finale) werden nicht eins zu eins übernommen,
aber MINs Kernfrage — „Bewirkt es etwas?" — stammt aus dem
aristotelischen Bekenntnis zur Kausalerklärung als Grundlage des
Verstehens.

**Eidos → Institutio.** Aristoteles' Eidos — die Wesensform, die ein
Ding zu dem macht, was es ist — taucht in MINs `Institutio` wieder
auf. Wenn MIN fragt „Was für ein Stahl ist das?" und antwortet „DC04",
dann ist diese Klassifikation ein institutioneller Akt, der eine
Wesensbestimmung zuweist. Institutio übernimmt die Eidos-Rolle: das
Bündel von Bestimmungen, das das Wesen konstituiert. Aber anders als
bei Aristoteles macht MIN dieses Bündel explizit konventionell — es
existiert, weil eine Fachgemeinschaft es anerkennt.

**Apodeixis → entails.** Aristoteles' Syllogistik — die Logik der
notwendigen Folge — untermauert `min:entails`. Wenn A B impliziert
und B C impliziert, dann impliziert A C. Die Transitivität von
entails ist aristotelische Logik, kodiert als OWL-Property.

**Sein vs. Sollen → Nexus / Forma.** Die tiefe Trennung zwischen
„was ist" (Nexus) und „was sein soll" (Forma, besonders Norma)
spiegelt Aristoteles' Trennung von theoretischem und praktischem
Wissen — allerdings führt MIN diese über Humes Guillotine (aus Sein
folgt kein Sollen; → daher sind Lex und Norma getrennte Klassen).

---

## 2 — Spinoza (1632–1677)

**Entlehnt:** Eine Substanz, zwei Attribute.

Spinoza argumentierte, es gebe nur eine Substanz, aber sie könne unter
zwei Attributen verstanden werden: Ausdehnung (das Physische) und
Denken (das Mentale). Keines ist auf das andere reduzierbar; beide sind
Aspekte derselben Wirklichkeit.

**Eine Substanz, zwei Attribute → Nexus-Polarität.** MINs Polarität
spiegelt genau das. Eine Nexus-Instanz — etwa ein Stahlblech — ist
ein Ding, aber es zeigt zwei Gesichter: seine materiale Seite (Masse,
Härte, Geometrie) und seine informationale Seite (Identifier,
Klassifikation, Provenienz). Die beiden Annotations-Superproperties
`materialProperty` und `informationalProperty` sind Spinozas zwei
Attribute, transponiert auf Schema-Ebene.

Die zentrale spinozistische Einsicht, die MIN bewahrt: Die zwei Pole
sind nicht zwei Dinge, sondern zwei Zugänge zu demselben Ding. Eine
Messdatei hat Bytes auf einer Festplatte (Ausdehnung) und semantischen
Inhalt (Denken). Sie spaltet sich nicht in eine physische und eine
informationale Hälfte. Sie ist eine Entität mit zwei Aspekten.

---

## 3 — Whitehead (1861–1947)

**Entlehnt:** Actual Entity, Eternal Object, Process, Creativity.

Whiteheads Prozessphilosophie ist wohl MINs nächster Vorfahr.

**Actual Entity → Nexus.** Whiteheads aktuale Entitäten — die
letztlich wirklichen Dinge, aus denen die Welt besteht — bilden sich
auf MINs Nexus-Zweig ab. Alles, was Wirkungen verursacht, alles, was
an kausalen Ketten teilnimmt, ist Nexus. Wie Whiteheads aktuale
Entitäten sind Nexus-Instanzen konkret, temporal und relational.

**Eternal Object → Forma.** Whiteheads Eternal Objects — reine
Möglichkeiten, die selbst nicht aktual sind, aber bestimmen, was
aktuale Entitäten sein können — bilden sich auf MINs Forma-Zweig ab.
Ein Naturgesetz (Lex) bestimmt, wie Prozesse ablaufen. Eine
mathematische Struktur (Structura) formt die Geometrie des Möglichen.
Eine Möglichkeit (Possibile) beschreibt, was geschehen könnte, aber
nicht geschieht. Nichts davon ist kausal wirksam an sich; sie sind
die Grammatik, nach der Nexus wirkt.

Whiteheads Begriff *Ingression* — die Art, wie ein Eternal Object in
eine aktuale Entität eingeht — wird zu MINs `min:realizes`. Ein
Zugversuch (Process) realisiert ISO 6892-1 (Norma). Ein Stahlblech
(Object) realisiert die bcc-Kristallstruktur (Structura). Realisierung
ist Ingression.

**Process → Process.** Whiteheads berühmteste These — „the becoming
of being" — ist MINs Klasse `Process`. Die Wirklichkeit besteht nicht
aus statischen Substanzen, sondern aus Ereignissen, Transformationen,
Werdeprozessen. MIN nimmt das ernst: Process ist nicht sekundär
gegenüber Object. Process ist eine vollwertige Nexus-Kategorie mit
eigenem Kausalitätsmodus (dispositional).

**Creativity → originates.** Whiteheads Creativity — das letzte
Prinzip, durch das aktuale Entitäten Neues hervorbringen — bildet sich
auf MINs `min:originates` ab. Wenn ein Forschungsprozess eine neue
Regularität erzeugt, wenn ein Normungsausschuss eine neue Norm
erschafft, wenn Daten ein neues Muster offenbaren: Nexus bringt NEUES
Formales hervor. Originates ist Whiteheads Creativity als
Brückenrelation.

---

## 4 — Latour (1947–2022)

**Entlehnt:** Aktant, Médiation technique, Symmetrieprinzip.

Latours Akteur-Netzwerk-Theorie (ANT) liefert MINs Konzept von Agency.

**Aktant → Agent.** Latours Aktant — alles, was einen Unterschied
macht, unabhängig davon, ob es menschlich, maschinell oder textuell
ist — bildet sich auf MINs `Agent` ab. Ein Koch ist Agent. Eine
CNC-Maschine ist Agent. Ein ML-Modell ist Agent. Korrosion, wenn sie
selektiv transformiert, ist Agent.

Der entscheidende Latoursche Zug, den MIN bewahrt: *Keine
Intentionalität gefordert*. Ein Thermostat hat Agency, aber keine
Intention. Eine Organisation handelt, hat aber kein Bewusstsein.
Agency meint selektive, zurechenbare kausale Wirksamkeit — nicht
Geist.

**Médiation technique → Boundary.** Latours Begriff der technischen
Mediation — bei der der Mediator ein eigenständiger Aktant ist, kein
neutraler Kanal — informiert MINs `Boundary`. Der Wärmeübergang
zwischen Wasser und Ei ist keine passive Verbindung; er ist ein
eigenständiges Phänomen mit eigener kausaler Kraft. Wie Latours
Mediatoren ist Boundary irreduzibel relational und kausal autonom.

**Symmetrieprinzip → Agent als Querkategorie.** Latour bestand darauf,
menschliche und nichtmenschliche Aktanten symmetrisch zu behandeln.
MIN folgt dem: Agent ist keine Seinskategorie (wie Object oder Lex),
sondern eine Handlungskategorie. Agent durchquert die Zweiggrenze. Ein
Mensch ist Agent ∩ Object. Eine Organisation ist Agent ∩ Institutio.
Ein ML-Modell ist Agent ∩ Data. Die Co-Typisierungspflicht stellt
sicher, dass jeder Agent einen Seinsmodus hat — aber Agency selbst
ist orthogonal zum Sein.

---

## 5 — Searle (1932–2022)

**Entlehnt:** Institutional Facts, Constitutive Rules, kollektive
Anerkennung.

Searle liefert das theoretische Fundament für MINs `Institutio`.

**Institutional Facts → Institutio.** Searle unterschied Brute Facts
(der Stein wiegt 5 kg) von institutionellen Tatsachen (dieses Stück
Papier ist Geld). Institutionelle Tatsachen existieren nur, weil
Agenten sie kollektiv anerkennen. MIN bildet das direkt ab:
`Institutio` ist alles, was durch kollektive Anerkennung existiert
und aufhört zu existieren, wenn niemand es mehr anerkennt.

**„X counts as Y in context C" → typifies.** Searles Formel für
konstitutive Regeln wird zu MINs `min:typifies`. Ein Stahlblech (X)
zählt als DC04 (Y) im Kontext der Metallurgie (C). Ein gekochtes Ei
(X) zählt als weichgekocht (Y) im Kontext der Küche (C). Typifizierung
ist ein institutioneller Akt — sie weist eine Wesensbestimmung zu, die
konventionell, nicht naturgegeben ist.

**Konstitutive Regeln → comprises.** Searles konstitutive Regeln —
die Regeln, die die Möglichkeit einer Aktivität erst schaffen (im
Gegensatz zu regulativen Regeln, die vorhandene Aktivitäten lenken) —
informieren MINs `min:comprises`. DC04 comprises Norma(C ≤ 0,08 %),
Structura(bcc-Ferrit), Lex(Diffusionsverhalten). Die Bündelung
atomarer Forma-Instanzen zu einer Wesensbestimmung ist ein
konstitutiver Akt. Ohne sie existiert DC04 nicht — nur einzelne
Anforderungen.

**Der Vernichtungstest.** Searles Analyse treibt auch eine
architektonische Schlüsselentscheidung in MIN v1.0: die Anhebung
von Agent von Nexus auf Entity. Eine Organisation handelt (Agent)
UND wird anerkannt (Institutio). Der Vernichtungstest —
Handelsregistereintrag löschen und sowohl die Agency als auch die
institutionelle Existenz verschwinden — zeigt, dass beide dieselbe
Vernichtungsbedingung haben. Was dieselbe Vernichtungsbedingung hat,
ist dasselbe Ding. Also muss Agent über der Zweiggrenze stehen, und
Co-Typisierung (Agent ∩ Institutio) muss in einem einzigen Knoten
möglich sein.

---

## 6 — Kripke (1940–2022) / Lewis (1941–2001)

**Entlehnt:** Possible Worlds, Modalsemantik.

Kripke und Lewis liefern das theoretische Rückgrat für MINs
`Possibile`.

**Possible Worlds → Possibile.** Kripkes Semantik möglicher Welten —
die Idee, dass modale Aussagen („es könnte der Fall sein, dass …") als
Aussagen über alternative Sachverhalte verstanden werden können —
bildet sich auf MINs `Possibile` ab. Ein Versagensszenario für ein
Bauteil ist ein Possibile: es könnte eintreten, ist aber nicht
eingetreten. Eine Designalternative ist ein Possibile: sie hätte
gewählt werden können, wurde aber nicht gewählt.

MIN verpflichtet sich nicht auf Lewis' modalen Realismus (die These,
dass alle möglichen Welten gleich real sind). Possibile ist eine
Forma-Kategorie: es bestimmt, was sein könnte, ohne zu behaupten, dass
alternative Welten buchstäblich existieren. Wenn ein Possibile
realisiert wird — wenn das Versagen tatsächlich eintritt — wird es
zum Process (Nexus). Der Übergang von Possibile zu Process ist
`min:realizes`.

**Kontrafaktisches Denken.** Das Kripke/Lewis-Gerüst untermauert auch
MINs `min:concerns` (ein Possibile betrifft einen aktualen Nexus) und
`min:alternativeTo` (ein Possibile ist Alternative zu einem aktualen
Nexus). Beide Relationen drücken kontrafaktisches Denken aus: Was wäre
anders, wenn die Dinge anders wären?

---

## 7 — Woodward (*1951)

**Entlehnt:** Interventionistische Kausalität.

Woodwards interventionistische Kausalitätstheorie liefert MINs
Existenzkriterium für Nexus.

**Interventionistische Kausalität → „Bewirkt es etwas?"** Woodward
definiert kausale Relevanz wie folgt: X ist kausal relevant für Y,
wenn eine Intervention auf X Y verändern würde. MIN übernimmt das als
Existenzkriterium für den Nexus-Zweig: Wenn eine Intervention auf die
Entität etwas anderes verändern würde, ist sie Nexus.

Genau das macht MINs Nexus-Zweig breiter als eine materialistische
Ontologie. Ein Schatten ist Nexus — interveniere auf den Schatten
(bewege das Hindernis) und nachgelagerte Wirkungen ändern sich. Ein
Vakuum ist Nexus — interveniere auf das Vakuum (brich es) und Prozesse
ändern sich. Ein elektromagnetisches Feld ist Nexus. Nichts davon
besteht aus Materie im gewöhnlichen Sinn, aber alles besteht den
interventionistischen Test.

**Drei Kausalitätsmodi.** Woodwards Rahmenwerk motiviert auch MINs
Differenzierung der Kausalitätsmodi innerhalb von Nexus. Nicht alle
Nexus-Kategorien wirken auf dieselbe Weise:

- **Dispositional** — Object und Process wirken oder könnten wirken,
  auch ohne Agent. Ein Stahlblech hat Masse, ob gerade jemand misst
  oder nicht.
- **Mediated** — Data wirkt NUR über einen interpretierenden Agent.
  Ein Festplattensektor mit zufälligen Bits ist physisch identisch
  mit einem, der den Produktpass enthält. Die kausale Differenz liegt
  im Agent, der die Bytes interpretiert.
- **Relational** — Boundary wirkt NUR zwischen Partnern. Entferne
  einen Partner, und die Boundary verschwindet.

Diese drei Modi machen Datas Sonderrolle als Scharnier zwischen Nexus
und Forma explizit: Data ist aktual (hat Bytes), aber kausal abhängig
von Agents (mediated), was es näher an Forma rückt als die anderen
Nexus-Kategorien.

---

## 8 — Popper (1902–1994)

**Entlehnt:** Falsifikationismus, Bewährung.

Popper liefert die epistemologische Schicht, die MIN v1.0.0 auf seine
ontologische Architektur aufsetzt.

**Falsifikation → refutes.** Poppers Zentralthese — dass
wissenschaftliches Wissen durch die Widerlegung von Hypothesen wächst —
bildet sich auf MINs `min:refutes` ab. Ein Process (Experiment,
Analyse, First-Principles-Denken) widerlegt ein Possibile. Die Range
ist spezifisch Possibile, nicht Forma generisch, weil nur Possibilia
den epistemischen Status „könnte der Fall sein" haben, der durch
Widerlegung aufgehoben wird.

**Bewährung → confirms.** Popper unterschied Verifikation (unmöglich)
von Bewährung (eine Hypothese hält Falsifikationsversuchen stand).
MIN bildet das auf `min:confirms` ab. Ein Process bestätigt, dass eine
Forma als Fundament tragfähig ist — aber das ist Bewährung, nicht
Beweis. Eine bestätigte Forma kann durch spätere Prozesse widerlegt
werden.

**Falsifikationismus als Architektur.** Das confirms/refutes-Paar
vervollständigt den Forma-Lebenszyklus in MIN:

```
originates  — Forma entsteht            (Whitehead: Creativity)
constrains  — Forma wirkt               (Aristoteles: Morphe formt Hyle)
realizes    — Forma wird wirklich       (Whitehead: Ingression)
confirms    — Forma hält der Prüfung stand  (Popper: Bewährung)
refutes     — Forma hält nicht stand    (Popper: Falsifikation)
supersedes  — Forma ersetzt Forma       (Kuhn: Paradigmenwechsel)
```

MIN ist selbst ein Produkt dieses Zyklus. Die Entscheidung,
Typifizierung über Institutio zu modellieren, war ein
First-Principles-Prozess, der Searles Konstitutivitätsprinzip
bestätigte: Klassifikation ist ein institutioneller Akt. MIN
modelliert seine eigene epistemologische Evolution mit seinen
eigenen Relationen.

---

## Die Synthese

Kein einzelner Philosoph liefert ganz MIN. Die Synthese ist der
Beitrag:

| Denker | Was MIN entlehnt | Wo es auftaucht |
|---|---|---|
| Aristoteles | Stoff/Form, Substanz, Bewegung, Ursache, Wesen | Polarität, Entity, Process, kausales Denken, Institutio (Eidos-Rolle), entails |
| Spinoza | Eine Substanz, zwei Attribute | Polarität als dualer Aspekt, nicht duale Substanz |
| Whitehead | Actual Entity, Eternal Object, Process, Creativity | Nexus, Forma, Process, originates, realizes |
| Latour | Aktant, Mediation, Symmetrie | Agent (keine Intentionalität gefordert), Boundary, Agent als Querkategorie |
| Searle | Institutional Facts, „X counts as Y in C" | Institutio, typifies, comprises, Agent ∩ Institutio |
| Kripke/Lewis | Possible Worlds | Possibile, concerns, alternativeTo |
| Woodward | Interventionistische Kausalität | Nexus-Existenzkriterium, drei Kausalitätsmodi |
| Popper | Falsifikation, Bewährung | refutes, confirms, epistemischer Lebenszyklus |

Was sie zusammenhält, ist die Frage, die MIN stellt: *„Bewirkt es
etwas?"* — und ihr Komplement: *„Bestimmt es, wie Wirkungen
funktionieren?"* Die erste Frage schneidet Nexus heraus (Woodward,
Whitehead, Latour). Die zweite schneidet Forma heraus (Whitehead,
Aristoteles, Searle, Kripke). Agent durchquert beides (Latour, Searle).
Und die epistemischen Relationen verfolgen, was wir über die gesamte
Struktur wissen (Popper, Aristoteles).

**Keine Metaphysik. Werkzeug. Gebaut auf 2.400 Jahren Nachdenken
darüber, was es gibt, was es bewirkt und wie wir es wissen.**

# Das ontologische Frühstücksei

> **Wie modelliert man einen Alltagsprozess mit einer Grundontologie?**
>
> Diese Anleitung zeigt am Beispiel des Eierkochens, wie die MIN-Ontologie 
> funktioniert. Jeder Schritt führt eine MIN-Kategorie ein und
> erklärt, warum genau diese Kategorie die richtige ist.

---

## Überblick

MIN hat zwei Zweige und eine Querkategorie unter `Entity`:

- **Nexus** — das, was etwas bewirkt (Object, Process, Data, Boundary)
- **Forma** — das Regelwerk, nach dem Nexus wirkt (Lex, Structura, Possibile, Norma, Institutio)
- **Agent** — das, was handelt. Orthogonale Querkategorie, die die Zweiggrenze durchquert.

Beim Eierkochen brauchen wir alle drei. Das Ei, der Topf, das Wasser —
das sind Nexus-Instanzen. Die Kochzeitvorgabe, das Naturgesetz der
Wärmeübertragung, die Garstufe „weichgekocht" — das sind Forma-Instanzen.
Der Koch und der Herd im Betrieb — das sind Agents mit Co-Typisierung.

![min_hierarchy.svg](min_hierarchy.svg)

---

## Schritt 1 — Die Dinge auf dem Tisch: Object

> *„Bewirkt es etwas als physisches Ding?"* → **Object.**

Alles, was auf dem Herd steht und physisch da ist: Topf, Wasser, Ei, Herd.
Object ist der material-dominante Nexus. Identitätskriterium: materiale
Kontinuität — das Ei bleibt dasselbe Ei, auch wenn es sich verändert.

```turtle
@prefix egg: <https://example.org/egg#> .
@prefix min: <https://w3id.org/min#> .

egg:Topf a min:Object ;
    min:hasIdentifier "OBJ-TOPF-001" ;
    min:hasName "Kochtopf"@de ;
    egg:material "Edelstahl" ;
    egg:volumen_ml "2000"^^xsd:float .

egg:Wasser a min:Object ;
    min:hasIdentifier "OBJ-WASSER-001" ;
    min:hasName "Kochwasser"@de ;
    egg:menge_ml "1500"^^xsd:float .

egg:Ei_roh a min:Object ;
    min:hasIdentifier "OBJ-EI-ROH-001" ;
    min:hasName "Rohes Ei"@de ;
    egg:gewicht_g "58"^^xsd:float ;
    egg:starttemperatur_C "7"^^xsd:float .
```

**Warum Object und nicht Agent?** Der Topf handelt nicht. Das Wasser
handelt nicht. Das Ei handelt nicht. Sie sind physisch da und werden
durch Processes transformiert — aber sie steuern nichts.

---

## Schritt 2 — Der Koch und der Herd: Agent

> *„Handelt es selektiv und zurechenbar?"* → **Agent.**

Der Koch ist Agent — er entscheidet, wann er das Ei einlegt, wie lange
er kocht, ob er abschreckt. Der Herd im Betrieb ist ebenfalls Agent —
er reguliert die Energiezufuhr selektiv.

Agent ist eine orthogonale Querkategorie unter Entity (v1.0). Agent ist
keine Seinskategorie, sondern eine Handlungskategorie. Sie durchquert
die Zweiggrenze Nexus/Forma. Co-Typisierung ist Pflicht: jeder Agent
muss mindestens eine Seinskategorie tragen.

```turtle
egg:Koch a min:Agent , min:Object ;
    min:hasIdentifier "AGT-KOCH-001" ;
    min:hasName "Koch"@de ;
    min:performs egg:Eierkochen ;
    min:controls egg:Eierkochen .

egg:Herd_aktiv a min:Agent , min:Object ;
    min:hasIdentifier "AGT-HERD-001" ;
    min:hasName "Herd (aktiv)"@de ;
    min:performs egg:Erhitzen .
```

**Warum `a min:Agent, min:Object`?** Weil der Koch physisch da ist
(Object) UND handelt (Agent). MIN erzwingt Co-Typisierung — Agent
allein reicht nie. Die Co-Klasse bestimmt den Seinsmodus:
Agent ∩ Object → Nexus-Zweig. Agent ∩ Institutio → Forma-Zweig.

**Warum ist die Gravitation kein Agent?** Sie wirkt universal, nicht
selektiv. Universalität disqualifiziert für Agency — qualifiziert aber
für Lex (→ Schritt 7).

**Warum ist Agent keine Nexus-Kategorie mehr?** Weil Agent die
Zweiggrenze durchquert. Eine Organisation handelt (Agent) UND wird
anerkannt (Institutio). Der Vernichtungstest zeigt: dieselbe
Vernichtungsbedingung — also dasselbe Ding. Agent muss über der
Zweiggrenze stehen: `rdfs:subClassOf min:Entity`.

---

## Schritt 3 — Was geschieht: Process

> *„Transformiert es Inputs zu Outputs über die Zeit?"* → **Process.**

Das Eierkochen ist ein Process mit Subprocesses. Process ist der
ausgewogene Nexus — beide Pole (material, informational) sind gleich
gewichtig.

```turtle
egg:Eierkochen a min:Process ;
    min:hasIdentifier "PRC-KOCHEN-001" ;
    min:hasName "Eierkochen"@de ;
    min:hasInput egg:Ei_roh ;
    min:hasInput egg:Wasser ;
    min:hasOutput egg:Ei_gekocht ;
    min:performedBy egg:Koch ;
    min:hasComponent egg:Erhitzen ;
    min:hasComponent egg:Garziehen ;
    min:hasComponent egg:Abschrecken .

egg:Erhitzen a min:Process ;
    min:hasIdentifier "PRC-ERHITZ-001" ;
    min:hasName "Wasser erhitzen"@de ;
    min:hasInput egg:Wasser ;
    min:hasOutput egg:Wasser ;
    min:performedBy egg:Herd_aktiv .

egg:Garziehen a min:Process ;
    min:hasIdentifier "PRC-GAR-001" ;
    min:hasName "Garziehen"@de ;
    min:hasInput egg:Ei_roh ;
    min:hasOutput egg:Ei_gekocht .

egg:Abschrecken a min:Process ;
    min:hasIdentifier "PRC-ABSCHR-001" ;
    min:hasName "Abschrecken"@de ;
    min:hasInput egg:Ei_gekocht ;
    min:hasOutput egg:Ei_gekocht .
```

**Zwei Modi der Transformation:**

- **Transformativ** (`hasInput`/`hasOutput`): Ei_roh → Garziehen → Ei_gekocht.
  Zwei verschiedene Entitäten, zwei IDs. Das rohe Ei ist nicht mehr da.
- **Konservativ** (`undergoes`): Erhitzen erwärmt das Wasser, aber es
  bleibt dasselbe Wasser.

Die Unterscheidung liegt in der Relation, nicht in der Kategorie.

**Warum ist `hasInput` auf Nexus, nicht auf Object?** Weil MIN kausal
denkt, nicht materialistisch. Ein Simulationsprozess konsumiert Data
als Input. Deshalb: `min:hasInput` → `rdfs:range min:Nexus`.

---

## Schritt 4 — Was dazwischen entsteht: Boundary

> *„Entferne einen Partner — existiert das Phänomen noch? Nein?"* → **Boundary.**

Der Wärmeübergang zwischen Wasser und Eischale gehört weder dem Wasser
noch dem Ei. Er entsteht nur *zwischen* beiden. Entferne das Ei aus dem
Wasser — der Wärmeübergangskoeffizient verschwindet.

```turtle
egg:Waermeuebergang_Wasser_Ei a min:Boundary ;
    min:hasIdentifier "BND-WE-001" ;
    min:hasName "Wärmeübergang Wasser–Ei"@de ;
    min:bounds egg:Wasser ;
    min:bounds egg:Ei_roh ;
    egg:waermeuebergangskoeffizient_W_m2K "3000"^^xsd:float .

egg:Waermeuebergang_Topf_Wasser a min:Boundary ;
    min:hasIdentifier "BND-TW-001" ;
    min:hasName "Wärmeübergang Topf–Wasser"@de ;
    min:bounds egg:Topf ;
    min:bounds egg:Wasser .
```

**Warum nicht einfach eine Property am Object?**
`egg:Wasser egg:waermeuebergangskoeffizient "3000"` wäre physikalisch
falsch. Der Koeffizient ist keine Eigenschaft des Wassers — er hängt
von der Strömung, der Schalenoberfläche und der Temperaturdifferenz ab.
Er ist eine Systemeigenschaft. Genau das ist Boundary.

**Warum nicht Object?** Die Oberfläche des Eies ist Object
(entferne alle Partner — die Oberfläche bleibt). Aber der
Wärmeübergang zwischen Wasser und Ei ist Boundary (entferne
das Ei — der Übergang verschwindet).

---

## Schritt 5 — Was beschreibt: Data

> *„Existiert es als Informationsträger — Bytes, Struktur, Semantik?"* → **Data.**

Das Rezept auf dem Küchentisch und die gemessene Kochzeit sind Data.
Sie haben eine physische Existenz (Papier, Bytes) und kodieren Forma
(Kochzeitvorgaben, Garstufen).

```turtle
egg:Messdaten_Kochzeit a min:Data ;
    min:hasIdentifier "DAT-ZEIT-001" ;
    min:hasName "Kochzeit-Messung"@de ;
    min:describes egg:Garziehen ;
    min:generatedBy egg:Eierkochen ;
    min:encodes egg:Norma_weich ;
    egg:kochzeit_min "5.5"^^xsd:float .

egg:Rezept a min:Data ;
    min:hasIdentifier "DAT-REZ-001" ;
    min:hasName "Kochrezept"@de ;
    min:describes egg:Eierkochen ;
    min:encodes egg:Norma_weich ;
    min:encodes egg:Norma_hart ;
    min:encodes egg:Garstufe_weichgekocht .
```

**Die Schlüsselrelation: `min:encodes`.**
Das Rezept (Data) kodiert die Kochzeitvorgabe (Norma). Wenn man das
Rezept wegwirft, bleibt die Vorgabe — jeder Koch kennt sie auswendig.
Data IST nicht Forma. Data KODIERT Forma.

---

## Schritt 6 — Ab hier: Forma

Alles bisher war Nexus — das Aktuale, Kausal-Wirksame. Jetzt kommt
Forma: das Regelwerk, nach dem Nexus wirkt. Forma bewirkt nichts.
Aber ohne Forma wäre jede Wirkung anders.

```
Nexus = die Sätze     →  Topf, Wasser, Ei, Koch, Kochen
Forma = die Grammatik  →  Wärmegesetz, Kochzeiten, Garstufen
```

---

## Schritt 7 — Was gilt: Lex

> *„Gilt es universell, ausnahmslos?"* → **Lex.**

Die Wärmeübertragung und die Proteindenaturierung sind Naturgesetze.
Sie bestimmen, WIE das Garziehen abläuft. Kein Koch kann sie ändern.

```turtle
egg:Waermeuebertragung a min:Lex ;
    min:hasIdentifier "LEX-WAERME-001" ;
    min:hasName "Wärmeübertragungsgesetz"@de ;
    min:governs egg:Garziehen ;
    min:constrains egg:Waermeuebergang_Wasser_Ei .

egg:Proteindenaturierung a min:Lex ;
    min:hasIdentifier "LEX-DENAT-001" ;
    min:hasName "Proteindenaturierung"@de ;
    min:governs egg:Garziehen .
```

**`min:governs`** ist die spezialisierte Brückenrelation: Lex → Process.
Das Naturgesetz bestimmt, WIE der Process abläuft.

**Warum ist die Proteindenaturierung kein Agent?** Sie wirkt universal —
jedes Protein denaturiert bei Wärme. Universalität disqualifiziert für
Agency (selektiv, zurechenbar). Aber sie qualifiziert für Lex.

---

## Schritt 8 — Was formt: Structura

> *„Ist es eine rein mathematische Struktur?"* → **Structura.**

Die Wärmeleitungsgleichung in Kugelkoordinaten formalisiert, wie sich
die Temperatur im Ei über die Zeit verteilt. Sie existiert nicht
physisch — aber sie bestimmt die Geometrie des Möglichen.

```turtle
egg:Waermeleitungsgleichung a min:Structura ;
    min:hasIdentifier "STRUCT-WL-001" ;
    min:hasName "Wärmeleitungsgleichung (Kugel)"@de ;
    min:formalizes egg:Garziehen .
```

**Warum nicht Data?** Die FEM-Implementierung der Gleichung wäre Data
(hat Bytes, Speicherort, Version). Die Gleichung *selbst* — ∂T/∂t = α·∇²T —
ist Structura. Die Implementierung *kodiert* die Struktur: `Data encodes Structura`.

---

## Schritt 9 — Was gelten soll: Norma

> *„Definiert es einen Soll-Wert, gegen den bewertet werden kann?"* → **Norma.**

Die Kochzeitvorgaben sind Normen. Sie bewirken nichts — aber sie
definieren den Unterschied zwischen „weich" und „zu hart".

Norma ist ATOMAR: jede einzelne Anforderung ist eine eigenständige
Norma-Instanz. Die Bündelung mehrerer Norma zu einer Wesensbestimmung
ist Institutio, nicht Norma (→ Schritt 10).

```turtle
egg:Norma_weich a min:Norma ;
    min:hasIdentifier "NORMA-WEICH-001" ;
    min:hasName "Kochzeit weichgekocht"@de ;
    min:evaluates egg:Ei_gekocht ;
    egg:kochzeit_min_min "4"^^xsd:float ;
    egg:kochzeit_max_min "5"^^xsd:float .

egg:Norma_wachsweich a min:Norma ;
    min:hasIdentifier "NORMA-WACHS-001" ;
    min:hasName "Kochzeit wachsweich"@de ;
    min:evaluates egg:Ei_gekocht ;
    egg:kochzeit_min_min "6"^^xsd:float ;
    egg:kochzeit_max_min "7"^^xsd:float .

egg:Norma_hart a min:Norma ;
    min:hasIdentifier "NORMA-HART-001" ;
    min:hasName "Kochzeit hartgekocht"@de ;
    min:evaluates egg:Ei_gekocht ;
    egg:kochzeit_min_min "9"^^xsd:float ;
    egg:kochzeit_max_min "11"^^xsd:float .
```

**`min:evaluates`**: Norma → Nexus. Die Kochzeitvorgabe *bewertet*
das gekochte Ei: bestanden oder nicht bestanden.

**Warum ist Norma nicht Lex?** Lex kann nicht verletzt werden —
die Proteindenaturierung passiert immer. Norma kann verletzt werden —
man kann 15 Minuten kochen und bekommt trotzdem ein Ei, nur kein gutes.
Genau das macht Norma zur Norma.

---

## Schritt 10 — Was etwas zu dem macht, was es ist: Institutio

> *„Was für ein Ei ist das?"* → **Institutio.**

Die Garstufe „weichgekocht" ist eine Institutio — eine konventionelle
Bündelung von Bestimmungen, die festlegt, als was das Ei zählt.
Institutio bündelt Norma, Lex, Structura und Properties zu einer
Wesensbestimmung. Diese Bündelung existiert, weil eine Fachgemeinschaft
(hier: Köche) sie anerkennt.

Searle: *„X counts as Y in context C."* Das gekochte Ei (Object) zählt
als weichgekocht (Institutio) im Kontext der Küche.

```turtle
egg:Garstufe_weichgekocht a min:Institutio ;
    min:hasIdentifier "INST-WEICH-001" ;
    min:hasName "weichgekocht"@de ;
    min:typifies egg:Ei_gekocht ;
    min:comprises egg:Norma_weich ;
    min:recognizedBy egg:Koch .

egg:Garstufe_wachsweich a min:Institutio ;
    min:hasIdentifier "INST-WACHS-001" ;
    min:hasName "wachsweich"@de ;
    min:typifies egg:Ei_gekocht ;
    min:comprises egg:Norma_wachsweich ;
    min:recognizedBy egg:Koch .

egg:Garstufe_hartgekocht a min:Institutio ;
    min:hasIdentifier "INST-HART-001" ;
    min:hasName "hartgekocht"@de ;
    min:typifies egg:Ei_gekocht ;
    min:comprises egg:Norma_hart ;
    min:recognizedBy egg:Koch .

egg:Huehner_M a min:Institutio ;
    min:hasIdentifier "INST-EI-M-001" ;
    min:hasName "Hühnerei Größe M"@de ;
    min:typifies egg:Ei_roh ;
    min:recognizedBy egg:Koch .
```

**`min:typifies`**: Institutio → Nexus. Die Institutio *bestimmt*,
als was der Nexus zählt. Nicht beschreiben (→ Data), nicht bewerten
(→ Norma), sondern BESTIMMEN.

**`min:comprises`**: Institutio → Forma. Die Bündelungsrelation.
Die Garstufe „weichgekocht" *umfasst* die Norma „Kochzeit 4–5 min".
Die gebündelten Forma-Instanzen existieren unabhängig. Die Bündelung
ist der institutionelle Akt.

**Warum ist „weichgekocht" nicht Norma?** Norma ist ATOMAR und bewertet:
„Die Kochzeit SOLL 4–5 Minuten betragen." Institutio BÜNDELT und
konstituiert: „Ein weiches Ei IST das, was festes Eiweiß und flüssiges
Eigelb hat — und die Koch-Community erkennt das an." Norma fragt:
Bestanden? Institutio fragt: Was ist es?

**Polyhierarchie:** Ein Ei kann mehrere Institutio-Typen haben — es ist
zugleich `Huehner_M` (Eisorte) und `Garstufe_weichgekocht` (Garstufe).

**Warum Institutio und nicht eine eigene Kategorie „Typus"?** Die
Bündelung von Forma-Instanzen zu einer Wesensbestimmung ist ein
institutioneller Akt — sie existiert, weil eine Fachgemeinschaft sie
anerkennt. „Weichgekocht" bleibt „weichgekocht", solange IRGENDWER
die Konvention anerkennt. Wenn NIEMAND sie mehr kennt, zerfällt sie
in ihre atomaren Norma-Bestandteile. Genau das ist Searles Kriterium
für Institutio. Klassifikation IST ein institutioneller Akt.

---

## Schritt 11 — Was schiefgehen könnte: Possibile

> *„Könnte es geschehen, ist aber nicht geschehen?"* → **Possibile.**

Das Wasser könnte überkochen. Es könnte ein grüner Ring am Eigelb
entstehen. Modale Aussagen über Nicht-Aktuales.

```turtle
egg:Ueberkochen a min:Possibile ;
    min:hasIdentifier "POSS-UEBER-001" ;
    min:hasName "Überkochen"@de ;
    min:concerns egg:Erhitzen .

egg:Gruener_Ring a min:Possibile ;
    min:hasIdentifier "POSS-GRUEN-001" ;
    min:hasName "Grüner Ring am Eigelb"@de ;
    min:concerns egg:Ei_gekocht .
```

**Warum nicht Process?** Ein Process GESCHIEHT. Ein Possibile geschieht
NICHT — es KÖNNTE geschehen. Wenn das Wasser tatsächlich überkocht,
wird es zum Process (`min:realizes`).

---

## Schritt 12 — Soziale Konstrukte: Institutio (zweite Funktion)

> *„Existiert es nur, weil Agenten es anerkennen?"* → **Institutio.**

In Schritt 10 haben wir Institutio als konventionelle Bündelung
kennengelernt (Garstufen). Institutio hat eine zweite Funktion:
soziale Konstrukte im engeren Sinne.

Die EU-Vermarktungsnorm für Eier (Größenklassen S/M/L/XL) existiert,
weil EU-Mitgliedstaaten sie anerkennen. Ohne Anerkennung — keine Norm.

```turtle
egg:EU_Vermarktungsnorm a min:Institutio ;
    min:hasIdentifier "INST-EU-EI-001" ;
    min:hasName "EU-Vermarktungsnormen für Eier"@de ;
    min:comprises egg:Norma_groesse_M ;
    min:constitutedBy egg:EU_Kommission ;
    min:recognizedBy egg:Koch .
```

**Institutio hat also zwei Funktionen:**

1. **Konventionelle Bündelungen** — Garstufen, Stahlsorten, Prüfverfahren.
   Die Bündelung atomarer Forma zu einer Wesensbestimmung (Schritt 10).
2. **Soziale Konstrukte** — Geld, Patente, Vermarktungsnormen, Organisationen.
   Institutionelle Tatsachen im Sinne Searles.

Beide existieren durch kollektive Anerkennung. Beide zerfallen,
wenn niemand sie mehr anerkennt.

---

## Schritt 13 — Domain Properties: Polarität

MIN unterscheidet auf Schema-Ebene zwischen materialen und
informationalen Eigenschaften. Das ist die Polarität — eine Heuristik,
kein Axiom.

```turtle
egg:material a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:materialProperty ;
    rdfs:domain min:Object ;
    rdfs:range xsd:string .

egg:gewicht_g a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:materialProperty ;
    rdfs:domain min:Object ;
    rdfs:range xsd:float .

egg:kochzeit_min a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:informationalProperty ;
    rdfs:domain min:Data ;
    rdfs:range xsd:float .

egg:waermeuebergangskoeffizient_W_m2K a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:materialProperty ;
    rdfs:domain min:Boundary ;
    rdfs:range xsd:float .
```

**Materialität** deklariert man bei Properties, die das Physische,
Kausale erfassen (Masse, Volumen, Temperatur). **Informationalität**
bei Properties, die das Strukturelle, Semantische erfassen (Kochzeit
als Messwert, Dateiformat). Die Deklaration liegt in der Property,
nicht in der Instanz. Die Instanzen bleiben flach.

Polarität ist HEURISTIK: Domänen-Properties KÖNNEN als Subproperties
deklariert werden, MÜSSEN aber nicht. Temporale, modale und
zustandsbezogene Properties (hasTimestamp, hasStatus) passen in keine
der beiden Kategorien und brauchen kein Polaritäts-Label.

---

## Zusammenfassung

```
Nexus (bewirkt)                    Forma (bestimmt)
─────────────────                  ─────────────────
Object:   Topf, Wasser, Ei         Lex:        Wärmeübertragung,
Process:  Kochen, Garziehen                    Proteindenaturierung
Data:     Messung, Rezept          Structura:  Wärmeleitungsgleichung
Boundary: Wärmeübergang ×2         Norma:      Kochzeiten (w/m/h)
                                   Possibile:  Überkochen, Grüner Ring
Querkategorie (handelt)            Institutio: Garstufen (weich/wachs/hart),
─────────────────                              Hühnerei Größe M,
Agent:    Koch, Herd (aktiv)                   EU-Vermarktungsnorm
          (jeweils Agent ∩ Object)
```

**Brückenrelationen verbinden die Zweige:**

| Relation | Beispiel |
|---|---|
| `realizes` | Garziehen realisiert die Wärmeleitungsgleichung |
| `governs` | Proteindenaturierung governs Garziehen |
| `evaluates` | Norma_weich evaluates Ei_gekocht |
| `encodes` | Rezept encodes Norma_weich |
| `typifies` | Garstufe_weichgekocht typifies Ei_gekocht |
| `comprises` | Garstufe_weichgekocht comprises Norma_weich |
| `formalizes` | Wärmeleitungsgleichung formalizes Garziehen |
| `concerns` | Grüner_Ring concerns Ei_gekocht |
| `constrains` | Wärmeübertragung constrains Wärmeübergang |

**Keine Metaphysik. Einfach ein leckeres Frühstücksei.**

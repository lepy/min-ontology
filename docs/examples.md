# Per-Class Examples

MIN provides example patterns for all instantiable classes in v3.7.1. Each `.ttl` file below is a
self-contained graph that can be used as a modeling reference.

All listed example files pass instance-level SHACL validation (`shapes/min-instance.shacl.ttl`).

## Overview

| Class | File | Scenario |
| --- | --- | --- |
| `min:Object` | `examples/object.ttl` | Steel beam in bridge construction |
| `min:Process` | `examples/process.ttl` | Laser welding in automotive manufacturing |
| `min:Data` | `examples/data.ttl` | Vibration measurement data from a wind turbine |
| `min:Agent` | `examples/agent.ttl` | Collaborative robot, human worker, software agent |
| `min:Boundary` | `examples/boundary.ttl` | Friction boundary between tool and sheet metal |
| `min:Lex` | `examples/lex.ttl` | Hooke's law in a spring test |
| `min:Structura` | `examples/structura.ttl` | Euler-Bernoulli beam theory in bridge design |
| `min:Possibile` | `examples/possibile.ttl` | Fatigue crack scenario (offshore wind) |
| `min:Norma` | `examples/norma.ttl` | Maximum deflection requirement (Eurocode) |
| `min:Institutio` | `examples/institutio.ttl` | ISO 9001 certification and type assignment |

Non-instantiable roots (`min:Entity`, `min:Nexus`, `min:Forma`) are abstract query anchors.

---

## Object — material-dominant entity

**File:** `examples/object.ttl`
**Pattern highlights:** material/informational subproperties, mereology, process participation.

```turtle
ex:Stahltraeger_B12 a min:Object ;
    min:hasIdentifier    "OBJ-IPE300-B12" ;
    min:hasName          "Stahlträger IPE 300, Brücke Feld 12" ;
    min:undergoes        ex:Feuerverzinken_B12 .
```

---

## Process — transformation and event

**File:** `examples/process.ttl`
**Pattern highlights:** `hasInput`, `hasOutput`, `performedBy`, `generates`.

```turtle
ex:Laserschweissen_047 a min:Process ;
    min:hasInput         ex:Profil_A_links ;
    min:hasInput         ex:Profil_B_links ;
    min:hasOutput        ex:Seitenteil_links ;
    min:performedBy      ex:Schweissroboter_R7 ;
    min:generates        ex:Schweissprotokoll_047 .
```

---

## Data — informational artifact

**File:** `examples/data.ttl`
**Pattern highlights:** `describes`, `generatedBy`, `encodes`.

```turtle
ex:Schwingungsdaten_G5_2026 a min:Data ;
    min:describes        ex:Getriebe_G5 ;
    min:generatedBy      ex:Schwingungsmessung_G5 .
```

---

## Agent — acting entity

**File:** `examples/agent.ttl`
**Pattern highlights:** dual typing (`Object` + `Agent`), `performs`, `controls`, `actsOn`.

```turtle
ex:Cobot_UR10e a min:Object , min:Agent ;
    min:performs  ex:Schraubmontage_Deckel ;
    min:actsOn    ex:Getriebegehaeuse_K9 .
```

---

## Boundary — friction as irreducibly relational nexus

**File:** `examples/boundary.ttl`
**Pattern highlights:** first-class boundary node, `bounds`, contextual coefficients.

```turtle
ex:Reibkontakt_Werkzeug_Blech_A17 a min:Boundary ;
    min:bounds ex:Matrize_A17 ;
    min:bounds ex:AluBlech_A17 .
```

---

## Lex — law-like regularity

**File:** `examples/lex.ttl`
**Pattern highlights:** `governs`, `constrains`, `realizedBy`, Data/Forma separation via `encodes`.

```turtle
ex:Hooke_Gesetz a min:Lex ;
    min:governs     ex:Federpruefung_101 ;
    min:constrains  ex:Druckfeder_F42 .
```

---

## Structura — mathematical structure

**File:** `examples/structura.ttl`
**Pattern highlights:** `formalizes`, `realizedBy`.

```turtle
ex:Euler_Bernoulli_Balkentheorie a min:Structura ;
    min:formalizes ex:Brueckenberechnung_Feld12 ;
    min:realizedBy ex:Brueckenberechnung_Feld12 .
```

---

## Possibile — possibility and counterfactual

**File:** `examples/possibile.ttl`
**Pattern highlights:** `concerns`, `alternativeTo`.

```turtle
ex:Ermuedungsriss_Naht_G5 a min:Possibile ;
    min:concerns      ex:Schweissnaht_Turmfuss_G5 ;
    min:alternativeTo ex:Inspektion_G5_2026 .
```

---

## Norma — normative requirement

**File:** `examples/norma.ttl`
**Pattern highlights:** `evaluates` with explicit threshold semantics.

```turtle
ex:Max_Durchbiegung_L300 a min:Norma ;
    min:evaluates ex:Stahltraeger_B12 ;
    min:evaluates ex:Brueckenberechnung_Feld12 .
```

---

## Institutio — institutional construct

**File:** `examples/institutio.ttl`
**Pattern highlights:** `constitutedBy`, `recognizedBy`, `typifies`, linked encoding artifacts.

```turtle
ex:ISO9001_Zertifizierung_WerkA a min:Institutio ;
    min:constitutedBy ex:TUeV_Sued ;
    min:recognizedBy  ex:TUeV_Sued .

ex:DC04_Institutio a min:Institutio ;
    min:typifies ex:Blech_042 .
```

---

## Integrated scenarios

- `examples/min-v3.3.0-examples.ttl`: integrated historical scenario.
- `examples/eierkochen.ttl`: tutorial-scale scenario used in current docs.

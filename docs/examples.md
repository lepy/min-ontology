# Per-Class Examples

MIN provides dedicated example files for the main instantiable classes. Each file is a
self-contained Turtle graph showing how to properly model instances of that class,
including the required relations and typical domain-specific properties.

All examples pass the instance-level SHACL validation (`shapes/min-instance.shacl.ttl`).

## Overview

| Class | File | Scenario |
| --- | --- | --- |
| `min:Object` | `examples/object.ttl` | Steel beam in bridge construction |
| `min:Process` | `examples/process.ttl` | Laser welding in automotive manufacturing |
| `min:Data` | `examples/data.ttl` | Vibration measurement data from a wind turbine |
| `min:Agent` | `examples/agent.ttl` | Collaborative robot, human worker, software agent |
| `min:Boundary` | - | Covered in ontology docs; standalone instance example pending |
| `min:Lex` | `examples/lex.ttl` | Hooke's Law in a spring test |
| `min:Structura` | `examples/structura.ttl` | Euler-Bernoulli beam theory in bridge design |
| `min:Possibile` | `examples/possibile.ttl` | Fatigue crack scenario (offshore wind) |
| `min:Norma` | `examples/norma.ttl` | Maximum deflection requirement (Eurocode) |
| `min:Institutio` | `examples/institutio.ttl` | ISO 9001 certification |

Non-instantiable classes (`min:Entity`, `min:Nexus`, `min:Forma`) serve as abstract
roots and query anchors — they are never directly instantiated.

---

## Object — material-dominant entity

**File:** `examples/object.ttl`
**Scenario:** A steel beam (IPE 300) in a bridge construction.

Key patterns shown:

- Material properties (`ex:masse_kg`, `ex:laenge_m`) declared as `rdfs:subPropertyOf min:materialProperty`
- Informational properties (`ex:werkstoffNr`, `ex:profilbezeichnung`) declared as `rdfs:subPropertyOf min:informationalProperty`
- Mereology via `min:hasComponent` (bridge field contains beam)
- Inverse relation `min:undergoes` linking to a process

```turtle
ex:Stahltraeger_B12 a min:Object ;
    min:hasIdentifier    "OBJ-IPE300-B12" ;
    min:hasName          "Stahlträger IPE 300, Brücke Feld 12" ;
    min:hasStatus        "montiert" ;
    ex:masse_kg          420.0 ;
    ex:laenge_m          10.0 ;
    ex:werkstoffNr       "1.0577" ;
    ex:profilbezeichnung "IPE 300" ;
    min:undergoes        ex:Feuerverzinken_B12 .
```

---

## Process — transformation and event

**File:** `examples/process.ttl`
**Scenario:** Laser welding of two aluminum profiles in vehicle manufacturing.

Key patterns shown:

- Multiple `min:hasInput` (two profiles) and `min:hasOutput` (welded part)
- `min:performedBy` linking to an Agent (welding robot, dual-typed as Object+Agent)
- `min:generates` producing Data (weld protocol)
- Domain-specific material properties on the process itself

```turtle
ex:Laserschweissen_047 a min:Process ;
    min:hasInput         ex:Profil_A_links ;
    min:hasInput         ex:Profil_B_links ;
    min:hasOutput        ex:Seitenteil_links ;
    min:performedBy      ex:Schweissroboter_R7 ;
    min:generates        ex:Schweissprotokoll_047 ;
    ex:laserleistung_kW  4.5 ;
    ex:vorschub_m_min    1.2 .
```

**SHACL requirement:** Every Process must have at least one `hasInput` and one `hasOutput` (range: `min:Nexus` — any Nexus instance can be input/output).

---

## Data — informational artifact

**File:** `examples/data.ttl`
**Scenario:** Vibration measurement data from an offshore wind turbine gearbox.

Key patterns shown:

- `min:describes` linking Data to the Object it is about
- `min:generatedBy` linking Data to the Process that produced it
- `min:encodes` as a bridge relation: a limit-value document (Data) encodes a threshold (Norma)
- Informational properties (`ex:abtastrate_Hz`, `ex:datenformat`) and material properties (`ex:dateigroesse_MB`)

```turtle
ex:Schwingungsdaten_G5_2026 a min:Data ;
    min:hasName          "Schwingungsmessdaten Getriebe G5" ;
    min:describes        ex:Getriebe_G5 ;
    min:generatedBy      ex:Schwingungsmessung_G5 ;
    ex:abtastrate_Hz     25600 ;
    ex:dateigroesse_MB   1840.0 ;
    ex:datenformat       "TDMS" .
```

---

## Agent — acting entity

**File:** `examples/agent.ttl`
**Scenario:** Collaborative robot (cobot) in gearbox assembly, plus human worker and software agent.

Key patterns shown:

- **Dual typing** `min:Object, min:Agent` for physical agents (cobot)
- **Pure Agent** for humans and software (no Object typing)
- `min:performs`, `min:controls` (stronger than performs), `min:actsOn`, `min:owns`
- Three distinct agent types showing breadth: machine, human, software

```turtle
ex:Cobot_UR10e a min:Object , min:Agent ;
    min:hasName   "UR10e Montagezelle 3" ;
    min:performs  ex:Schraubmontage_Deckel ;
    min:actsOn    ex:Getriebegehaeuse_K9 .

ex:Werker_Schmidt a min:Agent ;
    min:performs  ex:Qualitaetskontrolle_K9 ;
    min:controls  ex:Schraubmontage_Deckel ;
    min:owns      ex:Getriebegehaeuse_K9 .

ex:MES_Planner a min:Agent ;
    min:performs  ex:Reihenfolgeplanung_Montage .
```

**SHACL requirement:** Every Agent must have at least one `performs`.

---

## Lex — law-like regularity

**File:** `examples/lex.ttl`
**Scenario:** Hooke's Law governing a spring test.

Key patterns shown:

- `min:governs` (Lex → Process): the law governs the test
- `min:constrains` (Lex → Object): the law constrains the spring
- `min:realizedBy` (inverse bridge): the test realizes the law
- **Lex vs. Data distinction:** The textbook (Data) `min:encodes` the law (Lex) — deleting the book does not delete the law

```turtle
ex:Hooke_Gesetz a min:Lex ;
    min:hasName             "Hookesches Gesetz" ;
    ex:formel               "F = k · Δx" ;
    ex:gueltigkeitsbereich  "linear-elastisch, kleine Verformungen" ;
    min:governs             ex:Federpruefung_101 ;
    min:constrains          ex:Druckfeder_F42 ;
    min:realizedBy          ex:Federpruefung_101 .
```

---

## Structura — mathematical structure

**File:** `examples/structura.ttl`
**Scenario:** Euler-Bernoulli beam theory in a bridge calculation.

Key patterns shown:

- `min:formalizes` (Structura → Nexus): the theory formalizes the calculation
- `min:realizedBy` (inverse bridge): the calculation realizes the theory
- **Structura vs. Data distinction:** The FEM model (Data) `min:encodes` the theory (Structura)

```turtle
ex:Euler_Bernoulli_Balkentheorie a min:Structura ;
    min:hasName       "Euler-Bernoulli-Balkentheorie" ;
    ex:formel         "EI · w''''(x) = q(x)" ;
    min:formalizes    ex:Brueckenberechnung_Feld12 ;
    min:realizedBy    ex:Brueckenberechnung_Feld12 .
```

---

## Possibile — possibility and counterfactual

**File:** `examples/possibile.ttl`
**Scenario:** Fatigue crack scenario at an offshore wind turbine weld seam.

Key patterns shown:

- `min:concerns` (Possibile → Nexus): the scenario concerns a weld seam
- `min:alternativeTo` (Possibile → Nexus): the scenario is an alternative to an inspection process
- **Unrealized vs. realized:** One Possibile is pure risk, another could be realized by a Process
- **Possibile vs. Data:** The FMEA table (Data) `min:encodes` the scenarios (Possibile)

```turtle
ex:Ermuedungsriss_Naht_G5 a min:Possibile ;
    min:hasName             "Ermüdungsriss Schweißnaht Turmfuß Gondel 5" ;
    ex:wahrscheinlichkeit   0.08 ;
    ex:bedingung            "N > 10⁷ LW, ΔK > ΔK_th, keine Nachbehandlung" ;
    min:concerns            ex:Schweissnaht_Turmfuss_G5 ;
    min:alternativeTo       ex:Inspektion_G5_2026 .
```

---

## Norma — normative requirement

**File:** `examples/norma.ttl`
**Scenario:** Maximum deflection requirements for a bridge (Eurocode).

Key patterns shown:

- `min:evaluates` (Norma → Nexus): the requirement evaluates both an Object and a Process
- **Norma vs. Lex:** Laws cannot be violated, norms can — that is the key distinction
- **Norma vs. Data:** The Eurocode PDF (Data) `min:encodes` the requirement (Norma)

```turtle
ex:Max_Durchbiegung_L300 a min:Norma ;
    min:hasName          "Maximale Durchbiegung L/300" ;
    min:hasDescription   "Vertikale Durchbiegung ≤ L/300 unter Verkehrslast" ;
    ex:eigenschaft       "vertikale Durchbiegung" ;
    ex:operator          "<=" ;
    ex:schwellenwert     "L/300" ;
    min:evaluates        ex:Stahltraeger_B12 ;
    min:evaluates        ex:Brueckenberechnung_Feld12 .
```

---

## Institutio — institutional construct

**File:** `examples/institutio.ttl`
**Scenario:** ISO 9001 certification of a manufacturing plant.

Key patterns shown:

- `min:constitutedBy` (Institutio → Agent): the certification body created the institution
- `min:recognizedBy` (Institutio → Agent): multiple agents recognize the institution
- **Institutio vs. Agent:** TÜV SÜD as an Agent performs the audit and constitutes the certification; the certification itself is Institutio
- **Institutio vs. Data:** The certificate document (Data) `min:encodes` the certification (Institutio)

```turtle
ex:ISO9001_Zertifizierung_WerkA a min:Institutio ;
    min:hasName             "ISO 9001:2015 Zertifizierung Werk A" ;
    min:hasStatus           "gültig" ;
    ex:gueltig_bis          "2028-06-30"^^xsd:date ;
    min:constitutedBy       ex:TUeV_Sued ;
    min:recognizedBy        ex:TUeV_Sued ;
    min:recognizedBy        ex:Kunde_OEM_Nord .
```

---

## Integrated scenario

The file `examples/min-v3.0.0-examples.ttl` contains a larger integrated scenario
(deep drawing of a steel coil) that uses all 9 classes together with bridge
relations, polarity properties, and cross-references. It serves as the primary
integration test for the ontology.

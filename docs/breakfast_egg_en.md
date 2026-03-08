# The Ontological Breakfast Egg

> **How do you model an everyday process with a foundational ontology?**
>
> This guide uses the example of boiling an egg to show how the MIN ontology
> works. Each step introduces a MIN category and explains why exactly
> that category is the right one.

---

## Overview

MIN has two branches and one cross-cutting category under `Entity`:

- **Nexus** — that which causes effects (Object, Process, Data, Boundary)
- **Forma** — the rulebook by which Nexus operates (Lex, Structura, Possibile, Norma, Institutio)
- **Agent** — that which acts. Orthogonal cross-cutting category that traverses the branch boundary.

Boiling an egg requires all three. The egg, the pot, the water —
these are Nexus instances. The cooking time specification, the natural
law of heat transfer, the doneness grade "soft-boiled" — these are
Forma instances. The cook and the active stove — these are Agents
with co-typing.

![min_hierarchy.svg](min_hierarchy.svg)

---

## Step 1 — The Things on the Table: Object

> *"Does it cause effects as a physical thing?"* → **Object.**

Everything sitting on the stove that is physically there: pot, water,
egg, stove. Object is the material-dominant Nexus. Identity criterion:
material continuity — the egg remains the same egg, even as it changes.

```turtle
@prefix egg: <https://example.org/egg#> .
@prefix min: <https://w3id.org/min#> .

egg:Pot a min:Object ;
    min:hasIdentifier "OBJ-POT-001" ;
    min:hasName "Cooking pot"@en ;
    egg:material "Stainless steel" ;
    egg:volume_ml "2000"^^xsd:float .

egg:Water a min:Object ;
    min:hasIdentifier "OBJ-WATER-001" ;
    min:hasName "Cooking water"@en ;
    egg:amount_ml "1500"^^xsd:float .

egg:Egg_raw a min:Object ;
    min:hasIdentifier "OBJ-EGG-RAW-001" ;
    min:hasName "Raw egg"@en ;
    egg:weight_g "58"^^xsd:float ;
    egg:startTemperature_C "7"^^xsd:float .
```

**Why Object and not Agent?** The pot does not act. The water does not
act. The egg does not act. They are physically present and are
transformed by Processes — but they control nothing.

---

## Step 2 — The Cook and the Stove: Agent

> *"Does it act selectively and accountably?"* → **Agent.**

The cook is an Agent — they decide when to place the egg, how long to
cook, whether to quench. The active stove is also an Agent — it
regulates energy supply selectively.

Agent is an orthogonal cross-cutting category under Entity (v1.0).
Agent is not a category of being but a category of action. It traverses
the branch boundary between Nexus and Forma. Co-typing is mandatory:
every Agent must carry at least one category of being.

```turtle
egg:Cook a min:Agent , min:Object ;
    min:hasIdentifier "AGT-COOK-001" ;
    min:hasName "Cook"@en ;
    min:performs egg:EggBoiling ;
    min:controls egg:EggBoiling .

egg:Stove_active a min:Agent , min:Object ;
    min:hasIdentifier "AGT-STOVE-001" ;
    min:hasName "Stove (active)"@en ;
    min:performs egg:Heating .
```

**Why `a min:Agent, min:Object`?** Because the cook is physically
present (Object) AND acts (Agent). MIN enforces co-typing — Agent
alone never suffices. The co-class determines the mode of being:
Agent ∩ Object → Nexus branch. Agent ∩ Institutio → Forma branch.

**Why is gravity not an Agent?** It acts universally, not selectively.
Universality disqualifies for agency — but qualifies for Lex (→ Step 7).

**Why is Agent no longer a Nexus category?** Because Agent traverses
the branch boundary. An organisation acts (Agent) AND is recognised
(Institutio). The annihilation test shows: the same annihilation
condition — therefore the same thing. Agent must stand above the
branch boundary: `rdfs:subClassOf min:Entity`.

---

## Step 3 — What Happens: Process

> *"Does it transform inputs into outputs over time?"* → **Process.**

Egg boiling is a Process with sub-processes. Process is the balanced
Nexus — both poles (material, informational) carry equal weight.

```turtle
egg:EggBoiling a min:Process ;
    min:hasIdentifier "PRC-BOIL-001" ;
    min:hasName "Egg boiling"@en ;
    min:hasInput egg:Egg_raw ;
    min:hasInput egg:Water ;
    min:hasOutput egg:Egg_boiled ;
    min:performedBy egg:Cook ;
    min:hasComponent egg:Heating ;
    min:hasComponent egg:Simmering ;
    min:hasComponent egg:Quenching .

egg:Heating a min:Process ;
    min:hasIdentifier "PRC-HEAT-001" ;
    min:hasName "Heating water"@en ;
    min:hasInput egg:Water ;
    min:hasOutput egg:Water ;
    min:performedBy egg:Stove_active .

egg:Simmering a min:Process ;
    min:hasIdentifier "PRC-SIM-001" ;
    min:hasName "Simmering"@en ;
    min:hasInput egg:Egg_raw ;
    min:hasOutput egg:Egg_boiled .

egg:Quenching a min:Process ;
    min:hasIdentifier "PRC-QUENCH-001" ;
    min:hasName "Quenching"@en ;
    min:hasInput egg:Egg_boiled ;
    min:hasOutput egg:Egg_boiled .
```

**Two modes of transformation:**

- **Transformative** (`hasInput`/`hasOutput`): Egg_raw → Simmering → Egg_boiled.
  Two different entities, two IDs. The raw egg no longer exists.
- **Conservative** (`undergoes`): Heating warms the water, but it
  remains the same water.

The distinction lies in the relation, not in the category.

**Why does `hasInput` range over Nexus, not Object?** Because MIN
thinks causally, not materialistically. A simulation process consumes
Data as input. Therefore: `min:hasInput` → `rdfs:range min:Nexus`.

---

## Step 4 — What Emerges In Between: Boundary

> *"Remove one partner — does the phenomenon still exist? No?"* → **Boundary.**

The heat transfer between water and eggshell belongs to neither the
water nor the egg. It emerges only *between* them. Remove the egg from
the water — the heat transfer coefficient vanishes.

```turtle
egg:HeatTransfer_Water_Egg a min:Boundary ;
    min:hasIdentifier "BND-WE-001" ;
    min:hasName "Heat transfer water–egg"@en ;
    min:bounds egg:Water ;
    min:bounds egg:Egg_raw ;
    egg:heatTransferCoefficient_W_m2K "3000"^^xsd:float .

egg:HeatTransfer_Pot_Water a min:Boundary ;
    min:hasIdentifier "BND-PW-001" ;
    min:hasName "Heat transfer pot–water"@en ;
    min:bounds egg:Pot ;
    min:bounds egg:Water .
```

**Why not simply a property on the Object?**
`egg:Water egg:heatTransferCoefficient "3000"` would be physically
wrong. The coefficient is not a property of the water — it depends
on the flow, the shell surface, and the temperature difference.
It is a system property. That is precisely what Boundary is.

**Why not Object?** The surface of the egg is Object (remove all
partners — the surface remains). But the heat transfer between water
and egg is Boundary (remove the egg — the transfer vanishes).

---

## Step 5 — What Describes: Data

> *"Does it exist as an information carrier — bytes, structure, semantics?"* → **Data.**

The recipe on the kitchen table and the measured cooking time are Data.
They have a physical existence (paper, bytes) and encode Forma (cooking
time specifications, doneness grades).

```turtle
egg:MeasuredCookingTime a min:Data ;
    min:hasIdentifier "DAT-TIME-001" ;
    min:hasName "Cooking time measurement"@en ;
    min:describes egg:Simmering ;
    min:generatedBy egg:EggBoiling ;
    min:encodes egg:Norma_soft ;
    egg:cookingTime_min "5.5"^^xsd:float .

egg:Recipe a min:Data ;
    min:hasIdentifier "DAT-REC-001" ;
    min:hasName "Cooking recipe"@en ;
    min:describes egg:EggBoiling ;
    min:encodes egg:Norma_soft ;
    min:encodes egg:Norma_hard ;
    min:encodes egg:Doneness_softBoiled .
```

**The key relation: `min:encodes`.**
The recipe (Data) encodes the cooking time specification (Norma). If you
throw away the recipe, the specification remains — every cook knows it
by heart. Data IS NOT Forma. Data ENCODES Forma.

---

## Step 6 — From Here: Forma

Everything so far was Nexus — the actual, the causally effective.
Now comes Forma: the rulebook by which Nexus operates. Forma causes
nothing. But without Forma, every effect would be different.

```
Nexus = the sentences  →  Pot, Water, Egg, Cook, Boiling
Forma = the grammar    →  Heat law, Cooking times, Doneness grades
```

---

## Step 7 — What Holds: Lex

> *"Does it hold universally, without exception?"* → **Lex.**

Heat transfer and protein denaturation are natural laws. They determine
HOW simmering proceeds. No cook can change them.

```turtle
egg:HeatTransferLaw a min:Lex ;
    min:hasIdentifier "LEX-HEAT-001" ;
    min:hasName "Heat transfer law"@en ;
    min:governs egg:Simmering ;
    min:constrains egg:HeatTransfer_Water_Egg .

egg:ProteinDenaturation a min:Lex ;
    min:hasIdentifier "LEX-DENAT-001" ;
    min:hasName "Protein denaturation"@en ;
    min:governs egg:Simmering .
```

**`min:governs`** is the specialised bridge relation: Lex → Process.
The natural law determines HOW the Process unfolds.

**Why is protein denaturation not an Agent?** It acts universally —
every protein denatures under heat. Universality disqualifies for
agency (selective, accountable). But it qualifies for Lex.

---

## Step 8 — What Shapes: Structura

> *"Is it a purely mathematical structure?"* → **Structura.**

The heat conduction equation in spherical coordinates formalises how
temperature distributes inside the egg over time. It does not exist
physically — but it determines the geometry of the possible.

```turtle
egg:HeatConductionEquation a min:Structura ;
    min:hasIdentifier "STRUCT-HC-001" ;
    min:hasName "Heat conduction equation (sphere)"@en ;
    min:formalizes egg:Simmering .
```

**Why not Data?** The FEM implementation of the equation would be Data
(has bytes, storage location, version). The equation *itself* —
∂T/∂t = α·∇²T — is Structura. The implementation *encodes* the
structure: `Data encodes Structura`.

---

## Step 9 — What Ought to Hold: Norma

> *"Does it define a target value against which something can be evaluated?"* → **Norma.**

The cooking time specifications are norms. They cause nothing — but
they define the difference between "soft" and "too hard".

Norma is ATOMIC: each individual requirement is a self-standing Norma
instance. The bundling of multiple Norma into a type determination is
Institutio, not Norma (→ Step 10).

```turtle
egg:Norma_soft a min:Norma ;
    min:hasIdentifier "NORMA-SOFT-001" ;
    min:hasName "Cooking time soft-boiled"@en ;
    min:evaluates egg:Egg_boiled ;
    egg:cookingTime_min_min "4"^^xsd:float ;
    egg:cookingTime_max_min "5"^^xsd:float .

egg:Norma_medium a min:Norma ;
    min:hasIdentifier "NORMA-MED-001" ;
    min:hasName "Cooking time medium-boiled"@en ;
    min:evaluates egg:Egg_boiled ;
    egg:cookingTime_min_min "6"^^xsd:float ;
    egg:cookingTime_max_min "7"^^xsd:float .

egg:Norma_hard a min:Norma ;
    min:hasIdentifier "NORMA-HARD-001" ;
    min:hasName "Cooking time hard-boiled"@en ;
    min:evaluates egg:Egg_boiled ;
    egg:cookingTime_min_min "9"^^xsd:float ;
    egg:cookingTime_max_min "11"^^xsd:float .
```

**`min:evaluates`**: Norma → Nexus. The cooking time specification
*evaluates* the boiled egg: pass or fail.

**Why is Norma not Lex?** Lex cannot be violated — protein denaturation
always happens. Norma can be violated — you can cook for 15 minutes and
still get an egg, just not a good one. That is precisely what makes
Norma a Norma.

---

## Step 10 — What Makes Something What It Is: Institutio

> *"What kind of egg is it?"* → **Institutio.**

The doneness grade "soft-boiled" is an Institutio — a conventional
bundling of determinations that establishes what the egg counts as.
Institutio bundles Norma, Lex, Structura, and properties into a type
determination. This bundling exists because a community of practice
(here: cooks) recognises it.

Searle: *"X counts as Y in context C."* The boiled egg (Object) counts
as soft-boiled (Institutio) in the context of the kitchen.

```turtle
egg:Doneness_softBoiled a min:Institutio ;
    min:hasIdentifier "INST-SOFT-001" ;
    min:hasName "soft-boiled"@en ;
    min:typifies egg:Egg_boiled ;
    min:comprises egg:Norma_soft ;
    min:recognizedBy egg:Cook .

egg:Doneness_mediumBoiled a min:Institutio ;
    min:hasIdentifier "INST-MED-001" ;
    min:hasName "medium-boiled"@en ;
    min:typifies egg:Egg_boiled ;
    min:comprises egg:Norma_medium ;
    min:recognizedBy egg:Cook .

egg:Doneness_hardBoiled a min:Institutio ;
    min:hasIdentifier "INST-HARD-001" ;
    min:hasName "hard-boiled"@en ;
    min:typifies egg:Egg_boiled ;
    min:comprises egg:Norma_hard ;
    min:recognizedBy egg:Cook .

egg:ChickenEgg_M a min:Institutio ;
    min:hasIdentifier "INST-EGG-M-001" ;
    min:hasName "Chicken egg size M"@en ;
    min:typifies egg:Egg_raw ;
    min:recognizedBy egg:Cook .
```

**`min:typifies`**: Institutio → Nexus. The Institutio *determines*
what the Nexus counts as. Not describe (→ Data), not evaluate
(→ Norma), but DETERMINE.

**`min:comprises`**: Institutio → Forma. The bundling relation. The
doneness grade "soft-boiled" *comprises* the Norma "cooking time
4–5 min". The bundled Forma instances exist independently. The
bundling is the institutional act.

**Why is "soft-boiled" not Norma?** Norma is ATOMIC and evaluates:
"The cooking time SHALL be 4–5 minutes." Institutio BUNDLES and
constitutes: "A soft-boiled egg IS one with set white and runny yolk —
and the cooking community recognises this." Norma asks: Pass?
Institutio asks: What is it?

**Polyhierarchy:** An egg can have multiple Institutio types — it is
simultaneously `ChickenEgg_M` (egg variety) and `Doneness_softBoiled`
(doneness grade).

**Why Institutio and not a separate category "Typus"?** The bundling of
Forma instances into a type determination is an institutional act — it
exists because a community of practice recognises it. "Soft-boiled"
remains "soft-boiled" as long as ANYONE recognises the convention. If
NOBODY knows it any longer, it disintegrates into its atomic Norma
constituents. This is precisely Searle's criterion for Institutio.
Classification IS an institutional act.

---

## Step 11 — What Could Go Wrong: Possibile

> *"Could it happen, but has not happened?"* → **Possibile.**

The water could boil over. A green ring could form around the yolk.
Modal statements about the non-actual.

```turtle
egg:BoilingOver a min:Possibile ;
    min:hasIdentifier "POSS-OVER-001" ;
    min:hasName "Boiling over"@en ;
    min:concerns egg:Heating .

egg:GreenRing a min:Possibile ;
    min:hasIdentifier "POSS-GREEN-001" ;
    min:hasName "Green ring around yolk"@en ;
    min:concerns egg:Egg_boiled .
```

**Why not Process?** A Process HAPPENS. A Possibile does NOT happen —
it COULD happen. If the water actually boils over, it becomes a Process
(`min:realizes`).

---

## Step 12 — Social Constructs: Institutio (Second Function)

> *"Does it exist only because agents recognise it?"* → **Institutio.**

In Step 10 we encountered Institutio as conventional bundling (doneness
grades). Institutio has a second function: social constructs in the
narrower sense.

The EU marketing standard for eggs (size classes S/M/L/XL) exists
because EU member states recognise it. Without recognition — no standard.

```turtle
egg:EU_MarketingStandard a min:Institutio ;
    min:hasIdentifier "INST-EU-EGG-001" ;
    min:hasName "EU marketing standards for eggs"@en ;
    min:comprises egg:Norma_size_M ;
    min:constitutedBy egg:EU_Commission ;
    min:recognizedBy egg:Cook .
```

**Institutio thus has two functions:**

1. **Conventional bundlings** — doneness grades, steel grades, test methods.
   The bundling of atomic Forma into a type determination (Step 10).
2. **Social constructs** — money, patents, marketing standards, organisations.
   Institutional facts in Searle's sense.

Both exist through collective recognition. Both disintegrate when
nobody recognises them any longer.

---

## Step 13 — Domain Properties: Polarity

MIN distinguishes at the schema level between material and
informational properties. This is polarity — a heuristic, not an axiom.

```turtle
egg:material a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:materialProperty ;
    rdfs:domain min:Object ;
    rdfs:range xsd:string .

egg:weight_g a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:materialProperty ;
    rdfs:domain min:Object ;
    rdfs:range xsd:float .

egg:cookingTime_min a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:informationalProperty ;
    rdfs:domain min:Data ;
    rdfs:range xsd:float .

egg:heatTransferCoefficient_W_m2K a owl:DatatypeProperty ;
    rdfs:subPropertyOf min:materialProperty ;
    rdfs:domain min:Boundary ;
    rdfs:range xsd:float .
```

**Materiality** is declared for properties that capture the physical,
the causal (mass, volume, temperature). **Informationality** for
properties that capture the structural, the semantic (cooking time as
a measured value, file format). The declaration lies in the property,
not in the instance. The instances remain flat.

Polarity is a HEURISTIC: domain properties CAN be declared as
subproperties, but NEED NOT be. Temporal, modal, and state-related
properties (hasTimestamp, hasStatus) fit neither category and require
no polarity label.

---

## Summary

```
Nexus (causes effects)             Forma (determines)
──────────────────────             ──────────────────
Object:   Pot, Water, Egg           Lex:        Heat transfer,
Process:  Boiling, Simmering                   Protein denaturation
Data:     Measurement, Recipe      Structura:  Heat conduction equation
Boundary: Heat transfer ×2         Norma:      Cooking times (s/m/h)
                                   Possibile:  Boiling over, Green ring
Cross-cutting (acts)               Institutio: Doneness grades (soft/med/hard),
──────────────────────                         Chicken egg size M,
Agent:    Cook, Stove (active)                 EU marketing standard
          (each Agent ∩ Object)
```

**Bridge relations connect the branches:**

| Relation | Example |
|---|---|
| `realizes` | Simmering realises the heat conduction equation |
| `governs` | Protein denaturation governs Simmering |
| `evaluates` | Norma_soft evaluates Egg_boiled |
| `encodes` | Recipe encodes Norma_soft |
| `typifies` | Doneness_softBoiled typifies Egg_boiled |
| `comprises` | Doneness_softBoiled comprises Norma_soft |
| `formalizes` | Heat conduction equation formalizes Simmering |
| `concerns` | GreenRing concerns Egg_boiled |
| `constrains` | Heat transfer law constrains HeatTransfer_Water_Egg |

**No metaphysics. Just a delicious breakfast egg.**

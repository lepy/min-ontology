# What Engineering Knowledge Graphs Must Express

**Context:** MIN v1.1.0 — foundational ontology for engineers.

Engineering knowledge graphs face a specific challenge: they must represent
not only what exists and what happens, but also what determines, what is
believed, and what is uncertain. MIN addresses this through seven axes.

---

## Axis 1: Materiality — what exists physically?

| Question | MIN construct |
|---|---|
| What is physically there? | Object |
| What happens / was done? | Process |
| What data is available? | Data |
| What arises only between partners? | Boundary |

A tensile test has a specimen (Object), the testing procedure (Process),
measurement data (Data), and contact friction between specimen and grip
(Boundary). All four are causally efficacious — they cause something in
the world.

**Key relations:**
- `hasInput` / `hasOutput` — what goes in, what comes out
- `hasComponent` — mereological composition
- `generates` / `generatedBy` — process produces data
- `describes` / `describedBy` — data describes nexus
- `bounds` / `hasBoundary` — boundary between partners

---

## Axis 2: Formality — what determines without causing?

| Question | MIN construct |
|---|---|
| Which natural law holds? | Lex |
| Which formal model describes it? | Structura |
| What could happen? | Possibile |
| What requirement must be met? | Norma |
| What is collectively recognized (grade, standard, type)? | Institutio |
| What is held to be true? | Epistemicum |

A materials engineer needs all six: Hooke's law (Lex), Johnson-Cook model
(Structura), fatigue crack scenario (Possibile), Rm >= 270 MPa (Norma),
DC04 steel grade (Institutio), and "Hooke holds here up to 200 MPa" as
an evaluated hypothesis (Epistemicum).

**Key principle:** Forma causes nothing — but without Forma, every effect
would be different. Forma is the grammar, Nexus is the sentences.

**Key relations:**
- `governs` — Lex constrains Process
- `formalizes` — Structura constrains Nexus
- `evaluates` — Norma constrains Nexus
- `concerns` / `alternativeTo` — Possibile relates to Nexus
- `typifies` — Institutio determines what kind a Nexus counts as
- `comprises` — Institutio bundles atomic Forma instances

---

## Axis 3: Agency — who acts?

| Question | MIN construct |
|---|---|
| Who executes? | Agent ∩ Object (human, machine) |
| Which software decides? | Agent ∩ Data (ML model) |
| Which organization is responsible? | Agent ∩ Institutio |

Not just humans. A CNC machine, an ML model, a standards committee — all
act selectively. Agent is a cross-category under Entity, not a subcategory
of Nexus. Co-typing is mandatory.

**Key relations:**
- `performs` / `controls` — agent carries out process
- `actsOn` — agent acts on object (derived via property chain)
- `owns` — ownership / responsibility
- `constitutes` / `recognizes` — agent creates / acknowledges institution

---

## Axis 4: Causality — how does it connect?

### Within the world (Nexus ↔ Nexus)

- What goes in, what comes out? → `hasInput` / `hasOutput`
- Who carries out the process? → `performs` / `controls`
- What is it made of? → `hasComponent`

### Between world and determination (Nexus ↔ Forma)

Three generic bridge relations form the Forma lifecycle:

| Relation | Direction | Semantics |
|---|---|---|
| `originates` | Nexus → Forma | Nexus brings forth NEW formal determinants |
| `realizes` | Nexus → Forma | Nexus makes EXISTING formal determinants actual |
| `constrains` | Forma → Nexus | Forma restricts what Nexus can be or do |

Plus the encoding bridge:

| Relation | Direction | Semantics |
|---|---|---|
| `encodes` | Data → Forma | Data carries formal content (DIN document encodes Norma) |

**Key distinction:**
- `realizes` changes the world (ontological).
- `confirms` changes what we know (epistemic).

---

## Axis 5: Epistemics — what do we know, and how certain?

| Question | How MIN expresses it |
|---|---|
| Who believes it? | `heldBy` Agent (or agent-free) |
| About what? | `about` Entity |
| How certain? | `hasConfidence` [0..1] + `hasConfidenceType` |
| Which status? | `hasEpistemicStatus` (5 values) |
| Based on what? | `supportedBy` / `underminedBy` Nexus |
| What was believed before? | `supersedes` (Forma → Forma) |

This is what engineering knowledge graphs typically could *not* do before
MIN v1.1.0: formalize the difference between "42% recyclate content" and
"42% recyclate content, statistically confirmed with confidence 0.92
supported by XRF measurement data."

### Two complementary patterns

| Pattern | Carrier | Semantics | Since |
|---|---|---|---|
| Popperian | Process | Process confirms/refutes Forma | v1.0.0 |
| Evidence-centric | Epistemicum | Stance supported/undermined by Nexus | v1.1.0 |

Both are needed. The Popperian pattern is compact for simple assertions
("the tensile test confirms Hooke's law"). The evidence-centric pattern
is needed when epistemic state evolves, confidence must be typed, or
multiple agents disagree.

---

## Axis 6: Uncertainty — what do we not know?

| Question | MIN construct |
|---|---|
| Quantifiable risk? | Possibile + `isQuantifiable` = true |
| Deep / Knightian uncertainty? | Possibile + `isQuantifiable` = false |
| Missing evidence? | Epistemicum without `supportedBy` |
| Dissent? | Two Epistemicum, same `about`, different agents, different status |

**Known unknowns:** "Component failure with 2% probability." Normal risk,
a distribution is assignable.

**Unknown unknowns:** "Climate change impact on supply chain." No
distribution assignable. This is not a bug but a deliberate statement.

---

## Axis 7: Provenance — where does the information come from?

| Question | MIN construct |
|---|---|
| Who produced the data? | Data + `generatedBy` Process |
| Who encoded the formal content? | Data + `encodes` Forma |
| Who brought forth the formal determinant? | Forma + `originatedBy` Nexus |
| What evidence supports the belief? | Epistemicum + `supportedBy` Nexus |

Provenance in MIN runs through three complementary mechanisms:
- **Data provenance:** `generatedBy` traces which process produced the data.
- **Forma provenance:** `originatedBy` traces which nexus brought forth the formal determinant.
- **Epistemic provenance:** `supportedBy` / `underminedBy` traces which evidence supports or weakens a belief.

---

## Axis 8: Temporality — when does it happen?

| Question | MIN construct |
|---|---|
| When was it recorded? | `hasTimestamp` (Entity → xsd:dateTime) |
| When did the process start? | `startedAt` (Process → xsd:dateTime) |
| When did the process end? | `endedAt` (Process → xsd:dateTime) |
| What temporal sequence? | Process chains via `hasInput` / `hasOutput` |
| What replaced what? | `supersedes` (Forma → Forma) |

MIN embeds temporality implicitly rather than as a separate temporal model.
Timestamps attach directly to entities and processes. Temporal ordering
emerges from process chains: if Process B uses the output of Process A,
then A precedes B. Epistemic succession uses `supersedes` — when a new
Epistemicum replaces an old one, the temporal dimension is captured
structurally, not through explicit time intervals.

**What alignment provides:**
- OWL-Time (`alignment/min-time.ttl`): `min:Process rdfs:subClassOf time:ProperInterval` —
  processes can be treated as time intervals by OWL-Time reasoners.
- PROV-O (`alignment/min-prov.ttl`): `min:startedAt rdfs:subPropertyOf prov:startedAtTime` —
  timestamps become visible to PROV-O tools.

**What belongs in the domain layer:**
- Time series data (sensor readings at millisecond resolution)
- Lifecycle phase models (design → manufacture → use → end-of-life)
- Calendar and scheduling constraints
- Allen interval relations (before, during, overlaps)

---

## Summary: eight axes

```
1. Materiality     What exists physically?                → Nexus
2. Formality       What determines without causing?       → Forma
3. Agency          Who acts?                              → Agent
4. Causality       How does it connect?                   → Relations
5. Epistemics      What do we know, how certain?          → Epistemicum
6. Uncertainty     What do we not know?                   → Possibile + isQuantifiable
7. Provenance      Where does the information come from?  → Data + originatedBy + supportedBy
8. Temporality     When does it happen?                   → hasTimestamp + startedAt/endedAt
```

## What MIN deliberately does NOT cover

| Concern | Why not | Where instead |
|---|---|---|
| Truth | "X is true" is not a MIN concept. Epistemicum says what is *believed*, not what *is*. | — |
| Bayesian propagation | Confidence propagation is a Process, not an axiom. | Domain layer |
| Time series | Temporal resolution belongs in the domain layer. | sdata-measurements |
| Physical units | Unit systems are orthogonal to ontological structure. | QUDT alignment |
| Emotions | "I feel the component will fail" is not propositional. | — |
| Self-reference | "I believe that I believe" is not cleanly modelable in OWL. | — |

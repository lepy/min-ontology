# MIN Class Catalog (v3.2.0)

This page lists **all classes** defined in `min.ttl` for MIN v3.2.0.

## Complete class list

| Class | Parent | Branch | Role |
| --- | --- | --- | --- |
| `min:Entity` | - | Root | Absolute top class |
| `min:Nexus` | `min:Entity` | Actual | Root of causally effective entities |
| `min:Object` | `min:Nexus` | Actual | Material-dominant entity |
| `min:Process` | `min:Nexus` | Actual | Transformation/event entity |
| `min:Data` | `min:Nexus` | Actual | Informational artifact |
| `min:Agent` | `min:Nexus` | Actual | Acting/selective entity |
| `min:Boundary` | `min:Nexus` | Actual | Irreducibly relational boundary phenomenon |
| `min:Forma` | `min:Entity` | Formal | Root of formal determinants |
| `min:Lex` | `min:Forma` | Formal | Law-like regularity |
| `min:Structura` | `min:Forma` | Formal | Mathematical/formal structure |
| `min:Possibile` | `min:Forma` | Formal | Possibility/counterfactual |
| `min:Norma` | `min:Forma` | Formal | Normative requirement |
| `min:Institutio` | `min:Forma` | Formal | Institutional construct |

## Detailed class definitions

### `min:Entity`

- Absolute ontology root
- Every MIN individual is in either the `Nexus` or `Forma` branch
- Formal partition axiom (v3.1.0): `Entity ≡ Nexus ⊔ Forma`
- Not intended for direct instantiation

### `min:Nexus`

- Root of actual entities
- Existence criterion: causal efficacy
- Query anchor for all actual entities
- Not intended for direct instantiation

### `min:Object`

- Material-dominant actual entity
- Identity criterion: material continuity
- Typical examples: parts, tools, machines, fields, shadows
- Example: [`examples/object.ttl`](examples.md#object-material-dominant-entity) — Steel beam in bridge construction

### `min:Process`

- Event/transformative actual entity
- Uses nexus entities as input, produces nexus entities as output, can generate data
- Structural axiom: at least one `hasInput` and one `hasOutput` (range: `min:Nexus`)
- Example: [`examples/process.ttl`](examples.md#process-transformation-and-event) — Laser welding in automotive manufacturing

### `min:Data`

- Informational artifact in the actual branch
- Has physical realization (bytes/storage), but semantics is primary
- Encodes formal entities via `min:encodes`
- Example: [`examples/data.ttl`](examples.md#data-informational-artifact) — Vibration measurement data (wind turbine)

### `min:Agent`

- Acting entity with selective, attributable effects
- May overlap with object/process/data roles
- Structural axiom: at least one `performs` relation to a process
- Example: [`examples/agent.ttl`](examples.md#agent-acting-entity) — Cobot, human worker, software agent

### `min:Boundary`

- Irreducibly relational nexus phenomenon (exists only between partner nexus entities)
- Structural axiom: at least two `bounds` relations to nexus entities
- Typical examples: transition resistance, grain boundary, thermal contact resistance

### `min:Forma`

- Root of formal entities
- Existence criterion: constitutive determination
- Not causally effective itself
- Not intended for direct instantiation

### `min:Lex`

- Formal law-like regularity (e.g., conservation laws)
- Constrains and governs actual entities/processes
- Realized by nexus entities/processes
- Example: [`examples/lex.ttl`](examples.md#lex-law-like-regularity) — Hooke's Law in a spring test

### `min:Structura`

- Formal mathematical/model structure
- Formalizes actual systems/processes
- Distinct from data artifacts implementing the structure
- Example: [`examples/structura.ttl`](examples.md#structura-mathematical-structure) — Euler-Bernoulli beam theory

### `min:Possibile`

- Possibility or counterfactual scenario
- Concerns actual entities but is itself non-actual
- Useful for risk and what-if modeling
- Example: [`examples/possibile.ttl`](examples.md#possibile-possibility-and-counterfactual) — Fatigue crack scenario (offshore wind)

### `min:Norma`

- Normative requirement/evaluation criterion
- Evaluates actual entities/processes
- Distinct from documents encoding the norm
- Example: [`examples/norma.ttl`](examples.md#norma-normative-requirement) — Maximum deflection (Eurocode)

### `min:Institutio`

- Institutionally constituted entity
- Exists via collective recognition and constitutive acts
- Linked to agents through constitution/recognition relations
- Example: [`examples/institutio.ttl`](examples.md#institutio-institutional-construct) — ISO 9001 certification

## Disjointness axioms

- `min:Object`, `min:Process`, `min:Data`, `min:Boundary` are disjoint
- `min:Agent` is intentionally not disjoint from them
- `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio` are pairwise disjoint
- `min:Nexus` and `min:Forma` are disjoint

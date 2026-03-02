# MIN Class Catalog (v3.0.0)

This page lists **all classes** defined in `min.ttl` for MIN v3.0.0.

## Complete class list

| Class | Parent | Branch | Role |
| --- | --- | --- | --- |
| `min:Entity` | - | Root | Absolute top class |
| `min:Nexus` | `min:Entity` | Actual | Root of causally effective entities |
| `min:Object` | `min:Nexus` | Actual | Material-dominant entity |
| `min:Process` | `min:Nexus` | Actual | Transformation/event entity |
| `min:Data` | `min:Nexus` | Actual | Informational artifact |
| `min:Agent` | `min:Nexus` | Actual | Acting/selective entity |
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

### `min:Process`

- Event/transformative actual entity
- Uses objects as input, produces objects as output, can generate data
- Structural axiom: at least one `hasInput` and one `hasOutput`

### `min:Data`

- Informational artifact in the actual branch
- Has physical realization (bytes/storage), but semantics is primary
- Encodes formal entities via `min:encodes`

### `min:Agent`

- Acting entity with selective, attributable effects
- May overlap with object/process/data roles
- Structural axiom: at least one `performs` relation to a process

### `min:Forma`

- Root of formal entities
- Existence criterion: constitutive determination
- Not causally effective itself
- Not intended for direct instantiation

### `min:Lex`

- Formal law-like regularity (e.g., conservation laws)
- Constrains and governs actual entities/processes
- Realized by nexus entities/processes

### `min:Structura`

- Formal mathematical/model structure
- Formalizes actual systems/processes
- Distinct from data artifacts implementing the structure

### `min:Possibile`

- Possibility or counterfactual scenario
- Concerns actual entities but is itself non-actual
- Useful for risk and what-if modeling

### `min:Norma`

- Normative requirement/evaluation criterion
- Evaluates actual entities/processes
- Distinct from documents encoding the norm

### `min:Institutio`

- Institutionally constituted entity
- Exists via collective recognition and constitutive acts
- Linked to agents through constitution/recognition relations

## Disjointness axioms

- `min:Object`, `min:Process`, `min:Data` are disjoint
- `min:Agent` is intentionally not disjoint from them
- `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio` are pairwise disjoint
- `min:Nexus` and `min:Forma` are disjoint

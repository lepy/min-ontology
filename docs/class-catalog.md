# MIN Class Catalog (v3.3.0)

This catalog reflects the classes in `min.ttl` / `min-v3.3.0.ttl`.

## Complete class list

| Class | Parent | Branch | Direct instantiation | Core role |
| --- | --- | --- | --- | --- |
| `min:Entity` | - | Root | No (conceptual root) | Absolute root of MIN |
| `min:Nexus` | `min:Entity` | Nexus | No (branch root) | Actual, causally effective entities |
| `min:Object` | `min:Nexus` | Nexus | Yes | Material-dominant entity |
| `min:Process` | `min:Nexus` | Nexus | Yes | Transformation/event entity |
| `min:Data` | `min:Nexus` | Nexus | Yes | Informational artifact |
| `min:Agent` | `min:Nexus` | Nexus | Yes | Selectively acting entity |
| `min:Boundary` | `min:Nexus` | Nexus | Yes | Irreducibly relational boundary phenomenon |
| `min:Forma` | `min:Entity` | Forma | No (branch root) | Formal determinants |
| `min:Lex` | `min:Forma` | Forma | Yes | Law-like regularity |
| `min:Structura` | `min:Forma` | Forma | Yes | Mathematical/formal structure |
| `min:Possibile` | `min:Forma` | Forma | Yes | Possibility/counterfactual |
| `min:Norma` | `min:Forma` | Forma | Yes | Normative requirement |
| `min:Institutio` | `min:Forma` | Forma | Yes | Institutional construct |
| `min:Typus` | `min:Forma` | Forma | Yes | Essential type determination |

## Hierarchy

```text
Entity
|- Nexus
|  |- Object
|  |- Process
|  |- Data
|  |- Agent
|  `- Boundary
`- Forma
   |- Lex
   |- Structura
   |- Possibile
   |- Norma
   |- Institutio
   `- Typus
```

## Per-class details

### `min:Entity`

- Role: absolute ontology root.
- Formal axiom: `Entity ≡ Nexus ⊔ Forma`.
- Structural axiom: at least one identifier (`min:hasIdentifier minCardinality 1`).
- Modeling note: use as abstraction, not as direct instance type.

### `min:Nexus`

- Role: root for actual, causally effective entities.
- Design criterion: if it makes a causal difference in the world, it belongs in Nexus.
- Modeling note: instantiate one of its subclasses (`Object`, `Process`, `Data`, `Agent`, `Boundary`).

### `min:Object`

- Role: material-dominant actual entity.
- Identity criterion: material continuity.
- Key relations: `undergoes`, `hasComponent`, `actsOn`/`affectedBy`, `hasBoundary`, `typifiedBy`.
- Example: [Object section](examples.md#object-material-dominant-entity).

### `min:Process`

- Role: transformation/event entity.
- Structural axioms: at least one `hasInput` (from `Nexus`) and one `hasOutput` (to `Nexus`).
- Key relations: `hasInput`, `hasOutput`, `performedBy`, `generates`, `governed` via `Lex`.
- Example: [Process section](examples.md#process-transformation-and-event).

### `min:Data`

- Role: informational artifact in the actual branch.
- Identity criterion: informational identity.
- Key relations: `describes`, `generatedBy`, `encodes` (bridge to Forma).
- Example: [Data section](examples.md#data-informational-artifact).

### `min:Agent`

- Role: selectively acting and attributable entity.
- Structural axiom: at least one `performs` relation to a `Process`.
- Key relations: `performs`, `controls`, `actsOn`, `owns`, `constitutes`, `recognizes`.
- Example: [Agent section](examples.md#agent-acting-entity).

### `min:Boundary`

- Role: irreducibly relational nexus phenomenon.
- Structural axiom: minimum two `bounds` links.
- Key relations: `bounds` / `hasBoundary`.
- Example: [Boundary section](examples.md#boundary-friction-as-irreducibly-relational-nexus).

### `min:Forma`

- Role: root for formal determinants.
- Design criterion: does not act causally; determines validity/structure/possibility.
- Modeling note: instantiate one of its subclasses (`Lex`, `Structura`, `Possibile`, `Norma`, `Institutio`, `Typus`).

### `min:Lex`

- Role: law-like regularity.
- Key relations: `governs` (Process), `constrains` (Nexus), `realizedBy`.
- Example: [Lex section](examples.md#lex-law-like-regularity).

### `min:Structura`

- Role: mathematical/formal structure.
- Key relations: `formalizes` (Nexus), `realizedBy`.
- Example: [Structura section](examples.md#structura-mathematical-structure).

### `min:Possibile`

- Role: possibility/counterfactual scenario.
- Key relations: `concerns`, `alternativeTo`, `realizedBy` (when realized).
- Example: [Possibile section](examples.md#possibile-possibility-and-counterfactual).

### `min:Norma`

- Role: normative requirement and evaluation criterion.
- Key relations: `evaluates`, `constrains`, `encodedBy`.
- Example: [Norma section](examples.md#norma-normative-requirement).

### `min:Institutio`

- Role: institutionally constituted entity.
- Key relations: `constitutedBy`, `recognizedBy` (inverse direction from Agent relations).
- Example: [Institutio section](examples.md#institutio-institutional-construct).

### `min:Typus`

- Role: essential determination of what kind of Nexus something is.
- Key relations: `typifies` / `typifiedBy` (inverse pair), `constrains` (superproperty path).
- Typical use: classify Object/Process/Data/Agent/Boundary instances by type.
- Example: [Typus section](examples.md#typus-essential-determination).

## Disjointness and overlap rules

- `min:Object`, `min:Process`, `min:Data`, `min:Boundary` are pairwise disjoint.
- `min:Agent` is intentionally not disjoint from those Nexus subclasses.
- `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio`, `min:Typus` are pairwise disjoint.
- `min:Nexus` and `min:Forma` are disjoint.

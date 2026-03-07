# MIN Class Catalog (v3.7.1)

This catalog reflects the classes in `min.ttl` / `min-v3.7.1.ttl`.

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
   `- Institutio
```

## Per-class details

### `min:Entity`

- Role: absolute ontology root.
- Formal axiom: `Entity ≡ Nexus ⊔ Forma`.
- Structural axiom: at least one identifier (`min:hasIdentifier minCardinality 1`).

### `min:Nexus`

- Role: root for actual, causally effective entities.
- Modeling note: instantiate one of its subclasses (`Object`, `Process`, `Data`, `Agent`, `Boundary`).

### `min:Object`

- Role: material-dominant actual entity.
- Key relations: `undergoes`, `hasComponent`, `actsOn`/`affectedBy`, `hasBoundary`, `typifiedBy`.
- Example: [Object section](examples.md#object-material-dominant-entity).

### `min:Process`

- Role: transformation/event entity.
- Structural axioms: at least one `hasInput` and one `hasOutput`.
- Example: [Process section](examples.md#process-transformation-and-event).

### `min:Data`

- Role: informational artifact in the actual branch.
- Key relations: `describes`, `generatedBy`, `encodes`.
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
- Modeling note: instantiate one of its subclasses (`Lex`, `Structura`, `Possibile`, `Norma`, `Institutio`).

### `min:Lex`

- Role: law-like regularity.
- Key relations: `governs`, `constrains`, `realizedBy`, `originatedBy`.
- Example: [Lex section](examples.md#lex-law-like-regularity).

### `min:Structura`

- Role: mathematical/formal structure.
- Key relations: `formalizes`, `realizedBy`, `originatedBy`.
- Example: [Structura section](examples.md#structura-mathematical-structure).

### `min:Possibile`

- Role: possibility/counterfactual scenario.
- Key relations: `concerns`, `alternativeTo`, `realizedBy` (when realized).
- Example: [Possibile section](examples.md#possibile-possibility-and-counterfactual).

### `min:Norma`

- Role: normative requirement and evaluation criterion.
- Key relations: `evaluates`, `constrains`, `encodedBy`, `originatedBy`.
- Example: [Norma section](examples.md#norma-normative-requirement).

### `min:Institutio`

- Role: institutionally constituted formal entity.
- Key relations: `constitutedBy`, `recognizedBy`, `typifies`, `comprises`.
- Example: [Institutio section](examples.md#institutio-institutional-construct).

## Disjointness and overlap rules

- `min:Object`, `min:Process`, `min:Data`, `min:Boundary` are pairwise disjoint.
- `min:Agent` is intentionally not disjoint from those Nexus subclasses.
- `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio` are pairwise disjoint.
- `min:Nexus` and `min:Forma` are disjoint.

## Migration note from v3.4

- `min:Typus` is removed as class in v3.5.
- Typification remains available via `min:typifies` / `min:typifiedBy` with domain/range centered on `min:Institutio`.

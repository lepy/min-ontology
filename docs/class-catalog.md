# MIN Class Catalog (v1.0.0)

This catalog reflects the classes in `min.ttl` / `min-v1.0.0.ttl`.

## Complete class list

| Class | Parent | Branch | Direct instantiation | Core role |
| --- | --- | --- | --- | --- |
| `min:Entity` | - | Root | No (conceptual root) | Absolute root of MIN |
| `min:Nexus` | `min:Entity` | Nexus | No (branch root) | Actual, causally effective entities |
| `min:Object` | `min:Nexus` | Nexus | Yes | materielle Persistenz |
| `min:Process` | `min:Nexus` | Nexus | Yes | Veränderung |
| `min:Data` | `min:Nexus` | Nexus | Yes | informationelles Artefakt |
| `min:Agent` | `min:Entity` | Cross-category | Yes | selektive Handlungsfähigkeit |
| `min:Boundary` | `min:Nexus` | Nexus | Yes | Grenzphänomene |
| `min:Forma` | `min:Entity` | Forma | No (branch root) | Formal determinants |
| `min:Lex` | `min:Forma` | Forma | Yes | universelle Gültigkeit |
| `min:Structura` | `min:Forma` | Forma | Yes | formale Struktur |
| `min:Possibile` | `min:Forma` | Forma | Yes | Möglichkeitsraum |
| `min:Norma` | `min:Forma` | Forma | Yes | Anforderung |
| `min:Institutio` | `min:Forma` | Forma | Yes | kollektive Anerkennung |

## Hierarchy

```text
Entity ("Das, was existiert.")
├── Nexus ("Das, was etwas bewirkt.")
│   ├── Object ("Das, was da ist.")
│   ├── Process ("Das, was geschieht.")
│   ├── Data ("Das, was beschreibt.")
│   └── Boundary ("Das, was dazwischen entsteht.")
├── Forma ("Das, was bestimmt.")
│   ├── Lex ("Das, was immer gilt.")
│   ├── Structura ("Das, was die Wirklichkeit formalisiert.")
│   ├── Possibile ("Das, was sein könnte.")
│   ├── Norma ("Das, was gelten soll.")
│   └── Institutio ("Das, was anerkannt wird.")
└── Agent ("Das, was handelt.")
```

## Per-class details

### `min:Entity`

- Role: absolute ontology root.
- Formal axiom: `Entity ≡ Nexus ⊔ Forma`.
- Structural axiom: at least one identifier (`min:hasIdentifier minCardinality 1`).

### `min:Nexus`

- Role: root for actual, causally effective entities.
- Modeling note: instantiate one of its subclasses (`Object`, `Process`, `Data`, `Boundary`).

### `min:Object`

- Role: materielle Persistenz — "Das, was da ist."
- Key relations: `undergoes`, `hasComponent`, `actsOn`/`affectedBy`, `hasBoundary`, `typifiedBy`.
- Example: [Object section](examples.md#object-material-dominant-entity).

### `min:Process`

- Role: Veränderung — "Das, was geschieht."
- Structural axioms: at least one `hasInput` and one `hasOutput`.
- Example: [Process section](examples.md#process-transformation-and-event).

### `min:Data`

- Role: informationelles Artefakt — "Das, was beschreibt."
- Key relations: `describes`, `generatedBy`, `encodes`.
- Example: [Data section](examples.md#data-informational-artifact).

### `min:Agent`

- Role: selektive Handlungsfähigkeit — "Das, was handelt."
- Structural axioms: at least one `performs` relation to a `Process`; must be co-typed as `Nexus` or `Forma`.
- Key relations: `performs`, `controls`, `actsOn`, `owns`, `constitutes`, `recognizes`.
- Example: [Agent section](examples.md#agent-acting-entity).

### `min:Boundary`

- Role: Grenzphänomene — "Das, was dazwischen entsteht."
- Structural axiom: minimum two `bounds` links.
- Key relations: `bounds` / `hasBoundary`.
- Example: [Boundary section](examples.md#boundary-friction-as-irreducibly-relational-nexus).

### `min:Forma`

- Role: root for formal determinants.
- Modeling note: instantiate one of its subclasses (`Lex`, `Structura`, `Possibile`, `Norma`, `Institutio`).

### `min:Lex`

- Role: universelle Gültigkeit — "Das, was immer gilt."
- Key relations: `governs`, `constrains`, `realizedBy`, `originatedBy`.
- Example: [Lex section](examples.md#lex-law-like-regularity).

### `min:Structura`

- Role: formale Struktur — "Das, was die Wirklichkeit formalisiert."
- Key relations: `formalizes`, `realizedBy`, `originatedBy`.
- Example: [Structura section](examples.md#structura-mathematical-structure).

### `min:Possibile`

- Role: Möglichkeitsraum — "Das, was sein könnte."
- Key relations: `concerns`, `alternativeTo`, `realizedBy` (when realized).
- Example: [Possibile section](examples.md#possibile-possibility-and-counterfactual).

### `min:Norma`

- Role: Anforderung — "Das, was gelten soll."
- Key relations: `evaluates`, `constrains`, `encodedBy`, `originatedBy`.
- Example: [Norma section](examples.md#norma-normative-requirement).

### `min:Institutio`

- Role: kollektive Anerkennung — "Das, was anerkannt wird."
- Key relations: `constitutedBy`, `recognizedBy`, `typifies`, `comprises`.
- Example: [Institutio section](examples.md#institutio-institutional-construct).

## Disjointness and overlap rules

- `min:Object`, `min:Process`, `min:Data`, `min:Boundary` are pairwise disjoint.
- `min:Agent` is intentionally not disjoint from those Nexus subclasses and can overlap with `min:Institutio`.
- `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio` are pairwise disjoint.
- `min:Nexus` and `min:Forma` are disjoint.


# MIN Model (v3.3.0)

This page summarizes the current conceptual architecture and modeling rules in MIN.

## 1. Core architecture

MIN has an explicit partition under `min:Entity`:

- `min:Nexus`: actual, causally effective entities
- `min:Forma`: formal, constitutively determining entities

Formal axiom:

- `min:Entity owl:equivalentClass [ owl:unionOf ( min:Nexus min:Forma ) ]`

![min_hierarchy.svg](min_hierarchy.svg)

## 2. Why this split matters

The architecture separates artifacts from determinants:

- `min:Data` is an actual artifact (bytes, files, ownership, lifecycle)
- `min:Forma` is not an artifact (law, norm, type, structure, possibility, institution)

Typical pattern:

- Data node stores/communicates knowledge
- Forma node captures what that knowledge is about
- Bridge via `min:encodes`

## 3. Nexus branch (actual)

Classes:

- `min:Nexus` (root)
- `min:Object`
- `min:Process`
- `min:Data`
- `min:Agent`
- `min:Boundary`

Key structural constraints:

- `min:Process` has at least one `hasInput` and one `hasOutput` (range `min:Nexus`)
- `min:Agent` has at least one `performs`
- `min:Boundary` has at least two `bounds`

Disjointness:

- `Object`, `Process`, `Data`, `Boundary` are pairwise disjoint
- `Agent` intentionally overlaps with them (for dual typing)

## 4. Forma branch (formal)

Classes:

- `min:Forma` (root)
- `min:Lex`
- `min:Structura`
- `min:Possibile`
- `min:Norma`
- `min:Institutio`
- `min:Typus`

Disjointness:

- The six Forma subclasses are pairwise disjoint
- `min:Nexus` and `min:Forma` are disjoint

## 5. Bridge relations (Nexus <-> Forma)

General bridge:

- `realizes` / `realizedBy`

Forma-to-Nexus specialization:

- `constrains`
- `governs` (`Lex -> Process`)
- `formalizes` (`Structura -> Nexus`)
- `evaluates` (`Norma -> Nexus`)
- `concerns` and `alternativeTo` (`Possibile -> Nexus`)
- `typifies` / `typifiedBy` (`Typus <-> Nexus`)

Agent-to-institution bridge:

- `constitutes` / `constitutedBy`
- `recognizes` / `recognizedBy`

Data-to-forma bridge:

- `encodes` / `encodedBy`

## 6. Identity semantics for process modeling

MIN distinguishes two modeling modes:

- Transformative: `hasInput` / `hasOutput` represent new entities (new identity)
- Conservative: `undergoes` / `resultOf` represent persistence through change (same identity)

## 7. Property polarity (schema level)

Polarity is modeled on property definitions (not on blank-node wrappers):

- `min:materialProperty`
- `min:informationalProperty`

Domain properties should declare `rdfs:subPropertyOf` one of these two.

## 8. Practical modeling rules

1. If it acts causally, start in the `Nexus` branch.
2. If it determines validity/type/structure/possibility without causal action, use `Forma`.
3. Keep artifacts in `Data` and connect to formal meaning with `encodes`.
4. Use `Typus` for kind-of determination ("what it is"), not `Norma` ("what it should satisfy").
5. Model relational phenomena like friction/contact resistance as `Boundary`, not as single-object properties.

## 9. OWL-DL and inverse completeness

Current model characteristics:

- Polarity super-properties are `owl:AnnotationProperty` (OWL-DL compatible)
- 12 inverse object-property pairs are explicitly declared
- Branch disjointness and class partition are represented as OWL axioms

## 10. Backward compatibility

- Nexus-centric v2-style instance modeling remains valid in v3.x.
- v3 adds explicit formal semantics (`Forma` branch and bridge relations) without removing core Nexus patterns.


```mermaid
graph TD
    Entity["<b>Entity</b><br/><small>∃hasIdentifier ≥ 1</small>"]
    
    Nexus["<b>Nexus</b><br/><small>kausale Wirksamkeit</small>"]
    Forma["<b>Forma</b><br/><small>konstitutive Bestimmung</small>"]

    Object["Object"]
    Process["Process"]
    Data["Data"]
    Agent["Agent"]
    Boundary["Boundary"]

    Lex["Lex"]
    Structura["Structura"]
    Possibile["Possibile"]
    Norma["Norma"]
    Institutio["Institutio"]
    Typus["Typus"]

    Entity --> Nexus
    Entity --> Forma

    Nexus --> Object
    Nexus --> Process
    Nexus --> Data
    Nexus -.-> Agent
    Nexus --> Boundary

    Forma --> Lex
    Forma --> Structura
    Forma --> Possibile
    Forma --> Norma
    Forma --> Institutio
    Forma --> Typus

    style Entity fill:#f0ebe3,stroke:#9c8b75,color:#3d3225,stroke-width:2px
    style Nexus fill:#d6eaf8,stroke:#2e86c1,color:#1a3c5e,stroke-width:2px
    style Forma fill:#e8daef,stroke:#7d3c98,color:#4a235a,stroke-width:2px
    
    style Object fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Process fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Data fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Boundary fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Agent fill:#fdebd0,stroke:#e67e22,color:#7e4a12,stroke-width:2px,stroke-dasharray: 5 5

    style Lex fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Structura fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Possibile fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Norma fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Institutio fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Typus fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
```
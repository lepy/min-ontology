# MIN Model (v1.0.0)

This page summarizes the current conceptual architecture and modeling rules in MIN.

## 1. Core architecture

MIN has an explicit partition under `min:Entity` with these core definitions:

- `Entity · eindeutige Referenzierbarkeit · "Das, was existiert."`
- `Nexus · kausale Wirksamkeit · "Das, was etwas bewirkt."`
- `Forma · konstitutive Bestimmung · "Das, was bestimmt."`
- `Agent · selektive Handlungsfähigkeit · "Das, was handelt."`

Formal axiom:

- `min:Entity owl:equivalentClass [ owl:unionOf ( min:Nexus min:Forma ) ]`

## 2. Why this split matters

The architecture separates artifacts from determinants:

- `min:Data` is an actual artifact (files, storage, ownership, lifecycle)
- `min:Forma` is not an artifact (law, structure, possibility, norm, institution)

Typical pattern:

- Data node stores/communicates knowledge
- Forma node captures what that knowledge is about
- Bridge via `min:encodes`

## 3. Nexus branch (actual)

Classes:

- `min:Nexus` (root)
- `min:Object` · materielle Persistenz · "Das, was da ist."
- `min:Process` · Veränderung · "Das, was geschieht."
- `min:Data` · informationelles Artefakt · "Das, was beschreibt."
- `min:Boundary` · Grenzphänomene · "Das, was dazwischen entsteht."

Key structural constraints:

- `min:Process` has at least one `hasInput` and one `hasOutput`
- `min:Boundary` has at least two `bounds`

Disjointness:

- `Object`, `Process`, `Data`, `Boundary` are pairwise disjoint
- `Agent` is not part of this disjointness set

## 3b. Agent as "Das, was handelt."

- `min:Agent` is a direct subclass of `min:Entity` in v1.0.
- Structural constraints: at least one `performs`; co-typing with `Nexus` or `Forma` is required.
- Typical co-typing patterns: `Agent ∩ Object`, `Agent ∩ Data`, `Agent ∩ Process`, `Agent ∩ Institutio`.

## 4. Forma branch (formal)

Classes:

- `min:Forma` (root)
- `min:Lex` · universelle Gültigkeit · "Das, was immer gilt."
- `min:Structura` · formale Struktur · "Das, was die Wirklichkeit formalisiert."
- `min:Possibile` · Möglichkeitsraum · "Das, was sein könnte."
- `min:Norma` · Anforderung · "Das, was gelten soll."
- `min:Institutio` · kollektive Anerkennung · "Das, was anerkannt wird."

Disjointness:

- The five Forma subclasses are pairwise disjoint
- `min:Nexus` and `min:Forma` are disjoint

## 5. Bridge relations (Nexus <-> Forma)

Three generic bridge relations:

- `originates` / `originatedBy`: Nexus brings new Forma into existence
- `constrains`: Forma restricts what Nexus can be/do
- `realizes` / `realizedBy`: Nexus makes existing Forma actual

Specialized bridge relations:

- `governs` (`Lex -> Process`)
- `formalizes` (`Structura -> Nexus`)
- `evaluates` (`Norma -> Nexus`)
- `concerns` and `alternativeTo` (`Possibile -> Nexus`)
- `constitutes` / `constitutedBy` (`Agent <-> Institutio`)
- `recognizes` / `recognizedBy` (`Agent <-> Institutio`)
- `encodes` / `encodedBy` (`Data <-> Forma`)
- `typifies` / `typifiedBy` (`Institutio <-> Nexus`)
- `comprises` (`Institutio -> Forma`)

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
2. If it determines validity/structure/possibility without causal action, use `Forma`.
3. Keep artifacts in `Data` and connect to formal meaning with `encodes`.
4. Use `typifies` for kind-of determination via institutionalized types (`Institutio`).
5. Model relational phenomena like friction/contact resistance as `Boundary`, not as single-object properties.

## 9. OWL-DL and inverse completeness

Current model characteristics:

- Polarity super-properties are `owl:AnnotationProperty` (OWL-DL compatible)
- 13 inverse object-property pairs are explicitly declared
- Branch disjointness and class partition are represented as OWL axioms

## 10. Typification note

- `min:Typus` class is not part of the current model.
- Typification remains in the model via `min:Institutio` + `min:typifies`.
- `originates` / `originatedBy` are introduced as generic Forma-genesis relation.

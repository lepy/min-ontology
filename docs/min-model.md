# MIN Model (v3.3.0)

This page describes the conceptual architecture and modeling rules of MIN.

## 1. High-level architecture

MIN v3 introduces a strict two-branch ontology under `min:Entity`.
As of v3.2+, `min:Boundary` is part of the Nexus branch:

- `min:Nexus`: actual entities (causal efficacy criterion)
- `min:Forma`: formal entities (constitutive determination criterion)

This separation is the central design move in v3.

## 2. Why the split matters

In v2.x, many formal concepts were modeled as `min:Data`.  
In v3, this ambiguity is removed:

- `min:Data` is an **actual artifact** (bytes, storage, owner)
- `min:Forma` is **not an artifact** but a formal determinant

Example:

- DIN PDF document -> `min:Data`
- Requirement encoded by that document -> `min:Norma`

## 3. Nexus branch (actual)

Core classes:

- `min:Nexus` (branch root)
- `min:Object`
- `min:Process`
- `min:Data`
- `min:Agent`
- `min:Boundary`

Structural constraints:

- `min:Object`, `min:Process`, `min:Data`, `min:Boundary` are disjoint
- `min:Agent` is intentionally **not** disjoint from those classes
- `min:Boundary` has at least two `min:bounds` links to nexus instances
- `min:Process` has existential restrictions to at least one input and one output nexus
- `min:Agent` has existential restriction to perform at least one process

## 4. Forma branch (formal)

Core classes:

- `min:Forma` (branch root)
- `min:Lex`
- `min:Structura`
- `min:Possibile`
- `min:Norma`
- `min:Institutio`

Structural constraints:

- The five Forma subclasses are pairwise disjoint
- `min:Nexus` and `min:Forma` are disjoint
- Forma has no material/informational polarity split on instance properties

## 5. Property polarity

Polarity is represented at schema level only:

- `min:materialProperty`
- `min:informationalProperty`

Domain-specific properties should be declared as subproperties of one of these
super-properties. This keeps instance graphs flat and queryable without blank-node
indirection.

## 6. Relation families

Nexus-internal relations:

- Process/Nexus: `hasInput`, `hasOutput`, `undergoes`, `resultOf`
- Agent/Process: `performs`, `performedBy`, `controls`
- Agent/Object: `actsOn`, `affectedBy`, `owns`, `produces`
- Data links: `describes`, `describedBy`, `generates`, `generatedBy`
- Boundary links: `bounds`, `hasBoundary`
- Structural links: `nexusWith`, `hasComponent`

Nexus/Forma bridge relations:

- Realization/model links: `realizes`, `realizedBy`, `formalizes`
- Law/constraint links: `constrains`, `governs`
- Norm/risk links: `evaluates`, `concerns`, `alternativeTo`
- Institutional links: `constitutes`, `recognizes`
- Encoding links: `encodes`, `encodedBy`

## 7. Modeling playbook

Use these rules for stable modeling outcomes:

1. If it acts causally in the world, model as `min:Nexus` branch.
2. If it determines validity/possibility/structure without causal action, model as `min:Forma` branch.
3. If it is a representation (file, report, model artifact), keep it in `min:Data` and link with `min:encodes`.
4. Put domain semantics in subproperties, not in instance-level reification patterns.

## 8. Anti-patterns to avoid

- Do not model laws/norms as `min:Data`.
- Do not add blank-node wrappers for polarity.
- Do not collapse institution and actor into one node (e.g. legal entity as both `Agent` and `Institutio` without explicit semantics).

## 9. Formal axioms (v3.1.0+)

MIN v3.1 adds the following formal axioms to strengthen OWL-DL compatibility:

- **Entity partition**: `min:Entity owl:equivalentClass [ owl:unionOf ( min:Nexus min:Forma ) ]`.
  Every Entity is either a Nexus or a Forma. This makes the two-branch architecture a formal
  OWL axiom, not just a modeling convention.

- **OWL-DL polarity**: `min:materialProperty` and `min:informationalProperty` are typed as
  `owl:AnnotationProperty` (previously `rdf:Property`). This keeps MIN in OWL-DL rather than
  OWL Full, since domain-specific datatype properties declared as `rdfs:subPropertyOf` an
  annotation property do not violate the OWL-DL property hierarchy.

- **10 inverse property pairs**: All directional relations have formally declared inverses,
  including the new `min:constitutedBy` (inverse of `min:constitutes`) and `min:recognizedBy`
  (inverse of `min:recognizes`).

- **Boundary axioms (v3.2.0)**: `min:Boundary` is a dedicated Nexus category with
  cardinality constraint `min 2 min:bounds`, and `bounds` / `hasBoundary` are declared
  as inverse properties.

## 10. Backward compatibility

MIN v3 keeps v2.1 Nexus semantics stable:

- Existing Nexus-centric queries remain valid.
- Forma is additive for users who need formal semantics.
- OPA remains obsolete as separate active layer since `v2.0.0`.

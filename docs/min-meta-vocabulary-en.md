# MIN Meta — Self-Describing Documentation Vocabulary

**Ontology IRI:** `https://w3id.org/min/meta`  
**Version:** 1.0.0  
**Version IRI:** `https://w3id.org/min/meta/1.0.0`  
**Imports:** MIN v3.3.0 (`https://w3id.org/min/3.3.0`)  
**Author:** Dr. Ingolf Lepenies  
**Date:** 2026-03-05  
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> Historical note: this page documents the v3.3/v3.4 meta-vocabulary state and includes `Typus` examples.
> In MIN v3.7.1, `min:Typus` was removed as class.

---

## Purpose

MIN Meta defines the annotation properties used to structurally document any ontology entity — classes, properties, individuals — including MIN itself. The vocabulary comprises **11 properties** across **7 irreducible dimensions**.

The design draws inspiration from the Information Artifact Ontology (IAO) in the OBO ecosystem, but is MIN-native, leaner, and self-describing.

## Design Principles

The meta-vocabulary follows four principles:

**Irreducibility** — Each property covers a dimension that no other property can cover. Demonstrated through pairwise `distinguishedFrom` annotations.

**Self-description** — The vocabulary documents itself with itself. Each of the 11 properties is annotated using its own annotations.

**Minimality** — No property whose absence would be tolerable. No property replaceable by a combination of others.

**Universality** — Applicable to classes, properties, and individuals alike.

---

## Dimensions Overview

| No. | Dimension | Guiding Question | Properties |
|-----|-----------|------------------|------------|
| I | Intension | What is it? | `min:definition`, `min:criterion` |
| II | Extension | What does it look like? | `min:usageExample` |
| III | Boundary | What is it not? | `min:counterExample`, `min:distinguishedFrom` |
| IV | Provenance | Where does it come from? | `min:philosophicalBasis`*, `min:normativeSource` |
| V | Teleology | Why does it exist? | `min:rationale` |
| VI | Lifecycle | What state is it in? | `min:definedInVersion`, `min:status`, `min:replacedBy` |
| VII | Axiom Transparency | Why these formal constraints? | `min:axiomRationale` |

\* `min:philosophicalBasis` is already defined in the main MIN module and is only self-described in the meta-vocabulary.

---

## I. Intension — What is the Entity?

### `min:definition`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Definition (de) · definition (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** A natural-language sentence-level definition that describes an ontology entity such that a knowledgeable reader can unambiguously identify it without further sources.

**Criterion:** Could a knowledgeable reader, based solely on this sentence, decide whether a given thing belongs to the class or not?

**Rationale:** Without an explicit definition, the semantics of a class remain implicit in the label and the axiomatics. That suffices for machines, not for humans.

**Distinguished from:** Not to be confused with `rdfs:comment`, which may be informal, unstructured, and redundant. `min:definition` is normative and non-circular.

**Examples:**
- `min:Object min:definition "A thing that is causally efficacious — it can receive or exert effects."@en .`
- `min:Typus min:definition "The bundle of determinations that constitutes a class of Nexus instances. Typus determines WHAT a Nexus counts AS."@en .`

---

### `min:criterion`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Existenzkriterium (de) · criterion (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** An operationalizable yes/no question whose affirmation qualifies an entity as an instance of the annotated class.

**Criterion:** Can the question in principle be answered with yes or no, and does it reliably separate instances from non-instances?

**Rationale:** A definition says what something *is*. A criterion says how one *decides*. Both are irreducible: a good definition can have a bad decision procedure and vice versa.

**Distinguished from:** `min:definition` describes what the class is. `min:criterion` describes how to test membership.

**Counterexample:** "Is the object important?" — too vague, not operationalizable.

**Examples:**
- `min:Process min:criterion "Does the entity consume or transform inputs into outputs over time?"@en .`
- `min:Typus min:criterion "Can one ask: What kind of X is this? — and does the answer provide an essential determination?"@en .`

---

## II. Extension — What Does the Entity Look Like in Practice?

### `min:usageExample`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Verwendungsbeispiel (de) · usage example (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** A concrete example — as a natural-language description or as a Turtle fragment — that shows how the annotated entity is instantiated or used in practice.

**Criterion:** Does the example show a correct, non-trivial usage of the entity in a realistic context?

**Rationale:** Definitions and criteria are abstract. Examples anchor understanding in concrete practice and reduce ambiguity that definitions alone cannot resolve.

**Distinguished from:** `min:counterExample` shows what the entity *is not*. `min:usageExample` shows what it *is*.

**Counterexample:** "e.g. a car" — too unspecific, no usage context visible.

**Example:**
- `min:Agent min:usageExample "ex:Operator_01 a min:Agent ; rdfs:label \"Test engineer Müller\"@en ."@en .`

---

## III. Boundary — What is the Entity Not?

### `min:counterExample`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Gegenbeispiel (de) · counterexample (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** A concrete example of an entity that appears to belong to the annotated class but does not according to its criterion — together with the reasoning why not.

**Criterion:** Would a non-expert plausibly assign the named entity to the class even though it does not belong?

**Rationale:** Definitions and criteria alone leave borderline cases open. Counterexamples make the boundary of the class visible, especially where confusion is likely.

**Distinguished from:** `min:distinguishedFrom` demarcates *classes* from each other. `min:counterExample` names a concrete *thing* that does not belong to the class.

**Example:**
- `min:Agent min:counterExample "A CNC machine is not an Agent because it has no agency — it executes instructions. → min:Object."@en .`

---

### `min:distinguishedFrom`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Abgrenzung (de) · distinguished from (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** An explicit demarcation of the annotated class from a related class that another modeler might confuse or merge.

**Criterion:** Is there a documented risk of confusion between the two classes, and does the demarcation make the difference operationalizable?

**Rationale:** Ontologies grow through multiple contributors. Without explicit demarcations, class boundaries drift apart because each modeler has their own intuition.

**Distinguished from:** `min:counterExample` names a concrete thing. `min:distinguishedFrom` names a *class* and justifies the separation.

**Examples:**
- `min:Data min:distinguishedFrom "min:Object — Data is causally inert (can be copied, deleted without physical effect). Object is causally efficacious."@en .`
- `min:Typus min:distinguishedFrom "min:Norma — Norma EVALUATES (Rm SHALL ≥ 270 MPa). Typus CONSTITUTES (DC04 IS what has C ≤ 0.08% and Rm 270–350 MPa)."@en .`

---

## IV. Provenance — Where Does the Entity Come From?

### `min:philosophicalBasis`

> **Note:** This property is already defined in the main MIN module (`https://w3id.org/min/`). In the meta-vocabulary it is only self-described, not re-declared.

---

### `min:normativeSource`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Normative Quelle (de) · normative source (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** A reference to a published standard, specification, or recognized technical source whose content definition grounds or constrains the semantics of the annotated entity.

**Criterion:** Is the named source a published, citable document that substantively supports the definition of the entity?

**Rationale:** `min:philosophicalBasis` points to the conceptual tradition (Aristotle, Whitehead). But when a class is derived from DIN EN ISO 6892-1, a separate reference to the *technical* source is needed. Philosophical tradition ≠ normative reference.

**Distinguished from:**
- `min:philosophicalBasis` points to philosophical tradition and conceptual history. `min:normativeSource` points to technical or scientific authority sources.
- `dcterms:source` is a generic Dublin Core reference without the restriction to normative, definition-supporting sources.

**Examples:**
- `sdata:TensileTest min:normativeSource "DIN EN ISO 6892-1:2019, Section 3.1"@en .`
- `ex:DC04_typus min:normativeSource "EN 10130:2006, Table 3 — Chemical composition and mechanical properties"@en .`

---

## V. Teleology — Why Does the Entity Exist?

### `min:rationale`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Entwurfsbegründung (de) · design rationale (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** A natural-language justification that explains which concrete modeling problem the annotated entity solves and why no existing entity already covers it.

**Criterion:** Does the text name a concrete modeling problem and explain why no existing entity solves it?

**Rationale:** `min:definition` says *what*, `min:philosophicalBasis` says *where the concept originates* — but neither answers: "Why didn't you just subsume it under X?" Without a rationale, the design decision is lost once the author is no longer available.

**Distinguished from:**
- `min:definition` describes what the entity *is*. `min:rationale` describes why it *must be*.
- `min:philosophicalBasis` places the concept in an intellectual tradition. `min:rationale` places it in the context of the ontology architecture.

**Counterexample:** "Because it's practical" — no justification, no modeling problem named.

**Examples:**
- `min:EnvironmentAgent min:rationale "Natural processes (corrosion, aging) have no intentional agent. Without EnvironmentAgent one would have to create Agent instances for physical laws, diluting the semantics of Agent."@en .`
- `min:Typus min:rationale "MIN v3.2 could express individual determinations but not say: This is a DC04. The essential determination had no ontological home."@en .`

---

## VI. Lifecycle — What State is the Entity In?

### `min:definedInVersion`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Definiert in Version (de) · defined in version (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** The version number (SemVer) of the ontology in which the annotated entity was first introduced.

**Criterion:** Is the value a valid SemVer version number that corresponds to the release in which the entity first appeared?

**Rationale:** In an evolving ontology, users must be able to determine from which version an entity is available — especially for backward compatibility and migration.

**Distinguished from:**
- `min:status` describes the current maturity level. `min:definedInVersion` describes the historical point of introduction.
- `owl:versionInfo` versions the ontology as a whole. `min:definedInVersion` versions individual entities.

---

### `min:status`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Status (de) · status (en) |
| **Range** | `xsd:string` |
| **Allowed values** | `"experimental"` · `"stable"` · `"deprecated"` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** The current maturity level of the annotated entity in the ontology lifecycle. Exactly one of three values: `experimental` (may change), `stable` (committed), `deprecated` (do not use, see `min:replacedBy`).

**Criterion:** Is the value exactly one of the three permitted strings?

**Rationale:** `min:definedInVersion` says *when* an entity was introduced, but not whether it should still be used. Without an explicit status, a user cannot know whether a class is safe to use or about to be removed.

**Distinguished from:**
- `min:definedInVersion` marks a historical point in time. `min:status` describes the *current* state.
- `min:replacedBy` names the successor upon deprecation. `min:status` marks only the state itself.

**Counterexample:** `"beta"` — not a permitted value. The three-way split experimental/stable/deprecated is exhaustive.

---

### `min:replacedBy`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Ersetzt durch (de) · replaced by (en) |
| **Range** | `rdfs:Resource` (URI) |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** A reference to the ontology entity that functionally replaces the annotated (deprecated) entity. The value is a URI, not a string.

**Criterion:** Is the annotated entity deprecated, and does the referenced entity actually provide a functional replacement?

**Rationale:** Deprecation without a migration path is useless. Users need to know *where* to migrate, not just that they must migrate.

**Distinguished from:** `min:status` only marks the state `deprecated`. `min:replacedBy` names the concrete successor.

**Counterexample:** `min:replacedBy` on an entity with `min:status "stable"` — semantically contradictory.

**Example (hypothetical):**
```turtle
min:PhysicalObject min:status "deprecated" ;
    min:replacedBy min:Object .
```

---

## VII. Axiom Transparency — Why These Formal Constraints?

### `min:axiomRationale`

| | |
|---|---|
| **Type** | `owl:AnnotationProperty` |
| **Label** | Axiom-Begründung (de) · axiom rationale (en) |
| **Range** | `xsd:string` |
| **Status** | stable |
| **Since** | 1.0.0 |

**Definition:** A natural-language justification that explains why a specific OWL restriction (domain, range, cardinality, disjointness) was chosen and which modeling alternative was deliberately rejected.

**Criterion:** Does the text name the specific restriction, justify the choice, and name at least one rejected alternative?

**Rationale:** OWL axioms are machine-readable, but their design decisions are not. The recent correction of the Process axioms in MIN (opening for Data inputs alongside Object inputs) demonstrates: without a documented rationale, every successor must reconstruct the design decision from scratch.

**Distinguished from:** `min:rationale` justifies why the *entity* exists. `min:axiomRationale` justifies why a *formal constraint* on the entity was chosen as it was.

**Counterexample:** "Domain is Object because that makes sense." — no justification, no rejected alternative.

**Examples:**
- `min:hasInput min:axiomRationale "Range is min:Entity (not just min:Object) because processes can consume both physical objects and data. The earlier restriction to min:Object was corrected in v3.0.0 as it could not model FEM simulations."@en .`
- `min:typifies min:axiomRationale "typifies is subPropertyOf constrains because typification is a special form of determination. Rejected alternative: standalone top-level bridge relation."@en .`

---

## Demonstration — `min:Typus` with Complete Meta-Documentation

The following class demonstrates how all 11 properties work together to fully document a class.

### Intension

**Definition:** The bundle of determinations that constitutes a class of Nexus instances. Typus determines WHAT a Nexus counts AS — not what it has (Property), not what it should (Norma), but what it IS.

**Criterion:** Can one ask: "What kind of X is this?" — and does the answer provide an essential determination (a bundle of determinations that constitutes the sort/kind)?

### Extension

```turtle
ex:DC04_typus a min:Typus ;
    rdfs:label "DC04"@de ;
    min:hasIdentifier "DC04" ;
    min:typifies ex:blech_042 .
```

### Boundary

**Counterexample:** A SKOS concept "DC04" in a thesaurus. It classifies terminologically but does not determine the essential form — it has no connection to Structura, Lex, Norma. → `skos:Concept`, not `min:Typus`.

**Demarcations:**

| From | Difference |
|------|------------|
| `min:Norma` | Norma EVALUATES (ought). Typus CONSTITUTES (essence). |
| `min:Structura` | Structura is purely formal (a mathematical structure). Typus is composite — it BUNDLES Structura, Norma, Lex, and Properties. |
| `min:Institutio` | Institutio requires ongoing collective recognition. Typus does not — DC04 remains DC04 even if the standards body is dissolved. |
| `min:Lex` | Lex is universal and exceptionless. Typus is contingent — DC04 could have had different limits. |

### Provenance

**Normative sources:** Aristotle: Metaphysics, Book Z (Eidos as essential form). Quine: Natural Kinds (1969). Putnam: The Meaning of "Meaning" (1975). Weber: Objective Possibility and Adequate Causation (1906, ideal type).

### Teleology

MIN v3.2 could express individual determinations (Norma: Rm ≥ 270 MPa; Structura: bcc lattice) but could not say: "This is a DC04." The essential determination had no ontological home. Workarounds were insufficient: OWL class (has classes FOR types but no concept OF typus), SKOS concept (classifies without determining), Norma (codifies the typus but IS NOT the typus).

### Lifecycle

Defined in version **3.3.0**, status **stable**.

### Axiom Transparency

Typus is disjoint with Lex, Structura, Possibile, Norma, Institutio. Typus is composite (bundles other Forma categories), while every other Forma category is atomic. Rejected alternative: Typus as subclass of Norma — but Norma evaluates, Typus constitutes.

`min:typifies` is subPropertyOf `min:constrains`. Typification is a special form of determination. Rejected alternative: standalone top-level bridge relation. But typification IS constraint (to a kind), so it belongs under `constrains`.

---

## Completeness Proof

The meta-vocabulary proves three properties through self-description:

**Expressiveness** — The vocabulary can describe everything it is supposed to describe, including itself.

**Irreducibility** — No property is replaceable by a combination of others (demonstrable through the pairwise `distinguishedFrom` annotations).

**Completeness** — Every documentation question a knowledgeable reader might ask is answered by one of the 11 properties:

| Question | Property |
|----------|----------|
| What is X? | `min:definition` |
| How do I decide? | `min:criterion` |
| What does it look like concretely? | `min:usageExample` |
| What doesn't belong? | `min:counterExample` |
| How does X differ from Y? | `min:distinguishedFrom` |
| What philosophy is X based on? | `min:philosophicalBasis` |
| What standard does X come from? | `min:normativeSource` |
| Why does X exist in MIN? | `min:rationale` |
| Since when does X exist? | `min:definedInVersion` |
| Can I still use X? | `min:status` |
| What should I use instead? | `min:replacedBy` |
| Why does X have this restriction? | `min:axiomRationale` |

---

## Prefix Overview

| Prefix | Namespace |
|--------|-----------|
| `min:` | `https://w3id.org/min/` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` |
| `dcterms:` | `http://purl.org/dc/terms/` |

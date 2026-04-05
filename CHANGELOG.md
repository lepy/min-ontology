# Changelog

All notable changes to MIN are documented in this file.

## [1.1.0] - 2026-04-05

### Added
- `min:Epistemicum` as 6th Forma subclass ("That which is held to be true").
- `min:EpistemicStatus` enum class with 5 individuals: `ES_Hypothetical`, `ES_Confirmed`, `ES_Refuted`, `ES_Contested`, `ES_Axiomatic`.
- `min:ConfidenceType` enum class with 4 individuals: `CT_Subjective`, `CT_Statistical`, `CT_Bayesian`, `CT_Heuristic`.
- 7 new object properties: `holds`/`heldBy` (Agent ↔ Epistemicum), `about` (Epistemicum → Entity), `supportedBy`/`supports`, `underminedBy`/`undermines` (Epistemicum ↔ Nexus).
- 2 new functional object properties: `hasEpistemicStatus` (Epistemicum → EpistemicStatus), `hasConfidenceType` (Epistemicum → ConfidenceType).
- 2 new datatype properties: `hasConfidence` (Epistemicum → xsd:double [0..1], functional), `isQuantifiable` (Possibile → xsd:boolean).
- SHACL: `EpistemicumInstanceShape` with about (required), hasEpistemicStatus (exactly 1), confidence range, supportedBy/underminedBy class constraints.
- SHACL: SPARQL consistency rule — hasConfidence requires hasConfidenceType.
- Example: `examples/epistemic-zugversuch.ttl` — tensile test with both epistemic patterns.
- Documentation: `docs/epistemic-dimension-en.md`, `docs/epistemic-dimension-de.md`, `docs/migration-v1.0-to-v1.1.md`.
- `min-v1.1.0.ttl`: immutable release snapshot.

### Changed
- Forma partition extended: `Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio ⊔ Epistemicum` (**breaking change** — monotone extension, all v1.0.x graphs remain valid).
- Forma `AllDisjointClasses` extended to include `Epistemicum`.
- SHACL core shapes updated: `ClassLabelShape` +3 classes (Epistemicum, EpistemicStatus, ConfidenceType), `ObjectPropertyDomainRangeShape` +9 properties.
- Updated class catalog, property catalog, validation docs to v1.1.0.

### Unchanged
- `min:confirms` and `min:refutes` remain as-is (Process → Forma/Possibile, Popperian pattern).
- `min:supersedes` remains non-transitive.
- `min:EfficacyMode` retains exactly 10 individuals (no EM_Epistemic added).

## [1.0.1] - 2026-04-03

### Changed
- Split ontology into `min.ttl` (axioms only) and `min-docs.ttl` (annotations, philosophy, design rationale).
- Formalized `causalityMode` and `efficacyMode` from string annotations to OWL ObjectProperties with `owl:oneOf` individuals and `owl:hasValue` class restrictions.
- Added `min:CausalityMode` (3 individuals), `min:EfficacyMode` (10 individuals), `min:hasCausalityMode`, `min:hasEfficacyMode`.
- Removed old annotation properties `min:causalityMode` and `min:efficacyMode`.
- Fixed gap: Boundary now has `hasEfficacyMode EM_Relational`.
- All `rdfs:comment` in `min.ttl` now `@en` (was `@de`).
- Closed partitions: `Nexus ≡ Object ⊔ Process ⊔ Data ⊔ Boundary`, `Forma ≡ Lex ⊔ Structura ⊔ Possibile ⊔ Norma ⊔ Institutio`.
- Added `min:constrainedBy` as inverse of `min:constrains`.
- Datatype properties aligned to Dublin Core (`hasIdentifier → dcterms:identifier`, `hasTimestamp → dcterms:date`, `hasDescription → dcterms:description`).
- `min:owns` range widened from `min:Object` to `min:Entity`.
- `min:Agent` and `min:Process` are now disjoint (Agent ∩ Process no longer allowed).
- Moved `MetaTerm`, `OntologyArtifact`, `describesOntologyTerm` from `min.ttl` to `min-docs.ttl`.
- SHACL shapes fully updated: all 49 object properties, Boundary instance shape, all class labels.

### Added
- `min:startedAt`, `min:endedAt` (DatatypeProperties on Process, xsd:dateTime).
- Forma classification guide (decision tree) in class catalog.
- `alignment/min-prov.ttl`: optional PROV-O alignment (Entity, Process, Agent + properties).
- `alignment/min-bfo.ttl`: optional BFO 2020 alignment (Object → material entity, Process → process, Data → GDC).
- `alignment/min-schema.ttl`, `alignment/min-sosa.ttl`, `alignment/min-dolce.ttl`, `alignment/min-qudt.ttl`, `alignment/min-dcterms.ttl`: additional optional interoperability modules.
- `examples/dpp-coil.ttl`: end-to-end DPP use case (coil → deep drawing → part → tensile test).
- `docs/use-case-dpp.md`: use case documentation with SPARQL queries.
- `docs/validation.md`: SHACL shapes documentation.
- `min-v1.0.1.ttl`: immutable release snapshot.
- `min-docs.ttl` imports `min.ttl` via `owl:imports`.
- Removed all references to deprecated class `Typus` (subsumed under `Institutio`).
- Removed undeclared terms from documentation (`influences`, `expresses`, `between`, `EncodedData`, `SelectingAgent`).
- Added `MetaTerm` and `OntologyArtifact` to class catalog.
- Added epistemic relations to property catalog.
- Updated all documentation to v1.0.1.

## [1.0.0] - 2026-03-08

### Changed
- `min.ttl` now points to MIN `v1.0.0`.
- Added immutable release snapshot `min-v1.0.0.ttl`.
- Repository docs, validation script, and version checks updated to `v1.0.0`.

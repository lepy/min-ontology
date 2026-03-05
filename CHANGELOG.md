# Changelog

All notable changes to MIN are documented in this file.

## [3.3.0] - 2026-03-05

### Changed
- `min.ttl` now points to MIN `v3.3.0`.
- Added immutable release snapshot `min-v3.3.0.ttl` and compatibility variant `min_v3.3.0.ttl`.
- Documentation updated to reference `v3.3.0` as current stable release.
- Integrated example scenario promoted to `examples/min-v3.3.0-examples.ttl`.
- Validation updated for `v3.3.0` (`test-min-version.rq`, `scripts/validate.py`).

### Removed
- Separate file `min-meta-vocabulary.ttl` (meta vocabulary terms are no longer maintained as standalone ontology file).

## [3.2.0] - 2026-03-04

### Added
- New Nexus class `min:Boundary` for irreducibly relational, causally effective boundary phenomena.
- New boundary relation pair `min:bounds` / `min:hasBoundary` (inverse properties).
- Boundary cardinality axiom requiring at least two bound Nexus instances.
- New immutable release snapshot `min-v3.2.0.ttl`.

### Changed
- Nexus disjointness set extended to include `min:Boundary` (`Object`, `Process`, `Data`, `Boundary` pairwise disjoint).
- Ontology design rationale extended with explicit criteria and modeling guidance for Boundary vs. Object.
- `min.ttl` now points to MIN `v3.2.0`.

## [3.1.0] - 2026-03-03

### Changed
- `min:hasInput` / `min:hasOutput` range broadened from `min:Object` to `min:Nexus` — any Nexus (Object, Data, Agent) can now be process I/O.
- `min:undergoes` / `min:resultOf` domain broadened from `min:Object` to `min:Nexus`.
- `min:Process` existential restrictions updated: `owl:someValuesFrom min:Nexus` (was `min:Object`).
- Identity semantics documented: `hasInput`/`hasOutput` = transformative (new ID), `undergoes`/`resultOf` = conservative (same ID).
- Identity criteria added to `min:Data` and `min:Agent` comments.

### Fixed
- `min:materialProperty` / `min:informationalProperty` changed from `rdf:Property` to `owl:AnnotationProperty` for OWL-DL compatibility.
- Missing inverse properties `min:constitutedBy` and `min:recognizedBy` declared (used in examples but previously undefined).
- Missing `min:hasOutput` added to `Zugversuch_042` and `Sensorausfall_2026_03` in examples.

### Added
- `min:Entity owl:equivalentClass [ owl:unionOf ( min:Nexus min:Forma ) ]` — exhaustive partition axiom.
- Instance-level SHACL shapes (`shapes/min-instance.shacl.ttl`) for Process, Agent, and Entity.
- 9 per-class example files (`examples/{object,process,data,agent,lex,structura,possibile,norma,institutio}.ttl`).
- 5 new SPARQL regression tests (Forma classes, Entity partition, disjointness, bridge relations, inverse properties).
- 5 new competency queries (cq03–cq07: encodes, governs, evaluates, realizes, constitutes).
- Phase [4/4] Instance-SHACL validation in `scripts/validate.py`.
- Design-decision comment explaining why `dcterms:` is not imported via `owl:imports`.
- Documentation page `docs/examples.md` with per-class modeling guidance.

## [3.0.0] - 2026-03-02

### Changed
- `min.ttl` now points to MIN `v3.0.0`.
- The ontology architecture now has an explicit root `min:Entity` with two branches: `min:Nexus` (actual entities) and `min:Forma` (formal entities).
- New Forma classes were added: `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio`.
- New bridge relations were added between Nexus and Forma (e.g. `min:realizes`, `min:constrains`, `min:governs`, `min:formalizes`, `min:evaluates`, `min:concerns`, `min:constitutes`, `min:recognizes`, `min:encodes`).
- Validation and repository metadata were updated for the v3.0 line.

### Notes
- This is a major release and introduces a breaking conceptual model expansion compared to the 2.x line.

## [2.1.0] - 2026-03-02

### Changed
- `min.ttl` now points to MIN `v2.1.0`.
- Polarität moved from instance blank-node structure (`materialAspect` / `informationalAspect`) to schema-level super-properties (`materialProperty` / `informationalProperty`).
- Validation, examples, and competency queries were updated for the v2.1 model.

### Notes
- OPA remains obsolete for active lines since `v2.0.0`.

## [2.0.0] - 2026-03-01

### Changed
- `min.ttl` now points to MIN `v2.0.0`.
- OPA concepts were absorbed into MIN (no separate `opa.ttl` in active maintenance).
- Validation suite and repository docs were updated to MIN v2 structure.

### Removed
- Active OPA ontology file `opa.ttl`.
- OPA alignment and OPA import test from active validation.

## [1.0.0] - 2026-03-01

### Added
- Initial MIN release (`min.ttl`, `min-v1.0.0.ttl`).
- Initial OPA release (`opa.ttl`, `opa-v1.0.0.ttl`) importing MIN.
- Repository validation framework (SPARQL tests, SHACL shapes, CI workflows).

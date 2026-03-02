# Changelog

All notable changes to MIN are documented in this file.

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

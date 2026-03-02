# Changelog

All notable changes to MIN are documented in this file.

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

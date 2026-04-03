# Changelog

All notable changes to MIN are documented in this file.

## [1.0.1] - 2026-04-03

### Changed
- Split ontology into `min.ttl` (axioms only) and `min-docs.ttl` (annotations, philosophy, design rationale).
- Formalized `causalityMode` and `efficacyMode` from string annotations to OWL ObjectProperties with `owl:oneOf` individuals and `owl:hasValue` class restrictions.
- Added `min:CausalityMode` (3 individuals), `min:EfficacyMode` (10 individuals), `min:hasCausalityMode`, `min:hasEfficacyMode`.
- Removed old annotation properties `min:causalityMode` and `min:efficacyMode`.
- Fixed gap: Boundary now has `hasEfficacyMode EM_Relational`.
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

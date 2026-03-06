# Versioning policy

## Semantic versioning

- Major (`X.0.0`): conceptual or semantic breaks
- Minor (`X.Y.0`): backward-compatible ontology extensions
- Patch (`X.Y.Z`): metadata/docs/non-semantic corrections

## Files

- `min.ttl`: current stable version
- `min-vX.Y.Z.ttl`: immutable snapshot for release `X.Y.Z`
- `min_vX.Y.Z.ttl`: optional compatibility snapshot (underscore naming)
- Current stable line: `3.x` (`min.ttl` -> `v3.4.0`)

## Architecture note

- Since `v2.0.0`, OPA is absorbed into MIN and no separate `opa.ttl` is maintained.

## Release checklist

1. Update `owl:versionIRI` and `owl:versionInfo` in `min.ttl`.
2. Create `min-vX.Y.Z.ttl` from released `min.ttl` (optional: also `min_vX.Y.Z.ttl`).
3. Update validation assets (SPARQL/SHACL/scripts) if semantics changed.
4. Update `CHANGELOG.md` and docs pages.
5. Run full validation (`uv run ontology-validate`).
6. Tag release as `vX.Y.Z`.

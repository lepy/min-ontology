# Versioning policy

## Semantic versioning

- Major (`X.0.0`): breaking semantic changes
- Minor (`1.X.0`): backward-compatible additions
- Patch (`1.0.X`): non-semantic corrections and metadata fixes

## Files

- `min.ttl`: current stable version
- `min-vX.Y.Z.ttl`: immutable snapshot for release `X.Y.Z`

## Release checklist

1. Update `owl:versionIRI` and `owl:versionInfo` in `min.ttl`.
2. Create `min-vX.Y.Z.ttl` from released `min.ttl`.
3. Update `CHANGELOG.md`.
4. Tag release as `vX.Y.Z`.

# MIN Ontology Repository

This repository contains the MIN foundational ontology.

## Canonical ontology IRIs

- MIN ontology IRI: `https://w3id.org/min`
- MIN namespace: `https://w3id.org/min#`
- Current MIN version IRI: `https://w3id.org/min/3.0.0`

## Repository layout

- `min.ttl`: current MIN ontology
- `min-v1.0.0.ttl`: immutable MIN release snapshot
- `min-v2.0.0.ttl`: immutable MIN v2 release snapshot
- `min-v2.1.0.ttl`: immutable MIN v2.1 release snapshot
- `min-v3.0.0.ttl`: immutable MIN v3 release snapshot
- `opa-v1.0.0.ttl`: legacy OPA snapshot (historical reference only)
- `shapes/`: SHACL validation shapes
- `tests/sparql/`: SPARQL ASK checks
- `queries/competency/`: competency queries
- `examples/`: example instance data
- `scripts/validate.py`: local/CI validation entrypoint

## Validation

Recommended: run validation with `uv` (Python is pinned via `.python-version`):

```bash
uv run ontology-validate
```

Optional fallback with `pip`:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

## Documentation (MkDocs)

Build locally:

```bash
uv run mkdocs build --strict
```

Serve locally:

```bash
uv run mkdocs serve
```

Deployment to GitHub Pages is automated via `.github/workflows/docs.yml`
on every push to `main` (and via manual `workflow_dispatch`).

## Versioning policy

- Semantic versioning is used for ontology releases.
- `min-vX.Y.Z.ttl` files are immutable snapshots.
- `min.ttl` always points to the latest stable MIN release.
- Since `v2.0.0`, OPA is absorbed into MIN and no separate `opa.ttl` is maintained.

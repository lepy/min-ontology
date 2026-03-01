# MIN Ontology Repository

This repository contains the MIN foundational ontology and the OPA interpretation layer.

## Canonical ontology IRIs

- MIN ontology IRI: `https://w3id.org/min`
- MIN namespace: `https://w3id.org/min#`
- Current MIN version IRI: `https://w3id.org/min/1.0.0`

## Repository layout

- `min.ttl`: current MIN ontology
- `min-v1.0.0.ttl`: immutable MIN release snapshot
- `opa.ttl`: current OPA ontology (imports MIN)
- `opa-v1.0.0.ttl`: immutable OPA release snapshot
- `alignments/`: explicit mapping files
- `shapes/`: SHACL validation shapes
- `tests/sparql/`: SPARQL ASK checks
- `queries/competency/`: competency queries
- `examples/`: example instance data
- `scripts/validate.py`: local/CI validation entrypoint

## Validation

Install dependencies:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run checks:

```bash
python3 scripts/validate.py
```

## Versioning policy

- Semantic versioning is used for ontology releases.
- `min-vX.Y.Z.ttl` files are immutable snapshots.
- `min.ttl` always points to the latest stable MIN release.

# MIN Ontology

MIN (Material · Information · Nexus) is a foundational ontology for modeling
industrial and scientific domains with a strict distinction between:

- **Entity · eindeutige Referenzierbarkeit · "Das, was existiert."**
- **Nexus · kausale Wirksamkeit · "Das, was etwas bewirkt."**
- **Forma · konstitutive Bestimmung · "Das, was bestimmt."**
- **Agent · selektive Handlungsfähigkeit · "Das, was handelt."**

The current stable release line is **v1.x** (current: **v1.0.0**).

## Canonical IRIs

- Ontology IRI: `https://w3id.org/min`
- Namespace: `https://w3id.org/min#`
- Current version IRI: `https://w3id.org/min/1.0.0`

## Conceptual core (v1.0.0)

MIN v1 defines **13 classes**:

- Root: `min:Entity`
- Actual branch: `min:Nexus`, `min:Object`, `min:Process`, `min:Data`, `min:Boundary`
- Formal branch: `min:Forma`, `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio`
- Agent: `min:Agent` ("Das, was handelt.")

Canonical subclass profiles:

- `Object · materielle Persistenz · "Das, was da ist."`
- `Process · Veränderung · "Das, was geschieht."`
- `Data · informationelles Artefakt · "Das, was beschreibt."`
- `Boundary · Grenzphänomene · "Das, was dazwischen entsteht."`
- `Lex · universelle Gültigkeit · "Das, was immer gilt."`
- `Structura · formale Struktur · "Das, was die Wirklichkeit formalisiert."`
- `Possibile · Möglichkeitsraum · "Das, was sein könnte."`
- `Norma · Anforderung · "Das, was gelten soll."`
- `Institutio · kollektive Anerkennung · "Das, was anerkannt wird."`

For full class definitions, see `docs/class-catalog.md`.

![MIN Class Hierarchy](docs/min_hierarchy.svg)

## Repository structure

- `min.ttl`: current MIN ontology
- `min-v*.ttl`: immutable release snapshots
- `min-v1.0.0.ttl`: current immutable snapshot (hyphen naming)
- `examples/`: example instance graphs
- `examples/min-v1.0.0-examples.ttl`: integrated scenario
- `queries/competency/`: competency queries
- `shapes/`: SHACL shapes
- `tests/sparql/`: SPARQL ASK regression checks
- `scripts/validate.py`: local/CI validation runner
- `docs/`: MkDocs documentation source

## Quickstart

Requirements:

- Python `3.12`
- `uv` (recommended) or `pip`

Validate ontology quality:

```bash
uv run ontology-validate
```

Fallback:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

## Documentation

Local docs build:

```bash
uv run mkdocs build --strict
```

Local live preview:

```bash
uv run mkdocs serve
```

Regenerate class hierarchy artifacts (`.dot`, `.mmd`, `.svg`) from `min.ttl`:

```bash
uv run python scripts/generate_hierarchy.py
```

Published docs:

- `https://lepy.github.io/min-ontology/`

Core doc pages:

- `docs/min-model.md`
- `docs/class-catalog.md` (all classes in MIN v1)
- `docs/property-catalog.md`

Static visualization:

- `docs/min-v1_0_0-visualization.html`

## GitHub Pages deployment

Docs deployment is automated via `.github/workflows/docs.yml` on each push to
`main` and can also be triggered manually (`workflow_dispatch`).

Repository setting required:

- `Settings -> Pages -> Build and deployment -> Source: GitHub Actions`

## Release and versioning policy

- Semantic versioning is used for MIN releases.
- `min-vX.Y.Z.ttl` files are immutable snapshots.
- `min.ttl` always points to the latest stable MIN release.

## License and Attribution

- License: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
- Required attribution (Namensnennung): **Dr. Ingolf Lepenies** as author of MIN.
- Suggested citation:
  `"MIN Ontology" by Dr. Ingolf Lepenies, https://w3id.org/min, licensed under CC BY-SA 4.0.`

# MIN Ontology

MIN (Material · Information · Nexus) is a foundational ontology for modeling
industrial and scientific domains with a strict distinction between:

- **Nexus**: actual entities that are causally effective
- **Forma**: formal entities that are constitutively determining

The current stable release line is **v3.x** (current: **v3.3.0**, tag `v3.3.0`).

## Canonical IRIs

- Ontology IRI: `https://w3id.org/min`
- Namespace: `https://w3id.org/min#`
- Current version IRI: `https://w3id.org/min/3.3.0`

## Conceptual core (v3.3.0)

MIN v3 defines **14 classes**:

- Root: `min:Entity`
- Actual branch: `min:Nexus`, `min:Object`, `min:Process`, `min:Data`, `min:Agent`, `min:Boundary`
- Formal branch: `min:Forma`, `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio`, `min:Typus`

For full class definitions, see `docs/class-catalog.md`.

```mermaid
graph TD
    Entity["<b>Entity</b><br/><small>∃hasIdentifier ≥ 1</small>"]
    
    Nexus["<b>Nexus</b><br/><small>kausale Wirksamkeit</small>"]
    Forma["<b>Forma</b><br/><small>konstitutive Bestimmung</small>"]

    Object["Object"]
    Process["Process"]
    Data["Data"]
    Agent["Agent"]
    Boundary["Boundary"]

    Lex["Lex"]
    Structura["Structura"]
    Possibile["Possibile"]
    Norma["Norma"]
    Institutio["Institutio"]
    Typus["Typus"]

    Entity --> Nexus
    Entity --> Forma

    Nexus --> Object
    Nexus --> Process
    Nexus --> Data
    Nexus -.-> Agent
    Nexus --> Boundary

    Forma --> Lex
    Forma --> Structura
    Forma --> Possibile
    Forma --> Norma
    Forma --> Institutio
    Forma --> Typus

    style Entity fill:#f0ebe3,stroke:#9c8b75,color:#3d3225,stroke-width:2px
    style Nexus fill:#d6eaf8,stroke:#2e86c1,color:#1a3c5e,stroke-width:2px
    style Forma fill:#e8daef,stroke:#7d3c98,color:#4a235a,stroke-width:2px
    
    style Object fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Process fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Data fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Boundary fill:#d5f5e3,stroke:#28b463,color:#186a3b
    style Agent fill:#fdebd0,stroke:#e67e22,color:#7e4a12,stroke-width:2px,stroke-dasharray: 5 5

    style Lex fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Structura fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Possibile fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Norma fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Institutio fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
    style Typus fill:#f0e6f6,stroke:#8e44ad,color:#4a235a
```

**Legende:**  
`━━` rdfs:subClassOf (disjunkt) · `╌╌` rdfs:subClassOf (überlappt — Agent)  
⊥ Object · Process · Data · Boundary paarweise disjunkt · Agent überlappt  
⊥ Lex · Structura · Possibile · Norma · Institutio · Typus paarweise disjunkt  
Entity ≡ Nexus ⊔ Forma

[min_hierarchy.svg](docs/min_hierarchy.svg)

## Repository structure

- `min.ttl`: current MIN ontology
- `min-v*.ttl`: immutable release snapshots
- `min-v3.3.0.ttl`: current immutable snapshot (hyphen naming)
- `min_v3.3.0.ttl`: current compatibility snapshot (underscore naming)
- `examples/`: example instance graphs
- `examples/min-v3.3.0-examples.ttl`: integrated v3.3.0 scenario
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

Published docs:

- `https://lepy.github.io/min-ontology/`

Core doc pages:

- `docs/min-model.md`
- `docs/class-catalog.md` (all classes in MIN v3)
- `docs/property-catalog.md`

Static visualizations are intentionally kept as part of the docs:

- `docs/min-v3_0_0-visualization.html`
- `docs/min-v2_1_0-visualization.html`
- `docs/bfo-vs-min3_2_0.html` (historical comparison page)

## GitHub Pages deployment

Docs deployment is automated via `.github/workflows/docs.yml` on each push to
`main` and can also be triggered manually (`workflow_dispatch`).

Repository setting required:

- `Settings -> Pages -> Build and deployment -> Source: GitHub Actions`

## Release and versioning policy

- Semantic versioning is used for MIN releases.
- `min-vX.Y.Z.ttl` files are immutable snapshots.
- `min_vX.Y.Z.ttl` files may exist for compatibility with underscore naming.
- `min.ttl` always points to the latest stable MIN release.
- Since `v2.0.0`, OPA is absorbed into MIN and no separate `opa.ttl` is maintained.

## License and Attribution

- License: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- Required attribution (Namensnennung): **Dr. Ingolf Lepenies** as author of MIN.
- Suggested citation:
  `"MIN Ontology" by Dr. Ingolf Lepenies, https://w3id.org/min, licensed under CC BY 4.0.`

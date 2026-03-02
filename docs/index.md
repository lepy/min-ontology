# MIN Ontology Documentation

Welcome to the MIN ontology documentation.

MIN v3 models reality with two explicit branches under `min:Entity`:

- `min:Nexus` for actual, causally effective entities
- `min:Forma` for formal, constitutively determining entities

## What to read first

- `min-model.md`: architecture, modeling rules, and design rationale
- `class-catalog.md`: complete catalog of all MIN classes (v3.0.0)
- `property-catalog.md`: complete catalog of object/data/annotation properties
- `versioning.md`: release and semantic versioning rules

## Static visualizations (kept intentionally)

- [MIN v3.0.0 visualization](min-v3_0_0-visualization.html)
- [MIN v2.1.0 visualization](min-v2_1_0-visualization.html)

## Quality gates

MIN maintains ontology quality through:

- SPARQL ASK regression tests
- SHACL conformance checks
- Turtle parse checks across all released snapshots

Run locally:

```bash
uv run ontology-validate
```

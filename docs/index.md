# MIN Ontology Documentation

MIN v3.3.0 models reality with a strict two-branch architecture under `min:Entity`:

- `min:Nexus`: actual, causally effective entities
- `min:Forma`: formal, constitutively determining entities

## Reading paths

### If you are new to MIN

1. Start with [Modellüberblick](min-model.md).
2. Continue with [Klassenkatalog](class-catalog.md).
3. Use [Property-Katalog](property-catalog.md) as implementation reference.

### If you are modeling domain data

1. Pick class patterns in [Klassenbeispiele](examples.md).
2. Use [Frühstücksei Tutorial (DE)](breakfast_egg_de.md) or [Breakfast Egg Tutorial (EN)](breakfast_egg_en.md) for end-to-end modeling.

## Reference scope

The docs reflect MIN `v3.3.0` (`min.ttl` points to this release):

- 14 classes (`Entity`, 6 Nexus-side classes, 7 Forma-side classes including `Typus`)
- Full Nexus/Forma bridge relations (including `typifies` / `typifiedBy`)
- Current validation and versioning rules

## Validation command

```bash
uv run ontology-validate
```

## Historical artifacts

Static visualizations from earlier documentation phases are preserved under **Historisch**.

- [Visualization v3.3.0](min-v3_3_0-visualization.html)

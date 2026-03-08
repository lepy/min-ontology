# MIN Ontology Documentation

MIN v1.0.0 models reality with these core definitions:

- `Entity · eindeutige Referenzierbarkeit · "Das, was existiert."`
- `Nexus · kausale Wirksamkeit · "Das, was etwas bewirkt."`
- `Forma · konstitutive Bestimmung · "Das, was bestimmt."`
- `Agent · selektive Handlungsfähigkeit · "Das, was handelt."`

## Reading paths

### If you are new to MIN

1. Start with [Modellüberblick](min-model.md).
2. Continue with [Klassenkatalog](class-catalog.md).
3. Use [Property-Katalog](property-catalog.md) as implementation reference.

### If you are modeling domain data

1. Pick class patterns in [Klassenbeispiele](examples.md).
2. Use [Frühstücksei Tutorial (DE)](breakfast_egg_de.md) or [Breakfast Egg Tutorial (EN)](breakfast_egg_en.md) for end-to-end modeling.

## Reference scope

The docs reflect MIN `v1.0.0` (`min.ttl` points to this release):

- 13 classes (`Entity`, 5 Nexus-side classes, 6 Forma-side classes, plus `Agent` as "Das, was handelt.")
- Updated bridge model including `originates` / `originatedBy`
- Current validation and versioning rules
- Updated documentation for `realizes`, `constrains`, and `originates`

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

## Validation command

```bash
uv run ontology-validate
```

## Visualization

- [Visualization v1.0.0](min-v1_0_0-visualization.html)

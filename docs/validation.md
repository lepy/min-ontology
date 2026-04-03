# MIN Validation (SHACL Shapes)

MIN provides two SHACL shape files for validation.

## Core shapes (`shapes/min-core.shacl.ttl`)

Validates the **ontology structure** of `min.ttl` itself:

| Shape | Validates |
|-------|-----------|
| `OntologyMetadataShape` | Ontology IRI has versionIRI, versionInfo, title, description, creator, created, license |
| `ClassLabelShape` | All 13 domain classes + 2 enum classes have `rdfs:label` |
| `PolaritySuperPropertyShape` | Polarity super-properties have labels |
| `ObjectPropertyDomainRangeShape` | All 49 object properties have `rdfs:range` |

## Instance shapes (`shapes/min-instance.shacl.ttl`)

Validates **domain instance data** that imports `min.ttl`:

| Shape | Target class | Constraint |
|-------|-------------|------------|
| `EntityInstanceShape` | `min:Entity` | `hasIdentifier` min 1 (Violation), `hasName` min 1 (Warning) |
| `ProcessInstanceShape` | `min:Process` | `hasInput` min 1, `hasOutput` min 1 |
| `AgentInstanceShape` | `min:Agent` | `performs` min 1 |
| `BoundaryInstanceShape` | `min:Boundary` | `bounds` min 2 |

## Running validation

```bash
uv run ontology-validate
```

Or manually with pyshacl:

```bash
pyshacl -s shapes/min-core.shacl.ttl -df turtle min.ttl
pyshacl -s shapes/min-instance.shacl.ttl -df turtle examples/dpp-coil.ttl
```

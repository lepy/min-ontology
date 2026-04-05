# MIN Validation (SHACL Shapes)

MIN provides two SHACL shape files for validation.

## Core shapes (`shapes/min-core.shacl.ttl`)

Validates the **ontology structure** of `min.ttl` itself:

| Shape | Validates |
|-------|-----------|
| `OntologyMetadataShape` | Ontology IRI has versionIRI, versionInfo, title, description, creator, created, license |
| `ClassLabelShape` | All 14 domain classes + 4 enum classes have `rdfs:label` |
| `PolaritySuperPropertyShape` | Polarity super-properties have labels |
| `ObjectPropertyDomainRangeShape` | All 58 object properties have `rdfs:range` |

## Instance shapes (`shapes/min-instance.shacl.ttl`)

Validates **domain instance data** that imports `min.ttl`:

| Shape | Target class | Constraint |
|-------|-------------|------------|
| `EntityInstanceShape` | `min:Entity` | `hasIdentifier` min 1 (Violation), `hasName` min 1 (Warning) |
| `ProcessInstanceShape` | `min:Process` | `hasInput` min 1, `hasOutput` min 1 |
| `AgentInstanceShape` | `min:Agent` | `performs` min 1 |
| `BoundaryInstanceShape` | `min:Boundary` | `bounds` min 2 |
| `EpistemicumInstanceShape` | `min:Epistemicum` | `about` min 1, `hasEpistemicStatus` exactly 1, `hasConfidence` in [0,1], `supportedBy`/`underminedBy` class Nexus |
| `ConfidenceRequiresTypeShape` | `min:Epistemicum` | SPARQL rule: `hasConfidence` requires `hasConfidenceType` |

## Running validation

```bash
uv run ontology-validate
```

Or manually with pyshacl:

```bash
pyshacl -s shapes/min-core.shacl.ttl -df turtle min.ttl
pyshacl -s shapes/min-instance.shacl.ttl -df turtle examples/dpp-coil.ttl
```

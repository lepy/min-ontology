# MIN Property Catalog (v3.7.1)

This page lists MIN properties by modeling role and relation family.

## 1. Polarity super-properties

Both are schema-level `owl:AnnotationProperty` terms:

- `min:materialProperty`
- `min:informationalProperty`

## 2. Nexus structural relations

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:nexusWith` | `min:Nexus` | `min:Nexus` | Symmetric base relation |
| `min:hasComponent` | `min:Nexus` | `min:Nexus` | Transitive mereology |

## 3. Nexus category relations

### Process and transformation

| Property | Domain | Range | Inverse / semantics |
| --- | --- | --- | --- |
| `min:hasInput` | `min:Process` | `min:Nexus` | inverse: `min:undergoes` |
| `min:hasOutput` | `min:Process` | `min:Nexus` | inverse: `min:resultOf` |
| `min:undergoes` | `min:Nexus` | `min:Process` | conservative identity pattern |
| `min:resultOf` | `min:Nexus` | `min:Process` | inverse of `hasOutput` |

### Agency

| Property | Domain | Range | Inverse / semantics |
| --- | --- | --- | --- |
| `min:performs` | `min:Agent` | `min:Process` | inverse: `min:performedBy` |
| `min:performedBy` | `min:Process` | `min:Agent` | inverse of `performs` |
| `min:controls` | `min:Agent` | `min:Process` | stronger agency/control relation |
| `min:actsOn` | `min:Agent` | `min:Nexus` | inverse: `min:affectedBy` |
| `min:affectedBy` | `min:Nexus` | `min:Agent` | inverse of `actsOn` |
| `min:owns` | `min:Agent` | `min:Object` | ownership relation |
| `min:produces` | `min:Agent` | `min:Object` | derived via chain `(performs o hasOutput)` |

### Data and boundary

| Property | Domain | Range | Inverse / semantics |
| --- | --- | --- | --- |
| `min:describes` | `min:Data` | `min:Nexus` | inverse: `min:describedBy` |
| `min:describedBy` | `min:Nexus` | `min:Data` | inverse of `describes` |
| `min:generates` | `min:Process` | `min:Data` | inverse: `min:generatedBy` |
| `min:generatedBy` | `min:Data` | `min:Process` | inverse of `generates` |
| `min:bounds` | `min:Boundary` | `min:Nexus` | inverse: `min:hasBoundary` |
| `min:hasBoundary` | `min:Nexus` | `min:Boundary` | inverse of `bounds` |

## 4. Nexus/Forma bridge relations

### Generic bridges

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:originates` | `min:Nexus` | `min:Forma` | inverse: `min:originatedBy`; forma genesis |
| `min:originatedBy` | `min:Forma` | `min:Nexus` | inverse of `originates` |
| `min:realizes` | `min:Nexus` | `min:Forma` | inverse: `min:realizedBy`; realization of existing forma |
| `min:realizedBy` | `min:Forma` | `min:Nexus` | inverse of `realizes` |
| `min:constrains` | `min:Forma` | `min:Nexus` | general determination relation |

### Specialized bridges

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:governs` | `min:Lex` | `min:Process` | subproperty of `constrains` |
| `min:formalizes` | `min:Structura` | `min:Nexus` | subproperty of `constrains` |
| `min:evaluates` | `min:Norma` | `min:Nexus` | subproperty of `constrains` |
| `min:concerns` | `min:Possibile` | `min:Nexus` | possibility scope |
| `min:alternativeTo` | `min:Possibile` | `min:Nexus` | subproperty of `concerns` |
| `min:constitutes` | `min:Agent` | `min:Institutio` | inverse: `min:constitutedBy`; subproperty of `originates` |
| `min:constitutedBy` | `min:Institutio` | `min:Agent` | inverse of `constitutes` |
| `min:recognizes` | `min:Agent` | `min:Institutio` | inverse: `min:recognizedBy` |
| `min:recognizedBy` | `min:Institutio` | `min:Agent` | inverse of `recognizes` |
| `min:encodes` | `min:Data` | `min:Forma` | inverse: `min:encodedBy` |
| `min:encodedBy` | `min:Forma` | `min:Data` | inverse of `encodes` |
| `min:typifies` | `min:Institutio` | `min:Nexus` | subproperty of `constrains` |
| `min:typifiedBy` | `min:Nexus` | `min:Institutio` | inverse of `typifies` |
| `min:comprises` | `min:Institutio` | `min:Forma` | bundles formal determinants |

## 5. Datatype properties

All core datatype properties use domain `min:Entity`:

- `min:hasIdentifier`
- `min:hasName`
- `min:hasTimestamp`
- `min:hasDescription`
- `min:hasStatus`

## 6. Annotation properties

Core design/meta properties include:

- `min:designRationale`
- `min:philosophicalBasis`
- `min:definition`
- `min:criterion`
- `min:usageExample`
- `min:counterExample`
- `min:distinguishedFrom`
- `min:normativeSource`
- `min:rationale`
- `min:definedInVersion`
- `min:status`
- `min:replacedBy`
- `min:axiomRationale`

## 7. Modeling guidance

1. Use bridge relations explicitly; do not collapse Nexus and Forma in one node.
2. Use `originates` only when the formal entity is newly brought forth.
3. Use `realizes` when a formal entity already exists and is instantiated in actuality.
4. Use `encodes` for representation links (`Data -> Forma`).
5. Use `typifies` for kind-of determination via institutionalized type assignments.

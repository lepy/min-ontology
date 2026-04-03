# MIN Property Catalog (v1.0.1)

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
| `min:comprises` | `min:Institutio` | `min:Forma` | inverse: `min:comprisedBy`; bundles formal determinants |
| `min:comprisedBy` | `min:Forma` | `min:Institutio` | inverse of `comprises` |

### Epistemic relations

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:confirms` | `min:Process` | `min:Forma` | inverse: `min:confirmedBy`; epistemic corroboration |
| `min:confirmedBy` | `min:Forma` | `min:Process` | inverse of `confirms` |
| `min:refutes` | `min:Process` | `min:Possibile` | inverse: `min:refutedBy`; epistemic falsification |
| `min:refutedBy` | `min:Possibile` | `min:Process` | inverse of `refutes` |
| `min:entails` | `min:Forma` | `min:Forma` | transitive; logical implication |
| `min:supersedes` | `min:Forma` | `min:Forma` | inverse: `min:supersededBy`; NOT transitive |
| `min:supersededBy` | `min:Forma` | `min:Forma` | inverse of `supersedes` |
| `min:justifiedBy` | `min:Institutio` | `min:Forma` | inverse: `min:justifies`; epistemic grounding |
| `min:justifies` | `min:Forma` | `min:Institutio` | inverse of `justifiedBy` |

### Meta-relation

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:describesOntologyTerm` | `min:OntologyArtifact` | `min:MetaTerm` | subproperty of `describes` |

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
## 7. Mode properties (formalized enumerations)

| Property | Range | Type | Notes |
| --- | --- | --- | --- |
| `min:hasCausalityMode` | `min:CausalityMode` | ObjectProperty | Nexus & Agent (by restriction) |
| `min:hasEfficacyMode` | `min:EfficacyMode` | ObjectProperty | All leaf Entity subclasses |

### CausalityMode values

| Individual | Label | Applied to |
| --- | --- | --- |
| `min:CM_Dispositional` | dispositional | Object, Process, Agent |
| `min:CM_Mediated` | mediated | Data |
| `min:CM_Relational` | relational | Boundary |

### EfficacyMode values

| Individual | Label | Applied to |
| --- | --- | --- |
| `min:EM_Dispositional` | dispositional | Object, Process |
| `min:EM_Informational` | informational | Data |
| `min:EM_Agentive` | agentive | Agent |
| `min:EM_Relational` | relational | Boundary |
| `min:EM_Formal` | formal | (via Forma branch root, if instantiated) |
| `min:EM_Lawful` | lawful | Lex |
| `min:EM_Structural` | structural | Structura |
| `min:EM_Modal` | modal | Possibile |
| `min:EM_Normative` | normative | Norma |
| `min:EM_Institutional` | institutional | Institutio |

Reasoner infers mode automatically via `owl:hasValue` restrictions on each class.

## 8. Modeling guidance

1. Use bridge relations explicitly; do not collapse Nexus and Forma in one node.
2. Use `originates` only when the formal entity is newly brought forth.
3. Use `realizes` when a formal entity already exists and is instantiated in actuality.
4. Use `encodes` for representation links (`Data -> Forma`).
5. Use `typifies` for kind-of determination via institutionalized type assignments.

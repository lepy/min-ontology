# MIN Property Catalog (v1.1.0)

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
| `min:owns` | `min:Agent` | `min:Entity` | ownership / responsibility |
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
| `min:constrains` | `min:Forma` | `min:Nexus` | inverse: `min:constrainedBy`; general determination relation |
| `min:constrainedBy` | `min:Nexus` | `min:Forma` | inverse of `constrains` |

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

### Epistemic relations (process-centric, v1.0.0)

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:confirms` | `min:Process` | `min:Forma` | inverse: `min:confirmedBy`; Popperian corroboration |
| `min:confirmedBy` | `min:Forma` | `min:Process` | inverse of `confirms` |
| `min:refutes` | `min:Process` | `min:Possibile` | inverse: `min:refutedBy`; Popperian falsification |
| `min:refutedBy` | `min:Possibile` | `min:Process` | inverse of `refutes` |
| `min:entails` | `min:Forma` | `min:Forma` | transitive; logical implication |
| `min:supersedes` | `min:Forma` | `min:Forma` | inverse: `min:supersededBy`; NOT transitive |
| `min:supersededBy` | `min:Forma` | `min:Forma` | inverse of `supersedes` |
| `min:justifiedBy` | `min:Institutio` | `min:Forma` | inverse: `min:justifies`; epistemic grounding |
| `min:justifies` | `min:Forma` | `min:Institutio` | inverse of `justifiedBy` |

### Epistemicum relations (evidence-centric, v1.1.0)

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:holds` | `min:Agent` | `min:Epistemicum` | inverse: `min:heldBy`; agent holds epistemic stance |
| `min:heldBy` | `min:Epistemicum` | `min:Agent` | inverse of `holds`; optional (agent-free allowed) |
| `min:about` | `min:Epistemicum` | `min:Entity` | the entity this stance is about; required |
| `min:supportedBy` | `min:Epistemicum` | `min:Nexus` | inverse: `min:supports`; evidence supports stance |
| `min:supports` | `min:Nexus` | `min:Epistemicum` | inverse of `supportedBy` |
| `min:underminedBy` | `min:Epistemicum` | `min:Nexus` | inverse: `min:undermines`; evidence weakens stance |
| `min:undermines` | `min:Nexus` | `min:Epistemicum` | inverse of `underminedBy` |
| `min:hasEpistemicStatus` | `min:Epistemicum` | `min:EpistemicStatus` | functional; exactly one per Epistemicum |
| `min:hasConfidenceType` | `min:Epistemicum` | `min:ConfidenceType` | functional; required when hasConfidence present |

Both epistemic patterns complement each other:
- **Process-centric (Popperian):** "The tensile test confirms Hooke's law." Carrier: Process.
- **Evidence-centric (Epistemicum):** "The hypothesis is supported by measurement data." Carrier: Epistemicum.

### Meta-relation

| Property | Domain | Range | Notes |
| --- | --- | --- | --- |
| `min:describesOntologyTerm` | `min:OntologyArtifact` | `min:MetaTerm` | subproperty of `describes` |

## 5. Datatype properties

Core datatype properties (domain `min:Entity`):

- `min:hasIdentifier`
- `min:hasName`
- `min:hasTimestamp`
- `min:hasDescription`
- `min:hasStatus`

Process-specific:

- `min:startedAt` (domain: `min:Process`, range: `xsd:dateTime`)
- `min:endedAt` (domain: `min:Process`, range: `xsd:dateTime`)

Epistemicum-specific (v1.1.0):

- `min:hasConfidence` (domain: `min:Epistemicum`, range: `xsd:double` [0.0, 1.0], functional)
- `min:isQuantifiable` (domain: `min:Possibile`, range: `xsd:boolean`; true = risk, false = Knightian uncertainty)

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

### EpistemicStatus values (v1.1.0)

| Individual | Label | Meaning |
| --- | --- | --- |
| `min:ES_Hypothetical` | hypothetical | proposed, neither confirmed nor refuted |
| `min:ES_Confirmed` | confirmed | supported by evidence and accepted |
| `min:ES_Refuted` | refuted | contradicted by evidence |
| `min:ES_Contested` | contested | conflicting evidence, no consensus |
| `min:ES_Axiomatic` | axiomatic | foundational assumption, not empirically testable |

### ConfidenceType values (v1.1.0)

| Individual | Label | Meaning |
| --- | --- | --- |
| `min:CT_Subjective` | subjective | expert judgement |
| `min:CT_Statistical` | statistical | from sample (confidence interval) |
| `min:CT_Bayesian` | bayesian | posterior probability |
| `min:CT_Heuristic` | heuristic | experience-based estimate |

## 8. Modeling guidance

1. Use bridge relations explicitly; do not collapse Nexus and Forma in one node.
2. Use `originates` only when the formal entity is newly brought forth.
3. Use `realizes` when a formal entity already exists and is instantiated in actuality.
4. Use `encodes` for representation links (`Data -> Forma`).
5. Use `typifies` for kind-of determination via institutionalized type assignments.
6. Use `confirms`/`refutes` when a **Process** is the epistemic agent (Popperian pattern).
7. Use `supportedBy`/`underminedBy` when an **Epistemicum** accumulates evidence from Nexus instances.
8. When `hasConfidence` is present, always also provide `hasConfidenceType`.

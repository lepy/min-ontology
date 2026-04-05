# Migration Guide: MIN v1.0.x to v1.1.0

## Backward compatibility

MIN v1.1.0 is a **monotone extension** of v1.0.1. All v1.0.x instance
graphs remain valid. No existing classes, properties, or individuals
were removed or renamed.

## Breaking change: Forma partition extended

The closed Forma partition was extended from 5 to 6 subclasses:

```
v1.0.1: Forma = Lex | Structura | Possibile | Norma | Institutio
v1.1.0: Forma = Lex | Structura | Possibile | Norma | Institutio | Epistemicum
```

**Impact:** Any reasoner or query that relied on the closed 5-class
partition to infer that something is *not* one of the known Forma types
may need updating. The extension is monotone (existing Forma instances
keep their classification), but the equivalence axiom changed.

**Action required:** Update downstream imports from `min-v1.0.1.ttl`
to `min-v1.1.0.ttl`.

## New terms

### Classes (3)

- `min:Epistemicum` — 6th Forma subclass
- `min:EpistemicStatus` — enum (5 individuals: ES_Hypothetical, ES_Confirmed, ES_Refuted, ES_Contested, ES_Axiomatic)
- `min:ConfidenceType` — enum (4 individuals: CT_Subjective, CT_Statistical, CT_Bayesian, CT_Heuristic)

### Object Properties (9)

- `min:holds`, `min:heldBy` (Agent ↔ Epistemicum)
- `min:about` (Epistemicum → Entity)
- `min:supportedBy`, `min:supports` (Epistemicum ↔ Nexus)
- `min:underminedBy`, `min:undermines` (Epistemicum ↔ Nexus)
- `min:hasEpistemicStatus` (functional, Epistemicum → EpistemicStatus)
- `min:hasConfidenceType` (functional, Epistemicum → ConfidenceType)

### Datatype Properties (2)

- `min:hasConfidence` (Epistemicum → xsd:double, functional)
- `min:isQuantifiable` (Possibile → xsd:boolean)

## Unchanged

- `min:confirms` and `min:refutes` remain unchanged (Process → Forma/Possibile).
- `min:supersedes` remains non-transitive.
- `min:EfficacyMode` retains exactly 10 individuals (no EM_Epistemic).
- All alignment modules remain compatible.

## SHACL

Instance shapes were extended with `EpistemicumInstanceShape` and a
SPARQL-based consistency rule (hasConfidence requires hasConfidenceType).
Existing shapes are unchanged.

## For sdata-ontology users

Update the vendored MIN snapshot in sdata-core from `min-v1.0.1.ttl`
to `min-v1.1.0.ttl`. Epistemicum facades will be provided in sdata v0.3.0.

# MIN Property Catalog (v3.0.0)

This page lists the properties defined by MIN and groups them by modeling role.

## 1. Polarity super-properties (schema level)

These are used to classify domain-specific properties:

- `min:materialProperty`
- `min:informationalProperty`

Recommended pattern:

```ttl
ex:massKg a owl:DatatypeProperty ;
  rdfs:subPropertyOf min:materialProperty ;
  rdfs:domain min:Object ;
  rdfs:range xsd:decimal .
```

## 2. Nexus structural relations

- `min:nexusWith` (symmetric)
- `min:hasComponent` (transitive)

## 3. Nexus category relations

Process/Object:

- `min:hasInput`
- `min:hasOutput`
- `min:undergoes` (inverse of `min:hasInput`)
- `min:resultOf` (inverse of `min:hasOutput`)

Agent/Process:

- `min:performs`
- `min:performedBy` (inverse of `min:performs`)
- `min:controls`

Agent/Object:

- `min:actsOn`
- `min:affectedBy` (inverse of `min:actsOn`)
- `min:owns`
- `min:produces`

Data links:

- `min:describes`
- `min:describedBy` (inverse of `min:describes`)
- `min:generates`
- `min:generatedBy` (inverse of `min:generates`)

## 4. Nexus/Forma bridge relations

Realization/model:

- `min:realizes`
- `min:realizedBy` (inverse of `min:realizes`)
- `min:formalizes`

Constraint/governance:

- `min:constrains`
- `min:governs`

Norms and possibilities:

- `min:evaluates`
- `min:concerns`
- `min:alternativeTo`

Institutional:

- `min:constitutes`
- `min:recognizes`

Encoding:

- `min:encodes`
- `min:encodedBy` (inverse of `min:encodes`)

## 5. Datatype properties

All datatype properties are defined with domain `min:Entity`:

- `min:hasIdentifier`
- `min:hasName`
- `min:hasTimestamp`
- `min:hasDescription`
- `min:hasStatus`

## 6. Annotation properties

- `min:designRationale`
- `min:philosophicalBasis`

## 7. Modeling guidance

1. Keep instance data flat; avoid blank-node wrappers for polarity.
2. Put domain-specific semantics into subproperties beneath `materialProperty` or `informationalProperty`.
3. Use `min:encodes` to link artifacts (`min:Data`) to formal entities (`min:Forma` subclasses).
4. Use inverse relations only when they improve query ergonomics or consistency checks.

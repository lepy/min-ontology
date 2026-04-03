# Use Case: Digital Product Passport — Steel Coil to Part

This end-to-end example demonstrates how MIN's Nexus/Forma architecture models a real industrial scenario: from raw material to tested part, with full traceability.

## Scenario

A DC04 steel coil is deep-drawn into a part, then tested via tensile test. The result is a digital product passport linking material, process, agent, data, and normative requirements.

## Graph overview

```text
Coil(Object) → Tiefziehen(Process) → Bauteil(Object)
                    ↑                      ↑
               Operator(Agent)        Zugversuch(Process)
                    ↑                      ↓
               DIN-Dok(Data) ──encodes→ ISO6892(Norma)
                                           ↓
                                    DC04(Institutio) ──comprises→ Norma, Structura
                                           ↓
                                    typifies → Coil
```

## Example file

See [`examples/dpp-coil.ttl`](../examples/dpp-coil.ttl).

## Key SPARQL queries

### 1. Which Norma constrain this part?

```sparql
PREFIX min: <https://w3id.org/min#>
PREFIX ex:  <https://example.org/dpp/>

SELECT ?norma ?name WHERE {
  ?norma a min:Norma ;
         min:evaluates ex:bauteil_001 ;
         min:hasName ?name .
}
```

Returns: `Rm >= 270 MPa`, `Tensile test procedure ISO 6892-1`.

### 2. Who performed which process?

```sparql
SELECT ?agent ?agentName ?process ?processName WHERE {
  ?agent min:performs ?process ;
         min:hasName ?agentName .
  ?process min:hasName ?processName .
}
```

### 3. Which Forma is encoded by which Data?

```sparql
SELECT ?data ?dataName ?forma ?formaName WHERE {
  ?data min:encodes ?forma ;
        min:hasName ?dataName .
  ?forma min:hasName ?formaName .
}
```

### 4. What type is the coil? (Institutio → typifies)

```sparql
SELECT ?type ?typeName WHERE {
  ?type min:typifies ex:coil_042 ;
        min:hasName ?typeName .
}
```

Returns: `DC04`.

### 5. What does DC04 comprise?

```sparql
SELECT ?forma ?formaName WHERE {
  ex:DC04 min:comprises ?forma .
  ?forma min:hasName ?formaName .
}
```

Returns: `Rm >= 270 MPa`, `C <= 0.08%`, `von Mises yield criterion`.

## Why Nexus/Forma matters here

- **One-hop queries:** "Which norms constrain this part?" is a single `evaluates` hop — no joins across type hierarchies needed.
- **Data ≠ Forma:** The DIN document (Data, has bytes) and the requirement it encodes (Norma, has no bytes) are separate nodes connected by `encodes`. Deleting the document does not delete the requirement.
- **Institutio bundles:** DC04 is not a flat label but a structured bundle (`comprises`) of atomic Forma instances. Each can be queried, evaluated, and traced independently.
- **Epistemic layer:** The tensile test `confirms` the Rm requirement and `refutes` the failure scenario — recording what we *know*, not just what *is*.

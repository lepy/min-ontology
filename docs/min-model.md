# MIN model summary

MIN v2 defines five core classes:

- `min:Nexus`
- `min:Object`
- `min:Process`
- `min:Data`
- `min:Agent`

In MIN v2.1, polarität is modeled at schema level via super-properties:

- `min:materialProperty`
- `min:informationalProperty`

Domain properties are linked through `rdfs:subPropertyOf` chains to one of
these two super-properties, so instance graphs stay flat.

MIN v2 category relations are directly part of MIN:

- Process/Object: `min:hasInput`, `min:hasOutput`, `min:undergoes`, `min:resultOf`
- Agent/Process: `min:performs`, `min:performedBy`, `min:controls`
- Agent/Object: `min:actsOn`, `min:affectedBy`, `min:owns`, `min:produces`
- Data links: `min:describes`, `min:describedBy`, `min:generates`, `min:generatedBy`

Since v2, OPA is absorbed into MIN and no separate OPA layer is required.

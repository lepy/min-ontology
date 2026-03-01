# MIN model summary

MIN v2 defines five core classes:

- `min:Nexus`
- `min:Object`
- `min:Process`
- `min:Data`
- `min:Agent`

A `min:Nexus` is constrained to have both internal structural poles:

- `min:materialAspect some owl:Thing`
- `min:informationalAspect some owl:Thing`

MIN v2 category relations are directly part of MIN:

- Process/Object: `min:hasInput`, `min:hasOutput`, `min:undergoes`, `min:resultOf`
- Agent/Process: `min:performs`, `min:performedBy`, `min:controls`
- Agent/Object: `min:actsOn`, `min:affectedBy`, `min:owns`, `min:produces`
- Data links: `min:describes`, `min:describedBy`, `min:generates`, `min:generatedBy`

Since v2, OPA is absorbed into MIN and no separate OPA layer is required.

# MIN model summary

MIN v3.0 defines an explicit root and two branches:

- `min:Entity`
- `min:Nexus`
- `min:Forma`

Nexus branch classes:

- `min:Object`
- `min:Process`
- `min:Data`
- `min:Agent`

Forma branch classes:

- `min:Lex`
- `min:Structura`
- `min:Possibile`
- `min:Norma`
- `min:Institutio`

Polarität remains modeled at schema level via super-properties:

- `min:materialProperty`
- `min:informationalProperty`

Domain properties are linked through `rdfs:subPropertyOf` chains to one of
these two super-properties, so instance graphs stay flat.

Nexus category relations:

- Process/Object: `min:hasInput`, `min:hasOutput`, `min:undergoes`, `min:resultOf`
- Agent/Process: `min:performs`, `min:performedBy`, `min:controls`
- Agent/Object: `min:actsOn`, `min:affectedBy`, `min:owns`, `min:produces`
- Data links: `min:describes`, `min:describedBy`, `min:generates`, `min:generatedBy`

Nexus/forma bridge relations:

- `min:realizes`, `min:realizedBy`
- `min:constrains`, `min:governs`, `min:formalizes`
- `min:evaluates`, `min:concerns`, `min:alternativeTo`
- `min:constitutes`, `min:recognizes`
- `min:encodes`, `min:encodedBy`

Since v2, OPA is absorbed into MIN and no separate OPA layer is required.

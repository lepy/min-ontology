# MIN model summary

MIN defines three core classes:

- `min:Nexus`
- `min:Material`
- `min:Information`

A `min:Nexus` is constrained to have both:

- `min:hasMaterialAspect some min:Material`
- `min:hasInformationalAspect some min:Information`

MIN also defines a modality model via `min:Modality` and individuals:

- `min:MaterialModal`
- `min:Balanced`
- `min:InformationalModal`

Core repository requirement: all domain ontologies importing MIN must keep `owl:imports <https://w3id.org/min>` stable.

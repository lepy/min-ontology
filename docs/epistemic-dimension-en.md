# Epistemic Dimension (v1.1.0)

MIN v1.1.0 introduces `Epistemicum` as the 6th Forma subclass.

---

## Motivation

Engineering knowledge graphs need to express:
- "Engineer Mueller believes Hooke's law holds for DC04 up to 200 MPa."
- "This hypothesis is supported by test data with 0.95 statistical confidence."
- "Two experts disagree on whether the model is valid."

Before v1.1.0, MIN could express that a process confirms a law (`confirms`)
or refutes a possibility (`refutes`), but could not attach epistemic status,
confidence, or agent attribution to these judgements.

---

## Design decision: why Forma?

Epistemicum is not causally efficacious (it does not transform matter or
produce data) — so it is not Nexus. It formally determines how an agent
interprets a state of affairs — so it is Forma.

Checked against all existing Forma subclasses:

| Subclass | Why Epistemicum is different |
|---|---|
| Lex | Lex holds universally. Epistemicum is an agent's stance, not a law. |
| Structura | Structura formalizes. Epistemicum evaluates. |
| Possibile | Possibile is a possibility. Epistemicum is a stance *about* a possibility. |
| Norma | Norma prescribes what should hold. Epistemicum describes what is held to be true. |
| Institutio | Institutio exists through collective recognition. Epistemicum can be held by a single agent. |

---

## Core mechanics

Epistemicum has five building blocks that combine freely:

- **WHO** believes it? → `heldBy` Agent (or agent-free: institutionalized)
- **WHAT** is believed? → `about` Entity (Lex, Norma, Data, Object, Process — anything)
- **HOW CERTAIN?** → `hasConfidence` [0..1] + `hasConfidenceType` (Subjective / Statistical / Bayesian / Heuristic)
- **WHICH STATUS?** → `hasEpistemicStatus` (Hypothetical / Confirmed / Refuted / Contested / Axiomatic)
- **BASED ON WHAT?** → `supportedBy` / `underminedBy` Nexus (measurements, experiments, calculations)

All patterns below arise from these five building blocks.

---

## Two complementary epistemic patterns

MIN v1.1.0 maintains two distinct epistemic patterns:

### Pattern 1: Process-centric (Popperian, v1.0.0)

```turtle
ex:TensileTest  min:confirms  ex:HookesLaw .
ex:TensileTest  min:refutes   ex:LinearityAbove300MPa .
```

The **process** is the carrier. Semantics: a process evaluates a formal
determinant as tenable or untenable.

### Pattern 2: Evidence-centric (Epistemicum, v1.1.0)

```turtle
ex:Hypothesis  a min:Epistemicum ;
    min:heldBy       ex:Mueller ;
    min:about        ex:HookesLaw ;
    min:supportedBy  ex:TestData ;
    min:hasEpistemicStatus  min:ES_Confirmed ;
    min:hasConfidence       0.95 ;
    min:hasConfidenceType   min:CT_Statistical .
```

The **epistemic stance** is the carrier. Semantics: a reified belief
accumulates evidence, has status and confidence.

Both patterns are needed in practice. Pattern 1 is compact and sufficient
for simple process-level assertions. Pattern 2 is needed when epistemic
state changes over time, when confidence must be typed, or when multiple
agents hold conflicting stances.

---

## EpistemicStatus values

| Value | Meaning |
|---|---|
| ES_Hypothetical | Proposed, neither confirmed nor refuted |
| ES_Confirmed | Supported by evidence and accepted |
| ES_Refuted | Contradicted by evidence |
| ES_Contested | Conflicting evidence, no consensus |
| ES_Axiomatic | Foundational assumption, not empirically testable |

## ConfidenceType values

| Value | Meaning |
|---|---|
| CT_Subjective | Expert judgement |
| CT_Statistical | From sample (confidence interval) |
| CT_Bayesian | Posterior probability |
| CT_Heuristic | Experience-based estimate |

---

## Engineering patterns

**Model validation.** An FEM engineer models: "I believe the Euler-Bernoulli beam theory (Structura) holds for this load case. Confidence 0.7 (HeuristicConfidence). Supported by simulation data. Undermined by measurement data at high load." This is V&V as a graph instead of a report.

**Material release.** A test engineer models: "The tensile test (Process) confirms that Rm >= 270 MPa (Norma) is met. Status: Confirmed. Confidence 0.98 (StatisticalConfidence). Supported by 30 measurements." The acceptance criterion becomes queryable: "Which Norma instances on this part are Confirmed?"

**Failure analysis.** An expert models: "Hypothesis: Corrosion (Process) caused the failure. Status: Contested. Agent A says Confirmed (supported by metallography), Agent B says Refuted (supported by fracture surface analysis)." Dissent becomes visible, not hidden.

**Simulation chain trust.** In a process chain (deep drawing -> heat treatment -> assembly) each step has its own uncertainties. Epistemicum allows: one hypothesis with confidence per simulation step. The final question: "Which step has the lowest confidence?" — validate there first.

**Material model selection.** "For PP-GF30 I use the Mori-Tanaka model (Structura). Status: Hypothetical. Confidence 0.6 (SubjectiveConfidence). Alternative: RVE homogenization (second Epistemicum, about the same Structura, higher confidence)." Decisions become reasoned and comparable.

---

## DPP patterns (Digital Product Passport)

**Auditable recyclate content.** Not "42%", but: "42%, Epistemicum: Confirmed, Confidence 0.92 (StatisticalConfidence), supportedBy: XRF measurement data, heldBy: test lab TUeV." An auditor can ask: "Which DPP entries have confidence < 0.5?" or "Which are only SubjectiveConfidence?"

**SVHC declaration.** "This product contains no SVHC above 0.1%. Status: Confirmed. supportedBy: supplier declaration (Data)." Versus: "Status: Hypothetical. supportedBy: none." The difference is regulatorily relevant.

**Supply chain trust.** Each actor in the chain adds Epistemicum instances. Raw material supplier: "Origin: Virgin. Confidence 0.99." Recycler: "Origin: Recycled, 60% share. Confidence 0.85." OEM: can query the entire chain and identify the weakest link.

**DPP completeness analysis.** Query: "Which mandatory fields in the DPP have *no* associated Epistemicum?" — the gaps become visible. "Which have Status Assumed instead of Confirmed?" — the weak spots too.

---

## Digital twin patterns

**Sensor credibility.** A sensor (HardwareAgent) delivers temperature data (Data). Epistemicum: "This data is correct. Status: Confirmed. Confidence 0.95." After calibration drift: "Status: Contested. Confidence 0.4. underminedBy: reference measurement." The digital twin knows which sensors to trust.

**Predictive maintenance.** An ML model (SoftwareAgent) says: "Component fails within 200 operating hours (Possibile). Confidence 0.72 (BayesianConfidence). supportedBy: vibration data from the last 30 days." The maintenance decision has a formal basis.

**Model update.** Old hypothesis: "Linear degradation model holds." New hypothesis supersedes old, with higher confidence, supported by more data. The history is queryable via property paths: "What did we believe 6 months ago, and why not anymore?"

---

## Scientific patterns

**Hypothesis -> experiment -> result.** The classic scientific cycle becomes a graph pattern:

1. Epistemicum (Hypothetical, about Lex)
2. Process (Experiment) generates Data
3. Data supportedBy/underminedBy Epistemicum
4. New Epistemicum (Confirmed/Refuted) supersedes old

**Peer review.** Reviewer A: Epistemicum about paper thesis, Confirmed. Reviewer B: Epistemicum about same thesis, Refuted. Paper status: Contested. Queryable: "Which theses in my research project are contested?"

**Reproducibility.** Original study: Epistemicum, Confirmed, supportedBy Experiment_1. Replication study: new Epistemicum, underminedBy Experiment_2. Replication status is formalized.

**Meta-analysis.** Multiple Epistemicum instances about the same Lex, different supportedBy datasets, different confidences. The meta-question "How well is F=ma supported for this parameter range?" becomes an aggregation query.

---

## Organizational patterns

**Knowledge management.** "Department A believes procedure X is optimal. Department B prefers Y." Both formalized as Epistemicum with different supportedBy evidence. Management can ask: "Where is there dissent between departments?"

**Lessons learned.** A project error modeled as Epistemicum: "We assumed (Axiomatic) that supplier X delivers on time. Status: Refuted. underminedBy: delay data." The lesson learned is queryable, not buried in a PDF.

**Onboarding.** A new employee can ask: "What is Confirmed in our knowledge graph? What is still Hypothetical?" Instead of implicit knowledge, the epistemic state of the team becomes visible.

---

## Standards patterns

**Standard evolution.** DIN EN ISO 6892-1:2019 supersedes DIN EN ISO 6892-1:2009. Both as Institutio. The community's epistemic stance: old version Refuted (no longer valid), new version Confirmed. Queryable: "Which standards in my system are deprecated?"

**Compliance gaps.** Epistemicum: "We fulfill Norma X. Status: Confirmed." Versus: "We fulfill Norma Y. Status: Hypothetical, Confidence 0.3, supportedBy: none." The difference between "tested" and "claimed" becomes explicit.

---

## Knightian / deep uncertainty

**Known unknowns.** `isQuantifiable = true` on Possibile: "Component failure with 2% probability." Normal risk, quantifiable.

**Unknown unknowns.** `isQuantifiable = false` on Possibile: "Climate change impact on supply chain." No distribution assignable. This is not a bug but a deliberate statement: "We don't know what we don't know — but we know *that* we don't know it."

**Scenario planning.** Three Possibile instances (best case, base case, worst case), each with its own Epistemicum and different confidence. Queryable: "Which scenario has the most evidence?"

---

## Agent optionality

`heldBy` has no minimum cardinality in SHACL. Agent-free Epistemicum
instances model institutionalized epistemic states:

```turtle
ex:DatasetVerified  a min:Epistemicum ;
    min:about  ex:Dataset_042 ;
    min:hasEpistemicStatus  min:ES_Confirmed .
    # No heldBy — institutional state, not personal belief.
```

Provenance for agent-free instances runs through the existing `originatedBy`.

---

## Graph patterns (SPARQL)

```sparql
# Lowest confidence in the system — weakness analysis
SELECT ?e ?subject ?confidence WHERE {
    ?e a min:Epistemicum ; min:about ?subject ; min:hasConfidence ?confidence .
} ORDER BY ASC(?confidence) LIMIT 10

# Dissent between agents
SELECT ?forma ?a1 ?a2 WHERE {
    ?e1 min:about ?forma ; min:heldBy ?a1 ; min:hasEpistemicStatus min:ES_Confirmed .
    ?e2 min:about ?forma ; min:heldBy ?a2 ; min:hasEpistemicStatus min:ES_Refuted .
    FILTER (?a1 != ?a2)
}

# Knowledge progress: what was confirmed recently?
SELECT ?e ?forma WHERE {
    ?e min:about ?forma ; min:hasEpistemicStatus min:ES_Confirmed .
    ?e_old min:about ?forma ; min:hasEpistemicStatus min:ES_Hypothetical .
    ?e min:supersedes ?e_old .
}

# Key experiments: which evidence supports the most hypotheses?
SELECT ?evidence (COUNT(?e) AS ?count) WHERE {
    ?e min:supportedBy ?evidence .
} GROUP BY ?evidence ORDER BY DESC(?count)

# Blind spots: non-quantifiable Possibile
SELECT ?p WHERE {
    ?p a min:Possibile ; min:isQuantifiable false .
}

# Unsupported assumptions: Epistemicum without evidence
SELECT ?e ?subject WHERE {
    ?e a min:Epistemicum ; min:about ?subject .
    FILTER NOT EXISTS { ?e min:supportedBy ?x }
    FILTER NOT EXISTS { ?e min:underminedBy ?x }
}
```

---

## Design decisions

### Why no EM_Epistemic

EfficacyMode tracks the *mode of determination* — how a Forma subclass
constrains Nexus. Each EfficacyMode individual maps 1:1 to a Forma subclass
(lawful = Lex, structural = Structura, etc.).

Epistemicum does not *determine* — it *evaluates*. Adding EM_Epistemic
would conflate two orthogonal axes. The epistemic dimension is correctly
captured by `hasEpistemicStatus` and `hasConfidenceType`.

### Why supersedes stays non-transitive

`supersedes` was explicitly declared non-transitive in v1.0.0. The
rationale remains valid: A supersedes B and B supersedes C does not
imply A directly supersedes C (intermediate versions may change context).

For history queries, use SPARQL property paths:

```sparql
SELECT ?latest ?earliest WHERE {
    ?latest min:supersedes+ ?earliest .
}
```

---

## SHACL constraints

| Constraint | Severity |
|---|---|
| `about` min 1 | Violation |
| `hasEpistemicStatus` exactly 1 | Violation |
| `hasConfidence` in [0.0, 1.0] | Violation |
| `hasConfidence` present implies `hasConfidenceType` present | Violation |
| `supportedBy` / `underminedBy` must point to Nexus | Violation |
| `heldBy` must point to Agent (if present) | Violation |

---

## What Epistemicum CANNOT do

**No truth.** Epistemicum says "Agent A believes X with confidence 0.9." It does not say "X is true." Truth is not a MIN concept — and that is the right call.

**No reasoning over confidence.** A reasoner cannot infer: "If confidence(A) = 0.8 and confidence(B) = 0.7, then confidence(A and B) = 0.56." Bayesian propagation is a Process, not an axiom.

**No emotions.** "I *feel* that the component will fail" is not an Epistemicum. Epistemicum is propositional: it refers to states of affairs, not feelings.

**No self-reference.** "I believe that I believe" is not cleanly modelable in OWL. Epistemicum can talk about anything in the graph — except itself.

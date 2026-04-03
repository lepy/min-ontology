# MIN — The Philosophical Lineage

> **Eight thinkers, one ontology.**
>
> MIN does not invent from scratch. It inherits, transforms, and
> recombines ideas from a philosophical tradition spanning 2,400 years.
> This document traces what was borrowed from whom — and where it
> shows up in the architecture.

---

## The Architecture at a Glance

```
                     Entity
                    ╱  │  ╲
               Nexus   │   Forma
              ╱│╲  ╲   │  ╱│╲ ╲ ╲
       Object │ Data   │ Lex │ Norma
        Process   │  Agent │ Institutio
             Boundary    Structura
                          Possibile
```

Two branches (Nexus, Forma), one cross-cutting category (Agent),
connected by bridge relations. Every element in this architecture
has a philosophical ancestor.

---

## 1 — Aristotle (384–322 BCE)

**Borrowed:** Hyle/Morphe, Ousia, Kinesis, Aitia, Eidos, Apodeixis.

Aristotle is the deepest layer. MIN's entire two-branch architecture
is a transformation of his matter–form distinction.

**Hyle and Morphe → Polarity.** Aristotle's hyle (matter) and morphe
(form) become MIN's schema-level polarity: `materialProperty` and
`informationalProperty`. Every Nexus instance has a material and an
informational aspect. The pot has mass (hyle) and a design (morphe).
The measurement file has bytes (hyle) and semantics (morphe). MIN does
not force a choice — it treats polarity as a heuristic, not a
partition. Properties CAN be declared as material or informational
subproperties, but NEED NOT be.

**Ousia → Entity.** Aristotle's *to on* — "that which is" — becomes
MIN's `Entity`: the absolute root under which everything falls that is
explicitly modelled in the knowledge graph. Entity is not a metaphysical
claim about what exists in the universe; it is a pragmatic anchor for
what gets a node.

**Kinesis → Process.** Aristotle's concept of motion and change — the
becoming of being — maps directly onto `Process`. Process is
transformation: it takes Nexus instances as input and produces Nexus
instances as output. The two modes of transformation (transformative
vs. conservative) echo Aristotle's distinction between substantial
change and accidental change.

**Aitia → Causal Thinking.** Aristotle's four causes (material, formal,
efficient, final) are not adopted wholesale, but MIN's core question —
"Does it cause effects?" — descends from the Aristotelian commitment
to causal explanation as the foundation of understanding.

**Eidos → Institutio.** Aristotle's eidos — the essential form that
makes a thing what it is — reappears in MIN's `Institutio`. When MIN
asks "What kind of steel is this?" and answers "DC04", that
classification is an institutional act that assigns a type
determination. Institutio plays the eidos role: the bundle of
determinations that constitutes the essence. But unlike Aristotle, MIN
makes this bundle explicitly conventional — it exists because a
community of practice recognises it.

**Apodeixis → entails.** Aristotle's syllogistic — the logic of
necessary consequence — underpins `min:entails`. If A entails B and B
entails C, then A entails C. The transitivity of entails is Aristotelian
logic encoded as an OWL property.

**Sein vs. Sollen → Nexus / Forma.** The deep separation between "what
is" (Nexus) and "what ought to be" (Forma, especially Norma) echoes
Aristotle's separation of theoretical and practical knowledge — though
MIN routes this through Hume's guillotine (→ see Norma under Kant/Hume
below).

---

## 2 — Spinoza (1632–1677)

**Borrowed:** One substance, two attributes.

Spinoza argued that there is only one substance, but it can be
understood under two attributes: Extension (the physical) and Thought
(the mental). Neither is reducible to the other; both are aspects of
the same reality.

**One Substance, Two Attributes → Nexus Polarity.** MIN's polarity
mirrors this exactly. A Nexus instance — say, a steel sheet — is one
thing, but it shows two faces: its material aspect (mass, hardness,
geometry) and its informational aspect (identifier, classification,
provenance). The two annotation superproperties `materialProperty` and
`informationalProperty` are Spinoza's two attributes transposed to
schema-level property classification.

The key Spinozist insight MIN preserves: the two poles are not two
things but two ways of accessing the same thing. A measurement file has
bytes on a disk (extension) and semantic content (thought). It does not
split into a physical half and an informational half. It is one entity
with two aspects.

---

## 3 — Whitehead (1861–1947)

**Borrowed:** Actual Entity, Eternal Object, Process, Creativity.

Whitehead's process philosophy is arguably MIN's closest ancestor.

**Actual Entity → Nexus.** Whitehead's actual entities — the final real
things of which the world is made — map onto MIN's Nexus branch.
Everything that causes effects, everything that participates in causal
chains, is Nexus. Like Whitehead's actual entities, Nexus instances are
concrete, temporal, and relational.

**Eternal Object → Forma.** Whitehead's eternal objects — pure
potentials that are not themselves actual but determine what actual
entities can be — map onto MIN's Forma branch. A natural law (Lex)
determines how processes unfold. A mathematical structure (Structura)
shapes the geometry of the possible. A possibility (Possibile)
describes what could but does not happen. None of these are causally
effective in themselves; they are the grammar by which Nexus operates.

Whitehead's term *ingression* — the way an eternal object enters into an
actual entity — becomes MIN's `min:realizes`. A tensile test (Process)
realises ISO 6892-1 (Norma). A steel sheet (Object) realises the bcc
crystal structure (Structura). Realisation is ingression.

**Process → Process.** Whitehead's most famous thesis — "the becoming
of being" — is MIN's `Process` class. Reality is not made of static
substances but of events, transformations, becomings. MIN takes this
seriously: Process is not secondary to Object. Process is a full Nexus
category in its own right, with its own causal mode (dispositional).

**Creativity → originates.** Whitehead's creativity — the ultimate
principle by which actual entities bring forth novelty — maps onto
MIN's `min:originates`. When a research process generates a new
regularity, when a standards committee creates a new norm, when data
reveals a new pattern: Nexus brings forth NEW Forma. Originates is
Whitehead's creativity as a bridge relation.

---

## 4 — Latour (1947–2022)

**Borrowed:** Actant, Médiation technique, Symmetry principle.

Latour's actor-network theory (ANT) provides MIN's concept of agency.

**Actant → Agent.** Latour's actant — anything that makes a difference,
regardless of whether it is human, machine, or text — maps onto MIN's
`Agent`. A cook is an Agent. A CNC machine is an Agent. An ML model is
an Agent. Corrosion, if it transforms selectively, is an Agent.

The crucial Latourian move MIN preserves: *no intentionality required*.
A thermostat has agency but no intention. An organisation acts but has
no consciousness. Agency is about selective, accountable causal
effectiveness — not about minds.

**Médiation technique → Boundary.** Latour's concept of technical
mediation — where the mediator is an independent actant, not a neutral
channel — informs MIN's `Boundary`. The heat transfer between water and
egg is not a passive connection; it is an independent phenomenon with
its own causal power. Like Latour's mediators, Boundary is irreducibly
relational and causally autonomous.

**Symmetry Principle → Agent as Cross-Cutting Category.** Latour
insisted on treating human and non-human actants symmetrically. MIN
follows this: Agent is not a category of being (like Object or Lex)
but a category of action. Agent traverses the branch boundary. A
human is Agent ∩ Object. An organisation is Agent ∩ Institutio. An ML
model is Agent ∩ Data. The co-typing requirement ensures that every
Agent has a mode of being — but agency itself is orthogonal to being.

---

## 5 — Searle (1932–2022)

**Borrowed:** Institutional Facts, Constitutive Rules, Collective
Recognition.

Searle provides the theoretical foundation for MIN's `Institutio`.

**Institutional Facts → Institutio.** Searle distinguished brute facts
(the stone weighs 5 kg) from institutional facts (this piece of paper
is money). Institutional facts exist only because agents collectively
recognise them. MIN maps this directly: `Institutio` is everything that
exists through collective recognition and ceases to exist when nobody
recognises it any longer.

**"X counts as Y in context C" → typifies.** Searle's constitutive
rule formula becomes MIN's `min:typifies`. A steel sheet (X) counts as
DC04 (Y) in the context of metallurgy (C). A boiled egg (X) counts as
soft-boiled (Y) in the context of the kitchen (C). Typification is an
institutional act — it assigns a type determination that is
conventionally, not naturally, given.

**Constitutive Rules → comprises.** Searle's constitutive rules —
the rules that create the very possibility of an activity (as opposed
to regulative rules that govern pre-existing activities) — inform
MIN's `min:comprises`. DC04 comprises Norma(C ≤ 0.08%),
Structura(bcc-ferrite), Lex(diffusion behaviour). The bundling of
atomic Forma instances into a type determination is a constitutive act.
Without it, DC04 does not exist — only isolated requirements do.

**The Annihilation Test.** Searle's analysis also drives a key
architectural decision in MIN v1.0: Agent's promotion from Nexus to
Entity. An organisation acts (Agent) AND is recognised (Institutio).
The annihilation test — delete the trade register entry and both the
agency and the institutional existence vanish — shows that these have
the same annihilation condition. What has the same annihilation
condition is the same thing. Therefore Agent must stand above the
branch boundary, and co-typing (Agent ∩ Institutio) must be possible
in a single node.

---

## 6 — Kripke (1940–2022) / Lewis (1941–2001)

**Borrowed:** Possible Worlds, Modal Semantics.

Kripke and Lewis provide the theoretical backbone for MIN's `Possibile`.

**Possible Worlds → Possibile.** Kripke's possible worlds semantics —
the idea that modal statements ("it could be the case that…") can be
understood as statements about alternative states of affairs — maps
onto MIN's `Possibile`. A failure scenario for a component is a
Possibile: it could happen but has not happened. A design alternative
is a Possibile: it could have been chosen but was not.

MIN does not commit to Lewis's modal realism (the thesis that all
possible worlds are equally real). Possibile is a Forma category: it
determines what could be, without claiming that alternative worlds
literally exist. If a Possibile is realised — if the failure actually
occurs — it becomes a Process (Nexus). The transition from Possibile
to Process is `min:realizes`.

**Counterfactual Reasoning.** The Kripke/Lewis framework also
underpins MIN's `min:concerns` (a Possibile concerns an actual Nexus)
and `min:alternativeTo` (a Possibile is an alternative to an actual
Nexus). Both relations express counterfactual thinking: what would be
different if things were otherwise?

---

## 7 — Woodward (b. 1951)

**Borrowed:** Interventionist Causation.

Woodward's interventionist theory of causation provides MIN's
existence criterion for Nexus.

**Interventionist Causation → "Does it cause effects?"** Woodward
defines causal relevance as follows: X is causally relevant for Y if
an intervention on X would change Y. MIN adopts this as the existence
criterion for the Nexus branch: if an intervention on the entity
would change something else, it is Nexus.

This is what makes MIN's Nexus branch broader than a materialist
ontology. A shadow is Nexus — intervene on the shadow (move the
obstacle) and downstream effects change. A vacuum is Nexus — intervene
on the vacuum (break it) and processes change. An electromagnetic
field is Nexus. None of these are made of matter in the ordinary
sense, but all pass the interventionist test.

**Three Causality Modes.** Woodward's framework also motivates MIN's
differentiation of causal modes within Nexus. Not all Nexus categories
cause effects in the same way:

- **Dispositional** — Object and Process cause or could cause effects
  even without an agent. A steel sheet has mass whether or not anyone
  measures it.
- **Mediated** — Data causes effects ONLY through an interpreting
  agent. A hard drive sector with random bits is physically identical
  to one containing a digital product passport. The causal difference
  lies in the agent who interprets the bytes.
- **Relational** — Boundary causes effects ONLY between partners.
  Remove one partner and the boundary vanishes.

These three modes make Data's special role as the hinge between Nexus
and Forma explicit: Data is actual (has bytes) but causally dependent
on agents (mediated), which places it closer to Forma than the other
Nexus categories.

---

## 8 — Popper (1902–1994)

**Borrowed:** Falsificationism, Corroboration.

Popper provides the epistemological layer that MIN v1.0.0 adds on top
of its ontological architecture.

**Falsification → refutes.** Popper's central thesis — that scientific
knowledge grows through the refutation of hypotheses — maps onto
MIN's `min:refutes`. A process (experiment, analysis, first-principles
reasoning) refutes a Possibile. The range is specifically Possibile,
not Forma in general, because only Possibilia have the epistemic
status "could be the case" that can be overturned by refutation.

**Corroboration → confirms.** Popper distinguished verification
(impossible) from corroboration (a hypothesis withstands attempts at
falsification). MIN maps this onto `min:confirms`. A process confirms
that a Forma is tenable as a foundation — but this is corroboration,
not proof. A confirmed Forma can be refuted by later processes.

**Falsificationism as Architecture.** The confirms/refutes pair
completes the Forma lifecycle in MIN:

```
originates  — Forma comes into being    (Whitehead: creativity)
constrains  — Forma takes effect        (Aristotle: morphe shapes hyle)
realizes    — Forma becomes actual      (Whitehead: ingression)
confirms    — Forma withstands scrutiny (Popper: corroboration)
refutes     — Forma fails scrutiny      (Popper: falsification)
supersedes  — Forma replaces Forma      (Kuhn: paradigm shift)
```

MIN is itself a product of this cycle. The decision to handle
typification via Institutio was a first-principles process that
confirmed Searle's constitutive rule principle: classification is
an institutional act. MIN models its own epistemological evolution
with its own relations.

---

## The Synthesis

No single philosopher provides all of MIN. The synthesis is the
contribution:

| Philosopher | What MIN borrows | Where it appears |
|---|---|---|
| Aristotle | Matter/Form, Substance, Motion, Cause, Essence | Polarity, Entity, Process, causal thinking, Institutio (eidos role), entails |
| Spinoza | One substance, two attributes | Polarity as dual aspect, not dual substance |
| Whitehead | Actual Entity, Eternal Object, Process, Creativity | Nexus, Forma, Process, originates, realizes |
| Latour | Actant, Mediation, Symmetry | Agent (no intentionality required), Boundary, Agent as cross-cutting category |
| Searle | Institutional Facts, "X counts as Y in C" | Institutio, typifies, comprises, Agent ∩ Institutio |
| Kripke/Lewis | Possible Worlds | Possibile, concerns, alternativeTo |
| Woodward | Interventionist Causation | Nexus existence criterion, three causality modes |
| Popper | Falsification, Corroboration | refutes, confirms, epistemic lifecycle |

What holds them together is the question MIN asks: *"Does it cause
effects?"* — and its complement: *"Does it determine how effects
work?"* The first question carves out Nexus (Woodward, Whitehead,
Latour). The second carves out Forma (Whitehead, Aristotle, Searle,
Kripke). Agent traverses both (Latour, Searle). And the epistemic
relations track what we know about the whole structure (Popper,
Aristotle).

**No metaphysics. Tools. Built on 2,400 years of thinking about
what there is, what it does, and how we know.**

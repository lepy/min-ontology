#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from rdflib import Graph, Namespace
from rdflib.namespace import OWL, RDF, RDFS

MIN = Namespace("https://w3id.org/min#")
ONTOLOGY_IRI = "https://w3id.org/min"

KNOWN_NEXUS_ORDER = ["Object", "Process", "Data", "Agent", "Boundary"]
KNOWN_FORMA_ORDER = ["Lex", "Structura", "Possibile", "Norma", "Institutio"]


def _local_name(uri: str) -> str:
    if "#" in uri:
        return uri.rsplit("#", 1)[1]
    return uri.rsplit("/", 1)[-1]


def _class_names(g: Graph) -> set[str]:
    names: set[str] = set()
    for cls in g.subjects(RDF.type, OWL.Class):
        s = str(cls)
        if s.startswith(str(MIN)):
            names.add(_local_name(s))
    return names


def _direct_subclasses(g: Graph, parent: str) -> set[str]:
    target = MIN[parent]
    names: set[str] = set()
    for cls in g.subjects(RDFS.subClassOf, target):
        s = str(cls)
        if s.startswith(str(MIN)):
            names.add(_local_name(s))
    return names


def _ordered(branch: set[str], preferred: list[str]) -> list[str]:
    present_preferred = [name for name in preferred if name in branch]
    extra = sorted(name for name in branch if name not in preferred)
    return present_preferred + extra


def _ontology_version(g: Graph) -> str:
    ontology_node = Namespace(ONTOLOGY_IRI)[""]
    for lit in g.objects(ontology_node, OWL.versionInfo):
        return str(lit)

    for subj in g.subjects(RDF.type, OWL.Ontology):
        for lit in g.objects(subj, OWL.versionInfo):
            return str(lit)

    return "unknown"


def build_dot(version: str, nexus_classes: list[str], forma_classes: list[str]) -> str:
    forma_note = f"⊥ alle {len(forma_classes)} paarweise disjunkt"

    lines: list[str] = []
    lines.append("digraph MIN {")
    lines.append("    rankdir=TB;")
    lines.append('    bgcolor="transparent";')
    lines.append("    pad=0.4;")
    lines.append("    nodesep=0.3;")
    lines.append("    ranksep=0.65;")
    lines.append("    splines=true;")
    lines.append("")
    lines.append('    graph [fontname="Helvetica Neue, Helvetica, Arial, sans-serif"];')
    lines.append('    node  [fontname="Helvetica Neue, Helvetica, Arial, sans-serif"];')
    lines.append('    edge  [fontname="Helvetica Neue, Helvetica, Arial, sans-serif"];')
    lines.append("")
    lines.append("    node [")
    lines.append('        shape=box, style="rounded,filled", penwidth=1.5,')
    lines.append('        fontsize=11, height=0.42, margin="0.10,0.06"')
    lines.append("    ];")
    lines.append("    edge [ penwidth=1.2, arrowsize=0.55 ];")
    lines.append("")
    lines.append("    // ── ENTITY ──────────────────────────────────────────────")
    lines.append("    Entity [")
    lines.append('        label=<<B>Entity</B><BR/><FONT POINT-SIZE="8" COLOR="#777777">∃hasIdentifier ≥ 1</FONT>>,')
    lines.append('        fillcolor="#f0ebe3", color="#9c8b75", fontcolor="#3d3225",')
    lines.append("        fontsize=13, penwidth=2.0, width=2.0")
    lines.append("    ];")
    lines.append("")
    lines.append("    // ── NEXUS ───────────────────────────────────────────────")
    lines.append("    subgraph cluster_nexus {")
    lines.append('        label=<<TABLE BORDER="0" CELLPADDING="1"><TR>')
    lines.append('            <TD><B><FONT POINT-SIZE="11" COLOR="#1a5276">Nexus</FONT></B></TD>')
    lines.append('            <TD><FONT POINT-SIZE="9" COLOR="#5499c7">  ·  das, was etwas bewirkt</FONT></TD>')
    lines.append('        </TR><TR>')
    lines.append('            <TD COLSPAN="2"><FONT POINT-SIZE="7.5" COLOR="#aabbcc">⊥ Object · Process · Data · Boundary  ┃  Agent überlappt</FONT></TD>')
    lines.append("        </TR></TABLE>>;")
    lines.append('        fontsize=11; fontcolor="#1a5276";')
    lines.append('        style="rounded"; color="#85c1e9"; bgcolor="#f4f9ff";')
    lines.append("        margin=14; penwidth=1.4;")
    lines.append("")
    lines.append("        Nexus [")
    lines.append('            label=<<B>Nexus</B><BR/><FONT POINT-SIZE="8" COLOR="#666666">kausale Wirksamkeit</FONT>>,')
    lines.append('            fillcolor="#d6eaf8", color="#2e86c1", fontcolor="#1a3c5e",')
    lines.append("            fontsize=12, penwidth=1.8, width=1.7")
    lines.append("        ];")
    lines.append("")

    for name in nexus_classes:
        if name == "Agent":
            lines.append("        Agent [")
            lines.append('            label=<<B>Agent</B>>,')
            lines.append('            fillcolor="#fdebd0", color="#e67e22", fontcolor="#7e4a12",')
            lines.append('            style="rounded,filled,dashed", penwidth=1.6')
            lines.append("        ];")
        else:
            lines.append(
                f'        {name} [ label=<<B>{name}</B>>, fillcolor="#d5f5e3", color="#28b463", fontcolor="#186a3b" ];'
            )
    lines.append("    }")
    lines.append("")

    lines.append("    // ── FORMA ───────────────────────────────────────────────")
    lines.append("    subgraph cluster_forma {")
    lines.append('        label=<<TABLE BORDER="0" CELLPADDING="1"><TR>')
    lines.append('            <TD><B><FONT POINT-SIZE="11" COLOR="#6c3483">Forma</FONT></B></TD>')
    lines.append('            <TD><FONT POINT-SIZE="9" COLOR="#a569bd">  ·  das Regelwerk</FONT></TD>')
    lines.append('        </TR><TR>')
    lines.append(f'            <TD COLSPAN="2"><FONT POINT-SIZE="7.5" COLOR="#c5aacc">{forma_note}</FONT></TD>')
    lines.append("        </TR></TABLE>>;")
    lines.append('        fontsize=11; fontcolor="#6c3483";')
    lines.append('        style="rounded"; color="#bb8fce"; bgcolor="#fcf7ff";')
    lines.append("        margin=14; penwidth=1.4;")
    lines.append("")
    lines.append("        Forma [")
    lines.append('            label=<<B>Forma</B><BR/><FONT POINT-SIZE="8" COLOR="#666666">konstitutive Bestimmung</FONT>>,')
    lines.append('            fillcolor="#e8daef", color="#7d3c98", fontcolor="#4a235a",')
    lines.append("            fontsize=12, penwidth=1.8, width=1.7")
    lines.append("        ];")
    lines.append("")

    for name in forma_classes:
        lines.append(
            f'        {name} [ label=<<B>{name}</B>>, fillcolor="#f0e6f6", color="#8e44ad", fontcolor="#4a235a" ];'
        )
    lines.append("    }")
    lines.append("")

    lines.append("    // ── Edges ───────────────────────────────────────────────")
    lines.append('    Entity -> Nexus  [color="#2e86c1", penwidth=1.8];')
    lines.append('    Entity -> Forma  [color="#7d3c98", penwidth=1.8];')
    lines.append("")
    for name in nexus_classes:
        if name == "Agent":
            lines.append('    Nexus -> Agent    [color="#e67e22", style=dashed, penwidth=1.3];')
        else:
            lines.append(f'    Nexus -> {name} [color="#28b463"];')
    lines.append("")
    for name in forma_classes:
        lines.append(f'    Forma -> {name} [color="#8e44ad"];')
    lines.append("")

    lines.append("    // ── Rank ────────────────────────────────────────────────")
    lines.append("    { rank=same; Nexus; Forma; }")
    lines.append("")
    lines.append("    // ── Title ───────────────────────────────────────────────")
    lines.append("    labelloc=t;")
    lines.append(
        f'    label=<<FONT POINT-SIZE="16"><B>MIN — Material · Information · Nexus</B></FONT><BR/><FONT POINT-SIZE="10" COLOR="#888888">Klassenhierarchie · v{version}  ┃  Entity ≡ Nexus ⊔ Forma</FONT><BR/> >;'
    )
    lines.append("}")

    return "\n".join(lines) + "\n"


def build_mermaid(nexus_classes: list[str], forma_classes: list[str]) -> str:
    lines: list[str] = []
    lines.append("```mermaid")
    lines.append("graph TD")
    lines.append('    Entity["<b>Entity</b><br/><small>∃hasIdentifier ≥ 1</small>"]')
    lines.append('    Nexus["<b>Nexus</b><br/><small>kausale Wirksamkeit</small>"]')
    lines.append('    Forma["<b>Forma</b><br/><small>konstitutive Bestimmung</small>"]')
    lines.append("")

    for name in nexus_classes:
        lines.append(f'    {name}["{name}"]')
    lines.append("")
    for name in forma_classes:
        lines.append(f'    {name}["{name}"]')
    lines.append("")

    lines.append("    Entity --> Nexus")
    lines.append("    Entity --> Forma")
    lines.append("")
    for name in nexus_classes:
        if name == "Agent":
            lines.append("    Nexus -.-> Agent")
        else:
            lines.append(f"    Nexus --> {name}")
    lines.append("")
    for name in forma_classes:
        lines.append(f"    Forma --> {name}")
    lines.append("")

    lines.append("    style Entity fill:#f0ebe3,stroke:#9c8b75,color:#3d3225,stroke-width:2px")
    lines.append("    style Nexus fill:#d6eaf8,stroke:#2e86c1,color:#1a3c5e,stroke-width:2px")
    lines.append("    style Forma fill:#e8daef,stroke:#7d3c98,color:#4a235a,stroke-width:2px")
    lines.append("")

    for name in nexus_classes:
        if name == "Agent":
            lines.append(
                "    style Agent fill:#fdebd0,stroke:#e67e22,color:#7e4a12,stroke-width:2px,stroke-dasharray: 5 5"
            )
        else:
            lines.append(f"    style {name} fill:#d5f5e3,stroke:#28b463,color:#186a3b")
    lines.append("")

    for name in forma_classes:
        lines.append(f"    style {name} fill:#f0e6f6,stroke:#8e44ad,color:#4a235a")
    lines.append("```")
    lines.append("")
    lines.append("**Legende:**")
    lines.append("`━━` rdfs:subClassOf (disjunkt) · `╌╌` rdfs:subClassOf (überlappt — Agent)")
    lines.append("⊥ Object · Process · Data · Boundary paarweise disjunkt · Agent überlappt")
    lines.append(
        f"⊥ {' · '.join(forma_classes)} paarweise disjunkt"
    )
    lines.append("Entity ≡ Nexus ⊔ Forma")
    lines.append("")

    return "\n".join(lines)


def render_svg(dot_path: Path, svg_path: Path) -> None:
    if shutil.which("dot") is None:
        raise RuntimeError("Graphviz 'dot' command not found. Install graphviz to render SVG.")
    subprocess.run(["dot", "-Tsvg", str(dot_path), "-o", str(svg_path)], check=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate MIN hierarchy DOT/Mermaid/SVG from ontology classes."
    )
    parser.add_argument("--ttl", default="min.ttl", help="Input ontology Turtle file")
    parser.add_argument("--dot", default="docs/min_hierarchy.dot", help="Output DOT file")
    parser.add_argument("--mmd", default="docs/min_hierarchy.mmd", help="Output Mermaid file")
    parser.add_argument("--svg", default="docs/min_hierarchy.svg", help="Output SVG file")
    parser.add_argument(
        "--skip-svg", action="store_true", help="Only write DOT/Mermaid, do not render SVG"
    )
    args = parser.parse_args()

    ttl_path = Path(args.ttl)
    dot_path = Path(args.dot)
    mmd_path = Path(args.mmd)
    svg_path = Path(args.svg)

    if not ttl_path.exists():
        print(f"Input ontology not found: {ttl_path}", file=sys.stderr)
        return 1

    g = Graph()
    g.parse(ttl_path, format="turtle")

    classes = _class_names(g)
    if not {"Entity", "Nexus", "Forma"}.issubset(classes):
        print("Ontology is missing one of required classes: Entity, Nexus, Forma", file=sys.stderr)
        return 1

    nexus_classes = _ordered(_direct_subclasses(g, "Nexus"), KNOWN_NEXUS_ORDER)
    forma_classes = _ordered(_direct_subclasses(g, "Forma"), KNOWN_FORMA_ORDER)

    version = _ontology_version(g)

    dot_path.parent.mkdir(parents=True, exist_ok=True)
    mmd_path.parent.mkdir(parents=True, exist_ok=True)

    dot_path.write_text(build_dot(version, nexus_classes, forma_classes), encoding="utf-8")
    mmd_path.write_text(build_mermaid(nexus_classes, forma_classes), encoding="utf-8")

    if not args.skip_svg:
        try:
            render_svg(dot_path, svg_path)
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return 2

    print(f"Wrote {dot_path}")
    print(f"Wrote {mmd_path}")
    if not args.skip_svg:
        print(f"Wrote {svg_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

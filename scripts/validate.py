#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

from pyshacl import validate
from rdflib import Graph

ROOT = Path(__file__).resolve().parents[1]

TTL_FILES = [
    "min.ttl",
    "min-v1.0.0.ttl",
    "examples/min-example.ttl",
    "examples/min-v1.0.0-examples.ttl",
    "examples/min-examples.ttl",
    "examples/object.ttl",
    "examples/process.ttl",
    "examples/data.ttl",
    "examples/agent.ttl",
    "examples/boundary.ttl",
    "examples/lex.ttl",
    "examples/structura.ttl",
    "examples/possibile.ttl",
    "examples/norma.ttl",
    "examples/institutio.ttl",
    "shapes/min-core.shacl.ttl",
    "shapes/min-instance.shacl.ttl",
]

SPARQL_TESTS = [
    ("tests/sparql/test-min-version.rq", "min.ttl"),
    ("tests/sparql/test-min-metadata.rq", "min.ttl"),
    ("tests/sparql/test-min-domain-range.rq", "min.ttl"),
    ("tests/sparql/test-min-classes.rq", "min.ttl"),
    ("tests/sparql/test-min-polarity-superproperties.rq", "min.ttl"),
    ("tests/sparql/test-min-forma-classes.rq", "min.ttl"),
    ("tests/sparql/test-min-entity-partition.rq", "min.ttl"),
    ("tests/sparql/test-min-disjointness.rq", "min.ttl"),
    ("tests/sparql/test-min-bridge-relations.rq", "min.ttl"),
    ("tests/sparql/test-min-inverse-properties.rq", "min.ttl"),
]


def parse_turtle(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def run_sparql_ask(query_file: Path, data_file: Path) -> bool:
    graph = parse_turtle(data_file)
    query = query_file.read_text(encoding="utf-8")
    result = graph.query(query)
    return bool(result.askAnswer)


def main() -> int:
    failures = 0

    print("[1/4] Parsing Turtle files")
    for rel in TTL_FILES:
        path = ROOT / rel
        try:
            parse_turtle(path)
            print(f"  OK  {rel}")
        except Exception as exc:  # pragma: no cover
            failures += 1
            print(f"  ERR {rel}: {exc}")

    print("[2/4] Running SPARQL ASK tests")
    for query_rel, data_rel in SPARQL_TESTS:
        query_file = ROOT / query_rel
        data_file = ROOT / data_rel
        try:
            passed = run_sparql_ask(query_file, data_file)
            if passed:
                print(f"  OK  {query_rel} on {data_rel}")
            else:
                failures += 1
                print(f"  ERR {query_rel} on {data_rel}: ASK returned false")
        except Exception as exc:  # pragma: no cover
            failures += 1
            print(f"  ERR {query_rel} on {data_rel}: {exc}")

    print("[3/4] Running Core-SHACL validation")
    data_graph = parse_turtle(ROOT / "min.ttl")
    shapes_graph = parse_turtle(ROOT / "shapes/min-core.shacl.ttl")
    conforms, _, report_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference="rdfs",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )
    if conforms:
        print("  OK  SHACL shapes conform for min.ttl")
    else:
        failures += 1
        print("  ERR Core-SHACL validation failed")
        print(report_text)

    print("[4/4] Running Instance-SHACL validation")
    instance_shapes = parse_turtle(ROOT / "shapes/min-instance.shacl.ttl")
    example_files = [
        "examples/min-v1.0.0-examples.ttl",
        "examples/object.ttl",
        "examples/process.ttl",
        "examples/data.ttl",
        "examples/agent.ttl",
        "examples/boundary.ttl",
        "examples/lex.ttl",
        "examples/structura.ttl",
        "examples/possibile.ttl",
        "examples/norma.ttl",
        "examples/institutio.ttl",
    ]
    for ex_rel in example_files:
        instance_graph = parse_turtle(ROOT / "min.ttl")
        instance_graph.parse(ROOT / ex_rel, format="turtle")
        conforms, _, report_text = validate(
            instance_graph,
            shacl_graph=instance_shapes,
            inference="rdfs",
            abort_on_first=False,
            allow_infos=False,
            allow_warnings=True,
        )
        if conforms:
            print(f"  OK  Instance-SHACL: {ex_rel}")
        else:
            failures += 1
            print(f"  ERR Instance-SHACL: {ex_rel}")
            print(report_text)

    if failures:
        print(f"Validation finished with {failures} error(s).")
        return 1

    print("Validation successful.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

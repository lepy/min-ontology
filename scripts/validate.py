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
    "min-v2.0.0.ttl",
    "examples/min-example.ttl",
    "shapes/min-core.shacl.ttl",
]

SPARQL_TESTS = [
    ("tests/sparql/test-min-version.rq", "min.ttl"),
    ("tests/sparql/test-min-metadata.rq", "min.ttl"),
    ("tests/sparql/test-min-domain-range.rq", "min.ttl"),
    ("tests/sparql/test-min-classes-v2.rq", "min.ttl"),
    ("tests/sparql/test-min-no-opa-import.rq", "min.ttl"),
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

    print("[1/3] Parsing Turtle files")
    for rel in TTL_FILES:
        path = ROOT / rel
        try:
            parse_turtle(path)
            print(f"  OK  {rel}")
        except Exception as exc:  # pragma: no cover
            failures += 1
            print(f"  ERR {rel}: {exc}")

    print("[2/3] Running SPARQL ASK tests")
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

    print("[3/3] Running SHACL validation")
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
        print("  ERR SHACL validation failed")
        print(report_text)

    if failures:
        print(f"Validation finished with {failures} error(s).")
        return 1

    print("Validation successful.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

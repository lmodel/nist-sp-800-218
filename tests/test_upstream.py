"""Checks that the schema renders the SSDF version NIST's catalog publishes.

NIST publishes SP 800-218 version 1.1 as an OSCAL catalog in
usnistgov/oscal-content, and src/nist_sp_800_218/schema/oscal-content/ holds
the copy that scripts/check_upstream_release.py pins. These tests read the
copy with the standard library alone, derive from it the SsdfFramework the
schema describes, and hold that framework to the validator and to the counts
of the publication's table.
"""

import importlib.util
import json
import re
from functools import cache, lru_cache
from pathlib import Path

import yaml
from linkml.validator import validate

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "nist_sp_800_218" / "schema" / "nist_sp_800_218.yaml"
COPY = ROOT / "src" / "nist_sp_800_218" / "schema" / "oscal-content"
CATALOG = COPY / "NIST_SP800-218_ver1_catalog.json"

# The catalog appends a moved task's former identifier to its statement, as
# " .Formerly PW.3.1", where the publication writes "[Formerly PW.3.1]".
FORMERLY = re.compile(r"\s*\.?\s*Formerly\s+((?:PO|PS|PW|RV)\.\d+\.\d+)\s*$")

# What SP 800-218 version 1.1 holds: its table's practice groups, practices,
# tasks, notional implementation examples and references, and the tasks it
# notes it moved, by their former identifiers.
COUNTS = {
    "practice groups": 4,
    "practices": 19,
    "tasks": 42,
    "implementation examples": 198,
    "references": 528,
    "reference documents": 29,
}
MOVED = {"PO.1.3": ["PW.3.1"], "PW.1.3": ["PW.4.3"]}


@cache
def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _header():
    return yaml.safe_load(SCHEMA.read_text())


@lru_cache(maxsize=1)
def _catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))["catalog"]


def _prop(element, name):
    return next(p["value"] for p in element.get("props", []) if p["name"] == name)


def _prose(element, name):
    """The prose of the one part of the element with this name."""
    (text,) = [p["prose"] for p in element.get("parts", []) if p["name"] == name]
    return text


def derive(catalog):
    """The SsdfFramework that the catalog's groups, controls, parts and links
    describe, in the schema's terms."""
    resources = {r["uuid"]: r for r in catalog["back-matter"]["resources"]}
    version = _header()["version"]
    groups = []
    for group in catalog["groups"]:
        practices = []
        for practice in group["controls"]:
            assert practice["class"] == "practice", practice["id"]
            tasks = []
            for task in practice["controls"]:
                assert task["class"] == "task", task["id"]
                statement = _prose(task, "statement")
                former = FORMERLY.findall(statement)
                entry = {
                    "task_id": task["id"],
                    "description": FORMERLY.sub("", statement),
                    "implementation_examples": [
                        {"example_id": part["id"], "description": part["prose"]}
                        for part in task["parts"]
                        if part["name"] == "example"
                    ],
                    "task_references": [
                        {
                            "reference_document": resources[link["href"].lstrip("#")][
                                "title"
                            ],
                            "mapped_items": link["text"],
                        }
                        for link in task.get("links", [])
                        if link["rel"] == "external_reference"
                    ],
                }
                if former:
                    entry["former_task_ids"] = former
                tasks.append(entry)
            practices.append(
                {
                    "practice_id": practice["id"],
                    "title": practice["title"],
                    "description": _prose(practice, "statement"),
                    "practice_tasks": tasks,
                }
            )
        groups.append(
            {
                "group_id": group["id"],
                "title": group["title"],
                "description": _prose(group, "overview"),
                "group_practices": practices,
            }
        )
    return {
        "ssdf_version": ".".join(version.split(".")[:2]),
        "practice_groups": groups,
    }


@lru_cache(maxsize=1)
def _framework():
    return derive(_catalog())


def _practices():
    return [p for g in _framework()["practice_groups"] for p in g["group_practices"]]


def _tasks():
    return [t for p in _practices() for t in p["practice_tasks"]]


def test_copy_matches_the_pinned_blobs():
    """Every copied file has the git object hash the watch pins, so the copy
    is the file NIST published at the pinned commit, and nothing else is in
    the folder."""
    watch = _watch()
    pinned = watch.PINNED_BLOBS
    assert {p.name for p in COPY.iterdir()} == set(pinned)
    for name, (_source, sha) in pinned.items():
        assert watch._blob_sha(COPY / name) == sha, name


def test_header_pins_match_the_watch():
    """The header records the release, commit and publication the watch
    checks."""
    watch = _watch()
    header = _header()
    notes = header["annotations"]
    assert notes["oscal_content_tag"] == watch.PINNED_TAG
    assert notes["oscal_content_commit"] == watch.PINNED_COMMIT
    assert header["source"] == f"https://doi.org/{watch.PINNED_DOI}"
    tree = f"https://github.com/usnistgov/oscal-content/tree/{watch.PINNED_TAG}/"
    assert tree + watch.PINNED_PATH.rpartition("/")[0] in header["see_also"]


def test_catalog_is_the_pinned_edition():
    """The copy is NIST's final catalog of the version in the header, by the
    identifier NIST's reference tool gives that version."""
    metadata = _catalog()["metadata"]
    version = _header()["version"]
    identifier = "SP_800_218_" + version.replace(".", "_")
    assert _header()["annotations"]["cprt_framework_version"] == identifier
    assert _prop(metadata, "framework-version-identifier") == identifier
    assert _prop(metadata, "publication-status") == "Final"


def test_derived_framework_validates():
    """The whole of version 1.1, as the catalog gives it, is a valid
    SsdfFramework."""
    report = validate(_framework(), str(SCHEMA), "SsdfFramework")
    assert not report.results, [r.message for r in report.results][:10]


def test_counts_match_the_publication():
    """The derived framework holds what the publication's table holds."""
    tasks = _tasks()
    references = [r for t in tasks for r in t["task_references"]]
    counted = {
        "practice groups": len(_framework()["practice_groups"]),
        "practices": len(_practices()),
        "tasks": len(tasks),
        "implementation examples": sum(
            len(t["implementation_examples"]) for t in tasks
        ),
        "references": len(references),
        "reference documents": len({r["reference_document"] for r in references}),
    }
    assert counted == COUNTS


def test_reference_documents_are_the_enum():
    """The enum holds exactly the documents the catalog's references list."""
    enum = _header()["enums"]["SsdfReferenceDocument"]["permissible_values"]
    cited = {
        r["title"] for r in _catalog()["back-matter"]["resources"] if "citation" in r
    }
    used = {r["reference_document"] for t in _tasks() for r in t["task_references"]}
    assert set(enum) == cited == used


def test_identifiers_nest_and_are_unique():
    """Each identifier starts with the identifier of what holds it, which no
    pattern in the schema can check, and none repeats."""
    seen = []
    for group in _framework()["practice_groups"]:
        seen.append(group["group_id"])
        for practice in group["group_practices"]:
            assert practice["practice_id"].startswith(group["group_id"] + ".")
            seen.append(practice["practice_id"])
            for task in practice["practice_tasks"]:
                assert task["task_id"].startswith(practice["practice_id"] + ".")
                seen.append(task["task_id"])
                for example in task["implementation_examples"]:
                    assert example["example_id"].startswith(task["task_id"] + ".")
                    seen.append(example["example_id"])
    assert len(seen) == len(set(seen))


def test_moved_tasks_keep_their_former_identifiers():
    """The two tasks the publication marks as moved carry their former
    identifiers, and no other task does."""
    moved = {
        t["task_id"]: t["former_task_ids"] for t in _tasks() if "former_task_ids" in t
    }
    assert moved == MOVED
    assert not any("Formerly" in t["description"] for t in _tasks())

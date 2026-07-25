"""The SKILL.md contract.

A skill is installed and run by a model, so its guarantees live in the markdown,
not only in the Python. These tests assert the promises the skill makes about
itself hold in the file itself — the same properties tools/validate_skill.py
checks, kept here so a contributor running pytest sees them too.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def _split():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "frontmatter must be present and delimited"
    return yaml.safe_load(m.group(1)), text[m.end():]


def test_canonical_filename():
    # Strict skill-discovery tooling looks for uppercase SKILL.md.
    assert SKILL.exists(), "SKILL.md must exist at the repository root"


def test_frontmatter_required_and_recommended_fields():
    fm, _ = _split()
    for f in ("name", "description"):
        assert f in fm, f"frontmatter must declare '{f}'"
    for f in ("license", "version"):
        assert f in fm, f"frontmatter should declare '{f}'"
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_name_is_slug_safe():
    fm, _ = _split()
    assert re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm["name"]))


def test_metadata_declares_scope_and_compatibility():
    fm, _ = _split()
    meta = fm.get("metadata", {})
    assert meta.get("compatibility"), "metadata.compatibility must state where it runs"
    assert meta.get("not_for"), "metadata.not_for must bound the skill's scope"


def test_body_requires_scenarios_and_invalidation():
    _, body = _split()
    assert re.search(r"scenario", body, re.I)
    assert re.search(r"invalidation", body, re.I)
    assert re.search(r"uncertaint|confidence", body, re.I)


def test_body_degrades_honestly_without_data():
    _, body = _split()
    assert re.search(r"insufficient|no live data|abstain", body, re.I), \
        "the skill must declare what it does when data is missing"


def test_body_declines_personalized_advice():
    _, body = _split()
    assert re.search(r"not.{0,20}(financial|investment) advice|does not issue", body, re.I)

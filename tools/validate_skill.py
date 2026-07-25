#!/usr/bin/env python3
"""
validate_skill.py — integrity checks for Money Atlas Intelligence OS.

READ-ONLY. Never modifies SKILL.md. Verifies the skill is installable
(frontmatter well-formed) and that its safety-relevant structure is intact.

Run:  python tools/validate_skill.py
Exit: 0 pass · 1 fail
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # pragma: no cover
    pass

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
# The Claude/Anthropic standard filename is SKILL.md (uppercase). A lowercase
# skill.md is tolerated by a case-insensitive filesystem but missed by strict
# discovery tooling, so the canonical name is preferred and the old one is a
# fallback only.
SKILL = ROOT / "SKILL.md"
if not SKILL.exists() and (ROOT / "skill.md").exists():
    SKILL = ROOT / "skill.md"
REQUIRED = ["name", "description"]
RECOMMENDED = ["license", "version"]

results: list[tuple[str, bool]] = []


def check(name: str, cond: bool) -> None:
    results.append((name, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")


def main() -> int:
    if not SKILL.exists():
        print(f"FATAL: SKILL.md not found at {SKILL}")
        return 1
    text = SKILL.read_text(encoding="utf-8")

    print("\nINSTALLABILITY")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check("frontmatter present and delimited", m is not None)
    if not m:
        return 1
    try:
        fm = yaml.safe_load(m.group(1))
        check("frontmatter is valid YAML", isinstance(fm, dict))
    except yaml.YAMLError:
        check("frontmatter is valid YAML", False)
        return 1
    for f in REQUIRED:
        check(f"frontmatter has '{f}'", f in fm)
    check("name is slug-safe (a-z0-9-)",
          bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm.get("name", "")))))
    for f in RECOMMENDED:
        check(f"frontmatter declares '{f}'", f in fm)
    check("license is Apache-2.0 (matches LICENSE file)",
          str(fm.get("license", "")).lower().replace(" ", "-") == "apache-2.0")
    check("canonical filename is SKILL.md", SKILL.name == "SKILL.md")

    body = text[m.end():]
    print("\nINTEGRITY")
    check("activation modes declared", "LIGHT MODE" in body and "FULL MODE" in body)
    check("output requires explicit uncertainty",
          re.search(r"uncertaint|confidence", body, re.I) is not None)
    check("output requires scenarios",
          re.search(r"scenario", body, re.I) is not None)
    check("output requires an invalidation point",
          re.search(r"invalidation", body, re.I) is not None)
    check("declares graceful degradation when data is insufficient",
          re.search(r"insufficient|no live data|abstention|abstain", body, re.I) is not None)
    check("declares it is not personalized investment advice",
          re.search(r"not.{0,20}(financial|investment) advice|does not issue", body, re.I) is not None)

    print("\nREPOSITORY")
    check("LICENSE exists", (ROOT / "LICENSE").exists())
    check("NOTICE exists", (ROOT / "NOTICE").exists())
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8") if (ROOT / "NOTICE").exists() else ""
    # A markets tool must carry an explicit not-advice disclaimer.
    check("NOTICE carries the not-financial-advice disclaimer",
          "NOT FINANCIAL ADVICE" in notice)

    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    print(f"\n{'=' * 52}\nVALIDATION: {passed}/{total} passed")
    if passed != total:
        print("FAILED:", [n for n, ok in results if not ok])
        return 1
    print(f"{SKILL.name} is installable and structurally intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Rebuild the Cross-Disciplinary Standards Matrix from the canonical sources.

Sources of truth:
  • content/lessons/*.md        — per-lesson YAML frontmatter (standards, grades, etc.)
  • data/standards.json         — every standard code → {description, URL}

Outputs written:
  • static/matrix/index.html    — patched `const L=[...]`, `const S={...}`, prose counts
  • static/matrix/app.html      — same
  • static/js/standards-db.js   — regenerated window.STANDARDS_DB from standards.json
  • content/_index.md           — site meta description count
  • content/matrix/_index.md    — matrix landing meta description count
  • content/matrix/app.md       — matrix app meta description count
  • content/resources/_index.md — resources card description count
  • layouts/matrix/list.html    — hero lesson count

No other HTML/JS is touched. The script is idempotent: running it with no
corpus changes produces a zero-byte diff.

Usage (from repo root):
  python3 scripts/rebuild_matrix.py           # write changes
  python3 scripts/rebuild_matrix.py --check   # dry run, exit 1 on diff
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
LESSONS_DIR = REPO / "content" / "lessons"
STANDARDS_JSON = REPO / "data" / "standards.json"

MATRIX_HTML = [
    REPO / "static" / "matrix" / "index.html",
    REPO / "static" / "matrix" / "app.html",
]
STANDARDS_DB_JS = REPO / "static" / "js" / "standards-db.js"

COUNT_TEXT_FILES = [
    REPO / "content" / "_index.md",
    REPO / "content" / "matrix" / "_index.md",
    REPO / "content" / "matrix" / "app.md",
    REPO / "content" / "resources" / "_index.md",
    REPO / "layouts" / "matrix" / "list.html",
    REPO / "home.html",
]

FRAMEWORK_ORDER = [
    "CSTA",
    "CCSS ELA",
    "CCSS Math",
    "NGSS",
    "ISTE",
    "NCSS C3",
    "National Core Arts",
]

# ── Per-code URL resolution ─────────────────────────────────────────────────

def ngss_dci_slug(code: str) -> str:
    mapping = [
        ("PS1", "matter-and-its-interactions"),
        ("PS2", "motion-and-stability-forces-and-interactions"),
        ("PS3", "energy"),
        ("PS4", "waves-and-their-applications-in-technologies-for-information-transfer"),
        ("LS1", "from-molecules-to-organisms-structures-and-processes"),
        ("LS2", "ecosystems-interactions-energy-and-dynamics"),
        ("LS3", "heredity-inheritance-and-variation-of-traits"),
        ("LS4", "biological-evolution-unity-and-diversity"),
        ("ESS1", "earths-place-in-the-universe"),
        ("ESS2", "earths-systems"),
        ("ESS3", "earth-and-human-activity"),
        ("ETS1", "engineering-design"),
    ]
    for token, slug in mapping:
        if token in code:
            return slug
    return ""


def resolve_url(framework: str, code: str, fw_urls: dict) -> str:
    """Mirror the per-code link rules in layouts/partials/standards-display.html."""
    base = fw_urls.get(framework, "")
    if framework == "NGSS":
        dci = ngss_dci_slug(code)
        if dci:
            return f"https://www.nextgenscience.org/pe/{code}-{dci}"
        return f"https://www.nextgenscience.org/pe/{code}"
    if framework == "CCSS ELA":
        parts = code.split(".")
        strand = parts[0]
        grade = parts[1].replace("-", "") if len(parts) > 1 else ""
        return f"https://www.thecorestandards.org/ELA-Literacy/{strand}/{grade}/"
    if framework == "CCSS Math":
        if code.startswith("MP."):
            return "https://www.thecorestandards.org/Math/Practice/"
        if code.startswith("HS") and "-" in code:
            a, b = code.split("-", 1)
            b = b.split(".")[0]
            return f"https://www.thecorestandards.org/Math/Content/{a}/{b}/"
        if code.startswith(("G-", "F-", "N-", "A-", "S-")):
            a, b = code.split("-", 1)
            b = b.split(".")[0]
            return f"https://www.thecorestandards.org/Math/Content/HSG/{b}/" if a == "G" else base
        parts = code.split(".")
        if len(parts) >= 2:
            return f"https://www.thecorestandards.org/Math/Content/{parts[0]}/{parts[1]}/"
        return base
    return base


# ── Lesson loading ──────────────────────────────────────────────────────────

def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def load_lessons() -> list[dict]:
    rows = []
    for path in sorted(LESSONS_DIR.iterdir()):
        if path.suffix != ".md" or path.name == "_index.md":
            continue
        fm = parse_frontmatter(path)
        if fm is None:
            continue
        slug = path.stem
        standards = {
            fw: list(codes)
            for fw, codes in (fm.get("standards") or {}).items()
            if codes
        }
        rows.append({
            "s": slug,
            "t": fm.get("title", "") or "",
            "su": fm.get("subjects") or [],
            "g": fm.get("grade_levels") or [],
            "d": fm.get("cs_domains") or [],
            "p": fm.get("cs_principles") or [],
            "st": standards,
        })
    return rows


# ── Derivations ─────────────────────────────────────────────────────────────

def total_alignments(lessons: list[dict]) -> int:
    return sum(len(codes) for lesson in lessons for codes in lesson["st"].values())


def unique_codes(lessons: list[dict]) -> set[str]:
    out = set()
    for lesson in lessons:
        for codes in lesson["st"].values():
            out.update(codes)
    return out


def build_S(lessons: list[dict], standards_data: dict) -> tuple[dict, list[str]]:
    """Build the `const S` lookup for the matrix. Returns (S, missing_codes)."""
    descriptions = standards_data["descriptions"]
    fw_urls = standards_data["framework_urls"]
    # Flatten descriptions: code → {framework, desc}
    code_to_fw = {}
    for framework, codes in descriptions.items():
        for code, desc in codes.items():
            code_to_fw[code] = (framework, desc)

    S = {}
    missing = []
    for lesson in lessons:
        for framework, codes in lesson["st"].items():
            for code in codes:
                if code in S:
                    continue
                meta = code_to_fw.get(code)
                if meta is None:
                    missing.append((code, framework, lesson["s"]))
                    # Include it anyway with empty desc and framework URL so the
                    # matrix still renders; description will be blank.
                    S[code] = {"d": "", "u": fw_urls.get(framework, "")}
                    continue
                fw_from_json, desc = meta
                url = resolve_url(fw_from_json, code, fw_urls)
                S[code] = {"d": desc, "u": url}
    return S, missing


def ordered_L(lessons: list[dict]) -> list[dict]:
    """Match the per-lesson field order the matrix files already use."""
    out = []
    for lesson in sorted(lessons, key=lambda r: r["s"]):
        row = {"s": lesson["s"], "t": lesson["t"]}
        if lesson["su"]:
            row["su"] = lesson["su"]
        if lesson["g"]:
            row["g"] = lesson["g"]
        if lesson["d"]:
            row["d"] = lesson["d"]
        if lesson["p"]:
            row["p"] = lesson["p"]
        if lesson["st"]:
            row["st"] = lesson["st"]
        out.append(row)
    return out


# ── HTML patching ───────────────────────────────────────────────────────────

def replace_const(text: str, name: str, literal: str) -> str:
    """Replace `const <name>=<something>;` with the given literal.

    The matcher walks braces/brackets so it handles multi-line JSON values.
    """
    needle = f"const {name}="
    idx = text.find(needle)
    if idx == -1:
        raise RuntimeError(f"`const {name}=` not found")
    start = idx + len(needle)
    depth = 0
    opener = text[start]
    closer = {"[": "]", "{": "}"}[opener]
    i = start
    while i < len(text):
        ch = text[i]
        if ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                break
        i += 1
    # After closing brace/bracket expect a semicolon
    end = i + 1
    if end < len(text) and text[end] == ";":
        end += 1
    return text[:idx] + f"const {name}={literal};" + text[end:]


def patch_count_prose(text: str, lesson_count: int, alignment_count: int) -> str:
    """Rewrite known stale count phrases in place. No-ops if already correct."""
    # Primary matrix-page sentence variants
    text = re.sub(
        r"(\d[\d,]*)\s+computing-integrated lessons",
        f"{lesson_count} computing-integrated lessons",
        text,
    )
    # content/_index.md: "350+ free computing-integrated K-12 lesson plans"
    text = re.sub(
        r"(\d[\d,]*)\+?\s+free computing-integrated K-12 lesson plans",
        f"{lesson_count}+ free computing-integrated K-12 lesson plans",
        text,
    )
    # Matrix app sub-header tally: "379 lessons, 5,072 codes, 7 national frameworks"
    text = re.sub(
        r"(\d[\d,]*)\s+lessons,\s*(\d[\d,]*)\s+codes,\s*7\s+national frameworks",
        f"{lesson_count:,} lessons, {alignment_count:,} codes, 7 national frameworks",
        text,
    )
    # Matrix app stats footer: "379 lessons · 7 national frameworks · 5,072 standard alignments"
    text = re.sub(
        r"(\d[\d,]*)\s+lessons\s+&middot;\s+7\s+national frameworks\s+&middot;\s+(\d[\d,]*)\s+standard alignments",
        f"{lesson_count:,} lessons &middot; 7 national frameworks &middot; {alignment_count:,} standard alignments",
        text,
    )
    # Hugo landing hero prose: "Browse <strong>417 lessons</strong>" → live count
    text = re.sub(
        r"<strong>(\d[\d,]*)\s+lessons</strong>",
        f"<strong>{lesson_count} lessons</strong>",
        text,
    )
    # Resources page card: "Interactive map of 379 lessons"
    text = re.sub(
        r"Interactive map of (\d[\d,]*)\s+lessons",
        f"Interactive map of {lesson_count} lessons",
        text,
    )
    # Legacy home.html prose: "over 300 computing-infused lesson"
    text = re.sub(
        r"(\d[\d,]*)\s+computing-infused lesson",
        f"{lesson_count} computing-infused lesson",
        text,
    )
    # Matrix landing meta description: "an interactive map of 379 computing-integrated lessons"
    text = re.sub(
        r"map of (\d[\d,]*)\s+computing-integrated lessons",
        f"map of {lesson_count} computing-integrated lessons",
        text,
    )
    return text


def patch_matrix_html(path: Path, L: list[dict], S: dict, lesson_count: int, alignment_count: int) -> bool:
    before = path.read_text(encoding="utf-8")
    # Replace the two data constants. json.dumps with ensure_ascii=False so
    # unicode slugs (e.g., Spanish accents) round-trip faithfully.
    L_literal = json.dumps(L, ensure_ascii=False, separators=(",", ":"))
    S_literal = json.dumps(S, ensure_ascii=False, separators=(",", ":"))
    after = replace_const(before, "L", L_literal)
    after = replace_const(after, "S", S_literal) if "const S=" in after else after
    after = patch_count_prose(after, lesson_count, alignment_count)
    if after != before:
        path.write_text(after, encoding="utf-8")
    return after != before


def patch_text_file(path: Path, lesson_count: int, alignment_count: int) -> bool:
    before = path.read_text(encoding="utf-8")
    after = patch_count_prose(before, lesson_count, alignment_count)
    if after != before:
        path.write_text(after, encoding="utf-8")
    return after != before


# ── standards-db.js ─────────────────────────────────────────────────────────

def rebuild_standards_db_js(standards_data: dict) -> bool:
    descriptions_json = json.dumps(standards_data["descriptions"], ensure_ascii=False, separators=(",", ":"))
    fw_urls_json = json.dumps(standards_data["framework_urls"], indent=2, ensure_ascii=False)
    # Indent framework_urls 2 spaces (match existing style) and strip outer braces
    fw_urls_body = ",\n".join(
        f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}'
        for k, v in standards_data["framework_urls"].items()
    )
    content = (
        "// Auto-generated standards database for CxEd Hub\n"
        "// Covers CSTA, CCSS Math, CCSS ELA, NGSS, ISTE, NCSS C3, National Core Arts\n"
        "// Each framework maps code -> short description.\n"
        "// Regenerate with: python3 scripts/rebuild_matrix.py\n"
        f"window.STANDARDS_DB = {descriptions_json};\n"
        "window.STANDARDS_FW_URLS = {\n"
        f"{fw_urls_body}\n"
        "};\n"
    )
    before = STANDARDS_DB_JS.read_text(encoding="utf-8") if STANDARDS_DB_JS.exists() else ""
    if before != content:
        STANDARDS_DB_JS.write_text(content, encoding="utf-8")
        return True
    return False


# ── Main ────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="dry run; exit 1 on any diff")
    args = parser.parse_args()

    standards_data = json.loads(STANDARDS_JSON.read_text(encoding="utf-8"))
    lessons = load_lessons()
    L = ordered_L(lessons)
    S, missing = build_S(lessons, standards_data)
    lesson_count = len(L)
    alignment_count = total_alignments(lessons)

    print(f"Lessons discovered:   {lesson_count}")
    print(f"Standards alignments: {alignment_count}")
    print(f"Unique codes used:    {len(S)}")
    if missing:
        print(f"\n⚠️  {len(missing)} code(s) used in lessons but missing from data/standards.json:")
        seen = set()
        for code, framework, slug in missing:
            if code in seen:
                continue
            seen.add(code)
            print(f"    {framework:<20} {code:<18} (first seen in {slug})")
        print("\nAdd these to data/standards.json and rerun, or fix the lesson frontmatter.")

    changed: list[Path] = []
    if args.check:
        # Simulate writes without persisting
        for path in MATRIX_HTML:
            before = path.read_text(encoding="utf-8")
            L_literal = json.dumps(L, ensure_ascii=False, separators=(",", ":"))
            S_literal = json.dumps(S, ensure_ascii=False, separators=(",", ":"))
            after = replace_const(before, "L", L_literal)
            if "const S=" in after:
                after = replace_const(after, "S", S_literal)
            after = patch_count_prose(after, lesson_count, alignment_count)
            if after != before:
                changed.append(path)
        for path in COUNT_TEXT_FILES:
            before = path.read_text(encoding="utf-8")
            if patch_count_prose(before, lesson_count, alignment_count) != before:
                changed.append(path)
    else:
        for path in MATRIX_HTML:
            if patch_matrix_html(path, L, S, lesson_count, alignment_count):
                changed.append(path)
        for path in COUNT_TEXT_FILES:
            if patch_text_file(path, lesson_count, alignment_count):
                changed.append(path)
        if rebuild_standards_db_js(standards_data):
            changed.append(STANDARDS_DB_JS)

    if changed:
        print(f"\n{'Would change' if args.check else 'Updated'}:")
        for p in changed:
            print(f"  {p.relative_to(REPO)}")
    else:
        print("\nNo changes needed.")

    if args.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

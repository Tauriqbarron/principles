#!/usr/bin/env python3
"""Regenerate INDEX.md from index.json, validating every anchor against the live HTML.

Usage:
    python scripts/build_index.py            # writes INDEX.md
    python scripts/build_index.py --check    # validate only, writes nothing

Every `home.anchor` in index.json must appear verbatim in `home.file` as a heading (h1-h3)
or an Avoid/Preferred panel label. A stale or invented anchor fails the build with exit 1,
the same discipline `check_anchors.py` applies to plans.

The anchor extraction below mirrors the Hermes skill's
`principle-anchored-planning/scripts/anchors.py`. Keep the two in step.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "index.json"
TARGET = ROOT / "INDEX.md"

HEADING = re.compile(r"<h([123])[^>]*>(.*?)</h\1>", re.S)
LABEL = re.compile(r'panel-label">([^<]{2,90})<', re.S)


def strip(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", text))).strip()


def anchors(path: pathlib.Path):
    body = path.read_text(encoding="utf-8", errors="replace")
    return {strip(m.group(2)) for m in HEADING.finditer(body)} | {
        strip(m.group(1)) for m in LABEL.finditer(body)
    }


def norm(text: str) -> str:
    """Em dashes, en dashes and curly quotes are normalised before comparing."""
    for bad, good in (("\u2014", "-"), ("\u2013", "-"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"')):
        text = text.replace(bad, good)
    return re.sub(r"\s+", " ", text).strip().lower()


def main(argv):
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    principles = data["principles"]
    cache, bad = {}, []

    for p in principles:
        home = p.get("home")
        if not home:
            continue
        page = ROOT / home["file"]
        if not page.exists():
            bad.append((p["name"], home["anchor"], home["file"], "page does not exist"))
            continue
        cache.setdefault(home["file"], anchors(page))
        if norm(home["anchor"]) not in {norm(a) for a in cache[home["file"]]}:
            bad.append((p["name"], home["anchor"], home["file"], "anchor not found verbatim"))

    homed = [p for p in principles if p.get("home")]
    new = [p for p in principles if not p.get("home")]
    print(f"principles: {len(principles)}")
    print(f"  anchored to a page: {len(homed)}")
    print(f"  no page (agent conduct): {len(new)}")
    print(f"anchors checked: {len(homed)}")
    if bad:
        print("UNVERIFIED ANCHORS:")
        for name, anchor, page, why in bad:
            print(f"  [{why}] {name}: {anchor!r} -> {page}")
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")

    if "--check" in argv:
        return 0

    rows = []
    for p in sorted(principles, key=lambda x: x["short"]):
        home = p.get("home")
        if home:
            where = f'"{home["anchor"]}" in `{home["file"]}`'
        elif p.get("closest"):
            where = f"no page. Closest: {p['closest']}"
        else:
            where = "no page. Agent conduct, argued from this index."
        rows.append(
            f"| {p['short']} | **{p['name']}** | {p['rule']} | {where} |"
        )

    src = data["_source"]
    out = [
        "# Index",
        "",
        "Route from the situation you are in to the principle that governs it, and to the page you can",
        "open. Written for an agent with a task in hand, not for a reader browsing topics. `AGENTS.md`",
        "routes by task type; this routes by what the work currently feels like.",
        "",
        "Two kinds of row. Where `Read` names a page and an anchor, that exact heading or panel label",
        "exists in that file: cite it verbatim, and open it before citing. Where it says no page, the",
        "principle is agent conduct that this library does not cover as a topic page. Say that plainly",
        "rather than implying a citation, the same rule `principle-anchored-review` applies to gaps.",
        "",
        "| Situation | Principle | Rule | Read |",
        "|---|---|---|---|",
    ]
    out += rows
    out += [
        "",
        f"Source of truth: `index.json`. Regenerate this file with `python scripts/build_index.py`,",
        "which fails if any anchor above stops matching its page. Add a principle by adding a row there,",
        "never by editing this file.",
        "",
        "## Provenance",
        "",
        f"The {len(principles)} principle names, and the trigger phrasing behind the Situation column, come from",
        f"[pstack]({src['repo']}) by {src['author']}, MIT licensed. The rules, the anchor mapping and the",
        "no-page determinations are this repository's own. See `CREDITS.md`.",
        "",
        "## Playbooks",
        "",
        "The workflows that apply these principles step by step live in `playbooks/`: bug fix, runtime",
        "forensics, hillclimb, babysit and shipping. They are ports of pstack's playbooks onto Hermes",
        "primitives, and each one names the principles it leans on.",
        "",
    ]
    TARGET.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {TARGET} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

# Cross-Disciplinary Standards Matrix — Tracking

A living inventory of what the matrix covers. **Regenerate by running
`python3 scripts/rebuild_matrix.py`** — the numbers below are a snapshot.

See [`MATRIX_PROCESS.md`](MATRIX_PROCESS.md) for how to add a new lesson.

## Snapshot

| Metric | Value |
| --- | --- |
| Lessons in matrix | **379** |
| Standard alignments | **5,072** |
| National frameworks | **7** |
| Unique standard codes used | **267** |
| Standard codes described in `data/standards.json` | **358** |

## Framework coverage

| Framework | Lessons aligned | Alignments | Codes used | Codes described |
| --- | ---: | ---: | ---: | ---: |
| CSTA | 379 | 2,356 | 62 | 75 |
| ISTE | 377 | 1,711 | 18 | 24 |
| NGSS | 111 | 454 | 87 | 124 |
| CCSS ELA | 97 | 180 | 23 | 24 |
| CCSS Math | 81 | 130 | 26 | 30 |
| NCSS C3 | 37 | 90 | 35 | 59 |
| National Core Arts | 34 | 151 | 16 | 22 |

"Codes used" = codes referenced by at least one lesson's frontmatter.
"Codes described" = codes present in `data/standards.json` with a tooltip
description and source URL. The gap between the two is deliberate — the
database carries extra coverage so new lessons can pick up codes without
touching the DB.

## Per-lesson caps (enforced by authors, not the rebuild script)

To keep the matrix legible and discourage over-tagging, lessons should list
**only** codes they meaningfully cover:

| Framework | Max codes per lesson |
| --- | --- |
| CSTA | 8 |
| ISTE | 6 |
| NGSS, CCSS Math, CCSS ELA, NCSS C3, National Core Arts | 5 each |

These caps were set in commit `5639e15` (April 2026) after the corpus was
cleaned from 411 → 379 lessons and 6,637 → 5,072 alignments.

## Files kept in sync by the rebuild script

The script `scripts/rebuild_matrix.py` is the **single source of truth** for
regeneration. It edits these files and nothing else:

- `static/matrix/index.html` — patches `const L=[…]` and `const S={…}`, plus
  the "379 lessons · 5,072 alignments" prose.
- `static/matrix/app.html` — same as above.
- `static/js/standards-db.js` — regenerates `window.STANDARDS_DB` from
  `data/standards.json` so per-lesson standards tooltips stay consistent.
- `content/_index.md` — updates the site meta description's lesson count.
- `content/matrix/_index.md`, `content/matrix/app.md` — matrix-page meta
  descriptions.
- `content/resources/_index.md` — the "Interactive map of 379 lessons" card.
- `layouts/matrix/list.html` — the matrix-landing hero's lesson count.
- `home.html` — legacy landing copy (not currently rendered by Hugo but
  kept aligned for GitHub preview).

## Historical corrections

| Date | Change |
| --- | --- |
| 2026-04 | Added 18 standard codes used in lessons but missing from `data/standards.json` (3A-DA-10, 3A-IC-25, 3A-IC-26, 8.EE.C, D2.His.2.9-12, G-CO.8, G-GMD.3, G-MG.1, G-MG.3, HS-PS1-7, HS-PS4-3, HS-PS4-5, ISTE-5b, MP.1, MP.3, MP.4, RL.2.4, RL.7.4). |
| 2026-04 | Fixed stale "417 lessons" prose in `layouts/matrix/list.html`, "350+" in `content/_index.md`, "300 computing-infused" in `home.html`. Matrix `const L=` was already correct at 379. |
| 2026-04 | Introduced `scripts/rebuild_matrix.py` so counts and lookups stay in sync automatically. |
| 2026-04 | (Earlier, commit `5639e15`) Deduped 32 lessons, renamed 5 to `-part-N`, capped per-framework codes, fixed stale 350/411/417 counts, regenerated `const L`. |

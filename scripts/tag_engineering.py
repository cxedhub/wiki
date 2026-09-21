#!/usr/bin/env python3
"""Add the `Engineering` subject to lessons that teach engineering.

Background: the Wiki.js → Hugo migration normalised the `subjects` front
matter to a fixed list that had no `Engineering` entry, so the subject filter
on /lessons/ never offered it even though dozens of lessons are engineering
lessons by their authors' own description.

A lesson gets `Engineering` added to its `subjects` list when ANY of these
hold (the script reports which):

  1. author-declared  — the lesson body's "*Subject Area:*" line (written by
                        the lesson author) names Engineering.
  2. NGSS ETS         — the lesson aligns to an NGSS Engineering, Technology &
                        Applications of Science performance expectation
                        (K-2-ETS1-x, 3-5-ETS1-x, MS-ETS1-x, HS-ETS1-x, …), in
                        `standards.NGSS` or in the body.
  3. hand-reviewed    — a short curated list (CURATED below) of lessons that
                        lack both signals but are unmistakably build / design /
                        prototype lessons. Each entry carries its reason.

The `subjects:` block is edited in place (text-level, not a YAML re-dump) so
no other front-matter formatting changes. The script is idempotent.

Usage:
  python3 scripts/tag_engineering.py            # apply
  python3 scripts/tag_engineering.py --dry-run  # report only
"""

import os
import re
import sys

import yaml

LESSONS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'lessons')
SUBJECT = 'Engineering'

FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)', re.DOTALL)
SUBJECT_AREA_RE = re.compile(r'\*Subject Area:?\*:?\s*(.*)')
# NGSS ETS performance expectations: K-2-ETS1-1, 3-5-ETS1-2, MS-ETS1-3, HS-ETS1-4
ETS_RE = re.compile(r'\b(?:K-2|3-5|K|[1-5]|MS|HS)-ETS[12]-\d')
# Matches the existing block-style subjects list used by every lesson:
#   subjects:\n- Computer Science\n- Science\n
SUBJECTS_BLOCK_RE = re.compile(r'^subjects:\s*\n((?:[ \t]*-[ \t]*.+\n)+)', re.MULTILINE)

# Lessons with neither signal above, reviewed by hand. slug -> reason.
CURATED = {
    'arduino-traffic-light-2':
        'students code and then build an Arduino traffic-light simulator '
        '(sibling of arduino-traffic-lights, which is author-declared)',
    'create-a-cookie-cutter-device-using-technology-and-3d-printing-to-understand-add':
        'students model a cookie cutter in play-doh, then design and 3D-print it',
    'geometric-planter-find-volume':
        'geometry lesson built around designing a planter in Tinkercad/Blender for 3D printing',
    'lesson-1-activity-geometric-planter-find-total-surface-area':
        'companion 3D-printed planter design lesson',
    'whats-the-weather-2':
        'Arduino set up as a weather station (sibling of whats-the-weather, which is ETS-aligned)',
    'penguin-lab':
        'students construct and test a prototype insulated home instrumented with micro:bit sensors',
    'zombie-break-out-alarms':
        'students build and troubleshoot a Cubelets alarm circuit by trial and error',
    'sea-creature-safety':
        'students build a micro:bit sensor/output prototype to protect sea turtles',
    'microbit-step-counter':
        'students design and build a wearable micro:bit step-counter strap',
    'mindstorms-and-hidden-figures':
        'students design a Lego Mindstorms robot to orbit the moon',
    'do-you-want-to-build-a-robot':
        'students build a micro:bit pet (sibling of microbit-programming-creating-a-micropet, '
        'which is ETS-aligned, same author)',
}


def load(path):
    with open(path, encoding='utf-8', errors='replace') as fh:
        text = fh.read()
    m = FM_RE.match(text)
    if not m:
        return text, None, None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return text, None, None
    return text, fm, m.group(2)


def reasons_for(slug, fm, body):
    reasons = []
    m = SUBJECT_AREA_RE.search(body)
    if m and re.search(r'engineer', m.group(1), re.I):
        reasons.append('author-declared')
    ngss = []
    standards = fm.get('standards')
    if isinstance(standards, dict):
        ngss = standards.get('NGSS') or []
    codes = set(ETS_RE.findall(' '.join(str(c) for c in ngss)))
    codes |= set(ETS_RE.findall(body))
    if codes:
        reasons.append('NGSS ETS (' + ', '.join(sorted(codes)) + ')')
    if slug in CURATED:
        reasons.append('hand-reviewed: ' + CURATED[slug])
    return reasons


def add_subject(text):
    """Return (new_text, changed). Appends `- Engineering` to the subjects block."""
    m = SUBJECTS_BLOCK_RE.search(text)
    if not m:
        return text, False
    block = m.group(1)
    existing = [re.sub(r'^[ \t]*-[ \t]*', '', line).strip().strip('"\'')
                for line in block.splitlines()]
    if SUBJECT in existing:
        return text, False
    indent = re.match(r'[ \t]*', block).group(0)
    new_block = block + f'{indent}- {SUBJECT}\n'
    return text[:m.start(1)] + new_block + text[m.end(1):], True


def main(argv):
    dry_run = '--dry-run' in argv
    tallies = {'author-declared': 0, 'NGSS ETS': 0, 'hand-reviewed': 0}
    planned, already, changed, missing_block = [], [], [], []

    for fname in sorted(os.listdir(LESSONS_DIR)):
        if not fname.endswith('.md') or fname == '_index.md':
            continue
        slug = fname[:-3]
        path = os.path.join(LESSONS_DIR, fname)
        text, fm, body = load(path)
        if fm is None:
            continue
        reasons = reasons_for(slug, fm, body)
        if not reasons:
            continue
        for r in reasons:
            tallies[r.split(' (')[0].split(':')[0]] += 1
        if SUBJECT in (fm.get('subjects') or []):
            already.append(slug)
            continue
        planned.append((slug, reasons))
        if dry_run:
            continue
        new_text, ok = add_subject(text)
        if not ok:
            missing_block.append(slug)
            continue
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_text)
        changed.append(slug)

    for slug, reasons in planned:
        print(f'{slug}\n    ' + '\n    '.join(reasons))

    print()
    print(f"{'Would tag' if dry_run else 'Tagged'}: {len(planned)} lesson(s)"
          f"  (already tagged: {len(already)})")
    for k, v in tallies.items():
        print(f'  {k:16s} {v}')
    if missing_block:
        print('\nERROR: no block-style `subjects:` list found in:')
        for s in missing_block:
            print('  ' + s)
        return 1
    for slug in CURATED:
        if not os.path.exists(os.path.join(LESSONS_DIR, slug + '.md')):
            print(f'\nWARNING: curated slug not found: {slug}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

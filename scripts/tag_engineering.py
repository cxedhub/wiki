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

Second pass — engineering concepts, disciplines and STEL standards
-------------------------------------------------------------------
`--details` applies the reviewed per-lesson classification stored in
scripts/engineering_details.json (slug -> eng_concepts, eng_disciplines,
stel). For each lesson it writes:

  eng_disciplines:   Hugo taxonomy (hugo.toml `eng_discipline`)
  eng_concepts:      Hugo taxonomy (hugo.toml `eng_concept`)
  standards:
    ITEEA STEL:      core-standard codes STEL-1 … STEL-8 (data/standards.json)
  standard_types:    gains "ITEEA STEL" (kept alphabetised)

Blocks are replaced in place if they already exist, so the pass is
idempotent. The classification file is the reviewable source of truth; edit
it and re-run rather than hand-editing 95 lessons.

Usage:
  python3 scripts/tag_engineering.py                      # subject pass
  python3 scripts/tag_engineering.py --dry-run            # report only
  python3 scripts/tag_engineering.py --details            # concepts/disciplines/STEL pass
  python3 scripts/tag_engineering.py --details --dry-run
"""

import json
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


DETAILS_JSON = os.path.join(os.path.dirname(__file__), 'engineering_details.json')
STEL_FRAMEWORK = 'ITEEA STEL'

ENG_CONCEPTS = [
    'Engineering Design Process',
    'Criteria, Constraints & Trade-offs',
    'Systems, Inputs & Outputs',
    'Sensors & Measurement',
    'Control & Feedback',
    'Circuits & Electricity',
    'Structures, Forces & Materials',
    'Energy & Power',
    'Modeling & Simulation',
    'Fabrication & Making',
    'Troubleshooting & Failure Analysis',
    'Technology & Society',
]
ENG_DISCIPLINES = [
    'Electrical & Computer Engineering',
    'Mechanical Engineering',
    'Civil Engineering',
    'Environmental Engineering',
    'Aerospace Engineering',
    'Biomedical Engineering',
    'Software Engineering',
    'Materials & Chemical Engineering',
    'Agricultural & Biological Engineering',
    'Industrial & Systems Engineering',
]
STEL_CODES = [f'STEL-{i}' for i in range(1, 9)]


def _block_re(key):
    """Regex for a top-level block-style list `key:` followed by `- item` lines."""
    return re.compile(rf'^{re.escape(key)}:[ \t]*\n((?:[ \t]*-[ \t]*.+\n)+)', re.MULTILINE)


def _yaml_list(key, items, indent=''):
    return f'{indent}{key}:\n' + ''.join(f'{indent}- {i}\n' for i in items)


def set_list_block(fm_text, key, items, after_keys):
    """Insert or replace `key:` list block. New blocks go after the first key in
    `after_keys` that exists, else at the end of the front matter."""
    fm_text = _block_re(key).sub('', fm_text)
    fm_text = re.sub(rf'^{re.escape(key)}:[ \t]*(\[.*?\])?[ \t]*\n', '', fm_text, flags=re.MULTILINE)
    if not items:
        return fm_text
    block = _yaml_list(key, items)
    for anchor in after_keys:
        m = _block_re(anchor).search(fm_text)
        if m:
            return fm_text[:m.end()] + block + fm_text[m.end():]
        m = re.search(rf'^{re.escape(anchor)}:.*\n', fm_text, flags=re.MULTILINE)
        if m:
            return fm_text[:m.end()] + block + fm_text[m.end():]
    return fm_text.rstrip('\n') + '\n' + block


def set_standards_framework(fm_text, framework, codes):
    """Insert or replace one framework's code list inside the `standards:` map."""
    m = re.search(r'^standards:[ \t]*\n((?:[ \t]+.*\n)+)', fm_text, flags=re.MULTILINE)
    if not m:
        return fm_text if not codes else (fm_text.rstrip('\n') + '\n' + 'standards:\n' + _yaml_list(framework, codes, '  '))
    body = m.group(1)
    body = re.sub(rf'^[ \t]+{re.escape(framework)}:[ \t]*\n(?:[ \t]+-[ \t]*.+\n)*', '', body, flags=re.MULTILINE)
    if codes:
        body = body + _yaml_list(framework, codes, '  ')
    return fm_text[:m.start(1)] + body + fm_text[m.end(1):]


def set_standard_types(fm_text, fm, add_framework, want):
    types = [t for t in (fm.get('standard_types') or []) if t != add_framework]
    if want:
        types.append(add_framework)
    types = sorted(set(types))
    return set_list_block(fm_text, 'standard_types', types, ['tags', 'materials', 'standards'])


def apply_details(dry_run):
    with open(DETAILS_JSON, encoding='utf-8') as fh:
        details = json.load(fh)
    bad = []
    for slug, d in details.items():
        for c in d.get('eng_concepts', []):
            if c not in ENG_CONCEPTS:
                bad.append((slug, 'concept', c))
        for c in d.get('eng_disciplines', []):
            if c not in ENG_DISCIPLINES:
                bad.append((slug, 'discipline', c))
        for c in d.get('stel', []):
            if c not in STEL_CODES:
                bad.append((slug, 'stel', c))
    if bad:
        print('ERROR: values outside the controlled vocabulary:')
        for b in bad:
            print('  ', b)
        return 1

    changed, missing = [], []
    tally = {'eng_concepts': {}, 'eng_disciplines': {}, 'stel': {}}
    for slug, d in sorted(details.items()):
        path = os.path.join(LESSONS_DIR, slug + '.md')
        if not os.path.exists(path):
            missing.append(slug)
            continue
        text, fm, body = load(path)
        if fm is None:
            missing.append(slug)
            continue
        m = FM_RE.match(text)
        fm_text = m.group(1) + '\n'
        concepts = d.get('eng_concepts', [])
        disciplines = d.get('eng_disciplines', [])
        stel = sorted(d.get('stel', []))
        for k, vals in (('eng_concepts', concepts), ('eng_disciplines', disciplines), ('stel', stel)):
            for v in vals:
                tally[k][v] = tally[k].get(v, 0) + 1
        new_fm = set_list_block(fm_text, 'eng_disciplines', disciplines,
                                ['cs_principles', 'cs_domains', 'grade_levels', 'subjects'])
        new_fm = set_list_block(new_fm, 'eng_concepts', concepts,
                                ['eng_disciplines', 'cs_principles', 'cs_domains', 'grade_levels', 'subjects'])
        new_fm = set_standards_framework(new_fm, STEL_FRAMEWORK, stel)
        new_fm = set_standard_types(new_fm, fm, STEL_FRAMEWORK, bool(stel))
        new_text = '---\n' + new_fm.rstrip('\n') + '\n---\n' + body
        if new_text != text:
            changed.append(slug)
            if not dry_run:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(new_text)

    print(f"{'Would update' if dry_run else 'Updated'} {len(changed)} lesson(s) from {len(details)} entries")
    for k in ('eng_disciplines', 'eng_concepts', 'stel'):
        print(f'\n{k}:')
        for v, n in sorted(tally[k].items(), key=lambda x: -x[1]):
            print(f'  {n:3d}  {v}')
    if missing:
        print('\nWARNING: no lesson file for:', ', '.join(missing))
    return 0


def main(argv):
    dry_run = '--dry-run' in argv
    if '--details' in argv:
        return apply_details(dry_run)
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

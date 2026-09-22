#!/usr/bin/env python3
"""Auto-tag lessons based on content analysis.

Tag taxonomy:
  Program origin: GenCyber, WySTACK, WySLICE
  Activity format: Unplugged, Game-Based, Project-Based
  Tools/platforms: micro:bit, MakeCode, MicroPython, Scratch, Robotics, Code.org, Web Design
  Theme: Cybersecurity, Data Collection, AI, LLM, IoT

The pass is ADDITIVE: tags already on a lesson (e.g. WySTACK, WySLICE) are
kept, derived tags are merged in, and the `tags:` block is rewritten in
place so nothing else in the front matter moves. Re-running is a no-op.
"""

import os
import re
import yaml

LESSONS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'lessons')

# ── Tag rules: (tag_name, compiled_regex_for_body, compiled_regex_for_materials) ──
# We search description + body + materials for these patterns

TOOL_TAGS = {
    'micro:bit': re.compile(r'micro.?bit|makecode|microbit', re.I),
    'Scratch': re.compile(r'\bscratch\b(?!\s+paper)', re.I),
    'Robotics': re.compile(r'\brobot|botley|sphero|ozobot|dash\b|hexbug|bristlebot|bee.?bot|coding critter|lego.*mindstorm|tetrix|first lego', re.I),
    'Code.org': re.compile(r'code\.org|codeorg|code studio', re.I),
    'Web Design': re.compile(r'\bhtml\b|\bcss\b|web\s*design|web\s*page|website\s*creat|website\s*build|web\s*develop', re.I),
    # Editors for micro:bit lessons (tag names match the PD pages' tags)
    'MakeCode': re.compile(r'make\s*code', re.I),
}

FORMAT_TAGS = {
    'Unplugged': re.compile(r'unplugged|without\s*(a\s*)?computer|no\s*technolog|paper\s*and\s*pencil|offline\s*activit|hands.on.*no\s*device|kinesthetic|human\s*computer', re.I),
    'Game-Based': re.compile(r'\bgame\b.*\b(creat|design|build|mak|play|develop)\b|\b(creat|design|build|mak|develop)\b.*\bgame\b|escape\s*room|board\s*game|card\s*game|game.based|gamif', re.I),
    'Project-Based': re.compile(r'project.based|design\s*challenge|engineering\s*design|maker\s*project|build\s*a\b|create\s*a\s*(computational\s*)?artifact|stem\s*challenge|design\s*process', re.I),
}

THEME_TAGS = {
    'Cybersecurity': re.compile(r'cyber\s*secur|internet\s*safe|online\s*safe|phishing|password\s*secur|password\s*safe|cyber\s*defense|malware|encrypt|confidentiality.*integrity|think\s*like\s*an\s*adversar|cyber\s*attack|network\s*secur|cyber\s*awareness|cyber\s*threat|firewall|social\s*engineer', re.I),
    'Data Collection': re.compile(r'data\s*collect|collect\s*data|gather\s*data|data\s*gather|survey\s*data|record\s*data|measur.*data|data\s*table|spreadsheet|data\s*set|data\s*analy', re.I),
    'LLM': re.compile(r'\bLLMs?\b|large\s*language\s*model|chat\s*gpt|generative\s*ai|\bgpt\b|openai|copilot', re.I),
    'IoT': re.compile(r'\bIoT\b|internet\s*of\s*things', re.I),
}

# AI: the term is common in passing ("including AI in their studies"), so require it in the
# title/description or a substantial number of mentions in the body.
AI_RE = re.compile(r'\bAI\b|artificial\s*intelligence|machine\s*learning|neural\s*net|teachable\s*machine|deep\s*learning|reinforcement\s*learning', re.I)
AI_BODY_MIN_HITS = 5
MICROBIT_RE = re.compile(r'micro.?bit', re.I)
MICROPYTHON_RE = re.compile(r'micropython|\bpython\b', re.I)


def parse_frontmatter(filepath):
    """Parse YAML frontmatter and body from a markdown file."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Match --- delimited frontmatter
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not m:
        return None, None, content

    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, None, content

    return fm, m.group(1), content


def derive_tags(fm, body):
    """Derive tags from frontmatter + body content."""
    tags = []

    # Build searchable text from description, materials, and body
    desc = fm.get('description', '') or ''
    materials = fm.get('materials', '') or ''
    title = fm.get('title', '') or ''
    searchable = f"{title}\n{desc}\n{materials}\n{body}"

    # Program origin
    old_tags = fm.get('tags') or []
    if isinstance(old_tags, str):
        old_tags = [old_tags]
    if any('gencyber' in t.lower() for t in old_tags):
        tags.append('GenCyber')

    # Tool tags
    for tag, pattern in TOOL_TAGS.items():
        if pattern.search(searchable):
            tags.append(tag)

    # Format tags
    for tag, pattern in FORMAT_TAGS.items():
        if pattern.search(searchable):
            tags.append(tag)

    # Theme tags
    for tag, pattern in THEME_TAGS.items():
        if pattern.search(searchable):
            tags.append(tag)

    # Cybersecurity: also tag if subjects include "Cybersecurity"
    subjects = fm.get('subjects') or []
    if 'Cybersecurity' in subjects and 'Cybersecurity' not in tags:
        tags.append('Cybersecurity')

    # AI
    if AI_RE.search(f"{title}\n{desc}") or len(AI_RE.findall(body)) >= AI_BODY_MIN_HITS:
        tags.append('AI')

    # MicroPython: a micro:bit lesson programmed in (Micro)Python
    if MICROBIT_RE.search(searchable) and MICROPYTHON_RE.search(searchable):
        tags.append('MicroPython')

    # Additive: keep the lesson's existing tags (and their order); append new ones
    merged = [str(t) for t in old_tags]
    for t in tags:
        if t not in merged:
            merged.append(t)
    return merged


TAGS_BLOCK_RE = re.compile(r'^tags:[ \t]*(?:\[.*?\])?[ \t]*\n(?:[ \t]*-[ \t]*.+\n)*', re.MULTILINE)


def _yaml_item(t):
    """Quote only when plain YAML would misparse the value."""
    if re.search(r'(^[\[\]{}&*!|>\'"%@`#-])|(:\s)|(\s#)|(^\s|\s$)', t):
        return '"' + t.replace('"', '\\"') + '"'
    return t


def rebuild_file(filepath, fm, new_tags):
    """Rewrite the `tags:` block in place. Returns True if the file changed."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not m:
        return False
    fm_text = m.group(1) + '\n'
    body = m.group(2)

    if new_tags:
        tags_yaml = 'tags:\n' + ''.join(f'- {_yaml_item(t)}\n' for t in new_tags)
    else:
        tags_yaml = 'tags: []\n'

    if TAGS_BLOCK_RE.search(fm_text):
        fm_text = TAGS_BLOCK_RE.sub(lambda _: tags_yaml, fm_text, count=1)
    else:
        fm_text = fm_text + tags_yaml

    new_content = '---\n' + fm_text.rstrip('\n') + '\n---\n' + body
    if new_content == content:
        return False
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True


def main():
    stats = {}
    total = 0
    tagged = 0
    changed = 0

    for fname in sorted(os.listdir(LESSONS_DIR)):
        if not fname.endswith('.md'):
            continue
        if fname == '_index.md':
            continue

        filepath = os.path.join(LESSONS_DIR, fname)
        fm, fm_text, content = parse_frontmatter(filepath)
        if fm is None:
            print(f"SKIP (no frontmatter): {fname}")
            continue

        total += 1
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
        body = m.group(2) if m else ''

        new_tags = derive_tags(fm, body)
        if new_tags:
            tagged += 1

        for t in new_tags:
            stats[t] = stats.get(t, 0) + 1

        if rebuild_file(filepath, fm, new_tags):
            changed += 1

    print(f"\nProcessed {total} lessons, {tagged} have at least one tag, {changed} file(s) changed")
    print(f"\nTag distribution:")
    for tag, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {tag}: {count}")

    untagged = total - tagged
    print(f"\n  (untagged): {untagged}")


if __name__ == '__main__':
    main()

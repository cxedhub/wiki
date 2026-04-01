#!/usr/bin/env python3
"""Auto-tag lessons based on content analysis.

Tag taxonomy:
  Program origin: GenCyber, WySTACK, WySLICE
  Activity format: Unplugged, Game-Based, Project-Based
  Tools/platforms: micro:bit, Scratch, Robotics, Code.org, Web Design
  Theme: Cybersecurity, Data Collection
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
}

FORMAT_TAGS = {
    'Unplugged': re.compile(r'unplugged|without\s*(a\s*)?computer|no\s*technolog|paper\s*and\s*pencil|offline\s*activit|hands.on.*no\s*device|kinesthetic|human\s*computer', re.I),
    'Game-Based': re.compile(r'\bgame\b.*\b(creat|design|build|mak|play|develop)\b|\b(creat|design|build|mak|develop)\b.*\bgame\b|escape\s*room|board\s*game|card\s*game|game.based|gamif', re.I),
    'Project-Based': re.compile(r'project.based|design\s*challenge|engineering\s*design|maker\s*project|build\s*a\b|create\s*a\s*(computational\s*)?artifact|stem\s*challenge|design\s*process', re.I),
}

THEME_TAGS = {
    'Cybersecurity': re.compile(r'cyber\s*secur|internet\s*safe|online\s*safe|phishing|password\s*secur|password\s*safe|cyber\s*defense|malware|encrypt|confidentiality.*integrity|think\s*like\s*an\s*adversar|cyber\s*attack|network\s*secur|cyber\s*awareness|cyber\s*threat|firewall|social\s*engineer', re.I),
    'Data Collection': re.compile(r'data\s*collect|collect\s*data|gather\s*data|data\s*gather|survey\s*data|record\s*data|measur.*data|data\s*table|spreadsheet|data\s*set|data\s*analy', re.I),
}


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

    return sorted(set(tags))


def rebuild_file(filepath, fm, new_tags):
    """Rewrite the file with updated tags in frontmatter."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not m:
        return False

    fm_text = m.group(1)
    body = m.group(2)

    # Replace or insert tags line
    # Remove old tags line(s) - handle both inline and multi-line
    # First remove multi-line tags block
    fm_text = re.sub(r'^tags:\s*\n(?:\s*-\s*.+\n)*', '', fm_text, flags=re.MULTILINE)
    # Then remove inline tags
    fm_text = re.sub(r'^tags:\s*\[.*?\]\s*\n?', '', fm_text, flags=re.MULTILINE)
    # Remove any remaining empty tags
    fm_text = re.sub(r'^tags:\s*\n', '', fm_text, flags=re.MULTILINE)

    # Strip trailing whitespace from frontmatter
    fm_text = fm_text.rstrip()

    # Build new tags line
    if new_tags:
        # Use flow style for clean YAML
        tags_yaml = 'tags:\n' + ''.join(f'- "{t}"\n' for t in new_tags)
    else:
        tags_yaml = 'tags: []\n'

    # Append tags at end of frontmatter
    new_content = f"---\n{fm_text}\n{tags_yaml}---\n{body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    stats = {}
    total = 0
    tagged = 0

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

        rebuild_file(filepath, fm, new_tags)

    print(f"\nProcessed {total} lessons, {tagged} have at least one tag")
    print(f"\nTag distribution:")
    for tag, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {tag}: {count}")

    untagged = total - tagged
    print(f"\n  (untagged): {untagged}")


if __name__ == '__main__':
    main()

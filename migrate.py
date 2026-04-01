#!/usr/bin/env python3
"""Migrate Wiki.js lesson plans to Hugo content format."""

import os
import re
import glob
import yaml

SRC_DIR = "Resources/LP"
DEST_DIR = "content/lessons"


def parse_frontmatter(text):
    """Extract YAML frontmatter and body from markdown."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', text, re.DOTALL)
    if not match:
        return {}, text
    try:
        fm = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        fm = {}
    return fm or {}, match.group(2)


def extract_table_field(body, field_name):
    """Extract a value from the Wiki.js metadata table."""
    pattern = rf'\|\s*{re.escape(field_name)}\s*\|(.*?)\|'
    match = re.search(pattern, body, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""


def split_list(value):
    """Split comma-separated values, trim, deduplicate preserving order."""
    if not value:
        return []
    items = [v.strip() for v in value.split(",") if v.strip()]
    # Deduplicate case-insensitively, keeping first occurrence
    seen = set()
    result = []
    for item in items:
        key = item.lower()
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def clean_tags(tags):
    """Remove generic tags, keep meaningful ones."""
    skip = {"resources", "lesson plan", "resource"}
    return [t for t in tags if t.lower() not in skip]


def slugify(title):
    """Create a URL-friendly slug from title."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


def extract_materials(body):
    """Extract materials from the meta description section."""
    match = re.search(r'\*Materials:\*\s*\n(.*?)(?:\n\s*\+\s*\*|\n\n|\n#)', body, re.DOTALL)
    if match:
        text = match.group(1).strip()
        items = re.findall(r'(?:^|\n)\s*\+?\s*(.+)', text)
        return ", ".join(i.strip() for i in items if i.strip())
    return ""


def process_file(filepath):
    """Process a single Wiki.js markdown file into Hugo format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    fm, body = parse_frontmatter(text)
    title = fm.get('title', 'Untitled')
    description = fm.get('description', '')

    # Extract structured data from the table in the body
    author = extract_table_field(body, "Author/Educators")
    subjects_raw = extract_table_field(body, "Subject(s)")
    grade_level = extract_table_field(body, "Grade Level")
    cs_domains_raw = extract_table_field(body, "CS Domains")
    cs_principles_raw = extract_table_field(body, "CS Principles")
    standards = extract_table_field(body, "Other Content Standards")

    subjects = split_list(subjects_raw)
    cs_domains = split_list(cs_domains_raw)
    cs_principles = split_list(cs_principles_raw)
    grade_levels = split_list(grade_level)

    # Clean up tags
    raw_tags = fm.get('tags', '')
    if isinstance(raw_tags, str):
        tags = split_list(raw_tags)
    elif isinstance(raw_tags, list):
        tags = raw_tags
    else:
        tags = []
    tags = clean_tags(tags)

    # Extract materials
    materials = extract_materials(body)

    # Get date
    date_created = fm.get('dateCreated', '')
    if not date_created:
        date_created = fm.get('date', '')

    # Build Hugo frontmatter
    hugo_fm = {
        'title': title,
        'description': description,
        'date': str(date_created),
        'draft': not fm.get('published', True),
    }
    if author:
        hugo_fm['author'] = author
    if subjects:
        hugo_fm['subjects'] = subjects
    if grade_levels:
        hugo_fm['grade_levels'] = grade_levels
    if cs_domains:
        hugo_fm['cs_domains'] = cs_domains
    if cs_principles:
        hugo_fm['cs_principles'] = cs_principles
    if tags:
        hugo_fm['tags'] = tags
    if standards:
        hugo_fm['standards'] = standards
    if materials:
        hugo_fm['materials'] = materials

    # Clean up the body content:
    # Remove the Wiki.js metadata table (everything before # OVERVIEW or first heading)
    # Keep the actual lesson content
    content_match = re.search(r'^(# OVERVIEW.*)', body, re.MULTILINE | re.DOTALL)
    if content_match:
        clean_body = content_match.group(1)
    else:
        # Try finding any first-level heading
        content_match = re.search(r'^(# .+)', body, re.MULTILINE | re.DOTALL)
        if content_match:
            clean_body = content_match.group(1)
        else:
            clean_body = body

    # Remove the Wiki.js boilerplate license text
    clean_body = re.sub(
        r'This lesson plan, created on.*?maintainers\.\s*',
        '',
        clean_body,
        flags=re.DOTALL
    )

    # Remove {.dense} wiki.js directives
    clean_body = clean_body.replace('{.dense}', '')

    # Build output
    slug = slugify(title)
    output_fm = yaml.dump(hugo_fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    output = f"---\n{output_fm}---\n{clean_body}"

    return slug, output


def main():
    os.makedirs(DEST_DIR, exist_ok=True)

    files = glob.glob(os.path.join(SRC_DIR, "*.md"))
    print(f"Found {len(files)} lesson plan files")

    slugs_seen = {}
    converted = 0
    errors = 0

    for filepath in sorted(files):
        try:
            slug, content = process_file(filepath)

            # Handle duplicate slugs
            if slug in slugs_seen:
                slugs_seen[slug] += 1
                slug = f"{slug}-{slugs_seen[slug]}"
            else:
                slugs_seen[slug] = 1

            outpath = os.path.join(DEST_DIR, f"{slug}.md")
            with open(outpath, 'w', encoding='utf-8') as f:
                f.write(content)
            converted += 1
        except Exception as e:
            print(f"ERROR processing {filepath}: {e}")
            errors += 1

    print(f"Converted: {converted}, Errors: {errors}")


if __name__ == "__main__":
    main()

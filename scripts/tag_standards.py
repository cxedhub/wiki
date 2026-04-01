#!/usr/bin/env python3
"""Auto-tag lessons with national/recognized standard framework types.

Scans each lesson's frontmatter `standards` field AND body content (especially
the "Other Content Standards" table row) to detect references to known
standards frameworks, then writes a `standard_types` array into frontmatter.

Recognized frameworks:
  - CCSS Math        Common Core State Standards - Mathematics
  - CCSS ELA         Common Core State Standards - English Language Arts
  - NGSS             Next Generation Science Standards
  - CSTA             Computer Science Teachers Association (K-12 CS Framework)
  - ISTE             International Society for Technology in Education
"""

import os
import re
import yaml

LESSONS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'lessons')

# ── Detection patterns ──────────────────────────────────────────────────────
# Each entry: (framework_name, list_of_compiled_regexes)
# A lesson matches if ANY regex in the list hits the combined search text.

FRAMEWORKS = {
    'CCSS Math': [
        # Explicit CCSS Math references
        re.compile(r'CCSS\.?\s*Math', re.I),
        re.compile(r'CCSS\.MATH\.CONTENT', re.I),
        re.compile(r'Common\s+Core.*Math', re.I),
        re.compile(r'math\s+common\s+core', re.I),
        # Common Core math domain codes (grade.domain.cluster.standard)
        # OA = Operations & Algebraic Thinking, NBT = Number & Operations Base Ten,
        # NF = Number & Operations Fractions, MD = Measurement & Data,
        # G = Geometry, RP = Ratios, NS = Number System, EE = Expressions & Equations,
        # SP = Statistics & Probability, F = Functions
        re.compile(r'\b[K1-8]\.(?:OA|NBT|NF|MD|CC|RP|NS|EE|SP)\b', re.I),
        re.compile(r'\b\d\.(?:OA|NBT|NF|MD|G|RP|NS|EE|SP|F)\.[A-Z]?\.\d', re.I),
        # e.g., "4.NF.3", "3.OA.A.1", "K.CC.A.3", "6.EE.E.1"
        re.compile(r'\b[K1-8]\.(?:OA|NBT|NF|MD|CC|RP|NS|EE|SP|G)\.[A-Z0-9]', re.I),
        # High school math: HSN, HSA, HSF, HSG, HSS
        re.compile(r'\bHS[NAFGS]\b', re.I),
        # MP = Mathematical Practices
        re.compile(r'\bMP\.\d\b'),
        re.compile(r'\b\d\.MP\.\d\b'),
    ],
    'CCSS ELA': [
        # Explicit CCSS ELA references
        re.compile(r'CCSS\.?\s*ELA', re.I),
        re.compile(r'CCSS\.ELA-LITERACY', re.I),
        re.compile(r'Common\s+Core.*(?:ELA|English|Literacy|Reading|Writing)', re.I),
        # ELA strand codes: RL, RI, RF, W, SL, L  (with grade prefix)
        # e.g., "RL.5.5", "RI.3.1", "RF.K.2", "W.4.4", "SL.5.1", "L.4.3"
        re.compile(r'\b(?:RL|RI|RF|SL|L)\.[K1-9]\.\d', re.I),
        re.compile(r'\bW\.[K1-9]\.[1-9]\b'),
        # Compact: "SL5.1", "RI5.6", "RF1.4"
        re.compile(r'\b(?:RL|RI|RF|SL)\d\.\d', re.I),
        # Writing standards: W2.6, W.1.8
        re.compile(r'\bW\d\.\d', re.I),
        # WHST = Writing History/Science/Technical (also ELA)
        re.compile(r'\bWHST\.\d', re.I),
        # ELA explicit prefix
        re.compile(r'\bELA[.\s]', re.I),
    ],
    'NGSS': [
        # Explicit NGSS
        re.compile(r'\bNGSS\b', re.I),
        re.compile(r'Next\s+Generation\s+Science', re.I),
        # Performance Expectations: K-PS2-1, 4-PS3-2, MS-LS1-1, HS-PS1-3
        # K/grade prefix + disciplinary core idea + number
        re.compile(r'\b(?:K|[1-5])-(?:PS[1-4]|LS[1-4]|ESS[1-3]|ETS[1-2])-\d', re.I),
        re.compile(r'\b(?:MS|HS)-(?:PS[1-4]|LS[1-4]|ESS[1-3]|ETS[1-2])-\d', re.I),
        # Standalone "3-ESS2-1" style
        re.compile(r'\b\d-(?:ESS|ETS|PS|LS)\d-\d', re.I),
    ],
    'CSTA': [
        # Explicit CSTA
        re.compile(r'\bCSTA\b', re.I),
        # CSTA standard codes: 1A-CS-01, 1B-AP-08, 2-CS-01, 3A-AP-13
        re.compile(r'\b[123][AB]?-(?:CS|NI|DA|AP|IC)-\d{2}\b', re.I),
    ],
    'ISTE': [
        # Explicit ISTE
        re.compile(r'\bISTE\b', re.I),
        # ISTE codes when preceded by ISTE context (handled via body scan)
    ],
}

# Wyoming CS Standards patterns - detect these so we can tag them too
WYOMING_CS_PATTERNS = [
    # Grade-banded: K-2.AP.A.01, 3-5.IC.SI.02
    re.compile(r'\bK-2\.(?:CS|NI|DA|AP|IC)\b', re.I),
    re.compile(r'\b3-5\.(?:CS|NI|DA|AP|IC)\b', re.I),
    re.compile(r'\b6-8\.(?:CS|NI|DA|AP|IC)\b', re.I),
    # Single grade: 2.AP.A.01, 5.NI.C.01, 8.CS.HS.01
    re.compile(r'\b[2-8]\.(?:CS|NI|DA|AP|IC)\.[A-Z]{1,3}\.\d{2}\b', re.I),
    # Wyoming Boot Up: L1.AP.C.01
    re.compile(r'\bL[12]\.(?:CS|NI|DA|AP|IC)\b', re.I),
    re.compile(r'Wyoming\s+(?:Boot\s*Up|Computer\s+Science|CS)\b', re.I),
    re.compile(r'\bWYSS\b', re.I),
]


def parse_frontmatter(filepath):
    """Parse YAML frontmatter and body from a markdown file."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not m:
        return None, content, ''

    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, content, ''

    return fm, content, m.group(2)


def extract_standards_text(fm, body):
    """Build the combined text to scan for standards references."""
    parts = []

    # Frontmatter standards field
    std = fm.get('standards', '') or ''
    if isinstance(std, str):
        parts.append(std)

    # Body: look for the "Other Content Standards" table row
    table_match = re.search(
        r'\|\s*Other\s+Content\s+Standards\s*\|(.*?)\|',
        body, re.I | re.DOTALL
    )
    if table_match:
        parts.append(table_match.group(1))

    # Also scan the full body for explicit framework mentions
    parts.append(body)

    return '\n'.join(parts)


def detect_frameworks(search_text, fm):
    """Detect which standards frameworks are referenced."""
    found = []

    for framework, patterns in FRAMEWORKS.items():
        for pat in patterns:
            if pat.search(search_text):
                found.append(framework)
                break

    # Check for Wyoming CS standards
    for pat in WYOMING_CS_PATTERNS:
        if pat.search(search_text):
            found.append('Wyoming CS')
            break

    return sorted(set(found))


def rebuild_file(filepath, new_standard_types):
    """Add/update standard_types in frontmatter."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not m:
        return False

    fm_text = m.group(1)
    body = m.group(2)

    # Remove existing standard_types block
    fm_text = re.sub(r'^standard_types:\s*\n(?:\s*-\s*.+\n)*', '', fm_text, flags=re.MULTILINE)
    fm_text = re.sub(r'^standard_types:\s*\[.*?\]\s*\n?', '', fm_text, flags=re.MULTILINE)
    fm_text = re.sub(r'^standard_types:\s*\n', '', fm_text, flags=re.MULTILINE)

    fm_text = fm_text.rstrip()

    # Build new standard_types
    if new_standard_types:
        st_yaml = 'standard_types:\n' + ''.join(f'- "{t}"\n' for t in new_standard_types)
    else:
        st_yaml = ''

    # Insert before tags line if present, otherwise append
    if st_yaml:
        new_content = f"---\n{fm_text}\n{st_yaml}---\n{body}"
    else:
        new_content = f"---\n{fm_text}\n---\n{body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    stats = {}
    total = 0
    tagged = 0

    for fname in sorted(os.listdir(LESSONS_DIR)):
        if not fname.endswith('.md') or fname == '_index.md':
            continue

        filepath = os.path.join(LESSONS_DIR, fname)
        fm, content, body = parse_frontmatter(filepath)
        if fm is None:
            print(f"SKIP (no frontmatter): {fname}")
            continue

        total += 1
        search_text = extract_standards_text(fm, body)
        frameworks = detect_frameworks(search_text, fm)

        if frameworks:
            tagged += 1

        for fw in frameworks:
            stats[fw] = stats.get(fw, 0) + 1

        rebuild_file(filepath, frameworks)

    print(f"\nProcessed {total} lessons, {tagged} tagged with at least one standard framework")
    print(f"\nFramework distribution:")
    for fw, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {fw}: {count}")

    untagged = total - tagged
    print(f"\n  (no framework detected): {untagged}")


if __name__ == '__main__':
    main()

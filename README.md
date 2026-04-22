# CRAFT PD Series — Deployment Package

Generated: April 6, 2026

## What's in this package

### content/ (Hugo content pages — copy to repo's content/)

```
content/pds/craft-pd-series/
├── _index.md                      # Series overview (UPDATED: Zoom links, resource links, taxonomy)
├── workshop-1-ai-for-stem.md      # Workshop 1 (UPDATED: surveys, Zoom, shared doc, all resources)
├── workshop-2-verifying-outputs.md # Workshop 2 (UPDATED: surveys, Zoom, shared doc, all resources)
└── workshop-3-edge-iot.md          # Workshop 3 (UPDATED: surveys, Zoom, shared doc, all resources)
```

### static/ (static files — copy to repo's static/)

```
static/pds/craft-pd-series/
├── CRAFT_PD_Series_Facilitator_Agenda.docx    # Master facilitator agenda (all links embedded)
├── W1-Digital-Toolkit.pdf                      # Workshop 1 downloadable toolkit
├── W2-Digital-Toolkit.pdf                      # Workshop 2 downloadable toolkit
├── W3-Digital-Toolkit.pdf                      # Workshop 3 downloadable toolkit
├── Workshop-1-Shared-Group-Workspace.docx      # Backup copy of collaborative doc
├── Workshop-2-Shared-Group-Workspace.docx      # Backup copy of collaborative doc
├── Workshop-3-Shared-Group-Workspace.docx      # Backup copy of collaborative doc
└── resources/
    ├── prompt-library.html                     # NEW: Tested prompts for STEM teaching
    ├── platform-comparison.html                # NEW: ChatGPT vs Claude vs Gemini
    ├── sensor-reference-guide.html             # NEW: micro:bit V2 sensor guide
    ├── ngss-crosswalk.html                     # NEW: IoT activities → NGSS PEs
    ├── craft-cycle-one-pager.html              # NEW: Printable CRAFT overview
    ├── welcome-email-template.html             # NEW: Registration/reminder email templates
    ├── W1-Pre-Survey.txt                       # Qualtrics Advanced Format import
    ├── W1-Post-Survey.txt
    ├── W2-Pre-Survey.txt
    ├── W2-Post-Survey.txt
    ├── W3-Pre-Survey.txt
    └── W3-Post-Survey.txt
```

## Links embedded in all materials

### Zoom
- W1: https://ucf.zoom.us/j/96520248667
- W2: https://ucf.zoom.us/j/96789217432
- W3: https://ucf.zoom.us/j/97106116299
- Passwords: see calendar invitations

### Qualtrics Surveys
- W1 Pre: https://ucf.qualtrics.com/jfe/form/SV_bq1qU641tSt7O0S
- W1 Post: https://ucf.qualtrics.com/jfe/form/SV_eEswd3p2cnnrZVs
- W2 Pre: https://ucf.qualtrics.com/jfe/form/SV_5c01mD7bR8nzB3M
- W2 Post: https://ucf.qualtrics.com/jfe/form/SV_6KEIQN9w20YvCMm
- W3 Pre: https://ucf.qualtrics.com/jfe/form/SV_8G2kZYDDaRslsDY
- W3 Post: https://ucf.qualtrics.com/jfe/form/SV_5cnzJo6KUcwqa34

### Shared Group Workspaces (Google Docs)
- W1: https://docs.google.com/document/d/11sYpp3Ho0PUEOwjro4M5fkpMwp-9XPLo/edit
- W2: https://docs.google.com/document/d/1J3NOX0FSU1uqiCNphZHX1IIGM7oFa3Pd/edit
- W3: https://docs.google.com/document/d/1GaTY3haKOuy2qzUb-GfT4xE8yeRu9QpK/edit

### Live Agenda (facilitator timing board, visible to all)
- W1: https://docs.google.com/document/d/15c5VIEnaDM7NP8fU7pfKloeMp7f1L4rd/edit
- W2: https://docs.google.com/document/d/1HNAUpx-D3OZEaHAfd6hNqrhe-qxWsplo/edit
- W3: https://docs.google.com/document/d/1v_qa_kaK4uQp3etpBsuLfx_SCPwXGkdjOuLuF6BjIx8/edit?tab=t.0

Note: the participant-facing HTML pages at `/pds/craft-pd-series/workshop-N-agenda.html` are the **Planned Agenda** (static). The **Live Agenda** is a Google Doc that facilitators mark up during the session.

## Deployment steps

```bash
cd /path/to/cxedhub/wiki

# Extract the zip
unzip craft-pd-deploy.zip -d .

# Stage ALL files (content AND static)
git add content/pds/craft-pd-series/
git add static/pds/craft-pd-series/

# Commit and push
git commit -m "CRAFT PD Series: add surveys, shared docs, Zoom links, 6 new resource pages, digital toolkits"
git push origin main
```

## What changed in the markdown files

All 4 content markdown files were updated with:
- `cs_domains` and `standard_types` added to front matter (site taxonomy integration)
- `WySTACK` tag added
- Zoom join links in each workshop header
- Pre-survey and post-survey Qualtrics links in a new "Surveys" section
- Shared Group Workspace Google Doc links in a new "Shared Workspace" section
- Links to all 6 new resource pages in the "Session Resources" section
- Digital Toolkit PDF download links
- Cross-workshop resources included on every day (Prompt Library, Platform Comparison, CRAFT 1-Pager)
- Workshop-specific resources on their respective days only

## Resource distribution across workshops

| Resource | W1 | W2 | W3 |
|----------|:--:|:--:|:--:|
| CRAFT Cycle One-Pager | ✅ | ✅ | ✅ |
| Prompt Library | ✅ | ✅ | ✅ |
| Platform Comparison | ✅ | ✅ | — |
| Lesson Template | ✅ | — | — |
| Error Gallery | — | ✅ | — |
| Content Audit Checklist | — | ✅ | — |
| CtM Template | — | ✅ | ✅ |
| IoT Lesson Template | — | — | ✅ |
| Sensor Reference Guide | — | — | ✅ |
| NGSS Crosswalk | — | — | ✅ |

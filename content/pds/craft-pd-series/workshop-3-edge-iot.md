---
title: "Workshop 3: Programming Edge/IoT Systems with AI"
description: "BBC micro:bit + LLM-assisted coding to bridge abstract programming and physical science standards."
date: 2026-04-25
draft: false
tags: ["IoT", "micro:bit", "CRAFT", "edge-computing", "MakeCode", "MicroPython", "WySTACK"]
subjects: ["Computer Science", "Science", "Engineering"]
grade_levels: ["K-2", "3-5", "6-8", "9-12"]
cs_domains: ["Algorithms and Programming", "Computing Systems", "Data and Analysis"]
standard_types: ["NGSS", "ISTE", "CSTA"]
workshop_number: 3
series: "CRAFT PD Series"
facilitators: "Dr. Mike Borowczak & Dr. Andrea Borowczak"
audience: "Mixed in-service and pre-service STEM teachers (Noyce recipients)"
delivery: "Virtual (Zoom)"
time: "8:30 AM – 12:00 PM PST"
accent_color: "#27AE60"
accent_gradient: ["#27AE60", "#1ABC9C", "#8E6BBF"]
focus_tags:
  - "BBC micro:bit"
  - "Physical Computing"
  - "LLM-Assisted Coding"
learning_objectives:
  - "Explain Edge Computing and IoT and their workforce relevance"
  - "Program micro:bit with 2+ sensors using MakeCode"
  - "Use an LLM to write, debug, and extend micro:bit code"
  - "Optionally convert MakeCode to MicroPython"
  - "Align sensor activities to NGSS and CTE pathways"
  - "Plan a CRAFT-structured IoT lesson for their classroom"
key_activities:
  - "Hardware connectivity check + troubleshooting"
  - "Single-sensor program (temperature → LED display)"
  - "Multi-sensor breakout challenge (2+ sensors, LLM-assisted coding)"
  - "Level-up track split: Track A (MakeCode+) vs Track B (MicroPython)"
  - "Sensor verification experiment (temperature sensor reads CPU heat, not ambient — real calibration problem)"
  - "IoT lesson template customization"
takeaways:
  - "BBC micro:bit V2 kit (yours to keep)"
  - "MakeCode project files"
  - "MicroPython starters"
  - "Sensor reference guide"
  - "NGSS alignment crosswalk"
  - "IoT lesson template"
hardware: "BBC micro:bit V2 (mailed in advance, participants keep it)"
programming_environments: "MakeCode (blocks/JavaScript) primary, MicroPython optional level-up"
reframe_theme: "Coding is PHYSICAL, not just screens"
talk_do_ratio: "~30 min facilitator-led / ~150 min participant activities (1:5.0)"
talk_minutes: 30
do_minutes: 150
closing_quote: "You just programmed a physical computer using AI as your co-pilot and verified the results like an engineer. Your students can do this too."
---

**Date:** April 25, 2026 · 8:30 AM – 12:00 PM PST · Virtual (Zoom, with mailed hardware kits)

**Zoom:** [Join Workshop 3](https://ucf.zoom.us/j/97106116299) *(Password is in your calendar invitation.)*

**Focus:** NGSS/CTE alignment, hardware sensors, real-world data processing

**Talk:Do Ratio:** ~30 min facilitator / ~150 min participant activities (1:5.0)

**Hardware:** BBC micro:bit V2 — mailed in advance, yours to keep!

Take computing out of the browser and into the physical world. This session uses the BBC micro:bit and LLM-assisted coding to bridge abstract programming concepts and physical science standards.

## Surveys

- 📝 [Pre-Survey](https://ucf.qualtrics.com/jfe/form/SV_8G2kZYDDaRslsDY) — complete at the start of the session
- 📊 [Post-Survey](https://ucf.qualtrics.com/jfe/form/SV_5cnzJo6KUcwqa34) — complete at the end of the session

## Shared Workspace

- 📋 [Group Workspace (Google Doc)](https://docs.google.com/document/d/1GaTY3haKOuy2qzUb-GfT4xE8yeRu9QpK/edit?usp=drive_link&ouid=107503058538624505453&rtpof=true&sd=true) — collaborative document for all breakout and group activities

## Pre-Session Requirements

- BBC micro:bit V2 kit received by mail and connected via USB
- [MakeCode editor](https://makecode.microbit.org) open in browser (Chrome or Edge recommended)
- LLM of choice open in a second tab ([ChatGPT](https://chat.openai.com), [Claude](https://claude.ai), or [Gemini](https://gemini.google.com))
- Hardware check email sent 3 days prior with setup instructions

## Learning Objectives

- Explain what Edge Computing and IoT are and why they matter for the modern STEM workforce
- Program a BBC micro:bit to collect data from 2+ onboard sensors using MakeCode
- Use an LLM to assist with writing, debugging, and extending micro:bit code
- Optionally level-up from MakeCode (blocks) to MicroPython (text-based)
- Align a sensor-based activity to specific NGSS performance expectations and CTE pathways
- Identify CRAFT phases in the session and plan how to replicate the structure

## Session Resources

- [**📋 Live Agenda**](/pds/craft-pd-series/workshop-3-agenda.html) — participant-facing timeline with activity links and print view
- [**🖥 Web Slides**](/pds/craft-pd-series/slides-w3.html) — keyboard-navigable presentation (← → arrows, F for fullscreen)
- [**⬇ Download Slides (PPTX)**](/pds/craft-pd-series/Workshop-3-Slides.pptx) — import to Google Slides
- [**📄 IoT Lesson Template**](/resources/iot-lesson-template.html) — template for designing sensor-based STEM lessons
- [**🧰 Sensor-to-Standards Lesson Generator**](/pds/craft-pd-series/resources/sensor-builder.html) — fillable CRAFT-structured IoT lesson builder with sensor selection, multi-framework standards search (NGSS, CSTA, CCSS, ISTE, NCSS C3), auto-generated MakeCode + MicroPython scaffolds, and AI prompt round-trip
- [**🔬 Sensor Reference Guide**](/pds/craft-pd-series/resources/sensor-reference-guide.html) — all micro:bit V2 onboard sensors with code and calibration notes
- [**📊 NGSS Alignment Crosswalk**](/pds/craft-pd-series/resources/ngss-crosswalk.html) — IoT activities mapped to NGSS Performance Expectations
- [**📚 Prompt Library**](/pds/craft-pd-series/resources/prompt-library.html) — includes physical computing prompts for micro:bit
- [**✅ CtM Template**](/pds/craft-pd-series/resources/ctm-template.html) — for sensor verification activities
- [**📄 CRAFT Cycle One-Pager**](/pds/craft-pd-series/resources/craft-cycle-one-pager.html) — printable overview of the CRAFT framework

### MicroPython Starter Scripts

Ready-to-flash equivalents of every MakeCode activity (for Track B participants):

- [01 — Temperature Display](/pds/craft-pd-series/resources/micropython/01_temperature_display.py)
- [02 — Temperature + Light](/pds/craft-pd-series/resources/micropython/02_temp_and_light.py)
- [03 — Greenhouse Monitor](/pds/craft-pd-series/resources/micropython/03_greenhouse_monitor.py)
- [04 — Motion + Compass](/pds/craft-pd-series/resources/micropython/04_motion_compass.py)
- [05 — Comfort Index](/pds/craft-pd-series/resources/micropython/05_comfort_index.py)

## Programming Environments

- [**MakeCode Editor**](https://makecode.microbit.org) — block-based (primary)
- [**MicroPython Editor**](https://python.microbit.org) — text-based (level-up)

## Key Activities

| CRAFT Phase | Activity | Duration | Type |
|-------------|----------|----------|------|
| — | Hardware Check + Icebreaker + Pre-Survey | 15 min | You Do |
| Contextualize | CRAFT Orientation + IoT Brainstorm | 15 min | You Do |
| Reframe | Poll + "Coding Is Physical" | 15 min | Listen |
| Reframe | Breakout: Barriers to Hardware Teaching | 15 min | You Do |
| Assemble | I Do + Guided: First Sensor Program | 30 min | You Do |
| Assemble | Breakout: Multi-Sensor Challenge | 30 min | You Do |
| Assemble | Level Up: Track A (MakeCode+) or Track B (MicroPython) | 30 min | You Do |
| Fortify | Experiment: Verify Your Sensor Data | 15 min | You Do |
| Transfer | Build: IoT Lesson + Pair-Share + Post-Survey | 15 min | You Do |

## Level-Up Tracks

**Track A — MakeCode+:** Extend your project with LED visualization, radio communication between micro:bits, or complex sensor logic.

**Track B — MicroPython:** Convert your MakeCode project to Python using the [micro:bit Python editor](https://python.microbit.org). Ask an LLM to translate your blocks, then verify it actually runs on your device.

## Participant Takeaways

- BBC micro:bit V2 kit (yours to keep!)
- MakeCode project files from all session activities
- MicroPython starter scripts (equivalents for every MakeCode activity)
- Sensor reference guide for all micro:bit V2 onboard sensors
- NGSS alignment crosswalk (IoT activities mapped to performance expectations)
- Customized IoT lesson template with student-facing CtM prompt
- Digital Toolkit PDF with all resources

## Reframe Theme

> "Coding is PHYSICAL, not just screens." — The micro:bit costs ~$15, runs on USB with no WiFi needed. LLMs help you write the code — the skill is knowing WHAT to ask and HOW to verify.

---

**Other Workshops:** [Workshop 1: AI for STEM](/pds/craft-pd-series/workshop-1-ai-for-stem/) · [Workshop 2: Verifying AI Outputs](/pds/craft-pd-series/workshop-2-verifying-outputs/)

[← Back to Series Overview](/pds/craft-pd-series/) · [← All Professional Development](/pds/)

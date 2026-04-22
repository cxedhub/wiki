---
title: "Workshop 3: Programming Edge/IoT Systems with AI"
description: "BBC micro:bit in the MakeCode simulator + LLM-assisted coding — build a two-node IoT system without any hardware."
date: 2026-04-25
draft: false
tags: ["IoT", "micro:bit", "CRAFT", "edge-computing", "MakeCode", "simulator", "MicroPython", "radio", "WySTACK"]
subjects: ["Computer Science", "Science", "Engineering"]
grade_levels: ["K-2", "3-5", "6-8", "9-12"]
cs_domains: ["Algorithms and Programming", "Computing Systems", "Data and Analysis", "Networks and the Internet"]
standard_types: ["NGSS", "ISTE", "CSTA"]
workshop_number: 3
series: "CRAFT PD Series"
facilitators: "Dr. Mike Borowczak & Dr. Andrea Borowczak"
audience: "Mixed in-service and pre-service STEM teachers (Noyce recipients)"
delivery: "Virtual (Zoom) — 100% online, no hardware required during the session"
time: "8:30 AM – 12:00 PM PST"
accent_color: "#27AE60"
accent_gradient: ["#27AE60", "#1ABC9C", "#8E6BBF"]
focus_tags:
  - "BBC micro:bit (online simulator)"
  - "Physical Computing"
  - "IoT / Radio Networking"
  - "LLM-Assisted Coding"
learning_objectives:
  - "Explain Edge Computing and IoT as a two-role system: sensing nodes and aggregating/display nodes"
  - "Program a sensor node (collect + radio.send) in the MakeCode simulator"
  - "Program an aggregator node (radio.receive + aggregate + display) in the MakeCode simulator"
  - "Pair two simulated micro:bits on a shared radio group so they talk to each other"
  - "Use an LLM to write, debug, and extend two-node micro:bit code"
  - "Optionally port MakeCode to MicroPython (python.microbit.org) — simulator or real hardware"
  - "Align a sensor-and-aggregator activity to NGSS and CTE pathways"
  - "Plan a CRAFT-structured IoT lesson for their classroom"
key_activities:
  - "Simulator warm-up in makecode.microbit.org (no hardware needed)"
  - "Role A: Sensor Node program — read a sensor, radio.send the value"
  - "Role B: Aggregator Node program — radio.receive, running average/min/max, LED display"
  - "Paired breakout: one participant builds Role A, partner builds Role B, share a radio group"
  - "Level-up: multi-sensor mesh (2+ senders → 1 aggregator) or MicroPython port"
  - "Sensor verification in simulator (known-good inputs, edge cases) + discussion of real-hardware calibration surprise"
  - "IoT lesson template customization (two-node design)"
takeaways:
  - "BBC micro:bit V2 kit — SHIPPED AFTER the session to participants who complete both surveys + submit a draft IoT lesson (yours to keep)"
  - "MakeCode .hex files for Sensor Node + Aggregator Node (ready to flash when hardware arrives)"
  - "MicroPython radio starters (sender + receiver)"
  - "Sensor reference guide"
  - "NGSS alignment crosswalk"
  - "Two-node IoT lesson template"
hardware: "NONE required during the session. All activities run in the MakeCode online simulator (two simulated micro:bits appear automatically when you use radio). BBC micro:bit V2 kits are mailed AFTER the session to participants who complete it — yours to keep."
programming_environments: "MakeCode online simulator (primary, blocks/JavaScript), python.microbit.org simulator (level-up, MicroPython)"
reframe_theme: "IoT is a CONVERSATION between devices — and you can have that conversation in a browser tab."
talk_do_ratio: "~30 min facilitator-led / ~150 min participant activities (1:5.0)"
talk_minutes: 30
do_minutes: 150
closing_quote: "You just built a two-node IoT system in a browser, with AI as your co-pilot, and verified it like an engineer. When your kit arrives, the same .hex files flash to real hardware. Your students can do this too — even in schools with zero hardware budget."
---

**Date:** April 25, 2026 · 8:30 AM – 12:00 PM PST · Virtual (Zoom)

**Zoom:** [Join Workshop 3](https://ucf.zoom.us/j/97106116299) *(Password is in your calendar invitation.)*

**Focus:** Edge Computing + IoT as a two-device conversation — sensor node ↔ aggregator node — built entirely in the MakeCode online simulator.

**Talk:Do Ratio:** ~30 min facilitator / ~150 min participant activities (1:5.0)

**Hardware:** None required for the live session. Everything runs in [makecode.microbit.org](https://makecode.microbit.org) in your browser. Participants who complete both surveys + submit a draft IoT lesson receive a **BBC micro:bit V2 kit in the mail** — yours to keep, to bring this into your classroom.

Take computing out of the browser — conceptually — while still teaching it in one. The MakeCode simulator gives every participant a fully-functional micro:bit inside a browser tab, and the moment you drop in a radio block, MakeCode spawns a second simulator so you can build and test a two-node IoT system without owning any hardware. That same code flashes to a real device the day your kit arrives.

## Surveys

- 📝 [Pre-Survey](https://ucf.qualtrics.com/jfe/form/SV_8G2kZYDDaRslsDY) — complete at the start of the session
- 📊 [Post-Survey](https://ucf.qualtrics.com/jfe/form/SV_5cnzJo6KUcwqa34) — complete at the end of the session
- 📦 **Completing both surveys + submitting a draft IoT lesson unlocks your mailed micro:bit V2 kit.**

## Shared Workspace

- 📋 [Group Workspace (Google Doc)](https://docs.google.com/document/d/1GaTY3haKOuy2qzUb-GfT4xE8yeRu9QpK/edit?usp=drive_link&ouid=107503058538624505453&rtpof=true&sd=true) — collaborative document for all breakout and group activities

## Pre-Session Requirements

- A modern browser (Chrome or Edge recommended) with [makecode.microbit.org](https://makecode.microbit.org) accessible
- An LLM of choice open in a second tab ([ChatGPT](https://chat.openai.com), [Claude](https://claude.ai), or [Gemini](https://gemini.google.com))
- A pre-session email will confirm your browser can load MakeCode and that both simulators render
- **No hardware needed.** If your shipped kit has already arrived, great — but you do not need it for any activity today.

## Learning Objectives

- Explain Edge Computing and IoT and why the **two-role** pattern (sensor + aggregator) is the backbone of real-world IoT
- Build a Sensor Node program that reads a sensor and broadcasts the value on a radio group
- Build an Aggregator Node program that receives values, aggregates them (running average, min/max, counts, thresholds), and displays a result
- Pair two participants on the same radio group so one's sender talks to the other's receiver — all in simulation
- Use an LLM to assist with writing, debugging, and extending both halves of the system
- Optionally level-up from MakeCode (blocks) to MicroPython (text) — still in a simulator
- Align a two-node sensor activity to specific NGSS performance expectations and CTE pathways
- Identify CRAFT phases in the session and plan how to replicate the structure

## Session Resources

- [**📋 Live Agenda**](/pds/craft-pd-series/workshop-3-agenda.html) — participant-facing timeline with activity links and print view
- [**🖥 Web Slides**](/pds/craft-pd-series/slides-w3.html) — keyboard-navigable presentation (← → arrows, F for fullscreen)
- [**⬇ Download Slides (PPTX)**](/pds/craft-pd-series/Workshop-3-Slides.pptx) — import to Google Slides
- [**📄 IoT Lesson Template**](/resources/iot-lesson-template.html) — template for designing two-node sensor/aggregator STEM lessons
- [**🔬 Sensor Reference Guide**](/pds/craft-pd-series/resources/sensor-reference-guide.html) — all micro:bit V2 onboard sensors with code and calibration notes
- [**📊 NGSS Alignment Crosswalk**](/pds/craft-pd-series/resources/ngss-crosswalk.html) — IoT activities mapped to NGSS Performance Expectations
- [**📚 Prompt Library**](/pds/craft-pd-series/resources/prompt-library.html) — includes physical computing + radio communication prompts
- [**✅ CtM Template**](/pds/craft-pd-series/resources/ctm-template.html) — for sensor verification activities
- [**📄 CRAFT Cycle One-Pager**](/pds/craft-pd-series/resources/craft-cycle-one-pager.html) — printable overview of the CRAFT framework

### MicroPython Starter Scripts

Ready-to-flash equivalents of the simulator activities — run in the [python.microbit.org](https://python.microbit.org) simulator today, flash to your kit when it arrives:

- [01 — Sensor Node: Temperature Sender](/pds/craft-pd-series/resources/micropython/01_sensor_node_temp.py)
- [02 — Aggregator Node: Running Average Receiver](/pds/craft-pd-series/resources/micropython/02_aggregator_running_avg.py)
- [03 — Sensor Node: Multi-Sensor Sender (temp + light)](/pds/craft-pd-series/resources/micropython/03_sensor_node_multi.py)
- [04 — Aggregator Node: Threshold Alert Display](/pds/craft-pd-series/resources/micropython/04_aggregator_threshold.py)
- [05 — Comfort Index (single-device, level-up)](/pds/craft-pd-series/resources/micropython/05_comfort_index.py)

## Programming Environments

- [**MakeCode Editor**](https://makecode.microbit.org) — block-based, runs two simulated micro:bits side-by-side when you use radio (primary)
- [**MicroPython Editor**](https://python.microbit.org) — text-based, also has an online simulator (level-up)

## Key Activities

| CRAFT Phase | Activity | Duration | Type |
|-------------|----------|----------|------|
| — | Opening: Simulator Check + Icebreaker + Pre-Survey | 15 min | You Do |
| Contextualize | CRAFT Orientation + IoT as a Two-Device Conversation | 15 min | You Do |
| Reframe | Poll + "Physical Computing Lives in the Browser Too" | 15 min | Listen |
| Reframe | Breakout: Barriers to Teaching Hardware Without Hardware | 15 min | You Do |
| Assemble | Server Room Guardian: live-build sensor + aggregator, then swap in your own sensor | 30 min | You Do |
| Assemble | Enhancements + Brainstorm: liveness ping, Data panel graphing, LLM-driven extensions | 30 min | You Do |
| Assemble | Level Up: Multi-Sensor Mesh (A) or MicroPython Port (B) | 30 min | You Do |
| Fortify | Experiment: Verify Simulated Data + Calibration Preview | 15 min | You Do |
| Transfer | Build: Two-Node IoT Lesson + Pair-Share + Post-Survey | 15 min | You Do |

## The Two-Role IoT Pattern

Every IoT system — a smart farm, a weather station, a wearable, a traffic monitor — is at its heart a **conversation** between two kinds of devices:

| Role | Job | What It Looks Like in MakeCode |
|------|-----|-------------------------------|
| **Sensor Node** | Read the world. Broadcast the reading. | `on start: radio.setGroup(N)` · `forever: radio.sendNumber(input.temperature())` · sleep · repeat |
| **Aggregator Node** | Listen to one or many senders. Aggregate. Display. Decide. | `on start: radio.setGroup(N)` · `on radio.receivedNumber(v)`: update running average, show on LEDs, trigger alert |

When you drag a radio block into MakeCode, the simulator **automatically shows two simulated micro:bits** so you can watch the message go from sender to receiver in real time. That's your classroom-ready IoT demo — no mailing list required.

## Level-Up Tracks

**Track A — Multi-Sensor Mesh:** Add a second sensor node by opening your Sensor project in a second browser tab (MakeCode pairs two simulators per tab, but tabs on the same origin share the radio channel). Two senders broadcast on the same group with different IDs; the aggregator tracks per-sender averages and flags which node is out of range.

**Track B — MicroPython Port:** Port your Sensor Node and Aggregator Node to MicroPython using [python.microbit.org](https://python.microbit.org). Ask an LLM to translate your blocks. Run both scripts in the MicroPython simulator and confirm the message still goes through.

## Participant Takeaways

- MakeCode project files (.hex) for Sensor Node + Aggregator Node + level-up extensions
- MicroPython radio starter scripts
- Sensor reference guide for all micro:bit V2 onboard sensors
- NGSS alignment crosswalk (IoT activities mapped to performance expectations)
- Customized two-node IoT lesson template with student-facing CtM prompt
- Digital Toolkit PDF with all resources
- **BBC micro:bit V2 kit mailed after the session** — for participants who complete both surveys and submit a draft IoT lesson

## Reframe Theme

> "IoT is a CONVERSATION between devices — and you can have that conversation in a browser tab." — The MakeCode simulator runs two full micro:bits side-by-side the moment you add a radio block. Your students don't need hardware on day one. You don't need hardware today. When the kit arrives, the same .hex flashes to the real device — the code doesn't change.

---

**Other Workshops:** [Workshop 1: AI for STEM](/pds/craft-pd-series/workshop-1-ai-for-stem/) · [Workshop 2: Verifying AI Outputs](/pds/craft-pd-series/workshop-2-verifying-outputs/)

[← Back to Series Overview](/pds/craft-pd-series/) · [← All Professional Development](/pds/)

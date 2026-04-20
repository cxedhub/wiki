---
title: "Integrated STEM: Programming Edge/IoT Systems with AI"
description: "Take computing out of the browser — conceptually — while building a two-node IoT system entirely inside the browser."
date: '2026-04-25T08:30:00-07:00'
draft: true
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
  - "Program a Sensor Node (read sensor + radio.send) in the MakeCode online simulator"
  - "Program an Aggregator Node (radio.receive + aggregate + display) in the MakeCode online simulator"
  - "Pair two simulated micro:bits on a shared radio group so they talk to each other"
  - "Use an LLM to write, debug, and extend both halves of the two-node system"
  - "Optionally port MakeCode to MicroPython in a simulator"
  - "Align sensor + aggregator activities to NGSS and CTE pathways"
  - "Plan a CRAFT-structured two-node IoT lesson for their classroom"
key_activities:
  - "MakeCode simulator warm-up (no hardware needed)"
  - "Role A build: Sensor Node — read a sensor, radio.send the value"
  - "Role B build: Aggregator Node — radio.receive, aggregate, display"
  - "Paired breakout: one partner runs the sender, the other runs the receiver, on a shared radio group"
  - "Level-up split: Track A (multi-sensor mesh) vs Track B (MicroPython simulator port)"
  - "Sensor verification with known-good simulator inputs + preview of real-hardware calibration (temp sensor reads CPU heat, not ambient — a Fortify hook for when the kit arrives)"
  - "Two-node IoT lesson template customization"
takeaways:
  - "BBC micro:bit V2 kit — mailed after the session to participants who complete both surveys + submit a draft IoT lesson (yours to keep)"
  - "MakeCode .hex files for Sensor Node + Aggregator Node"
  - "MicroPython radio starters (sender + receiver)"
  - "Sensor reference guide"
  - "NGSS alignment crosswalk"
  - "Two-node IoT lesson template"
hardware: "NONE required during the session. All activities run in the MakeCode online simulator. BBC micro:bit V2 kits are mailed AFTER the session to participants who complete it."
programming_environments: "MakeCode online simulator (primary), python.microbit.org simulator (optional level-up)"
reframe_theme: "IoT is a CONVERSATION between devices — and you can have that conversation in a browser tab."
talk_do_ratio: "~30 min facilitator-led / ~150 min participant activities (1:5.0)"
talk_minutes: 30
do_minutes: 150
closing_quote: "You just built a two-node IoT system in a browser, with AI as your co-pilot, and verified it like an engineer. When your kit arrives, the same .hex files flash to real hardware. Your students can do this too — even in schools with zero hardware budget."
---

## Overview

BBC micro:bit in the MakeCode **online simulator** + LLM-assisted coding, framed around the two-role IoT pattern. Participants build a **Sensor Node** (collects + broadcasts) and an **Aggregator Node** (receives + aggregates + displays), paired with a partner so the two simulated devices talk on a shared radio group. No hardware is required to participate. Kits ship after the session to participants who complete it — they flash the same .hex files onto real devices.

## Reframe

**"IoT is a CONVERSATION between devices — and you can have that conversation in a browser tab."** — The moment you drop a radio block into MakeCode, the simulator spawns a second simulated micro:bit so you can watch the message travel from sender to receiver. Physical computing pedagogy is no longer gated by a hardware budget or a shipping timeline.

## Hardware & Environments

- **During the session:** NONE. All activities run in [makecode.microbit.org](https://makecode.microbit.org).
- **After the session:** BBC micro:bit V2 kit mailed to participants who complete both surveys + submit a draft IoT lesson. The .hex files built today flash directly to the hardware when it arrives.
- **Primary environment:** MakeCode online simulator (blocks/JavaScript).
- **Level-Up:** MicroPython simulator at [python.microbit.org](https://python.microbit.org).

## Session Structure

| Block | Time | Type | Duration |
|-------|------|------|----------|
| Welcome + Simulator Check + Pre-Survey | 8:30 | Admin/Do | 15 min |
| CRAFT Orientation + IoT as a Two-Device Conversation | 8:45 | Listen + Do | 15 min |
| Reframe (poll + breakout) | 9:00 | Listen + Do | 30 min |
| Break #1 | 9:30 | Break | 15 min |
| Assemble: Sensor Node → Aggregator Node → Paired pairs | 9:45 | Listen(brief) + Do(extended) | 60 min |
| Break #2 | 10:45 | Break | 15 min |
| Assemble: Level-Up (mesh or MicroPython) | 11:00 | Do | 30 min |
| Fortify (simulator verification + calibration preview) | 11:30 | Listen(brief) + Do | 15 min |
| Transfer (two-node lesson design + pair-share) | 11:45 | Do | 10 min |
| Resources + Post-Survey + Kit Unlock + Close | 11:55 | Admin | 5 min |

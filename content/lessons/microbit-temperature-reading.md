---
title: Micro:bit Temperature Reading
description: Students will program micro:bits to measure temperature readings in Celsius
  and then convert to Fahrenheit either using a math conversion.
date: '2023-03-13 00:00:00+00:00'
draft: false
author: Casey Harmon
subjects:
- Computer Science
- Mathematics
- Science
grade_levels:
- 6-8
cs_domains:
- Computing Systems
- Data Analysis
- Algorithms and Programming
cs_principles:
- Collaborating Around Computing
- Creating Computational Artifacts
- Testing and Refining Computational Artifacts
standards:
  CSTA:
  - 2-AP-10
  - 2-AP-11
  - 2-AP-12
  - 2-AP-17
  - 2-CS-01
  - 2-CS-02
  - 2-CS-03
  - 2-DA-07
  - 2-DA-08
  - 2-DA-09
  - 2-NI-06
  ISTE:
  - ISTE-1d
  - ISTE-4a
  - ISTE-4c
  - ISTE-4d
  - ISTE-6b
  CCSS Math:
  - 6.EE
  - 6.SP
  - 7.G
  NGSS:
  - MS-ESS2-4
  - MS-ESS2-5
  - MS-ESS2-6
  - MS-PS1-4
  - MS-PS1-6
  - MS-PS3-3
materials: Website, Micro:bit, makecode.microbit.org
tags:
- Data Collection
- micro:bit
standard_types:
- CCSS Math
- CSTA
- ISTE
- NGSS
supplements:
- /uploads/microbit-temperature-reading/microbit-temperature_-_Casey_Harmon.hex
- /uploads/microbit-temperature-reading/microbit-caseys-temp_-_Casey_Harmon.hex
---
# OVERVIEW
## Activity Overview:  
Students will program micro:bits to measure temperature readings in Celsius and then convert to Fahrenheit either using a math conversion.
## Meta description
+ *Subject Area:* Computer Science, Mathematics, Science 
+ *Grade Level :* 6-8 
+ *Computer Science Domains:*
   + Computing Systems, Data Analysis, Algorithms and Programming
+ *Computer Science Principles:*
   + Collaborating Around Computing, Creating Computational Artifacts, Testing and Refining Computational Artifacts
+ *Materials:* 
   + Website, Micro:bit, makecode.microbit.org
+ *Considerations:*
   + Basic weather gathering materials and knowledge needed. This lesson will enhance a two week period of gathering weather information.


# Lesson Plan
## Overview
Students will program micro:bits to measure temperature readings in Celsius and then convert to Fahrenheit either using a math conversion.
## ASSESSMENT PRE/POST-TEST
Can you accurately measure and interpret the temperature outside?
Can you program a micro:bit to measure the temperature outside?
Can you convert degrees Celsius to degrees Fahrenheit?
## OBJECTIVES
program a micro:bit, interpret and convert temperature readings


## CATCH/HOOK
https://nasaeclips.arc.nasa.gov/video/realworld/real-world-cubesats-a-satellite-small-enough-to-fit-in-your-hand


## ACTIVITY INSTRUCTIONS
*I will be sharing my screen for students to follow along and do as I do.


1. Students will receive materials necessary to accomplish task (micro:bit, USB charger, battery pack charger).
2. Students will log in to makecode.microbit.org and create a new project titled 'temperature'.
3. Students will use block code to program micro:bit with the ability to read the current temperature
4. Use 'On Start' block located on current board
5. Go to variables tab and make a 'temp C' variable
6. In variables tab- now find 'set temp C to ___', drag and drop block into your 'on start' block
7. Go to the input tab and find the 'temperature (C)' oval shape, place into the oval shape at the end of your red 'set temp C' block. Your micro:bit should now show a thermometer.
8. Now choose an input block, either 'on shake' or 'on button A (or B, or A &B) pressed', and drag and drop it on a clear space on your board.
9. Go to the Basics tab and choose the 'show number' block and drag and drop it into your purple input tab.
10. Right click the 'temperature (C)' oval from previous, or drag and drop a new one from the inputs tab, and carefully place into the number oval on your blue 'show number' block. 
11. Depending on your input block, use the action listed and do so to your micro:bit. The temperature should scroll across the screen.
12. Attach your handheld micro:bit with the USB and download the program. Find the 'hex' file located in your file explorer and drag and drop it to the 'Micro:bit' folder. Wait for download to complete and unplug mirco:bit.
13. Plug the battery pack into the microbit and test the temperature outside.
14. Take your temperature reading and convert to Fahrenheit. Multiply the reading by 9/5, then add 32. This is the temperature in Fahrenheit.


### Supplements
**Any items in this section are the property & under the license of their respective owners.**




## REVIEW
Now you know a simple program to place on a microbit, and how to convert Celsius to Fahrenheit. Reading the temperature can be an amusing and fun task when using computer science. 
For a career idea or another real life example:  https://climatekids.nasa.gov/career-satellites/
## STANDARDS        
| Type | Listing | 
|-----------|-----------|
| CS Domains  | Computing Systems, Data Analysis, Algorithms and Programming|
| CS Principles   | Collaborating Around Computing, Creating Computational Artifacts, Testing and Refining Computational Artifacts|
| Other Content Standards | ESS2  |
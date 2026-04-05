---
title: Power walkers
description: 'Students will program a mirco: bit to count steps while walking and
  then while power walking. They will compare the two readings.'
date: '2023-03-13 00:00:00+00:00'
draft: false
author: Casey Harmon
subjects:
- Computer Science
- Science
grade_levels:
- 6-8
cs_domains:
- Data Analysis
- Algorithms and Programming
cs_principles:
- Fostering an Inclusive Computing Culture
- Creating Computational Artifacts
materials: Website, Micro:bit
tags:
- Data Collection
- micro:bit
standards:
  CSTA:
  - 2-AP-10
  - 2-AP-11
  - 2-AP-12
  - 2-AP-17
  - 2-DA-07
  - 2-DA-08
  - 2-DA-09
  ISTE:
  - ISTE-1d
  - ISTE-4a
  - ISTE-4c
  - ISTE-6b
  - ISTE-7a
standard_types:
- CSTA
- ISTE
---
# OVERVIEW
## Activity Overview:  
Students will program a mirco: bit to count steps while walking and then while power walking. They will compare the two readings.
## Meta description
+ *Subject Area:* Computer Science, Science 
+ *Grade Level :* 6-8 
+ *Computer Science Domains:*
   + Data Analysis, Algorithms and Programming
+ *Computer Science Principles:*
   + Fostering an Inclusive Computing Culture, Creating Computational Artifacts
+ *Materials:* 
   + Website, Micro:bit
+ *Considerations:*
   + The amount of bounce or force in one's steps may affect the count, make sure the student's know to use big actions.


# Lesson Plan
## Overview
Students will program a mirco: bit to count steps while walking and then while power walking. They will compare the two readings.
## ASSESSMENT PRE/POST-TEST
Can you program a micro:bit to count your steps? Is the coding done in the micro:bit accurate? How did your two tests compare? How would you add to the program to enhance this lesson?
## OBJECTIVES
Program a micro:bit with step counting capabilities, Compare and Contrast


## CATCH/HOOK
https://www.youtube.com/watch?v=epT9o_Hksio


## ACTIVITY INSTRUCTIONS
Coding:
1. Open the website makecode.microbit.org
2. Start a new project and name it 'Power Walkers'
3. In this lesson, we will be counting our steps. The number of steps is our variable (because that number can change depending on many things), so let's make a variable. Go to the Variables tab and click on 'Make a Variable'. Name this variable 'step'.
4. Under that same tab- choose 'set step to 0' and place that block into your 'on start' block.
5. In the Input tab, we will use the 'on shake' block to be our stepping action. Place that tab beside your on start tab (they will not stick together).
6. Back in the variables tab, choose 'change step by 1' and place that block into your input shake block.
7. We'd like the number of steps to show constantly on our micro:bit, so we will now use the forever block. Under the Basic tab, find the block 'show number' block and place that into your forever tab. We want to to show our variable 'step', so go to the variables tab and place the oval 'step' block into the show number block. 
8. One way to ease the transition of numbers (especially on a faster walk) we can choose to show the number all at once instead of having it scroll. So now go to the more (...)  tab, and choose 'stop animation'. 


Experiment:
1. While holding the programmed micro:bit in your hand, walk around the upstairs hallway and return to the library. Write down the number of steps. Reset your micro:bit.
2. Starting from the same spot as your first walk, power walk the same route and end in the same place. Write down the number of steps. 
3. Compare with other students.


### Supplements
**Any items in this section are the property & under the license of their respective owners.**






## REVIEW
The accelerometer that is built into the mirco:bit is one of many capabilities micro:bits have.
## STANDARDS        
| Type | Listing | 
|-----------|-----------|
| CS Domains  | Data Analysis, Algorithms and Programming|
| CS Principles   | Fostering an Inclusive Computing Culture, Creating Computational Artifacts|
| Other Content Standards |   |
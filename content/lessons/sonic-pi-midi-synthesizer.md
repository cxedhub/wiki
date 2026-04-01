---
title: 'Sonic Pi: Midi Synthesizer'
description: Most commercial music produced today involves the use of synthesized
  and sampled sounds. MIDI (musical instrument digital interface) is the standard
  language used for electronic musical instruments and computers to communicate with
  one another. Sonic Pi is capable of producing a wide variety of synthesized sounds
  which can be controlled via MIDI. The goal of this project is to provide students
  the opportunity to create electronic music using Sonic Pi and MIDI keyboards.
date: '2022-04-26 00:00:00+00:00'
draft: false
author: Colin Botts
subjects:
- Computer Science
- Music
grade_levels:
- 3-5
cs_domains:
- Algorithms and Programming
- Impacts of Computing
cs_principles:
- Collaborating Around Computing
- Creating Computational Artifacts
tags:
- computer science
- Music
materials: 'Raspberry Pi, MIDI keyboards or controllers.  Optional: PC''s running
  Sonic Pi instead of Raspberry Pi''s'
---
# OVERVIEW
## Activity Overview:  
Most commercial music produced today involves the use of synthesized and sampled sounds. MIDI (musical instrument digital interface) is the standard language used for electronic musical instruments and computers to communicate with one another. Sonic Pi is capable of producing a wide variety of synthesized sounds which can be controlled via MIDI. The goal of this project is to provide students the opportunity to create electronic music using Sonic Pi and MIDI keyboards.
## Meta description
+ *Subject Area:* Computer Science, Music 
+ *Grade Level :* 3-5 
+ *Computer Science Domains:*
   + Algorithms and Programming, Impacts of Computing
+ *Computer Science Principles:*
   + Collaborating Around Computing, Creating Computational Artifacts
+ *Materials:* 
   + Raspberry Pi, MIDI keyboards or controllers.  Optional: PC's running Sonic Pi instead of Raspberry Pi's
+ *Considerations:*
   + 


# Lesson Plan
## Overview
Most commercial music produced today involves the use of synthesized and sampled sounds. MIDI (musical instrument digital interface) is the standard language used for electronic musical instruments and computers to communicate with one another. Sonic Pi is capable of producing a wide variety of synthesized sounds which can be controlled via MIDI. The goal of this project is to provide students the opportunity to create electronic music using Sonic Pi and MIDI keyboards.
## ASSESSMENT PRE/POST-TEST
What is MIDI?
What is a synthesizer?
Describe how Sonic Pi can be used to create sounds and music?
## OBJECTIVES
Manipulate code within Sonic Pi to create music using variety of synthesized sounds.


## CATCH/HOOK
A brief demonstration of the musical capabilities of Sonic Pi.


## ACTIVITY INSTRUCTIONS
Day 1: Getting started with MIDI and Sonic Pi


Teacher demonstration and introduction of Sonic Pi including a demonstration of some of its capabilities, including live looping and MIDI controlled events.


Discuss what is MIDI (musical instrument digital interface), its history, and some of its applications.


Hand out computers, MIDI keyboards, cables, etc. to students (in pairs)


Have students launch Sonic Pi and open the code template (preinstalled by teacher).  Discuss the code with the class, explaining how it works, and highlight the line of code that they are to alter in order to explore what other sounds can be created.


Display a list of available Sonic Pi synthesizers and give students time to play with Sonic Pi code changing the synth sounds as their parter makes music by playing the MIDI keyboard.


#experiment with [synth :piano] to change to other synthesizer sounds


live_loop :synth do
  use_real_time
  note, velocity = sync '/midi/nanokey2_keyboard/0/1/note_on'
  synth :piano, note: note, amp: velocity/127.0
end




Day 2: Delving deeper into the Sonic Pi Code: synth parameters


Review concepts from previous class and address any issues, questions, or problems that arose 


Demonstrate how Sonic Pi code can further be altered to radically change the sounds of individual synthesizers by accessing their parameters.


Have students get computers and MIDI keyboards and open new Sonic Pi code template.  Walk students through the process of altering synth parameters within the code, explaining and demonstrating what each parameter is and what it does.


Allow students time to explore code template, altering synthesizers and their parameters while creating music using the MIDI keyboards.


# midi controller with randomized filter and panning
# experiment with different ADSR values (attack, decay, sustain, release)
# experimented with cutoff, res, wave, and pan values


live_loop :synth do
  use_real_time
  note, velocity = sync '/midi/nanokey2_keyboard/0/1/note_on'
  synth :prophet, note: note,
    amp: velocity/127.0,
    attack: 0, decay: 0,  sustain: 0,  release: 0.4,
    cutoff: rrand_i(70, 130), res: rrand(0.1, 1), pan: rrand(-1, 1), wave: rrand_i(0,2)
end


### Supplements
**Any items in this section are the property & under the license of their respective owners.**




## REVIEW
Have a few student volunteers show the class what they were able to create and provide an opportunity for students to ask questions and provide feedback.
## STANDARDS        
| Type | Listing | 
|-----------|-----------|
| CS Domains  | Algorithms and Programming, Impacts of Computing|
| CS Principles   | Collaborating Around Computing, Creating Computational Artifacts|
| Other Content Standards | Wyoming Fine & Performing Arts FPA4.1.M.3 FPA 4.1.M.4  |
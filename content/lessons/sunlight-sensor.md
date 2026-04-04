---
title: Sunlight Sensor
description: Turn your micro:bit into a light sensor! Using the light level sensor feature of the micro:bit, students will program the micro:bit to display different images based on the level of light in
  the room.
date: '2022-07-14 00:00:00+00:00'
draft: false
author: Anita Tope
subjects:
- Computer Science
- Science
grade_levels:
- 3-5
cs_domains:
- Computing Systems
- Data Analysis
- Algorithms and Programming
- Impacts of Computing
cs_principles:
- Collaborating Around Computing
materials: Micro:bit
tags:
- Data Collection
- micro:bit
standard_types:
- CSTA
- ISTE
- NGSS
standards:
  CSTA:
  - 1B-AP-08
  - 1B-AP-09
  - 1B-AP-10
  - 1B-AP-15
  - 1B-CS-01
  - 1B-CS-02
  - 1B-CS-03
  - 1B-DA-06
  - 1B-DA-07
  - 1B-IC-18
  - 1B-IC-19
  - 1B-IC-20
  ISTE:
  - ISTE-1d
  - ISTE-7b
  - ISTE-7c
  NGSS:
  - 4-PS3-1
  - 4-PS3-2
  - 4-PS3-4
  - 4-PS4-1
  - 4-PS4-3
  - 5-ESS1-1
  - 5-ESS1-2
---
# OVERVIEW
## Activity Overview:  
Turn your micro:bit into a light sensor! Using the light level sensor feature of the micro:bit, students will program the micro:bit to display different images based on the level of light in the room.
## Meta description
+ *Subject Area:* Computer Science, Science 
+ *Grade Level :* 3-5 
+ *Computer Science Domains:*
   + Computing Systems, Data Analysis, Algorithms and Programming, Impacts of Computing
+ *Computer Science Principles:*
   + Collaborating Around Computing
+ *Materials:* 
   + Micro:bit
+ *Considerations:*
   + Background knowledge from microbit.org https://support.microbit.org/support/solutions/articles/19000024023-how-does-the-light-sensing-feature-on-the-micro-bit-work-


The micro:bit does not have a special light sensor device fitted. However, it can use the LEDs of the matrix display to estimate the amount of ambient light. Using the editors, you can return a light level value (0-255) that you can use in your program.
 
Note that the LED column and row mapping is different on a V2 micro:bit to a V1. 
A V2 micro:bit uses the top row of LEDs for light sensing, whereas on V1 this is spread across the display. In practice, this means that if you cover the top row of LEDs on a V2, the light level will read 0.


This light sensing method uses an LED both as an output device, and an input device. When the output pin of the microprocessor drives a voltage across the LED, the LED lights up. If the micro-controller then sets that drive pin as an input, and times how long it takes for the voltage at the top end of the LED to collapse, that time is roughly proportional to the amount of ambient light. This method should be considered an approximation of the light level and will not be as accurate as using a dedicated light sensor such as an Light Dependent Resistor (LDR).


There is some background into the general technique in these links, which include details on not just how to sense ambient light with LEDs, but how to transfer small amounts of data wirelessly using the same technique.


https://www.sparkfun.com/news/2161


http://www.merl.com/publications/docs/TR2003-35.pdf


http://electronics.stackexchange.com/questions/902/detecting-light-with-an-led


http://www.instructables.com/id/LEDs-as-light-sensors/


https://microbit.org/get-started/user-guide/features-in-depth/#light-sensor


# Lesson Plan
## Overview
Turn your micro:bit into a light sensor! Using the light level sensor feature of the micro:bit, students will program the micro:bit to display different images based on the level of light in the room.
## ASSESSMENT PRE/POST-TEST
How can you program a micro:bit so the LED display becomes a sensor that reacts to light?
## OBJECTIVES
1. Program the micro:bit using an ‘if… else’ statement to show a sun image only if the light level is greater than (>) a certain level.
2.Cover the micro:bit with your hand and the sun icon should vanish.
3. Adjust the programming so it will work depending on the amount of light in the room.


## CATCH/HOOK
Turn the micro:bit LED display into a sensor to make your micro:bit react to light.


## ACTIVITY INSTRUCTIONS
1.  Read aloud Running on Sunshine: How Does Solar Energy Work? by 
Carolyn Cinami DeCristofano (or another book about solar energy)
2.  Discuss how the intensity of the sunlight can potentially affect solar powered devices.
3.  Ask students how they could create a sensor that would show the amount of energy coming from the sun.
4.  Introduce the Sunlight Sensor activity for micro:bit Sunlight Sensor
5.  Students will program the micro:bit to sense the light.
6.  Extension Activities:
Show a different picture, like a moon or star, when it’s dark.
Show an animated sun when light falls on your micro:bit.
Turn this project into a night-light by making it light up the micro:bit’s display when it goes dark.
Choose another activity:  Night Light or   Light Alarm


### Supplements
**Any items in this section are the property & under the license of their respective owners.**






## REVIEW
Share how this could be combined with a solar battery (such as the Snap Circuits Green Energy kit) to track data about the amount of sunlight needed to power different circuits.


Discuss how this type of sensor could impact the future of solar energy.  Would it be useful?  Why or why not?  How could you improve your sensor?
## STANDARDS        
| Type | Listing | 
|-----------|-----------|
| CS Domains  | Computing Systems, Data Analysis, Algorithms and Programming, Impacts of Computing|
| CS Principles   | Collaborating Around Computing|
| Other Content Standards | [4-PS3-2](https://www.nextgenscience.org/search-standards?keys=4-PS3-2).        Make observations to provide evidence that energy can be transferred from place to place by sound, light, heat, and electric currents. [4-PS3-4](https://www.nextgenscience.org/search-standards?keys=4-PS3-4).        Apply scientific ideas to design, test, and refine a device that converts energy from one form to another.  |
ELA
RI.4.1        Refer to details and examples in a text when explaining what the text says explicitly and when drawing inferences from the text.
RI.4.3        Explain events, procedures, ideas, or concepts in a historical, scientific, or technical text, including what happened and why, based on specific information in the text.
RI.4.9        Integrate information from two texts on the same topic in order to write or speak about the subject knowledgeably.
W.4.2        Write informative/explanatory texts to examine a topic and convey ideas and information clearly.
W.4.7        Conduct short research projects that build knowledge through investigation of different aspects of a topic.  |
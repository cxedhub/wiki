---
title: Magic 8 ball
description: Make your own magic 8 ball! Students will code a micro:bit in makecode.org
  to tell other's 'fortunes'.
date: '2022-11-01 00:00:00+00:00'
draft: false
author: Casey Harmon
subjects:
- Computer Science
- Technology
grade_levels:
- 6-8
cs_domains:
- Computing Systems
- Algorithms and Programming
cs_principles:
- Collaborating Around Computing
tags:
- computer science
- Technology
materials: Micro:bit
---
# OVERVIEW
## Activity Overview:  
Make your own magic 8 ball! Students will code a micro:bit in makecode.org to tell other's 'fortunes'.
## Meta description
+ *Subject Area:* Computer Science, Technology 
+ *Grade Level :* 6-8 
+ *Computer Science Domains:*
   + Computing Systems, Algorithms and Programming
+ *Computer Science Principles:*
   + Collaborating Around Computing
+ *Materials:* 
   + Micro:bit
+ *Considerations:*
   + 


# Lesson Plan
## Overview
Make your own magic 8 ball! Students will code a micro:bit in makecode.org to tell other's 'fortunes'.
## ASSESSMENT PRE/POST-TEST
Can programming a micro:bit be fun and entertaining? Can you make more programs like this (e.g. Rock, Paper, Scissors game, multiple choice answerer...)
## OBJECTIVES
Students will make their own Magic 8 ball using a mirco:bit. They will program a mirco:bit to randomly choose an answer when shaken.


## CATCH/HOOK
https://www.youtube.com/watch?v=P18EdAKuC1U


## ACTIVITY INSTRUCTIONS
Coding:
1. Open the website makecode.microbit.org
2. Start a new project and name it 'Magic 8 ball'
3. In this lesson, we will be making our own Magic 8 ball. 
4. Start with an 'on shake' block in the input tab. 
5. In that block, we need to see our variable (which in this case is our answer) . So go to the variables tab and set our variable to 'answer'. Then choose the 'set answer to...' block and place in the 'on shake' block.
6. In order to have  random answer every time we shake, we need to code that. Go to the math tab and choose 'pick random 0 to 10' and replace the 10 with 4, and the 0 with 1. This will give us four different answers depending on the random number picked. If you want more than 4 answers, you can do so later on. 
7. Now we need to show certain answers for each number. From the Logic tab, choose an 'if true then' block. 
8. In this block, we will place our variable (answer) and the number associated with it. From the Logic tab, choose the ' 0 = 0' block from the comparison section. Place this in the 'true' section of the if/then logic block. Put your variable 'answer' into one side of the block and a 1 in the other. 
9. Now to show an answer, go to the LED tab and choose the 'show string' block. Place this in the if/when block. Type any answer, such as 'no' or 'yes' or 'only time will tell'.
10. We need 3 more answers so we are going to duplicate the block set we just made. To do this, right click the if/when block and select duplicate. The same set of blocks appears to the side for us to use. Place this set under our last if/when block set but still in the 'on shake' block.
11. Set each of the remaining numbers 2-4 in the right side of the logic block and change the strings to different answers. 
12. Download the hex file and transfer it to your micro:bit. Then start your fortune telling career!


### Supplements
**Any items in this section are the property & under the license of their respective owners.**






## REVIEW
By determining our variable early on in the lesson, it helps to make the process go more smoothly as if makes more sense. A step by step process like this is easy to follow but by knowing what we are controlling in our coding, we have limitless possibilities later on.
## STANDARDS        
| Type | Listing | 
|-----------|-----------|
| CS Domains  | Computing Systems, Algorithms and Programming|
| CS Principles   | Collaborating Around Computing|
| Other Content Standards |   |
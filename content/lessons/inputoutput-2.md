---
title: Input/Output
description: 'In this lesson students will be translating mathematical functions into
  computer programming functions to solve. This can be used as an introductory lesson
  before teaching equation solving. Note: students will need to have an understanding
  of Javascript.'
date: '2022-10-30 00:00:00+00:00'
draft: false
author: Kristy Barr
subjects:
- Computer Science
- Mathematics
grade_levels:
- 6-8
cs_domains:
- Algorithms and Programming
cs_principles:
- Collaborating Around Computing
- Recognizing and Defining Computational Problems
- Communicating About Computing
materials: Javascript
tags:
- "Code.org"
- "micro:bit"
---
# OVERVIEW
## Activity Overview:  
In this lesson students will be translating mathematical functions into computer programming functions to solve. This can be used as an introductory lesson before teaching equation solving. Note: students will need to have an understanding of Javascript.
## Meta description
+ *Subject Area:* Computer Science, Mathematics 
+ *Grade Level :* 6-8 
+ *Computer Science Domains:*
   + Algorithms and Programming
+ *Computer Science Principles:*
   + Collaborating Around Computing, Recognizing and Defining Computational Problems, Communicating About Computing
+ *Materials:* 
   + Javascript
+ *Considerations:*
   + 


# Lesson Plan
## Overview
In this lesson students will be translating mathematical functions into computer programming functions to solve. This can be used as an introductory lesson before teaching equation solving. Note: students will need to have an understanding of Javascript.
## ASSESSMENT PRE/POST-TEST
List three examples of real world machines that input and output data.
## OBJECTIVES
The students will understand how inputs and outputs relate to mathematical functions.
The students will use the concepts of inputs and outputs to solve one step equations.
The students will apply the concepts of inputs and outputs to real world scenarios.


## CATCH/HOOK
Share the following Youtube video-but stop it at 1:50 (unless you will be introducing microbits to the class.)  http://youtu.be/NkoS2JXaBuM


## ACTIVITY INSTRUCTIONS
After showing the input/output video, discuss examples of input/output devices in the classroom or school.  Next we will be taking a mathematical function and translating it into a function you’d find in computer programming.


Show an example of a one step math equation:


                y = x + 7


Next we will rewrite the equation using the notation of a Javascript function. So, we need to find out some information.
What would be the argument for the function? This is the input.
What would be the output for this function?
What might go inside the brackets of our function?
Answer:
Function addNumbers (x) {
Return  x + 7
}


addNumbers (3)
//result is 10


Explain that this is an example of an algorithm.  This is a simple example that only has one line of instruction, however others can be more complex with hundreds of lines of instructions.
With a partner solve this function:
turnLeft(x);   and x is the number of times that a person turned 90 degrees
How would I write this function so that a person turns all the way around in a circle?
Answer: turnLeft(4);
How would I write this function so that a person turns right instead? 
Extension: Show your answer as a Javascript function.
Answer: turnLeft(3);
turnRight(x){
X * turnLeft(3);
}


Lesson based on Input and Output, Math Activity on Code.org


### Supplements
**Any items in this section are the property & under the license of their respective owners.**




## REVIEW
Exit slip:  Write 2-3 sentences explaining at least 3 things in your life that have an input and output.
## STANDARDS        
| Type | Listing | 
|-----------|-----------|
| CS Domains  | Algorithms and Programming|
| CS Principles   | Collaborating Around Computing, Recognizing and Defining Computational Problems, Communicating About Computing|
| Other Content Standards | AP.V [8.AP.V.01](https://edu.wyoming.gov/educators/standards/computer-science/)  |
---
title: Writing CSV files in Python
description: Students will design a flight path for a programmable drone and collect the data from the drone such as altitude, motor temperature, air pressure, and flight time.  The students will record the data to a file on their computer using python .
date: '2023-04-03'
draft: false
author: John Lupher
subjects:
- Computer Science
grade_levels:
- 9-12
cs_domains:
- Algorithms and Programming
cs_principles:
- Recognizing and Defining Computational Problems
- Creating Computational Artifacts
- Testing and Refining Computational Artifacts
materials: Website, CoDrone Lite Programmable Drones
tags:
- Data Collection
- WySTACK
supplements:
- /uploads/writing-csv-files-in-python/Wystack_asg1_-_John_Lupher.docx
- /uploads/writing-csv-files-in-python/Python_CSV_filewriting_Lupher_-_John_Lupher.docx
- /uploads/writing-csv-files-in-python/Pressure2_-_John_Lupher.pdf
- /uploads/writing-csv-files-in-python/Pressure1_-_John_Lupher.pdf
- /uploads/writing-csv-files-in-python/Temp1_-_John_Lupher.pdf
standards:
  NGSS:
  - HS-PS2-1
  - HS-PS3-1
  Wyoming CS:
  - L1.AP.A.01
  - L1.AP.M.01
  - L1.DA.CVT.01
  - L2.AP.A.03
  - L2.DA.CVT.02
  CSTA:
  - 3A-AP-13
  - 3A-AP-14
  - 3A-AP-15
  ISTE:
  - ISTE-3a
  - ISTE-3b
  - ISTE-5a
  - ISTE-5b
  - ISTE-6a
  - ISTE-6b
standard_types:
- CSTA
- ISTE
- NGSS
- Wyoming CS
---
# OVERVIEW
## Activity Overview:  
Students will design a flight path for a programmable drone and collect the data from the drone such as altitude, motor temperature, air pressure, and flight time.  The students will record the data to a file on their computer using python .
## Meta description
+ *Subject Area:* Computer Science 
+ *Grade Level :* 9-12 
+ *Computer Science Domains:*
   + Algorithms and Programming
+ *Computer Science Principles:*
   + Recognizing and Defining Computational Problems
   + Creating Computational Artifacts
   + Testing and Refining Computational Artifacts
+ *Materials:* 
   + Website, CoDrone Lite Programmable Drones


# Lesson Plan
## Overview
Students will design a flight path for a programmable drone and collect the data from the drone such as altitude, motor temperature, air pressure, and flight time.  The students will record the data to a file on their computer using python .
## ASSESSMENT PRE/POST-TEST
How will you capture flight data from your drone?  How will you record your data so that it can be used for analysis?  What applications can be used to view the data in your file?
## OBJECTIVES
The students will capture data from the drone using the CoDrone library. Students will write the file in CSV format using the CSV library for Python. Students will verify the data was written by opening the resulting file in MS Excel.

## CATCH/HOOK
Capturing data from drones can be fun! In this exercise you will be able to find out whose drone flew the highest, used the most power, and flew for the longest time. You can also choose when and where the data is recorded.

## ACTIVITY INSTRUCTIONS
I.	Introduction (5 minutes)

A.	Explain purpose of lesson: Today we will be learning about writing csv data files in in Python. 

B.	Present learning target and success criteria: The learning target is for students to be able to explain and utilize a file writing techniques in Python. The success criteria is for Students to determine how to write data using the CSV library and determine where the data was written, as well as confirm the format it is written in.

II.	Guided Practice (15 minutes)

A.	Explain the purpose of a CSV file: Comma Separated Values format is the most common import and export format for spreadsheets and databases. You can easily view a CSV file in spreadsheets such as Microsoft Excel.

B.	Explain how to write a CSV file:
•	First, open the CSV file for writing (w mode) by using the open() function.
•	Second, create a CSV writer object by calling the writer() function of the csv module.
•	Third, write data to CSV file by calling the writerow() or writerows() method of the CSV writer object.
•	Finally, close the file once you complete writing data to it.
•	For our example we will use a with statement so that you don’t need to call the close() method.



C.	Demonstrate example: Write CSV files with sample data in Python on the classroom large format monitors.
Imports:
import CoDrone
import csv

Example 1: 

#Writing the headers for the csv:

f = open("drone_data.csv","w")
f.write("Height,Temp\n")
f.close()

# Create a function to collect drone data:

def dr_data():
    temp = drone.get_drone_temp()
    height = drone.get_height()
    print(temp)
    print(height)
    csvwriter.writerow([height,temp])

# Write data to csv file:
with open('drone_data.csv', 'a',newline='') as file:
    csvwriter = csv.writer(file)
    dr_data()
    drone.takeoff()
    drone.hover(1)
    dr_data()
    drone.set_pitch(30)
    drone.move(2)
    dr_data()

D.	Have students work in pairs to complete exercises: Provide students with exercises to complete and have them work in pairs to practice writing data to files on their computer.

### Supplements
**Any items in this section are the property & under the license of their respective owners.**


## REVIEW
A.	Review material: Review the material taught in the lesson. 

B.	Check for understanding: (3-2-1 Google Form) 
1.	Record 3 things you learned during this lesson.
2.	Record two things you found interesting and would like to know more about.
3.	Record 1 question you still have about the material.
## STANDARDS        
| Type | Listing | 
|-----------|-----------|
| CS Domains  | Algorithms and Programming|
| CS Principles   | Recognizing and Defining Computational Problems, Creating Computational Artifacts, Testing and Refining Computational Artifacts|
| Other Content Standards | NGSS:
HS-PS2-1,HS-PS3-1
Wyoming Computer Science Standards:
L1.DA.CVT.01, L2.DA.CVT.02, L1.AP.A.01.C, L2.AP.A.03, L1.AP.M.01  |
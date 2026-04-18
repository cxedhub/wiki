"""micro:bit MicroPython: Greenhouse Monitor
Alert when temperature > 30°C AND light < 50 (door closed, overheating risk).
Combines two sensors with conditional logic.

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
from microbit import *
import music

while True:
    temp = temperature()
    light = display.read_light_level()
    if temp > 30 and light < 50:
        display.show(Image.SAD)
        music.play(["A5:500"])
    else:
        display.show(Image.HAPPY)
    sleep(1000)

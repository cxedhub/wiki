"""micro:bit MicroPython: Temperature + Light
Reads both temperature and light level. Button A shows temp, Button B shows light.

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll("T:" + str(temperature()))
    if button_b.was_pressed():
        display.scroll("L:" + str(display.read_light_level()))
    sleep(100)

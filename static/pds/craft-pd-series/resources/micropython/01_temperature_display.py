"""micro:bit MicroPython: Temperature Display
Reads the onboard temperature sensor and scrolls the value on the LED matrix.
NOTE: Reads CPU temperature, not ambient air (typically 3-8°C higher).

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
from microbit import *

while True:
    temp = temperature()
    display.scroll(str(temp) + "C")
    sleep(2000)

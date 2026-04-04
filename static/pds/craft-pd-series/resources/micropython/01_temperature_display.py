"""micro:bit MicroPython: Temperature Display
Reads the onboard temperature sensor and scrolls the value on the LED matrix.
NOTE: Reads CPU temperature, not ambient air (typically 3-8°C higher).
"""
from microbit import *

while True:
    temp = temperature()
    display.scroll(str(temp) + "C")
    sleep(2000)

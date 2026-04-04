"""micro:bit MicroPython: Temperature + Light
Reads both temperature and light level. Button A shows temp, Button B shows light.
"""
from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll("T:" + str(temperature()))
    if button_b.was_pressed():
        display.scroll("L:" + str(display.read_light_level()))
    sleep(100)

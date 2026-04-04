"""micro:bit MicroPython: Motion + Compass
Shows compass direction only when the device is shaken.
Combines accelerometer gesture detection with compass heading.
"""
from microbit import *

compass.calibrate()
while True:
    if accelerometer.was_gesture("shake"):
        heading = compass.heading()
        if heading < 45 or heading > 315:
            display.show("N")
        elif heading < 135:
            display.show("E")
        elif heading < 225:
            display.show("S")
        else:
            display.show("W")
    else:
        display.show("-")
    sleep(300)

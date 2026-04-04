"""micro:bit MicroPython: Greenhouse Monitor
Alert when temperature > 30°C AND light < 50 (door closed, overheating risk).
Combines two sensors with conditional logic.
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

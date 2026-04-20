"""micro:bit MicroPython: Sensor Node (Multi-Sensor Sender)

Level-up version of Role A. Reads both temperature and light level on
each cycle and broadcasts a single comma-separated payload:

    <SENDER_ID>,<temp_C>,<light_0_255>

Pair with 04_aggregator_threshold.py on the same radio group. Change
SENDER_ID on a second micro:bit (e.g. "2") to build a two-sender mesh.

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
from microbit import *
import radio

RADIO_GROUP = 7
SENDER_ID = "1"

radio.config(group=RADIO_GROUP)
radio.on()

while True:
    temp = temperature()
    light = display.read_light_level()
    payload = "{0},{1},{2}".format(SENDER_ID, temp, light)
    radio.send(payload)
    display.show(SENDER_ID)
    sleep(300)
    display.clear()
    sleep(1700)

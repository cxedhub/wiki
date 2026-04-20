"""micro:bit MicroPython: Aggregator Node (Running Average Receiver)

Role B in the two-node IoT pattern. Listens on a shared radio group for
numeric readings from one or more Sensor Nodes and keeps a running
average over the last WINDOW readings. Displays the current average on
the LED matrix and indicates activity with a brief arrow when a new
reading arrives.

Pair with 01_sensor_node_temp.py (or any sender broadcasting numbers on
the same RADIO_GROUP). Run it in the python.microbit.org simulator today
and flash to a real device when your kit arrives.

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
from microbit import *
import radio

RADIO_GROUP = 7
WINDOW = 10

radio.config(group=RADIO_GROUP)
radio.on()

readings = []

while True:
    msg = radio.receive()
    if msg is not None:
        try:
            value = float(msg)
        except ValueError:
            continue
        readings.append(value)
        if len(readings) > WINDOW:
            readings.pop(0)
        avg = sum(readings) / len(readings)
        display.show(Image.ARROW_S)
        sleep(150)
        display.scroll(str(int(avg)))
    sleep(50)

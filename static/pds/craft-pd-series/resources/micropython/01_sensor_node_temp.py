"""micro:bit MicroPython: Sensor Node (Temperature Sender)

Role A in the two-node IoT pattern. Reads the onboard temperature sensor
and broadcasts it on a shared radio group every 2 seconds. Pair with an
Aggregator Node (02_aggregator_running_avg.py) on the same radio group.

Run it today in the python.microbit.org simulator. Flash it to a real
BBC micro:bit V2 when your kit arrives.

NOTE: On real hardware, temperature() reads the CPU die, not ambient air
(typically 3-8 degrees C higher). In the simulator, the value is idealized
and follows the simulator's temperature slider.

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
from microbit import *
import radio

RADIO_GROUP = 7

radio.config(group=RADIO_GROUP)
radio.on()

while True:
    temp = temperature()
    radio.send(str(temp))
    display.show(Image.ARROW_N)
    sleep(200)
    display.clear()
    sleep(1800)

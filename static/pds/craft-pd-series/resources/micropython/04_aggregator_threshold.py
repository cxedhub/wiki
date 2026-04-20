"""micro:bit MicroPython: Aggregator Node (Threshold Alert Display)

Level-up version of Role B. Listens for comma-separated payloads from
multi-sensor senders:

    <SENDER_ID>,<temp_C>,<light_0_255>

Tracks the latest reading per sender and displays an alert icon if any
sender reports temperature > TEMP_MAX (overheating greenhouse) AND light
< LIGHT_MIN (door closed). Otherwise scrolls the current maximum
temperature across the LED matrix.

Pair with one or more copies of 03_sensor_node_multi.py on the same
RADIO_GROUP (with distinct SENDER_IDs).

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
from microbit import *
import radio

RADIO_GROUP = 7
TEMP_MAX = 30
LIGHT_MIN = 50

radio.config(group=RADIO_GROUP)
radio.on()

latest = {}  # sender_id -> (temp, light)

while True:
    msg = radio.receive()
    if msg is not None:
        parts = msg.split(",")
        if len(parts) == 3:
            sender_id = parts[0]
            try:
                temp = int(parts[1])
                light = int(parts[2])
            except ValueError:
                continue
            latest[sender_id] = (temp, light)

    if latest:
        alert = any(t > TEMP_MAX and l < LIGHT_MIN for t, l in latest.values())
        if alert:
            display.show(Image.SAD)
        else:
            max_temp = max(t for t, _ in latest.values())
            display.scroll(str(max_temp))

    sleep(100)

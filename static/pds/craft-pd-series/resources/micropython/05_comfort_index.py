"""micro:bit MicroPython: Classroom Comfort Index (V2 only)
Scores 0-9 based on temperature, light, and sound.
Requires micro:bit V2 for microphone access.
"""
from microbit import *

def comfort_score():
    score = 0
    # Temperature: ideal 20-25°C
    t = temperature()
    if 20 <= t <= 25:
        score += 3
    elif 18 <= t <= 28:
        score += 2

    # Light: ideal 100-200
    light = display.read_light_level()
    if 100 <= light <= 200:
        score += 3
    elif 50 <= light <= 250:
        score += 2

    # Sound: ideal below 80 (V2 only)
    sound = microphone.sound_level()
    if sound < 80:
        score += 3
    elif sound < 150:
        score += 2

    return score

while True:
    s = comfort_score()
    display.show(str(s))
    sleep(2000)

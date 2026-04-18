"""Snippet 1: Projectile Range Calculator
BUG: Missing degree-to-radian conversion in math.sin()

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
import math

def projectile_range(velocity, angle):
    """Calculate the range of a projectile.
    velocity: initial velocity in m/s
    angle: launch angle in degrees
    Returns: range in meters
    """
    g = 9.81
    range_m = (velocity ** 2 * math.sin(2 * angle)) / g
    return round(range_m, 2)

# Test: 20 m/s at 45 degrees should give ~40.77 m
print(projectile_range(20, 45))

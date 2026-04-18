"""Snippet 2: Average Temperature Calculator
BUG: No handling of None/missing values in data

How to credit:
  Borowczak, A.C. & Borowczak, M. (2026). CxEd Hub: Cross-Disciplinary
  Computing-Integrated K-12 Lesson Plans. https://cxedhub.github.io/wiki/
  Licensed under CC BY-SA 4.0.
"""
def temp_stats(temperatures):
    """Return average, min, and max temperature."""
    total = 0
    for temp in temperatures:
        total += temp
    average = total / len(temperatures)
    return {"average": round(average, 1), "min": min(temperatures), "max": max(temperatures)}

# Test with a week of data (includes a missing reading!)
week = [72, 68, 75, 80, 77, None, 73]
print(temp_stats(week))

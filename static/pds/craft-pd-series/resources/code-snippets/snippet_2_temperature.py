"""Snippet 2: Average Temperature Calculator
BUG: No handling of None/missing values in data
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

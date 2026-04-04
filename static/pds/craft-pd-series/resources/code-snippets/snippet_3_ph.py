"""Snippet 3: pH Classification
BUGS: (1) No input validation for invalid pH values
      (2) Using == 7 for "neutral" is scientifically misleading
"""
def classify_ph(ph):
    """Classify pH as acidic, neutral, or basic."""
    if ph < 7:
        return "acidic"
    if ph == 7:
        return "neutral"
    if ph > 7:
        return "basic"

# Tests
print(classify_ph(6.8))   # acidic
print(classify_ph(7.0))   # neutral
print(classify_ph(7.2))   # basic
print(classify_ph(-1))    # acidic?? (invalid!)
print(classify_ph(15))    # basic?? (invalid!)

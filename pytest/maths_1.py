def add(a, b):
    """Add two numbers, raises error if inputs are invalid."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a + b

def subtract(a, b):
    """Subtract b from a, raises error if inputs are invalid."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a - b
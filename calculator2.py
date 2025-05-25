def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def divide(a, b):
    """Return the division of a by b. Handles division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

import pytest
from calculator_cli import add, subtract, multiply, divide

# --- 1. ADDITION ---
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),              # Standard
    (-1, -1, -2),           # Negatives
    (0, 0, 0),              # Zeros
    (1.5, 2.5, 4.0),        # Floats
    (1000000, 1000000, 2000000), # Large numbers
    (-5, 5, 0),             # Additive inverse
])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)

# --- 2. SUBTRACTION ---
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),             # Standard
    (5, 10, -5),            # Result negative
    (-5, -5, 0),            # Double negative
    (5.5, 2.5, 3),          # Floats
    (0, 5, -5),             # Subtract from zero
    (100, 0, 100),          # Subtract zero
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)

# --- 3. MULTIPLICATION ---
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),             # Standard
    (-3, 4, -12),           # Negative result
    (10, 0, 0),             # Multiply by zero (right)
    (0, 10, 0),             # Multiply by zero (left)
    (0.5, 2, 1.0),          # Floats
    (5, 1, 5),              # Identity (multiply by 1)
    (-5, -5, 25),           # Negative * Negative
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)

# --- 4. DIVISION ---
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),             # Standard
    (1, 4, 0.25),           # Decimal result
    (-10, 2, -5),           # Negative result
    (0, 10, 0),             # Divide zero by number
    (5, 1, 5),              # Divide by 1
])
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
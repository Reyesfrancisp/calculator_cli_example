import pytest
from Calculator import add, subtract, multiply, divide

# --- 1. ADDITION ---
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),          
    (-1, -1, -2),       
    (0, 0, 0),          
    (1.5, 2.5, 4.0),    
])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)

# --- 2. SUBTRACTION ---
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),         
    (5, 10, -5),        
    (-5, -5, 0),        
    (5.5, 2.5, 3),    
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)

# --- 3. MULTIPLICATION ---
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),         
    (-3, 4, -12),       
    (10, 0, 0),        
    (0.5, 2, 1.0)       
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)

# --- 4. DIVISION ---
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),        
    (1, 4, 0.25),      
    (-10, 2, -5),       
])
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
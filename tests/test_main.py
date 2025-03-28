
# test_main.py
import pytest
from main import Calculator

def test_add():
    calculator = Calculator()
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 10) == 0

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(0, 5) == 5

def test_divide():
    calculator = Calculator()
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(9, 3) == 3.0
    
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)

import pytest
from main import Calculator

# Фікстура для створення об'єкта Calculator
@pytest.fixture(scope="module")
def calculator():
    return Calculator()

@pytest.mark.usefixtures("calculator")
class TestCalculator:
    
    # Параметризація для тесту додавання
    @pytest.mark.parametrize(
        "a, b, expected", 
        [(2, 3, 5), (-1, 1, 0), (0, 0, 0)]
    )
    def test_add(self, calculator, a, b, expected):
        assert calculator.add(a, b) == expected

    # Параметризація для тесту віднімання
    @pytest.mark.parametrize(
        "a, b, expected", 
        [(5, 3, 2), (10, 10, 0)]
    )
    def test_subtract(self, calculator, a, b, expected):
        assert calculator.subtract(a, b) == expected

    # Параметризація для тесту множення
    @pytest.mark.parametrize(
        "a, b, expected", 
        [(3, 4, 12), (0, 5, 0)]
    )
    def test_multiply(self, calculator, a, b, expected):
        assert calculator.multiply(a, b) == expected

    # Параметризація для тесту ділення
    @pytest.mark.parametrize(
        "a, b, expected", 
        [(10, 2, 5.0), (9, 3, 3.0)]
    )
    def test_divide(self, calculator, a, b, expected):
        assert calculator.divide(a, b) == expected

    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(5, 0)  # Це викликає помилку при діленні на нуль


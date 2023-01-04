import pytest

from calculator.calculator_class import Calculator


class TestCalculator:

    def test_add(self, calc):
        """
        GIVEN a Calculator with the values 9 and 3
        WHEN the add function is called
        THEN the result is 12
        """
        result = calc.add()
        assert result == 12

    def test_subtract(self, calc):
        """
        GIVEN a Calculator with the values 9 and 3
        WHEN the subtract function is called
        THEN the result is 6
        """
        result = calc.subtract()
        assert result == 6

    def test_multiply(self, calc):
        """
        GIVEN a Calculator with the values 9 and 3
        WHEN the multiply function is called
        THEN the result is 27
        """
        result = calc.multiply()
        assert result == 27

    def test_divide(self, calc):
        """
        GIVEN a Calculator with the values 9 and 3
        WHEN the divide function is called
        THEN the result is 3
        """
        result = calc.divide()
        assert result == 3

    def test_divide_by_zero_returns_error(self):
        """
        GIVEN a Calculator with the values 3 and 0
        WHEN the divide function is called
        THEN the result is a zero division error
        """
        with pytest.raises(ZeroDivisionError):
            c = Calculator(3, 0)
            c.divide()

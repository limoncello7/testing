"""
Unit tests for the calculator functions
"""
import pytest

import calculator.calculator_functions as cf


def test_addition():
    """
    GIVEN the values 2 and 2
    WHEN the calculator_functions.add function is called
    THEN the result is 4
    """
    assert cf.add(2, 2) == 4


def test_subtraction():
    """
    GIVEN the values 4 and 2
    WHEN the calculator_functions.subtract function is called
    THEN the result of subtracting the second value from the first is 2
    """
    assert cf.subtract(4, 2) == 2


def test_multiplication():
    """
        GIVEN the values 2 and 2
        WHEN the calculator_functions.multiply function is called
        THEN the result is 4
    """
    assert cf.multiply(2, 2) == 4


def test_division():
    """
    GIVEN the values 6 and 2
    WHEN the calculator_functions.divide function is called
    THEN the result is 3
    """
    assert cf.divide(6, 2) == 3


def test_divide_by_zero_returns_value_error():
    """
    GIVEN the values 6 and 0
    WHEN the calculator_functions.divide function is called
    THEN a zero division error is raised
    """
    with pytest.raises(ZeroDivisionError):
        cf.divide(3, 0)

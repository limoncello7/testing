import pytest

from calculator.calculator_class import Calculator


@pytest.fixture(scope='class')
def calc():
    """Returns a calculator with two integers"""
    yield Calculator(9, 3)

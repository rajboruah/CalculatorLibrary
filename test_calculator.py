"""
Unit tests for calculator library

"""


import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multilication(self):
        assert 6 == calculator.multiplication(2, 3)

"""Tests for calculator - run on remote Jenkins agents across architectures."""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from calculator import add, subtract, multiply, divide, power, modulo


class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-2, -3) == -5

    def test_add_zero(self):
        assert add(0, 5) == 5

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(10, 3) == 7

    def test_subtract_negative(self):
        assert subtract(-5, -3) == -2

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(4, 3) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative(self):
        assert multiply(-2, 3) == -6

    def test_multiply_floats(self):
        assert multiply(2.5, 4.0) == 10.0


class TestDivide:
    def test_divide_positive(self):
        assert divide(10, 2) == 5.0

    def test_divide_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Division by zero"):
            divide(10, 0)

    def test_divide_negative(self):
        assert divide(-10, 2) == -5.0


class TestPower:
    def test_power_basic(self):
        assert power(2, 3) == 8

    def test_power_zero_exp(self):
        assert power(5, 0) == 1

    def test_power_one(self):
        assert power(7, 1) == 7


class TestModulo:
    def test_modulo_basic(self):
        assert modulo(10, 3) == 1

    def test_modulo_zero_result(self):
        assert modulo(9, 3) == 0

    def test_modulo_by_zero_raises(self):
        with pytest.raises(ValueError, match="Modulo by zero"):
            modulo(5, 0)

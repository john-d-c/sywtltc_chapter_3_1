""" Tests calculator.py """

import calculator

def test_calculator_add():
    """ Tests the calculator_add function """
    assert calculator.calculator_add(4, 4) == 8
    assert calculator.calculator_add(0, 0) == 0
    assert calculator.calculator_add(0, 1) == 1
    assert calculator.calculator_add(0, -5) == -5

def test_calculator_subtract():
    """ Tests the calculator_subtract function """
    assert calculator.calculator_subtract(4, 4) == 0
    assert calculator.calculator_subtract(0, 0) == 0
    assert calculator.calculator_subtract(0, 1) == -1
    assert calculator.calculator_subtract(0, -5) == 5

def test_calculator_multiply():
    """ Tests the calculator_multiply fuction """
    assert calculator.calculator_multiply(4, 4) == 16
    assert calculator.calculator_multiply(0, 0) == 0
    assert calculator.calculator_multiply(0, 1) == 0
    assert calculator.calculator_multiply(0, -5) == 0

def test_calculator_divide():
    """ Tests the calculator_divide function """
    assert calculator.calculator_divide(4, 4) == 1
    assert calculator.calculator_divide(16, 8) == 2
    assert calculator.calculator_divide(1, 1) == 1
    assert calculator.calculator_divide(15, -5) == -3

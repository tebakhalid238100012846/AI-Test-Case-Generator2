# This file will contain the generated tests.
from target_code import add, subtract, multiply, divide, is_even, factorial
import pytest

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(10,5) == 5

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(0,5) == 0

def test_divide():
    assert divide(6,3) == 2
    assert divide(5,2) == 2.5

def test_is_even():
    assert is_even(100) == True
    assert is_even(101) == False

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add (1,2) == 3
    assert add (5,5) == 10
    assert add (-1,1) == 0
    assert add (-1,-1) == -2
    assert add (0,0) == 0

def test_substract():
    assert subtract (10, 5) == 5
    assert subtract (10, 12) == -2
    assert subtract (-6, -12) == 6
    assert subtract (10, -13) == 23
    assert subtract (5, 5) == 0

def test_multiply():
    assert multiply (10, 5) == 50
    assert multiply (10, 12) == 120
    assert multiply (-6, -12) == 72
    assert multiply (10, -13) == -130
    assert multiply (5, 5) == 25
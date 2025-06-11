import pytest
from Class2_practice import *

def test_positivenumbers():
    obj = Calculator2(12,15)
    assert obj.mul() == 180, "Multiplication is not as expected"
    assert obj.add() == 27, "Addition is not as expected"
    assert obj.div() == 0.8, "Division is not as expected"

def test_negativenumbers():
    obj = Calculator2(-2,15)
    assert obj.mul() == -30, "Multiplication is not as expected"
    assert obj.add() == 13, "Addition is not as expected"
    assert obj.div() == -0.13333333333333333, "Division is not as expected"

def test_withZero():
    obj = Calculator2(15,0)
    assert obj.mul() == 0, "Multiplication is not as expected"
    assert obj.add() == 15, "Addition is not as expected"
    assert obj.div() == "Please enter a valid integer", "Division is not as expected"


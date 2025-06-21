# from  Revision_python_pytest import PalendromeStr, ReverseStr, Revision
import pytest

from  Revision_python_pytest import *


@pytest.mark.tc_multiply
@pytest.mark.calc
@pytest.mark.regression
@pytest.mark.smoke

def test_Multipication():
    calObj = Calculator()
    assert calObj.multiply(5, 10) == 50
    assert calObj.multiply(-5, 10) == -50
    assert calObj.multiply(-5, -5) == 25

@pytest.mark.tc_001
@pytest.mark.calc
@pytest.mark.regression
@pytest.mark.sanity
def test_add():
    callObj = Calculator()
    assert callObj.add(5,10) == 15
    assert callObj.add(-5, 10) == 5
    assert callObj.add(15, 20) == 35

def test_revstr():
    revobj = ReverseStr()
    assert  revobj.reverse_str("India") == "aidnI"
    assert  revobj.reverse_str("New India") == "aidnI weN"


def test_palendrome():
    palenObj = PalendromeStr()
    assert palenObj.ispalendrome("MalayalaM")  == True
    assert palenObj.ispalendrome("Malayalam")  == False






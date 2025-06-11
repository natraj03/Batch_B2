from stringPrrogram_practice import reverse_str, palendrome
import pytest


inputStr = ""
def setup_function():
    print("this is setup_function ")

    global inputStr
    inputStr = "python"

def teardown_function():
    print("this is teardown function")
    global inputStr
    inputStr = None


def test_rev():
    print("test_rev called")
    global inputStr
    assert reverse_str(inputStr) == "nohtyp"
    inputStr = "malayalam"
    assert reverse_str(inputStr) == "malayalam"



def test_palendrome():
    print("test_palendrome input",inputStr)
    assert palendrome(inputStr) == False

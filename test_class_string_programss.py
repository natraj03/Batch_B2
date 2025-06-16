from class_string_programss import ReverseString, Palendrome

def test_Positive1():
    revObj = ReverseString()
    palenObj = Palendrome()

    inpstr1 = "MalayalaM"
    revStrr = revObj.revsStr(inpstr1)
    isPalendrome = palenObj.isPalendrome(inpstr1,revStrr)

    assert inpstr1 == revStrr
    assert  isPalendrome == True

    inpstr2 = "DAD"
    revStrr2 = revObj.revsStr(inpstr2)
    isPalendrome2 = palenObj.isPalendrome(inpstr2, revStrr2)

    assert inpstr2 == revStrr2
    assert isPalendrome2 == True

    inpstr3 = "MOM"
    revStrr3 = revObj.revsStr(inpstr3)
    isPalendrome3 = palenObj.isPalendrome(inpstr3, revStrr3)

    assert inpstr3 == revStrr3
    assert isPalendrome3 == True




def test_Positive2():
    revObj = ReverseString()
    palenObj = Palendrome()

    inpstr1 = "123454321"
    revStrr = revObj.revsStr(inpstr1)
    isPalendrome = palenObj.isPalendrome(inpstr1,revStrr)

    assert inpstr1 == revStrr
    assert  isPalendrome == True

def test_Negative():
    revObj = ReverseString()
    palenObj = Palendrome()

    inpstr1 = "122345"
    revStrr = revObj.revsStr(inpstr1)
    isPalendrome = palenObj.isPalendrome(inpstr1,revStrr)

    assert inpstr1 != revStrr
    assert  isPalendrome == False
class ReverseString:

    def revsStr(self,input_str):
        resultstr = ""
        for char in input_str:
            resultstr = char + resultstr
        return resultstr


class Palendrome:

    def isPalendrome(self,inputStr,revStr):
        if inputStr == revStr:
            return True
        else:
            return  False


# def isPalendrome(inputStr,revStr):
#     if inputStr == revStr:
#         return True
#     else:
#         return  False
#
# temvar = "998991"
#
#
# temresutl = isPalendrome(temvar,"989898")

# revobj = ReverseString()
# palenObj = Palendrome()
#
# revStr = revobj.revsStr(temvar)
# ispanedrome = palenObj.isPalendrome(temvar, revStr)
#
# print("Reverrse of the string = ",revStr )
# print(temvar, " is palendrome = ",ispanedrome )
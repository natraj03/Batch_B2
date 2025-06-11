# Problem statement : count all the characters in a given string
# inputstr = "Welcome to python"
# output : w= 1 e = 2, o = 3
#  imout st = "welcome to india"
# output = w= 1 e = 2, o = 2 , i=2

inputStr = "Welcome to python eee"

outDict = {}
for char in inputStr:
    if char in outDict:
        tempVal = outDict[char]
        outDict[char] = tempVal + 1
    else:
        outDict[char] = 1

for key, val in outDict.items():
    print(key, val)

# Problem statement : count all the repeated characters in a given string
# inputstr = "Welcome to python"
# output :  e = 2, o = 3
#  imout st = "welcome to india"
# output = e = 2, o = 2 , i=2

print("========Print only repeated characters=======")
outDict = {}
for char in inputStr:
    if char in outDict:
        tempVal = outDict[char]
        outDict[char] = tempVal + 1
    else:
        outDict[char] = 1

for key, val in outDict.items():
    if val > 1:
        print(key, val)


#  check if a given string is a palendrome or not
# input = "1221"
# output = "1221" is palendrome
# input = "1231"
# output  = "1321" not a palendrome
# input = "malayalam"
# output = "malayalam" is a palendrome
# input = "india"
# output = "aidni" not a palendrome
#  "input" is equalt to "reverse of input" is palendrome

# inpStr = "1221"




def palenFunction():
    inputDict = {
        "k1": "1221",
        "k2": "332233",
        "k3": "malayalam",
        "k4": "abcdcba",
        "k5": "random"
    }
    for key1 , inpStr in inputDict.items():

        revInput = ""
        for char in inpStr:
            revInput = char + revInput

        if inpStr == revInput:
            print(inpStr, " = given steing is palendrome")
        else:
            print(inpStr, " = given steing is not palendrome")


palenFunction()

def palenfunction2():
    inputDict = {
        "1221": "",
        "3322331": "",
        "malayalam": "",
        "abcdcba": "",
        "random": ""
    }

    for keystr , _ in inputDict.items():
        revInput = ""
        for char in keystr:
            revInput = char + revInput

        if keystr == revInput:
            inputDict[keystr] = "**Palendrome**"
        else:
            inputDict[keystr] = "**Not Palendrome**"
    print("palendrome Dict", inputDict)


palenfunction2()
# def palenFunctionList():
#     inputlist = ["1221", "332233", "malayalam", "abcdcba","random" ]
#
#     for inpStr in inputlist:
#         revInput = ""
#         for char in inpStr:
#             revInput = char + revInput
#
#         if inpStr == revInput:
#             print(inpStr, " = given steing is palendrome")
#         else:
#             print(inpStr, " = given steing is not palendrome")
#
# palenFunctionList()
#
#

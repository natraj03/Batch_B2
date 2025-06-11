#
# # 1 reverse of a stirng
#
# testStr = "india"
# outStr2 = ""
# for index in range(len(testStr)):
#     tempStr = testStr[index]
#     outStr2 =  tempStr + outStr2
# print("reverse of str method 2: ",outStr2)
#
#
# testStr = "Csk"
# outStr2 = ""
# for index in range(len(testStr)):
#     tempStr = testStr[index]
#     outStr2 =  tempStr + outStr2
# print("reverse of str method 2: ",outStr2)
#
#
# testStr = "RCB"
# outStr2 = ""
# for index in range(len(testStr)):
#     tempStr = testStr[index]
#     outStr2 =  tempStr + outStr2
# print("reverse of str method 2: ",outStr2)


def reversestr(testStr):
    outStr2 = ""
    for index in range(len(testStr)):
        tempStr = testStr[index]
        outStr2 = tempStr + outStr2
    return outStr2

# reversestr("CSK")
# reversestr("India")
# reversestr("KKR")
# reversestr("RCB")
# reversestr("GT")

#
# revstr2 = reversestr("988922")
# print("revstr2",revstr2)

# inputstr = "9889"
# revstr = reversestr(inputstr)
#
# # if revstr == inputstr:
# #     print(inputstr , " ****is palendrome")
# # else:
# #     print(inputstr, " ****Not is palendrome")

def check_palendrome(inp1):
    revstr = reversestr(inp1)
    if revstr == inp1:
        print(inp1 , " ****is palendrome")
    else:
        print(inp1, " ****Not is palendrome")


revstr = reversestr("india")
print("revstr",revstr)
check_palendrome("9887889")
check_palendrome("988889")
check_palendrome("9888888891")
out1 = reversestr("asdasfasdfsa111111")
print(out1)


testStr = "Welcome"
#
# print("input String=",testStr)
#
# # print all characters of string individually
# #  Welcome : output = W \n e \n l \n c \n
#
print(testStr[0])
print(testStr[1])
print(testStr[2])
print(testStr[3])
#
# # reverse a string
# # welcome : output = emoclew
#
reverse_str = testStr[6] + testStr[5] + testStr[4] + testStr[3] + testStr[2] + testStr[1] + testStr[0]
#
print("Reverse of a string", reverse_str)
#
# # reverse a string using a for loop Solution 1
#
outStr = ""
for index in range(len(testStr) -1,-1,-1):
    print(testStr[index])
    outStr += testStr[index]
print("reverse of str Method 1",outStr)


outStr2 = ""
for index in range(len(testStr)):
    print(testStr[index])
    tempStr = testStr[index]
    outStr2 =  tempStr + outStr2
print("reverse of str method 2: ",outStr2)

outStr3 = ""
for charac in testStr:
    outStr3 =  charac + outStr3
print("reverse of str method 3: ",outStr3)



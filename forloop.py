#  need of for loop
print("1")
print("2")
print("3")
print("4")
print("10")

print("-----Using for loop---------")
# basic range
print("-----Basic Range Loop---------")
#  range(start, end, stepper)
for index in range(10):
    print(index + 1)


# basic range with start
print("-----Basic Range loop with start---------")
for index in range(5,11):
    print(index)


# basic range with start and stepper
print("-----Basic Range loop with start---------")
for index in range(1,20,3):
    print(index)

# basic with object / length of string
print("-----with object / length of string---------")
inpStr = "welcome"
for index in range(0,len(inpStr)):
    print(inpStr[index])

for index in range(10,0,-1):
    print(index)

for chare in inpStr:
    print(chare)
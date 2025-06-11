
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7

mylist2 = [a1,a2,a3,a4,a5,a6,a7]
mylist = [1,2,1,4,5,4,10]

total = mylist[6] + mylist[5] + mylist[4] + mylist[3] + mylist[2] + mylist[1] + mylist[0]
print(total)
#  add all the integers in side of a list

total = 0
for item in mylist:
    total =  item + total
print("Total= ",total)

# prnint the biggest number in the List

biggest_number = 5
for item in mylist:
    if biggest_number < item:
        biggest_number = item
print("Biggest number",biggest_number)

# find smallest number in the list
smallest_number = mylist[0]
for item in mylist:
    if smallest_number > item:
        smallest_number = item
print("smallest number",smallest_number)



# reverse of a list

reverseList = []
for item in mylist:
    reverseList.insert(0,item)

print("reverseList",reverseList)

# remove duplicates values form list
outputList = []
for item in mylist:
    if item not in outputList:
        outputList.append(item)

print("unique values of list",outputList)

# odd eve number seperate form list
oddList = []
evenList = []
for item in mylist:
    if item % 2 != 0:
        oddList.append(item)
    elif item % 2 == 0:
        evenList.append(item)
print("oddlist",oddList)
print("evenlist",evenList)

# remove the given item form list
removeint = 1
mylist.remove(removeint)
print(f"list after removing{removeint} =",mylist)

# removing item from the list even if it is repeted
int_to_remove = 1
removedList = []
for item in mylist:
    if int_to_remove != item:
        removedList.append(item)

print("lisst after removal",removedList)

# remove item at index
# print("list",mylist)
indexval = 3
deletedVal = mylist.pop(indexval)

print("mylist after using pop",mylist)
print("deletedVal",deletedVal)

indexval = 3
del mylist[indexval]

print("list after using del", mylist)

mylist.insert(3,100)
print("list afterr inserting 100 at index 3",mylist)

# remove duplicates form list
myduplicate = [5,2,3,4,5,6,1,22,3,7,8,88,22]
outputList = []
for item in myduplicate:
    if item not in outputList:
        outputList.append(item)

print(outputList)



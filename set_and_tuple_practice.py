
#  set does not allow duplicates
#  list1 = [], mutable, duplictes, indexing, order
#  set = {}, Mutable, no duplicates, no indexing , no order
#  tuple = (), not mutable, duplicates, indexing, order

myduplicate = [5,2,3,4,5,6,1,22,3,7,8,88,22]

myset = set(myduplicate)



print("list=",myduplicate)
print("set=",myset)
myset.add(100)
myset.add(200)
myduplicate.append(100)
myduplicate.append(200)
myset.add(21)

print("After adding values in set",myset)
print("After adding values in list",myduplicate)
print("accesing values in list",myduplicate[5])
#
# print("accesing  values in set",myset[1])
#
for item in myset:
    print("set item",item)
#
#
mytuple = tuple(myduplicate)
#
print("item at intdex 5 for tuple",mytuple[5])

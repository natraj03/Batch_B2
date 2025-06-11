# simple function
def myfucn():
    print("=====myfucn =====")
    print(4*5)
    print(4 + 5)

myfucn()

# function with argument

def myfunc_with_Arg(a1,a2):
    print("=====myfunc_with_Arg =====")
    print(a1 * a2)
    print(a1 + a2)

myfunc_with_Arg(4,5)
myfunc_with_Arg(6,3)
myfunc_with_Arg(5,9)

#  function with return
def myfunc_with_return():
    print("=====myfunc_with_return =====")
    return 5 * 4
myvar = myfunc_with_return()

print("myvar",myvar)

#  function with argument and return
def myfunc_with_arg_return(a1, a2):
    print("=====myfunc_with_arg_return =====")
    return a1 * a2

myvar2 = myfunc_with_arg_return(5,4)
print("myvar",myvar2)

myvar3 = myfunc_with_arg_return(6,9)
print("myvar3",myvar3)

myvar4 = myfunc_with_arg_return(15,14)
print("myvar4",myvar4)

#  function with n number of arguments
def n_argument(*arg1):
    print("arg1",arg1)
    print("arg1", arg1[0])
    print("item at position 8", arg1[8])

n_argument(1,2,3,4,5,6,78,"asdfa d ","abc")

# calling function with argument in different types

def myfunct_123(name,age,city):
    print("name",name)
    print("age", age)
    print("city", city)

myfunct_123("Litu",22,"BLR")
myfunct_123("BLR",22,"Litu")
# we can change teh order of the arguments if we mention the variable/keyword of the argument
myfunct_123(city="BLR",name="Litu",age=22)
# function with optional
def opt_func(name, country="India", city="BLR"):
    print("name=",name)
    print("country=", country)
    print("city=", city)

opt_func("Rashmi Ranjan")
opt_func("Rashmi Ranjan****","US","Newyork")

# call by value Ex: int, string, tuple

myint = 55
print("before calling function",myint)

def add_random(inp1):
    inp1 = inp1 + 10
    print("inside function inp1",inp1)

add_random(myint)

print("after calling function",myint)

# call by reference Ex: list, set, dictionary

mylist = [123,543]
print("before calling function",mylist)

def some_random(inp1):
    print("inside function inp1",inp1)
    inp1.append("in side fun")
    inp1.append("test reference")
    print("inside function after change inp1",inp1)


some_random(mylist)

print("after calling function",mylist)


print("-----------------------------------------")
# adding list of integers
# myinplist = [1,5,2,"tesst",3,4,1]
myinplist = [1,5,2,"tesst",3,4,1,[1,3,4,5,6]]


def add_list_of_numbers(arg1):
    result = 0
    for item in arg1:
        if type(item) == int:
            result = result + item
        elif type(item) == list:
            result = result + addlist(arg1)
    print("result = ", result)

def addlist(list1):
    result = 0
    for item in list1:
        if type(item) == int:
            result = result + item

    return result

add_list_of_numbers(myinplist)

addlist([1,3,4,5])



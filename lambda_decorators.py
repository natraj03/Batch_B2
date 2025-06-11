
def multiply_fun(inp1,inp2,inp3):
    return inp1 * inp2 * inp3

returnvar = multiply_fun(5,7,2)
# print("returnvar",returnvar)



#  lambda syntax: lambda  arguments: expression
# function without name
# anonumus function

ressult1 = lambda inp1, inp2, inp3: inp1 * inp2 * inp3
# print("ressult1",ressult1(5,6,2))


# using lambda in for myltiplying list of objects by itself
list_numbnerr = [2,4,5,6,8]
# print("map",list(map(lambda arg1: arg1 * 2, [10,2])))
rresultList = list(map(lambda arg1: arg1 * 2, list_numbnerr))
# print("rresultList",rresultList)


# -------------- Decorator ----------------------


def validIntonly(func):
    def mywrapper(arg1,arg2):
        if type(arg1) == int and type(arg2) == int:
            print("This is before execution of original function ")
            if arg1 < arg2:
                func(arg2, arg1)
            else:
                func(arg1, arg2)
            print("This is after execution of original function ")
        else:
            print("Plesae enter a valid int only")
    return mywrapper



inp1 = 50
inp2 = 5

@validIntonly
def mult(a1,a2):
    print("mul:",  a1 * a2)


@validIntonly
def add(a1, a2):
    print("add:",  a1 + a2)


@validIntonly
def sub(a1,a2):
    print("sub:", a1 - a2)

@validIntonly
def dev(a1,a2):
    print("div:", a1 / a2)



mult(inp1,inp2)
add(inp1,inp2)
sub(inp1,inp2)
dev(inp1,inp2)



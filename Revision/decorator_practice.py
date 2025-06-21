def int_input_only(myfunc):

    def mywrapper(arg1,arg2):
        if type(arg1) == int and type(arg2) == int:
            return myfunc(arg1,arg2)
        else:
            print("only int Type is accepted")
    return mywrapper


@int_input_only
def multiply(inp1, inp2):
    return inp1 * inp2

@int_input_only
def add(inp1, inp2):
    return inp1 + inp2

@int_input_only
def sub(inp1, inp2):
    return inp1 - inp2



print(multiply(4,5))
print(multiply("asb","abc"))



default_var = 10

def multFun():
    inp1 = 5
    inp2 = 2
    global default_var
    print(inp1 * inp2 + default_var)
    inp2 = 4
    default_var = 10
    print(inp1 * inp2 + default_var)


multFun()





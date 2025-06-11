# inp1 = 5
# inp2 = 10
#
# def mul():
#     return inp1 * inp2
#
#
# def add():
#     return inp1 + inp2
#
# print(mul())
# print(add())


class Calculator2:
    inp1 = 10
    inp2 = 5
    def __init__(self,arg1,arg2):
        print("Constrructor called",arg1,arg2)
        self.inp1 = arg1
        self.inp2 = arg2
#
    def mul(self):
        self.inp1 = 20
        return  self.inp1 * self.inp2

    def add(self):
        return self.inp1 + self.inp2

    def div(self):
        if self.inp2 != 0:
            return self.inp1 / self.inp2
        else:
            return "Please enter a valid integer"


# obj= Calculator2(20,30)
# print(obj.mul())
# print(obj.add())
# print(obj.div())
#
#
# obj2= Calculator2(15,0)
# print(obj2.mul())
# print(obj2.add())
# print(obj2.div())
#
# obj2= Calculator2(-4,-4)
# print(obj2.mul())
# print(obj2.add())
# print(obj2.div())
#
# obj2= Calculator2(4,-4)
# print(obj2.mul())
# print(obj2.add())
# print(obj2.div())
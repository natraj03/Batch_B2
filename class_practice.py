
class Calculator:

    def mul(self, arg1, arg2):
        return arg1 * arg2

    def add(self,arg1, arg2):
        return arg1 + arg2

    def common(self):
        print(self.mul(10,20))
        print(self.add(15, 20))


obj1 = Calculator()
mul1 = obj1.mul(4,6)
print("--mul rreslt--",mul1)
add1 = obj1.add(4,6)
print("--add rresult--",add1)
obj1.common()


obj2 = Calculator()
mul2 = obj2.mul(14,60)
print("--mul rreslt--",mul2)
add2 = obj2.add(46,60)
print("--add rresult--",add2)
obj2.common()

mul11 = obj1.mul(4,6)
mul12 = obj2.mul(4,6)




class Calculator:

    def multiply(self, inp1, inp2):
        return inp1 * inp2

    def add(self, inp1, inp2):
        return inp1 + inp2

    def sub(self, inp1, inp2):
        return inp1 - inp2


class ReverseStr:
    def reverse_str(self,inp_str):
        result = ""
        for mychar in inp_str:
            result = mychar + result

        return result

class PalendromeStr:

    def ispalendrome(self,inpstr):
        revObj = ReverseStr()
        revstr = revObj.reverse_str(inpstr)
        return revstr == inpstr



# myobj = Calculator()
# print("Multiplication result = ",myobj.multiply(5,6))
# result_add = myobj.add(15,5)
# print("Addition result = ",result_add)
# print("Substrraction result= ",myobj.sub(11,7))
# strobj = ReverseStr()
# print("rerverse String = ",strobj.reverse_str("india"))
# palobj = PalendromeStr()
#
# print("is given string palendrrome = ",palobj.ispalendrome("malayalam"))
#


















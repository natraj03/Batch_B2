# import openpyxl
#
# workbook = openpyxl.load_workbook("practicefile.xlsx")
#
# current_sheet = workbook.active
#
# values = []
# for row in current_sheet.iter_rows(values_only=True):
#     values.append(row)
#
#
# print("all values",values)

class CalculatorFromFile:

    def mult(self,inp1,inp2):
        return inp1 * inp2

    def add(self,inp1,inp2):
        return inp1 + inp2

    def sub(self,inp1,inp2):
        return inp1 - inp2


#
# tempObj = CalculatorFromFile()
#
# for row in values:
#     print("Input values",row)
#     print("Multiplication result ",tempObj.mult(row[0],row[1]))
#     print("Addition result ",tempObj.add(row[0],row[1]))
#     print("Substraction result ",tempObj.sub(row[0],row[1]))
#     print("---------------------------------------\n")


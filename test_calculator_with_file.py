import openpyxl
from  calculator_with_file import CalculatorFromFile


workbook = None

def setup_function():
    global workbook
    workbook = openpyxl.load_workbook("practicefile.xlsx")

def teardown_function():
    global workbook
    if workbook:
        workbook.close()

def test_calculator():
    current_sheet = workbook.active
    values = []
    for row in current_sheet.iter_rows(values_only=True):
        values.append(row)


    tempObj = CalculatorFromFile()

    row = values[0]
    assert tempObj.mult(row[0],row[1]) == 50.0
    assert tempObj.add(row[0],row[1]) == 15.0
    assert tempObj.sub(row[0],row[1]) == -5.0
    print("---------------------------------------\n")

    row2 = values[1]
    assert tempObj.mult(row2[0], row2[1]) == 300.0
    assert tempObj.add(row2[0], row2[1]) == 35.0
    assert tempObj.sub(row2[0], row2[1]) == -5.0
    print("---------------------------------------\n")

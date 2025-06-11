mylist = [5,2,3,4,"asdf asdf",6,1,[1,2,3,4],2]


# rajesh1 = [ name = "rajesh", age =24,exp = 2,pythonEX =2,Living in bengalute = 2,noumber of = 2]
# litu = ["litu", 22,2,3]
# Subrat = ["Subrat", 24,2,2]
# biswajit = ["biswajit", 23, 2, 2]

student1 = {
    "name": "Rajesh M",
    "age": 24,
    "Total Exp" : 2,
    "PythonEXP" : 2,
    "Selenium" : 2,
    "Pytest" : 2,
    "NoOfCompanies": 2
}

student2 = {
    "name": "litu M",
    "age": 24,
    "Total Exp" : 2,
    "PythonEXP" : 2,
    "Selenium" : 2,
    "Pytest" : 2,
    "NoOfCompanies": 2
}

student3 = {
    "name": "Subrat M",
    "age": 24,
    "Total Exp" : 2,
    "PythonEXP" : 2,
    "Selenium" : 2,
    "Pytest" : 2,
    "NoOfCompanies": 2
}

print(" Name = ", student3["Selenium"])

student3["state"] = "Odisha"
print(" state = ", student3["state"])

student3["Selenium"] = 2.5
print(" state = ", student3["Selenium"])
print(" Full info", student3)
del student3["Pytest"]
print(" Full info", student3)
student3.pop("PythonEXP")
print(" Full info", student3)

student3.popitem()
print(" Full info", student3)

student3.clear()
print(" Full info", student3)
student3["name"] = "Subrath"
print(" Full info", student3)
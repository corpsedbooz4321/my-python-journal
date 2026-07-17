class Employee:
    name = (self,)
    language = "Py"
    salary = 1200000


aditya = Employee()
aditya.name = "aditya"
print(aditya.name, aditya.language, aditya.salary)

ankit = Employee()
ankit.name = "ankit"
print(ankit.name, ankit.language, ankit.salary)
# Here name is object attribute and salary and language are class attribute
# as they directly belong to the classH

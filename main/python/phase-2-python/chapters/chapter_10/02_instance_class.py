class Employee:
    language = "Python"  # Class variable
    salary= 50000  # Class variable


aditya = Employee()
aditya.language = "Java"  # Instance variable
print(aditya.salary,aditya.language)  # Output: Java
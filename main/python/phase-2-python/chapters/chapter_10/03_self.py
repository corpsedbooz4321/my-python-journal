class Employee:
    language = "Python"  # Class variable
    salary = 50000  # Class variable

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("good morning!")


aditya = Employee()
aditya.language = "Java"  # Instance variable
print(aditya.salary, aditya.language)  # Output: Java
aditya.getinfo()
aditya.greet()

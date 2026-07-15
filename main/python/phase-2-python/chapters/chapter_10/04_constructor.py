class Employee:
    language = "Python"  # Class variable
    salary = 50000  # Class variable

    def __init__(
        self, name, salary, language
    ):  # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("good morning!")


aditya = Employee("aditya", 50000, "java")
aditya.language = "Java"  # Instance variable
# print(aditya.salary,aditya.language)  # Output: Java
aditya.getinfo()
aditya.greet()

# create a class 'programmer' for storing information of two programmer working
# in Microsoft!
class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("aditya", 129999, 800001)
print(p.name, p.salary, p.pin, p.company)
r = programmer("rohan", 123383, 824122)
print(p.name, p.salary, p.pin, p.company)

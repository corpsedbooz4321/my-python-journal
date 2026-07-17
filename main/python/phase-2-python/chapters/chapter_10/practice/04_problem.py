'''using static method'''

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The squre root is {self.n**(1/2)}")

    @staticmethod
    def hello():
        print("hello aditya!!")


a = calculator(4)

a.square()
a.squareroot()
a.cube()
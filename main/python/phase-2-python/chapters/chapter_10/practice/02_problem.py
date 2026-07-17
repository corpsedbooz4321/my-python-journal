"""write a class "calculator" capable of finding squre, cube and squre root of a number!"""


class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squre root is {self.n**(1/2)}")


a = calculator(4)

a.square()
a.squareroot()
a.cube()

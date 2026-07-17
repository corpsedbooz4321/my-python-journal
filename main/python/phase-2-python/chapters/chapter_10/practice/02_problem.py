"""write a class "calculator" capable of finding squre, cube and squre root of a number!"""


class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")


a = calculator()
a.square()

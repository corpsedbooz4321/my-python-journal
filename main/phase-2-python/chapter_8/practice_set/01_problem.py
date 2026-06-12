'''Write a program using functions to find the greatest of three numbers?'''

def greatest(a, b, c):
    if (a > b and a > c):
        return a
    if (b > a and b > c):
        return b
    if (a > b and a > c):
        return b
    if (c > a and c > b):
        return c
a = 1
b = 2
c = 8568
print(greatest(a, b, c))
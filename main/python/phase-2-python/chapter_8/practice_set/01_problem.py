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
a = int(input('Enter your first number: '))
b = int(input('Enter your esecond number: '))
c = int(input('Enter your third number: '))
print("The greatest number you entered is,", greatest(a, b, c))
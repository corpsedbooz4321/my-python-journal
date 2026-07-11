"""Write a python function to print first lines of the following pattern:"""


def pattern(n):
    print("*" * n)
    print("*" * (n - 1))
    print("*" * (n - 2))


while True:
    n = int(input("Enter your number: "))
    if n == 0:
        print("invalid input, exiting.....")
        break
    pattern(n)

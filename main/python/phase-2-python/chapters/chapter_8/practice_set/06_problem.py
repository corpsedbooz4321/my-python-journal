"""Write a python function which converts inches to centimeters."""


def inches_to_cm(n):
    return n * 2.54


while True:
    n = int(input("Enter your length in inches: "))

    print(f"The converted value in cms is: , {inches_to_cm(n)}")

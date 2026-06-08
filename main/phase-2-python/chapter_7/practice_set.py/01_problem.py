'''write a program to print multiplication table of a given number using for loop'''
while True:
    n = int(input("Enter the number or press (q) to exit: "))
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")
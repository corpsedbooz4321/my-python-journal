'''Write a python functin to print multiplication of the a given number?'''
def table(n):
    for i in range(1, 11):
        #calculating result
        result = n * i
        #printing the result using f string
        print(f"{n} X {i} = {result}")
#taking input from the user
n = int(input('Enter your number: '))
table(n)
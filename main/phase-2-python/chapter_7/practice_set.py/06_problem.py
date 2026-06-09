'''Write a program to calculate the factoral of a given number using for loop?'''

n = int(input("Enter the number: "))

#5! = 1 X 2 X 3 X 4 X 5
product = 1

for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")






n = int(input("Enter the number: "))

product = 1

for i in range(1, n+1):
    product = product * i
print(product)
    
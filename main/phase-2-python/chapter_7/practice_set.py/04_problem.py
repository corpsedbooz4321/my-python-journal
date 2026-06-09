'''write  a program to find out that the given number is prime or not?'''

prime = int(input("Enter your number: "))

for i in range(2, prime):
    if (prime%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
    

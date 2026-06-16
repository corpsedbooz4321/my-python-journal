a = int(input("Enter age: "))
if a >= 18:
    print("you are above the age of consent")
    print("GOOD for you")
elif a < 0:
    print("you are entering an inavlid negative age")
elif(a==0):
    print("you are enteringa 0 which is not a valid age")
else:
    print("you are below the age of consent")

print("end of the program")

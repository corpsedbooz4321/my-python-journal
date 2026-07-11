a = int(input("Enter age: "))

#if staatement no. 1
if (a%2 == 0):
    print("a is even")
else:
    print("a is odd")
#end of statement no.1

#if statement no. 2
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
#end of statement no. 2
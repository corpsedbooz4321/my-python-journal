'''write a program to find the greatest of four numbers entered by the user.'''

u1 = int(input("Enter the number: "))
u2 = int(input("Enter the number: "))
u3 = int(input("Enter the number: "))
u4 = int(input("Enter the number: "))

if (u1 > u2 and u1 > u3 and u1 > u4):
    print("the greatest number is:",u1)
elif (u2 > u1 and u2 > u3 and u2 > u4):
    print("the greatest number is:",u2)
elif(u3 > u1 and u3 > u2 and u3 > u4):
    print("the greatest number is:",u3)
elif(u4 > u1 and u4 > u2 and u4 > u3):
    print("the greatest number is:",u4)


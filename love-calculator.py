name1 = input("Enter your name: ")
name2 = input("Enter you Girlfriend's name: ")


import random
num = random.randint(0,100)

print(num, "is your love score!")

if(num >= 90):
    print("You are made for each other🥳💖") 
elif(num < 90 and num > 70):
    print("You both are heading to the path of each others heart!🥰")
elif(num < 70 and num >= 40):
    print("You both need and try to understand each other, btw it'll be fine!😃")
else:
    print("it'd would be better if you guys focus on your careers!🤡 ")



print("\n======================THE LOVE CALCULATOR======================")

def LOVE():#All the calculation part. 
    import random
    num = random.randint(0,100)

    print(num, "is your love score!")

    if(num >= 90):
        print("You are made for each other🥳💖") 
    elif(num < 90 and num > 70):
        print("You both are heading to the path of each others heart!🥰")
    elif(num < 70 and num >= 40):
        print("You both need to try to understand each other, btw it'll be fine!😃")
    else:
        print("it'd would be better if you guys focus on your studies!🤡 ")

#taking users input.
while True:
    try:
        boy = input("\nEnter your name🚹: ")
        if not boy.replace(" ","").isalpha():
            raise ValueError
        girl = input("Enter your Girlfriend's name🚺: ")
        print("\nKEEP IN MIND THAT THIS IS JUST A SIMULATOR❗")
        input("\nto view the love score press enter..")
        print("==========YOUR LOVE SCORE==========")
        LOVE()
        xx = input("\nDo you wish to continue...(Yes/No): ").lower()
        if xx == "yes":
            continue
        elif xx == "no":
            break
    except ValueError:
        print("Invalid input....enter a valid name.")
    

        
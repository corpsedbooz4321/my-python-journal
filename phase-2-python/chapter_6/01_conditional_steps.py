# if elif else ladder
while True:
    a = int(input("Enter your age: "))

    if a >= 18:
        print("you are eligible to vote")
        break
    elif a < 18:
        print("you are not eligible to vote!")
        break

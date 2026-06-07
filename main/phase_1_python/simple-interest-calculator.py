#simple interest calculator

while True:
    P = float(input("principal: "))
    R = float(input("rate: "))
    T = float (input("time: "))

    #calculation part
    print(P*R*T/100,"is your simple interest")
    
    

    xx = input("if you want to continue press(Y)😀 or if you want to exit(N)😶.......").lower()
    if xx == "y":
       continue

    elif xx == "n":
       break
    else:
        print("invalid input")
        continue

     
    


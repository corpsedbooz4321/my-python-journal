'''We all have played snake, water gun game in our childhood. if you haven't.
google the rles of this game and write a python program capcale of playing this game with
the user.'''

'''1 for snake
   -1 for water
   0 for gun'''
import random

#MAPPING
youdict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}
reversedict = {
    1 : "snake", 
    -1 : "water",
    0 : "gun"
}

while True:
    youstr = input("\nEnter your choice: ").lower()
    if youstr == 'q': 
        break
    if youstr not in youdict:
        print("Invalid input")
        continue

    you = youdict[youstr]

    computer = random.choice([-1, 1 ,0])

    print(f"\nyou chose, {reversedict[you]}\ncomputer chose, {reversedict[computer]}")

    diff = computer - you

    if diff == 0:
        print('its a draw!')
    elif diff == -1 or diff == 2:
        print('you lost!')
    else:
        print('you win!')
#the logic
    # if computer == -1 and you == 1:
    #     print('You win!')

    # elif computer == -1 and you == 0:
    #     print('You lost!')

    # elif computer == 1 and you == -1:
    #     print('you lost!')

    # elif computer == 1 and you == 0:
    #     print('you win!')

    # elif computer == 0 and you == -1:
    #     print('you win!')

    # elif computer == 0 and you == 1:
    #     print('you lost!')

    # else:
    #     print('something went wrong')



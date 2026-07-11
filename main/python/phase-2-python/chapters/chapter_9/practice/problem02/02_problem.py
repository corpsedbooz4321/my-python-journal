"""The game() function in a program lets a user play a game and returns the score as
an integer. You need to read a file "high_score.txt" which is either blank or contains the game high score.
"""

import os
import random

script = os.path.dirname(os.path.abspath(__file__))
path_file = os.path.join(script, "score.txt")


def game():
    print("You are playin the game...")
    score = random.randint(1, 100)

    if os.path.exists(path_file):
        with open(path_file, "r") as file:
            high_score = file.read()
            if high_score != "":
                high_score = int(high_score)
            else:
                high_score = 0
    else:
        high_score = 0

    print(f"Your score is {score}")
    if score > high_score:
        print("New High Score!")
        with open(path_file, "w") as file:
            file.write(str(score))
    return score


game()

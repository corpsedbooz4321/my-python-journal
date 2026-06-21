'''The game() function in a program lets a user play a game and returns the score as 
an integer. You need to read a file "high_score.txt" which is either blank or contains the game high score.'''

import random
import os

script = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script, "high_score.txt")

def game():
    print("You are playing the game...")
    score = random.randint(1, 100)

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0
    else:
        highscore = 0

    print(f"Your score: {score}")
    if score > highscore:
        print("New High Score!")
        # write this high score into a file!
        with open(file_path, "w") as f:
            f.write(str(score))
    return score
game()
	


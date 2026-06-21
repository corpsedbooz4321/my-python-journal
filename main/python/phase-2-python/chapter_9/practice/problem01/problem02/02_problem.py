'''The game() function in a program lets a user play a game and returns the score as 
an integer.you need to read a file "Hi-score.txt"
which is either bland or contains the game() function breaks the Hi-score?'''

import random

def game():
	print("You are playing the game...")
	score = random.randint(1, 100)
	with open("high_score.txt", "r") as f:
		highscore = f.read()
		if highscore != "":
			highscore = int(highscore)
		else:
			highscore = 0
	print(f"Your score: {score}")
	if score > highscore:
		#write this high score into a file!
		with open("high_score.txt", "w") as f:
			print(f.write(str(f"your high score is : {score}")))
game()
	


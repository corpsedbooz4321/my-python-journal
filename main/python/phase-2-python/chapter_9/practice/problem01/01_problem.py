'''write a program to read the text from the given file "poems.txt" and find out
whether it contains the word twinkle?
'''

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"poems.txt")
with open(file_path, "r") as f:
	data = f.read()

	if "Twinkle" in data:
		print('found!')
	#print(data)
	
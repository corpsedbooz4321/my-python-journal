'''A file contains a word "donkey" multiple times. you need to weite a program which
replace this word with ####3 by updating the same file.
'''



words = "Donkey"

with open("file.txt", "r") as f:
	data = f.read()


for word in words:
    New_data = data.replace(word, "######")

	

with open("file.txt", "w") as f:
	f.write(New_data)
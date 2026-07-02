words = ['Donkey', 'ganda', 'dihh', 'am']


with open('file.txt', "r") as f:
	data = f.read()


for word in words:
	data = data.replace(word, "#######")

with open('file.txt', "w")as f:
	f.write(data)
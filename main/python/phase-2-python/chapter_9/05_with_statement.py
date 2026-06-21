f = open("file.txt")
print(f.read())
f.close()



'''the same can be written using the with 
statement like this'''

with open("file.txt") as f:
	print(f.read())

'''using this pathway, you won't have to writ f.close()
everytime at the end
'''
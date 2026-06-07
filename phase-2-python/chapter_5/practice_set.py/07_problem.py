''' fi the names of 2 friends are same; what will happen to the program in problem 6'''

d = {}

# Friend 1
name = input('Enter friends name: ')
lang = input('Enter language name: ')
d.update({name: lang})

# Friend 2
name = input('Enter friends name: ')
lang = input('Enter language name: ')
d.update({name: lang})

# Friend 3
name = input('Enter friends name: ')
lang = input('Enter language name: ')
d.update({name: lang})

# Friend 4
name = input('Enter friends name: ')
lang = input('Enter language name: ')
d.update({name: lang})

# This will now print right after the 4th friend!
print(d)
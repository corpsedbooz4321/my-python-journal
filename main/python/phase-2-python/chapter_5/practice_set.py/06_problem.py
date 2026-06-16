'''create an empty dictionary allow 4 friends to enter their favorite languages as values and 
use key as their names. assume that the names are unique'''
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
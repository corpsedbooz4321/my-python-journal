'''File processing
A text file can be thought of as a sequence of lines'''

'''Before we can read the contents of the file, we must tell python
which file we are going to work with and what we will be doing wiht the file.'''

'''This is done with the "open()" function
open() returns a "file handel" -a variable used to perform
operations ont the file.


similar to "File -> Open" in a word processor.


USING OPEN()


handle = open(filename, mode)


returns a handle use to manipulate the file

file name is string

mode is optional and should be 'r' if we are planning to read
the file and "w" if we are going to write to the file.'''
# =====================================================================================

##example and practices.

# farm = open('mbox.txt')
# print(farm)

#WHEN FILES ARE MISSING.
'''farm = open('stuff.txt')
traceback (most recent call last):
file "<stdin>", line 1, in <module>
filenotfounderror: [ERRNO 2] No such file or directory: "stuff.txt"'''


'''We use a special character called the "newline" to indicate 
when a line ends.

we represent it as /n in strings

Newline is still one charcter - not two.'''

stuff = 'hello\nworld'
print(stuff)
print("The lenght of the string is:", len(stuff))
# a = (1, 3455, 53, 33564, 453564, 534525, 2525, 'rohan', 'rahul', 'aditya')
# print(type(a))


# #tuple method "1"
# #[count]
# xx = a.count(53)
# print(xx) #this method counts the available number of 53 present in the tuple list.


#tuple method "2"
#[index]
t = (10, 48, 39, 57, 19, 49, 4854895, 20, 10, 48, 39, 39, 39)
print(t.index(39))#this method returns the first occurence of the number you have inserted.

'''some common operation on tuples.
even though tuples dont have many methods, i can stilll use built-in functions and operators:'''

print(len(t))
print(max(t))
print(min(t))
print(sum(t))

'''we can do slicing in the tuples as we did in the strings
'''

xx = t[0:5]
print(xx)


'''we can also do concatenation in tuples'''
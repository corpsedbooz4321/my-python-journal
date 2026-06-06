s = {4, 3, 3, 4848, 43846, 83, 36378, 47347, 0, 65, 'aditya', 'mahima'}

print(type(s))


#core set methods.
'''*1*'''
s.add(7684)
print(s)  # output - {0, 65, 3, 4, 7684, 43846, 4848, 83, 47347, 'mahima', 'aditya', 36378}

'''*update()*'''
s.update([7684, 7])
print(s) # output - {0, 65, 3, 4, 7684, 43846, 7, 4848, 83, 47347, 36378, 'aditya', 'mahima'}


'''*remove()*'''
s.remove(7684)
print(s) # output - {0, 65, 3, 4, 43846, 7, 'mahima', 4848, 83, 47347, 'aditya', 36378}

'''*discard()*'''
s.discard(0)
print(s) # output - {65, 3, 4, 43846, 7, 'mahima', 4848, 83, 47347, 'aditya', 36378}
                    #does nothing if the that specific element not found. 

'''*pop()*'''
s.pop( ) #removs and returns an arbtrary element.

# '''*clear()*'''
# s.clear #removes all the elemets.


#SET OPERATIONS
'''*union()*'''
a = {2, 5} ; b = {3, 6, 2}
print(a.union(b)) #output - {2, 3, 5, 6} combines eleements form two sets.

'''*intersection()*'''
print(a.intersection(b)) #output - common elements btween sets.

'''*difference()*'''
print(a.difference(b)) #output - {5} elements i none set but not the other.
print(b.difference(a)) #output - {3, 6} elements i none set but not the other.

'''symmetric_difference()**'''
print(a.symmetric_difference(b)) #output - {3, 5, 6} elements in either set but not in both.
print(b.symmetric_difference(a)) #output - {3, 5, 6} elements in either set but not in both.

#MEMBERSSIP $ RELATIONS

a.issubset(b) #checks if all elements of one set are in another.

a.issuperset(b) #checks if a set contains all the elements of another.

a.isdisjoint(b) #checks if two sets have no elements in common.
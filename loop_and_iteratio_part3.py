# #python basic loop.
#===============================================================================================================================
#to run all this code you have to comment other codes except one you want to use.
print("Before")
for thing in [9, 42, 33, 55,33,]:
    print(thing)
print("after")
#================================================================================================================================
#Finfindg the largest value.
largest_so_far = -1
print('before', largest_so_far)
for the_num in [45, 23, 645, 643, 2 ,24,5252, 4234,]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)
# ==================================================================================================================================
#largest number finder.
largest = -1
print("first", largest)
for n > largest:
        largestum in [43, 54, 77, 343, 3543, 88, 11]:
    if num = num
    print("current number:", num, "largest number:", largest)
#==============================================================================================================================
#to count how may times we execute a loop , weintroduce a counter variable tht astarts at 0 and we add one to it each time
#each time thorough the loop.
zork = 0
print('Before', zork)
for thing in [38, 854, 49, 477, 48]:
    zork = zork + 1
    print(zork, thing)
print('after', zork)
print('blastoff!')
# ==================================================================================================================================
summing in a loop
to add up a value we encounter in a loop, we intoduce a sum variable that starts afj 0 and we add the value to the sum each
time thorough the loop.
zork = 0
print('Before', zork)
for thing in [8, 33, 55, 44, 11, 304]:
    zork = zork + thing
    print(zork, thing)
print('after', zork)
#===================================================================================================================================
#Finding the average in loop
# An avrage just combines the counting and sum patterns and divides when the loop is done.
count = 0
sum = 0
print('Before', count, sum)
for value in [844, 34, 43, 56, 18]:
    count = count + 1
    sum  = sum + value
    print(count, sum, value)
print('after', count, sum, sum / count)
# ====================================================================================================================================
Filtering out the loop.
we use an if statement in the loop to catch/filter the values we are looking for.
print("before")
for value in [49, 48, 47, 94, 646]:
    if value > 50:
        print("large number: ",value)
print('after')
# =====================================================================================================================================
#search using a boolean variable
#if we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find
#what we are looking for.
found = False
print('Before', found)
for value in [56, 93, 47, 494, 99, 00, 36]:
    if value == 494:
        found = True
    print(found, value)
print('after', found)
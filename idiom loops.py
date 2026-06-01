Searching using boolean variable
found = False
print('Before', found)
for value in [9, 48, 49, 4, 12, 45]:
    if value == 4:
       found = True
       print('found',value)
       break
    else: continue
print('after', found)
======================================================================================



How to find the smallest value?

largest_so_far = -1
print('before', largest_so_far)
for the_num in [48, 48888,30, 34, 487]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)






smallestsofar = -1
print('before', smallestsofar)
for num in [38, 30, 22, 44, 576]:
    if num < smallestsofar:
       smallestsofar = num
    print(smallestsofar, num)




smallest = None
print('Before')
for value in [48, 96, 77, 39, 63]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("after", smallest)







smalllest = None
print('Before')
for value in [49, 79, 89, 99,]:
    if smalllest is None:
        smalllest = value
    elif value < smalllest:
        smalllest = value
    print(smalllest,value)
print('the smallest number:', smalllest)


smallest = e
for Nonvalue in min(93, 48, 49, 38, 84, 30, 288, 83, 20000, 288, 1):
    print(value)
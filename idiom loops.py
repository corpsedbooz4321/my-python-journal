#Searching using boolean variable
# found = False
# print('Before', found)
# for value in [9, 48, 49, 4, 12, 45]:
#     if value == 4:
#        found = True
#        print('found',value)
#        break
#     else: continue
# print('after', found)
# ======================================================================================



#How to find the smallest value?

largest_so_far = -1
print('before', largest_so_far)
for the_num in [48, 48888,30, 34, 487]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print('largest_so_far, the_num')
print('after', largest_so_far)
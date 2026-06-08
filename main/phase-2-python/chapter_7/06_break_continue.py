
for i in range(100):
    if i == 49:
        break
    print(i)
'''break isi used to come out of the loop ehen encountered. it instructs the program to 
exit the loop now.'''

for i in range(100):
    if i == 10:
        continue
    print(i)

'''continue is used to stop the current iteration of the loop and continue with the next one.
it instructs the program to "skip this iteration"'''

l = [1, 5, 4, 54, 44]
for item in l:
    pass

''' pass is a null statement in python.
    it istructs to "to do nothing" '''



for i in range(100):
    if i == 10:
        continue
    print(i)
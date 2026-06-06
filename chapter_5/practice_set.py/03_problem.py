'''can we have a set with 18 (int) and '18' (str) as a value in it?'''

s = set()
n = input("enter the number: ")
s.add(int(n))
n = input("enter the number: ")
s.add(n)

print(s)

#this code printes the 18 as integer and '18' as string.
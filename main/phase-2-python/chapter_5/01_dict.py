d = {}#empty dictionary

marks = {
    "aditya": 100,
    "mahima": 98,
    "ankit": 85
}
# print(marks.items)
# print(marks, type(marks))
# print(marks["aditya"])
def marks_():
    while True:
       t = input("enter the name: ")
       if t in marks:
           p = (marks[t])
           print(f"marks of,{t}: {p}")
           continue
       else:
           print('Name not found!')
while True:
    print("To check your marks press 2 or press 1 to check the toppers and the lowest marks.")
    x = int(input())
    if x == 1:
        print("Topper:", max(marks, key=marks.get))
        print("failed:", min(marks, key=marks.get))
        continue
    elif x== 2:
        marks_()



#Dictionary methods

'''get() returns the value for a key if  it exists, otherwise return none or a default value.
ex-
marks.get("aditya") returns 100
marks.get("unknown", "not found") #'not found'''

'''keys() returns all keys in the dictionary
ex-
markd.keys() #dict_keys(['aditys', 'mahima', 'ankit'])

values() returns all values
ex-
marks.values() #dict_values([100, 98, 85])

items returns key -- value pairs as tuples

update() updates dictionary with new key--value pairs

pop() removes a key and returns its values

popitem() removes all the items from the dictionary.

copy() returns a shallow copy of the dictionary.

setdefault() returns the value of a key, and if the key doesn't exist 
intserts it with a default value.'''
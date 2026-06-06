'''write a program to create a dictionary of hindi words with values as their english
translarions. Provide user with an option to look it up.'''

words = {
    "madad": "help",
    "chor": "thief",
    "chatt": "roof"
}
while True:
    try:
        word = input("Enter the word you want the meaning of: ")
        print(words[word])
        continue
    except:
        print("not found!")
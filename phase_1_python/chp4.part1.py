def thing():
    print("hello aadi")
    print("kumar")
thing()
print("zip")
thing()

big = max('Hello world')
print(big)

  

# #building our own functions 
# #  we create a new function using def keyword followed by optional parameters in parentheses


# more paractice

def print_lyrics():
    print("oh its hard to see you when i get you every where,all this time i thinki'n slow enough to thinking")
print_lyrics() 

# # how we define 

def greet(lang):
    if lang == "en":
        print("HELLO")
    elif lang == "es":
        print("HOLA!")
    elif lang == "bh":
        print("kaisan bada ho!!")
    else:
        print("welcome")

lang = greet(input("enter your language's first two letter's: "))


# part2

def greet():
    return "hello"
print(greet(), "aditya")
print(greet(), "mahima")
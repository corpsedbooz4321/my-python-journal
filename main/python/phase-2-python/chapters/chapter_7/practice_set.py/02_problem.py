"""write a program to greet all the persons name stored in a list "i" and which starts with S."""

l = ["aditya", "soham", "sachin", "rahul"]

for i in l:
    if i.startswith("s"):
        print(f"Hello, and welcome, {i}")

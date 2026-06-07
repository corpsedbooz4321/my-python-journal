'''write a program to find out whether a given post is talking about "aditya" or not'''

post = input("Enter the post: ").lower()


if "aditya" in post:
    print("this post is talking about", post)
else:
    print("this post is not talking about", post)
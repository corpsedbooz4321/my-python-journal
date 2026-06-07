'''write a program to find whether a given usernae contains less then 10 characters or not'''

username = input("Enter your user name: ")

if len(username) < 10:
    print("the user name can not contain less than 10 letters...invalid user name.")
else:
    print("valid user name. go ahead")
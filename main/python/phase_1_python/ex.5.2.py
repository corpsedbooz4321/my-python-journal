# 5.2 Write a program that repeatedly prompts a user for integer numbers 
# until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. If the user 
# enters anything other than a valid number 
# catch it with a try/except and put out an appropriate message 
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.





largest = None
smallest = None
while True:
    '''taking a endless input from the user until the user types "done".'''
    count_ = input('Enter a number: ')
    if count_ == 'done':
        break
    try:
        cal_ = int(count_)
        if largest is None or cal_ > largest:
            largest = cal_
        elif smallest is None or cal_ < smallest:
            smallest = cal_
    except:
        print("Invalid input")
print('Maximum', largest)
print('Minimum', smallest)



   

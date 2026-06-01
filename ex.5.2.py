# 5.2 Write a program that repeatedly prompts a user for integer numbers 
# until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. If the user 
# enters anything other than a valid number 
# catch it with a try/except and put out an appropriate message 
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.





largest = None
smallest = None
while True:
    '''taking input form the user!'''
    val_ = input('Enter a number: ')
    if val_ == 'done':
        break
    try:
        sval_= int(val_)
        if largest is None or sval_ > largest:
            largest = sval_
        elif smallest is None or sval_ < smallest:
            smallest = sval_
    except:
        print('INVALID INPUT')
print('Maximum is', largest)
print('Minimum is', smallest)

   

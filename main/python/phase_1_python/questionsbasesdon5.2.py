# write a program that keeps asking the user for numbers until they type "done". 
# At the end, print the sum of all valid numbers entered. 
# Ignore invalid inputs with try/except.

total = 0
while True:
    """taking input from the user!"""
    val_ = input('Enter a number: ')
    if val_ == 'Finish':
        break
    try:
        pval_ = int(val_)
        total += sum
    except:
        print('Invalid input!')
print('The sum of all the numbers you enterd is:', total)
    

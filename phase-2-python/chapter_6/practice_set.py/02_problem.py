'''write a program to find out whether a student ahs passed or failedkif it requires a fotal of 4o% and at least 33% in each subject to pass. assume 3 subjects
and take marks as an iput form the user'''

def check_result(mk, mp, mc):
    total_percentage = ((mk + mp + mc) / 300) * 100
    
    if mk >= 33 and mp >= 33 and mc >= 33 and total_percentage >= 40:
        return True, total_percentage
    else:
        return False, total_percentage


mk = int(input("Enter the marks of first subject : "))
mp = int(input("Enter the marks of second subject : "))
mc = int(input("Enter the marks of third subject : "))

if mk > 100 or mc > 100 or mp > 100:
    print("invalid marks")
else:
    is_passed, percentage = check_result(mk, mp, mc)

    if is_passed:
        print(f"Congratulations! You passed. Total percentage: {percentage:.2f}%")
    else:
        print(f"Sorry, you failed. Total percentage: {percentage:.2f}%")

   

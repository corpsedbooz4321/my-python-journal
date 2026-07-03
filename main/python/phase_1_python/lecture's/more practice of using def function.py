# Question

# Write a program to prompt the user for a score between 0.0 and 1.0.

# Create a function called:

# computegrade(score)

# The function should return a grade using this table:

# Score	Grade
# >= 0.9	A
# >= 0.8	B
# >= 0.7	C
# >= 0.6	D
# < 0.6	F


# Requirements
# Use input() to take score
# Use float() conversion
# Use a function
# Use return
# Print the final grade

# Example
# Input:

# 0.85

# Output:

# B


def computegrade(score):
    # print("in computegrade", score)
    if score > 1.0 or score < 0.0:          #for the input greater than 1.0
        return "invalid score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6:
        return "F"
    # return score

score = float(input("Enter your score: "))

result = computegrade(score)

if result == "invalid score":
    print("invalid score")
else:
    print("Grade:",result)
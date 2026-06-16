'''How do you prevent python to prevent print() function
to print a new line at the end?'''

# Use the 'end' parameter in print() function
# By default, end='\n' (newline)
# To prevent newline, set end='' or any other string

# Example 1: Without newline
print("Hello", end='')
print("World")

# Example 2: With custom separator instead of newline
print("Python", end=' ')
print("Programming")

# Example 3: Multiple prints on the same line
for i in range(1, 4):
    print(i, end=' ')
print()  # This prints a newline to move to next line
# ============================================
# PYTHON FUNCTIONS - COMPREHENSIVE TEACHING CODE
# ============================================


# 1. BASIC FUNCTION WITHOUT ARGUMENTS
# ====================================
def greet():
    """Function with no arguments"""
    print("Hello! Welcome to Python Functions")


# greet()  # Call it


# 2. FUNCTION WITH POSITIONAL ARGUMENTS
# ======================================
def goodday(name):
    """Function with one argument"""
    print(f"Hello Mr. {name}")


# goodday("Aditya")  # Call it


# 3. FUNCTION WITH MULTIPLE ARGUMENTS
# ====================================
def add(a, b):
    """Function that adds two numbers"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


# add(5, 3)


# 4. FUNCTION WITH DEFAULT ARGUMENTS
# ===================================
def greet_with_age(name, age=18):
    """Function with default argument"""
    print(f"Hello {name}, you are {age} years old")


# greet_with_age("Aditya")  # uses default age
# greet_with_age("Aditya", 25)  # overrides default


# 5. FUNCTION WITH RETURN VALUES
# ===============================
def multiply(x, y):
    """Function that returns a value"""
    return x * y


# result = multiply(4, 5)
# print(f"Multiply result: {result}")


# 6. FUNCTION WITH MULTIPLE RETURN VALUES
# ========================================
def get_user_info():
    """Function that returns multiple values"""
    name = "Aditya"
    age = 22
    city = "Delhi"
    return name, age, city


# name, age, city = get_user_info()
# print(f"{name} is {age} years old and lives in {city}")


# 7. FUNCTION WITH *args (VARIABLE LENGTH ARGUMENTS)
# ==================================================
def sum_all(*numbers):
    """Function that accepts any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total


# print(sum_all(1, 2, 3))  # 6
# print(sum_all(1, 2, 3, 4, 5))  # 15


# 8. FUNCTION WITH **kwargs (KEYWORD ARGUMENTS)
# ==============================================
def print_details(**details):
    """Function that accepts keyword arguments"""
    for key, value in details.items():
        print(f"{key}: {value}")


# print_details(name="Aditya", age=22, city="Delhi")


# 9. COMBINING ARGS AND KWARGS
# ============================
def full_function(name, *args, **kwargs):
    """Function with positional, args, and kwargs"""
    print(f"Name: {name}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


# full_function("Aditya", 1, 2, 3, age=22, city="Delhi")


# 10. FUNCTION WITH TYPE HINTS
# ============================
def calculate_area(radius: float) -> float:
    """Function with type hints (Python 3.5+)"""
    import math

    return math.pi * radius**2


# area = calculate_area(5.0)
# print(f"Area: {area}")


# 11. SCOPE - LOCAL VS GLOBAL VARIABLES
# =====================================
global_var = "I am global"


def scope_example():
    local_var = "I am local"
    print(global_var)  # Can access global
    print(local_var)  # Can access local


# scope_example()
# print(global_var)  # Works
# print(local_var)   # Error - not defined outside function


# 12. NESTED FUNCTIONS
# ====================
def outer_function():
    """Function containing another function"""

    def inner_function():
        print("I am inside outer function")

    print("Outer function")
    inner_function()


# outer_function()


# 13. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ===========================================
square = lambda x: x**2
add_lambda = lambda a, b: a + b

# print(square(5))  # 25
# print(add_lambda(3, 4))  # 7


# 14. PRACTICAL EXAMPLE - CALCULATOR
# ==================================
def calculator(a, b, operation):
    """Calculator function with operation"""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"


# print(calculator(10, 5, "+"))  # 15
# print(calculator(10, 5, "-"))  # 5


# 15. INTERACTIVE FUNCTION WITH USER INPUT
# ========================================
def interactive_greet():
    """Interactive function with user input"""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old!")


# interactive_greet()


# ============================================
# PRACTICE EXERCISES
# ============================================


# Exercise 1: Create a function that calculates factorial
def factorial(n):
    """Calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# print(f"Factorial of 5: {factorial(5)}")  # 120


# Exercise 2: Create a function that checks if a number is prime
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# print(is_prime(17))  # True
# print(is_prime(15))  # False


# Exercise 3: Create a function that reverses a string
def reverse_string(s):
    """Reverse a string"""
    return s[::-1]


# print(reverse_string("Aditya"))  # aytiidA


# UNCOMMENT AND RUN ANY FUNCTION TO TEST IT!
if __name__ == "__main__":
    # Test area - uncomment functions below to run them
    greet()
    goodday("Aditya")
    add(10, 20)
    greet_with_age("Aditya", 25)
    print(f"Multiply: {multiply(4, 5)}")
    print(f"Sum all: {sum_all(1, 2, 3, 4, 5)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Reverse 'Aditya': {reverse_string('Aditya')}")

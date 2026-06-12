'''Write a python program using function to convert celsius to 
Fahrenheit.'''

def celsius_to_fahrenheit(a):
    fahrenheit = (a * 1.8) + 32
    return fahrenheit

a = float(input("Enter your celsius number: "))
fahrenheit = celsius_to_fahrenheit(a)
print(f"The the temperature in fahrenheit is {fahrenheit}")

# Phase 1: Python Fundamentals - Assignment 1
#
# Learnt in this file:
# - Reading and formatting console input/output with f-strings.
# - Performing arithmetic operations and type casting.
# - Swapping variable values.
# - Implementing basic formulas (Celsius to Fahrenheit, Area of a Circle, Simple Interest).
# - Extracting parts of numbers using type casting.

def greet_user():
    """Learned: Reading string inputs and formatting output using f-strings."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello, {name}! You are {age} years old.")

def basic_calculator():
    """Learned: Performing addition, multiplication, division and casting input to integers."""
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum_result = num1 + num2
    product_result = num1 * num2
    quotient_result = num1 / num2
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The product of {num1} and {num2} is: {product_result}")
    print(f"The quotient of {num1} divided by {num2} is: {quotient_result}")

def calculate_average():
    """Learned: Calculating average of three numbers and working with float types."""
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    avg = float((num1+num2+num3)/3)
    print(f"The average of {num1}, {num2}, and {num3} is: {avg}, and type is {type(avg)}")

def type_conversions():
    """Learned: Explicit type conversion / casting between int, float, and string."""
    num = input("Enter first number: ")
    to_int = int(num)
    to_float = float(num)
    to_str = str(num)
    print(f"The integer value is: {to_int}, and type is {type(to_int)}")
    print(f"The float value is: {to_float}, and type is {type(to_float)}")
    print(f"The string value is: {to_str}, and type is {type(to_str)}")

def operator_precedence():
    """Learned: Understanding operator precedence (exponents first, then multiplication, then addition)."""
    # Calculation: 10 + 3 * (2**2) = 10 + 3 * 4 = 10 + 12 = 22
    x = 10 + 3 * 2**2
    print(f"Result of 10 + 3 * 2**2 is: {x}")

def swap_variables():
    """Learned: Swapping values of two variables using a temporary storage variable."""
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Before swapping: first = {num1}, second = {num2}")
    num3 = num1 
    num1 = num2
    num2 = num3
    print(f"After swapping, first number is: {num1}, second number is: {num2}")

def celsius_to_fahrenheit():
    """Learned: Converting temperatures from Celsius to Fahrenheit."""
    celcius = input("Enter temperature in Celsius: ")
    conversion = float(celcius)
    fahrenheit = (conversion * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}")

def area_of_circle():
    """Learned: Computing circle area using standard mathematical formula (pi * r^2)."""
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.1416
    area = pi * radius**2
    print(f"The area of the circle with radius {radius} is: {area}")

def simple_interest():
    """Learned: Calculating simple interest based on Principal, Rate, and Time."""
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time (in years): "))
    interest = (principal * rate * time) / 100
    print(f"The simple interest is: {interest}")

def extract_fractional_part():
    """Learned: Isolating the fractional component of a floating-point number."""
    num = float(input("Enter a number: "))
    fractional_part = num - int(num)
    print(f"The fractional part of the number {num} is: {fractional_part}")

if __name__ == "__main__":
    # Let's showcase operator precedence and run a demo or list of functions
    print("--- Assignment 1: Python Fundamentals Demo ---")
    operator_precedence()
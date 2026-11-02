# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
math_operations.py
"""Custom module with basic math operations."""
 
 
def add(a, b):
    """Return the sum of a and b."""
    return a + b
 
 
def subtract(a, b):
    """Return the difference of a and b."""
    return a - b
 
 
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
 
 
def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
 
 
def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent

# TODO: Import the custom module and use its functions
import math

# Test the imported functions
result_add = math.add(10, 5)
result_sub = math.subtract(10, 5)
result_mul = math.multiply(10, 5)
result_div = math.divide(10, 5)
result_zero = math.divide(10, 0)

# Print results
print(f"10 + 5 = {result_add}")
print(f"10 - 5 = {result_sub}")
print(f"10 * 5 = {result_mul}")
print(f"10 / 5 = {result_div}")
print(f"10 / 0 = {result_zero}")

# TODO: Use a while loop to create a simple calculator
from math_operations import add, subtract, multiply, divide, power
 
OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
}
 
 
def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")
 
 
def main():
    print("Simple Calculator")
    print("Operations: + - * / **   (type 'q' to quit)")
 
    while True:
        op = input("\nEnter operation: ").strip()
 
        if op.lower() == "q":
            print("Goodbye!")
            break
 
        if op not in OPERATIONS:
            print("Unknown operation, please use one of: + - * / **")
            continue
 
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
 
        try:
            result = OPERATIONS[op](a, b)
            print(f"{a} {op} {b} = {result}")
        except ValueError as error:
            print(f"Error: {error}")
 
 
if __name__ == "__main__":
    main()
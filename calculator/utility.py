"""
Assignment

Build and Test a Utility Module

Create a module with basic math functions.

Use `__name__ == "__main__"` to test the functions.

Import the module in another file and reuse the functions without triggering the test code.
"""

def add(x:int, y:int):
    return x+y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


if __name__ == "__main__":
    print("-"*5)
    print('Calculator')
    prompt = input("Select any operation below by entering the number\n1. Add\n2. Subtract\n3. Multiplication\n4. Division\n")

    num1 = int(input("Enter an operand: "))
    num2 = int(input("Enter second operand: "))

    if prompt == '1':
        result = add(x=num1, y=num2)
        print(result)
    elif prompt == '2':
        result = subtract(x=num1, y=num2)
        print(result)
    elif prompt == '3':
        result = multiply(x=num1, y=num2)
        print(result)
    elif prompt == '4':
        result = divide(x=num1, y=num2)
        print(result)
    else: 
        print("Operation not available")
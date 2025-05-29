# x = 1 #global scope

# def outer():
#     enclosing_variable = 10 #enclosing scope

#     def inner_func():
#         print(enclosing_variable) #local scope

#     inner_func()


# outer() #local x
# print(x) #global x

# count = 0

# def foo():
#     global count
#     count += 4
#     print(count)

# print(f"count before function call: {count}")
# foo()
# print(f"count after function call: {count}")

# ----------------------

def outer():
    x = 10 

    def inner():
        nonlocal x
        x += 2
        print(x) 

    inner()

# outer()

"""
- Define a global list `fruits = ["apple", "banana"]`.  
- Write a function `add_fruit(fruit)` that **adds a new fruit** to `fruits`.  

"""
# fruits = ["apple", "banana"]

# def add_fruit(new_fruit: str):
#     fruits = []
#     fruits.append(new_fruit)
#     return fruits

# print(fruits)
# print(add_fruit('citrus'))
# print(fruits)

x = 10

def outer():
    """
    Outer function to explain enclosing scope
    """
    x = 20
    def inner():
        nonlocal x
        x += 30
    inner()
    print(x)

# outer()
# print(x)

"""

Assignment

1.  Buggy Code

```
balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ${amount}. Current balance: ${balance}")

def withdraw(amount):
    balance -= amount
    print(f"Withdrew ${amount}. Current balance: ${balance}")


deposit(500)
withdraw(200)
```

# Task:
Run the code and observe the output. You'll notice that the `withdraw` function doesn't seem to be updating the `balance` variable correctly.

# Debugging Exercise:
1. Identify the scope issue in the withdraw function.
2. Explain why the `balance` variable is not being updated correctly.
3. Modify the code to fix the scope issue.


2.  Nonlocal
Write a Python program that demonstrates the use of the `nonlocal` keyword.
Define an enclosing scope with variable `x` and a local scope with variable `x`.
Use the `nonlocal` keyword to modify the enclosing scope variable `x`.

"""
# def func_a():
#     x = 0

#     def func_b():
#         nonlocal x
#         x = 1

#     func_b()

# balance = 1000

# def deposit(amount):
#     global balance
#     balance += amount
#     print(f"Deposited ${amount}. Current balance: ${balance}")

# def withdraw(amount):
#     global balance
#     balance -= amount
#     print(f"Withdrew ${amount}. Current balance: ${balance}")

# DRY - Don't Repeat Yourself
# WET - We Enjoy Typing

# deposit(500)
# withdraw(200)
# import random as eyije_eyi_oje
# eyije_eyi_oje.shuffle()
# random.randint()
# randint()
# shuffle()

# Dunder: Double underscore


print(__name__)
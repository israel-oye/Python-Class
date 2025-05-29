# Scopes (In-Depth Pedagogical Note)

---

## **1. Understanding Scope**
**Scope** refers to the region of a program where a variable or function is accessible. Python uses scopes to manage the visibility and lifetime of identifiers (variables, functions, etc.). Variables defined inside a function are **local** and inaccessible outside it, while those defined at the top level are **global**.

### Example:
```python
def my_func():
    local_var = "I'm local"
    print(local_var)  # Accessible inside the function

my_func()
print(local_var)  # Error: NameError: name 'local_var' is not defined
```
**Output:**
```
I'm local
NameError: name 'local_var' is not defined
```
**Explanation:** `local_var` is only accessible within `my_func()`.

---

## **2. Introducing the LEGB Rule**
Python resolves variable names using the **LEGB** hierarchy:
- **L (Local):** Variables defined within a function.
- **E (Enclosing):** Variables in nested functions' outer scopes.
- **G (Global):** Variables at the top level of a module.
- **B (Built-in):** Predefined names (e.g., `print`, `len`).

### Example:
```python
x = "global"

def outer():
    y = "enclosing"
    def inner():
        z = "local"
        print(z)        # Local
        print(y)        # Enclosing
        print(x)        # Global
        print(len([1])) # Built-in (len)
    inner()

outer()
```
**Output:**
```
local
enclosing
global
1
```

---

## **3. Exploring Scopes in Detail**

### **Local Scope**
Variables declared inside a function are local. They are destroyed when the function exits.

```python
def greet():
    message = "Hello"  # Local variable
    print(message)

greet()        # Output: Hello
print(message) # Error: NameError
```

### **Enclosing Scope**
Variables in outer nested functions are accessible to inner functions.

```python
def outer():
    outer_var = "Outer"
    def inner():
        print(outer_var)  # Accesses enclosing scope
    inner()

outer()  # Output: Outer
```

### **Global Scope**
Variables declared outside functions/modules are global.

```python
global_var = "I'm global"

def access_global():
    print(global_var)  # Accesses global variable

access_global()  # Output: I'm global
```

### **Built-in Scope**
Predefined names like `str`, `list`, or `sum`.

```python
# Using built-in 'len'
print(len("Python"))  # Output: 6

# Shadowing a built-in
len = 5               # Overrides built-in 'len'
print(len)            # Output: 5
del len               # Restore built-in
print(len("Test"))    # Output: 4
```

---

## **4. Using the `global` Statement**
The `global` keyword allows modifying global variables inside a function.

### Example:
```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # Output: 1
```

### Pitfall Without `global`:
```python
counter = 0

def increment():
    counter = 100  # Creates a local variable; global unchanged
    print(counter)

increment()  # Output: 100
print(counter)  # Output: 0 (global unchanged)
```

---

## **5. Preventing Pitfalls**

### **1. Accidental Shadowing of Built-ins**
Redefining built-ins (e.g., `list`, `str`) can cause unexpected errors.

```python
list = [1, 2, 3]  # Shadows built-in 'list'

# Later in code:
a = list("abc")    # Error: TypeError (list is now a list, not a constructor)
```

### **2. Unintended Global Modifications**
Forgetting `global` can lead to bugs:
```python
total = 10

def calculate():
    total = 100   # Creates a local variable
    print(total)

calculate()  # Output: 100
print(total) # Output: 10 (global unchanged)
```

### **3. Variable Leakage in Loops**
Loop variables in Python are **not** confined to the loop block:
```python
for i in range(3):
    pass

print(i)  # Output: 2 (i exists in global scope)
```

---

## **Summary of Best Practices**
1. Use `global` and `nonlocal` sparingly.
2. Avoid shadowing built-in names.
3. Prefer function parameters and return values over global variables.
4. Use descriptive variable names to avoid conflicts.

By understanding LEGB scoping, you can write cleaner, more predictable Python code!



***

---

## **🔹 1️⃣ Local Scope (Inside a Function)**
A variable **declared inside a function** is local to that function and **cannot be accessed outside** of it.  

```python
def my_function():
    message = "Hello from inside the function!"
    print(message)  # ✅ Accessible inside

my_function()

print(message)  # ❌ Error: 'message' is not defined
```

🔹 **Key Takeaway:**  
- The variable `message` exists **only inside `my_function()`**.  
- Trying to access `message` outside the function causes an **error**.  

---

## **🔹 2️⃣ Enclosing Scope (Nested Functions)**
When a function is defined **inside another function**, the inner function can access variables from the outer function.  

```python
def outer_function():
    outer_var = "I'm from outer function"

    def inner_function():
        print(outer_var)  # ✅ Accessible inside the inner function

    inner_function()

outer_function()
```

🔹 **Key Takeaway:**  
- `inner_function()` **can access** `outer_var`, but `outer_var` is **not global**.  
- This is known as the **enclosing scope**.  

---

## **🔹 3️⃣ Global Scope (Accessible Everywhere)**
A variable **declared outside any function** is **global** and can be accessed **anywhere** in the program.  

```python
global_var = "I am global"

def show_variable():
    print(global_var)  # ✅ Accessible inside the function

show_variable()
print(global_var)  # ✅ Accessible outside the function
```

🔹 **Key Takeaway:**  
- `global_var` is accessible **both inside and outside functions**.  
- It exists throughout the entire script.  

---

## **🔹 4️⃣ Built-in Scope (Python’s Reserved Names)**
Python provides built-in functions like `print()`, `len()`, and `sum()`, which are **always available**.  

```python
print(len([1, 2, 3]))  # ✅ Uses built-in 'len' function
```

🔹 **Key Takeaway:**  
- Built-in functions **should not be overridden** by user-defined variables.  
- ❌ Avoid naming variables like `sum`, `list`, or `print`.  

---

## **🔹 The `global` Keyword**
If you try to **modify a global variable** inside a function, Python treats it as **a new local variable** unless explicitly declared as `global`.  

### **Without `global` (Causes Error)**
```python
counter = 10  # Global variable

def increase():
    counter += 1  # ❌ Error: 'counter' is treated as a new local variable
    print(counter)

increase()
```
🔹 **Python raises an error** because it assumes `counter` inside `increase()` is a **new local variable**, not the global one.  

---

### **With `global` (Correct Approach)**
```python
counter = 10  # Global variable

def increase():
    global counter  # ✅ Declares that we're using the global variable
    counter += 1
    print(counter)

increase()  # Output: 11
print(counter)  # Output: 11
```

🔹 **Key Takeaway:**  
- Use `global` when **modifying** a global variable inside a function.  
- Avoid excessive use of `global`, as it makes code harder to debug.  

---

## **🔹 The `nonlocal` Keyword**
When modifying a variable from an **enclosing function (not global)** inside a nested function, use `nonlocal`.  

```python
def outer():
    x = 5  # Enclosing variable

    def inner():
        nonlocal x  # ✅ Modifies 'x' from outer function
        x += 1
        print(x)  # Output: 6

    inner()
    print(x)  # Output: 6

outer()
```

🔹 **Key Takeaway:**  
- `nonlocal` allows modification of variables from an **enclosing function**.  
- Useful for **nested functions** that need to modify outer variables.  

---

## **🔹 Exercises (Increasing Difficulty)**  

### **1️⃣ Local vs. Global**
📌 **Task:**  
- Create a global variable `count = 0`.  
- Write a function that prints `count`.  
- Call the function **without modifying `count`**.  

🛠 **Assignment:** Modify the function to **increase `count` inside** using `global`.  

---

### **2️⃣ Nested Function Scope**  
📌 **Task:**  
- Write a function `outer()` that defines a variable `x = 10`.  
- Inside `outer()`, define another function `inner()` that prints `x`.  
- Call `inner()` inside `outer()` and call `outer()` outside.  

🛠 **Assignment:** Modify `inner()` to **increase `x` by 5** using `nonlocal`.  

---

### **3️⃣ Using Global Variables Properly**  
📌 **Task:**  
- Define a global list `fruits = ["apple", "banana"]`.  
- Write a function `add_fruit(fruit)` that **adds a new fruit** to `fruits`.  

🛠 **Assignment:** Modify the function to **prevent modifying `fruits` directly**, returning a new list instead.  

---

### **4️⃣ Avoiding Variable Name Conflicts**  
📌 **Task:**  
- Write a function that defines a local variable `sum = 100`.  
- Inside the function, try to use the built-in `sum()` function.  
- Observe what happens.  

🛠 **Assignment:** Rename the local variable to avoid conflicts and make it work correctly.  

---

### **5️⃣ Scope Challenge – Guess the Output**  
📌 **Task:**  
What will this program print?  

```python
x = 10

def outer():
    x = 20
    def inner():
        global x
        x = 30
    inner()
    print(x)

outer()
print(x)
```

🔹 **Think:**  
- What is the scope of each `x`?  
- What does `global x` do?  
- Why does `print(x)` outside `outer()` print `30`?  




Below is a short, beginner-friendly pedagogical note covering **recursion** and **decorators** in Python. Each section includes clear explanations, illustrative code examples, and a few exercises to practice the concept.

---

## **A. Recursion in Python**

### **What Is Recursion?**
Recursion is a programming technique where a function **calls itself** to solve a problem. The idea is to break a problem into smaller instances until you reach a **base case**—a situation where the answer is obvious and no further recursion is needed.

### **Key Concepts:**
- **Base Case:** The condition where recursion stops. Without it, the function would call itself indefinitely.
- **Recursive Case:** The part of the function where it calls itself with a modified parameter.

### **Example: Factorial Function**
The factorial of a number `n` (written as `n!`) is the product of all positive integers up to `n`. For instance, `5! = 5 * 4 * 3 * 2 * 1 = 120`.

```python
def factorial(n):
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Testing the function
print(factorial(5))  # Output: 120
```

### **Another Example: Fibonacci Sequence**
The Fibonacci sequence is a series where each number is the sum of the two preceding ones. For example, `fib(1) = 1`, `fib(2) = 1`, and for n > 2, `fib(n) = fib(n-1) + fib(n-2)`.

```python
def fibonacci(n):
    # Base cases: first two Fibonacci numbers
    if n == 1 or n == 2:
        return 1
    # Recursive call: sum of the two preceding Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the function
print(fibonacci(6))  # Output: 8 (Sequence: 1, 1, 2, 3, 5, 8)
```

### **Exercises for Recursion:**
1. **Sum of Numbers:** Write a recursive function that calculates the sum of all numbers from `1` to `n`.
2. **Power Function:** Create a recursive function to compute `a^b` (where `^` is exponentiation) for two numbers `a` and `b`.
3. **String Reversal:** Write a recursive function that reverses a given string.

---

# Comprehensive Pedagogical Guide on Higher-Order Functions

Higher-order functions play a significant role in Python programming by allowing functions to operate on other functions. This guide explores the concepts of higher-order functions—specifically `map()`, `filter()`, and `reduce()`—along with lambda expressions, all of which enable you to write concise, expressive, and efficient code.

---

## What Are Higher-Order Functions?

A **higher-order function** is a function that can accept other functions as arguments and/or return functions as its output. This concept encourages code modularity, reuse, and abstraction by allowing you to encapsulate behavior into functions that can be passed around.

### Why Use Higher-Order Functions?

- **Conciseness:** Reduce boilerplate by applying operations to collections in a streamlined manner.
- **Expressiveness:** Express intent more clearly using functions designed to manipulate data.
- **Reusability:** Write functions that can work with a variety of operations and data types.

---

## The `map()` Function

The `map()` function applies a given function to each item of an iterable (like a list or tuple) and returns a map object (which can be converted to a list or another iterable type).

### Syntax

python
map(function, iterable, ...)


- **`function`**: The function to apply to each item.
- **`iterable`**: One or more iterables whose items are passed to the function.

### When to Use `map()`

- When you want to transform each item in a collection.
- When the operation is stateless, i.e., it doesn’t depend on previously processed items.

### Example

```python
# Define a function to square numbers
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

You can achieve similar functionality using lambda expressions, which we discuss later.

---

## The `filter()` Function

The `filter()` function constructs an iterator from elements of an iterable for which a function returns True.

### Syntax

```python
filter(function, iterable)
```

- **`function`**: A function that tests each element in the iterable. It should return a Boolean value.
- **`iterable`**: The collection to filter.

### When to Use `filter()`

- When you want to select a subset of items from a collection based on a condition.
- When you need to remove items that do not meet specific criteria.

### Example

```python
# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

This can be streamlined using a lambda function for quick one-off tests.

---

## The `reduce()` Function

The `reduce()` function from the `functools` module applies a two-argument function cumulatively to the items of an iterable, reducing the iterable to a single cumulative value.

### Syntax

```python
from functools import reduce

reduce(function, iterable[, initializer])
```

- **`function`**: A function that takes two arguments. It applies this function cumulatively to the items of the iterable.
- **`iterable`**: The data to process.
- **`initializer`** (optional): A value that is used as the first argument to the function along with the first item from the iterable.

### When to Use `reduce()`

- When you want to compute a single value from a collection, such as the sum, product, or concatenation of elements.
- When the operation is associative, meaning that the grouping of operations does not affect the outcome.

### Example

```python
from functools import reduce

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print(product)  # Output: 120
```

Using an initializer can change the behavior slightly. For example, if you specify an initializer of 10:

```python
product_with_initializer = reduce(multiply, numbers, 10)
print(product_with_initializer)  # Output: 1200 (because 10 * 1 * 2 * 3 * 4 * 5)
```

---

## Lambda Expressions

Lambda expressions (or lambda functions) provide a succinct way to define small anonymous functions. They are particularly useful with higher-order functions like `map()`, `filter()`, and `reduce()`.

### Syntax

```python
lambda arguments: expression
```

- **`arguments`**: A comma-separated list of arguments.
- **`expression`**: A single expression evaluated and returned by the function.

### When to Use Lambda Functions

- When the function is simple and short.
- When a full function definition is unnecessary or would clutter your code.
- When passing a function as an argument to higher-order functions.

### Examples

**Using lambda with `map()`:**

```python
numbers = [1, 2, 3, 4, 5]
# Square each number using a lambda expression
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

**Using lambda with `filter()`:**

```python
# Filter even numbers using a lambda expression
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```

**Using lambda with `reduce()`:**

```python
from functools import reduce
# Calculate the sum using a lambda expression
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 15
```

---

## Integrating Higher-Order Functions and Lambdas in Practice

### Key Concepts to Remember

- **Immutability of Data:** Higher-order functions often work on immutable sequences to prevent side effects.
- **Conciseness vs. Clarity:** While lambda expressions make code concise, ensure that they don't compromise readability, especially when performing complex operations.
- **Modularity:** Using functions as first-class objects helps in writing modular and testable code.

### Practical Exercises

1. **Transformation Pipeline:**
   - Use `map()` to convert a list of temperatures (in Celsius) to Fahrenheit.
   - Use `filter()` to select only those temperatures that exceed a certain threshold.
   - Use `reduce()` to calculate the average of the filtered temperatures.

2. **Data Cleaning Task:**
   - Given a list of strings, use `map()` to trim whitespace.
   - Use `filter()` to remove any empty strings.
   - Use `reduce()` (or an alternative technique) to concatenate the strings into a single paragraph.

3. **Sorting with Lambdas:**
   - Create a list of tuples (each containing a student's name and grade).
   - Use the `sorted()` function with a lambda to sort the list by grade.

---


Higher-order functions such as `map()`, `filter()`, and `reduce()`—along with lambda expressions—unlock a powerful and expressive programming style in Python. They not only help in reducing boilerplate code but also encourage a more functional approach to problem solving. As you practice and incorporate these tools into your code, you'll find that they streamline data processing tasks and make your code more adaptable and readable.


-----
## **Understanding the `yield` Keyword in Python**

### **What Is `yield`?**
The `yield` keyword is used in **generators** — special functions that allow you to **pause and resume execution**. Instead of computing all the values at once and returning them (like `return`), a generator **yields values one at a time**, only when needed.

Think of `yield` as a **bookmark**: it saves the function's state at that moment, so when you resume (by calling `next()`), it continues right from where it left off.

### **Why Use `yield`?**
- Saves memory — doesn't build entire lists at once.
- Useful for working with **large datasets** or **infinite sequences**.
- Enables **lazy evaluation**: compute values only when needed.

---

### **Basic Example: Counting Numbers**
```python
def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1

counter = count_up_to(5)
for number in counter:
    print(number)
```

**What’s happening:**
- The function does **not** return all the numbers at once.
- Instead, it **pauses** at each `yield`, and `for` automatically calls `next()` to get the next number.
- Output:
  ```
  1
  2
  3
  4
  5
  ```

---

### **Comparison: `return` vs `yield`**
```python
def with_return():
    return [1, 2, 3]

def with_yield():
    yield 1
    yield 2
    yield 3

print(with_return())        # Output: [1, 2, 3]
print(list(with_yield()))   # Output: [1, 2, 3]
```

- `with_return` builds and returns the entire list.
- `with_yield` creates a generator object that produces values **one at a time**.

---

### **Under the Hood**
A function that contains `yield` becomes a **generator function**.
```python
def gen():
    yield "A"
    yield "B"

g = gen()
print(next(g))  # Output: A
print(next(g))  # Output: B
```

Once the function finishes, calling `next()` again raises `StopIteration`.

---

### **When to Use `yield`**
Use `yield` when:
- You're dealing with **large or unknown sequences**.
- You want to **improve performance** (memory or speed).
- You don’t need all the values at once.

---

### **Exercises**
1. **Even Number Generator**  
   Write a generator function that yields even numbers between 1 and 20.

2. **Word Splitter**  
   Create a function that takes a sentence and yields each word (without using `split()`).

3. **Infinite Counter**  
   Write a generator that counts up infinitely from 0. (Hint: Use `while True` and `yield`)

4. **Fibonacci Generator**  
   Write a generator that yields the first `n` Fibonacci numbers.

5. **Custom Range**  
   Create a function `my_range(start, stop, step)` that mimics Python's built-in `range()` using `yield`.

---
# Understanding Python Decorators

Decorators in Python provide a powerful design pattern that allows you to modify or extend the behavior of functions **without altering their original code**.

---

## What Is a Decorator?

A **decorator** is a special function that "wraps" another function, adding additional functionality before or after the original function runs. Essentially, decorators serve as wrappers that enhance or modify behavior without permanently changing the target function's code.



---

## Fundamental Concepts

Before diving into decorators, you should be comfortable with a few key concepts:

- **Defining Functions:** Creating functions using the `def` keyword.
- **Functions as First-Class Citizens:** In Python, functions are treated as objects. This means you can:
  - Assign them to variables.
  - Pass them as arguments to other functions.
  - Return them from other functions.

- **Higher-Order Functions:** Functions that accept other functions as arguments or return them.


**Example: Functions as First-Class Citizens**

```python
def greet():
    return "Hello!"

say_hello = greet
print(say_hello())  # Output: Hello!
```

---

## How Decorators Work

### Writing a Basic Decorator

A simple decorator is a function that takes another function as an argument, defines a nested wrapper function that adds extra functionality, and returns the wrapper. Consider the example below:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function runs.")
        func()
        print("Something is happening after the function runs.")
    return wrapper

def say_hello():
    print("Hello!")

# Applying the decorator manually
decorated = my_decorator(say_hello)
decorated()
```

### Cleaner Approach Using the `@` Syntax

The `@` syntax offers a neater and more intuitive way to apply decorators:

```python
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

This is functionally equivalent to writing:
```python
say_hello = my_decorator(say_hello)
```

### Decorators with Parameters

When the target function accepts arguments, the decorator’s inner function (wrapper) should handle them using `*args` and `**kwargs`:

```python
def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print(a / b)

divide(10, 2)  # Output: 5.0
divide(5, 0)   # Output: Cannot divide by zero!
```

---

## Practical Decorator Examples

### Simple Logging Decorator

This decorator logs the function call details and its result, helping with debugging and tracking function execution.

```python
def my_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting '{func.__name__}' with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished '{func.__name__}' with result {result}")
        return result
    return wrapper

@my_logger
def add(a, b):
    return a + b

print(add(3, 5))
```

### Timing Decorator

This example measures how long a function takes to execute:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute")
        return result
    return wrapper

@timer
def compute_sum(n):
    return sum(range(1, n + 1))

print(compute_sum(1000000))
```

---

## Real-World Applications of Decorators

Decorators are widely used in various domains such as:

- **Logging:** Tracking function calls and outputs.
- **Timing:** Measuring the performance of code blocks.
- **Authorization:** Checking user permissions before accessing certain functionalities.
- **Memoization:** Caching results of expensive computations.
- **Repeat Execution:** Re-running functions multiple times for reliability or testing.

---

## Exercises to Practice Decorators

1. **Basic Decorator:**  
   Write a decorator that prints `"Starting..."` before the function runs and `"Done."` after it completes.

2. **Uppercase Decorator:**  
   Create a decorator that transforms the output of a function returning a string into uppercase.

3. **Function Timer:**  
   Implement a decorator that uses the `time` module to print how long the decorated function takes to execute.

4. **Authentication Check:**  
   Write a decorator named `@login_required` that checks if a user is logged in (using a simple hardcoded variable) before allowing the function to run.

5. **Flexible Decorator:**  
   Modify any of the above decorators to handle functions with any number of positional and keyword arguments using `*args` and `**kwargs`.

6. **Repeat Execution:**  
   Create a decorator that runs the decorated function a predetermined number of times (e.g., 3 times) and returns the result of the last execution.

---

## Key Points to Remember

- **Decorators Enhance Functions:** They wrap functions to add additional functionality without modifying the original code.
- **Syntactic Sugar:** The `@decorator_name` syntax simplifies the application of decorators.
- **Practical Uses:** Beyond educational examples, decorators are essential in real-world applications such as web frameworks (Django, Flask), where they handle logging, authentication, routing, and caching.
- **Functional Programming Concepts:** Understanding functions as first-class citizens and the use of higher-order functions is crucial in mastering decorators.

---

## **Exception Handling in Python**

### **What is an Exception?**
An exception is an **error** that occurs while a program is running.

For example:
```python
print(10 / 0)
```
This will raise a **ZeroDivisionError**, and the program crashes.

Instead of letting the program crash, we can **handle the error** gracefully using exception handling.

---

### **Why Exception Handling is Important**
- Prevents the entire program from crashing due to one mistake.
- Makes your programs **robust** and **user-friendly**.
- Allows you to define **what to do when something goes wrong**.

---

### **Basic Syntax: `try`, `except`**
```python
try:
    # code that might raise an error
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
```

- `try`: where you place code that might cause an error.
- `except`: defines how to handle specific errors.
- You can have **multiple except blocks** to handle different types of errors.

---

### **Optional: `else` and `finally`**
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Input must be a number.")
else:
    print("Success! The result is:", result)
finally:
    print("This always runs, no matter what.")
```

- `else`: runs **only if no error occurs** in the try block.
- `finally`: runs **no matter what**, useful for cleaning up (like closing files).

---

### **Common Exceptions to Know**
| Exception | Reason |
|----------|--------|
| `ZeroDivisionError` | Division by 0 |
| `ValueError` | Wrong data type (e.g., int("hello")) |
| `IndexError` | List index out of range |
| `TypeError` | Incompatible operation (e.g., "2" + 5) |
| `FileNotFoundError` | File doesn’t exist |

---

### **Custom Error Messages**
```python
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)
```

- `raise` allows you to create your own error.
- You can also use `as` to refer to the error object and print custom messages.

---

### **Exercises**
1. **Division App**  
   Write a program that asks the user for two numbers and prints the result of dividing them. Handle:
   - ZeroDivisionError
   - ValueError

2. **List Index Checker**  
   Create a list of items and ask the user to pick an index. Handle:
   - IndexError
   - ValueError

3. **Safe Input**  
   Ask the user for their age and make sure it is a positive integer. Handle bad inputs and display appropriate messages.

4. **File Reader**  
   Write a function that asks for a filename and tries to open and read it. Handle:
   - FileNotFoundError
   - PermissionError

5. **Custom Exception**  
   Write a function `check_password(pw)` that raises a `ValueError` if the password is less than 6 characters. Catch and display a custom error message.

---

### **Wrap-Up Tips**
- Start with general `try/except`, then introduce specific errors.
- Use real-world examples (e.g., user input, file handling).
- Emphasize **graceful failure** — show that programs can keep running even when things go wrong.


---

# **Context Management in Python (Focused on File Handling)**

---

## **1. What is Context Management?**

**Context management** in Python refers to the proper handling of **resources** (like files, database connections, network sockets, etc.) that need setup and teardown (cleaning up).
This ensures that:

* Resources are properly **acquired and released**.
* Errors (exceptions) don't prevent cleanup.
* Code is **cleaner and easier to read**.

The main tool for context management is the **`with` statement**.

---

## **2. Why Use the `with` Statement for Files?**

When opening files, you must close them after use. Forgetting to close a file can lead to:

* **Memory leaks**
* **File corruption**
* **Locked files**

The `with` statement **automatically closes** the file, even if an error occurs.

---

### **Basic Syntax:**

```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
# File is automatically closed here
```

This is equivalent to:

```python
f = open("file.txt", "r")
try:
    content = f.read()
    print(content)
finally:
    f.close()
```

### **Exercise 1:**

Create a text file `hello.txt` with the content “Hello, world!”
Use a `with` block to read and print the file content.

---

## **3. Writing to a File Using `with`**

```python
with open("output.txt", "w") as f:
    f.write("This is a new file.\n")
    f.write("Second line.")
```

* `"w"` mode = write (overwrites file)
* Automatically closes the file after the block

### **Exercise 2:**

Write a program that creates a file called `student.txt` and writes the names of three students, one per line.

---

## **4. Appending to a File**

```python
with open("log.txt", "a") as f:
    f.write("Log entry 1\n")
```

* `"a"` mode = append (adds to existing content)

### **Exercise 3:**

Ask the user for a message, and append it to a file named `journal.txt`.

---

## **5. Reading Line by Line**

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

* `.strip()` removes newline and whitespace.

### **Exercise 4:**

Create a file `fruits.txt` with 5 fruit names.
Write code to read and print each fruit in uppercase.

---

## **6. Reading Lines into a List**

```python
with open("words.txt", "r") as f:
    lines = f.readlines()
print(lines)
```

* Returns all lines as a list

### **Exercise 5:**

Write a program that reads all lines from `poem.txt` and prints how many lines the poem has.

---

## **7. Writing Lists of Lines**

```python
lines = ["Python\n", "Java\n", "C++\n"]

with open("languages.txt", "w") as f:
    f.writelines(lines)
```

* `.writelines()` writes a list of strings.

### **Exercise 6:**

Create a list of 5 countries. Write them into `countries.txt`, one per line using `.writelines()`.

---

## **8. Using `with` for Temporary Files (advanced idea)**

The `tempfile` module is used for temporary files that are automatically deleted.

```python
import tempfile

with tempfile.TemporaryFile(mode="w+t") as temp:
    temp.write("Temporary data")
    temp.seek(0)
    print(temp.read())
```

This is more advanced but demonstrates the power of context management beyond basic files.

---

## **9. Best Practices**

* Always use `with` when working with files.
* Avoid manually calling `.close()`.
* Use `.strip()` when reading lines to avoid `\n`.
* For large files, read them line-by-line (avoid `.read()` all at once).

---

## **10. Common Mistakes to Avoid**

* Forgetting to open a file in the correct mode (`r`, `w`, `a`).
* Assuming `.read()` returns a list — it returns one big string.
* Forgetting to strip newline characters when printing lines.

---

## **11. Challenge Exercises**

1. **Reverse File Lines**
   Read a file `quotes.txt` and print its lines in reverse order.

2. **Line Numbering**
   Read `notes.txt` and print each line prefixed with its line number.

3. **Copy File Content**
   Write code to copy all content from `original.txt` to `backup.txt`.

4. **Word Counter**
   Count and print the number of words in `story.txt`.

5. **Filter Lines**
   Read `log.txt` and write only lines containing the word `"ERROR"` into `errors.txt`.

# Object-Oriented Programming (OOP) in Python

## Introduction

In real life, we often describe things by what they **are** and what they **can do**. For example, a car has wheels, an engine, and a color (what it is). It can drive, honk, and stop (what it can do).

**Object-Oriented Programming (OOP)** is a programming style that helps us write code the same way. Instead of just writing functions and variables randomly, we group related **data** and **behaviors** together in something called a **class**.

---

## 1. What is a Class?

A **class** is a blueprint or template for creating objects. It defines what kind of data (called **attributes**) and what kind of actions (called **methods**) the objects will have.

### Example:

```python
class Dog:
    pass
```

This defines an empty `Dog` class. Right now, it doesn't do anything. It just says: "Hey, a `Dog` exists as a concept."

---

## 2. What is an Object?

An **object** is an actual example (or **instance**) of a class. You can make many objects from a single class.

### Example:

```python
dog1 = Dog()
dog2 = Dog()
```

Now we have two dogs. They are **different objects**, but both follow the same structure from the `Dog` class.

---

## 3. Adding Attributes with a Constructor

A **constructor** is a special method used to initialize objects. In Python, it's called `__init__`.

### Example:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

* `self` refers to the current object.
* `name` and `breed` are **parameters** we pass when creating a dog.
* `self.name` and `self.breed` are the actual **attributes** of the object.

### Using the class:

```python
my_dog = Dog("Buddy", "Labrador")
print(my_dog.name)  # Output: Buddy
```

### Exercise:

1. Create a class `Cat` with attributes `name` and `color`.
2. Create two cat objects with different values.

---

## 4. Adding Methods (What an Object Can Do)

A **method** is a function defined inside a class.

### Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Max")
my_dog.bark()  # Output: Max says woof!
```

### Exercise:

1. Add a method `sleep` that prints a message.
2. Call both methods.
3. Create a class `Book` with `title` and `author`.
4. Initialize it using `__init__()` and print its data.

Instance methods are functions defined in a class that operate on instances. `self` refers to the instance itself. It must be the first parameter in instance methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
```

#### 🔁 Exercises

1. Add a method `rename()` that changes the dog's name.
2. Create multiple dogs and let them bark.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())
```

#### 🔁 Exercises

1. Create a `Rectangle` class with `width`, `height` and a method `area()`.
2. Add another method `perimeter()`.


---

## 5. Class vs Instance Attributes

A **class attribute** is shared by all objects. An **instance attribute** is unique to each object.

### Example:

```python
class Circle:
    pi = 3.14159  # class attribute

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):
        return Circle.pi * self.radius ** 2
```
```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute
```
### Exercise:

1. Create a class `Student` with a class attribute `school_name` and instance attributes `name` and `grade`.
2. Print out both kinds of attributes.
3. Add an `age` instance attribute and compare between dogs.
4. Access the class attribute using both `Dog.species` and `dog1.species`.

---

## 5b. Class Methods vs Static Methods in Python

In Python, beyond regular **instance methods**, you can define two other types of methods in a class:

* `@classmethod`
* `@staticmethod`

These methods **do not depend on an instance (`self`)** but serve different purposes.

---

### 🔹 Instance Method (Context)

An **instance method** is the most common type of method. It takes `self` as the first argument and operates on the instance:

```python
class MyClass:
    def instance_method(self):
        print("I am an instance method")
```

* Called via an object: `obj.instance_method()`
* Has access to instance data

Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

p = Person("Ada")
print(p.greet())  # Output: Hello, my name is Ada
```

---

### 🔸 Class Method

A **class method**:

* Is bound to the **class**, not the instance
* Uses `cls` as its first parameter
* Can access and modify class-level data
* Declared with the `@classmethod` decorator

```python
class MyClass:
    @classmethod
    def my_class_method(cls, args):
        pass
```

#### ✅ Use Cases

* Alternative constructors (factory methods)
* Tracking class-level data
* Modifying class variables

#### Examples

**Alternative Constructor:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(',')
        return cls(name, int(age))

p1 = Person.from_string("Alice,30")
print(p1.name)  # Alice
print(p1.age)   # 30
```

**Tracking Instances:**

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def total_students(cls):
        return cls.count

Student("A")
Student("B")
print(Student.total_students())  # 2
```

**Factory Method Example:**

```python
class Book:
    default_cover = "Soft"

    @classmethod
    def with_cover(cls, title):
        return cls(title, cls.default_cover)

    def __init__(self, title, cover):
        self.title = title
        self.cover = cover
```

---

### 🧠 Exercises for Class Methods

1. Create a `Book` class with a class variable `total_books` and a class method to return the count.
2. Define a class method `from_dict()` in a `Car` class that creates a `Car` instance from a dictionary.
3. Create a `Temperature` class with a class method to convert from Fahrenheit to Celsius.
4. Add a method to display how many objects have been created so far for a `Student` class.
5. Use `cls` to instantiate different subclasses from a parent class.

---

### 🔹 Static Method

A **static method**:

* Doesn't take `self` or `cls` as a parameter
* Cannot access or modify class or instance data
* Declared with `@staticmethod`
* Useful for logic related to the class but not dependent on class/instance data

```python
class MyClass:
    @staticmethod
    def my_static_method(args):
        pass
```

#### ✅ Use Cases

* Utility/helper functions
* Validation or standalone logic relevant to the class domain

#### Examples

**Utility Function:**

```python
class MathHelper:
    @staticmethod
    def add(x, y):
        return x + y

print(MathHelper.add(3, 4))  # 7
```

**Validation Logic:**

```python
class PasswordManager:
    @staticmethod
    def is_valid(password):
        return len(password) >= 8

print(PasswordManager.is_valid("secret"))     # False
print(PasswordManager.is_valid("secret123"))  # True
```

**Temperature Conversion:**

```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def is_valid_temp(c):
        return -273.15 <= c <= 1000

print(Temperature.celsius_to_fahrenheit(30))  # 86.0
print(Temperature.is_valid_temp(-500))        # False
```

---

### 🧠 Exercises for Static Methods

1. Create a `Validator` class with a static method to check if a string is a valid email (use `"@" in email` as the check).
2. Write a static method `is_even(number)` in a `NumberTools` class.
3. Create a `StringTools` class with a static method to check if a string is a palindrome.
4. Create a static method to convert km to miles in a class `Converter`.
5. Use both instance and static methods in the same class and compare their behaviors.

---

### 🧪 Combo Class Example: Circle

```python
class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)  # Instance method

    @classmethod
    def unit_circle(cls):
        return cls(1)  # Creates a Circle with radius 1

    @staticmethod
    def describe():
        return "A circle is a round shape."

c = Circle(2)
print(c.area())           # 12.5664

unit = Circle.unit_circle()
print(unit.radius)        # 1

print(Circle.describe())  # A circle is a round shape.
```

---

### 📝 Assignment: BankAccount Class

Create a `BankAccount` class with:

* A class variable `bank_name`
* An instance variable `balance`
* A class method `change_bank_name()` to update the shared bank name
* A static method `validate_account_number()` that returns `True` if the number is 10 digits
* A method `deposit()` to add funds

#### Example Usage:

```python
acc1 = BankAccount("1234567890", 500)
acc2 = BankAccount("0987654321", 300)

print(BankAccount.validate_account_number("1234567890"))  # True
BankAccount.change_bank_name("NewBank")
```

### 💡 Extra Examples

#### Tracking Instances

```python
class Employee:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        return f"Total employees: {cls.employee_count}"

e1 = Employee("Alice")
e2 = Employee("Bob")
print(Employee.total_employees())  # Total employees: 2
```

#### Static Email Validator

```python
class EmailValidator:
    @staticmethod
    def is_valid(email):
        return "@" in email and "." in email

print(EmailValidator.is_valid("user@example.com"))  # True
print(EmailValidator.is_valid("userexample.com"))   # False
```

#### Alternative Constructor

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def free_sample(cls, name):
        return cls(name, 0.0)

sample = Product.free_sample("Sample Soap")
print(sample.name, sample.price)  # Sample Soap 0.0
```

---

### 🧠 Final Exercises

#### Exercise 1: Static Utility Class

Create `MathTools` with:

* `square(n)` – returns `n` squared
* `is_even(n)` – checks if `n` is even

Use both methods **without creating an instance**.

#### Exercise 2: User Class with Class Method

Create a class `User` that:

* Takes `username` and `email` in `__init__`
* Has a class method `from_string(data)` that takes `"john,john@example.com"` and returns a `User` instance

```python
user_str = "john,john@example.com"
u = User.from_string(user_str)
print(u.username, u.email)
```

## 6. Encapsulation (Protecting Data)

You can hide data inside a class using **private attributes**.

### Example:

```python
class Safe:
    def __init__(self, code):
        self.__code = code  # private attribute

    def unlock(self, attempt):
        if attempt == self.__code:
            print("Unlocked")
        else:
            print("Wrong code")
```

### Exercise:

1. Create a class `Locker` with a private PIN.
2. Add a method `check_pin()` to verify access.



### 6b. Setters and Getters (Using Properties)

#### 🔍 What Are They?

Setters and Getters in Python are used to manage how private data (usually prefixed with `__`) is accessed or modified. While Python doesn’t enforce strict access controls, we use properties to control data safely and cleanly.

#### 📌 Example

```python
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            print("Invalid name")
```

**Usage:**

```python
p = Person("John")
print(p.name)     # John
p.name = "Mary"   # Mary
p.name = ""       # Invalid name
```

#### 🧪 Exercises

1. Create a `Car` class with a private `speed` that cannot be negative.
2. Implement a `Student` class with a `score` between 0 and 100.
3. Add getter and setter logic to validate the attributes.

---


## 7. Inheritance in Python

### 🧠 What Is Inheritance?

**Inheritance** allows one class (called the **child** or **subclass**) to inherit properties and methods from another (called the **parent** or **superclass**).

It helps to:

* Avoid code repetition
* Promote code reuse
* Establish logical relationships between classes

Python supports:

* Single Inheritance
* Multi-Level Inheritance
* Multiple Inheritance
* Method Overriding
* `super()` for parent method access

---

### 🔹 1. Single Inheritance

A subclass inherits from one superclass.

```python
class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

**Usage:**

```python
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog
```

---

### 🔹 2. Multi-Level Inheritance

A class inherits from a child class, forming a chain.

```python
class Animal:
    def move(self):
        print("Moves")

class Dog(Animal):
    def bark(self):
        print("Barks")

class Puppy(Dog):
    def weep(self):
        print("Weeps")
```

**Usage:**

```python
p = Puppy()
p.move()   # From Animal
p.bark()   # From Dog
p.weep()   # From Puppy
```

---

### 🔹 3. Multiple Inheritance

A class inherits from more than one parent class.

```python
class Father:
    def height(self):
        print("Tall")

class Mother:
    def eyes(self):
        print("Blue eyes")

class Child(Father, Mother):
    pass
```

**Usage:**

```python
c = Child()
c.height()
c.eyes()
```

---

#### 🧭 Method Resolution Order (MRO)

When multiple parents have overlapping methods, Python uses **MRO** to resolve conflicts.

```python
print(Child.__mro__)
```

This prints the order Python follows to search for methods.

---

### 🔹 4. Method Overriding

Child classes can **override** methods from the parent class to change behavior.

```python
class Animal:
    def speak(self):
        print("Generic sound")

class Cat(Animal):
    def speak(self):
        print("Meow")
```

**Usage:**

```python
c = Cat()
c.speak()  # Meow (overrides Animal's speak)
```

---

### 🔹 5. Using `super()` in Inheritance

#### 🧠 What Is `super()`?

The `super()` function is used to call methods or constructors from the parent class in a subclass. It's especially useful in:

* Calling the parent’s `__init__` method
* Extending parent methods without rewriting

> Promotes DRY principles and clean inheritance.

---

#### ✅ Example: Calling Parent Constructor

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal named {self.name} created")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"{self.name} is a {self.breed}")
```

**Usage:**

```python
dog = Dog("Buddy", "Golden Retriever")
```

---

#### ✅ Example: Extending Parent Method

```python
class Employee:
    def greet(self):
        print("Hello from Employee")

class Manager(Employee):
    def greet(self):
        super().greet()
        print("Hello from Manager")
```

**Usage:**

```python
m = Manager()
m.greet()
```

---

#### ✅ Example: Real-World Case — Bank Account

```python
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def display(self):
        print(f"Account Holder: {self.holder}, Balance: ${self.balance}")

class SavingsAccount(Account):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance)
        self.interest_rate = interest_rate

    def display(self):
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")
```

**Usage:**

```python
acc = SavingsAccount("Alice", 1000, 2.5)
acc.display()
```

---

#### ❗ Common Pitfalls with `super()`

1. Forgetting to call `super().__init__()` in subclasses.
2. Passing wrong or missing arguments.
3. Using `super()` in a class with no parent class.

---

### 📝 Practice Exercises

1. Create a `Vehicle` class with a method `start()`.
2. Create a `Car` class that inherits from `Vehicle` and adds a `fuel_type` attribute.
3. Use `super()` in the `Car` constructor to initialize the parent’s `brand` attribute.

---

4. Create a `Person` class with `name` and `age` attributes.
5. Inherit `Teacher` and `Student` classes.

   * `Teacher` should add `subject`.
   * `Student` should add `grade`.
6. Override `introduce()` in both subclasses.
7. Use `super()` to call the base version and extend it.

---

8. Create a `Laptop` base class with method `specs()`.
9. Inherit `GamingLaptop`, and override `specs()` to include GPU info. Use `super().specs()` in the override.

---

### 🧑‍💻 Assignment Project: Library System

Create a mini system using inheritance and `super()`.

#### 🔹 Base Class: `LibraryItem`

* Attributes: `title`, `author`
* Method: `show_info()`

#### 🔹 Subclasses:

* `Book`: Adds `pages`
* `Magazine`: Adds `issue_number`

✅ Use `super()` in constructors and `show_info()` to avoid code repetition.

---

### ✅ Key Takeaways

* Inheritance allows reusability and structured class design.
* `super()` enables cleaner, DRY code when extending behavior.
* Understanding `MRO` is critical in multiple inheritance scenarios.
* Method overriding gives flexibility to customize inherited behavior.

---

## 8. Polymorphism

### 🔍 What Is It?

Polymorphism allows different classes to be treated **as if** they’re the same, provided they implement a common interface or method.
---

### a. Duck Typing (If it quacks like a duck…)

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def make_sound(animal):
    animal.speak()
```

```python
make_sound(Dog())
make_sound(Cat())
```

---

### b. Built-in Polymorphism

```python
print(len("Hello"))     # 5
print(len([1, 2, 3]))   # 3
```

The same function `len()` works for different types.

---

### c. Polymorphism via Inheritance

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 2 * 2

class Square(Shape):
    def area(self):
        return 4 * 4
```

```python
shapes = [Circle(), Square()]
for s in shapes:
    print(s.area())
```

---

### 🧪 Exercises

1. Create a class `Bird` with `fly()` method.
2. Implement it in `Sparrow`, `Penguin`.
3. Override `fly()` such that `Penguin` says “Cannot fly”.
4. Create a `Staff` base class and override `work()` in `Manager`, `Intern`.
---


## 9. Abstraction in Python OOP

---

### 🔹 What is Abstraction?

**Abstraction** is one of the four fundamental principles of Object-Oriented Programming (OOP), alongside **Encapsulation**, **Inheritance**, and **Polymorphism**.

> **Abstraction** means *hiding internal implementation details and showing only the essential features* to the user.

Think of a **TV remote**—you don’t need to know the internal circuitry to use it. You press a button, and it works. That’s abstraction.

---

### 🔹 Why Use Abstraction?

* Keeps code **clean and manageable**
* Promotes **modular design**
* Makes code **easier to understand**
* Encourages **reusability** and **extendability**

---

### 🔹 How is Abstraction Achieved in Python?

Python provides abstraction through the **`abc` module** (Abstract Base Classes):

* An **abstract class** cannot be instantiated directly.
* An abstract class contains one or more **abstract methods**.
* Abstract methods are declared but **not implemented** in the abstract class.
* Any class inheriting from an abstract class **must implement** the abstract methods.

---

#### 📦 Syntax (Using `abc` module):

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
```

---

### ✅ Example 1: Basic Abstract Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

d = Dog()
print(d.sound())  # Bark
```

🧠 **Explanation**:

* `Animal` is an abstract class.
* It defines an abstract method `sound()` with no implementation.
* `Dog` and `Cat` are concrete subclasses that must implement `sound()`.

---

#### 🧪 Exercise 1:

Create an abstract class `Vehicle` with an abstract method `move()`. Create two subclasses `Car` and `Bicycle` and implement the `move()` method in both.

---

### ✅ Example 2: Multiple Abstract Methods

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def authorize(self):
        print("Authorizing credit card...")

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

cc = CreditCard()
cc.authorize()
cc.pay(100)
```

🧠 **Explanation**:

* `Payment` enforces a blueprint for all types of payments.
* Each subclass must provide its own logic for authorization and payment.

---

#### Exercise 2:

Create an abstract class `Shape` with abstract methods `area()` and `perimeter()`. Create `Rectangle` and `Circle` classes that implement both.

---

### Example 3: Abstract Class with Constructor and Concrete Method

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return 70000

dev = Developer("Alice")
dev.greet()                    # Hello, I'm Alice
print(dev.calculate_salary())  # 70000
```

**Explanation**:

* Abstract classes can have constructors and concrete methods.
* `calculate_salary()` must be implemented in all subclasses.

---

#### Exercise 3:

Create an abstract class `Appliance` with a constructor for `brand` and a concrete method `turn_on()`. Include an abstract method `operate()`. Create subclasses `WashingMachine` and `Microwave`.

---

### Assignment Task

#### Task: Employee Payroll System

Build an employee system with the following:

1. **Abstract class**: `Employee`

   * Fields: `name`, `department`
   * Abstract method: `calculate_salary()`
   * Concrete method: `get_details()` – returns name and department

2. **Subclasses**:

   * `FullTimeEmployee` – fixed salary
   * `PartTimeEmployee` – hourly wage × hours worked

3. Create instances of each employee type and display their details and salary.

#### Bonus:

* Add a class method in `Employee` to keep track of the number of employees created.
---


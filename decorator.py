# def decorator(func):
#     def wrapper():
#         print("Before function runs....")
#         func()
#         print("After function runs")
#     return wrapper


# @decorator
# def greet():
#     print("Hello world")

# def describe():
#     print("I am me")

# greet()
# @timer
def say_hello():
    print("Hello world")

so_hello = say_hello
# so_hello() #functions as first class citizens
# say_hello()


# decorator(greet)
# decorator(describe)

# decorated_greet = decorator(greet)
# decorated_greet()
def decorator(func):
    def wrapper():
        print("Before function")
        for _ in range(3):
            func()
        print("After function")
    return wrapper

@decorator
def french_greeting():
    print("Bonjour")

# wrapped = decorator(french_greeting)
# wrapped()

# french_greeting()
# french_greeting('Ẹnlẹ o, araye!')

# map(french_greeting, [])
# returned_wrapper = decorator(french_greeting)
# returned_wrapper()

name = ''

person = name

new_func = french_greeting
# new_func() #functions as first-class citizens


returned_wrapper = decorator(french_greeting)
# returned_wrapper()

# Syntactic sugar
# import time

# # raw list
# hundred_thousand_nums = list(range(100000))

# initial_time = time.time()

# for i in hundred_thousand_nums:
#     i + 1

# time_difference = time.time() - initial_time
# print(f"Raw list: {time_difference}")

# # Range
# initial_time2 = time.time()

# for i in range(100000):
#    i + 1

# time_difference2 = time.time() - initial_time2
# print(f"Range: {time_difference2}")

def timer(func):
    def wrapper(*args, **kwargs):
        import time
        initial_time = time.time()
        result = func(*args, **kwargs)
        time_taken = time.time() - initial_time
        print(f"Function executed with code 0. Took {time_taken} seconds to run")
        return result
    return wrapper

# @timer
def say_hello(person):
    print(f"Hello {person}")

# say_hello()
# timed_say_hello = timer(say_hello)
# timed_say_hello('Sogo')
# @timer
def add(*operands):
    return sum(operands)

wrapped_add = timer(add)
# print(wrapped_add(2, 5))

# add(1000, 10, 5, 3, 2)
# add(2, 3)
# timed_printer = timer(add)
# result = timed_printer(1000, 2000)


# print_a_million()

"""
**Basic Decorator:**  
   Write a decorator that prints `"Starting..."`
    before the function runs and `"Done."` after it completes.
"""

"""
1. **Uppercase Decorator:**
   Create a decorator that transforms the output of a function
   returning a string into uppercase.
2. **Repeat Execution:**  
   Create a decorator that runs the decorated function a
   predetermined number of times (e.g., 3 times) and returns
   the result of the last execution.
"""

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@upper
def name_setter(name):
    return name

@upper
def text_getter(text):
    return text

# print(name_setter('Giorgio'))
# print(text_getter('Lorem ipsum dolor sit amet'))

def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat(1)
def greet_room():
    print('Hello, room')

# greet_room()

# decorated = repeat(5)
# wrapped = decorated(greet_room)
# wrapped()

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            time.sleep(seconds)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@delay(5)
def add_nums(*args):
    return sum(args) #sum((2, 3))

# print(add_nums(1, 2, 3))
# print(add_nums(2, 4))

def withdraw(func):
    def wrapper(*args, **kwargs):
        balance = func(*args, **kwargs)
        if balance <= 1000:
            print("Insufficient funds ❌")
        else:
            print(f"Withdrawing...₦{balance}...")
    return wrapper

@withdraw
def get_balance(bal):
    return bal

# get_balance(1001)

import time
def is_admin(func):
    def wrapper(user):
        if user == 'admin':
            func(user)
        else:
            print("You're not authorized ❌")        
    return wrapper

@is_admin
def delete_records(user):
    print(f"Deleting records of {user}...")
    time.sleep(1.5)

@is_admin
def modify_user(user):
    print(f'Modifying {user} settings')
    time.sleep(1.5)


def message_user(user):
    print(f"Message sent to {user}")


delete_records('fola')
modify_user('admin')
message_user('Admin')

"""
1. Block on Negative Numbers
    Write a decorator @no_negatives that blocks
    the function if the first argument is negative
    e.g 
    @no_negatives
    def square(num):
        return num * num
2. Block if Underage
    Write a decorator @min_age that only runs the function
    if the min_age is exceeded i.e
    @min_age(19)
    def buy_ticket(qge):
          print("Ticket purchased")
"""
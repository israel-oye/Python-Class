# numbers.append()

# def say_hello(person: str, language):
#     if language.lower() == 'english':
#         print(f"Hello {person}. You are welcome")
#     elif language.lower() == 'yoruba':
#         print(f"Ẹnlẹ o, {person}. E kaabo")

# text = "Glory"
# text.lower()
    

# # say_hello('Morty', 'ENGlish')

# # print()

# def get_title_case(text: str):
#     return text.title()

# name_title_case = get_title_case('toluwanimi')
# titled_text = get_title_case('Harry')
# print(get_title_case('jurrasic park'))

# numbers = list(range(3, 50))

# def calculate_sum(list_of_nums):
#     sum_ = 0

#     for 

"""
def name_of_your_fucntion():
    body of your function
"""



def say_hello(name, country, language='English'):
    
    print( f"Hello {name} from {country}. You speak {language}")

# say_hello(name='Chen', country='Taiwan', language='Mandarin')
# say_hello('Ousmane', 'Mali')
# say_hello('Ghana', 'Ayew')

# say_hello('Muller', 'Germany', 'Dutch')

# say_hello(name='Huey', country='Canada')
# say_hello(language='French', name='Huey', country='Canada')
# say_hello('Huey', 'Canada', 'French')

# def formatted_name(first_name, last_name, middle_name=''):
#     print(f"Hello {first_name.title()} {middle_name.title()} {last_name.title()}")

# formatted_name('DWAYNE', 'olorunsogo')

def my_func():
    return True

def subtract(a, b):
    result = a - b
    print(result)

# subtract(2, 5)
# subtract(b=5, a=2)

def another_func():
    a = 1 + 2

# print(another_func())

# print(subtract())

# result = subtract(500, 200)
# print(result)

# print(subtract(4, 2))

# print(say_hello('Melchi', 'Israel', 'Hebrew'))

# input()

# print(f"5 minus 2 is {subtract(5, 2)}")

def sum_of_collection(collection):
    total = 0

    for num in collection:
        total += num
    print(total)


numbers = list(range(1, 5)) #[1, 2, 3, 4]

# sum_of_collection(collection=[2, 3])

# Write a function that takes a list as an argument and prints the biggest
# And smallest numbers in the list

"""
    -   Write a function called make_album() that builds a dictionary
        describing a music album.
    -   The function should take in an artist name and an album title,
        and it should return a dictionary containing these two pieces of
        information
    -   Use the function to make three dictionaries representing different albums 
    -   Print each return value to show that the dictionaries are storing the
        album information correctly
    -   Add an optional parameter to make_album() that allows you to store the
        number of tracks on an album
"""
def make_album(artist, album_title, tracks=0):
    return {'artist': artist, 'album_title': album_title, 'total_tracks': tracks}

# print(make_album('Evergreen', 'Chief Obey', 5))

def get_maximum(collection_of_num):
    max_num = 0

    for num in collection_of_num:
        if num > max_num:
            max_num = num
    print(max_num)

# get_maximum(collection_of_num=(4, 9, 20, 1, 2))

def print_numbers(*numbers):
    print(numbers)

print_numbers(1, 2, 3, 4)
print_numbers(2, 6)

def person_info(name, **extra_details):
    print(f'Name: {name}\nExtra details: {extra_details}')
    
person_info('Farouq', bal=122222222, height=1.85, skin_color='dark', age=2, nationality='Brazilian')
person_info('Babalawo', occupation='Doctor', state_of_origin='Kwara')


"""
Cars: Write a function that stores information about a car in a dictionary
- The function should ALWAYS receive a manufacturer and a model name
- It should then accept an ARBITRARY number of keyword arguments
- Call the function with the required information and two other name-value pairs,
    such as a color or an optional feature.
- Your function should work for a call like this one:
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that's returned to make sure all the information was stored correctly
"""

def make_car(manufacturer, model_name, **extra_details):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model_name

    for key, value in extra_details.items():
        car_info[key] = value
    print(car_info)

# make_car('Toyota', 'Corolla', color='blue', steering='left', is_suv=False)


#docstrings, lambdas, random.choice, scopes, modules/packages

# def generate_random_list(size_of_list: int, max_num: int):
#     import random
#     random_list = []
#     for _ in range(size_of_list):
#         random_list.append(random.randint(0, max_num))
#     return random_list

# print(generate_random_list(5, 10))

"""
Create a function that generates a random list of numbers.

The function should take two parameters: size of list and max number.


Hint: Use `random.randint()` inside a loop.
"""

def generate_random_list(size_of_list: int, max_num: int):
    import random
    random_list = []

    for _ in range(size_of_list):
        random_num = random.randint(0, max_num)
        random_list.append(random_num)
    return random_list

# print(generate_random_list(5, 35))

import string
import random

# print(string.ascii_uppercase)

# print(random.choice(string.ascii_letters))

# random_chars = []
# for _ in range(5):
#     random_pool = string.ascii_letters + string.digits + string.punctuation
#     random_char = random.choice(random_pool)
#     random_chars.append(random_char)

# random_word = "".join(random_chars)
# print(random_word)

# Modify the code above to create a password generator function that takes the length
# of the random-characters-to-generate as a parameter


# Assignment: Modify the code below to generate at least a certain number of letters,
# and a certain number of symbols

def generate_password(length: int):
    """
    This function generates a random sequece of characters including
    - Alphabets
    - Digits
    - Special symbols
    docstring
    """


    import random, string
    
    random_list = []
    random_pool = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length):
        random_char = random.choice(random_pool)
        random_list.append(random_char)
    
    password = "".join(random_list)
    return password
    
# print(generate_password(length=10))


# lambda param : result_to_return

square = lambda num : num ** 2

def square_2(num):
    return num ** 2

# print(square(5))

# vowel_counter('aeiou') => 5
# Write a function that returns the number of vowels in a string
# Hints: Convert the word to lowercase
#        Add a counter variable
#        loop through the string
#        Use a conditional to check each character and increment the counter if
#       the condition is matched

def vowel_counter(word: str) -> int:
    word = word.lower()
    count = 0

    for char in word:
        if char in "aeiou":
            count += 1
    return count

# word = input("Enter a word: ")
# print(f"There are {vowel_counter(word)} vowels in {word}")

# Recursion
# 5! = 5*4*3*2*1

def factorial(num: int):
    if num == 1:
        return 1
    return num * factorial(num - 1)

# Write a recursive function that calculates the power of a number n
# e.g power(n, m) => n ^ m => n * n ^ (m-1)

def power(n: int, m: int):
    if m == 0:
        return 1
    return n * power(n, m-1)

# print(type(power))
# print(id(power))
# memoization

# Higher Order Functions

def calculator(operator, *operands: int): #Higher Order Function
    return operator(*operands)

def add(x, y):
    return x + y

def modulo(x: int, y: int):
    return x % y


print(calculator(add, 1, 2))
print(calculator(modulo, 2, 2))

# Filter
def cube(num):
    return num ** 3
numbers = list(range(0, 11))
numbers__cubes = list(map(cube, numbers))


def title_case(text: str) -> str:
    return text.title()
names = ['dopesi', 'oluwo', 'tinubu']
# print(list(map(title_case, names)))

# Filter
def is_odd(num):
    return True if num % 2 == 1 else False #Ternary statement

# print(list(filter(is_odd, numbers)))

heights_in_m = [1.55, 1.88, 1.92, 1.75]
# Transform the list of numbers above to heights_in_cm using map()

def to_cm(value):
    return value * 100

heights_in_cm = list(map(to_cm, heights_in_m))
# print(heights_in_cm)

from functools import reduce

# print(reduce(add, [2, 5]))


# Lambda is an anonymous (often one-line) function.
square = lambda x : x ** 2

square(2)

"""
1. A recursive function that generates a sum of numbers before it
    i.e add_sum(3) => 3+2+1
2. **Transformation Pipeline:**
   - Use `map()` to convert a list of temperatures (in Celsius) to Fahrenheit.
   - Use `filter()` to select only those temperatures that exceed a certain threshold.
   - Use `reduce()` to calculate the average of the filtered temperatures.

2. **Data Cleaning Task:**
   - Given a list of strings, use `map()` to trim whitespace.
   - Use `filter()` to remove any empty strings.
   - Use `reduce()` (or an alternative technique) to concatenate the strings into a single paragraph.

"""

temps_in_celsius = [random.randint(20, 45) for _ in range(5)]

def to_fahrenheit(temp_in_c: float):
    temp_in_f = (temp_in_c * (9 / 5)) + 32
    
    return round(temp_in_f, 2)

temps_in_fahrenheit = list(map(to_fahrenheit, temps_in_celsius))
# temps_in_fahrenheit = list(map(lambda celsius: celsius * (9/5) + 32, temps_in_celsius))

# print(temps_in_celsius, temps_in_fahrenheit, sep='\n')

def normal_temp(temp):
    if 97.7 <= temp <= 99.5:
        return True
    return False


normal_temps = list(filter(normal_temp, temps_in_fahrenheit))
# print(normal_temps)

def average(*items):
    return sum(items) / len(items)

average_temp = reduce(average, temps_in_fahrenheit)
# print(average_temp)

list_of_strings = [
    ' Ada is a girl     ',
    ' Bob came here   ',
    '    Cyle XY',
    '\tDada Estate',
    '',
    'Erinle means elephant\n',
    '\n\n',
    ]

stripped_strings = list(map(str.strip, list_of_strings))
stripped_strings = list(map(lambda string: string.strip(), list_of_strings))

# print(stripped_strings)

def is_not_empty(string):
    if string:
        return True
    return False
    return True if string else False

is_not_empty('Toriola')


non_empty_strings = list(filter(is_not_empty, stripped_strings))
# non_empty_strings = list(filter(lambda string: bool(string), stripped_strings))
# print(non_empty_strings)

# use reduce to concatenate the list of non_empty_strings
# from functools import reduce

students_data = [
    ('Yomi', 56, True),
    ('Ayo', 78, False),
    ('Abayomi', 85, True),
    ('Bayo', 80, True),
]


def get_score(details: tuple):
    return details[1]

get_score(('Bobo', 99))

# sorted_students = sorted(students_data, key=get_score)
sorted_students = sorted(students_data, key=lambda details: details[-1])
# print(sorted_students)

def normal_func(stuff):
    return stuff
    return "another stuff"

def n_generator():
    yield "stuff"
    yield "another stuff"

gen = n_generator()
print(next(gen))
print(next(gen))






# Map, filter, reduce

nums = [1, 2, 3, 4, 5, 6]

def doubler(x):
    return x * 2

def to_upper(text):
    return text.upper()

friends = ['Bobo', 'Emeka', 'Biyi']

upper_friends = list(map(to_upper, friends))

distances_km = [1.4, 2.5, 10, 4]
# using map convert the distances_km list above to an equivalent list in m
# hint: create a function that converts any given value to meters.

doubled_nums = list(map(doubler, nums))
doubled_nums = list(map(lambda x: x * 2, nums))

# print(doubled_nums)

def is_even(x):
    if x % 2 == 0:
        return True
    return False

even_nums = list(filter(is_even, nums))

# "baba".startswith('a')
# Using filter, create a list of strings that only start with the letter 'a'
# hint: use str.startswith() to check

from functools import reduce

def subtract(a, b):
    return a - b

difference = reduce(subtract, [4, 2, 1, 0])

# print(difference)


def add_10_to(x):
    return x + 10

add_10_to(5)

add_20_to = lambda num: num + 20

summer = lambda x, y: x + y

map(lambda text: text.lower(), ['ada', 'lovelace', 'rita'])
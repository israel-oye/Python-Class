# A Boolean data type represents binary value OR True/False values
True
False
'False'

#Type Hinting
# farouq_is_tired: str = 'jdjddjjdjd'
# num: float = 20.67
# print(type(farouq_is_tired))

tired_status = True
# print(f"It is {tired_status} that I am tired.")

#Comparison Operators
# >, <, ==, !=, >=, <=
my_num = 13

# print(my_num != 10 )

num_is_even = my_num % 2 == 0
# print(int('12') == 12)

a = 1
b = 2

# print(f"Before swap: {a, b}")
#a = 2
#b = 1
x = a # x = 1
a = b # a = 2
b = x # b = 1

# print(f"After swap: {a, b}")

a, b = b, a
# print(f"Swap again with shortcut: {a, b}")

#TRUTHY AND FALSEY values
"""
An empty string, None type, and a 0 integer or float are FALSEY values i.e bool(such)= False
Otherwise, bool(such) evaluates to True. TRUTHY values.
"""
var = None
var_in_bool = bool(var)
# print(var_in_bool)


# print(bool(True) == bool(' '))

"""
Pseudocode

if condition-is-true:
    do something;
else (when condition is not true):
    do something else;

"""
# Indentation


# if 'a' == 'A'.lower():
#     print("It's true")
# else:
#     print("Condition is false")

# user_input = int(input("Enter a number: "))
# if user_input % 2 != 0:
#     print(f"{user_input} is an odd number.")
# else:
#     print(f"{user_input} is an even number.")

"""
Assignment
Write a program that checks the age of a user,
And print a restriction message to them if they are not
adults i.e less than 18.
"""
# age = ''
# if age:
#     print("You are old enough")
# else:
#     print("Sorry, you are not eligible.")


# user_input = input("Please enter a text: ")

# if user_input != '' and int(user_input) > 18:
#     print(f"You are eligible")
# else:
#     print("Please enter a valid age.")

name = 'ABNDJderg'
#      True         and   (         False      or  False)    
# if name.islower() or name.startswith('b') or not name:
#     print("Condition is true")
# else:
#     print("Condition is false")

# if type(bool(name)) == bool:
#     print('Name is a boolean')
#     # name = bool(name)
#     print(type(name))

#Identity operator
my_name = 'Seyi'
name_copy = 'Seyi'
name_copy_2 = 'SEYI'

my_var = None

# print(id(my_name))
# print(id(name_copy_2))

# if name_copy is None:
#     print("Condition is true")

# user_age = int(input("Enter your age in digits: "))
# if not user_age <= 18:
#     print("You are eligible")
# else:
#     print("You are not eligible!")





"""
if condition_is_true:
    do sth;
elif another_condition_is_true:
    do sth;
elif another_condition_2_is_true:
    do sth else;
else:
    do sth else;
"""
#BMI formula = weight (kg) / height(m)^2
"""
Underweight. Less than 18.5.
Healthy Weight. 18.5 to less than 25.
Overweight. 25 to less than 30.
Obesity. 30 or greater.
"""

# user_weight = float(input("Enter your weight in lbs: ")) * 2.2
# user_height = float(input("Enter your height in ft: ")) / 3.28
# bmi = user_weight / (user_height ** 2)

# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 < bmi < 25:
#     print("You have healthy weight!")
# elif 25 <= bmi < 30:
#     print("You are overweight...")
# elif bmi >= 30:
#     print("You are obese.")
# else:
#     print("Invalid bmi.")
    
#Logical operators: and, or, not
#And: Both true -> True else false
#Or: Any condition is true -> True else false
#Not: Negates a value. e.g not True -> False and vice-versa

#Nested if statements.
#Nested: inside

# num = 10

# if num % 2 == 0:
#     if num % 5 == 0:
#         print("number is a multiple of 5")
#     else:
#         print("Number is not a multiple of five")
# else:
#     print("Number is not even")

# if num % 2 == 0 and num % 5 == 0:
#     print("Number is a multiple of 5")
# else:
#     print("Number is not even")


"""
Assignment:
Write a program that determines if a year input is a leap year.
Hint: A leap year is one that is divisible by 4 but it IS NOT if it is a century
e.g 1900, 2000 i.e It is not divisible by 100
"""




"""
Classwork
Alien Colors #1: Imagine an alien was just shot down in a game 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
•	 Write an if statement to test whether the alien’s color is green If it is, print
a message that the player just earned 5 points
•	 

Choose a color for an alien as you did above, and
write an if-else chain
•	 If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien
•	 If the alien’s color isn’t green, print a statement that the player just earned
10 points

Turn your if-else chain from the exercise above into an if-elif-else chain
•	 If the alien is green, print a message that the player earned 5 points
•	 If the alien is yellow, print a message that the player earned 10 points
•	 If the alien is red, print a message that the player earned 15 points

"""

#Correction
# alien_color = input("Guess the colour of the alien: ").lower()
# score = 0

# if alien_color == 'green':
#     score += 5
#     print(f"You just got {score} points")
# elif alien_color == 'yellow':
#     score += 10
#     print(f"You just earned {score} points")
# elif alien_color == 'red':
#     score += 15
#     print(f"You earned {score} points")
# else:
#     print(f"Alien of {alien_color} color doesn't exist\nYour score: {score}")

#Leap Year
# year = int(input("Enter year (in digits): "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         print('Year is NOT a leap year')
#     else:
#         print('Year is a leap year')
# else:
#     print('Year is NOT a leap year')
# year = 2025
# var2 = 34

# sentence = "This my variable {var_1}; Another var: {var_2}".format(var_1=67, var_2='Goodluck')
# print(sentence)

condition = False

# if condition:
#     print('Condition is true')
# else:
#     print("Condition is false")

# print("After the if statement")

for _ in range(3):
    if condition == True:
        print("Condition is true")
    print("Condition is false")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
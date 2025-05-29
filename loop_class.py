"""
for item in container:
    do something with each item;
"""

# meals = ['Rice', 'Spag', 'Amala', 'Rice', 'Pounded Yam', 'Beans']

# characters = list("Ibadan")
# print(characters)
# for char in characters:
#     print(f"{char.upper()}")

numbers = range(10)

# for num in range(10):
#     print(num)

"""
Animals: Think of at least three different animals that have a common characteristic
Store the names of these animals in a list, and then use a for loop to
print out the name of each animal
•	 Modify your program to print a statement about each animal, such as
A dog would make a great pet
"""


# animals = ['Dog', 'Cat', 'Goldfish']
# for animal in animals:
#     if animal == 'Cat':
#         print(f'My favorite pet is {animal}')
#     # print(f"A/An {animal} would make a great pet")

# list_of_numbers = [9, 1, -2, 0, -5, 2, 3, 7, -3, 4]

# if 'Z' not in 'Abracadabra':
#     print('a is in the string')

age_of_students = [99, 10, 24, 45, 16, 53, 40]

# for num in list_of_numbers:
#     if num > 0:
#         counter += 1
# print(counter)

# sum = 0

# for num in list_of_numbers:
#     sum += num

age_of_students = [99, 10, 24, 45, 16, 53, 40]
"""
average = sum of items / number of items
"""


sum = 0

for age in age_of_students:
    sum += age

average_age = sum / len(age_of_students)
# print(average_age)

my_list = [5, 4, 6]

max_num = my_list[0]

for num in my_list:
    if max_num < num:
        max_num = num
# print(max_num)

nouns = ["cat", "Mongolia", "mouse", "Solape", "computer", "Solape"]

# for noun in nouns:
#     if noun == 'Solape':
#         print(f'What did you add in your stew, {noun}')

# list_of_numbers = list(range(11))
# odd_numbers = []

# for num in range(11):
#     if num % 2 == 1:
#         odd_numbers.append(num)

# in, not in
even_numbers = list(range(0, 11, 2))

# if 'ab' in 'Abracadabra':
#     print('Condition is true')

# Collect a word from the user, and print all the vowels in the word

# user_input = input("Enter a word: ")

# user_entry = user_input.lower()

# vowel_count = 0

# for char in user_entry:
#     if char in "aeiou":
#         vowel_count += 1

# print(f"There are {vowel_count} vowels in {user_input}")

"""
1. Using a loop, find the minimum number in a list of integers

2. Cubes: A number raised to the third power is called a cube For example,
the cube of 2 is written as 2**3 in Python.

Using a loop, make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10)
"""


# int_list = [20, 10, 4, 2, 9, -4, 93]
# old_minimum = int_list[0]

# for num in int_list:
#     if num < old_minimum:
#         new_minimum = num
# print(new_minimum)

list_of_cubes = []
for i in range(1, 11):
    cube = i**2
    list_of_cubes.append(cube)

# print(list_of_cubes)

# 🔹 Multiplication table
# Looping through a slice

# word = "PYTHON"
# reversed_word = ""
# for letter in word:
#     reversed_word = letter + reversed_word
# print(reversed_word)


# Nested for loop
# for i in range(1, 4):
#     for j in range (1, 4):
#         print(f"{i} * {j} = {i*j}")


"""
Checking Usernames: Do the following to create a program that simulates how websites ensure that
everyone has a unique username
•	 Make a list of five or more usernames called current_users
•	 Make another list of five usernames called new_users Make sure one or
two of the new usernames are also in the current_users list
•	 Loop through the new_users list to see if each new username has already
been used.
If it has, print a message that the person will need to enter a
new username.
If a username has not been used, print a message saying
that the username is available
•	 Make sure your comparison is case insensitive If 'John' has been used,
'JOHN' should not be accepted
"""

# current_users = ['farouq4', 't0lu', 'ninja']

# new_users = ['t3ni', 'Ninja', 'l00kman', 'tijay_01']

# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(f"{new_user} exists. Please try another username")
#     else:
#         print(f'{new_user} is available')

word = "Aibohphobia"
reversed_word = ""
# reversed_word = word[::-1]
for char in word:

    reversed_word = char + reversed_word

# if word.lower() == reversed_word.lower():
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

"""
Multiplication table 1-3 printed side by side
"""

# for i in range(1, 13):
#     for j in range(1, 4):
#         print(f"{j} * {i} = {j*i}", end="\t")
#     print()

# for _ in range(2):
#     print("ab", end="\t")

# print("ab", end='x')
# print("cd")

numbers = list(range(21))

# for even_number in numbers[:]:
#     print(even_number)

players = ["Jake", "Orlando", "Tess", "Segun"]
copy_of_players = players[:]

# print(f"Players: {players}\t ID: {id(players)}")
# print(f"Copy: {copy_of_players}\t ID: {id(copy_of_players)}\n")

copy_of_players[1] = "Bolu"

# print(f"Players: {players}")
# print(f"Copy: {copy_of_players}")


# print(first_three_players)

# for player in players[1:]:
#     print(player.upper())

# enumerate

names = ["Adeola", "Bibanke", "Kolapo", "Dolapo"]

# serial_no = list(range(len(names)))
# range=> 1, 2, 3, 4 ....range(1, len(names) + 1)

#     unpacking
# for x, name in enumerate(names):
#       tup = (0, 'Adeola')
#       tup = (1, 'Bibanke)        
#     print(x, name)

# for name in names:
#     print(name)

# break, continue

# numbers = list(range(11))

# for num in numbers:
#     if num < 6:
#         pass

"""
while condition-is-true:
    do stuff

"""


# count = 1
# word = 'baby'

# while count <= 3:
#     user_input = input("Guess the word: ")
#     if user_input == word:
#         print("You guessed correctly!")
#         break
#     else:
#         print(f'You guessed wrong. You have {3 - count} attempts left\n')
#     count += 1

#     if count == 3:
#         print('You have lost')


# attempts = 3
# word_to_guess = 'lorem'

# while attempts > 0:
#     user_guess = input("Guess the word: ")
#     attempts -= 1

#     if user_guess ==  word_to_guess:
#         print('Correct guess')
#         break
#     print(f"You guess wrongly. You have {attempts} attempts left")

#     if attempts == 0:
#         print("You have lost.")


# actual_pin = '1234'
# attempts = 3

# while attempts > 0:  
#     user_entry = input("Enter your PIN: ")
#     attempts -= 1

#     if user_entry == actual_pin:
#         print("Login success...")
#         break
#     print(f"Wrong PIN. You have {attempts} attempts left before your ATM will be blocked!")

# if attempts == 0:
#     print("You have tried 3 times and your card is blocked")



# Modify the while loop above to inform the user that they have lost after
# all attempts have been exhausted.

# random module

# from main import yoruba_greeting
import random

random_number = random.randint(1, 5)
# attempts:int = 5


# while attempts > 0:
#     user_guess = int(input("Guess a number btw 1 and 5: "))
#     if user_guess == random_number:
#         print("You guessed right!")
#         break
#     elif user_guess > random_number:
#         attempts -= 1
#         print(f"Your guess is high. You have {attempts} attempts left\n")
#     elif user_guess < random_number:
#         attempts -= 1
#         print(f"Your guess is too low. You have {attempts} attempts left\n")
# else:
#     print("\nYou lose")

# while user_guess != random_number:
#     user_guess = int(input("Guess a number btw 1 and 5: "))

#     if user_guess == random_number:
#         print("You guessed correctly!")
#     else:
#         print("Wrong! Try again...\n")


# players = {'Arjun', s

# print(f"List before shuffling: {players}")
# random.shuffle(players)
# print(f"List after shuffling: {players}")

"""
1. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value As they enter each topping,
print a message saying you’ll add that topping to their pizza

2. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age.
If a person is under the age of 3, the ticket is free;
if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket
"""


# flag: A boolean value that you use to control a loop
# flag = True

# while flag:
#     topping = input('Enter a pizza topping: ')

#     if topping == 'quit':
#         flag = False
#         # break
#     else:
#         print(f"I'll add {topping} to your pizza...")


flag = True
# ticket = 0

# while flag:
#     user_age = int(input("Enter your age (in digits): "))

#     if user_age < 3:
#         print("You get a free ticket!")
#     elif 3 <= user_age <= 12:
#         print("Your ticket fee is ₦10")
#     else:
#         print("Your ticket fee is ₦15")

"""
Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not
"""

# while True:
#     user_input = int(input("Enter a whole number: "))

#     if user_input % 10 == 0:
#         print(f"The {user_input} is a multiple of 10\n")
#     else:
#         print(f"The {user_input} is not a multiple of 10.\n")
# else:
#     ...



"""
while conditon_is_true:
    do stuff;
"""

# count = 0

# while count < 10:
#     # print(count)

#     if count % 2 == 0:
#         print(count)
#     count = count + 1

# password = ''

# while password != 'fish123':
#     password = input("Enter your password: ")
    
#     if password == 'fish123':
#         print("Correct PIN")
#         break
#     else:
#         print('Incorrect password. Try again')

# attempts = 3

# while attempts > 0:
#     user_pin = input("Enter your PIN: ")

#     if user_pin == '1234':
#         print("Login success!...")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect PIN. You have {attempts} trials left")

"""
Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such
as "I made your tuna sandwich."
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made.
""" 

import random

secret = random.randint(0, 5)

# names = ['Ada', 'Bob', 'Curtis']
# random_name = random.choice(names)
# print(random_name)

# user_guess = ''
# attempts = 3

# print("---------- GUESSING GAME ------------\nType 'q' to quit\n")

# while attempts > 0:
#     user_guess = input("Guess a number: ")

#     if user_guess.lower() == 'q':
#         break

#     user_guess = int(user_guess)

#     if user_guess == secret:
#         print("You guessed right!")
#         break
#     elif user_guess > secret:
#         attempts -= 1
#         print('Your guess is too high; try sth lower perharps..')
#     elif user_guess < secret:
#         attempts -= 1
#         print("Your guess is too low; maybe try sth lower...")
#     else:
#         attempts -= 1

#     print(f'You have {attempts} trials left\n')

# print("You're out of attempts, you lose.")

guys = ['Bob', 'Shola', 'Henry']

print(random.choice(guys))


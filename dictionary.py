# Dictionary: key, value pairs

contact_book = {
    'Sam': '+490122222',
    'Tolu': '+4490000',
    'Israel': '+234000',
    'Bolu': '+1-319-000'
    }

# print(contact_book['Sam'])


details = {
    1: 123,
    'name': 'John Fray',
    'age': 16,
    'is_engaged': False,
    True: 'Boolean value',
    'items': []
}

# student = {'name': 'Esupofo Onimekun', 'age': 10, 'is_graduate': True}

details[1]

"""
. Person: Use a dictionary to store information about a person you know
Store their first name, last name, age, and the city in which they live You
should have keys such as first_name, last_name, age, and city Print each
piece of information stored in your dictionary
"""

person = {
    'first_name': 'Adeola',
    'age': 36,
    'last_name': 'Onimoto',
    'city': 'Sydney'
}
# print(person)
# person['friends'] = ['Solape', 'Don', 'Bruce', 'Raphinha']

person['favorite_food'] = 'Eba and Banga soup with brokoto'

person['age'] = 37


# del person['city']
# print(person)
# print(person['balance'])
# print(f"{person['first_name']} {person['last_name']} is {person['age']} years old. They reside at {person['city']}")

"""
Glossary: A Python dictionary can be used to model an actual dictionary
However, to avoid confusion, let's call it a glossary
•	 Think of five programming words you've learned about in this course
    Use these words as the keys in your glossary, and store their meanings
     as values
•	 Print each word and its meaning as neatly formatted output.
     You might print the word followed by a colon and then its meaning,
     or print the word on one line and then print its meaning indented on a second line.
     Use the newline character (\n) to insert a blank line between each word-meaning
     pair in your output
"""

glossary = {
    'variable': 'computer',
    'string': 'A collection of characters',
    'loop': 'A sequence of instructions repeated',
    'module': 'A set of inbuilt functions where you import an existing value'
}

# if 'computer' in glossary.values():
#     print(True)
# else:
#     print(False)

# print(glossary.items())
# print(f"variable\n\t{glossary['variable']}")
# print(f"string\n\t{glossary['string']}")
# print(f"loop\n\t{glossary['loop']}")
# print(f"module\n\t{glossary['module']}")

# for k in sorted(glossary.keys()):
#     print(k)

"""
Rivers: Make a dictionary containing three major rivers and the country
each river runs through.
One key-value pair might be 'nile': 'egypt'
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt
•	 Use a loop to print the name of each river included in the dictionary
•	 Use a loop to print the name of each country included in the dictionary
"""

river_pairings = {
    'niger': 'nigeria',
    'thames': 'united kingdom',
    'volga': 'russia',
    'limpopo': 'south africa'
}

# for river, country in river_pairings.items():
#     print(f"The {river.title()} runs through {country.title()}")

# print()

# for river in river_pairings.keys(): 
#     print(river.title())

# print()

# for country in river_pairings.values():
#     print(country.title())

# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {1: 'aa'}

# print(f"Dict 1 before update: {dict_1}")

# dict_1.update(dict_2)

# print(dict_1)

students = {
    'Segun': [10, 9, 9, 7],
    'Alicia': [9, 8, 7, 4],
    'Doe': [2, 10, 8, 5],
    'Julian': [10, 10, 10, 10],
    'Solape': [8, 8, 7, 9],
    'Kingsley': [2, 10, 10, 6],
    'Opemipo': [10, 10, 9, 10],
}

averages_of_students = {}

for student, scores in students.items():
    average = sum(scores)/ len(scores)
    averages_of_students[student] = average
    # averages[student] = average
    # print(f"{student}'s average score is {average}")

# print(averages_of_students)

max_average = 0
for stud, avg in averages_of_students.items():
    if avg > max_average:
        max_average = avg
        top_student = stud

# print(max_average)

for stud, avg in averages_of_students.items():
    if avg == max_average:
        # print(f"Student with the highest average is {stud} with {avg}")
        pass


'''
Modify the code above to indicate who got the highest average.
'''


"""
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

Polling: Use the code above
•	Make a list of people who should take the favorite languages poll.
    Include some names that are already in the dictionary and some that are not.
•	Loop through the list of people who should take the poll.
    If they have already taken the poll, print a message thanking them for responding
    If they have not yet taken the poll, print a message inviting them to take the poll
"""
import random

people = {
    'james': {
        'first_name': 'James',
        'last_name': 'Toriola',
        'age': 12,
        'scores': []
    },
    'tope': {
        'first_name': 'Tope',
        'last_name': 'Calvin',
        'age': 11,
        'scores': [ random.randint(50, 100) for _ in range(5)]
    }
}

people['tope']['scores']
# print(people)


"""
Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet In each dictionary, include the kind of animal and the owner’s
name Store these dictionaries in a list called pets Next, loop through your list
and as you do print everything you know about each pet
"""

pets = [
    {
        'name': 'Bingo',
        'breed': 'Basenji',
        'age': 3
    },
    {
        'name': 'jack_sparrow',
        'breed': 'Harpy Eagle',
        'age': 12
    },
    {
        'name': 'segun',
        'breed': 'Ibadan Cat',
        'age': 4
    },
]

# for pet in pets:
#     print(f"{pet['name']} is {pet['breed']}")


# print("----------Average Calculator---------\n\n")

# total = int(input("How many numbers do you want to average (digits): "))
# counter = 0
# numbers = []

# while counter != total:
#     number = int(input("Enter number: "))
#     numbers.append(number)
#     counter += 1

# average = sum(numbers) / total
# print(f"Average of {numbers} is {average}")

# shopping_list = {
#     'body_cream': 4950,
#     'bag': 250000,
#     'wristwatch': 50000,
#     'ogede': 2500
# }

# while True:
#     print("\n1. View Items\n2. Add items\n3. Remove item\n4. View total cost\n5. Update price\nX: Quit")

#     prompt = input("Enter a choice: ")

#     if prompt == '1':
#         print()
#         for item, price in shopping_list.items():
#             formatted_item = " ".join(item.split('_'))
#             print(f'Item: {formatted_item.capitalize()}, Price: {price:.2f}')
#     elif prompt == '2':
#         new_item = input("\nEnter item name: ").lower()
#         new_item_price = float(input("Enter item price: "))
        
#         shopping_list[new_item] = new_item_price
#     elif prompt == '3':
#         item_to_remove = input('Enter item name to remove: ').lower()
#         if item_to_remove in shopping_list:
#             del shopping_list[item_to_remove]
#         else:
#             print('Item does not exist. View list of available list to cross check')
#     elif prompt == '4':
#         total_cost = sum(shopping_list.values())
#         print(f"Total cost of items: ${total_cost:.2f}")
#     elif prompt == '5':
#         item_to_update = input("What item do you want to update? ")
#         if item_to_update in shopping_list.keys():
#             new_price =  float(input("Enter new price: "))
#             shopping_list[item_to_update] = new_price
#             print(f"{item_to_update}'s price is now ${new_price}")
#         else:
#             print(f"{item_to_update} is not in the list. Please try again.\n")
#     elif prompt == 'X':
#         print('Quitting...')
#         break

"""
Modify the code above
1. to add a further option to view total cost of the shopping list
BONUS: to update the price of an item
"""

"""
Cities: Make a dictionary called cities
- Use the names of three cities as keys in your dictionary
- Create a dictionary of information about each city and include the country that the city is in,
  its approximate population, and one fact about that city
- The keys for each city's dictionary should be something like:
  country, population, and fact
- Print the name of each city and all of the information you have stored about it
"""


cities = {
    'Kano': {
        'population': 10000000,
        'random_fact': 'Kano is the most populous city in Northern Nigeria',
        'country': 'Nigeria'
    },
    'Ibadan': {
        'population': 7000000,
        'random_fact': 'Ibadan is not full of rusted zinc roofs as supposed.',
        'country': 'Nigeria'
    },
    'Frankfurt': {
        'population': 4000000,
        'random_fact': 'Frankfurt is a busting metropolis in Western Germany.',
        'country': 'Germany'
    }
    
}

# print("Random Trivia\n")
# # print(f"Random fact:\t{random.choice(citi)}")

# user_city = input("Enter a city name: ").title()

# if user_city in cities:
#     print(f"Random fact about {user_city.title()}: {cities[user_city]['random_fact']}")
# else:
#     print(f"Please enter one of these: {list(cities.keys())}")


# random: randint, choice, shuffle, sample 
# random.sample()

# words = "apple apple banana orange coconut grape orange coconut banana"

# list_of_words = words.split()
# # print(list_of_words)

# word_count = {}
# for word in list_of_words:
#     word_count[word] = word_count.get(word, 0) + 1

# print(word_count)

"""
Build a simple guessing game where a user guesses the computer's rolled dice
(i.e. A random number between 1 and 6 is generated and the user input is compared to it)
Implement a dictionary to record the number of right guesses and wrong guesses.
"""

# secret = random.randint(1, 6)
# user_guess = 0
# record = {}

# while user_guess != secret:
#     prompt = input("\n1. Play game\n2. Exit\n3.View score\nEnter Choice: ")
    
#     if prompt == '1':
#         while True:
#             user_guess = int(input("Guess the rolled dice: "))

#             if user_guess == secret:
#                 print("Badass!")
#                 record['wins'] = record.get('wins', 0) + 1
#             else:
#                 print('wrong')
#                 record['losses'] = record.get('losses', 0) + 1

#             if record.get('losses', 0) > 2:
#                 print('GAME OVER!')
#                 break
#     elif prompt == '3':
#         print(f"Wins: {record.get('wins', 0)}\tLosses: {record.get('losses', 0)}\n")
#     elif prompt == '2':
#         break


"""
try:
    stuff that could potentially cause an error
except TheErrorThatCouldComeUp:
    do this when error occurs
else:
    do this when the error didn't come up
finally:
    do this anyway...regardless of whatever comes up
"""
nums = [num for num in range(0, 11)]
# squares = {}
# for num in nums:
#     squares[num] = num ** 2

# dict_comprehension = {k, v for i in container }
squares = {num: num ** 2 for num in nums if num % 2 == 0}
print(squares)

scores = [('Ada', 77), ('Boboye', 75), ('Curtis', 56), ('Daphne', 75)]

scores_ = {person: score for person, score in scores}

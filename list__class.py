#A list is a  (ordered) collection of items

my_list = [1, 2, 3, 4, 5, 6]

# print(my_list[0])
# print(my_list)

# my_friends = ['Ada', 'Bob', 'Curtis', 'Drey', 'Elon', 'Fike', 'Gamora', 'Hus', 'Ian', 'Jake', 'Sam']

# print(my_friends)

#Deleting items
# my_friends.remove('Sam')
# removed_friend = my_friends.pop(2)
# print(removed_friend)
# del my_friends[0]

# print(my_friends)

#Inserting items
# my_friends[0] = 'Adachukwu' #This replaces
# my_friends[1] = 'bobola'.title()
# my_friends.insert(3, 'Teni') #This inserts
# my_friends.insert(0, 'Ajiboye')

# print(my_friends)

'''
You just heard that one of your guests can't make the dinner, so you need to send out
a new set of invitations. You'll have to think of someone else to invite
•	 Add a print statement at the end of your program stating the name of the guest who can't
     make it
•	 Modify your list, replacing the name of the guest who can't make it with
     the name of the new person you are inviting
'''

# guests = ['Wolverine', 'Deadpool', 'Thanos', 'Spiderman']
# print(f"These are my guests: {guests}")
# print(f"Unfortunately, {guests[2]} cannot make it to the party...\n")
# removed_guest = guests.pop(2)

# cap_steve = 'Captain America'
# guests.insert(2, cap_steve)
# print(f'{cap_steve} has taken {removed_guest}\' place')
# print(f"\nThese are my new guests: {guests}")

my_friends = ['Ada', 'Bob', 'Curtis', 'Drey', 'Elon', 'Fike', 'Gamora', 'Hus', 'Ian', 'Jake']
# print(f"List before extending: {my_friends}\n")

new_friends = ['Kyle', 'Leon', 'Morris', 'Noserafatul', 'Obi']
my_friends.extend(new_friends)
# print(f"List after extending: {my_friends}\n")

# my_friends += ['Pascal', 'Qing', 'Rotimi', 'Sage', 'Tars']

my_friends += ['Peter', 'Quasim', 'Rosie']
# more_friends = ('Suleiman', 'Taju', 'Undertaker')

# my_friends.extend(more_friends)

# print(f"More extension: {my_friends}")

my_numbers = [6, 7, 2, 0, 3, 2, 1, 9]
#This changes the list
my_numbers.sort()


#Returns a sorted copy w/o changing the list
sorted_list = sorted(my_numbers, reverse=True) 

# print(f"List:{my_numbers}\nUsing sorted()\nNew sorted list:{sorted_list}")

# my_numbers.reverse()
# print(my_numbers)

numbers_to_100 = list(range(100, 50, -2))
# print(numbers_to_100)

'''
Seeing the World: Think of at least five places in the world you’d like to
visit
•	 Store the locations in a list Make sure the list is not in alphabetical order
•	 Print your list in its original order Don’t worry about printing the list neatly,
      just print it as a raw Python list
•	 Use sorted() to print your list in alphabetical order without modifying the
      actual list
•	 Show that your list is still in its original order by printing it
•	 Use sorted() to print your list in reverse alphabetical order without changing
      the order of the original list
'''

#str.split()
#str.join()
#list slicing
# places = ['Maldives', 'Norway', 'Casablanca', 'France', 'Czech Republic']
# print(places, '\n')

# sorted_places = sorted(places, reverse=True)
# print(sorted_places, '\n')
# print(places)

"""
Create a list of 10 countries and sort in reverse. 
Write a program that checks if the LAST item is in title case,
and print the number of times that it has the 'a' in it (i.e in the last item)
"""

# countries = ['Switzerland', 'Nigeria', 'Togo', 'USA', 'Senegal', 'Canada', 'UK', 'Malta', 'India', 'Ukraine']
# print(f"In my list of countries,there are {len(countries)} items")

# for country in countries:
#       if country.startswith('S'):
            # print(country.upper())
# print(countries[11])
# last_item = countries[-1]
# if last_item.istitle():
#     print('It is in title case')
# else:
#     print('Not in title case')

# frequency_of_a = last_item.count('a')
# print(f"The number of times that 'a' shows in {last_item} is: {frequency_of_a}")

#Nested lists

# to_do_list = []

# prompt = input('Welcome, would you like to enter a todo: Yes/No: ').lower()
# if prompt == 'yes':
#       todo_item = input("Enter your plan for the day: ")
#       to_do_list.append(todo_item)
#       another_prompt = input("Would you like to add another, Yes/No: ").lower()
#       if another_prompt == 'yes':
#             another_todo_item = input("Enter todo item: ")
            
# else:
#       print("Understandable, have a great day!")


# new_list = [0, 1, ['a']]

"""
Create a list and do the following:
•	 Print the message, The first three items in the list are: Then use a slice to
print the first three items from that program’s list
•	 Print the message, Three items from the middle of the list are: Use a slice
to print three items from the middle of the list
•	 Print the message, The last three items in the list are: Use a slice to print
the last three items in the list
"""

fruits = ['ogede', 'agbon', 'ibepe', 'kasu', 'agbalumo', 'orombo', 'osan']

# print(f"The first three items are: {fruits[:3]}")

# middle_index = len(fruits) // 2
# print(f"Three middle item: {fruits[middle_index -1 : middle_index + 2]}")

# print(f"Last three items: {fruits[-3:]}")

upper_case_fruits = []
for fruit in fruits:
    upper_case_fruits.append(fruit.upper())

tile_case_fruits = [item.title() for item in fruits if item.endswith('e')]  #List Comprehension
# print(tile_case_fruits)

# print(upper_case_fruits)

# upper_case_fruits = [fruit for fruit in fruits if fruit.startswith('o')]
# print(upper_case_fruits)


# numbers = list(range(11))
# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(even_numbers, odd_numbers, sep="\n")

# string.split()
# break, continue, pass, ellipsis
# random
# set, dictionary
# while

"""
Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd Most ordinal numbers end in th, except 1, 2, and 3
•	 Store the numbers 1 through 9 in a list
•	 Loop through the list
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for
       each number Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
       and each result should be on a separate line
"""

# my_list = list(range(1, 10))

# for num in my_list:
#       if num == 1:
#             suffix = 'st'
#       elif num == 2:
#             suffix = 'nd'
#       elif num == 3:
#             suffix = 'rd'
#       else:
#            suffix = 'th'

#       print(f"{num}{suffix}") 



# for even in numbers[::]:
#     print(even)

# cubes = []
# for num in range(11):
#     cubes.append(num ** 3)

# cubes_ = [num ** 3 for num in range(11) if num % 2 == 0]
# print(cubes, cubes_, sep="\n")

numbers_to_10 = list(range(11))

numbers_plus_3 = [num + 3 for num in numbers_to_10]
# print(numbers_plus_3)

# Lists, Range, Tuple, Set

grades = ('A1', 'B2', 'F9')
scores = (10, 9, 8, 9, 3, 4, 7, 0, 1, 2)

grades = ('A1', 'B2', 'C3', 'D4', 'F9')

# for grade in grades[1:]:
#     print(grade)

# Set

my_friends = {'Sam', 'Farouq', 'Tolu', 'Teniola', 'Farouq'}

# for unique_friend in my_friends:
#       print(unique_friend)

# word = "Abracadabra"
# print(sorted(list(set(word))))

scores = [9, 0, 0, 1, 2, 6, 3, 5, 5, 0, 3, 10, 4, 8, 7]
unique_scores = list(set(scores))

print(scores)
print(unique_scores)

'''
List - []
Tuple - ()
Set - {}
'''

"""
Buffet: A buffet-style restaurant offers only five basic foods Think of five
simple foods, and store them in a tuple
•	 Use a for loop to print each food the restaurant offers
•	 Try to modify one of the items, and make sure that Python rejects the
change
•	 The restaurant changes its menu, replacing two of the items with different
foods Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu
"""

names = ['Ada', 'Bob', 'Curtis']

# upper_names = []

# for x in names:
#     upper_names.append(x.upper())

# #  List Comprehension
upper_names = [item.upper() for item in names if item.isdigit()]



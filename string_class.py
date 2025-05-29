text = "My boss said 'come' "
text = 'My boss said "come" '
text_3 = "Solomon's Temple"

example_text = 'introduction to computer science'

name = 'FAROUQ'

# Changing Case

# print(example_text.upper())
# print(example_text.capitalize())
# print(name)
# print(name.lower())

# print(example_text.capitalize())
# print(example_text.title())

# print("Title case is: ", example_text.title())
# print("Hello", name.capitalize())
# print("abc".upper())


# Concatenation - Adding strings

greeting = "Good morning"
person_to_greet = "mr abdullah"
space = " "

greeting_sentence = greeting.upper() + " " + person_to_greet.title() + ' ' + "I'm with you".lower()
# print(greeting.upper() + " " + person_to_greet.title())

intro_text = "Introduction to "
subject_text = "Mathematics"


# print(intro_text + subject_text)

# Character escaping

# print("Name")
# print("Israel")
# print("Hello")

# \n - next line
# print("Hello world!\nWelcome to Aptech Python class\nMy name is Israel")

greeting = "Hello world\nWelcome to Aptech Python"
# print(greeting)

# print('Mr Emmanuel\'s plate')


# Stripping

# paragraph_text = "        Long texttttttt      ".lstrip()+ "Next text"
# print(paragraph_text)
# user_name = input("Enter your name: ")
# print(f"\nUser name is: {user_name.strip()}")

# Other string methods

# string, float, int, boolean

switch_state = True
is_python_boring = False
# print(f"I believe it is {is_python_boring} that Python is boring.")

# endswith, startswith
my_favorite_fruit = "Banana"
my_favorite_fruit.endswith('na')
my_favorite_fruit.startswith('b')
# print(my_favorite_fruit.startswith('B'))

# islower, isupper
genotype = "AA"
# print("12O".isdigit())

# print("ABEL".islower())

# isdigit
user_age = "32"
# print(user_age.isdigit())

# count
sentence = "This is a sentence. It contains a subject, verb and a predicate."
sentence = sentence.upper()
# print(sentence.count("a"))

mr_sam_wise_saying ="A word is enough for the wise."
# print('I heard Mr Sam saying "A word is enough for the wise" ')


# Split method

# sentence = "My name is Barry Allen, and I'm the fastest man alive"

# text = input("Enter a sentence: ")
# text_as_list = text.split()
# words_gt_3 = []

# for word in text_as_list:
#     if len(word) > 3:
#         words_gt_3.append(word)

# words_greater_than_3 = [word for word in text_as_list if len(word) > 3]

# print(words_gt_3)

# user_name = input('Enter your name: ')
# splitted_name = user_name.split()

# first_name = splitted_name[0]
# last_name = splitted_name[-1]

# print(f"Your initials: {first_name[0]}.{last_name[0]}.")

# print(f"Your initials: {splitted_name[0][0]}.{splitted_name[0][0]}.")

# break
# continue

"""
Givem that the string "I love Python" is split into a list of words as shown below:
sentence = "I love Python"
words = sentence.split()
print(words)

1. Modify the sentence to be a user input✅
2.Modify the code to print each word on a new line✅
3. Modify the program to also print the first and last word in the sentence✅
4. Modify the code to exlude common words like 'the', 'and', 'over'✅
"""

# sentence = input("Enter a sentence: ")
# words = sentence.split()

# for word in words:
#     if word.lower() not in ['the', 'and', 'over']:
#         print(word)

# first_word = words[0]
# last_word = words[-1]

# print(first_word, last_word)

"""
Q2
Prompt the user to enter their full name i.e. First, Middle and Last name,
and print the initials of their name e.g John Michael Doe -> J.M.D
"""

name_as_list = ['ada', 'chukwu']
# user_name = input("Enter your full name: ")
# name_as_list = user_name.split()
# name

# first_name = name_as_list[0]
# middle_name = name_as_list[1]
# last_name = name_as_list[-1]

# print(f"{user_name} initials: {first_name[0].upper()}.{middle_name[0].upper()}.{last_name[0].upper()}")

print('X'.join(['a', 'b', 'c']))
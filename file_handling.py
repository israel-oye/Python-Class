
# try:
#     f = open('file.txt', 'w')
#     f.write('This is a text')
#     f.close()
# except FileExistsError as e:
#     print('File exists...use another file name?')

# Create a file named hello.txt with some text in it
# Print the file content

# f = open('file.txt', 'w')
# f.write(input("Enter text: "))
# f.close()

open_f = open('file.txt', 'r')
file_content = open_f.read()
open_f.close()
# print("File contains: {0}".format(file_content))

# f = open('file.txt', 'r')
# lines = f.readlines()
# f.close()
# print(f"File has {len(lines)} lines")

# Read a file quotes.txt and print its lines in reverse order
import random as eyi_je_eyi_o_je #Alias naming


# with open('file.txt', 'r') as f:
#     print(f.read())


with open('new-file.txt', 'w') as f:
    # f.write()
    f.writelines(['This file was created by a Python script\n', 'This is another line'])

# Write a program that creates a file called `student.txt`
# and writes the names of three students, one per line.
# Let the students names' be inputted by the user.

# count = 3
# students = []

# while count > 0:
#     student_name = input("Enter a student name: ")
#     students.append(student_name+'\n')
#     count -= 1

# with open('students.txt', 'w') as f:
#     f.writelines(students)
#     print('Done ✅')

# with open('students.txt', 'a') as st:
#     st.write('Zach')

# with open('students.txt', 'r') as f:
#     print(f.read())

#Ask the user for a message, and append it to a file named `journal.txt`.

# with open('journal.txt', 'a') as j:
#     user_input = input("What's on your mind?: ")
#     j.write(user_input + '\n')

# Create a file `fruits.txt` with 5 fruit names.
# Write code to read and print each fruit in uppercase.
# with open('fruits.txt', 'r') as f:
#     text_content = f.readlines()
#     print(text_content) #'Apple\nBanana\nCherry\nDates\nEgg plant\nFufu'

with open('poem.txt', 'r') as poem:
    poem_lines = poem.readlines()
    print(f"Poem has {len(poem_lines)} lines")

import os

os.path.exists('fruits.txt')

"""
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
"""

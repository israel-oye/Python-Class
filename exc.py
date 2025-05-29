# print("ab" + 5)

"""
try:
    stuff that could potentiallcy cause Error
except Error:
    do sth if error comes up
else:
    execute this if no errors
finally:
    will execute no matter what happens
"""

# try:
#     age = int(input("Enter your age: "))
#     print(f"You will be {age + 5} in 5 years")
# except ValueError as e: 
#     print(e)
# except TypeError as e:
#     print(e)

"""
 Create a list of items and ask the user to pick an index. Handle:
   - IndexError
"""
import random

nums = [random.randint(0, 9) for _ in range(5)]

try:
    choice = int(input("Select an item in the list: "))
    user_choice = nums[choice]
except IndexError as e:
    print("Item doesn't exist in list...")
except ValueError as e:
    print('Please enter choice in digits...')
else:
    print(f"You chose {nums[choice]}")


try:
    user_age = int(input("Enter your age: "))
    print(user_age + 5)
except TypeError as e:
    print('An error occured...')
except ValueError as e:
    print(e)
print('Success')

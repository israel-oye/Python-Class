class Human:
    species = 'Homo Sapiens' #Class attribute

    def __init__(self, name, gender):
        self.name = name    #Instance attribute
        self.gender = gender
        self.legs = 2
        self.hands = 2
    
    # Method: a func that belongs to a class
    def describe(self):
        print(f"{self.gender} human with the name: {self.name}")

    def get_num_of_limbs(self):
        return self.hands + self.legs
    
    def get_species(self):
        return Human.species



peacock_lady = Human(name='Toluwanimi', gender='Female')
peacock_lady.feathers = 0
peacock_lady.name = 'Ogedengbe'
# print(peacock_lady.species)


ninja_guy = Human('Big Stepper Sam', 'Male')
# print(ninja_guy.hands)
# ninja_guy.gender = 'Non-binary pansexual identifying as a cup'

# ninja_guy.describe()
# print(ninja_guy.get_num_of_limbs())
# print(ninja_guy.species)


class Student:
    # Static attrribute
    school_name = 'Aptech Computer Institute'
    is_institute = True

    def __init__(self, name: str):
        self.name: str = name # Instance attribute
        self.__score: int = 0

    def __str__(self):
        return f"<Student: {self.name}>"
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, new_score: int):
        if new_score >= 0 and new_score <= 100:
            self.__score = new_score
        print('Please enter a valid score')

    # Instance method
    def get_grade(self) -> str:
        Student.school_name
        if (self.score > 90):
            return 'A'
        elif (self.score > 80):
            return 'B'
        else:
            return 'C'

    # Static method
    @staticmethod    
    def get_school():
        return Student.school_name
    
    @classmethod
    def get_institutional_status(cls):
        return cls.is_institute
    
    

lolade = Student(name='Lolade')
# print(lolade)
ololade = Student('Ololade')
# print(Student.get_school())
# Student.score
# print(ololade.get_school())
lolade.score = 90
print(lolade.get_grade())

# print(ololade.school_name)
# print(lolade.school_name)


# names = ['Ada', 'Bob', 'Cyle', 'Dolapo', 'Ezekiel', 'Fahran', 'Ganiyu']
# students = []
# import random
# for name in names:
#     random_score = random.randint(0, 100)
#     student = Student(name, random_score)
#     students.append(student)

# for student in students:
#     print(f"Name: {student.name}\tGrade: {student.get_grade()}")






# student1 = Student('Bob', 'A')
# print(student1.school_name) #Aptech Computer Institute

# student2 = Student('Curtis', 'D')
# student2.school_name = 'New School'
# print(student2.school_name)

# student3 = Student('Dada', 'A')
# print(student3.school_name)

# Add a method to the class, `get_grade` to tell the student what grade they got
# based on their score


class Animal:
    def __init__(self, animal_name, phylum):
        self.name = animal_name
        self.phylum = phylum
        self.is_living_thing = True

    def describe(self):
        print(f'I\'m an animal belonging to Phylum: {self.phylum}')


goat = Animal('Goat', 'Chordata')
dog = Animal('Dog', 'Chordata')
# print(goat.phylum)
# print(dog.is_living_thing)
# dog.is_living_thing = False
# goat.describe()
def add(*operands):
        # sum = 0
        # for n in operands:
        #     sum += n
        # return sum
        return sum(operands)
add(5, 4, 39)

class Math:
    @staticmethod
    def add(*operands):
        # sum = 0
        # for n in operands:
        #     sum += n
        # return sum
        return sum(operands)
    
    @staticmethod
    def subtract(*operands):
        difference = operands[0]
        for i, operand in enumerate(operands):
            if i == 0:
                continue
            difference = difference - operand
        return difference
    
# print(Math.add(3, 4))
# print(Math.subtract(3, 2, 5))

class Safe:
    def __init__(self, code):
        self.__code = code  # private attribute

    def get_code(self): #getter
        print(f'Code: {self.__code}')

    def set_code(self, new_code): #setter
        self.__code = new_code

    @property
    def code(self):
        return self.__code

    def unlock(self, attempt):
        if attempt == self.__code:
            print("Unlocked")
        else:
            print("Wrong code")

my_piggy_bank = Safe(1234)
# my_piggy_bank.get_code()
# my_piggy_bank.set_code('0090')
# my_piggy_bank.get_code()
print(my_piggy_bank.code)
# print(my_piggy_bank.__code)
# my_piggy_bank.unlock(1234)

class Locker:
    def __init__(self, pin: str):
        self.__pin = pin

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, value):
        self.__pin = value

    @property
    def pin(self):
        return self.__pin
    
    @pin.setter
    def pin(self, value):
        self.__pin = value

    def check_pin(self, value: str):
        if value == self.__pin:
            return True
        return False
    

my_locker = Locker('2025')

# print(my_locker.check_pin(2025))

my_locker.pin = 2020
# print(my_locker.pin)

# Create a Person class that encapsulates the person's year of birth.
# Add other attributes as you deem fit they don't need to be private
# Add a getter method to get the person's AGE
# And a corresponding setter i.e the setter sets the year of birth.

class Person:
    def __init__(self, name: str, year_of_birth: int, gender: str):
        self.name = name
        self.gender = gender
        self.__birth_year = year_of_birth

    def get_age(self):
        return 2025 - self.__birth_year
    
    def set_birth_year(self, year: int):
        if year > 2025:
            print('Invalid year')
        self.__birth_year = year

class Student(Person):
    def __init__(self, name, year_of_birth, gender):
        super().__init__(name, year_of_birth, gender)

john = Person('John', 2015, 'Male')
john.set_birth_year(1955)
# print(john.get_age())

class BankAccount:
    def __init__(self, account_holder: str, opening_bal: float):
        self.owner = account_holder
        self.__balance = opening_bal

    def get_balance(self):
        return self.__balance
    
    def get_balance_in_dollars(self):
        return self.__balance * 1500
    
    def deposit(self, value: float):
        if value > 0:
            self.__balance += value

class Player:
    occupation = 'Football Player' #class attribute

    def __init__(self, name, club):
        self.name = name #Instance attribute
        self.club = club

lamine = Player(name='Lawal Yemi', club='Best Club')
vini = Player('Vinicius', 'RMA')

# print(lamine.name, vini.name)
Player.occupation = 'European footballers'
# print(vini.occupation)
# print(vini.occupation  == lamine.occupation)

"""
Student:
Create a class Student with a class attribute school_name and instance attributes name and grade.
Print out both kinds of attributes.

Dog: class
Add an age instance attribute and compare between dogs.
Access the class attribute using both Dog.species and dog1.species.
"""

# class Student:
#     school_name = 'University of Oke-Fiaa'

#     def __init__(self, name: str, grade: str):
#         self.name = name
#         self.grade = grade

# olododo = Student(name='Olododo Benjamin', grade='A2')

# print(Student.school_name) # Class attribute
# print(olododo.grade) # Instance attribute

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age: int):
        self.name = name  # Instance attribute
        self.age = age

    # Instance method
    def bark(self):
        print(f"Woof woof! {self.name} is barking!")

    @classmethod
    def evolve(cls, new_species):
        cls.species = new_species
    
    @classmethod
    def create_from_dict(cls, data: dict):
        # data = {'name': 'Doggo', 'age': 0}
        # new_dog = Dog()
        new_dog = cls(name=data['name'], age=data['age'])
        return new_dog  
    
    # new_dog = Dog(name, age) #default constructor
    # new_dog_2 = Dog.create_from_sth(sth) # alternatice constructor

dog_data = {
    'name': 'Jack',
    'age': 6
}


# new_dog = Dog.create_from_dict(data=dog_data)
# print(new_dog.name)
# new_dog.bark()

# bingo = Dog('Bingo', 4)
# bingo.bark() # Instance method called

# Dog.evolve('Feline')
# print(Dog.species)
# print(bingo.species)
# print(Dog.species == bingo.species)

# Define a class method from_dict() in a Car class that creates a Car instance from a dictionary.

"""
1. **Alternative Constructor for a Rectangle Class**:
   - Create a `Rectangle` class with attributes `length` and `width`.
   - Implement an alternative constructor `from_square` that takes a single argument `side` and creates a square with equal length and width.
   - Write code to create a `Rectangle` object using the alternative constructor and print its dimensions.

2. **Alternative Constructor for a Circle Class**:
   - Create a `Circle` class with an attribute `radius`.
   - Implement an alternative constructor `from_diameter` that takes a single argument `diameter` and creates a circle with the given diameter.
   - Write code to create a `Circle` object using the alternative constructor and print its radius.

3*. **Alternative Constructor for a Person Class**:
   - Create a `Person` class with attributes `name`, `age`, and `email`.
   - Implement an alternative constructor `from_string` that takes a single argument `person_info` in the format "name,age,email"
     and creates a `Person` object with the corresponding attributes.
   - Write code to create a `Person` object using the alternative constructor and print its details.

4. **Alternative Constructor for a Time Class**:
   - Create a `Time` class with attributes `hours`, `minutes`, and `seconds`.
   - Implement an alternative constructor `from_minutes` that takes a single argument `total_minutes` and creates a `Time` object with the corresponding hours, minutes, and seconds.
   - Write code to create a `Time` object using the alternative constructor and print its time.

"""

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.width = breadth
    
    @property
    def area(self):
        return self.length * self.width

    @classmethod
    def from_square(cls, side):
        new_rectangle = cls(length=side, breadth=side)
        return new_rectangle
    
my_square = Rectangle.from_square(4)
print(my_square.area)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        new_circle = cls(radius)
        return new_circle

circle = Circle.from_diameter(14)
print(circle.area())


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @classmethod
    def from_string(cls, person_info: str):
        name, age, email = person_info.split(',')
        return cls(name, age, email)
    
john_doe = Person.from_string('John D, 19, j.doe@mail.org')
print(john_doe.email)


class Time:
    def __init__(self, hours: int, mins: int, sec: int):
        self.hours = int(hours)
        self.minutes = int(mins)
        self.seconds = int(sec)

    def __str__(self):
        return f"<Time: {self.hours}:{self.minutes}:{self.seconds}>"

    @classmethod
    def from_minutes(cls, total_minutes: float):
        # total_minutes = 150.5

        # 150.5 // 60 = 2
        hours = total_minutes // 60 

        # 150.5 - (2 * 60) = 30.5
        minutes = total_minutes - (hours * 60) 

        # 30.5 % 1 = 0.5 * 60 = 30
        seconds = (minutes % 1) * 60 

        # 30.5 // 1 = 30.0
        minutes = minutes // 1 

        return cls(hours, minutes, seconds)
    
    @staticmethod
    def get_time_from_minutes(total_minutes: float)-> str:
        hours = total_minutes // 60
        mins = total_minutes - (hours * 60)
        secs = (mins % 1) * 60
        mins = mins // 1

        return f"{hours}:{mins}:{secs}"


    # Time.from_minutes(65) -> Time(1, 5, 0)

wakeup = Time(6, 30, 15)
print(wakeup)

rand_time = Time.from_minutes(1420)
print(rand_time)

# Create a Book class with a class variable total_books
# and a class method to return the count.

class EmailValidator:
    @staticmethod
    def is_valid(email: str) -> bool:
        if len(email) and '@' in email and '.' in email:
            return True
        return False
    
    @staticmethod
    def print_stuff(stuff):
        print(stuff)

EmailValidator.print_stuff(456690)
    
print(EmailValidator.is_valid('dopemu@gmailcom'))


# Write a static method is_even(number) in a NumberTools class.
# Create a static method to convert km to miles in a class Converter.

class BankAccount:
    bank_name = 'Melchi Corp'

    def __init__(self, holder: str, account_number: str):
        self.__balance = 0 # private attribute
        self.account_number = account_number
        self.account_holder = holder

    def deposit(self, amount: float):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        self.__balance = amount

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @property
    def balance_in_usd(self):
        return self.__balance / 1550


    @classmethod
    def change_bank_name(cls, new_bank_name):
        cls.bank_name = new_bank_name

    @staticmethod
    def validate_account(account_number):
        if len(account_number) == 10:
            return True
        return False
    

acc1 = BankAccount(holder='John Doe', account_number='2001234569')
print(acc1.balance)
acc1.balance = 500.50
print(acc1.balance_in_usd)


BankAccount.change_bank_name('FCMB')
# print(BankAccount.bank_name)

# print(BankAccount.validate_account('9034567821'))

class StringTools:
    @staticmethod
    def is_palindrome(text: str):
        return text == text[::-1]
    
class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine
        self.__speed = 0.0

    @property
    def speed(self):
        return self.__speed
    
    def __speed_in_mph(self):
        return self.speed * 0.142
    
    def get_speed_all_units(self):
        return {
            'km/h': self.speed,
            'mph': self.__speed_in_mph()
        }
    
    @speed.setter
    def speed(self, new_speed: float):
        if new_speed < 0:
            print('Invalid speed...')
        self.__speed = new_speed

car1 = Car('Corolla 2006', 'v4') # Car.__init__('Corolla 2006', 'v4')
# Name mangling

car1.speed = 360.85
# print(car1.speed)
# print(car1.get_speed_all_units())
# car1.__speed_in_mph()
    

# joe = Student()

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def describe(self):
        print(f"I'm a shape with {self.sides} sides")

class Square(Polygon):
    def __init__(self, sidex):
        super().__init__(sides=sidex)

    def describe(self):
        return super().describe()



sq = Square(4)
sq.describe()

'''
1. Create a Vehicle class with a method start().

2. Create a Car class that inherits from Vehicle and adds an attribute fuel_type.
'''

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        wheels = 4
        super().__init__(4) 

diesel_car = Car('Diesel')

class Mammal:
    # Instance/Class/Static?
    def gives_birth(self):
        return False
    
    
class Platypus(Mammal):
    def gives_birth(self):
        return super().gives_birth()
    
    def lays_egss(self):
        return True

perry = Platypus()
print(perry.gives_birth())

# mamm = Mammal()
# mamm.gives_birth()

'''
1. Employee Inheritance:
Create a base class called Employee with attributes like name, employee_id, and salary, and methods like get_details() and give_raise().
Derive two subclasses from Employee: Manager and Developer. Each subclass should have its own unique method, such as assign_task() for Manager and write_code() for Developer.
2. Book Inheritance:
Create a base class called Book with attributes like title, author, and genre, and methods like read() and bookmark().
Derive two subclasses from Book: Textbook and Novel. Each subclass should have its own unique method, such as assign_chapter() for Textbook and add_bookmark() for Novel.
Write a program that creates instances of Textbook and Novel, and demonstrates the use of both inherited and unique methods
'''

class Employee:
    def __init__(self, name: str, _id: int, salary: float):
        self.name = name
        self.employee_id = _id
        self.salary = salary

    def get_details(self):
        return {
            'id': self.employee_id,
            'name': self.name,
            'salary': self.salary
        }
    
    def give_raise(self, percentage: float):
        incease = (percentage / 100) * self.salary
        self.salary += incease

class Manager(Employee):
    def __init__(self, name, _id, salary, has_office_keys: bool = True):
        self.has_keys = has_office_keys
        super().__init__(name, _id, salary)

    def get_details(self):
        details = super().get_details()
        details['has_keys'] = self.has_keys
        return details
    
    def assign_task(self, task_name: str):
        print(f"Assigned task: {task_name}")

class Developer(Employee):
    def __init__(self, name, _id, salary):
        super().__init__(name, _id, salary)

    def write_code(self):
        print('py script.py running...')

    

ms_fransica = Manager('Fransica', 1, 500000, False)
details = ms_fransica.get_details()
print(details)
ms_fransica.assign_task('Switch on the screen')

farouq = Developer('Farouq', 2, 600000)
print(farouq.get_details())
farouq.write_code()

'''
2. Book Inheritance:
- Create a base class called Book with attributes like title, author, and genre,
  and methods like read() and bookmark().
- Derive two subclasses from Book: Textbook and Novel. 
  Each subclass should have its own unique method, such as assign_chapter()
  for Textbook and add_bookmark() for Novel.
 
 Write a program that creates instances of Textbook and Novel, and demonstrates the use of both inherited and unique methods
'''
# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return(f"Name: {self.name}, Marks: {self.marks}")

s1:Student = Student("Ali Yousuf", 70)
s2:Student = Student("Rahima Khan", 80)
print("s1 Details:" ,s1.display())
print("s2 Details:" ,s2.display())


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        return f"Total objects created: {cls.count}"
    
obj1: Counter = Counter()
obj2: Counter = Counter()
obj3: Counter = Counter()
print(Counter.display_count())


#  Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f'{self.brand} is starting.'
    
car: Car = Car("Toyota")
print(car.brand)
print(car.start())


#  Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1: Bank = Bank()
print(b1.bank_name)
b2: Bank = Bank()
print(b2.bank_name)

# Change the bank name and show that it affects both instances
Bank.change_bank_name("Habib Bank")
print(b1.bank_name)
print(b2.bank_name)


#  Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
print(MathUtils.add(5, 7))



# Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created")
    
    # def __del__(self):
    #     print("Logger object destroyed")

log: Logger = Logger()
print(log)


# Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp: Employee = Employee("Ali", 60000, "123-45-6789")
print(emp.name)  # Accessing public variable
print(emp._salary)  # Accessing protected variable
# print(emp.__ssn)  # Accessing private variable (AttributeError)
print(emp._Employee__ssn) #name mangling


#  The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
    
class Teacher(Person):
        def __init__(self, name, subject):
            super().__init__(name)
            self.subject = subject
        
teacher: Teacher = Teacher("Anum Khalid", "Physics")
print(f'Name: {teacher.name}, Subject: {teacher.subject}')


# Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rec1: Rectangle = Rectangle(5, 10)
print(f'Area of rectangle: {rec1.area()}')


#  Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return(f'{self.name} the {self.breed} says Woof!')

dog: Dog = Dog("Tommy", "Labrador")
print(dog.bark())


# Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added. 

class Book:
    def __init__(self, total_books):
        self.total_books = total_books

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        # Create an instance of Book with 10 books and print the initial count

b1: Book = Book(5)
print(f'Initial count: {b1.total_books}')
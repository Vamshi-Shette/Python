'''
1. Crafting Your First Python Object: The Power of Instance Attributes

Scenario:
Imagine you're building a digital notebook. You want each note to have its own title and content.

What you’ll learn:
How to define classes and create objects with unique data
The magic of instance attributes in organizing information

Task:
Design a Note class with title and content as instance attributes.
Log Session two different note objects and print their details.

Example:
Suppose you create notes like “Meeting Notes” and “Grocery List”.

Expected Output:
Meeting Notes : Discuss project status with team.
Grocery List : Eggs, Milk, Bread
'''

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

note1 = Note("Meeting Notes", "Discuss project status with team.")
note2 = Note("Grocery List", "Eggs, Milk, Bread")

print(f"{note1.title} : {note1.content}")
print(f"{note2.title} : {note2.content}")


'''
2. The Mysterious Empty Class: Why Bother?

Scenario:
You're designing a game and want to reserve a class for future magical creatures—but for now, it's empty.

What you’ll learn:
Why and how to define an empty class
Using pass and setting up blueprints for future code

Task:
Log Session an empty MagicCreature class and show that you can still make objects from it.

Example:
You make a new MagicCreature object and print its type.

Expected Output:
<class '__main__.MagicCreature'>
'''

class MagicCreature:
    pass

creature = MagicCreature()
print(type(creature))


'''
3. Family Traits: Inheritance in Action with Vehicles and Buses

Scenario:
You’re modeling a transportation system. Buses are vehicles, so shouldn’t they share common features?

What you’ll learn:
Inheriting attributes and methods from a parent class
The principle of code reuse and extension

Task:
Log Session a Vehicle class and a Bus class that inherits from it. Demonstrate shared behavior.

Example:
Suppose you make a Bus object and call its move() method.

Expected Output:
Vehicle is moving
'''

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bus(Vehicle):
    pass

b = Bus()
b.move()


'''
4. Shape Shifters: Mastering Class Inheritance

Scenario:
Imagine you’re building a drawing tool. You have a general Shape, but want to specialize it into Circle and Square.

What you’ll learn:
The basics of inheritance
How subclasses can extend or override parent class functionality

Task:
Log Session a Shape class with a method called draw(). Inherit and customize in Circle and Square.

Example:
If you create a Circle and ask it to draw():

Expected Output:
Drawing a circle
'''

class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

c = Circle()
c.draw()


'''
5. One for All: The Magic of Class Attributes

Scenario:
All students in a school belong to the same institution. How can you ensure this is reflected in every student object?

What you’ll learn:
Class (static) attributes: properties shared by all instances
When and why to use them

Task:
Define a Student class where every student has the same school_name.

Example:
If you create two students and print their school_name:

Expected Output:
Central High School Central High School
'''

class Student:
    school_name = "Central High School"

s1 = Student()
s2 = Student()

print(s1.school_name, s2.school_name)


'''
6. Is That What I Think It Is? Type Checking Objects

Scenario:
You’re building a dynamic form. You need to know if a user input is a string, number, or something else.

What you’ll learn:
How to use type() and why it’s useful
Avoiding type errors in your code

Task:
Check and print the type of various objects.

Example:
You create an integer and a string and check their types.

Expected Output:
<class 'int'>
<class 'str'>
'''

a = 10
b = "Python"

print(type(a))
print(type(b))


'''
7. Are You One of Us? Checking Class Membership

Scenario:
You want to make sure a Bus object can access special parking. But only if it’s really a Vehicle.

What you’ll learn:
Using isinstance() to check an object’s class or parent classes
Dynamic type safety

Task:
Check if a Bus object is an instance of Vehicle.

Example:
You check with isinstance() for a Bus object.

Expected Output:
True
'''

class Vehicle:
    pass

class Bus(Vehicle):
    pass

b = Bus()
print(isinstance(b, Vehicle))


'''
8. True Descendants: Subclass Checking

Scenario:
You’re building a plugin system and want to know if a new class is a valid type of plugin.

What you’ll learn:
The use of issubclass()
Class relationships in Python

Task:
Check if Bus is a subclass of Vehicle.

Example:
You use issubclass() with Bus and Vehicle.

Expected Output:
True
'''

class Vehicle:
    pass

class Bus(Vehicle):
    pass

print(issubclass(Bus, Vehicle))


'''
9. Polymorphism in the Real World: Area of Shapes

Scenario:
You’re making a geometry tool. Different shapes need to compute area, but each does it differently.

What you’ll learn:
Polymorphism: different classes, same interface
Practical OOP design patterns

Task:
Log Session a Shape base class with an area() method, then implement it differently in Circle and Square.

Example:
If you create a Square with side 4 and call area():

Expected Output:
16
'''

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

sq = Square(4)
print(sq.area())


'''
10. All About Circles: Area and Perimeter

Scenario:
Designing a map app? You’ll want to know the area covered by a circular pond!

What you’ll learn:
Implementing methods with calculations
Understanding encapsulation

Task:
Build a Circle class with area() and perimeter() methods.

Example:
For a circle of radius 3:

Expected Output:
28.27
18.85
'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

c = Circle(3)
print(c.area())
print(c.perimeter())

'''
11. Meet the Person: Calculate Age from Date of Birth

Scenario:
Log Session a birthday tracker! Determine someone’s age from their date of birth.

What you’ll learn:
Handling dates and calculating with them
Real-world use of classes

Task:
Make a Person class and compute age.

Example:
For a person born on 2000-05-25 (today is 2026-03-01):

Expected Output:
Alice is 25 years old.
'''

from datetime import date

class Person:
    def __init__(self, name, year, month, day):
        self.name = name
        self.dob = date(year, month, day)

    def calculate_age(self):
        today = date(2026, 3, 1)
        age = today.year - self.dob.year
        return age

p = Person("Alice", 2000, 5, 25)
print(f"{p.name} is {p.calculate_age()} years old.")


'''
12. The Ultimate Calculator: Basic Arithmetic by OOP

Scenario:
Build your own pocket calculator with class-based design.

What you’ll learn:
Encapsulating operations in methods
Using OOP for real utilities

Task:
Log Session a Calculator class with methods for add, subtract, multiply, and divide.

Example:
Adding 4 and 5, then dividing 10 by 2:

Expected Output:
9
5.0
'''

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calc = Calculator()
print(calc.add(4, 5))
print(calc.divide(10, 2))


'''
13. The Shape Family: Hierarchies for Area and Perimeter

Scenario:
Simulate a graphics editor: various shapes with their own formulas.

What you’ll learn:
Creating class hierarchies
Overriding methods for specialized behavior

Task:
Write a Shape base class, then subclasses for Circle, Triangle, and Square, each with its own area/perimeter.

Example:
If you create a Triangle with base 6 and height 4 and call area():

Expected Output:
12.0
'''

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

t = Triangle(6, 4)
print(t.area())


'''
14. Binary Find Tree: Smart Organization

Scenario:
Organize data for fast searching, like contacts or scores.

What you’ll learn:
Implementing data structures as classes
Recursion in OOP

Task:
Build a BST class with methods for insertion and search.

Example:
Insert numbers and search for 5.

Expected Output:
True or False (depending on search)
'''


'''
15. Stack in Python: Undo That Move!

Scenario:
Log Session a feature like "undo" in a drawing app.

What you’ll learn:
How to build a stack (LIFO) using classes
Using lists for stack operations

Task:
Implement a Stack class with push and pop methods.

Example:
Push 10, then 20; pop an element.

Expected Output:
20
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

s = Stack()
s.push(10)
s.push(20)
print(s.pop())


'''
16. The Linked List: Chain Reaction

Scenario:
Store and process data efficiently, like songs in a playlist.

What you’ll learn:
Building a linked list from scratch
Understanding nodes and pointers

Task:
Write a LinkedList class with insert, delete, and display.

Example:
Add 10, then 20, and display list.

Expected Output:
10 -> 20
'''


'''
17. Shopping Cart: OOP for Online Stores

Scenario:
Simulate adding/removing items and computing the bill in an online store.

What you’ll learn:
Real-world application of classes
Encapsulation and methods

Task:
Design a ShoppingCart class with add, remove, and total methods.

Example:
Add "Book" (2 × 200) and "Pen" (5 × 20); show total.

Expected Output:
500
'''

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name, quantity, price):
        self.items[name] = (quantity, price)

    def total(self):
        total = 0
        for quantity, price in self.items.values():
            total += quantity * price
        return total

cart = ShoppingCart()
cart.add("Book", 2, 200)
cart.add("Pen", 5, 20)
print(cart.total())


'''
18. Enhanced Stack: Show Me What’s Inside

Scenario:
See the current state of the stack—great for debugging.

What you’ll learn:
Extending existing classes
Useful methods for state visibility

Task:
Add a display method to your Stack class to show its elements.

Example:
Push 1, then 2; display stack.

Expected Output:
[1, 2]
'''

class StackEnhanced:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def display(self):
        print(self.items)

se = StackEnhanced()
se.push(1)
se.push(2)
se.display()


'''
19. Queue It Up: Fair Turn for All

Scenario:
Manage waiting lines—like people in a ticket queue.

What you’ll learn:
Implementing a queue (FIFO) in Python
Real-world queue management

Task:
Build a Queue class with enqueue and dequeue methods.

Example:
Enqueue 10, then 20; dequeue once.

Expected Output:
10
'''

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())


'''
20. The Banking System: Managing Accounts with OOP

Scenario:
Simulate a simple bank system: create accounts, deposit, withdraw, and check balances.

What you’ll learn:
Using classes for real-life simulations
Method design and data encapsulation

Task:
Log Session a BankAccount class with methods for deposit, withdraw, and balance check.

Example:
Start with balance 1000, deposit 500, withdraw 300, show balance.

Expected Output: 1200
'''

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.check_balance())
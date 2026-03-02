'''
Write a function print_details(name, age) that prints a sentence using both parameters
Sample data: print_details("Alice", 25)
expected output: 
Name: Alice, Age: 25
'''
def print_details(name, age):
    print(f"Name: {name}, Age: {age}")

print_details("Alice", 25)

'''
Write a function multiply(x, y) that returns the product of its two arguments
Sample data:
result = multiply(4, 5)
print(result)
expected output:
20
'''
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)

'''
Write a function greet_person(name, greeting) that prints a personalized message
Sample data: greet_person("John", "Hi")
expected output:
Hi, John!
'''
def greet_person(name, greeting):
    print(f"{greeting}, {name}!")

greet_person("John", "Hi")

'''
Write a function area_of_circle(radius) that returns the area (πr²)
Sample data: print(area_of_circle(3))
expected output:
28.274333882308138
'''
import math
def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(3))

'''
Write a function is_negative(number) that returns True if the number is negative, else False
Sample data:
print(is_negative(-7))
print(is_negative(0))
expected output:
True
False
'''
def is_negative(number):
    return number < 0

print(is_negative(-7))
print(is_negative(0))

'''
Write a function grade(score) that returns letter grade
Sample data:
print(grade(85))
print(grade(72))
print(grade(50))
expected output:
B
C
F
'''
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(grade(85))
print(grade(72))
print(grade(50))

'''
Write a function sign(num) that returns 'Positive', 'Negative', or 'Zero'
Sample data:
print(sign(10))
print(sign(-4))
print(sign(0))
expected output:
Positive
Negative
Zero
'''
def sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(sign(10))
print(sign(-4))
print(sign(0))

'''
Write a function power(base, exponent=2) that returns base raised to exponent
Sample data:
print(power(3))
print(power(2, 5))
expected output:
9
32
'''
def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 5))

'''
Write a function introduction(name, country='India') that prints intro message
Sample data:
introduction("Sara")
introduction("Alex", "USA")
expected output:
My name is Sara and I am from India.
My name is Alex and I am from USA.
'''
def introduction(name, country='India'):
    print(f"My name is {name} and I am from {country}.")

introduction("Sara")
introduction("Alex", "USA")

'''
Write a function calculate(a, b) that returns sum and difference
Sample data:
s, d = calculate(10, 3)
print("Sum:", s)
print("Difference:", d)
expected output:
Sum: 13
Difference: 7
'''
def calculate(a, b):
    return a+b, a-b

s, d = calculate(10, 3)
print("Sum:", s)
print("Difference:", d)

'''
Write a function string_stats(s) that returns number of vowels, consonants, digits
Sample data: print(string_stats("Hello123"))
expected output:
(2, 5, 3)
'''
def string_stats(s):
    vowels = 'aeiouAEIOU'
    v = c = d = 0
    for ch in s:
        if ch.isdigit():
            d += 1
        elif ch in vowels:
            v += 1
        elif ch.isalpha():
            c += 1
    return (v, c, d)

print(string_stats("Hello123"))

'''
Write a function factorial(n) using recursion
Sample data: print(factorial(5))
expected output:
120
'''
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

'''
Write a recursive function sum_list(lst) to return sum of elements
Sample data: print(sum_list([1, 2, 3, 4]))
expected output:
10
'''
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))

'''
Write a recursive function reverse_string(s) that returns reversed string
Sample data: print(reverse_string("python"))
expected output:
nohtyp
'''
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))

'''
Write a recursive function fibonacci(n) that returns nth Fibonacci number
Sample data: print(fibonacci(6))
expected output:
8
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

'''
Write a function min_max(numbers) that returns smallest and largest number
Sample data:
small, large = min_max([8, 3, 5, 2, 10])
print("Smallest:", small)
print("Largest:", large)
expected output:
Smallest: 2
Largest: 10
'''
def min_max(numbers):
    return min(numbers), max(numbers)

small, large = min_max([8, 3, 5, 2, 10])
print("Smallest:", small)
print("Largest:", large)
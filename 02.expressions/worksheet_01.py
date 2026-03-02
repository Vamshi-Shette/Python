'''
Calculate the Square of a Number
Write an expression to calculate the square of a number.
Sample Input: n = 7
'''
n = 7

# Using exponentiation
square1 = n ** 2

# Using multiplication
square2 = n * n

print("Square using ** :", square1)
print("Square using * :", square2)

'''
Evaluate a Quadratic Expression
Given values for x, a, b, and c, write an expression to compute ax² + bx + c.
Sample Input: a = 2, b = 3, c = 4, x = 5
'''
# Given values
a = 2
b = 3
c = 4
x = 5

# Quadratic expression: ax^2 + bx + c
result = a * x**2 + b * x + c

print("The value of the quadratic expression is:", result)


'''
Find the Remainder (Modulo Operation)
Write an expression to get the remainder when one number is divided by another.
Sample Input: num = 29, divisor = 6
'''
num = 29
divisor = 6

remainder = num % divisor
print("Remainder:", remainder)

'''
Check if a Number is Positive, Negative, or Zero (Conditional Expression)
Use a single line expression to print whether a number is positive, negative, or zero.
Sample Input: num = -8
'''
num = int(input("input: "))

print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

'''
Get the Absolute Value
Write an expression to get the absolute value of a number.
Sample Input: n = -12
'''
n = int(input("input: "))

absolute = abs(n)
print("Absolute value:", absolute)

'''
Swap Two Numbers Without Using a Third Variable
Swap two variables’ values using a single line of code.
Sample Input: a = 15, b = 8

'''
a = int(input("a: "))
b = int(input("b: "))

a, b = b, a  # swap in one line
print("a:", a, "b:", b)

'''
Calculate the Average of Three Numbers
Write an expression to find the average of three numbers.
Sample Input: x = 5, y = 8, z = 10
'''
x = 5
y = 8
z = 10

average = (x + y + z) / 3
print("Average:", average)

'''
Use the Ternary Operator to Find the Minimum of Two Numbers
Use a single expression to find the smaller of two numbers.
Sample Input: a = 20, b = 13
'''
a = 20
b = 13

minimum = a if a < b else b
print("Minimum:", minimum)

'''
Bitwise OR and XOR
Write expressions to calculate the result of bitwise OR and bitwise XOR between two numbers.
Sample Input: x = 9, y = 5
'''
x = 9   # 1001 in binary
y = 5   # 0101 in binary

bitwise_or = x | y
bitwise_xor = x ^ y

print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)

'''
Check if a Number is Divisible by Both 2 and 3
Write a single expression that evaluates to True if a number is divisible by both 2 and 3, otherwise False.
Sample Input: num = 18
'''
num = 18

divisible = (num % 2 == 0) and (num % 3 == 0)
print(divisible)

'''
Find the Largest of Three Numbers Using Only Expressions
Without using if, elif, or any function, write an expression to find the largest of three given numbers.
Sample Input: a = 14, b = 27, c = 19
'''
a = 14
b = 27
c = 19

largest = a if (a > b and a > c) else b if b > c else c
print("Largest:", largest)

'''
Check if a Number is a Power of Two
Write a single Boolean expression to check if a number is a power of two.
Sample Input: n = 32
'''
n = 32

is_power_of_two = n > 0 and (n & (n - 1)) == 0
print(is_power_of_two)

'''
Find the Second Largest of Three Numbers
Write an expression (no functions, no if) to get the second largest value among three numbers.
Sample Input: a = 20, b = 12, c = 18
'''
a = 20
b = 12
c = 18

second_largest = a + b + c - max(a, b, c) - min(a, b, c)
print("Second Largest:", second_largest)

'''
Toggle a Specific Bit in an Integer
Given a number and a bit position, write an expression to toggle (flip) that bit.
Sample Input: n = 12, bit_position = 2
'''
n = 12
bit_position = 2  # 0-indexed from right

toggled = n ^ (1 << bit_position)
print("Toggled Number:", toggled)

'''
Count the Number of 1 Bits in an Integer (No Loops)
Write an expression (using built-in functions) to count how many 1s are in the binary representation of a number.
Sample Input: n = 29
'''
n = 29

count_ones = bin(n).count('1')
print("Number of 1 bits:", count_ones)

'''
Find the Sign of a Number as -1, 0, or 1 (Using Only Expressions)
Write a single expression that gives -1 for negative numbers, 0 for zero, and 1 for positive numbers.
Sample Input: n = -56
'''
n = -56

sign = (n > 0) - (n < 0)
print("Sign:", sign)

'''
Check If a Number is a Multiple of 4 but Not of 8
Write an expression that is True only if a number is divisible by 4 but not by 8.
Sample Input: n = 12
'''
n = 12

check = (n % 4 == 0) and (n % 8 != 0)
print(check)

'''
Rotate Bits Left by k Positions
Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
Sample Input: n = 150, k = 2
'''
n = 150       # 10010110 in binary
k = 2

rotated = ((n << k) | (n >> (8 - k))) & 0xFF
print("Rotated Left:", rotated)

'''
Find the Difference Between the Largest and Smallest of Three Numbers (Using Only Expressions)
Write an expression to find the difference between the largest and the smallest of three numbers.
Sample Input: a = 8, b = 27, c = 14
'''
a = 8
b = 27
c = 14

diff = max(a, b, c) - min(a, b, c)
print("Difference:", diff)

'''
Set the nth Bit of a Number
Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
Sample Input: n = 9, bit_position = 3
'''
n = 9
bit_position = 3

new_number = n | (1 << bit_position)
print("Number after setting bit:", new_number)
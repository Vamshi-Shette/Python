'''
Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
Example: 153 → 1³ + 5³ + 3³ = 153
'''
# Loop through 3-digit numbers
for num in range(100, 1000):
    # Extract digits
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10

    # Check Armstrong condition
    if hundreds**3 + tens**3 + units**3 == num:
        print(num)

'''
For a given number, print its multiplication table from 1 to 10, but don’t use the * operator.
'''
n = 7  # Example number

print(f"Multiplication table for {n}:")

for i in range(1, 11):
    # Calculate n*i using repeated addition
    product = sum([n for _ in range(i)])
    print(f"{n} x {i} = {product}")
'''
sum([n for _ in range(i)])
Creates a list of n repeated i times.
Then adds all those values together.
Effectively: n * i
'''

'''
Using only loops, print all prime numbers between 2 and n (n is user input).
'''
n = 20  # Example upper limit
#n=int(input("num: "))
print(f"Prime numbers between 2 and {n}:")

for num in range(2, n+1):
    is_prime = True
    # Check divisibility by numbers from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

'''
For a given number of rows, print the following number pyramid pattern
1
1 2
1 2 3
...
1 2 ... n
'''
n = 5  # Example, can change to any positive integer

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Move to next line

'''
Take an integer input and print its digits in reverse order (don’t use slicing or strings).
'''
num = int(input("Enter an integer: "))
temp = num

print("Digits in reverse order:", end=' ')
while temp > 0:
    digit = temp % 10        # get last digit
    print(digit, end=' ')
    temp = temp // 10         # remove last digit

'''
Check if the input number reads the same backward as forward, using only loops and arithmetic.
'''
num = int(input("Enter an integer: "))
temp = num
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit  # build reversed number
    temp = temp // 10

if num == reversed_num:
    print("Palindrome")
else:
    print("Not a Palindrome")

'''
Ask for two numbers and compute their Greatest Common Divisor (GCD) using repeated subtraction or division with loops.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Make sure a >= b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
'''
while b != 0:
    remainder = a % b
    a = b
    b = remainder
'''
print("GCD is:", a)

'''
Print a hollow square pattern of size n (n ≥ 3).
'''
n = int(input("Enter the size of the square (n ≥ 3): "))

if n < 3:
    print("Size must be at least 3")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Print '*' at border, space inside
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()  # Move to next line

'''
Take an integer and, using only loops, sum its digits repeatedly until only a single digit remains.
Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2
'''
num = int(input("Enter an integer: "))
temp = num

while temp >= 10:  # repeat until single digit
    sum_digits = 0
    t = temp
    while t > 0:
        sum_digits += t % 10
        t //= 10
    temp = sum_digits

print("Single-digit sum:", temp)

'''
Input a number and count how many digits it contains, using only arithmetic and loops.
'''
num = int(input("Enter an integer: "))
temp = abs(num)  # handle negative numbers
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)

'''
Take a number as input and calculate its factorial using loops (no recursion).
'''
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")

'''
For n rows, print a right-aligned triangle pattern:
'''
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # Print spaces first
    for s in range(n - i):
        print(" ", end='')
    # Print stars
    for j in range(i):
        print("*", end='')
    print()  # Next line

'''
Print the sum of all odd numbers from 1 up to n (inclusive), using loops only
Sample Input: n = 10
'''
n = int(input("input: "))
sum_odd = 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum_odd += i
print("Sum of odd numbers:", sum_odd)

'''
Check if a given number is a perfect number (sum of divisors excluding itself), using only loops
Sample Input: num = 28
'''
num = int(input("input: "))
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
print("Perfect Number" if sum_div == num else "Not a Perfect Number")

'''
Print all numbers from n down to 1 using a single loop
Sample Input: n = 5
'''
n = int(input("input: "))
for i in range(n, 0, -1):
    print(i, end=" ")
print()

'''
Input an integer and count how many times 0 appears in it (no strings or lists)
Sample Input: num = 102040
'''
num = int(input("input: "))
count = 0
temp = num
while temp > 0:
    if temp % 10 == 0:
        count += 1
    temp //= 10
print("Number of zeros:", count)

'''
Using only loops and arithmetic, compute the sum of all numbers below 1000 that are multiples of 3 or 5
'''
sum_mul = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_mul += i
print("Sum of multiples of 3 or 5 below 1000:", sum_mul)

'''
Input a number and find its smallest divisor greater than 1 (using only loops)
Sample Input: num = 91
'''
num = int(input("input: "))
divisor = 2
while divisor <= num:
    if num % divisor == 0:
        break
    divisor += 1
print("Smallest divisor greater than 1:", divisor)

'''
For n rows, print the following double triangle pattern
Sample Input: n = 4

*
**
***
**
*
'''
n = int(input("input: "))

# Upper part
for i in range(1, n+1):
    print("*" * i)

# Lower part
for i in range(n-1, 0, -1):
    print("*" * i)

'''
Input n and print the nth Fibonacci number using only variable updates and a loop (no lists, no recursion)
Sample Input: n = 7
'''
n = int(input("input: "))

a, b = 0, 1

if n == 0:
    print("Fibonacci number:", a)
elif n == 1:
    print("Fibonacci number:", b)
else:
    for _ in range(2, n+1):
        a, b = b, a + b
    print("Fibonacci number:", b)
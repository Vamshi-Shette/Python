# Is type(5) == int always True? Is isinstance(5, int) always True? Explain the difference.
x = 5
print(type(x) == int)  # True

x = 5
print(isinstance(x, int))  # True

#Can a Python variable change its data type after assignment? Give an example and explain the implications.
x = 10        # integer
print(x, type(x))

x = 3.14      # now a float
print(x, type(x))

x = "Python"  # now a string
print(x, type(x))
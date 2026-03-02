# Add an integer (5) to a string ("Hello"), observe the error, and explain why it occurs.

# Integer and string
num = 5
text = "Hello"

# Try to add them
#result = num + text
result = (str(num) + text)
print(result)
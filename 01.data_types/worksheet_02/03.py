# Given x = [1, 2, 3] and y = x, then x[0] = 9. What are the values of x and y? Explain the behavior 

x = [1, 2, 3]
y = x           #y has reference to list x, like pointer

x[0] = 9

print("x =", x) #9,1,2
print("y =", y) # 9,1,2

# Lists are mutable, so this modifies the existing list object.
'''

x = [1, 2, 3]
y = x
x = [4, 5, 6]
print(y)
'''
x = [1, 2, 3]
y = x
x = [4, 5, 6]  #It creates a new list object and makes x point to it. we can modify only through []
print(y) # [1,2,3]
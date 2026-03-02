# What is the difference between None, 0, False, and "" in Python? Are they the same or different as variables?
#  How does Python treat them in conditional statements?

values = [None, 0, False, ""]

for v in values:
    print(v, "→", type(v))
'''
None → <class 'NoneType'>
0 → <class 'int'>
False → <class 'bool'>
 → <class 'str'>
 '''
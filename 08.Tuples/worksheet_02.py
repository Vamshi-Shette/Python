'''
Description: Compute the element-wise sum of multiple tuples of equal length.
This exercise teaches how to combine tuples by adding corresponding elements, often used in mathematical and data processing tasks.
Input: t1 = (1, 2, 3, 4), t2 = (3, 5, 2, 1), t3 = (2, 2, 3, 1)
Output: (6, 9, 8, 6)
'''

t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)

result = tuple(a + b + c for a, b, c in zip(t1, t2, t3))
print(result)


'''
Description: Calculate the product by multiplying all the numbers in a tuple.
This is useful for aggregate calculations and is commonly found in mathematical programming and statistics.
Input: t = (4, 3, 2, 2, -1, 18)
Output: -864
'''

t = (4, 3, 2, 2, -1, 18)

product = 1
for num in t:
    product *= num

print(product)


'''
Description: Convert a tuple of positive integers into a single integer by concatenating their values.
This is a common data transformation task, often seen in problems that require generating a unique number from a sequence.
Input: t = (1, 2, 3)
Output: 123
'''

t = (1, 2, 3)
number = int("".join(str(i) for i in t))
print(number)


'''
Description: Sort a tuple of (string, float) pairs by the float value in descending order.
Sorting by a specific field is essential in data analysis and organization, especially when dealing with mixed data types.
Input: t = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))
Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
'''

t = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))

sorted_list = sorted(t, key=lambda x: float(x[1]), reverse=True)
print(sorted_list)


'''
Description: Find all possible pair combinations from two tuples,
combining each element from the first tuple with each from the second.

This problem introduces the concept of Cartesian product and 
is useful for combinatorial tasks.
Input: t1 = (1, 2), t2 = (3, 4)
Output: [(1, 3), (1, 4), (2, 3), (2, 4)]
'''
t1 = (1, 2)
t2 = (3, 4)

result = []
for a in t1:
    for b in t2:
        result.append((a, b))

#result = [(a, b) for a in t1 for b in t2]
print(result)


'''
Description: Compute the frequency of each element in a tuple and 
return the result as a dictionary.

Element frequency counting is widely used for data summarization, analytics,
and validation tasks.
Input: t = (1, 2, 2, 3, 3, 3)
Output: {1: 1, 2: 2, 3: 3}
'''
t = (1, 2, 2, 3, 3, 3)

freq = {}
for num in t:
    freq[num] = freq.get(num, 0) + 1

print(freq)


'''
Description: Filter a list of tuples, keeping only those where the tuple length 
or value at a specific index meets a condition.

This task helps develop conditional filtering skills and
deeper data selection logic in nested structures.
Input: lst = [(1, 2, 3), (4, 5), (6, 7, 8)], Keep tuples of length 3
Output: [(1, 2, 3), (6, 7, 8)]
'''

lst = [(1, 2, 3), (4, 5), (6, 7, 8)]

filtered = [t for t in lst if len(t) == 3]
print(filtered)


'''
Description: Check if a specified value is present in any of the inner tuples in a 
tuple of tuples.
This teaches how to search through nested tuples, which is useful in 
multi-dimensional data handling.

Input: t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'),
 ('Orange', 'Yellow', 'Lime')), Check: 'White'
Output: True
'''

t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'),
      ('Orange', 'Yellow', 'Lime'))
value = 'White'

found = any(value in inner for inner in t)
print(found)


'''
Description: Convert a tuple of key-value pairs into a dictionary.
This conversion is fundamental in Python for transitioning between sequence and mapping data types for fast lookups.
Input: t = (('a', 1), ('b', 2), ('c', 3))
Output: {'a': 1, 'b': 2, 'c': 3}
'''

t = (('a', 1), ('b', 2), ('c', 3))

dictionary = dict(t)
print(dictionary)


'''
Description: Perform elementwise AND and XOR operations between two tuples of integers of equal length.
Elementwise bitwise operations are crucial in low-level data processing and algorithm optimization.
Input: t1 = (1, 2, 3), t2 = (2, 2, 2)
Output: AND: (0, 2, 2), XOR: (3, 0, 1)
'''

t1 = (1, 2, 3)
t2 = (2, 2, 2)

and_result = tuple(a & b for a, b in zip(t1, t2))
xor_result = tuple(a ^ b for a, b in zip(t1, t2))

print("AND:", and_result)
print("XOR:", xor_result)
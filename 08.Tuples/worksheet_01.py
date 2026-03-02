
'''
Description: Log Session a tuple containing elements of various data types.
Input: No input; directly define the tuple.
Expected Output: (10, 3.14, "Python", True)
'''
def create_mixed_tuple():
    return (10, 3.14, "Python", True)

print(create_mixed_tuple())


'''
Description: Print the first and last elements of a tuple using positive and negative indexing.
Input: my_tuple = (10, 20, 30, 40, 50)
Expected Output:
10
50
'''
def first_and_last(t):
    return t[0], t[-1]

first, last = first_and_last((10, 20, 30, 40, 50))
print(first)
print(last)


'''
Description: Unpack a tuple into three variables and print each variable separately.
Input: t = (1, 2, 3)
Expected Output:
1
2
3
'''
def unpack_tuple(t):
    a, b, c = t
    return a, b, c

a, b, c = unpack_tuple((1, 2, 3))
print(a)
print(b)
print(c)


'''
Description: Check if a specified value exists in a tuple.
Input: my_tuple = ('a', 'b', 'c'), Check: 'b'
Expected Output: True
'''
def check_value(t, value):
    return value in t

print(check_value(('a', 'b', 'c'), 'b'))


'''
Description: Slice a tuple from index 1 to 3.
Input: t = (0, 1, 2, 3, 4, 5)
Expected Output: (1, 2, 3)
'''
def slice_tuple(t):
    return t[1:4]

print(slice_tuple((0, 1, 2, 3, 4, 5)))


'''
Description: Print the number of elements in a tuple.
Input: t = (10, 20, 30, 40)
Expected Output: 4
'''
def tuple_length(t):
    return len(t)

print(tuple_length((10, 20, 30, 40)))


'''
Description: Iterate through all elements in a tuple.
Input: t = ("apple", "banana", "cherry")
Expected Output:
apple
banana
cherry
'''
def iterate_tuple(t):
    for item in t:
        print(item)

iterate_tuple(("apple", "banana", "cherry"))


'''
Description: Join two tuples using + operator.
Input: t1 = (1, 2), t2 = (3, 4)
Expected Output: (1, 2, 3, 4)
'''
def join_tuples(t1, t2):
    return t1 + t2

print(join_tuples((1, 2), (3, 4)))


'''
Description: Repeat a tuple using * operator.
Input: t = (5, 6)
Expected Output: (5, 6, 5, 6, 5, 6)
'''
def repeat_tuple(t):
    return t * 3

print(repeat_tuple((5, 6)))


'''
Description: Find maximum and minimum in a tuple.
Input: t = (11, 3, 55, 21)
Expected Output:
55
3
'''
def max_min_tuple(t):
    return max(t), min(t)

maximum, minimum = max_min_tuple((11, 3, 55, 21))
print(maximum)
print(minimum)


'''
Description: Convert a list to tuple and tuple to list.
Input: lst = [1, 2, 3], tup = (4, 5, 6)
Expected Output:
Tuple: (1, 2, 3)
List: [4, 5, 6]
'''
def convert_types(lst, tup):
    return tuple(lst), list(tup)

tup_result, list_result = convert_types([1, 2, 3], (4, 5, 6))
print("Tuple:", tup_result)
print("List:", list_result)


'''
Description: Add an item to a tuple.
Input: t = (1, 2, 3), Add: 4
Expected Output: (1, 2, 3, 4)
'''
def add_to_tuple(t, item):
    temp = list(t)
    temp.append(item)
    return tuple(temp)

print(add_to_tuple((1, 2, 3), 4))


'''
Description: Remove a specific element from a tuple.
Input: t = (1, 2, 3, 4), Remove: 2
Expected Output: (1, 3, 4)
'''
def remove_from_tuple(t, item):
    temp = list(t)
    if item in temp:
        temp.remove(item)
    return tuple(temp)

print(remove_from_tuple((1, 2, 3, 4), 2))


'''
Description: Convert tuple of characters to string and back to tuple.
Input: t = ('P', 'y', 't', 'h', 'o', 'n')
Expected Output:
String: "Python"
Tuple: ('P', 'y', 't', 'h', 'o', 'n')
'''
def tuple_to_string_and_back(t):
    string_value = "".join(t)
    tuple_value = tuple(string_value)
    return string_value, tuple_value

string_val, tuple_val = tuple_to_string_and_back(('P', 'y', 't', 'h', 'o', 'n'))
print('String:', string_val)
print('Tuple:', tuple_val)


'''
Description: Convert tuple of string numbers to tuple of integers.
Input: (("11", "22"), ("33", "44"))
Expected Output: ((11, 22), (33, 44))
'''
def convert_string_numbers(t):
    result = []
    for inner in t:
        temp = []
        for num in inner:
            temp.append(int(num))
        result.append(tuple(temp))
    return tuple(result)

print(convert_string_numbers((("11", "22"), ("33", "44"))))
#return tuple(tuple(int(num) for num in inner) for inner in t)


'''
Description: Find the index of a specified value in a tuple using index().
Input: t = ("cat", "dog", "rabbit"), Find: "dog"
Expected Output: 1
'''
def find_index(t, value):
    return t.index(value)

print(find_index(("cat", "dog", "rabbit"), "dog"))


'''
Description: Count how many times a particular value occurs in a tuple.
Input: t = (1, 2, 3, 2, 2, 4), Count: 2
Expected Output: 3
'''
def count_occurrences(t, value):
    return t.count(value)

print(count_occurrences((1, 2, 3, 2, 2, 4), 2))


'''
Description: Reverse the order of items in a tuple.
Input: t = (10, 20, 30, 40)
Expected Output: (40, 30, 20, 10)
'''
def reverse_tuple(t):
    return t[::-1]

print(reverse_tuple((10, 20, 30, 40)))

'''
Description: Identify elements that occur more than once in a tuple.
Input: t = (2, 4, 6, 2, 8, 4, 6, 2)
Expected Output: 2, 4, 6
'''
def find_duplicates(t):
    duplicates = []
    for item in t:
        if t.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

print(*find_duplicates((2, 4, 6, 2, 8, 4, 6, 2)))

'''
Description: Check whether all elements in a tuple are unique.
Input: t = (1, 2, 3, 4, 5)
Expected Output: True
'''
def all_unique(t):
    return len(t) == len(set(t))

print(all_unique((1, 2, 3, 4, 5)))


'''
Description: Sort a list of (name, age) tuples by age in ascending order.
Input: [("Alice", 25), ("Bob", 20), ("Eve", 22)]
Expected Output: [('Bob', 20), ('Eve', 22), ('Alice', 25)]
'''
def sort_by_age(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_by_age([("Alice", 25), ("Bob", 20), ("Eve", 22)]))


'''
Description: Sort tuples by total number of digits across elements.
Input: [(1, 2), (10, 11), (3, 44)]
Expected Output: [(1, 2), (3, 44), (10, 11)]
'''
def sort_by_digit_count(lst):
    def digit_count(t):
        return sum(len(str(num)) for num in t)
    return sorted(lst, key=digit_count)

print(sort_by_digit_count([(1, 2), (10, 11), (3, 44)]))


'''
Description: Change the last value in every tuple to a given value.
Input: [(10,20,40),(40,50,60),(70,80,90)], New value: 100
Expected Output: [(10,20,100),(40,50,100),(70,80,100)]
'''
def change_last_value(lst, new_value):
    return [t[:-1] + (new_value,) for t in lst]

print(change_last_value([(10,20,40),(40,50,60),(70,80,90)], 100))


'''
Description: Remove all empty tuples from a list.
Input: [(), (), ('a','b'), ('c',)]
Expected Output: [('a','b'), ('c',)]
'''
def remove_empty_tuples(lst):
    return [t for t in lst if t]

print(remove_empty_tuples([(), (), ('a','b'), ('c',)]))


'''
Description: Count tuples where every element is divisible by K.
Input: [(3,6),(9,12,15),(4,8)], K=3
Expected Output: 2
'''
def count_divisible(lst, k):
    count = 0
    for t in lst:
        if all(x % k == 0 for x in t):
            count += 1
    return count

print(count_divisible([(3,6),(9,12,15),(4,8)], 3))


'''
Description: Keep only tuples where all numbers are positive.
Input: [(1,2),(-3,4),(5,6)]
Expected Output: [(1,2),(5,6)]
'''
def keep_positive(lst):
    return [t for t in lst if all(x > 0 for x in t)]

print(keep_positive([(1,2),(-3,4),(5,6)]))


'''
Description: Sum elements of each tuple and return list of sums.
Input: [(1,2),(2,3),(3,4)]
Expected Output: [3,5,7]
'''
def sum_each_tuple(lst):
    return [sum(t) for t in lst]

print(sum_each_tuple([(1,2),(2,3),(3,4)]))


'''
Description: Unzip list of tuples.
Input: [(1,'a'),(2,'b'),(3,'c')]
Expected Output:
[1,2,3]
['a','b','c']
'''
def unzip_tuples(lst):
    a, b = zip(*lst)
    return list(a), list(b)

x, y = unzip_tuples([(1,'a'),(2,'b'),(3,'c')])
print(x)
print(y)


'''
Description: Flatten tuple of nested tuples into single flat tuple.
Input: ((1,2),(3,4),(5,6))
Expected Output: (1,2,3,4,5,6)
'''
def flatten_nested_tuple(t):
    return tuple(item for sub in t for item in sub)

print(flatten_nested_tuple(((1,2),(3,4),(5,6))))


'''
Description: Find all unique elements in tuple of tuples using set logic.
Input: ((1,2),(2,3),(4,5))
Expected Output: {1,2,3,4,5}
'''
def unique_elements(t):
    result = set()
    for sub in t:
        result.update(sub)
    return result

print(unique_elements(((1,2),(2,3),(4,5))))
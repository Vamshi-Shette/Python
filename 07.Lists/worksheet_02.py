'''
Task: Write a Python program to sum all the items in a list.
Sample input: [1, 2, 3, 4, 5]
Expected Output: 15
'''
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))


'''
Task: Write a Python program to multiply all the items in a list.
Sample input: [1, 2, 3, 4]
Expected Output: 24
'''
def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print(multiply_list([1, 2, 3, 4]))


'''
Task: Write a Python program to get the largest number from a list.
Sample input: [1, 2, 3, 4, 5]
Expected Output: 5
'''
def largest_number(lst):
    return max(lst)

print(largest_number([1, 2, 3, 4, 5]))


'''
Task: Write a Python program to get the smallest number from a list.
Sample input: [1, 2, 3, 4, 5]
Expected Output: 1
'''
def smallest_number(lst):
    return min(lst)

print(smallest_number([1, 2, 3, 4, 5]))


'''
Task: Write a Python program to count the number of strings where 
the string length is 2 or more and the first and last character 
are the same from a given list of strings.
Sample input: ['abc', 'xyz', 'aba', '1221']
Expected Output: 2
'''
def count_special_strings(lst):
    count = 0
    for s in lst:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

print(count_special_strings(['abc', 'xyz', 'aba', '1221']))


'''
Task: Write a Python program to get a list sorted in increasing 
order by the last element in each tuple.
Sample input: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
def sort_by_last_element(lst):
    return sorted(lst, key=lambda x: x[-1])

print(sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


'''
Task: Write a Python program to remove duplicates from a list.
Sample input: [1, 2, 3, 2, 4, 3, 5]
Expected Output: [1, 2, 3, 4, 5]
'''
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

#def remove_duplicates(lst):
#   return list(set(lst))

print(remove_duplicates([1, 2, 3, 2, 4, 3, 5]))


'''
Task: Write a Python program to check if a list is empty or not.
Sample input: []
Expected Output: List is empty
'''
def check_empty(lst):
    if not lst:
        return "List is empty"
    else:
        return "List is not empty"

print(check_empty([]))


'''
Task: Write a Python program to clone or copy a list.
Sample input: [1, 2, 3, 4]
Expected Output: [1, 2, 3, 4]
'''
def clone_list(lst):
    return lst.copy()

print(clone_list([1, 2, 3, 4]))


'''
Task: Write a Python program to find the list of words that are 
longer than n from a given list of words.
Sample input: ['hello', 'world', 'python', 'is', 'great'], n = 4
Expected Output: ['hello', 'world', 'python', 'great']
'''

def words_longer_than_n(words, n):
    result = []                 # Step 1: create empty list
    for word in words:          # Step 2: loop
        if len(word) > n:       # Step 3: condition
            result.append(word) # Step 4: add to new list
    return result               # Step 5: return list

#def words_longer_than_n(words, n):
#    return [word for word in words if len(word) > n]

print(words_longer_than_n(['hello', 'world', 'python', 'is', 'great'], 4))


'''
Task: Write a Python program to find the common elements between two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Expected Output: [3, 4]
'''
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

'''
Task: Write a Python program to flatten a shallow list.
Sample input: [[1, 2], [3, 4], [5, 6]]
Expected Output: [1, 2, 3, 4, 5, 6]
'''
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

print(flatten_list([[1, 2], [3, 4], [5, 6]]))


'''
Task: Write a Python program to create a list of squares 
from 1 to 10 using list comprehension.
Sample input: Range: 1 to 10
Expected Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
def squares_1_to_10():
    return [i*i for i in range(1, 11)]
print(squares_1_to_10())


'''
Task: Write a Python program to create a list of even numbers 
from a given list using list comprehension.
Sample input: [1,2,3,4,5,6,7,8,9,10]
Expected Output: [2, 4, 6, 8, 10]
'''
def even_numbers(lst):
    return [i for i in lst if i % 2 == 0]
print(even_numbers([1,2,3,4,5,6,7,8,9,10]))

'''
Task: Write a Python program to remove all occurrences of 
a specific element from a list.
Sample input: [1,2,3,2,4,2,5], element to remove: 2
Expected Output: [1, 3, 4, 5]
'''
def remove_element(lst, element):
    return [i for i in lst if i != element]

print(remove_element([1,2,3,2,4,2,5], 2))

'''
Task: Write a Python program to insert an element at a specified position in a list.
Sample input: [1, 2, 3, 4], element: 5, position: 2
Expected Output: [1, 2, 5, 3, 4]
'''
def insert_element(lst, element, position):
    lst.insert(position, element)
    return lst

print(insert_element([1, 2, 3, 4], 5, 2))


'''
Task: Write a Python program to combine two lists into a dictionary.
Sample input: ['a', 'b', 'c'], [1, 2, 3]
Expected Output: {'a': 1, 'b': 2, 'c': 3}
'''
def combine_to_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

#print(combine_to_dict(['a', 'b', 'c'], [1, 2, 3]))
#def combine_to_dict(keys, values):
#    return dict(zip(keys, values))

print(combine_to_dict(['a', 'b', 'c'], [1, 2, 3]))

'''
Task: Write a Python program to unzip a list of tuples into individual lists.
Sample input: [(1, 'a'), (2, 'b'), (3, 'c')]
Expected Output: [1, 2, 3], ['a', 'b', 'c']
'''
def unzip_list(lst):
    nums = []
    chars = []
    
    for num, char in lst:
        nums.append(num)
        chars.append(char)
    
    return nums, chars

#    nums, chars = zip(*lst)
#    return list(nums), list(chars)

print(unzip_list([(1, 'a'), (2, 'b'), (3, 'c')]))


'''
Task: Write a Python program to create a list of numbers from 1 to 20,
where each number is squared if it is even, and cubed if it is odd.
Sample input: Range: 1 to 20
Expected Output: [1, 4, 27, 16, 125, 36, 343, 64, 729, 100,
1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859, 400]
'''
def square_even_cube_odd():
    result = []
    for i in range(1, 21):
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

print(square_even_cube_odd())
#return [i**2 if i % 2 == 0 else i**3 for i in range(1, 21)]


'''
Task: Write a Python program to create a 3x3 matrix using nested list comprehensions.
Sample input: Rows: 3, Columns: 3
Expected Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
'''
def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i)
        matrix.append(row)
    return matrix

print(create_matrix(3, 3))    
#return [[i for j in range(cols)] for i in range(rows)]

'''
Task: Write a Python function to reverse a list at a specific location.
Sample input: [1, 2, 3, 4, 5, 6], position: 3
Expected Output: [1, 2, 3, 6, 5, 4]
'''
def reverse_from_position(lst, position):
    return lst[:position] + lst[position:][::-1]

print(reverse_from_position([1, 2, 3, 4, 5, 6], 3))


'''
Task: Write a Python function to find the length of the longest increasing sub-sequence.
Sample input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Expected Output: 6
(The longest increasing subsequence is [10, 22, 33, 50, 60, 80])
'''
def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))


'''
Task: Write a Python function that generates all the permutations of a given list.
Sample input: [1, 2, 3]
Expected Output: 
[[1, 2, 3], [1, 3, 2], [2, 1, 3],
 [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''
import itertools

def generate_permutations(lst):
    return [list(p) for p in itertools.permutations(lst)]

print(generate_permutations([1, 2, 3]))


'''
Task: Write a Python function to find the k-th smallest element in a list.
Sample input: [7, 10, 4, 3, 20, 15], k = 3
Expected Output: 7
'''
def kth_smallest(lst, k):
    return sorted(lst)[k - 1]

print(kth_smallest([7, 10, 4, 3, 20, 15], 3))


'''
Task: Write a Python function to check if a list is a palindrome.
Sample input: [1, 2, 3, 2, 1]
Expected Output: True
'''
def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))

'''
Task: Write a Python function to find the union and intersection of two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Expected Output:
Union: [1, 2, 3, 4, 5, 6]
Intersection: [3, 4]
'''
def union_intersection(lst1, lst2):
    union = list(set(lst1) | set(lst2))
    intersection = list(set(lst1) & set(lst2))
    return union, intersection

u, i = union_intersection([1, 2, 3, 4], [3, 4, 5, 6])
print("Union:", u)
print("Intersection:", i)


'''
Task: Remove duplicates while preserving original order.
Sample input: [1, 2, 2, 3, 4, 4, 5, 6, 5]
Expected Output: [1, 2, 3, 4, 5, 6]
'''
def remove_duplicates_order(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates_order([1, 2, 2, 3, 4, 4, 5, 6, 5]))


'''
Task: Find the maximum sum sub-sequence (non-contiguous).
Sample input: [2, -1, 2, 3, 4, -5]
Expected Output: 11
(The maximum sum subsequence is 2 + 2 + 3 + 4)
'''
def max_sum_subsequence(lst):
    return sum(x for x in lst if x > 0)

print(max_sum_subsequence([2, -1, 2, 3, 4, -5]))


'''
Task: Find the longest common subsequence between two lists.
Sample input: 
[1, 3, 4, 1, 2, 3, 4, 1]
[3, 4, 1, 2, 1, 3]
Expected Output: [3, 4, 1, 3]
'''
def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + [X[i]]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=len)

    return dp[m][n]

print(longest_common_subsequence(
    [1, 3, 4, 1, 2, 3, 4, 1],
    [3, 4, 1, 2, 1, 3]
))
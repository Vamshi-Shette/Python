'''
Log Session a dictionary to store the roll numbers (as keys) and names (as values) 
for 3 students.
Sample Output: {101: 'Ravi', 102: 'Priya', 103: 'Amit'}
'''
students = {101: 'Ravi', 102: 'Priya', 103: 'Amit'}
print(students)


'''
Suppose you write a dictionary with the same key twice. What value is stored?
Sample Input: d = {'x': 1, 'y': 2, 'x': 5}
Sample Output: {'x': 5, 'y': 2}
'''
d = {'x': 1, 'y': 2, 'x': 5}
print(d)


'''
How can you check if the key 'fruit' exists in a dictionary called d?
Sample Input: d = {'fruit': 'apple', 'veg': 'carrot'}
Sample Output: True (when checked for 'fruit')
'''
d = {'fruit': 'apple', 'veg': 'carrot'}
print('fruit' in d)


'''
Count the frequency of each letter in the string "apple", 
store results in a dictionary, and print it.
Sample Input: "apple"
Sample Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
'''
text = "apple"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)


'''
2. Access Dictionaries
Given marks = {'math': 75, 'science': 80}, 
access and print the marks for 'science'.
'''

marks = {'math': 75, 'science': 80}
print(marks['science'])


'''
What happens if you try to access a key that doesn’t exist in a dictionary?
 Try to print the value for key 'english' in marks = {'math': 75}.
Expected Output: A KeyError.
'''

marks = {'math': 75}
# print(marks['english'])  #  will raise KeyError


'''
How can you safely access a value for key 'history' in a 
dictionary scores without causing an error?
Sample Input: scores = {'math': 80, 'science': 90}
Expected Output: If not present, print a custom message like 'Not found'.
'''

scores = {'math': 80, 'science': 90}
print(scores.get('history', 'Not found'))


'''
Print all subjects and marks from this dictionary:
 student = {'math': 90, 'english': 88, 'science': 92}.
Sample Output:
math 90
english 88
science 92
'''
student = {'math': 90, 'english': 88, 'science': 92}
for subject, mark in student.items():
    print(subject, mark)


'''
3. Change Dictionaries
Updating dictionary values is needed when data changes during runtime.
Update the age of 'Anil' from 21 to 22 in this dictionary: 
ages = {'Anil': 21, 'Sunita': 20}.
'''
ages = {'Anil': 21, 'Sunita': 20}
ages['Anil'] = 22
print(ages)


'''
Change multiple values at once in the dictionary: 
info = {'a': 10, 'b': 20} so that both 'a' and 'b' become 100.
'''
info = {'a': 10, 'b': 20}
info['a'] = 100
info['b'] = 100
print(info)


'''
Increase every salary in salaries = {'A': 20000, 'B': 30000} by 10%.
Sample Output: {'A': 22000.0, 'B': 33000.0}
'''
salaries = {'A': 20000, 'B': 30000}
for key in salaries:
    salaries[key] *= 1.10
print(salaries)


'''
Assign a value to a key that doesn't exist (e.g., add 'C': 25000 to salaries).
 What happens?
'''
salaries['C'] = 25000
print(salaries)


'''
4. Add Dictionary Items
Dynamic addition of new items allows for scalable and flexible data storage.
Add 'Bangalore': 12000000 to cities = {'Delhi': 18000000, 'Mumbai': 20000000}.
'''
cities = {'Delhi': 18000000, 'Mumbai': 20000000}
cities['Bangalore'] = 12000000
print(cities)


'''
Add a key 'status' with value 'active' to user = {'name': 'Riya'}
 only if it doesn’t exist.
'''
user = {'name': 'Riya'}
if 'status' not in user:
    user['status'] = 'active'
print(user)


'''
Given a list ['dog', 'cat', 'rabbit'], create a dictionary with words as keys 
and their lengths as values.
Expected Output: {'dog': 3, 'cat': 3, 'rabbit': 6}
'''
words = ['dog', 'cat', 'rabbit']
length_dict = {word: len(word) for word in words}
print(length_dict)


'''
Merge two dictionaries: d1 = {'x': 1} and d2 = {'y': 2}.
Expected Output: {'x': 1, 'y': 2}
'''
d1 = {'x': 1}
d2 = {'y': 2}
merged = d1.copy()  # make a copy of d1
merged.update(d2)   # add items from d2
print(merged)       # {'x': 1, 'y': 2}
#merged = {**d1, **d2}
print(merged)


'''
5. Remove Dictionary Items
Sometimes, you need to clean up or adjust your dictionary as data changes.
Remove key 'math' from marks = {'math': 80, 'science': 85} using del.
'''
marks = {'math': 80, 'science': 85}
del marks['math']
print(marks)


'''
Use .pop() to remove 'name' from info = {'name': 'Amit', 'city': 'Pune'}
 and print the value removed.
'''
info = {'name': 'Amit', 'city': 'Pune'}
removed = info.pop('name')
print("Removed:", removed)
print(info)

'''
Remove all items from the dictionary: d = {'x': 1, 'y': 2}.
'''
d = {'x': 1, 'y': 2}
d.clear()
print(d)

'''
Write a program to remove key 'z' from d = {'x': 1, 'y': 2} only if it exists.
Expected Output: If not found, print 'Key not found'.
'''
d = {'x': 1, 'y': 2}
if 'z' in d:
    del d['z']
else:
    print('Key not found')

'''
6. Loop Dictionaries
Iterating over dictionaries lets you process or filter keys and values.
Loop and print all keys in d = {'a': 10, 'b': 20, 'c': 30}.
Input: d = {'a': 10, 'b': 20, 'c': 30}
Expected Output:
a
b
c
'''
d = {'a': 10, 'b': 20, 'c': 30}
for key in d:
    print(key)


'''
Loop and print all values in the same dictionary.
Input: d = {'a': 10, 'b': 20, 'c': 30}
Expected Output:
10
20
30
'''
for value in d.values():
    print(value)


'''
Loop and print each key and its value together.
Input: d = {'a': 10, 'b': 20, 'c': 30}
Expected Output:
a 10
b 20
c 30
'''
for key, value in d.items():
    print(key, value)


'''
Print only the subjects with marks above 60 from scores = {'math': 75, 'science': 55, 'english': 82}.
Input: scores = {'math': 75, 'science': 55, 'english': 82}
Sample Output:
math
english
'''
scores = {'math': 75, 'science': 55, 'english': 82}
for subject, mark in scores.items():
    if mark > 60:
        print(subject)


'''
7. Copy Dictionaries
Copying dictionaries is critical when you need to manipulate data without affecting the original.
Make a shallow copy of d = {'p': 2, 'q': 3} and print the copy.
Input: d = {'p': 2, 'q': 3}
Expected Output: {'p': 2, 'q': 3}
'''
d = {'p': 2, 'q': 3}
copy_d = d.copy()
print(copy_d)


'''
Show what happens when you do b = a with a = {'x': [1, 2]} and then modify b['x']
What happens to a?

Input: a = {'x': [1, 2]}
Expected Output: a also changes because both refer to same dictionary.
'''
a = {'x': [1, 2]}
b = a
b['x'].append(3)
print("a:", a)
print("b:", b)


'''
Log Session a copy of original = {'car': 'red', 'bike': 'blue'}. Change the 'car' in the copy to 'green' and print both dictionaries.
Input: original = {'car': 'red', 'bike': 'blue'}
Expected Output: Original remains unchanged.
'''
original = {'car': 'red', 'bike': 'blue'}
copy_original = original.copy()
copy_original['car'] = 'green'
print("Original:", original)
print("Copy:", copy_original)

'''
Explain (with code) the difference between a shallow copy and a deep copy using a nested dictionary. Show the effect of changing an inner list.
Input: nested = {'a': [1, 2], 'b': [3, 4]}
Expected Output: Deep copy remains unchanged when inner list is modified.
'''
import copy
nested = {'a': [1, 2], 'b': [3, 4]}
shallow_copy = nested.copy()
deep_copy = copy.deepcopy(nested)
shallow_copy['a'].append(5)
print("Original:", nested)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)


'''
8. Nested Dictionaries
Nested dictionaries help organize complex data, like student records or configurations.
Represent student info with name, age, and a marks dictionary (math, english) using nested dictionaries for two students.
Input: No input; directly define the dictionary.
Expected Output: Nested dictionary structure printed.
'''
students = {
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
}
print(students)


'''
Access and print the english marks of 'Rahul' in:

        students = {
          'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
          'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
        } 
Expected Output: 88
'''
print(students['Rahul']['marks']['english'])


'''
For each student in the above students dictionary, print the name and all subject marks.
Expected Output:
Rahul {'math': 90, 'english': 88}
Simran {'math': 95, 'english': 92}
'''
for name, details in students.items():
    print(name, details['marks'])


'''
Add 'science': 93 to 'Simran''s marks in the nested dictionary.
Expected Output: 'Simran' marks updated with science: 93
'''
students['Simran']['marks']['science'] = 93
print(students['Simran']['marks'])    
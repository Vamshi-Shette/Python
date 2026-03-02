'''
1. Lost & Found in the Supermarket
You’re managing the stock system for a small supermarket. Each item is a key, and its count is the value. A frantic customer wants to know if “apples” are still available. How will you instantly check if “apples” are on your shelf?
Input: stock = {'apples': 14, 'bananas': 22, 'rice': 12}, query = 'apples'
Expected Output: Yes, apples are in stock!
'''
stock = {'apples': 14, 'bananas': 22, 'rice': 12}
query = 'apples'
if query in stock:
    print("Yes, apples are in stock!")
else:
    print("Item not available")


'''
2. The Magic Dictionary of Hogwarts
Every student at Hogwarts has a pet. Sometimes, a student forgets to register a pet. 
If someone asks for Hermione’s pet, and her name isn’t registered, 
you must politely tell them “No record, maybe try another student!” 
Can you build this polite pet query?

Input: pets = {'Harry': 'owl', 'Ron': 'rat'}, query = 'Hermione'
Expected Output: No record, maybe try another student!
'''
pets = {'Harry': 'owl', 'Ron': 'rat'}
query = 'Hermione'
print(pets.get(query, "No record, maybe try another student!"))


'''
3. The Unique Collector’s Auction
You’re at a collector’s auction. Each lot number is a key, 
and the value is the type of collectible. Auctioneers want to quickly know 
how many unique collectibles are being auctioned, not just the number of lots.
 Can you wow them with an instant count?

Input: auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
Expected Output: Unique collectibles: ['coin', 'stamp', 'comic']
'''
auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
unique = list(set(auction.values()))
print("Unique collectibles:", unique)


'''
4. Robot Warehouse – Fast Inventory Sum
A robot does inventory at the end of the day and must tell the boss the 
total number of items, not just per item. What’s the fastest way for the robot to 
add up all item counts in the warehouse?
Input: inventory = {'box': 30, 'crate': 22, 'pallet': 8}
Expected Output: Total items in warehouse: 60
'''
inventory = {'box': 30, 'crate': 22, 'pallet': 8}
total = sum(inventory.values())
print("Total items in warehouse:", total)


'''
5. The Dictionary of Two Kingdoms
The “North” kingdom and the “South” kingdom both keep ledgers of gold reserves. 
Suddenly, there’s a war—when they merge, the South’s gold value should overwrite the
North’s wherever the city names match! What do the ledgers look like after the
kingdoms unite?

Input: north = {'Winterfell': 1000, 'The Eyrie': 800},
 south = {'The Eyrie': 1200, "King's Landing": 2500}
Expected Output: {'Winterfell': 1000, 'The Eyrie': 1200, "King's Landing": 2500}
'''
north = {'Winterfell': 1000, 'The Eyrie': 800}
south = {'The Eyrie': 1200, "King's Landing": 2500}
north.update(south)
print(north)


'''
6. Secret Spy Codes
You intercepted a list of coded messages (keys), but your team uses new code names
 (a mapping). How will you quickly rename every code to its new secret label?

Input: codes = {'alpha': 'ok', 'beta': 'wait'},
 new_labels = {'alpha': 'red', 'beta': 'blue'}
Expected Output: {'red': 'ok', 'blue': 'wait'}
'''
codes = {'alpha': 'ok', 'beta': 'wait'}
new_labels = {'alpha': 'red', 'beta': 'blue'}
renamed = {new_labels[k]: v for k, v in codes.items()}
print(renamed)


'''
7. Erase the Forbidden Spells
You have a dictionary of spells, but some spells are now forbidden. 
Given a list of banned spell names, wipe them from your magic book!

Input: spells = {'fireball': 5, 'healing': 10, 'curse': 2}, 
banned = ['curse', 'fireball']
Expected Output: {'healing': 10}
'''
spells = {'fireball': 5, 'healing': 10, 'curse': 2}
banned = ['curse', 'fireball']
for spell in banned:
    spells.pop(spell, None)
print(spells)


'''
8. The Cafe’s Popular Menu
Every order is tracked in a list. Can you build a menu board that shows
 how many times each item was ordered today?
Input: orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
Expected Output: {'latte': 3, 'espresso': 2, 'tea': 1}
'''
orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
menu = {}
for item in orders:
    menu[item] = menu.get(item, 0) + 1
print(menu)


'''
9. Update the Employee Profile
A nested dictionary holds employee info. An employee changed their phone number. 
Update it without touching the rest of their info.
Input: profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}, 
new_phone = '555-9999'
Expected Output: {'info': {'name': 'Sam', 'phone': '555-9999'}}
'''
profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}
new_phone = '555-9999'
profile['info']['phone'] = new_phone
print(profile)


'''
10. Pairing the Guest List
You have two lists: guest names and their seat numbers. 
Match each guest to their seat for the dinner plan!

Input: names = ['Alice', 'Bob', 'Eve'], seats = [5, 12, 8]
Expected Output: {'Alice': 5, 'Bob': 12, 'Eve': 8}
'''
names = ['Alice', 'Bob', 'Eve']
seats = [5, 12, 8]
paired = dict(zip(names, seats))
print(paired)


'''
11. Empty Desk Detective
You check a colleague's desk (dictionary) for items. 
If it's empty, print a clear message so you don't miss anything!
Input: desk = {}
Expected Output: Dictionary is empty!
'''
desk = {}
if not desk:
    print("Dictionary is empty!")


'''
12. Max and Min Detective
Among all your valuables (dictionary values), who owns the largest and smallest? 
Report both the max and min key names.
Input: valuables = {'ring': 5, 'necklace': 9, 'watch': 2}
Expected Output: Max: 'necklace', Min: 'watch'
'''
valuables = {'ring': 5, 'necklace': 9, 'watch': 2}
max_key = max(valuables, key=valuables.get)
min_key = min(valuables, key=valuables.get)
print("Max:", repr(max_key) + ",", "Min:", repr(min_key))


'''
13. Substring Key Find
Given a search term, find out which keys in your dictionary contain it. 
Useful for partial name search!
Input: d = {'hello': 1, 'world': 2, 'hell': 3}, substring = 'hell'
Expected Output: Keys containing 'hell': ['hello', 'hell']
'''
d = {'hello': 1, 'world': 2, 'hell': 3}
substring = 'hell'
result = [k for k in d if substring in k]
print("Keys containing 'hell':", result)


'''
14. Value to Key Reverse Find
You know a value, but not which key owns it. Trace back and report the key 
for a given value!
Input: d = {'x': 100, 'y': 200}, value = 200
Expected Output: Key for value 200: 'y'
'''
d = {'x': 100, 'y': 200}
value = 200
for k, v in d.items():
    if v == value:
        print("Key for value 200:", repr(k))


'''
15. Sort by Key
Organize a scrambled dictionary by key order so that the output is sorted by key.
Input: d = {'b': 2, 'a': 1, 'c': 3}
Expected Output: [('a', 1), ('b', 2), ('c', 3)]
'''
d = {'b': 2, 'a': 1, 'c': 3}
sorted_items = sorted(d.items())
print(sorted_items)


'''
16. Log Session Nested Dictionary from List
Given a list, build a nested dictionary where each item is a deeper level
 (like a Russian doll).
Input: lst = ['a', 'b', 'c', 'd']
Expected Output: {'a': {'b': {'c': {'d': {}}}}}
'''
lst = ['a', 'b', 'c', 'd']
nested = current = {}
for item in lst:
    current[item] = {}
    current = current[item]
print(nested)


'''
17. Flip Nested Dictionary
Given a nested dictionary, swap the outer and inner keys. 
Who becomes the new outer boss?
Input: d = {'x': {'p': 1}, 'y': {'q': 2}}
Expected Output: {'p': {'x': 1}, 'q': {'y': 2}}
'''
d = {'x': {'p': 1}, 'y': {'q': 2}}
flipped = {}
for outer, inner in d.items():
    for inner_key, value in inner.items():
        flipped[inner_key] = {outer: value}
print(flipped)

'''
18. Invert the Nest
Given a nested dictionary of students and their subjects, 
flip it so that subjects are outer keys and students are inside.

Input: d = {'math': {'john': 90, 'jane': 80}, 'science': {'john': 85, 'jane': 95}}
Expected Output: {'john': {'math': 90, 'science': 85}, 
'jane': {'math': 80, 'science': 95}}
'''
d = {'math': {'john': 90, 'jane': 80}, 'science': {'john': 85, 'jane': 95}}
flipped = {}
for subject, students in d.items():
    for student, marks in students.items():
        flipped.setdefault(student, {})[subject] = marks
print(flipped)


'''
19. Reverse the Order
Reverse the order of keys in a dictionary, so the last becomes first and vice versa.
Input: d = {'first': 1, 'second': 2, 'third': 3}
Expected Output: {'third': 3, 'second': 2, 'first': 1}
'''
d = {'first': 1, 'second': 2, 'third': 3}
reversed_dict = dict(reversed(list(d.items())))
print(reversed_dict)


'''
20. Key Present in List and Dictionary
Given a list and a dictionary, extract values for all keys that appear in both.
Input: d = {'a': 100, 'b': 200, 'c': 300}, lst = ['b', 'c', 'd']
Expected Output: {'b': 200, 'c': 300}
'''
d = {'a': 100, 'b': 200, 'c': 300}
lst = ['b', 'c', 'd']
result = {k: d[k] for k in lst if k in d}
print(result)


'''
21. Remove High-Value Keys
Remove all keys whose value is greater than a given number. 
Ignore non-numeric values.
Input: d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}, limit = 10
Expected Output: {'a': 5, 'b': 10, 'd': 'big'}
'''
d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}
limit = 10
filtered = {k: v for k, v in d.items() if not isinstance(v, (int, float)) or v <= limit}
print(filtered)


'''
22. Remove Keys with Substring
Remove all keys from the dictionary that contain a certain substring 
(like a keyword filter).
Input: d = {'sun': 1, 'sunny': 2, 'rain': 3}, substring = 'sun'
Expected Output: {'rain': 3}
'''
d = {'sun': 1, 'sunny': 2, 'rain': 3}
substring = 'sun'
filtered = {k: v for k, v in d.items() if substring not in k}
print(filtered)


'''
23. Dictionary with Most Pairs
Given multiple dictionaries, find the one with the most key-value pairs 
(the biggest dictionary wins).
Input: dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
Expected Output: {'x': 1, 'y': 2, 'z': 3}
'''
dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
largest = max(dicts, key=len)
print(largest)


'''
24. Append Dictionary Keys and Values
Append the keys and values of one dictionary to another, keeping the order. 
Build a bigger dictionary!
Input: d1 = {'one': 1, 'two': 2}, d2 = {'three': 3, 'four': 4}
Expected Output: {'one': 1, 'two': 2, 'three': 3, 'four': 4}
'''
d1 = {'one': 1, 'two': 2}
d2 = {'three': 3, 'four': 4}
d1.update(d2)
print(d1)


'''
25. Extract Unique Dictionary Values
Extract all unique values from the dictionary. How many distinct items are there?
Input: d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
Expected Output: [1, 2, 3]
'''
d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
unique_values = list(set(d.values()))
print(unique_values)


'''
26. Keys Associated with Values
Find all keys that share the same value. Group keys by their values.
Input: d = {'m': 1, 'n': 2, 'o': 1}
Expected Output: {1: ['m', 'o'], 2: ['n']}
'''
d = {'m': 1, 'n': 2, 'o': 1}
grouped = {}
for k, v in d.items():
    grouped.setdefault(v, []).append(k)
print(grouped)


'''
27. Filter Dictionary Values in Heterogeneous Dictionary
Your dictionary has mixed value types. Filter only the integer values into
 a new dictionary.
Input: d = {'x': 100, 'y': 'hello', 'z': 200}
Expected Output: {'x': 100, 'z': 200}
'''
d = {'x': 100, 'y': 'hello', 'z': 200}
filtered = {k: v for k, v in d.items() if isinstance(v, int)}
print(filtered)


'''
28. Print Anagrams Together Using List and Dictionary
Group words that are anagrams together from a list 
(all the jumbled twins in one basket).
Input: words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
Expected Output: [['listen', 'silent', 'enlist'], ['hello', 'ohlle']]
'''
words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
anagrams = {}
for word in words:
    key = ''.join(sorted(word))
    anagrams.setdefault(key, []).append(word)
print(list(anagrams.values()))


'''
29. Check if Binary Representations of Two Numbers are Anagrams
Given two numbers, check if their binary representations are anagrams 
(same bits, just shuffled).
Input: num1 = 5, num2 = 6
Expected Output: False
'''
num1 = 5
num2 = 6
b1 = bin(num1)[2:]
b2 = bin(num2)[2:]
print(sorted(b1) == sorted(b2))


'''
30. Largest Subset of Anagram Words
Given a list of words, find the size of the largest subset where all are anagrams
 of each other.
Input: words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
Expected Output: 3
'''
words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
groups = {}
for word in words:
    key = ''.join(sorted(word))
    groups.setdefault(key, []).append(word)
largest_size = max(len(v) for v in groups.values())
print(largest_size)


'''
31. Count Groups by Digit Sum
Group numbers by the sum of their digits and report the size of the largest group.
Input: nums = [11, 20, 12, 21, 3]
Expected Output: 2
'''
nums = [11, 20, 12, 21, 3]
groups = {}
for num in nums:
    s = sum(int(d) for d in str(num))
    groups.setdefault(s, []).append(num)
largest_group = max(len(v) for v in groups.values())
print(largest_group)


'''
32. Sort Dictionary Keys and Values List
Sort a dictionary by keys, and also sort the values list of each key.
Input: d = {'c': [3,1], 'a': [2,4], 'b': [5,1]}
Expected Output: [('a', [2,4]), ('b', [1,5]), ('c', [1,3])]
'''
d = {'c': [3,1], 'a': [2,4], 'b': [5,1]}
sorted_dict = sorted((k, sorted(v)) for k, v in d.items())
print(sorted_dict)


'''
33. Sort by Values Summation
Sort a dictionary by the sum of its list values, from smallest to largest.
Input: d = {'x': [5,5], 'y': [1,2,3], 'z': [10]}
Expected Output: [('y', [1,2,3]), ('x', [5,5]), ('z', [10])]
'''
d = {'x': [5,5], 'y': [1,2,3], 'z': [10]}
sorted_sum = sorted(d.items(), key=lambda item: sum(item[1]))
print(sorted_sum)


'''
34. Sort Dictionaries List by Key’s Value List Index
Given a list of dictionaries, sort them by the value at a specific index in each key’s value list.
Input: dicts = [{'a': [5,1]}, {'a': [3,4]}, {'a': [7,0]}], index = 1
Expected Output: [{'a': [7,0]}, {'a': [5,1]}, {'a': [3,4]}]
'''
dicts = [{'a': [5,1]}, {'a': [3,4]}, {'a': [7,0]}]
index = 1
sorted_list = sorted(dicts, key=lambda d: list(d.values())[0][index])
print(sorted_list)


'''
35. Sort Nested Keys by Value
Sort the keys inside each nested dictionary by their value.
Input: d = {'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}}
Expected Output: {'group1': [('a', 1), ('b', 2)], 'group2': [('d', 0), ('c', 3)]}
'''
d = {'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}}
sorted_nested = {k: sorted(v.items(), key=lambda item: item[1]) for k, v in d.items()}
print(sorted_nested)


'''
36. Scoring Matrix Using Dictionary
Build a scoring matrix for students and subjects using a dictionary.
Input: students = ['A', 'B'], subjects = ['math', 'sci'], scores = [[90, 80], [85, 95]]
Expected Output: {'A': {'math': 90, 'sci': 80}, 'B': {'math': 85, 'sci': 95}}
'''
students = ['A', 'B']
subjects = ['math', 'sci']
scores = [[90, 80], [85, 95]]
matrix = {}
for i, student in enumerate(students):
    matrix[student] = {subjects[j]: scores[i][j] for j in range(len(subjects))}
print(matrix)


'''
37. Factors Frequency Dictionary
Count the frequency of each factor for all numbers in a list using a dictionary.
Input: nums = [10, 15]
Expected Output: {1: 2, 2: 1, 5: 2, 10: 1, 3: 1, 15: 1}
'''
nums = [10, 15]
freq = {}
for num in nums:
    for i in range(1, num + 1):
        if num % i == 0:
            freq[i] = freq.get(i, 0) + 1
print(freq)


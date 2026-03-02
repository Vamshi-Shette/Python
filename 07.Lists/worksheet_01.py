'''
1. List Creation and Indexing
Create a list named fruits containing "apple", "banana", "cherry".
Print the second item.
Change "banana" to "kiwi".
Print updated list.
Print length of list.
'''
fruits = ["apple", "banana", "cherry"]
print("Second item:", fruits[1])
fruits[1] = "kiwi"
print("Updated list:", fruits)
print("Length of list:", len(fruits))
'''
2. Adding and Removing Items
Append "orange".
Insert "mango" at second position.
Remove "apple".
Pop last item.
Clear the list.
'''
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("apple")
fruits.pop()
print("After operations:", fruits)
fruits.clear()
print("After clear:", fruits)

'''
3. Looping Through Lists
Create list of numbers 1 to 5.
Print using for loop.
Print using while loop.
Create new list with squares using list comprehension.
'''
numbers = [1, 2, 3, 4, 5]
print("For loop:")
for num in numbers:
    print(num)
print("While loop:")
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
squares=[]
for num in numbers:
    squares.append(num**2)    
#squares = [num**2 for num in numbers]
print("Squared list:", squares)

'''
4. List Comprehension
Create fruits list.
Create list with fruits containing letter 'a'.
Convert to uppercase.
Replace "banana" with "orange".
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#Fruits containing 'a'
with_a = []
for fruit in fruits:
    if 'a' in fruit:
        with_a.append(fruit)

print("Fruits with 'a':", with_a)


#Convert to uppercase
upper_fruits = []
for fruit in fruits:
    upper_fruits.append(fruit.upper())

print("Uppercase:", upper_fruits)


# Replace banana with orange
replaced = []
for fruit in fruits:
    if fruit == "banana":
        replaced.append("orange")
    else:
        replaced.append(fruit)

print("Replaced list:", replaced)
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
with_a = [fruit for fruit in fruits if 'a' in fruit]
print("Fruits with 'a':", with_a)
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase:", upper_fruits)
replaced = ["orange" if fruit == "banana" else fruit for fruit in fruits]
print("Replaced list:", replaced)
'''

'''
5. Sorting and Copying Lists
Create numbers list.
Sort ascending.
Sort descending.
Copy to new list.
Verify separate copies.
'''
nums = [3, 1, 4, 2, 5]
nums.sort()
print("Ascending:", nums)
nums.sort(reverse=True)
print("Descending:", nums)
copy_list = nums.copy()
print("Original list:", nums)
print("Copied list:", copy_list)

'''
6. Joining and Extending Lists
Create list1 and list2.
Concatenate.
Use extend().
Print final lists.
'''
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
new_list = list1 + list2
print("Concatenated:", new_list)
list1.extend(list2)
print("Extended list1:", list1)

'''
7. List Methods Practice
Create colors list.
Count "green".
Find index of "blue".
Reverse list.
Clear list.
'''
colors = ["red", "green", "blue", "green"]
print("Count of green:", colors.count("green"))
print("Index of blue:", colors.index("blue"))
colors.reverse()
print("Reversed list:", colors)
colors.clear()
print("After clear:", colors)
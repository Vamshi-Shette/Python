'''
Find the size of a Set in Python
Story: You have a bag of unique toys. How many toys do you have?
Sample Input: 
bag = {"ball", "car", "puzzle", "car", "yo-yo"}
Sample Output: 
4
Tip: Remember, sets only keep one of each thing!
'''
bag = {"ball", "car", "puzzle", "car", "yo-yo"}
print(len(bag))


'''
Iterate over a set in Python
Story: You want to see every animal in your mini zoo, but the order doesn't matter.
Sample Input: 
animals = {"lion", "tiger", "bear"}
Tip: The order may change every time. When is this helpful?
'''
animals = {"lion", "tiger", "bear"}
for animal in animals:
    print(animal)


'''
Python - Maximum and Minimum in a Set
Story: You played some games. What’s your best and worst score?
Sample Input: 
scores = {3, 7, 10, 2, 9}
Sample Output: 
Max: 10
Min: 2
Tip: What Python functions can help you find biggest and smallest?
'''
scores = {3, 7, 10, 2, 9}
print("Max:", max(scores))
print("Min:", min(scores))


'''
Python - Remove items from Set
Story: You want to take out an old toy from your toy box.
Sample Input:
toys = {"robot", "car", "doll"}
# remove "doll"
Sample Output: 
{"robot", "car"}
Tip: What’s the difference between remove and discard if the item isn't there?
'''
toys = {"robot", "car", "doll"}
toys.remove("doll")  # or toys.discard("doll")
print(toys)


'''
Python - Check if two lists have at-least one element common
Story: You and your friend want to see if you both like any of the same cartoons.
Sample Input:
my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]
Sample Output: 
Yes! "Jerry" is common.
Tip: Which set operation shows what you both like?
'''
my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]
common = set(my_favs) & set(friend_favs)
if common:
    print('Yes!', list(common), 'is common.')
else:
    print("No common elements.")


'''
Python program to find common elements in three lists using sets
Story: Three friends want to pick a movie everyone likes. Which ones do they all like?
Sample Input:
a = ["Toy Story", "Frozen", "Moana"]
b = ["Moana", "Coco", "Frozen"]
c = ["Frozen", "Moana", "Up"]
Sample Output: 
["Frozen", "Moana"]
Tip: Can you use set.intersection for this?
'''
a = ["Toy Story", "Frozen", "Moana"]
b = ["Moana", "Coco", "Frozen"]
c = ["Frozen", "Moana", "Up"]
common_movies = list(set(a) & set(b) & set(c))
print(common_movies)


'''
Python - Find missing and additional values in two lists
Story: You compared last week's and this week's homework lists. What's missing and what's new?
Sample Input:
old_hw = ["math", "science", "art"]
new_hw = ["math", "history", "science"]
Sample Output:
Missing: art
Additional: history
Tip: What set difference shows what you forgot?
'''
old_hw = ["math", "science", "art"]
new_hw = ["math", "history", "science"]
missing = list(set(old_hw) - set(new_hw))
additional = list(set(new_hw) - set(old_hw))
print("Missing:", missing[0])
print("Additional:", additional[0])


'''
Python program to find the difference between two lists
Story: What games do you want to play this week that you didn't play last week?
Sample Input:
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
Sample Output: 
["jump", "run"]
Tip: Use set subtraction: A - B!
'''
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
new_games = list(set(this_week) - set(last_week))
print(new_games)


'''
Python Set difference to find lost element from a duplicated array
Story: You had four marbles yesterday, now one is missing. Which one?
Sample Input:
yesterday = [1, 2, 3, 4]
today = [1, 4, 2]
Sample Output: 
3
Tip: What does set(yesterday) - set(today) give you?
'''
yesterday = [1, 2, 3, 4]
today = [1, 4, 2]
lost = list(set(yesterday) - set(today))
print(lost[0])


'''
Python program to count number of vowels using sets in given string
Story: You want to count the vowels in your secret code message.
Sample Input: 
msg = "hello world"
Sample Output: 
3
Tip: Vowels can be put in a set for quick checking!
'''
msg = "hello world"
vowels = set("aeiou")
count = sum(1 for ch in msg if ch in vowels)
print(count)

'''
Concatenated string with uncommon characters in Python
Story: You and your friend invent two words. Make a mashup with only letters not shared by both.
Sample Input:
word1 = "apple"
word2 = "orange"
Sample Output:
"plrgn"
Tip: What does set(word1) ^ set(word2) do?
'''
word1 = "apple"
word2 = "orange"
uncommon = ''.join(set(word1) ^ set(word2))
print(uncommon)


'''
Python - Program to accept the strings which contains all vowels
Story: Find all words that have a, e, i, o, and u!
Sample Input:
words = ["education", "python", "sequoia"]
Sample Output:
["education", "sequoia"]
Tip: Can you check if the set of vowels is inside your word's letters?
'''
words = ["education", "python", "sequoia"]
vowels = set("aeiou")
all_vowels = [w for w in words if vowels <= set(w)]
print(all_vowels)


'''
Python - Check if a given string is binary string or not
Story: Is your note just 0s and 1s?
Sample Input:
note = "101010"
Sample Output:
Yes
Sample Input:
note = "1201"
Sample Output:
No
Tip: What does set(note) show you?
'''
note = "101010"
if set(note) <= {"0", "1"}:
    print("Yes")
else:
    print("No")


'''
Python set to check if string is panagram
Story: Does your sentence use every letter in the alphabet?
Sample Input:
sentence = "The quick brown fox jumps over a lazy dog"
Sample Output:
Yes
Tip: Compare set of your letters with the alphabet set!
'''
import string
sentence = "The quick brown fox jumps over a lazy dog"
if set(sentence.lower()) >= set(string.ascii_lowercase):
    print("Yes")
else:
    print("No")


'''
Python Set - Pairs of complete strings in two sets
Story: Pick a word from each basket to make a pair that covers all 26 letters!
Sample Input:
A = {"abc", "defg", "xyz"}
B = {"mnopq", "rstuv", "wxyz"}
Tip: Try making pairs and see if all alphabet letters are used together.
'''
import itertools
A = {"abc", "defg", "xyz"}
B = {"mnopq", "rstuv", "wxyz"}
alphabet = set(string.ascii_lowercase)
pairs = [(a, b) for a, b in itertools.product(A, B) if set(a + b) >= alphabet]
print(pairs)


'''
Python program to check whether a given string is Heterogram or not
Story: Does your word have only different letters, no repeats?
Sample Input:
word = "lamp"
Sample Output:
Yes
Sample Input:
word = "hello"
Sample Output:
No
Tip: Compare len(set(word)) and len(word).
'''
word = "lamp"
print("Yes" if len(set(word)) == len(word) else "No")

word = "hello"
print("Yes" if len(set(word)) == len(word) else "No")


'''
Python program to convert Set into Tuple and Tuple into Set
Story: You line up your toys (tuple—order matters), then put them in a toy box (set—order doesn’t matter).
Sample Input:
toys_set = {"teddy", "robot", "ball"}
Sample Output:
("teddy", "robot", "ball")
Tip: What changes when you go from set to tuple and back?
'''
toys_set = {"teddy", "robot", "ball"}
toys_tuple = tuple(toys_set)
print(toys_tuple)
back_to_set = set(toys_tuple)
print(back_to_set)


'''
Python program to convert set into a list
Story: You pour your collection of badges (set) out into a row (list) to show your friends.
Sample Input:
badges = {"star", "moon", "heart"}
Sample Output:
["star", "moon", "heart"]
Tip: Does the list always come out in the same order?
'''
badges = {"star", "moon", "heart"}
badges_list = list(badges)
print(badges_list)


'''
Python program to convert Set to String
Story: You turn your collection of letters into a cool code word.
Sample Input:
letters = {"A", "B", "C"}
Sample Output:
"ABC"
Tip: Set has no order—how can you make it alphabetical?
'''
letters = {"A", "B", "C"}
letters_str = ''.join(sorted(letters))
print(letters_str)


'''
Python program to convert String to Set
Story: Find all different letters in your name!
Sample Input:
myname = "samantha"
Sample Output:
{'s', 'a', 'm', 'n', 't', 'h'}
Tip: It's a fast way to spot repeated letters.
'''
myname = "samantha"
unique_letters = set(myname)
print(unique_letters)

'''
Python - Convert a set into dictionary
Story: Give each pet a number for your pet show.
Sample Input:
pets = {"dog", "cat", "fish"}
Sample Output:
{'dog': 0, 'cat': 1, 'fish': 2}
Tip: Try using enumerate() to give each item a number.
'''
pets = {"dog", "cat", "fish"}
pets_dict = {pet: i for i, pet in enumerate(pets)}
print(pets_dict)


'''
Python program to find union of n arrays
Story: Collect favorite colors from all your classmates—what are all the colors?
Sample Input:
friends_colors = [
  ["red", "blue"],
  ["green", "red"],
  ["yellow", "blue"]
]
Sample Output:
{'red', 'blue', 'green', 'yellow'}
Tip: What happens if someone likes the same color twice?
'''
friends_colors = [
  ["red", "blue"],
  ["green", "red"],
  ["yellow", "blue"]
]
union_colors = set().union(*friends_colors)
print(union_colors)


'''
Python - Intersection of two lists
Story: Which stickers do you and your friend both have?
Sample Input:
mine = ["dino", "star", "moon"]
yours = ["star", "rocket", "moon"]
Sample Output:
{"star", "moon"}
Tip: How is this different if you use a list instead of a set?
'''
mine = ["dino", "star", "moon"]
yours = ["star", "rocket", "moon"]
common_stickers = set(mine) & set(yours)
print(common_stickers)


'''
Python program to get all subsets of given size of a set
Story: How many different teams of 3 can you make from 5 kids?
Sample Input:
kids = {"Amy", "Bob", "Cara", "Dan", "Eva"}
size = 3
Sample Output:
("Amy", "Bob", "Cara")  # one possible team
Tip: Which Python library helps you make all teams?
'''
import itertools
kids = {"Amy", "Bob", "Cara", "Dan", "Eva"}
size = 3
teams = list(itertools.combinations(kids, size))
print(teams)


'''
Python - Minimum number of subsets with distinct elements using Counter
Story: You have lots of marbles. How many bags do you need so that no bag has two marbles of the same color?
Sample Input:
marbles = ["red", "blue", "red", "green", "blue", "red"]
Sample Output:
3
Tip: The most common color
'''
from collections import Counter
marbles = ["red", "blue", "red", "green", "blue", "red"]
counts = Counter(marbles)
min_bags = max(counts.values())
print(min_bags)
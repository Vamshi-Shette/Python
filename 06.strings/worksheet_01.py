'''
Check if a String is a Palindrome or Symmetrical
Palindrome reads the same forwards and backwards. Symmetrical string has matching halves.
Sample Input: "madam"
expected output:
Palindrome: Yes
Symmetrical: Yes
'''
s = input("input: ")
mid = len(s)//2

is_palindrome = "Yes" if s == s[::-1] else "No"
is_symmetrical = "Yes" if s[:mid] == s[-mid:] else "No"

print("Palindrome:", is_palindrome)
print("Symmetrical:", is_symmetrical)

'''
Find the Length of a String
Count total characters including spaces.
Sample Input: "hello world"
Expected Output: Length: 11
'''
s = input("input: ")
print("Length:", len(s))

'''
Reverse Words in a String
Reverse the order of words, not letters.
Sample Input: "I love Python"
Expected Output: "Python love I"
'''
s = input("input: ")
words = s.split()
reversed_words = " ".join(words[::-1])
print(reversed_words)

'''
Remove the i-th Character from a String
Remove character at index i (starting from 0)
Sample Input: String="Python", i=2
Expected Output: "Pythn"
'''
s = input("input string: ")
i = int(input("input index: "))
new_s = s[:i] + s[i+1:]
print(new_s)

'''
Count Vowels in a String Using Sets
Sample Input: "education"
Expected Output: Vowels Count: 5
'''
s = input("input: ")
vowels = set("aeiouAEIOU")
count = 0
for c in s:
    if c in vowels:
        count += 1
print("Vowels Count:", count)

'''
Eliminate Duplicate Characters from a String
Keep only first occurrence of each character
Sample Input: "programming"
Expected Output: "progamin"
'''
s = input("input: ")
seen = set()
result = ""
for c in s:
    if c not in seen:
        result += c
        seen.add(c)
print(result)

'''
Identify the Least Frequent Character in a String
Sample Input: "statistics"
Expected Output: Least frequent character: 'a'
'''
s = input("input: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
min_freq = min(freq.values())
least_chars = [k for k, v in freq.items() if v == min_freq]
print("Least frequent character:", least_chars[0])

'''
Find the Maximum Frequency Character
Sample Input: "banana"
Expected Output: Maximum frequency character: 'a'
'''
s = input("input: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
max_freq = max(freq.values())
max_chars = [k for k, v in freq.items() if v == max_freq]
print("Maximum frequency character:", max_chars[0])

'''
Check if a String Contains Special Characters
Sample Input: "Hello@123"
Expected Output: Contains special character: Yes
'''
s = input("input: ")
special = False
for c in s:
    if not c.isalnum():
        special = True
        break
#special = any(not c.isalnum() for c in s)
print("Contains special character:", "Yes" if special else "No")

'''
Generate Random Strings Until a Target String is Formed
Sample Input: Target="abc"
'''
import random
import string

target = input("input target: ")
attempts = 0
while True:
    attempts += 1
    rand_str = ''.join(random.choices(string.ascii_lowercase, k=len(target)))
    if rand_str == target:
        break
print(f"Randomly generated '{target}' after {attempts} attempts")

'''
Check If a String is a Binary String
Sample Input: "101101"
'''
s = input("input: ")
is_binary = all(c in "01" for c in s)
print("Is binary string:", "Yes" if is_binary else "No")

'''
Find Close Matches for a String in a List
Sample Input: Target="apple", List=["apply", "apples", "ape", "maple"]
'''
from difflib import get_close_matches
target = input("input target: ")
lst = input("input list separated by spaces: ").split()
matches = get_close_matches(target, lst)
print("Close matches:", matches)

'''
Find Uncommon Words Between Two Strings
Sample Input: "red blue green", "blue yellow red"
'''
s1 = set(input("input string 1: ").split())
s2 = set(input("input string 2: ").split())
uncommon = list(s1 ^ s2)
print("Uncommon words:", uncommon)

'''
Swap Commas and Dots in a String
Sample Input: "23,45.89,78.90"
'''
s = input("input: ")
s = s.replace(",", "#").replace(".", ",").replace("#", ".")
print(s)

'''
Generate All Permutations of a String
Sample Input: "abc"
'''
from itertools import permutations
s = input("input: ")
perm = [''.join(p) for p in permutations(s)]
print(perm)

'''
Detect URLs Within a String
Extract all URLs from a string
Sample Input: "Check this link: https://openai.com and http://github.com"
'''
import re
s = input("input: ")
urls = re.findall(r'https?://\S+', s)
print("URLs found:", urls)

'''
Execute Code Stored in a String
Run the code present in a string (use cautiously!)
Sample Input: "print(5+2)"
'''
code_str = input("input code string: ")
exec(code_str)

'''
Print the Middle Character of a String
Display the middle character(s)
Sample Input: "python"
'''
s = input("input: ")
mid = len(s)//2
if len(s) % 2 == 0:
    print("Middle character:", s[mid-1], "and", s[mid])
else:
    print("Middle character:", s[mid])

'''
Convert Integer to String and Vice Versa
Sample Input: Integer=123, String="456"
'''
num = int(input("input integer: "))
s = input("input string of digits: ")
print("Integer to string:", str(num))
print("String to integer:", int(s))

'''
Split a String into a List of Characters
Sample Input: "dog"
'''
s = input("input: ")
char_list = list(s)
print(char_list)

'''
Convert a List or Tuple of Characters to a String
Sample Input: ['p', 'y', 't', 'h', 'o', 'n']
'''
chars = input("input list of characters separated by space: ").split()
s = ''.join(chars)
print(s)

'''
Sort a List of Strings Alphabetically
Sample Input: ["pear", "apple", "banana"]
Expected Output: ['apple', 'banana', 'pear']  
'''
lst = input("input list separated by space: ").split()
lst.sort()
print(lst)

'''
Convert a String to a Set (Unique Characters)
Sample Input: "balloon"
Expected Output: {'b', 'a', 'l', 'o', 'n'}
'''
s = input("input: ")
unique_chars = set(s)
print(unique_chars)

'''
Generate All Valid IP Addresses from a String
Sample Input: "25525511135"
Expected Output: ['255.255.11.135', '255.255.111.35']
'''
from itertools import product

s = input("input digits string: ")
result = []
def valid(segment):
    return 0 <= int(segment) <= 255 and (segment == "0" or not segment.startswith("0"))

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            l = len(s) - (i + j + k)
            if 1 <= l <= 3:
                a, b, c, d = s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]
                if all(valid(seg) for seg in [a,b,c,d]):
                    result.append(".".join([a,b,c,d]))
print(result)

'''
Convert Numeric Words to Actual Numbers
Sample Input: "I have one apple and two oranges."
Expected Output: "I have 1 apple and 2 oranges."
'''
num_words = {"one":"1","two":"2","three":"3","four":"4","five":"5",
             "six":"6","seven":"7","eight":"8","nine":"9","zero":"0"}
s = input("input: ")
for word, digit in num_words.items():
    s = s.replace(word, digit)
print(s)

'''
Find the Location of a Word in a String
Sample Input: String="welcome to python", Word="python"
Expected Output: Position: 11
'''
s = input("input string: ")
word = input("input word: ")
pos = s.find(word)
print("Position:", pos)

'''
Frequency of Consecutive Characters
Sample Input: "aabccddd"
Expected Output: {'a': 2, 'b': 1, 'c': 2, 'd': 3}
'''
s = input("input: ")
freq = {}
i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    freq[s[i]] = count
    i += 1
print(freq)

'''
Rotate a String by k Positions
Shift characters to the right by k positions
Sample Input: String="hello", k=2
Expected Output: "lohel"
'''
s = input("input string: ")
k = int(input("input k: "))
k %= len(s)
rotated = s[-k:] + s[:-k]
print(rotated)

'''
Minimum Rotations to Get the Original String
Count rotations needed to return to original string
Sample Input: "abcde"
Expected Output: 5
'''
s = input("input: ")
rot = s
count = 0
while True:
    rot = rot[-1] + rot[:-1]
    count += 1
    if rot == s:
        break
print(count)

'''
Count Frequency of Words in String (Short Form)
Sample Input: "apple apple orange"
Expected Output: {'apple': 2, 'orange': 1}
'''
s = input("input: ")
freq = {}
for w in s.split():
    freq[w] = freq.get(w, 0) + 1
print(freq)
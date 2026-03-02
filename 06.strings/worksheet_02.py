'''
Convert Snake Case to Pascal Case
Sample Input: "my_variable_name"
Expected Output: "MyVariableName"
'''
s = input("input snake_case string: ")
pascal = ''.join(word.capitalize() for word in s.split('_'))
print(pascal)

'''
Find the Position of a Character in the k-th Word
Sample Input: List=["hello","world"], k=2, char="r"
Expected Output: Position: 2
'''
lst = input("input list separated by space: ").split()
k = int(input("input k-th word: "))
char = input("input character: ")
word = lst[k-1]
pos = word.find(char)
print("Position:", pos)

'''
Mirror Image of a String
Reverse the string
Sample Input: "abcd"
Expected Output: "dcba"
'''
s = input("input: ")
print(s[::-1])

'''
Replace Multiple Words at Once
Sample Input: String="I like apples and bananas.", Replace={"apples":"oranges","bananas":"grapes"}
Expected Output: "I like oranges and grapes."
'''
s = input("input string: ")
repl = eval(input("input replacement dictionary: "))
for old, new in repl.items():
    s = s.replace(old, new)
print(s)

'''
Remove Punctuation from a String
Sample Input: "Hello, world! How are you?"
Expected Output: "Hello world How are you"
'''
import string
s = input("input: ")
clean = ''.join(c for c in s if c.isalnum() or c.isspace())
print(clean)

'''
Check if Two Strings are Rotationally Equivalent
Sample Input: "abcde", "cdeab"
Expected Output: Rotationally equivalent: Yes
'''
s1 = input("input string 1: ")
s2 = input("input string 2: ")
is_rot = "Yes" if len(s1)==len(s2) and s2 in s1*2 else "No"
print("Rotationally equivalent:", is_rot)

'''
Generate a Random Binary String
Sample Input: Length=8
'''
import random
n = int(input("input length: "))
rand_bin = ''.join(random.choice('01') for _ in range(n))
print(rand_bin)

'''
Reverse Sort a String
Sample Input: "python"
'''
s = input("input: ")
sorted_s = ''.join(sorted(s, reverse=True))
print(sorted_s)

'''
Validate a Password String
Conditions: length >= 8, contains letters, digits, and special chars
Sample Input: "MyPass123@"
'''
import re
pwd = input("input password: ")
valid = len(pwd)>=8 and bool(re.search(r'[A-Za-z]', pwd)) \
        and bool(re.search(r'\d', pwd)) and bool(re.search(r'[^A-Za-z0-9]', pwd))
print("Valid password:", "Yes" if valid else "No")

'''
Pad a String with Characters
Sample Input: "cat", Length=6, Pad char="*"
'''
s = input("input string: ")
length = int(input("desired length: "))
pad = input("pad character: ")
padded = s.rjust(length, pad)
print(padded)

'''
Print Superscript and Subscript in String Output
Sample Input: "E = mc2" (2 as superscript)
'''
s = input("input string: ")
s = s.replace("2", "²")
print(s)

'''
Check for Pangram
Sample Input: "The quick brown fox jumps over the lazy dog"
'''
import string
s = input("input: ").lower()
is_pangram = all(c in s for c in string.ascii_lowercase)
print("Is pangram:", "Yes" if is_pangram else "No")

'''
Sort List of Dates Given as Strings
Sample Input: ["2021-05-21", "2019-01-12", "2020-12-15"]
'''
dates = input("input dates separated by space: ").split()
dates.sort()
print(dates)

'''
Split String into Groups of n Characters
Sample Input: "abcdefgh", n=3
'''
s = input("input string: ")
n = int(input("input n: "))
groups = [s[i:i+n] for i in range(0, len(s), n)]
print(groups)

'''
Extract Indices of Substring Matches
Sample Input: String="abracadabra", Substring="abra"
'''
s = input("input string: ")
sub = input("input substring: ")
indices = [i for i in range(len(s)-len(sub)+1) if s[i:i+len(sub)]==sub]
print(indices)

'''
Remove After a Substring
Sample Input: String="abcdeFGhiJK", Substring="FG"
'''
s = input("input string: ")
sub = input("input substring: ")
idx = s.find(sub)
if idx != -1:
    s = s[:idx+len(sub)]
print(s)

'''
Remove Redundant Substrings from a List
Sample Input: ["hellohello","world","testtesttest"]
'''
lst = input("input list separated by space: ").split()
cleaned = [''.join(lst[i][:len(lst[i])//(len(lst[i])//len(set(lst[i])))]) if lst[i]*2 in lst[i]*2 else lst[i] for i in range(len(lst))]
print(cleaned)

'''
Filter Strings with a Combination of k Substrings
Sample Input: List=["applebanana","apple","banana","applebananacherry"], Substrings=["apple","banana"]
'''
lst = input("input list separated by space: ").split()
subs = input("input substrings separated by space: ").split()
filtered = [s for s in lst if all(sub in s for sub in subs)]
print(filtered)
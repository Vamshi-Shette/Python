"""
• Task:
Write a script that reads a text file and counts the occurrence of each word.

• Validation:
Verify that the output dictionary correctly represents word counts for given test files.
"""

# Program: Count occurrence of each word in a text file

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        word_count = {}  # dictionary to store word frequencies

        for line in file:
            words = line.strip().split()

            for word in words:
                word = word.lower()  # convert to lowercase for accurate counting

                # remove simple punctuation
                word = word.strip(".,!?;:\"()[]{}")

                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        print("\nWord Count Dictionary:")
        print(word_count)

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

"""
Task:
Create a simple script that reads a log file, 
filters lines containing the word "ERROR",
and writes those lines into a new file.

Validation:
After running, open the output file and check that
it contains only the lines with "ERROR".
"""

# Ask user for file names
input_file = input("Enter the log file name: ")
output_file = input("Enter the new file name to store ERROR lines: ")

try:
    # Open input file for reading
    infile = open(input_file, "r")

    # Open output file for writing
    outfile = open(output_file, "w")

    # Read file line by line
    for line in infile:
        # Check if the word "ERROR" is present in the line
        if "ERROR" in line:
            outfile.write(line)   # Write only ERROR lines

    # Close both files
    infile.close()
    outfile.close()

    print("Filtering completed successfully.")
    print("Check the output file for ERROR lines only.")

except FileNotFoundError:
    print("File not found. Please check the file name.")

"""
Concepts: String methods, slicing, formatting, and parsing.

Task:
Develop a script that processes log entries by extracting
the timestamp, severity, and message from each line.

Validation:
Ensure that the parsed elements match expected values
for sample log entries.

2026-02-27 10:15:32 - ERROR - Database connection failed

Timestamp : 2026-02-27 10:15:32
Severity  : ERROR
Message   : Database connection failed
"""

# Sample log format:
# 2026-02-27 10:15:32 - ERROR - Database connection failed
# 2026-02-27 10:16:01 - INFO - User logged in

filename = input("Enter log file name: ")

try:
    file = open(filename, "r")

    for line in file:
        line = line.strip()  # remove newline

        # Split based on " - "
        parts = line.split(" - ")

        # Check if line has correct format
        if len(parts) == 3:
            timestamp = parts[0]
            severity = parts[1]
            message = parts[2]

            print("Timestamp :", timestamp)
            print("Severity  :", severity)
            print("Message   :", message)
            print("-" * 40)
        else:
            print("Invalid log format:", line)

    file.close()

except FileNotFoundError:
    print("File not found. Please check the file name.")        

"""
Task:
Refactor the earlier log parsing task into reusable functions and modules.

Validation:
Test the functions independently to ensure they work correctly
with predefined inputs.
"""

# -------------------------------
# Module-like Functions Section
# -------------------------------

def parse_log_line(line):
    """
    Takes one log line as input.
    Returns a dictionary with timestamp, severity, and message.
    Returns None if format is invalid.
    """
    line = line.strip()
    parts = line.split(" - ")

    if len(parts) == 3:
        return {
            "timestamp": parts[0],
            "severity": parts[1],
            "message": parts[2]
        }
    else:
        return None


def parse_log_file(filename):
    """
    Reads a log file and returns a list of parsed log dictionaries.
    """
    parsed_logs = []

    try:
        file = open(filename, "r")

        for line in file:
            result = parse_log_line(line)
            if result is not None:
                parsed_logs.append(result)

        file.close()

    except FileNotFoundError:
        print("File not found.")

    return parsed_logs


# -------------------------------
# Validation Section (Testing)
# -------------------------------

# Test 1: Independent function test
print("Testing parse_log_line function:")

sample_line = "2026-02-27 10:15:32 - ERROR - Database connection failed"
parsed = parse_log_line(sample_line)

print(parsed)
print()

# Test 2: Testing file parsing
filename = input("Enter log file name to test: ")
logs = parse_log_file(filename)

print("\nParsed Log Entries:")
for log in logs:
    print(log)

"""
Task:
Given a list of log lines, group them by severity 
(e.g., INFO, WARNING, ERROR) using a dictionary.

Validation:
Verify that the dictionary keys and counts correctly reflect 
the distribution of log entries.
"""

# Sample list of log lines
log_lines = [
    "2026-02-27 10:15:32 - ERROR - Database connection failed",
    "2026-02-27 10:16:01 - INFO - User logged in",
    "2026-02-27 10:17:45 - WARNING - Disk space low",
    "2026-02-27 10:18:20 - ERROR - Timeout occurred",
    "2026-02-27 10:19:10 - INFO - File uploaded"
]

# Dictionary to store grouped logs
severity_dict = {}

# Loop through each log line
for line in log_lines:
    parts = line.split(" - ")
    
    if len(parts) == 3:
        severity = parts[1]
        
        # If severity not already in dictionary, add it
        if severity not in severity_dict:
            severity_dict[severity] = []
        
        # Append log line to respective severity list
        severity_dict[severity].append(line)

# Display grouped logs
print("Grouped Logs by Severity:\n")

for key in severity_dict:
    print(key, ":", len(severity_dict[key]), "entries")
    for log in severity_dict[key]:
        print("  ", log)
    print()

# Validation Output Example:
# ERROR : 2 entries
# WARNING : 1 entries
# INFO : 2 entries


"""
Task:
Write a script that filters out and transforms a list of log entries 
using list comprehensions (for instance, extracting only error messages).

Validation:
Confirm that the resultant list contains only the expected entries.
"""

# Sample list of log entries
log_entries = [
    "2026-02-27 10:15:32 - ERROR - Database connection failed",
    "2026-02-27 10:16:01 - INFO - User logged in",
    "2026-02-27 10:17:45 - WARNING - Disk space low",
    "2026-02-27 10:18:20 - ERROR - Timeout occurred",
    "2026-02-27 10:19:10 - INFO - File uploaded"
]

# Using list comprehension to filter only ERROR messages
error_messages = [
    line.split(" - ")[2]          # Extract only the message part
    for line in log_entries
    if " - ERROR - " in line      # Filter condition
]

# Display result
print("Extracted ERROR Messages:")
for msg in error_messages:
    print(msg)

"""
Validation:

Expected Output:
Database connection failed
Timeout occurred

✔ Only ERROR messages are extracted.
✔ INFO and WARNING entries are excluded.
"""
'''
7. Data Structures: Lists, Dictionaries, and Sets
• Concepts: Efficient use of lists, dictionaries, tuples, and sets to store and manipulate data.
• Task:
• Given a list of log lines, group them by severity (e.g., INFO, WARNING, ERROR)
using a dictionary.
• Validation: Verify that the dictionary keys and counts correctly reflect the
distribution of log entries. 
'''

import os,sys
filename=input("Enter file name:")
if not os.path.exists(filename):
    print("File not exist:")
    sys.exit()
count={}
with open(filename,'r') as fp:
    for line in fp:
        if 'ERROR' in line:
            count['ERROR']=count.get('ERROR',0)+1
        elif 'INFO' in line:
            count['INFO']=count.get('INFO',0)+1
        elif 'WARN' in line:
            count['WARN']=count.get('WARN',0)+1
for key,value in count.items():
    print(f"{key}:{value}")

'''
8. List and Dictionary Comprehensions
• Concepts: Using comprehensions for concise and efficient data transformations.
• Task:
• Write a script that filters out and transforms a list of log entries using list
comprehensions (for instance, extracting only error messages).
• Validation: Confirm that the resultant list contains only the expected entries.
'''

import os,sys
filename=input("Enter file name:")
msg=input("enter msg to filter lines:")

if not os.path.exists(filename):
    print("File not exist:")
    sys.exit()
with open(filename,'r') as file:
    lines=file.readlines()
    filtered=[l for l in lines if msg in l]
    for l in filtered:
        print(l)

#................................................................
"""
Task 1: Word Count Script
Covers: Basic syntax, data types, and file I/O

Description:
Read a text file, count the frequency of each word, 
and output the results as a dictionary.
"""

filename = input("Enter the file name: ")

try:
    file = open(filename, "r")
    word_count = {}

    for line in file:
        words = line.strip().split()

        for word in words:
            word = word.lower().strip(".,!?;:\"()[]{}")

            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    file.close()

    print("Word Frequency Dictionary:")
    print(word_count)

except FileNotFoundError:
    print("File not found. Please check the file name.")

"""
Task 2: Log Filter
Covers: File I/O and exception handling

Description:
Process a log file to extract lines containing "ERROR" 
and write them to a new file, handling missing files gracefully.
"""

input_file = input("Enter log file name: ")
output_file = input("Enter output file name: ")

try:
    infile = open(input_file, "r")
    outfile = open(output_file, "w")

    for line in infile:
        if "ERROR" in line:
            outfile.write(line)

    infile.close()
    outfile.close()

    print("ERROR lines successfully written to output file.")

except FileNotFoundError:
    print("Log file not found. Please check the file name.")

"""
Task 3: Log Parser
Covers: String manipulation and regular expressions

Description:
Extract and format key details (timestamp, severity, message) 
from each log entry.
"""

import re

filename = input("Enter log file name: ")

# Example log format:
# 2026-02-27 10:15:32 - ERROR - Database connection failed

pattern = r"^(.*?) - (.*?) - (.*)$"

try:
    file = open(filename, "r")

    for line in file:
        line = line.strip()
        match = re.match(pattern, line)

        if match:
            timestamp = match.group(1)
            severity = match.group(2)
            message = match.group(3)

            print("Timestamp :", timestamp)
            print("Severity  :", severity)
            print("Message   :", message)
            print("-" * 40)

    file.close()

except FileNotFoundError:
    print("Log file not found. Please check the file name.")
    
            
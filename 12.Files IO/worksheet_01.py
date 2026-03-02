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
    
"""
Task 4: Modular Code Development
Covers: Functions, modular programming, and data structures
Description: Refactor the log parser into reusable functions, and group log entries by severity using dictionaries.
"""

# ----------------------------
# Function 1: Parse a single log line
# ----------------------------
def parse_log_line(line):
    """
    Parses a log line into a dictionary.
    Expected format:
    2026-02-27 10:15:32 - ERROR - Database connection failed
    """
    try:
        parts = line.strip().split(" - ")
        if len(parts) != 3:
            return None  # Skip malformed lines
        
        return {
            "timestamp": parts[0],
            "severity": parts[1],
            "message": parts[2]
        }
    except Exception:
        return None


# ----------------------------
# Function 2: Read and parse file
# ----------------------------
def read_log_file(filename):
    logs = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print("File not found.")
    return logs


# ----------------------------
# Function 3: Group by severity
# ----------------------------
def group_by_severity(logs):
    severity_count = {}
    
    for log in logs:
        level = log["severity"]
        severity_count[level] = severity_count.get(level, 0) + 1
    
    return severity_count


# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    filename = "sample_log.txt"   # Replace with your log file
    
    logs = read_log_file(filename)
    result = group_by_severity(logs)
    
    print("Log Count by Severity:")
    print(result)

"""
Task 5: Command-Line Tool
Covers: Command-line argument parsing and list comprehensions
Description: Create a script that accepts file names and search terms from the command line,
processes logs, and outputs filtered results.
"""

import sys

def filter_logs(filename, keyword):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        
        # Using list comprehension to filter
        filtered = [line.strip() for line in lines if keyword in line]
        
        return filtered
    
    except FileNotFoundError:
        print("File not found.")
        return []


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <search_term>")
    else:
        filename = sys.argv[1]
        keyword = sys.argv[2]
        
        results = filter_logs(filename, keyword)
        
        print("\nFiltered Results:")
        for line in results:
            print(line)

"""
Task 7: CSV Data Analyzer

Concepts:
- File I/O
- Lists and Dictionaries
- List Comprehensions
- Basic Data Analysis

Description:
Develop a script that reads a CSV file containing columns such as 
"TestCase," "Status," and "ExecutionTime."
The script should produce a summary report showing counts for each 
status (e.g., Passed, Failed) and compute the average execution time.

Validation:
Use a sample CSV file and compare the output summary with expected statistics.
"""

import csv

def analyze_csv(file_name):
    status_count = {}
    execution_times = []

    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                status = row["Status"]
                time = float(row["ExecutionTime"])

                # Count status
                if status in status_count:
                    status_count[status] += 1
                else:
                    status_count[status] = 1

                execution_times.append(time)

        # Calculate average execution time
        if execution_times:
            avg_time = sum(execution_times) / len(execution_times)
        else:
            avg_time = 0

        print("Status Summary:")
        print(status_count)
        print("Average Execution Time:", round(avg_time, 2))

    except FileNotFoundError:
        print("File not found. Please check the file name.")

# Example usage
file_name = input("Enter CSV file name: ")
analyze_csv(file_name)
            

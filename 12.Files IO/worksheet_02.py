"""
Log Level Counter

Write a script that reads the provided log file and counts the number of occurrences 
of each log level (INFO, DEBUG, WARNING, ERROR) using file I/O and dictionaries. 
Avoid using regular expressions for this task.

Challenge:
Ensure your code gracefully handles lines that do not follow the expected format.
"""

filename = input("Enter log file name: ")

log_counts = {
    "INFO": 0,
    "DEBUG": 0,
    "WARNING": 0,
    "ERROR": 0
}

try:
    file = open(filename, "r")

    for line in file:
        parts = line.strip().split(" - ")

        if len(parts) >= 3:
            level = parts[1]
            if level in log_counts:
                log_counts[level] += 1

    file.close()

    print("Log Level Counts:")
    print(log_counts)

except FileNotFoundError:
    print("File not found.")

"""
Error Log Extractor

Using basic string manipulation (without regex), write a script that filters 
and prints all log entries containing the word “ERROR”.

Challenge:
Verify that only well-formed error lines are extracted while ignoring 
misformatted lines.
"""

filename = input("Enter log file name: ")

try:
    file = open(filename, "r")

    print("Well-formed ERROR logs:")

    for line in file:
        parts = line.strip().split(" - ")

        if len(parts) >= 3 and parts[1] == "ERROR":
            print(line.strip())

    file.close()

except FileNotFoundError:
    print("File not found.")


"""
Log Parser to Dictionary

Develop a function that reads each line of the log file and parses it into 
a dictionary with keys:
timestamp, log_level, module (if available), and message.

Return a list of such dictionaries.

Challenge:
Handle lines that deviate from the standard format by either skipping 
them or recording an error message.
"""

def parse_log_file(filename):
    parsed_logs = []

    try:
        file = open(filename, "r")

        for line in file:
            parts = line.strip().split(" - ")

            if len(parts) >= 4:
                log_dict = {
                    "timestamp": parts[0],
                    "log_level": parts[1],
                    "module": parts[2],
                    "message": parts[3]
                }
                parsed_logs.append(log_dict)
            else:
                # Skip misformatted lines
                continue

        file.close()

    except FileNotFoundError:
        print("File not found.")

    return parsed_logs


# Example usage
filename = input("Enter log file name for parsing: ")
logs = parse_log_file(filename)

print("Parsed Logs:")
for log in logs:
    print(log)


"""
Group Logs by Module

Using the output from Question 3, write a function that groups log entries 
by their module.

For each module, output the count of log entries.

Challenge:
Use dictionary comprehensions or iterative methods to build the grouped result.
"""

def group_by_module(logs):
    module_counts = {}

    for log in logs:
        module = log["module"]

        if module in module_counts:
            module_counts[module] += 1
        else:
            module_counts[module] = 1

    return module_counts


# Example usage
grouped = group_by_module(logs)

print("Logs Grouped by Module:")
print(grouped)


"""
Format Validator with Exception Handling

Create a script that reads the log file and identifies lines that do not 
match the expected log format.

For each misformatted line, log a warning with its line number while 
continuing to process the rest of the file.

Challenge:
Ensure that your solution uses try-except blocks to catch and handle 
exceptions without crashing.
"""

filename = input("Enter log file name for validation: ")

try:
    file = open(filename, "r")

    line_number = 0

    for line in file:
        line_number += 1

        try:
            parts = line.strip().split(" - ")

            if len(parts) < 4:
                raise ValueError("Invalid format")

        except Exception as e:
            print(f"Warning: Misformatted line at {line_number}")

    file.close()

except FileNotFoundError:
    print("File not found.")

'''
JSON Log Converter
Write a script that converts the log file into a JSON file. Each log entry should be a JSON
object containing the keys: timestamp, log_level, module, and message.
Challenge: Ensure that the JSON output correctly represents all valid log entries while
ignoring or flagging misformatted lines.

'''


import json

def parse_log_file(input_file):
    logs=[]
    errors=[]

    with open(input_file,"r") as f:
        for line_no,line in enumerate(f,1):
            line=line.strip()
            parts=line.split()

            if len(parts)<4:
                errors.append(f"Line {line_no}: Invalid format")
                continue

            timestamp=parts[0]+" "+parts[1]
            log_level=parts[2]

            if len(parts)>=5:
                module=parts[3]
                message=" ".join(parts[4:])
            else:
                module=None
                message=" ".join(parts[3:])

            log_entry={
                "timestamp":timestamp,
                "log_level":log_level,
                "module":module,
                "message":message
            }

            logs.append(log_entry)

    return logs,errors


def convert_to_json(input_file,output_file):
    logs,errors=parse_log_file(input_file)

    with open(output_file,"w") as f:
        json.dump(logs,f,indent=4)

    print("JSON file created:",output_file)

    if errors:
        print("Some lines were skipped:")
        for e in errors:
            print(e)


if __name__=="__main__":
    convert_to_json("log.txt","output.json")
    
'''
Command-Line Log Filter

Task:
Develop a command-line tool using Python’s argparse module that accepts two
arguments: a log level (e.g., "ERROR") and a module name. The script should
filter the log file to print only those entries matching both criteria.

Challenge:
Validate the command-line inputs and provide helpful error messages for
invalid or missing arguments.

Example usage in terminal:
python log_filter.py server_logs.log ERROR auth
'''

import argparse

# Create argument parser
parser = argparse.ArgumentParser(description="Filter log entries by log level and module name")

# Add command line arguments
parser.add_argument("filename", help="Log file name")
parser.add_argument("level", help="Log level (INFO, DEBUG, WARNING, ERROR)")
parser.add_argument("module", help="Module name")

args = parser.parse_args()

# Valid log levels
valid_levels = ["INFO", "DEBUG", "WARNING", "ERROR"]

# Validate log level
if args.level.upper() not in valid_levels:
    print("Invalid log level. Please use INFO, DEBUG, WARNING, or ERROR")
    exit()

try:
    with open(args.filename, "r") as file:
        for line in file:
            parts = line.strip().split(" - ")

            # Check if line has expected format
            if len(parts) < 4:
                continue

            timestamp = parts[0]
            log_level = parts[1]
            module = parts[2]
            message = parts[3]

            # Filter by level and module
            if log_level == args.level.upper() and module == args.module:
                print(line.strip())

except FileNotFoundError:
    print("Error: Log file not found. Please check the file name.")

'''
Regular Expression Challenge (IP Address Extractor)

Task:
Write a Python function that uses a regular expression to extract all unique IPv4 addresses
from a log file. Some log messages include IP addresses (for example:
"Ping to server 192.168.1.100 succeeded").

The function should return a list of unique IP addresses found in the file.

Challenge:
Ensure the regex correctly matches valid IPv4 formats and avoids invalid patterns.

Example Log Line:
2026-03-10 10:15:32 - INFO - network - Ping to server 192.168.1.100 succeeded
'''

import re

filename = input("Enter log file name: ")

# Regular expression for valid IPv4 addresses
pattern = r'\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b'

unique_ips = set()

try:
    with open(filename, "r") as file:
        for line in file:
            matches = re.findall(pattern, line)

            for match in matches:
                # match[0] contains the full IP portion except last number
                # so we search again for full IP in the line
                full_ips = re.findall(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', line)

                for ip in full_ips:
                    parts = ip.split('.')
                    if all(0 <= int(p) <= 255 for p in parts):
                        unique_ips.add(ip)

    print("Unique IPv4 addresses found:")
    print(list(unique_ips))

except FileNotFoundError:
    print("Error: File not found.")
    
        

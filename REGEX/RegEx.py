# For this assignment you are welcomed to use other regex resources such a regex "cheat sheets" you find on the web.

# PART A -- Find a list of all of all the names in the following string using regex.

    # Loading libraries

import re 

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. Ruth and Peter, their parents, have 3 kids."""
    list_names = re.findall("[A-Z][a-z]*"), simple_string)
    return list_names
    
# PART B -- The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class. Create a regex to generate a list of just those students who received a B in the course.

def grades():
    with open ("/home/aspphem/Desktop/Data Science/Files/TXT/grades.txt", "r") as file:
        grades = file.read()
    
    list_students = re.findall("([A-Z][\w]+ [A-Z][\w]+): B", grades)
    return list_students
    
# PART C -- Consider the standard web log file in assets/logdata.txt. This file records the access a user makes when visiting a web page (like this one). Each line of the log has the following items: 

    # a host (e.g., '146.204.224.152').
    # a user_name (e.g., 'feest6811' note: sometimes the user name is missing. In this case, use '-' as the value for the username).
    # the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700').
    # the post request type (e.g., 'POST/incentivize HTTP/1.1' note: NOT everything is a POST).
    
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
    
    # example_dict = {"host": 146.204.224.152, "user_name": "feest6811", "time": "21/Jun/2019:15:45:24 -0700", "request": "POST /incentivize HTTP/1.1"}
    
regex = re.compile(
    r'(?P<host>(?:\d+\.){1,3}\d+)\s+-\s'
    r'(?P<user_name>[\w+\-]+)?\s+'
    r'\[(?<time>[-\w\s:/]+)\]\s+'
    r'"(?P<request>\w+.+?)"'
)

def logs():
    data = []
    with open("/home/aspphem/Desktop/Data Science/Files/TXT/logdata.txt") as f:
        logdata = f.read()
        for item in regex.finditer(logdata):
            x = item.groupdict()
            if x["username"] is None:
                x["username"] = "-"
            data.append(x)
    return data

logs()

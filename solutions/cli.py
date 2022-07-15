""" This module implements a command-line interface which opens, appends an item to,
and saves a document.

Usage: 
    python cli.py [filepath] [dict string to append]

Example:
    python cli.py ./capitals.json "{‘state’: ‘Texas’, ‘capital’: ‘Austin’}"

Hints:
    sys.argv provides a list of command line arguments
    ast.literval_eval() converts strings into dictionaries
"""
import sys, ast

import FileChooser as FileChooser

# get the path from the command line args
path = sys.argv[1]

# get the dict string from the command line args and cast it as a dict using the ast library
item = ast.literal_eval(sys.argv[2])

# open, append, and save the Document
document = FileChooser.open(path)
document.append(item)
print(document)
document.save()
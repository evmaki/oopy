""" This module implements a singleton called FileChooser.

FileChooser takes a string path to a file and returns the appropriate
Document subclass depending on the file type.
"""
from Document import *

def open(path: str) -> Document:
    ls = path.split('.')
    ext = ls[len(ls) - 1]

    if ext == 'csv':
        return CsvDocument(path)
    elif ext == 'json':
        return JsonDocument(path)
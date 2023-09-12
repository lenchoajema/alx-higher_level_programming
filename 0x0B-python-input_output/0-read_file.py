#!/usr/bin/python3
""" Trying to write a function to read a file"""


def read_file(filename=""):
    """ 
Exception: when the file can be opened
"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')

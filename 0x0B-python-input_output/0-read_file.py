#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """Reads a text file with UTF-8 encoding and prints it to stdout

    Args:
        filename: (str) The name of a file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")

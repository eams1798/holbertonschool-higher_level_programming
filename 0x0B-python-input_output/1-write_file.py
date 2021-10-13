#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file with UTF-8 encoding

    Args:
        filename: (str) The name of a file
        text: (str) The text to be written to the file

    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

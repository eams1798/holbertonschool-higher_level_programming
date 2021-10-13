#!/usr/bin/python3
"""2.Append to a file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename: (str) The name of a file
        text: (str) A text to append to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

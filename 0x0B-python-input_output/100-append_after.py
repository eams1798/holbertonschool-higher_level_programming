#!/usr/bin/python3
"""13. Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
    specific string

    Args:
        filename: the name of a file
        search_string: a string to search in the file
        new_string: a string tobe added in the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in text:
            if search_string in line:
                line = line + new_string
            f.write(line)

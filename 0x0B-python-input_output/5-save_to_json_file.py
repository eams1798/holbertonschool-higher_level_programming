#!/usr/bin/python3
"""5. Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: A object to save in the file
        filename: The name of a file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

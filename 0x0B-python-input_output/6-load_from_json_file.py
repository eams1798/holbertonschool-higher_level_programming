#!/usr/bin/python3
"""6. Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename: The name of a file

    Returns:
        a JSON Object
    """
    with open(filename, 'r') as f:
        obj = f.read()
        return json.loads(obj)

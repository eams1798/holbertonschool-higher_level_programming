#!/usr/bin/python3
"""3. To JSON string"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj: An object to convert in a JSON representation

    Returns:
        A string
    """
    ld = json.dumps(my_obj)
    return ld

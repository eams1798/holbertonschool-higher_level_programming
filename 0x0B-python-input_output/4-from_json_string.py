#!/usr/bin/python3
"""4. From JSON string to Object"""


import json


def from_json_string(my_obj):
    """Returns an object (Python data structure) represented by a JSON string

    Args:
        my_obj: A string of an object

    Returns:
        A JSON object"""
    ld = json.loads(my_obj)
    return ld

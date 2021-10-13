#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object

    Args:
        obj: An abject

    Returns:
        A dictionary
    """
    return obj.__dict__

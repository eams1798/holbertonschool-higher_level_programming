#!/usr/bin/python3
"""2. Say my name"""


def say_my_name(first_name, last_name=""):
    """Prints the full name of a person
    Args:
        first_name: str
        last_name: str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""0. Integers addition"""


def add_integer(a, b=98):
    """adds two integers

    Args:
        a: must be of type int or raises an exception
        b: must be of type int or raises an exception

    Returns:
        The sum of a and b
    """
    if not(type(a) in (int, float)):
        raise TypeError("a must be an integer")
    elif not(type(b) in (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

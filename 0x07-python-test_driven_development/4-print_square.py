#!/usr/bin/python3
"""3. Print square"""


def print_square(size):
    """Prints a square with the prompt `#`
    Args:
        size: int
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()

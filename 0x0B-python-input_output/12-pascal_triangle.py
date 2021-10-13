#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
    triangle of ´n´

    Args:
        n: The size of the Pascal's Triangle

    Returns:
        A list of lists of integers"""
    t = []
    if n <= 0:
        return t

    for i in range(n):
        t.append([])
        t[i].append(1)
        for j in range(1, i):
            t[i].append(t[i - 1][j - 1] + t[i - 1][j])
        if (i != 0):
            t[i].append(1)
    return t

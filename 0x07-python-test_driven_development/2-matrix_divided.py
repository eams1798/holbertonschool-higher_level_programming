#!/usr/bin/python3
"""1. Divide a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix: an array of arrays of ints or floats
        div: The divisor
    """
    l = -1
    te = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(te)
    div_m = []
    for m in range(len(matrix)):
        if type(matrix[m]) is not list:
            raise TypeError(te)
        if l != -1 and l != len(matrix[m]):
            raise TypeError("Each row of the matrix must have the same size")
        l = len(matrix[m])
        div_m.append([])
        for i in range(len(matrix[m])):
            if type(matrix[m][i]) not in (int, float):
                raise TypeError(te)
            if type(div) not in (int, float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            div_m[m].append(round(matrix[m][i] / div, 2))
    return div_m

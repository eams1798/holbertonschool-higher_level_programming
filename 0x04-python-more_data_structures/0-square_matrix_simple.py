#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m2 = matrix.copy()
    for i in range(len(m2)):
        m2[i] = list(map(lambda n: n ** 2, m2[i]))
    return m2

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for i in range(len(m)):
            if i < len(m) - 1:
                print("{:d} ".format(m[i]), end="")
            else:
                print("{:d}".format(m[i]), end="")
        print()

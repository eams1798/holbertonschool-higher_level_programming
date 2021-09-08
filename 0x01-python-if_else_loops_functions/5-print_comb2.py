#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i * 10 + j) != 99:
            print("{:d}{:d}".format(i, j), end=(", "))
        else:
            print("{:d}{:d}".format(i, j))

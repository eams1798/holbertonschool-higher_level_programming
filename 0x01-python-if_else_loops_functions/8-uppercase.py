#!/usr/bin/python3
def uppercase(chain):
    for c in chain:
        if ord(c) in range(97, 123):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{}".format(char), end="")
    print()

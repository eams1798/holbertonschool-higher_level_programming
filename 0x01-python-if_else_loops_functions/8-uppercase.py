#!/usr/bin/python3
def uppercase(chain):
    for i in range(len(chain)):
        if ord(chain[i]) in range(97, 123):
            char = chr(ord(chain[i]) - 32)
        else:
            char = chain[i]
        if i < len(chain) - 1:
            print("{}".format(char), end="")
        else:
            print("{}".format(char))

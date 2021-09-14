#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    lrev = my_list.copy()
    lrev.reverse()
    for i in lrev:
        print("{:d}".format(i))
    lrev.clear()

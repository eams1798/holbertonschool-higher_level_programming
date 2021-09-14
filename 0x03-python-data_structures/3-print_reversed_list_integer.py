#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lrev = my_list.copy()
    lrev.reverse()
    for i in lrev:
        print(i)
    lrev.clear()

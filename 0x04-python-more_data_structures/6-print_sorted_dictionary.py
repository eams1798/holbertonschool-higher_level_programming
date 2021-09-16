#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    asort = list(a_dictionary.keys())
    asort.sort()
    for s in asort:
        print(s + ": " + str(a_dictionary.get(s)))
    asort.clear()

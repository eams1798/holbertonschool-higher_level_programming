#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = None
    for k in a_dictionary:
        if a_dictionary[k] == value:
            key = a_dictionary[k]
            break
    if not(key is None):
        a_dictionary.pop(k)
        complex_delete(a_dictionary, value)
    return a_dictionary

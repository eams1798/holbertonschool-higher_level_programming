#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) <= idx:
        return None
    else:
        lst = my_list.copy()
        lst[idx] = element
        return lst

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list == None:
        return None
    lst = my_list.copy()
    if idx >= 0 and len(my_list) > idx:
        lst[idx] = element
    return lst

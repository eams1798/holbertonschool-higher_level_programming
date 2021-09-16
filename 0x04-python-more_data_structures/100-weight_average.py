#!/usr/bin/python3
def weight_average(my_list=[]):
    add = 0
    weight = 0
    if len(my_list) == 0:
        return add
    for tup in my_list:
        add += tup[0] * tup[1]
        weight += tup[1]
    add /= weight
    return add

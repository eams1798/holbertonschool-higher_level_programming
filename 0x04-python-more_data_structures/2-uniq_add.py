#!/usr/bin/python3
def uniq_add(my_list=[]):
    lcmp = []
    add = 0
    for i in my_list:
        if not(i in lcmp):
            add += i
        lcmp.append(i)
    lcmp.clear()
    return add

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lstbool = []
    for i in my_list:
        if i % 2 == 0:
            lstbool.append(True)
        else:
            lstbool.append(False)
    return lstbool

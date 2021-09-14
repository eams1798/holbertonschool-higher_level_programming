#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_t0 = 0
    add_t1 = 0
    for i in range(2):
        if len(tuple_a) <= i:
            add_a = 0
        else:
            add_a = tuple_a[i]
        if len(tuple_b) <= i:
            add_b = 0
        else:
            add_b = tuple_b[i]
        if i == 0:
            add_t0 += add_a + add_b
        else:
            add_t1 += add_a + add_b
    tuple_c = (add_t0, add_t1)
    return tuple_c

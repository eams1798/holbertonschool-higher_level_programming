#!/usr/bin/python3
def remove_char_at(string, n):
    if n >= 0:
        c = string[0:n] + string[n+1:]
    else:
        c = string
    return c

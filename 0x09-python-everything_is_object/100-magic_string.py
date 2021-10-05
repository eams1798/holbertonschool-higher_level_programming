#!/usr/bin/python3
def magic_string(i):
    a = "BestSchool"
    return a + (", " + a) * (i - 1)

for i in range(10):
    print(magic_string(i))

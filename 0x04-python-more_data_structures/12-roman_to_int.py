#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if type(roman_string) != str or roman_string is None:
        return num
    if len(roman_string) == 1:
        return rom.get(roman_string[0])
    for r in range(len(roman_string) - 1):
        if rom.get(roman_string[r]) < rom.get(roman_string[r + 1]):
            num += rom.get(roman_string[r]) * -1
        else:
            num += rom.get(roman_string[r])
        if r == len(roman_string) - 2:
            num += rom.get(roman_string[r + 1])
    return num

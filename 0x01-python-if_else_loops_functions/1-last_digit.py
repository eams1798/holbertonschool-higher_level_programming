#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
s1 = "Last digit of and is"
if last == 0:
    cmpr = " 0"
elif last > 5:
    cmpr = " greater than 5"
else:
    cmpr = " less than 6 and not 0"
print(s1[:14] + str(number) + " is " + str(last) + s1[-7:] + cmpr)

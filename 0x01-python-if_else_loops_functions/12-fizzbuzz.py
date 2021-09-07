#!/usr/bin/python3
def fizzbuzz():
    c1 = "Fizz"
    c2 = "Buzz"
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            char = (c1 if i % 3 == 0 else "") + (c2 if i % 5 == 0 else "")
        else:
            char = str(i)
        print("{}".format(char), end=" ")

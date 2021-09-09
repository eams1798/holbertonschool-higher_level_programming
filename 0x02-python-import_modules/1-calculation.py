#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    func = [add, sub, mul, div]
    op = ["+", "-", "*", "/"]

    for f in range(0, 4):
        print("{:d} {:s} {:d} = {:d}".format(a, op[f], b, func[f](a, b)))

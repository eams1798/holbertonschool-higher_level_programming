#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) - 1 < 1):
        print("0 arguments.")
    elif (len(sys.argv) - 1 > 1):
        print("{:d} arguments:".format(len(sys.argv) - 1))
    else:
        print("{:d} argument:".format(len(sys.argv) - 1))
    if (len(sys.argv) - 1 != 0):
        for i in range(len(sys.argv) - 1):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))

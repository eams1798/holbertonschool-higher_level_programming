#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError:
        sys.stderr.write("Exception: " + str(sys.exc_info()[1]) + "\n")
        return False
    except TypeError:
        sys.stderr.write("Exception: " + str(sys.exc_info()[1]) + "\n")
        return False
    return True

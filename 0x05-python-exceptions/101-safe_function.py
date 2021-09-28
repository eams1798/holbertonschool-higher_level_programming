#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except:
        sys.stderr.write("Exception: " + str(sys.exc_info()[1]) + "\n")
        return None
    return res

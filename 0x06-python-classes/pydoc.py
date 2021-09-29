#!/usr/bin/python3
import sys
pyfile = __import__("{}".format(sys.argv[1]))

try:
    print("module: " + pyfile.__doc__)
except:
    print("module: None")
try:
    print("evaluate_size: " + pyfile.evaluate_size.__doc__)
except:
    print("evaluate_size: None")
try:
    print("evaluate_position: " + pyfile.evaluate_position.__doc__)
except:
    print("evaluate_position: None")
try:
    print("Square: " + pyfile.Square.__doc__)
except:
    print("Square: None")
try:
    print("Square.positive_int_required: " + pyfile.Square.positive_int_required.__doc__)
except:
    print("Square.positive_int_required: None")
try:
    print("Square.required: " + pyfile.Square.required.__doc__)
except:
    print("Square.required: None")
try:
    print("Square.__init__: " + pyfile.Square.__init__.__doc__)
except:
    print("Square.__init__: None")
try:
    print("Square.size: " + pyfile.Square.size.__doc__)
except:
    print("Square.size: None")
try:
    print("Square.position: " + pyfile.Square.position.__doc__)
except:
    print("Square.position: None")
try:
    print("Square.area: " + pyfile.Square.area.__doc__)
except:
    print("Square.area: None")
try:
    print("Square.my_print: " + pyfile.Square.my_print.__doc__)
except:
    print("Square.my_print: None")

#!/usr/bin/python3
"""7. A script that adds all arguments to a Python list, and then save
them to a file"""


import sys
import os.path

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

if os.path.isfile(filename):
    lst = load_from(filename)
else:
    lst = []

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        lst.append(sys.argv[i])

save_to(lst, filename)

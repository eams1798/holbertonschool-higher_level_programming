#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys

r = requests.get(sys.argv[1])
if r.status_code >= 400:
    print("Error code: {}".format(r.status_code))
else:
    print(r.text)

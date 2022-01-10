#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))

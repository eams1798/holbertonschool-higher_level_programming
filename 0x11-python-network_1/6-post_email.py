#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys


datadct = {'email': sys.argv[2]}
r = requests.post(sys.argv[1], data=datadct)
print(r.text)

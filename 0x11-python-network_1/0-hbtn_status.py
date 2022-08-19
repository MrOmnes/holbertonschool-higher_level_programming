#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response:")
    print("\t- type:", type(response.read()))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode('utf8'))

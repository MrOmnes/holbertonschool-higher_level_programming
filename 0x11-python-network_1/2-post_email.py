#!/usr/bin/python3
"""Better Documentation"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    params = {'email': sys.argv[2]}
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))

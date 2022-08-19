#!/usr/bin/python3
"""Better Documentation"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
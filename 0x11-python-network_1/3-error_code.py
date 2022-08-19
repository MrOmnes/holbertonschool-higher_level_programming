#!/usr/bin/python3
"""Better Documentation"""
from urllib.error import HTTPError
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print("Error code:", err.code)

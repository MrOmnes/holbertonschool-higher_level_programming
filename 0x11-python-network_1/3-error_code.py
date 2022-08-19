#!/usr/bin/python3
"""Better Documentation"""
from urllib.error import HTTPError
import urllib.request
import sys


"""Try by adding random comment here"""

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))

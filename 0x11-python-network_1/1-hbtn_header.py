#!/usr/bin/python3
"""Get header response"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        info = response.getheader('X-Request-Id')
        print(info)

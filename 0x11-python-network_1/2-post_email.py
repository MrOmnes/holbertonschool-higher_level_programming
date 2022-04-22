#!/usr/bin/python3
"""Get header response"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
params = {"email": sys.argv[2]}


if __name__ == "__main__":
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string
    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        print(response_text)

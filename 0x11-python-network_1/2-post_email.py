#!/usr/bin/python3
"""Get header response"""

from urllib import request, parse
import sys

if __name__ == "__main__":
	data = parse.urlencode({"email":"test"}).encode()
	req = request.Request(sys.argv[1], data=data)
	resp = request.urlopen(req)
	print(req)

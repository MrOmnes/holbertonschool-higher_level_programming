#!/usr/bin/python3
"""Get body response"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        info = response.read()
        utf = info.decode(response.headers.get_content_charset())

print("Body response:")
print("\t- type:", type(info))
print("\t- content:", info)
print("\t- utf8 content:", utf)

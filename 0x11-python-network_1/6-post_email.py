#!/usr/bin/python3
"""Better Documentation"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}
    response = requests.post(url, mail)
    print(response.text)
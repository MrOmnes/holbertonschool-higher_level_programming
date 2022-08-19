#!/usr/bin/python3
"""Better Documentation"""
import requests
import sys
if __name__ == "__main__":
    mail = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], mail)
    print(response.text)

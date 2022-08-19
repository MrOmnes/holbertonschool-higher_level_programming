#!/usr/bin/python3
"""Better Documentation"""
import requests
import sys
response = requests.get(sys.argv[1])
print(response.headers['X-Request-Id'])

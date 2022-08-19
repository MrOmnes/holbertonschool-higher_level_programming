#!/usr/bin/python3
import requests
import sys
url = sys.argv[1]
mail = {'email': sys.argv[2]}
response = requests.post(url, mail)
print(response.text)

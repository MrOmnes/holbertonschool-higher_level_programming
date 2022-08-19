#!/usr/bin/python3                                                                                
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 2:
        mail = {'q': sys.argv[1]}
    else:
        mail = {'q': ""}
    response = requests.post(url, params=mail)
    print(response.content)
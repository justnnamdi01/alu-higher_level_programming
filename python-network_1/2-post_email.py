#!/usr/bin/python3
'''Script that takes in URL and email,
- sends a POST request to the URL and
- displays the body of the response'''


import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':

    url = sys.argv[1]
    mssg = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(mssg).encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

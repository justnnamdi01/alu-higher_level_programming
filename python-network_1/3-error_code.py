#!/usr/bin/python3
'''Script that takes in a URL, sends it a request and
- displays the body of the response'''


import sys
import urllib.request
import urllib.error

if __name__ == '__main__':

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            print("{}".format(data.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print(e.reason)

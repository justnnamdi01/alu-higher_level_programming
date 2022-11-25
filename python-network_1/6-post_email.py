#!/usr/bin/python3
'''Script that takes in URL and email,
- sends a POST request to the URL and
- displays the body of the response'''


import sys
import requests


if __name__ == "__main__":
    """send the email"""
    url = sys.argv[1]
    email = sys.argv[2]
    context = {
        "email": email
    }
    response = requests.post(url, data=context)
    print("{}".format(response.text))

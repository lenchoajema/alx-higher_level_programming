#!/usr/bin/python3
"""
given URL as parameter, fetch URL and display value from reponse headerder.py  https://alx-intranet.hbtn.io  nnnn 
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
        req = urllib.request.Request(argv[1])
            with urllib.request.urlopen(req) as response:
                        print(response.getheader('X-Request-Id'))

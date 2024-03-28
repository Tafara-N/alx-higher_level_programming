#!/usr/bin/env python3

"""
Script sends an HTTP Request to a URL and prinyt out the response
"""

import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    the_text = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(the_text)))
    print('\t- content: {}'.format(the_text))

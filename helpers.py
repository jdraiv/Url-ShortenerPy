
import string
import random

import urllib.request as req
import urllib.parse as p

from random import randint

def valid_url(url):
    request = req.Request(url)
    try:
        response = req.urlopen(request)
        return True
    except:
        return False


def valid_https(url):
    https = url[0:8]
    if https == 'http://' or https == 'https://':
        return valid_url(url)
    else:
        new_url = 'https://' + url
        return valid_url(new_url)


def url_key():
    letters = list(string.ascii_lowercase)
    key = ""
    
    key_length = randint(2,5)
    for char in range(0, key_length):
        if char % 2 == 0:
            n = randint(0,9)
            key += str(n)
        else:
            key += random.choice(letters)
    return key


        


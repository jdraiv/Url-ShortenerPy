
import requests
import string
import random
from random import randint


def valid_url(url):
    https = url[0:8]

    if https == 'http://' or https == 'https://':
        valid = requests.get(url)

        if valid.status_code == 200:
            return True
        else:
            return False

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

        


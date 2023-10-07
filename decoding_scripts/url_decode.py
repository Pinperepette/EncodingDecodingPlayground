#!/usr/bin/env python

import urllib.parse

def decode(encoded_text):
    decoded_text = urllib.parse.unquote(encoded_text)
    return decoded_text

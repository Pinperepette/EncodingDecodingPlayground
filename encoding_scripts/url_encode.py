#!/usr/bin/env python

import urllib.parse

def encode(text):
    encoded_text = urllib.parse.quote(text)
    return encoded_text

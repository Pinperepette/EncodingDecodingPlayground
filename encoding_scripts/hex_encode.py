#!/usr/bin/env python

def encode(text):
    encoded_text = text.encode('utf-8').hex()
    return encoded_text

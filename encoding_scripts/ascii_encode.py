#!/usr/bin/env python

def encode(text):
    encoded_text = ''.join(str(ord(char)) for char in text)
    return encoded_text

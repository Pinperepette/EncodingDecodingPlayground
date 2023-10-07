#!/usr/bin/env python

def decode(text):
    decoded_text = ''.join(chr(int(text[i:i+3])) for i in range(0, len(text), 3))
    return decoded_text
